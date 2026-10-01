---
name: snapshot-debug
description: Analyze Business Central snapshot debug and .alcpuprofile artifacts
agent: agent
tools: ["read", "search"]
---

Analyze without editing using the runtime-artifact reference in `al-debugging-methodology`. Return the relevant execution path, evidence, uncertainty, and next check. For isolated analysis of a large artifact, select `al-snapshot-debugger` separately.

Snapshot or profile investigation:
${input:task:Describe the symptom and attach or reference the snapshot/profile artifact}