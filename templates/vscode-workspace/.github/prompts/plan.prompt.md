---
name: plan
description: Create an AL solution plan with trade-offs and BC integration notes
tools: ["read", "search"]
---

Use this prompt as the VS Code launcher for the installed `al-plan-orchestrator` agent from this plugin.

Keep this wrapper thin. The canonical planning workflow now lives in the orchestrator agent definition, not in this prompt body.

Execution intent:
- adopt the `al-plan-orchestrator` workflow contract
- use `al-solution-architect` reasoning for design depth
- produce one implementation-ready plan
- end with a clear approval gate for moving into development

If the environment cannot hand off automatically to the named agent, follow the same orchestration contract manually and keep the output aligned with the `al-plan-orchestrator` agent definition.

Task:
${input:task:Describe the feature or change}
