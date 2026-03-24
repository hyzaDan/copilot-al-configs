---
name: snapshot-debug
description: Analyze Business Central snapshot debug and .alcpuprofile artifacts
tools: ["read", "search"]
---

Use this prompt as the VS Code launcher for the installed `al-snapshot-debugger` agent from this plugin.

Keep this wrapper thin. The canonical snapshot analysis workflow lives in the worker agent definition, not in this prompt body.

Execution intent:
- adopt the `al-snapshot-debugger` analysis contract
- reconstruct the runtime path from the attached snapshot or `.alcpuprofile` artifact
- rank the most likely failure points, subscriber chains, or performance hotspots
- end with the smallest useful next step and the right handoff target

If the environment cannot hand off automatically to the named agent, follow the same analysis contract manually and keep the output aligned with the `al-snapshot-debugger` agent definition.

Snapshot or profile investigation:
${input:task:Describe the symptom and attach or reference the snapshot/profile artifact}