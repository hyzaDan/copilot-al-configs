---
name: TDD And Test Rules
description: TDD discipline and AL test quality rules
applyTo: "**/*{Test,Tests}*.al"
---

- Follow RED, GREEN, REFACTOR discipline explicitly.
- Do not implement production logic before the failing test has been validated.
- Keep tests deterministic and isolated.
- Prefer scenario names that describe behavior, not implementation details.
- Call out missing edge cases and missing negative tests during review.
