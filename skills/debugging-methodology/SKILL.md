---
name: debugging-methodology
description: Uses hypothesis-driven debugging for AL defects, runtime issues, event problems, and unclear regressions.
user-invocable: false
---

# Debugging Methodology

Use this skill when an AL issue is not obvious from first inspection and a fix requires disciplined diagnosis.

## Core method

1. Reproduce the issue or narrow the conditions where it occurs.
2. Collect evidence before editing: error text, failing step, object scope, recent change, runtime condition.
3. Form a short ranked hypothesis list rather than one untested guess.
4. Verify the leading hypothesis with the smallest reliable check available.
5. Apply the narrowest safe fix that matches the evidence.
6. Re-verify the original symptom and nearby regression risk.

## Common AL debugging checks

- event subscriber signature mismatch or subscriber not firing
- missing validation path or wrong trigger behavior
- permission or data-access failure hidden behind generic errors
- record filtering or loading mistakes
- wrong integration-point assumption
- environment-specific issue between extension-backed tooling and CLI fallback validation

## Good outputs

- probable root cause stated explicitly
- hypotheses ranked by confidence
- evidence that confirmed or disproved the main hypothesis
- minimal fix scope
- residual uncertainty if runtime confirmation was limited
