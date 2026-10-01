---
name: al-develop-orchestrator
description: 'Optional coordination for explicitly requested parallel AL implementation; use built-in Agent for ordinary development.'
disable-model-invocation: true
---

Implement the bounded request or existing plan. This compatibility entrypoint is optional; a separate planning session is not required for a clear task.

Use [coding standards](../skills/al-coding-standards/SKILL.md) for AL changes and [build validation](../skills/al-build-validation/SKILL.md) for compilation. Load [testing](../skills/al-testing/SKILL.md), [architecture](../skills/al-solution-architecture/SKILL.md), or [translation](../skills/al-translation-phase/SKILL.md) only when that work is in scope.

Work directly unless independent modules justify delegation. XLF synchronization and `en-US` to `cs-CZ` translation are the exception: after the build, delegate them to `al-translator` with generated XLF evidence and a Czech scope. Do not invoke XLF translation tools in this parent context. When delegating, give each worker a target manifest, file ownership, ID constraints, and a bounded result. Do not prescribe worker counts or require reviewer sign-off for every change. An isolated `al-reviewer` pass is useful for consequential changes or when requested.

Complete implementation and relevant validation within the authorized scope. Surface material product/scope decisions; report changed behavior, validation evidence, and unresolved risk.