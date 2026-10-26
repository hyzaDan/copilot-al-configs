# Storage and setup UI

## Scope

All scopes are within the extension context:

| Scope | Accessibility |
| --- | --- |
| `Module` | App context |
| `Company` | Company in the app |
| `User` | User in the app |
| `CompanyAndUser` | User and company in the app |

Omitting a scope defaults to `Module`; do not rely on that default for credentials. Scope is not a substitute for controlling which app code/UI can call the credential service.

## Encrypted write and read

These procedures fit in the consuming credential-management codeunit when its runtime supports the SecretText overloads. The caller supplies the chosen scope and a non-secret storage key.

```al
local procedure SaveCredential(StorageKey: Text; Value: SecretText; Scope: DataScope)
var
    SaveFailedErr: Label 'The credential could not be stored securely.';
begin
    if not IsolatedStorage.SetEncrypted(StorageKey, Value, Scope) then
        Error(SaveFailedErr);
end;

local procedure TryReadCredential(StorageKey: Text; Scope: DataScope; var Value: SecretText): Boolean
begin
    Clear(Value);
    exit(IsolatedStorage.Get(StorageKey, Scope, Value));
end;
```

The method's capacity/encryption failure remains a failure; there is no `Set` fallback. Check the provider's documented credential format and length before selecting this implementation, and test the target's rejection path with boundary values. Do not unwrap SecretText merely to format it or include it in an error. Confirm that the actual target preserves a previous value after a failed replacement.

Missing credentials should produce a clear configuration state. A failed read must not be treated as successful authentication. Use `Contains`/`Delete` with the same key and scope for explicit removal; handle absent values deliberately.

## UI lifecycle

- Display a Boolean/status such as “Credential configured”; do not load the stored secret back into a visible setup field.
- Use a dedicated input variable for replacement and clear it after a successful save. Retain the target runtime's secret-safe UI/API boundary.
- Distinguish unchanged input, replacement, and an explicit clear action. Do not interpret a literal mask or an empty field as an instruction to overwrite/delete the secret.
- When migrating a plaintext setup field, write securely and verify success before clearing the old value. Preserve recoverable configuration on failure and avoid exposing the source value during migration.

## Primary sources

- [Isolated storage](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-isolated-storage) and [DataScope](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/datascope/datascope-option).
- [SetEncrypted with SecretText](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/isolatedstorage/isolatedstorage-setencrypted-string-secrettext-datascope-method): runtime, capacity and failure result.
- [Get with SecretText](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/isolatedstorage/isolatedstorage-get-string-datascope-secrettext-method).
