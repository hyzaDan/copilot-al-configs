# Coupling list and lookup

Use an existing compatible list page where available. Otherwise create a `List` page over the verified integration table. A read-only coupling selector should set `Editable`, `InsertAllowed`, `ModifyAllowed` and `DeleteAllowed` to `false`; that is a UI choice, not a claim that CDS tables can never be written through integration code.

Allocate the page ID against the consuming manifest's ranges and all project source locations. Follow its naming policy and actual schema. Show the identifiers, names and status needed to disambiguate a selection; expose technical IDs only when they help that task. Avoid an unconditional requirement for a specific directory, prefix, action or initialization call.

## Lookup sequence

The Microsoft walkthrough uses this sequence. The integration table/page and its GUID field depend on the entity; any `SetCurrentlyCoupled...` method is a custom page procedure you implement, not a platform method.

1. Load the current external GUID if it still exists and position the page on it.
2. Pass the currently coupled record when the UI needs to distinguish it from the selection.
3. Apply the integration mapping's view/filter with `SetView` and `SetTableView` before lookup. Preserve company and eligibility restrictions.
4. Call `LookupMode(true)` and run the page modally.
5. Only after `Action::LookupOK`, call `GetRecord` and return the selected external GUID. On Cancel, return failure and keep the caller's coupling unchanged.

If adding an action to create BC records from selected external rows, use the target integration management API and selection filter. Treat it as a business mutation with permissions and duplicate/coupling checks, not a mandatory list-page decoration. Do not hide synchronization failure behind a successful page close.

Test empty results, stale current coupling, an already-coupled selection, ambiguous names, Cancel, and LookupOK. Check that normal page browsing cannot accidentally change coupling.

Source: [Microsoft's custom Dataverse integration walkthrough](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/administration-custom-cds-integration).
