# Implementing mappings

Build a field contract before code. A useful working table is:

| Field pair | Authority/direction | Conversion | Validation | Conflict/null policy |
| --- | --- | --- | --- | --- |
| BC code to external code | BC to Dataverse | Exact code mapping | Per business rules | Reject collisions |
| External status to BC status | Dataverse to BC | Explicit option mapping | Validate transition | Reject unknown values |

These rows illustrate decisions, not universal directions. Lookup values are entity references; an option's numeric value or caption is not a portable mapping by itself. Microsoft documents option synchronization as one-way rather than bidirectional; check the relevant mapping support for the target.

## New table mapping

The Microsoft walkthrough uses `CDS Setup Defaults.OnAfterResetConfiguration` to add default mappings, and lookup/entity-registration publishers to enable coupling. Inspect their actual signatures and invocation conditions before subscribing. A fixed count of subscribers is not a requirement.

Create the table mapping with the actual table identity, external primary GUID, modified-on field, filters and templates. Choose whether to sync only coupled records and what creation/deletion/uncoupling means. Table-level and field-level directions must agree. Keep company filters and coupling identity explicit to avoid synchronizing another company's records.

The walkthrough's `InsertIntegrationTableMapping` and `InsertIntegrationFieldMapping` procedures are locally defined wrappers. They must be implemented in your code or replaced with verified target methods; they are not ambient APIs. Different published examples even use different `CreateRecord` overloads, so copy the signature from the consuming symbols.

## Extend an existing mapping

Find the target's extra-field-mapping event and restrict the subscriber to the intended mapping/table pair. Use `FieldNo(...)` on verified typed records rather than hard-coded field numbers. Only add the required fields; do not rebuild the standard table mapping to add one field.

An idempotent application of desired mappings should:

1. Locate the existing mapping using its actual key.
2. Compare its source/destination fields and direction with the intended definition.
3. Insert when absent; preserve an equivalent row; handle a conflicting row deliberately instead of overwriting it silently.
4. Apply the same rule when setup events run again or an app upgrades.

Resetting default synchronization setup is an operational action that can replace configuration. Explain its impact for the selected environment before executing it within authorized scope; it is not a build step.

## Primary sources

- [Customizing a Dataverse integration](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/administration-custom-cds-integration): new and existing mappings, helpers, lookup and coupling.
- [Customizing option mappings](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/administration-custom-option-mapping): one-way option mapping behavior.
- [Connect to Microsoft Dataverse](https://learn.microsoft.com/dynamics365/business-central/admin-how-to-set-up-a-dynamics-crm-connection): matching, coupling conflicts and setup behavior.
