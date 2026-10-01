---
name: al-debugging-methodology
description: 'Use for unclear AL runtime defects, event/trigger failures, regressions, snapshot traces, or .alcpuprofile analysis.'
user-invocable: false
---

# Debugging Methodology

Use this skill when an AL issue is not obvious from first inspection and a fix requires disciplined diagnosis.

Anchor diagnosis to the failing action, error, or trace and the smallest check that distinguishes the leading explanation. A simple defect does not need a ranked hypothesis report.

## Common AL debugging checks

- `Validate` versus assignment, and whether record operations execute triggers
- subscriber signature, publisher conditions, `IsHandled` interaction, and unintended session state
- filters, current key, partial-record loading, FlowField calculation, and company context
- user permissions versus indirect object permissions; foreground versus job-queue/session identity
- installed app/dependency version versus inspected symbols and source

For snapshot exports and CPU profiles, read [runtime artifacts](./references/runtime-artifacts.md). For a wrong build target or contradictory editor diagnostics, use [build validation](../al-build-validation/SKILL.md).

## Good outputs

- probable root cause stated explicitly
- remaining hypotheses only when uncertainty matters
- evidence that confirmed or disproved the main hypothesis
- minimal fix scope
- residual uncertainty if runtime confirmation was limited
