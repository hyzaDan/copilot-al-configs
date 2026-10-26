---
name: bc-app-lifecycle
description: Implement Business Central extension installation, reinstallation and data upgrades, including scoped initialization, upgrade tags, migration checks and fresh-install behavior.
---

# App lifecycle

Separate initialization from migration. Read the consuming app's current install/upgrade code, supported source versions, schema, dependencies and symbols before choosing triggers or APIs. Adding an AL codeunit does not authorize publishing, schema synchronization or data upgrade against an environment.

## Select the lifecycle

| Operation | AL mechanism | Intended work |
|---|---|---|
| First install or reinstall | `Subtype = Install` | Create missing required setup/defaults without overwriting retained customer configuration. |
| Upgrade existing data | `Subtype = Upgrade` | Validate prerequisites, transform existing data, then validate the result. |
| New company | Relevant company initialization/upgrade-tag registration hooks | Ensure the current schema's initial state and tags are correct for a company created later. |

Use `OnInstallAppPerCompany` for company data and `OnInstallAppPerDatabase` for shared state. `NavApp.GetCurrentModuleInfo` exposes `DataVersion`; zero indicates first installation, while retained data can exist on reinstall. Do not infer the presence of a setup row solely from version information. See [installation code](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-extension-install-code).

For upgrades, use `OnCheckPreconditionsPerCompany/PerDatabase`, `OnUpgradePerCompany/PerDatabase` and `OnValidateUpgradePerCompany/PerDatabase` as needed. Per-database upgrade sessions have no open company; do not read company tables there without an explicit, justified company strategy. Do not depend on ordering between separate upgrade codeunits. See [upgrade execution and tags](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-upgrading-extensions).

## Initialize without resetting customer choices

- Insert missing singleton/configuration rows and set defaults deliberately. Reinstall must preserve existing values, including intentional blanks or disabled options.
- Separate essential setup from demo data or optional features. Do not auto-enable integrations, assign elevated user permissions or create scheduled work unless requested.
- Keep company and database scope consistent with `DataPerCompany` and the applicable framework APIs.
- If telemetry is needed, use stable technical event identifiers and measured counts/durations. Company names, document IDs and raw errors are not `SystemMetadata`.

## Make migrations repeatable

An upgrade tag marks a particular completed transformation, not merely entry into an upgrade trigger:

1. Check whether the tag is already present in the intended scope.
2. Validate the source state and destination conflict policy.
3. Apply the migration and verify its postconditions.
4. Set the tag after successful work within the same transaction boundary.

Fresh installation already creates the latest schema, so mark historical migrations as satisfied without running transformations intended for older data. Register relevant tags for companies created later through the target `Upgrade Tag` events. Keep these registrations scoped to this app's migrations; inspect shared `SetAllUpgradeTags` effects before using it. Read [migration decisions](references/migration-decisions.md) for field/data moves and failure handling.

Do not use `NavApp.RestoreArchiveData` for modern uninstall recovery: the [API was deprecated for the historical V1-to-V2 extension migration](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/navapp/navapp-restorearchivedata-method). Recovery requires a separately verified backup/restore or supported migration path for the target environment.

## Verify the paths actually affected

Compile, then exercise fresh installation, reinstall with user-edited setup, upgrade from supported prior data, a repeated migration, failure before the tag is written and a newly created company where relevant. Assert retained configuration and migrated data after reload. A test that finds an existing setup row does not prove install code created it. Report static/compile checks separately from lifecycle tests and environment execution.
