---
name: al-project-context-bootstrap
description: 'Use when onboarding to an unfamiliar AL app or explicitly preparing reusable project context for a feature stream.'
argument-hint: "project root or module"
---

# Project Context Bootstrap

Use this skill at the start of a new feature stream or in an unfamiliar codebase.

Not a prerequisite for ordinary edits. Start with the affected module and capture only facts needed for the task; do not map every workspace root. Record source paths and app/version identity so later sessions can revalidate stale context.

## Capture

- object ID ranges
- naming conventions
- folder structure
- core extension patterns
- known integration points
- testing conventions

## Output

Produce a concise working context that future planning and implementation can reuse.

## Rules

- summarize only high-value facts
- avoid dumping large code excerpts
- prefer facts that change design or implementation decisions
