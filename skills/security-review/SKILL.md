---
name: security-review
description: Reviews AL changes for permission design, data classification, sensitive data handling, and access-control risks.
user-invocable: false
---

# Security Review

Use this skill when AL changes affect permissions, sensitive data, posting actions, integrations, or fields whose data classification matters.

## Review focus

- least-privilege permission design
- permission set naming and AL-format permission set usage
- missing or weak `DataClassification`
- fields left as `ToBeClassified`
- sensitive data handling and auditability
- direct data access patterns that bypass expected security boundaries
- UI exposure that may reveal data without matching access control

## Review questions

- Does the change grant only the permissions needed?
- Are read, edit, and execute capabilities separated appropriately?
- Is the chosen data classification accurate for the field content?
- Does the implementation touch sensitive data without a clear security or audit rationale?
- Are codeunits or integration points performing actions that need stronger permission scrutiny?

## Output expectations

- findings first
- clear risk statements
- concrete remediation steps
- note compliance or runtime validation gaps when they cannot be fully checked in the current environment
