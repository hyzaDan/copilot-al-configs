---
name: develop
description: Implement AL code from an approved plan
tools: ["read", "search", "edit"]
---

Use this prompt as the VS Code launcher for the installed `al-develop-orchestrator` agent from this plugin.

Keep this wrapper thin. The canonical development workflow now lives in the orchestrator agent definition, not in this prompt body.

Execution intent:
- adopt the `al-develop-orchestrator` workflow contract
- use `al-developer` reasoning for focused code changes
- preserve the approved plan unless a material deviation must be surfaced
- hand off review-ready changes with verification status and residual risk

If the environment cannot hand off automatically to the named agent, follow the same orchestration contract manually and keep the output aligned with the `al-develop-orchestrator` agent definition.

Plan or task:
${input:task:Paste the approved plan or describe the implementation task}
