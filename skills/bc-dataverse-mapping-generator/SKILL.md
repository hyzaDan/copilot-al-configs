---
name: bc-dataverse-mapping-generator
description: Design AL Dataverse table and field mappings, extend existing synchronization, and add coupling lookup pages.
---

# Dataverse mappings and coupling

Start from the actual BC table, Dataverse integration table, installed integration symbols and existing mappings. A custom Dataverse logical-name prefix does not determine the implementation path: inspect what is already mapped, including standard BC tables mapped to custom Dataverse entities.

| Existing state | Change |
| --- | --- |
| Table mapping already exists | Extend its field mappings through the supported target event; preserve its configuration |
| No suitable table mapping | Define table mapping, field mappings, coupling/lookup and synchronization behavior |
| Integration table missing or stale | Resolve its schema prerequisite before writing mappings |

If a proxy table is required, use the target AL tooling and actual Dataverse schema as a separate scoped step. This skill supplies no entity-generation script. Do not derive the consuming project from a plugin installation path or move broad `*.al` selections. Any authorized generation must target an explicit staging directory, record its outputs, and check collisions before importing them.

## Mapping decisions

- Record BC/integration table IDs, primary GUID and modified-on fields, company filters, table mapping name, and current coupling behavior.
- For each field, define source of truth, direction, conversion, null/empty behavior and validation on each side. Bidirectional is a decision about conflicts, not a default. Option/lookup fields may need specialized mappings.
- Resolve registration events and `Integration Table Mapping` / `Integration Field Mapping` methods through [target symbols](../al-symbol-lookup/SKILL.md). Project helper codeunits are optional local abstractions, not Microsoft platform APIs.
- Preserve mappings and user configuration when extending an existing integration. Configuration reset/full synchronization can change live behavior and data; source generation does not require executing them.

Read [mapping implementation](references/mapping.md) for extension points and idempotency, and [coupling UI](references/coupling-ui.md) only when a lookup/list page is needed.

## Verification

Compile in the consuming project, then validate the authorized sandbox path: initial coupling, matching conflicts, each configured direction, validation failures, lookup/option conversion, repeated configuration application, uncoupling, and sync retries. Compare both systems' values and sync logs. Do not claim a successful sync from compilation or page display alone.
