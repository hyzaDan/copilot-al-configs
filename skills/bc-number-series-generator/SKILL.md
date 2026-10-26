---
name: bc-number-series-generator
description: Add or repair Business Central automatic/manual numbering and AssistEdit, including related series, date selection and correct use of the target No. Series APIs.
---

# Number series

Inspect the entity's insert, number validation, copy and AssistEdit paths plus the setup field holding its default series. Use the consuming app's allocated IDs and target symbols. Modern `No. Series` and legacy `NoSeriesManagement` contracts differ; do not mix their parameter conventions.

## Number assignment

- Allocate only when a new persistent record needs a number. Preserve an existing number during edits, posting retries and copies according to that entity's rules; avoid consuming numbers for a temporary preview.
- When the number is blank, validate the configured default series. Reuse a previous/selected series only when the relevant relationship rule permits it, then obtain the number through the supported API.
- Choose the usage date explicitly: document date, posting date or work date can select different series lines. The one-argument modern `GetNextNo` uses the work date.
- When the user changes the number manually, enforce the configured manual-number policy using the target `TestManual` equivalent. Clear the record's automatic-series marker where the standard entity pattern requires it. Do not mistake a programmatically assigned automatic number for manual entry.
- `PeekNextNo` does not reserve a number. Do not persist its result or promise it will remain available. Let the numbering implementation coordinate concurrency; do not calculate `MAX(No.) + 1`.

The current [No. Series API](https://learn.microsoft.com/dynamics365/business-central/application/business-foundation/codeunit/microsoft.foundation.noseries.no.-series) documents `GetNextNo`, `PeekNextNo`, `TestManual`, `AreRelated` and `LookupRelatedNoSeries`. Verify availability in the target symbols before generating calls. Number-series [gap and manual-entry settings](https://learn.microsoft.com/dynamics365/business-central/ui-create-number-series) are business choices; do not enable gaps as an incidental optimization.

## AssistEdit result and cancellation

Work on a candidate series until selection succeeds. Cancellation must leave the original record unchanged. On success, assign the selected series and allocated number, then **return true** so a caller guarded by `if Rec.AssistEdit(...) then` refreshes correctly.

This helper illustrates the modern selection/result contract; it does not persist a record or replace the entity's validation:

```al
local procedure TrySelectNumber(DefaultSeries: Code[20]; UsageDate: Date;
    var SelectedSeries: Code[20]; var SelectedNo: Code[20]): Boolean
var
    NoSeries: Codeunit "No. Series";
    CandidateSeries: Code[20];
    CandidateNo: Code[20];
begin
    CandidateSeries := SelectedSeries;
    if not NoSeries.LookupRelatedNoSeries(DefaultSeries, CandidateSeries) then
        exit(false);
    CandidateNo := NoSeries.GetNextNo(CandidateSeries, UsageDate);
    SelectedSeries := CandidateSeries;
    SelectedNo := CandidateNo;
    exit(true);
end;
```

Do not invoke a selection dialog from APIs or background jobs; use an explicit configured series there. Do not add a `Commit` to resolve number-series locking without understanding the document transaction.

Verify automatic insert, manual allowed/forbidden, related/unrelated series, cancellation, date boundaries, exhaustion and concurrent creation. Check rollback/gap expectations for the actual series implementation, and verify the page refreshes only after a successful AssistEdit result.
