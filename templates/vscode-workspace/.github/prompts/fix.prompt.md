---
name: fix
description: Run a lightweight AL bug-fix workflow with minimal safe scope
tools: ["read", "search", "edit"]
---

Use this prompt as the VS Code launcher for the installed `fix-orchestrator` agent from this plugin.

Keep this wrapper thin. The canonical bug-fix workflow now lives in the orchestrator agent definition, not in this prompt body.

Execution intent:
- adopt the `fix-orchestrator` workflow contract
- classify the issue before editing
- implement the smallest safe correction that fits the defect
- report root cause, verification status, and remaining risk

If the environment cannot hand off automatically to the named agent, follow the same orchestration contract manually and keep the output aligned with the `fix-orchestrator` agent definition.

Issue:
${input:task:Describe the bug, error, or regression}
