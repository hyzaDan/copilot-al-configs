"""Read-only structure, routing and provenance checks; never executes AL or imported scripts."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
try:
    import yaml
except ImportError:
    raise SystemExit("Install dependencies: python -m pip install -r scripts/requirements-validation.txt")


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root, upstream=None):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    lock = json.loads((root / "third-party/al-copilot-skills-collection.json").read_text(encoding="utf-8"))
    check(lock.get("schemaVersion") == 2, "Expected provenance schema 2")
    active = lock["activeSkills"]
    actual = sorted(p.parent.name for p in (root / "skills").glob("*/SKILL.md"))
    check(sorted(active) == actual and len(active) == len(set(active)), "Active skill inventory mismatch")
    expected = {f"skills/{n}/SKILL.md" for n in active}
    discovered = {p.relative_to(root).as_posix() for p in root.rglob("SKILL.md") if ".git" not in p.relative_to(root).parts}
    check(discovered == expected, "Unexpected discovery entrypoint outside active inventory")
    for relative in sorted(expected):
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        if not match:
            errors.append(f"Missing frontmatter: {relative}")
            continue
        try:
            meta = yaml.load(match[1], Loader=UniqueLoader)
            if not isinstance(meta, dict):
                raise ValueError("Frontmatter is not a mapping")
            name, desc = meta.get("name"), meta.get("description")
            check(set(meta) <= {"name", "description", "license", "allowed-tools", "metadata"}, f"Nonportable skill frontmatter: {relative}")
            check(name == path.parent.name and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name))) and len(name) <= 64, f"Invalid name: {relative}")
            check(isinstance(desc, str) and 0 < len(desc.strip()) <= 1024, f"Invalid description: {relative}")
            check("model" not in meta, f"Unsupported skill model routing: {relative}")
        except (yaml.YAMLError, ValueError, TypeError) as exc:
            errors.append(f"Invalid YAML: {relative}: {exc}")

    ds, source = lock["dispositions"], lock["upstream"]
    upstream_names = {Path(f["path"]).parts[1] for f in source["files"]}
    original = set(lock["baseline"]["localSkills"]) | upstream_names
    check(len(original) == lock["baseline"]["skillCount"] == 50 and len(upstream_names) == source["skillCount"] == 39, "Baseline source inventory mismatch")
    check(len(ds) == len(original) and {d["sourceSkill"] for d in ds} == original, "Incomplete or duplicate source dispositions")
    for d in ds:
        check(d["origin"] == ("upstream" if d["sourceSkill"] in upstream_names else "local"), f"Wrong origin: {d['sourceSkill']}")
        check(d["action"] in {"retained", "merged", "removed"} and bool(d["reason"].strip()), f"Invalid disposition: {d['sourceSkill']}")
        check(all(n in active for n in d["destinations"]), f"Inactive destination: {d['sourceSkill']}")
        check(bool(d["destinations"]) == (d["action"] != "removed"), f"Destination/action mismatch: {d['sourceSkill']}")
        if d["action"] == "retained":
            check(d["destinations"] == [d["sourceSkill"]], f"Retained skill renamed without merge: {d['sourceSkill']}")
    check({n for d in ds for n in d["destinations"]} == set(active), "Active skill without disposition")
    actual_files = {p.relative_to(root).as_posix() for p in (root / "skills").rglob("*") if p.is_file()}
    files = lock["maintainedFiles"]
    check(len(files) == len(actual_files) and {f["path"] for f in files} == actual_files, "Maintained file inventory mismatch")
    for f in files:
        path = root / f["path"]
        check(path.is_file() and sha(path) == f["sha256"], f"Maintained hash mismatch: {f['path']}")
        if path.is_file():
            check(b"\r\n" not in path.read_bytes(), f"Maintained content must use LF: {f['path']}")
        parts = Path(f["path"]).parts
        check(len(parts) >= 3 and parts[0] == "skills" and parts[1] in active, f"File outside active skill: {f['path']}")
        origins = sorted(d["sourceSkill"] for d in ds if parts[1] in d["destinations"])
        check(sorted(f["sourceSkills"]) == origins, f"Incorrect maintained attribution: {f['path']}")
    for f in source["files"]:
        for key in ["upstreamSha256", "baselineImportedSha256"]:
            check(bool(re.fullmatch("[0-9a-f]{64}", f[key])), f"Invalid original hash: {f['path']}")
    check(sha(root / source["licenseFile"]) == source["licenseSha256"], "License hash mismatch")
    check(sha(root / source["authorsFile"]) == source["authorsSha256"], "Source authorship hash mismatch")
    attrs = (root / ".gitattributes").read_text(encoding="utf-8")
    check("/skills/** text eol=lf" in attrs and f"/{source['licenseFile']} -text" in attrs and f"/{source['authorsFile']} text eol=lf" in attrs, "Missing stable checkout byte policy")

    link_count = 0
    markdown = list((root / "skills").rglob("*.md")) + list((root / "com.github.copilot").rglob("*.md")) + list((root / "docs").rglob("*.md")) + [root / "README.md", root / "THIRD-PARTY-NOTICES.md"]
    for path in markdown:
        content = path.read_text(encoding="utf-8")
        prose = re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", content, flags=re.M | re.S)
        for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            target = raw.strip().strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            if target:
                link_count += 1
                check((path.parent / target).exists(), f"Broken local link: {path.relative_to(root)} -> {target}")
        if "skills" in path.relative_to(root).parts:
            check("upstream-skill-integration" not in content, f"Active wrapper dependency: {path}")
            check(not re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", content), f"Machine path in active skill: {path}")

    manifests = ["plugin.json", ".codex-plugin/plugin.json", ".github/plugin/plugin.json", ".github/plugin/marketplace.json", ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]
    def versions(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if k == "version":
                    yield v
                else:
                    yield from versions(v)
        elif isinstance(value, list):
            for v in value:
                yield from versions(v)
    for relative in manifests:
        data = json.loads((root / relative).read_text(encoding="utf-8"))
        found = list(versions(data))
        check(bool(found) and all(v == lock["packageVersion"] for v in found), f"Manifest version mismatch: {relative}")
        if "skills" in data:
            values = data["skills"] if isinstance(data["skills"], list) else [data["skills"]]
            check(all((root / v).resolve() == (root / "skills").resolve() for v in values), f"Unexpected discovery root: {relative}")
        if "agents" in data:
            check(data["agents"].strip("./") == "com.github.copilot/agents", f"Unexpected agents root: {relative}")
    portable = json.loads((root / "mcp.json").read_text(encoding="utf-8"))["mcpServers"]
    compat = json.loads((root / ".mcp.json").read_text(encoding="utf-8"))["mcpServers"]
    normalize = lambda obj: json.loads(json.dumps(obj).replace('"streamable-http"', '"http"'))
    check(normalize(portable) == normalize(compat), "MCP manifests differ beyond transport spelling")
    marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    check(marketplace["plugins"][0]["source"] == {"source": "local", "path": "./"}, "Unexpected Codex marketplace root")
    if upstream:
        specs = [f"{source['commit']}:{f['path']}" for f in source["files"]] + [f"{source['commit']}:LICENSE"]
        result = subprocess.run(["git", "-C", str(upstream), "cat-file", "--batch"], input=("\n".join(specs) + "\n").encode(), capture_output=True)
        check(result.returncode == 0, "Cannot read pinned upstream Git objects")
        payload = result.stdout
        for i, spec in enumerate(specs):
            header, sep, payload = payload.partition(b"\n"); bits = header.split()
            if not sep or len(bits) != 3 or bits[1] != b"blob":
                errors.append(f"Missing upstream blob: {spec}"); break
            size = int(bits[2]); blob, payload = payload[:size], payload[size + 1:]
            wanted = source["files"][i]["upstreamSha256"] if i < len(source["files"]) else source["licenseSha256"]
            check(hashlib.sha256(blob).hexdigest() == wanted, f"Upstream blob mismatch: {spec}")
    return errors, f"{len(active)} skills; {len(files)} maintained hashes; 50 dispositions; {link_count} local links; 6 versioned manifests"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--upstream", type=Path, help="Checkout with pinned upstream Git objects")
    args = parser.parse_args()
    try:
        errors, summary = validate(args.root.resolve(), args.upstream)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL: invalid package/manifest: {exc}"); return 1
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        return 1
    print(f"PASS: {summary}")
    if args.upstream:
        print("PASS: pinned raw upstream blobs and MIT license")
    print("LIMIT: static package checks; no host discovery, AL compilation or BC runtime implied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
