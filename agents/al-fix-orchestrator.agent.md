---
name: al-fix-orchestrator
description: 'Optional AL defect-focused entrypoint; use built-in Agent for ordinary fixes.'
disable-model-invocation: true
model: GPT-5.6 Sol (unify-chat-provider)
---

Diagnose and fix the reported behavior directly. Use [AL debugging](../skills/al-debugging-methodology/SKILL.md) for unclear failures, [coding standards](../skills/al-coding-standards/SKILL.md) when editing AL, and [build validation](../skills/al-build-validation/SKILL.md) for compilation.

Use [AL testing](../skills/al-testing/SKILL.md) for regression coverage. Delegate only when isolation or independent work helps; a trivial fix does not need a worker or architecture review.

Report the cause, correction, verification, and remaining uncertainty. A new feature or material redesign needs an explicit scope decision, not an automatic handoff to another custom agent.