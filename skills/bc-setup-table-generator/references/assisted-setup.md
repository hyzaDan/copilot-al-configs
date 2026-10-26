# Assisted setup and concurrent saves

Use a `NavigatePage` with a temporary source/buffer or page variables for a multi-step wizard. Define the fields it owns and keep a baseline snapshot of those values when opening it. Persist only on a successful Finish; Back, Cancel and closing with X must not save partial setup or mark the guide complete.

## Navigation and validation

Show one coherent step at a time, with Back/Next/Finish state derived from the current step. Validate prerequisites before leaving the step and revalidate them at Finish, since dependencies may have changed. A review page should display the values that will actually be saved.

If validation writes other persistent tables, moving the source to a temporary table alone does not make the wizard nonpersistent. Inspect table validation helpers and isolate any such side effects until Finish. Keep new credentials in appropriately protected transient state until final storage; never copy them through a persistent Text field.

## Finish without overwriting another session

1. Start the short save transaction, acquire the appropriate lock/concurrency protection and reread current setup. Do not hold locks while the user works through the wizard.
2. Compare each wizard-owned field against its baseline. If another session changed the same field to a conflicting value, report the conflict or apply a documented merge rule. Preserve unrelated changed fields.
3. Apply only the owned changes to the freshly read record, using field validation in a deliberate order. Insert if truly absent; handle another session creating the singleton in the meantime.
4. Persist the validated configuration and then record successful completion. Do not mark a wizard complete before its required work succeeds.

Do not use `TransferFields` from an old temporary snapshot to overwrite the entire current setup. If saving several related records, keep their database writes atomic. If an external service operation is also required, define the partial-failure behavior; an AL transaction cannot roll back a remote call.

## Guided Experience registration

Register the wizard only when needed, using the actual supported event and `Guided Experience` overload. The current [InsertAssistedSetup contract](https://learn.microsoft.com/dynamics365/business-central/application/system-application/codeunit/system.environment.configuration.guided-experience) expresses `ExpectedDuration` in **minutes**, not seconds. Verify the target symbols, group, primary-setup flag and completion API before generating code. Use stable object identity and preserve user completion state on registration refresh.

Check cancellation at every step, failed validation, failed save, reopening completed setup, simultaneous edits to the same and unrelated fields, and setup creation by another session before Finish. Registration and successful compilation do not establish that the wizard completed in a running tenant.
