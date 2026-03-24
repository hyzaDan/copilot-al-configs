---
name: test
description: Create or review AL tests for a feature
tools: ["read", "search", "edit"]
---

Use this prompt as the VS Code launcher for the installed `al-test-orchestrator` agent from this plugin.

Keep this wrapper thin. The canonical testing workflow now lives in the orchestrator agent definition, not in this prompt body.

Execution intent:
- adopt the `al-test-orchestrator` workflow contract
- cover unit, integration, scenario, and edge-case needs as applicable
- keep tests deterministic and assertions meaningful
- report execution status, coverage summary, and remaining gaps

If the environment cannot hand off automatically to the named agent, follow the same orchestration contract manually and keep the output aligned with the `al-test-orchestrator` agent definition.

Feature or plan:
${input:task:Describe the feature, bug fix, or approved plan}
