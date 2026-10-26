# Migration decisions

Use this when moving or transforming persisted data.

- Document the source-version range and the source-to-destination identity. A join must uniquely identify the intended destination; decide how duplicate or conflicting existing target data is handled before writing it.
- Keep stable IDs and existing data until the supported obsoletion/migration sequence allows removal. Renaming a field in source, renumbering it, and migrating its data are different operations.
- When filling a new field, distinguish an uninitialized target from a legitimate zero/blank. Preserve customer edits made after an earlier partial attempt according to an explicit conflict rule.
- Select `Validate`, `Insert`/`Modify` trigger execution and other business operations intentionally. `Modify(false)` persists data but skips `OnModify`; blanket use can omit necessary invariants, while full business triggers may have unwanted side effects in a migration.
- Large set-based moves may fit `DataTransfer` where the target runtime supports it and business validation is unnecessary. It is an upgrade tool, not a substitute for triggers or application validation. Verify matching keys, allowed fields and restrictions against [DataTransfer documentation](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-data-transfer).
- Keep migration and completion marker atomic. Consider durable chunks only if the actual upgrade execution context supports the required commits; verify those restrictions first. Where supported, design explicit progress, idempotent resume and partial-state validation; a final tag alone cannot describe unfinished batches.
- Preconditions should detect unsupported source data before mutation. Postconditions should measure the intended result, such as mapped counts, preserved values and absence of orphan references, not merely that a loop ran.

Record the supported recovery path before a destructive migration. Extension uninstall/reinstall is not proof that data can be restored. In a code-generation task, describe unexecuted migration or recovery checks as pending.
