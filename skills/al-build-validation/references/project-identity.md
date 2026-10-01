# Project Identity and Diagnostics

- Identify the primary manifest and any dependent validation manifests. Keep unrelated roots out of scope.
- Prefer a manifest-targeted build in multi-root workspaces. If an active-project tool is used, verify the project identity in its output; focusing an editor is not proof of the build target.
- If the tool built another project, discard that result and select the intended manifest explicitly before diagnosing code.
- Associate errors and warning baselines with their originating project. Record the exact manifest and available success/error/warning fields.
- A successful build after the final source changes is authoritative for compilation of that manifest. A contradictory editor-only missing-object diagnostic such as AL0185 can be reported as stale; it is not a reason to move objects or change permission references.
- This exception does not cover errors in the authoritative build, another manifest, or edits made after that build. Rebuild the affected project after subsequent source changes.
- Git tracking does not determine AL source inclusion. Do not stage files to make the compiler discover them; inspect actual project configuration and build evidence.
- If target selection cannot be established, report validation as blocked, including intended and actual targets. Do not make speculative source fixes.