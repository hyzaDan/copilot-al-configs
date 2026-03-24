---
name: al-bc-solution-review
description: Reviews AL or BC solutions for correctness, maintainability, standards compliance, and testability.
argument-hint: "changed files or feature description"
---

# BC Solution Review

Use this skill during review-oriented tasks.

## Review checklist

- Is the chosen extension pattern upgrade-safe?
- Does object responsibility stay clear?
- Are validation rules explicit and complete?
- Are page extensions resilient to base app changes?
- Are permission and data-classification choices appropriate?
- Is testability preserved through clear dependency boundaries?
- Are there missing edge cases or regression risks?
- Are there performance-sensitive patterns that should trigger the `al-performance-review` skill?
- Are there security or permission concerns that should trigger the `al-security-review` skill?

## Output expectations

- findings first
- severity ordering
- concrete fixes where possible
- note residual risk if verification was incomplete

## Related skills

- `al-coding-standards` for canonical naming, affix, and AL structure expectations
- `al-performance-review` for deeper performance-focused review passes
- `al-security-review` for permission, data-protection, and classification review passes
