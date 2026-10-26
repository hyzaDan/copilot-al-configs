---
name: bc-table-dimensions-generator
description: Add Business Central default dimensions or document dimension sets to custom tables and pages, including shortcut dimensions, source inheritance, line cascades and read-only historical views.
---

# Table dimensions

Distinguish master-data **Default Dimensions** from the **Dimension Set ID** captured on a document/journal/entry. A master record's defaults are input to a later transaction's dimensions, not the same persisted object. Identify which model the target table needs before adding fields.

Use the consuming app's field allocation, source-code policy and target `DimensionManagement` symbols. Match an appropriate standard table's behavior; do not import paths or conventions from an unrelated customer project.

## Preserve dimension-set consistency

A dimension set identifies a reusable combination of dimension values. Use supported management APIs to obtain/change the set, rather than modifying shared dimension-set entries in place. See [dimension-set storage](https://learn.microsoft.com/dynamics365/business-central/design-details-dimension-set-entries-overview).

- For a document model, persist `Dimension Set ID` and the required global/shortcut dimension fields. Allocate field IDs from the app; a standard table's field numbers are not an automatic allocation for a custom table.
- Validate shortcut values through `DimensionManagement` so blocked values/combinations and the set are handled consistently. Refresh global dimension 1/2 values from the resulting set after edits or inheritance.
- Updating a shortcut/set does not by itself prove combination or value-posting checks ran. Inspect the target helpers and standard flow; perform the applicable combination and value-posting checks explicitly when they are not included.
- Display shortcut dimensions 3-8 from the set through page variables where appropriate, rather than creating another unsynchronized authoritative copy.
- Keep table/business validation reachable by APIs and imports. Direct assignment to a source field bypasses its `OnValidate`; call validated operations when dimensions must follow.
- For master-data defaults, use the standard Default Dimensions integration and lifecycle behavior for that table identity. Check rename/delete handling, value-posting constraints and priority participation.

The current [DimensionManagement API](https://learn.microsoft.com/dynamics365/business-central/application/base-application/codeunit/microsoft.finance.dimension.dimensionmanagement) documents helpers such as `ValidateShortcutDimValues`, `UpdateGlobalDimFromDimSetID` and `GetDeltaDimSetID`. Resolve exact overloads in the target symbols before writing calls.

## Source inheritance and lines

Read [inheritance decisions](references/inheritance.md) for multiple sources, fallback and header-to-line changes. Define whether a master-data change replaces, merges or preserves manually edited dimensions. Do not silently pick the sales source code for an unrelated process.

## Page and history behavior

- Use configured dimension captions and visibility from the target's dimension setup. Refresh shortcut arrays on record navigation, new record and successful dimension changes so the previous record's values cannot remain visible.
- For newly declared page fields use `OnValidate`; `OnAfterValidate` belongs to modification of an existing page field in a page extension. See [page-field validation](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/triggers-auto/pagefield/devenv-onvalidate-pagefield-trigger) and [page-field extension validation](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/triggers-auto/pagefieldextension/devenv-onaftervalidate-pagefieldextension-trigger).
- Dimension editing should refresh the set, global fields and page variables together. Avoid implicit extra saves merely to refresh a page.
- Archive and posted records retain the historical set and expose read-only dimension viewing unless a specific supported correction flow is requested. Verify the actual posting/archive copy path; matching field numbers help `TransferFields` but do not establish that it is used.
- Do not expose unrestricted raw set-ID writes as an API shortcut; validate existence, allowed changes and synchronization with the displayed globals.

Verify source defaults, conflicts/priorities, cleared sources, manual dimensions, shortcut 3-8 edits, blocked values, line cascades and historical viewing. Test table/API validation independently of page refresh, and report the checks actually executed.
