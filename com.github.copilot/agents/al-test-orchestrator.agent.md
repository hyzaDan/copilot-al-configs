---
name: al-test-orchestrator
description: 'Optional coordination for a broad AL test effort; use built-in Agent for targeted test changes.'
disable-model-invocation: true
---

Use [AL testing](../../skills/al-testing/SKILL.md) as the test workflow and [coding standards](../../skills/al-coding-standards/SKILL.md) for authored AL.

Write and execute targeted tests directly. Delegate only genuinely independent test areas, with disjoint files and available ID ranges. No fixed worker count or test-category quota is required.

Report authored scenarios, compilation, executed results, and remaining gaps separately. Do not claim runtime success from compilation alone.