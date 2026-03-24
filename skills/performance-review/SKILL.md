---
name: performance-review
description: Reviews AL solutions for record loading, query shape, looping cost, scalability, and inefficient data-access patterns.
user-invocable: false
---

# Performance Review

Use this skill when a change touches large data volumes, loops over records, posting flows, background processing, or integration-heavy operations.

## Review focus

- broad record loading where narrower field or filter usage is possible
- queries inside loops and other N+1 patterns
- missing `SetLoadFields` on partial-record scenarios
- weak `FindSet` / `FindFirst` / `FindLast` choices
- repeated FlowField calculations or expensive work in loops
- unnecessary row-by-row updates where bulk operations are available
- design choices that should move heavy work to separate tables, summaries, or background processing

## Review questions

- Is the database doing the filtering, or is code filtering too late?
- Are only required fields being loaded?
- Is the iteration pattern appropriate for expected volume?
- Will the design stay acceptable at 10K, 100K, or larger record counts?
- Is there a simpler architectural split that reduces runtime cost?

## Output expectations

- findings first
- concrete AL-level improvement suggestions
- note expected impact when it is reasonably clear
- separate must-fix performance risks from optional optimization ideas
