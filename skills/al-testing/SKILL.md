---
name: al-testing
description: 'Use when creating AL test codeunits, selecting BC regression cases, or executing tests against a BC test environment.'
---

# AL Testing

Reuse the project's test app, library codeunits, handlers, and fixtures. Allocate IDs from its actual `app.json` ranges without collisions; do not impose ranges by test category.

Test changed behavior through the appropriate public procedure, trigger, or posting flow. Include the relevant rejection/boundary case, not a fixed matrix for every change. Consider company isolation, permissions, concurrency, and transaction rollback when behavior depends on them. Keep setup deterministic and isolate side effects.

Compile production and dependent test apps using [build validation](../al-build-validation/SKILL.md). Compilation, authored scenarios, and executed passing tests are separate claims.

Use the repository's configured runner against an identified, authorized test environment. Server configuration alone does not authorize publishing or mutating tests. If the runner is `bc-test`, read [runner notes](./references/bc-test.md).

Report scenarios added, tests actually executed, results, and blockers. An explicitly requested TDD task should demonstrate the intended failure before the implementation fix.