"""Fault-injection tests for the package validator; changes disposable copies only."""
from pathlib import Path
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate-skills.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class PackageValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="al-skill-validator-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ["skills", "docs", "scripts", "third-party", "com.github.copilot", ".codex-plugin", ".github/plugin", ".claude-plugin", ".agents/plugins"]:
            shutil.copytree(ROOT / folder, self.root / folder)
        for name in ["README.md", "THIRD-PARTY-NOTICES.md", "plugin.json", "mcp.json", ".mcp.json", "hooks.json", ".gitattributes"]:
            shutil.copy2(ROOT / name, self.root / name)

    def mutate_json(self, name, action):
        path = self.root / name
        data = json.loads(path.read_text(encoding="utf-8"))
        action(data)
        path.write_text(json.dumps(data), encoding="utf-8")

    def detects(self, message):
        errors, _ = validator.validate(self.root)
        self.assertTrue(any(message in e for e in errors), errors)

    def test_valid_package(self):
        errors, _ = validator.validate(self.root)
        self.assertEqual(errors, [])

    def test_altered_skill(self):
        path = self.root / "skills/al-testing/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nChanged content\n", encoding="utf-8")
        self.detects("Maintained hash mismatch")

    def test_missing_skill(self):
        (self.root / "skills/al-testing/SKILL.md").unlink()
        self.detects("Active skill inventory mismatch")

    def test_hidden_discovery_path(self):
        path = self.root / "retired/SKILL.md"
        path.parent.mkdir()
        path.write_text("Retired entrypoint", encoding="utf-8")
        self.detects("Unexpected discovery entrypoint")

    def test_broken_link(self):
        path = self.root / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Broken](missing-file.md)\n", encoding="utf-8")
        self.detects("Broken local link")

    def test_duplicate_yaml(self):
        path = self.root / "skills/al-testing/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("name: al-testing", "name: al-testing\nname: duplicate"), encoding="utf-8")
        self.detects("Duplicate YAML key")

    def test_missing_disposition(self):
        self.mutate_json("third-party/al-copilot-skills-collection.json", lambda d: d["dispositions"].pop())
        self.detects("Incomplete or duplicate source dispositions")

    def test_version_drift(self):
        self.mutate_json(".codex-plugin/plugin.json", lambda d: d.update(version="0.0.0"))
        self.detects("Manifest version mismatch")

    def test_license_change(self):
        (self.root / "third-party/AL-Copilot-Skills-Collection.LICENSE").write_text("Replaced", encoding="utf-8")
        self.detects("License hash mismatch")

    def test_routing_drift(self):
        self.mutate_json(".codex-plugin/plugin.json", lambda d: d.update(skills="./retired/"))
        self.detects("Unexpected discovery root")

    def test_mcp_drift(self):
        self.mutate_json(".mcp.json", lambda d: d["mcpServers"].pop("alcops"))
        self.detects("MCP manifests differ")

    def test_unrecorded_file(self):
        (self.root / "skills/al-testing/old-template.md").write_text("Stale", encoding="utf-8")
        self.detects("Maintained file inventory mismatch")

    def test_https_is_not_machine_path(self):
        path = self.root / "skills/al-testing/SKILL.md"
        path.write_bytes(path.read_bytes() + b"\nhttps://learn.microsoft.com/example\n")
        errors, _ = validator.validate(self.root)
        self.assertFalse(any("Machine path" in e for e in errors), errors)

    def test_machine_paths_detected(self):
        path = self.root / "skills/al-testing/SKILL.md"
        original = path.read_bytes()
        for example in [b"C:/customer/project", b"C:\\customer\\project"]:
            path.write_bytes(original + b"\n" + example + b"\n")
            self.detects("Machine path")

    def test_crlf_rejected(self):
        path = self.root / "skills/al-testing/SKILL.md"
        path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.detects("Maintained content must use LF")

    def test_authorship_change(self):
        (self.root / "third-party/AL-Copilot-Skills-Collection.AUTHORS.md").write_text("Replaced", encoding="utf-8")
        self.detects("Source authorship hash mismatch")

    def test_checkout_policy(self):
        (self.root / ".gitattributes").write_text("", encoding="utf-8")
        self.detects("Missing stable checkout byte policy")


if __name__ == "__main__":
    unittest.main()
