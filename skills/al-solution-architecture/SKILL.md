---
name: al-solution-architecture
description: 'Use for AL data-model design, BC extension-point selection, or architectural trade-offs in a feature plan or refactor.'
---

# AL Solution Architecture

## Purpose

Provide Business Central / AL-specific architectural guidance to the active planning workflow. This skill supplements the planner; it does **not** orchestrate planning, spawn agents, manage approval gates, control task tracking, or prescribe the general planning process.

## Principles

- Prefer BC-native, extend-don't-modify patterns, official extension points, maintainability, and upgrade safety.
- Follow relevant existing project patterns unless there is a clear reason not to.
- Separate data structure, business logic, UI, and integration responsibilities.
- Keep architecture proportional to the task; avoid unnecessary abstraction.
- Treat translation as a later implementation phase.

## Design boundaries

Resolve consequential uncertainty about data ownership/lifecycle, cardinality, posting behavior, permissions, or integration contracts before committing to the design. Use nearby source and project constraints; ask only for decisions that cannot be inferred safely. Routine implementation details do not require approval.

For unknown dependency APIs, use [symbol lookup](../al-symbol-lookup/SKILL.md). For uncertain platform behavior consult official Microsoft documentation. Do not prescribe a full repository map or load unrelated skills before a local design decision.

## AL architecture heuristics

- Prefer `tableextension` for simple 1:1 data that belongs to an existing entity lifecycle.
- Prefer a separate table for 1:N, lifecycle-independent, integration-heavy, or responsibility/performance-isolated data.
- Prefer event subscribers and official extension points over coupling to Base App implementation details.
- Keep reusable business logic out of pages.
- Keep responsibilities explicit across tables, pages, codeunits, reports, queries, and subscribers.
- Identify dependency boundaries and substitution points when they materially improve automated testability.

## Contribution to the plan

Make the design concrete enough that development should not require silent redesign. When relevant, identify:

- recommended approach and rationale
- objects/files to add or change and their responsibilities
- standard application integration points and events
- data lifecycle and validation/business rules
- permissions, integrations, and testability
- sequencing constraints, assumptions, risks, and accepted trade-offs

Recommend one primary design. Mention alternatives only when they clarify a meaningful BC-specific trade-off. In a planning-only task, use signatures or small skeletons rather than implementing production code; this skill does not prevent implementation when the user requested it.
