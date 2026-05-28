---
name: al-tdd-discipline
description: Applies RED, GREEN, REFACTOR discipline for implementation tasks that explicitly use TDD.
argument-hint: "feature or approved test specification"
---

# TDD Discipline

Use this skill when a task explicitly requires test-driven development.

## What this skill does

- keeps test creation and production implementation separated
- enforces RED, GREEN, REFACTOR thinking
- prevents vacuous tests that never failed first
- improves traceability of why code was added

## How to use it

1. Write or refine the failing test first.
2. Confirm what behavior is supposed to fail and why.
3. Implement only what is needed to make the intended behavior pass.
4. Refactor only after the behavior is passing.
5. Summarize what changed at each phase.

## Rules

- Do not present tests and implementation as one inseparable batch when strict TDD is required.
- Keep each test focused on one behavior.
- Do not implement production logic before the failing test has been validated.
- Keep tests deterministic and isolated.
- Call out when full RED or GREEN verification could not be executed in the environment.
- Prefer deterministic tests with explicit setup and assertions.
- Prefer scenario names that describe behavior, not implementation details.
- Call out missing edge cases and missing negative tests during review.
