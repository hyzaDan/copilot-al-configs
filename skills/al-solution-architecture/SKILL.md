---
name: al-solution-architecture
description: Use when planning, designing, or evaluating changes to Microsoft Dynamics 365 Business Central extensions written in AL. Applies to tasks involving AL code, .al files, Business Central features, refactoring, data model changes, AL object design, events and subscribers, integration points, validation, upgrade safety, performance, permissions, or automated tests.
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

## Ask design-impacting questions

Before committing to an architecture, actively identify unknowns that can materially change the solution design or Business Central behavior.

Ask the user targeted questions when an answer can affect areas such as:

- data ownership, lifecycle, cardinality, or source of truth
- existing entity extension versus a separate table
- business process, posting behavior, validation, or user interaction
- Base App / System App integration points and extension strategy
- permissions, external integrations, dependencies, or background processing
- performance, data volume, upgrade compatibility, or automated testability

Inspect the workspace first and do not ask what can already be determined from existing code and conventions. Ask about design-relevant ambiguity even when implementation could continue with an assumption if a different answer could lead to a different architecture or business behavior. Prefer specific, bounded questions whose design consequence is clear. Decide low-level implementation details yourself when safe. State reasonable assumptions explicitly. Do not carry important unresolved architecture questions silently into development.

## Analyze before designing

- Inspect relevant AL objects and similar existing functionality.
- Identify naming, object ID ranges, folders, permissions, and workspace constraints.
- Identify existing responsibilities, extension patterns, and relevant standard integration points.
- Prefer project context before broad external research.
- Prefer `al-symbols-mcp` for BC symbols and standard objects, `microsoft.docs.mcp` for official Microsoft behavior, and `context7` for third-party documentation when available.
- Verify uncertain integration points or make the uncertainty explicit.

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

Recommend one primary design. Mention alternatives only when they clarify a meaningful BC-specific trade-off. Do not emit full production AL code; small signatures or skeletons are acceptable only when they remove architectural ambiguity.
