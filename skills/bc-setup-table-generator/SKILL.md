---
name: bc-setup-table-generator
description: Create or change Business Central singleton setup tables and cards, including safe initialization, field validation, secret references and optional assisted setup wizards.
---

# Setup tables and pages

Choose configuration scope first: one row per company, shared across companies or per user. Do not use a singleton key for multiple independent configurations. Follow the consuming app's ID allocation, naming, permissions and initialization convention.

## Singleton contract

- Use one stable primary-key value, commonly blank, with a dedicated lookup/initialization path. `Get()` with an omitted key uses default key values; it does not fetch an arbitrary first row. Make the intended key explicit where that improves clarity.
- Keep the key noneditable and prevent alternative rows through the actual supported write paths. Page `InsertAllowed = false` alone does not enforce a table-wide singleton invariant.
- Ensure initialization is idempotent and concurrent first access cannot overwrite a row another session just created. A setup page may initialize an absent row if the app intentionally permits that write and the user has suitable rights; otherwise display a clear setup requirement.
- Create defaults for a new row, not on every read/open. Preserve intentional zero/blank/false values on reinstall and future initialization.
- If using cached setup, define invalidation after changes. A session cache can otherwise continue using obsolete settings, especially in long-running/background sessions.

Company-wide shared configuration (`DataPerCompany = false`) requires an explicit business decision because an edit affects other companies. Do not switch the storage scope of an existing setup table as a cosmetic change. See [DataPerCompany](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/properties/devenv-datapercompany-property).

## Validate and authorize

Put business validation on table fields or shared management operations used by UI and non-UI paths. Use meaningful relations, ranges and cross-field rules. Do not put confirmations or page-only logic into a path that APIs and background processing must call.

Grant the needed tabledata permissions and object execute permissions through the project's permission model. Pages/codeunits use execute permission; setup data needs the appropriate read/insert/modify rights. Hiding or disabling a page field is not a security boundary.

## Store secrets separately

An API token/password does not belong in a persistent plain Text setup field, even if marked `ExtendedDatatype = Masked`. That property changes [display behavior](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/properties/devenv-extendeddatatype-property), not storage protection.

Persist a nonsecret key/reference and configuration state in setup; use the target's supported encrypted/isolated storage with the intended company/user scope for the actual secret. Verify `SecretText` and encrypted-storage API support, length limits and failure behavior. Do not fall back to plaintext or show the stored secret again. A credential-entry page variable must not accidentally be copied to the setup record.

## Assisted setup

When the task needs a step-by-step wizard, use [assisted setup and concurrent saves](references/assisted-setup.md). A simple setup card does not require a wizard, extra feature toggles or Guided Experience registration.

Verify absent/existing setup, repeated initialization, concurrent access, rejected values, least-privilege access and any background/API write path affected. For secrets, verify only presence/success and failure behavior without logging their value.
