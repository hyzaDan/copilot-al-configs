# Consequential BC design choices

Capture only relevant decisions and their source evidence:

- Data owner, cardinality, complete identity (company, document type/number, line where relevant), retention and source-of-truth boundaries.
- Lifecycle through draft, posting, archive, copy, reversal/correction and upgrade. State who writes each field and when; distinguish historical snapshots from current master data.
- Transaction boundaries, retry/idempotency, concurrency and external side effects. An external send and a BC database commit are not one atomic transaction.
- Verified extension points and supported versions. Mark unavailable event signatures as unresolved rather than generating invented APIs.
- Permissions, setup, localization, observability without customer data, and tests for the important failure path.

An ADR records the selected alternative, rationale and consequences, not a quota of patterns or diagrams. Include object/API inventory only when it serves a consumer; distinguish proposed objects, compiled source, deployed endpoints, and verified reachable operations.
