"""Compile the two dependency-free method examples using an installed Microsoft AL CLI.

Creates a disposable app outside the repository. Does not publish or run anything in BC.
Other examples require consuming-app symbols and are deliberately outside this probe.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, help="New evidence directory; default is a temporary folder")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
compiler = shutil.which("al")
if not compiler:
    raise SystemExit("Missing Microsoft AL CLI executable 'al'; no compilation performed.")
out = args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix="al-skill-compile-"))
if args.output:
    out.mkdir(parents=True, exist_ok=False)
inputs = ["skills/bc-isolated-storage-generator/references/storage-patterns.md", "skills/bc-telemetry-generator/references/producer-and-kql.md"]
fragments, evidence = [], []
for name in inputs:
    raw = (root / name).read_bytes()
    matches = re.findall(r"```al\n(.*?)```", raw.decode("utf-8").replace("\r\n", "\n"), re.S)
    if len(matches) != 1:
        raise SystemExit(f"Expected one AL method-fragment block in {name}; inspect the changed example first.")
    fragments.append(matches[0])
    evidence.append({"path": name, "sha256": hashlib.sha256(raw).hexdigest()})
manifest = {"id": "a6f8470f-fb2d-4821-a719-144d7b431d63", "name": "Skill Snippet Probe", "publisher": "Local Validation", "version": "1.0.0.0", "runtime": "15.0", "target": "Cloud", "idRanges": [{"from": 50100, "to": 50100}]}
(out / "app.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode())
(out / "Probe.Codeunit.al").write_bytes(('codeunit 50100 "Skill Snippet Probe"\n{\n' + "\n".join(fragments) + "\n}\n").encode())
result = subprocess.run([compiler, "compile", "--", f"/project:{out}", f"/out:{out / 'probe.app'}", f"/errorlog:{out / 'diagnostics.json'}"], capture_output=True, text=True, encoding="utf-8", errors="replace")
(out / "compiler-output.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
passed = result.returncode == 0 and (out / "probe.app").is_file()
(out / "evidence.json").write_bytes((json.dumps({"inputs": evidence, "runtime": manifest["runtime"], "target": manifest["target"], "exitCode": result.returncode, "packageProduced": (out / "probe.app").is_file(), "passed": passed, "scope": "Compilation only: storage and telemetry method fragments. No BC runtime."}, indent=2) + "\n").encode())
print(result.stdout + result.stderr)
print(f"{'PASS' if passed else 'FAIL'}: two portable examples; evidence at {out}")
sys.exit(0 if passed else 1)
