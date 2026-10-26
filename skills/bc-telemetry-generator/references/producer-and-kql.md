# Matching producer and KQL

## Numeric duration example

`Duration` stores milliseconds as a 64-bit integer. Assign it to `BigInteger`, then format that number with standard format 9. The example event ID is a sample contract to replace consistently in source and query. Pass a deliberate scope from the consuming implementation.

```al
local procedure LogBatchCompleted(Elapsed: Duration; ProcessedCount: Integer; Scope: TelemetryScope)
var
    ElapsedMs: BigInteger;
    Dimensions: Dictionary of [Text, Text];
begin
    ElapsedMs := Elapsed;
    Dimensions.Add('DurationMs', Format(ElapsedMs, 0, 9));
    Dimensions.Add('ProcessedCount', Format(ProcessedCount, 0, 9));
    Session.LogMessage('ExampleBatchCompleted01', 'Batch processing completed.',
        Verbosity::Normal, DataClassification::SystemMetadata, Scope, Dimensions);
end;
```

Only numeric technical measurements and a static message are emitted. The caller computes `Elapsed` from the actual operation and does not pass document identifiers or free-form errors. This is a method fragment; compile it inside the target app with its supported runtime and naming policy.

Business Central adds `AL` to the emitted AL event ID and `al` to custom dimension names. Thus the matching Application Insights query is:

```kusto
traces
| where timestamp > ago(24h)
| where tostring(customDimensions.eventId) == 'ALExampleBatchCompleted01'
| extend DurationMs = tolong(customDimensions.alDurationMs),
         ProcessedCount = tolong(customDimensions.alProcessedCount)
| where isnotnull(DurationMs) and DurationMs >= 0
| summarize Runs = count(),
            P50Ms = percentile(DurationMs, 50),
            P95Ms = percentile(DurationMs, 95),
            Processed = sum(ProcessedCount)
    by bin(timestamp, 1h)
| order by timestamp asc
```

Inspect an actual trace before relying on the query: match the configured resource/table schema and project event ID. If malformed durations exist, report/count them separately instead of presenting the filtered sample as all runs. A zero-row result can mean no events, wrong destination, prefix/schema mismatch or time range; it does not prove healthy behavior.

For failures, define a small fixed taxonomy such as timeout, validation, configuration and unexpected failure. A helper should accept that taxonomy or an enum and generate the allowed dimension value, rather than accepting arbitrary error text. Preserve useful stack/error detail in the appropriate access-controlled diagnostic channel when required, not indiscriminately in custom telemetry.

## Primary sources

- [Create custom telemetry](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-instrument-application-for-telemetry-app-insights): overloads, scopes and `al` dimensions.
- [Telemetry event IDs](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/telemetry-event-ids#find-al-event-ids-in-the-application-source): `AL` event ID prefix.
- [Duration type](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/duration/duration-data-type) and [AL assignment/type conversion](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-al-variables#assignment-and-type-conversion): milliseconds and conversion to BigInteger.
- [Formatting values](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-format-property): standard format 9.
