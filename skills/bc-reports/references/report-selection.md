# Report selection and document actions

Use this for a custom usage, configurable report choice or a print action that should honor standard selections.

## Usage and defaults

Inspect `Report Selections`, the common `Report Selection Usage` enum and the actual area's selection page/enum. The area enum and common enum may use conversion logic, not equal integer values. Extend both directions of that mapping where needed; adding one enum value does not establish a working selection.

For example, the [sales report-selection page](https://learn.microsoft.com/dynamics365/business-central/application/base-application/page/microsoft.sales.setup.report-selection---sales) exposes usage initialization/filtering extension points. Resolve signatures in the target symbols and examine the page's conversion path before choosing a subscriber.

Seed defaults only for absent app-owned usage/sequence entries and preserve user selections. Use install/upgrade code when the task needs versioned registration; do not reset report choices whenever a page opens. Honor configured order, customer/vendor-specific layouts and email/body choices when the requested flow uses them.

## Restrict current-document printing

`Report.RunModal` uses filters attached to its record argument; a card's current row is not automatically a singleton filter. Use a separate record variable filtered explicitly by the full primary key. For a sales document, this means both `Document Type` and `No.`. Preserve the UI record's filters and state.

`SetRecFilter` is also usable after confirming the **current key** uniquely selects the intended record. It filters fields in the current key, which may be a secondary key; it is not a universal synonym for primary-key filtering. See [SetRecFilter](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/record/record-setrecfilter-method) and [RunModal filters](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/report/report-runmodal-method).

For multi-selection, use the page's supported selection-filter pattern instead of reducing it to one current row. Verify the report's root dataitem accepts the passed table/filter. Test current-document printing while the page has no restrictive filter, with another document sharing its number in a different type. Test empty selections, multiple configured reports and preserved user defaults.
