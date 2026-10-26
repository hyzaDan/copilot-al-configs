---
name: bc-isolated-storage-generator
description: Implement scoped Business Central isolated storage for credentials, including encrypted writes, SecretText handling and setup UI behavior.
---

# Isolated storage for credentials

Separate ordinary setup fields from secrets. `ExtendedDatatype = Masked` hides display text; it does not encrypt a table field. Isolated storage separates extension data, and `SetEncrypted` adds encryption. `SecretText` reduces accidental disclosure in AL; it does not itself choose encrypted persistence.

## Design the boundary

- Determine who must use the credential: one user, one company, the app, or one user within a company. Choose `DataScope` explicitly and use the same scope for save/read/check/delete. A user's token usually cannot serve a job running as a different user.
- Read the target runtime and symbols. `SecretText` isolated-storage overloads are documented from runtime 13.0; use them when supported. For older targets, minimize the lifetime and exposure of required Text values rather than pretending SecretText APIs exist.
- Use a stable key or a persisted opaque key reference. A manually supplied GUID is not mandatory. Never put the secret in the key, telemetry, captions, logs or errors.
- `SetEncrypted` accepts at most 215 plain characters, with special characters consuming more space. Determine whether the expected credential fits before choosing this storage. Never truncate tokens. For longer credentials, select a supported project-approved secret store; do not silently fall back to `Set` or split arbitrary tokens into invented storage chunks.
- Handle encryption unavailability and write failure explicitly. Leave the prior valid configuration intact and report a sanitized error; do not store plaintext as fallback.

Read [storage and UI patterns](references/storage-patterns.md) for the supported method shape and configuration lifecycle.

## Verify

Compile against the target and test save/read/replacement/delete in the intended scope, a different user/company, missing values, long/Unicode values and write failure. Check the actual background identity when the credential is used by Job Queue. Verify that a UI mask never becomes the stored value and that errors reveal no secret. Report persistence tests separately from a successful authenticated provider request.
