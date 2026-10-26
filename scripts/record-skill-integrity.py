"""Refresh maintained hashes after reviewed edits; never alter upstream/baseline evidence."""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--write", action="store_true", help="Record reviewed working-tree bytes")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
path = root / "third-party/al-copilot-skills-collection.json"
lock = json.loads(path.read_text(encoding="utf-8"))
actual = sorted(p.parent.name for p in (root / "skills").glob("*/SKILL.md"))
if actual != sorted(lock["activeSkills"]):
    raise SystemExit("Skill inventory changed: review activeSkills and all source dispositions first.")
files = []
for p in sorted((root / "skills").rglob("*")):
    if p.is_file():
        if b"\r\n" in p.read_bytes():
            raise SystemExit(f"Normalize maintained text to LF before recording hashes: {p}")
        skill = p.relative_to(root / "skills").parts[0]
        if skill not in actual:
            raise SystemExit(f"Unexpected retired content: {p}")
        files.append({"path": p.relative_to(root).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "sourceSkills": [d["sourceSkill"] for d in lock["dispositions"] if skill in d["destinations"]]})
if not args.write:
    raise SystemExit(f"Preview: {len(files)} files. Pass --write after reviewing content changes.")
lock["maintainedFiles"] = files
path.write_bytes((json.dumps(lock, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
print(f"Recorded {len(files)} maintained hashes; original evidence unchanged.")
