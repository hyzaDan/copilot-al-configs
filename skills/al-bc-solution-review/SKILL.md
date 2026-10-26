---
name: al-bc-solution-review
description: 'Use when reviewing AL changes or a BC solution design for defects, regressions, or missing tests.'
---

# BC Solution Review

Use this skill during review-oriented tasks.

## Review checklist

- Is the chosen extension pattern upgrade-safe?
- Does object responsibility stay clear?
- Are validation rules explicit and complete?
- Do record operations preserve required triggers, transaction boundaries, and company context?
- Are page extensions resilient to base app changes?
- Are permission and data-classification choices appropriate?
- Is testability preserved through clear dependency boundaries?
- Are there missing edge cases or regression risks?
- Are there performance-sensitive patterns that should trigger the `al-performance-review` skill?
- Are there security or permission concerns that should trigger the `al-security-review` skill?

## Output expectations

- findings first
- cite file/symbol evidence and explain the failure scenario; distinguish project conventions from platform requirements
- severity ordering
- concrete fixes where possible
- note residual risk if verification was incomplete
- No quota of findings: correct code may have none. A finding needs a reachable failure, relevant requirement, or measured cost; put unverified assumptions and optional style suggestions outside defects.
- Do not demand `SingleInstance`, inherent permissions, full architecture documents, or a new test suite merely because this is AL. Use [record-access semantics](../al-debugging-methodology/references/record-access.md) when partial loading, FlowFields, or trigger behavior are disputed.

## Related skills

- [Coding standards](../al-coding-standards/SKILL.md) when assessing naming or AL structure
- [Performance](../al-performance-review/SKILL.md) only for meaningful data-access or runtime-cost risk
- [Security](../al-security-review/SKILL.md) only for permission, sensitive-data, or access-control risk
