# Execution and diagnosis

## Entry construction

Use the target's helper when it matches the requested schedule. Otherwise inspect the verified enqueue codeunit's expected entry state and construct only the required fields. Typical decisions include:

| Entry setting | Decision |
| --- | --- |
| Object type and ID | Actual runnable codeunit/report |
| Earliest start | Not-before time, not guaranteed start time |
| Recurrence | Intentional schedule for future successful runs |
| Maximum attempts and rerun delay | Failure policy for this workload |
| Parameter string / record ID | Validated business context, without secrets |
| Category | Serialization needed for this category |

Use `MaxStrLen` to reject oversized parameters rather than silently truncating a machine contract. Do not use captions/descriptions as a parser contract.

For a job whose entire parameter is a durable run GUID, a parsing helper can be:

```al
local procedure ParseRunId(ParameterValue: Text): Guid
var
    RunId: Guid;
    InvalidParameterErr: Label 'The job parameter must be a non-empty run identifier.';
begin
    if not Evaluate(RunId, ParameterValue) then
        Error(InvalidParameterErr);
    if IsNullGuid(RunId) then
        Error(InvalidParameterErr);
    exit(RunId);
end;
```

Call this on `Rec."Parameter String"` in a codeunit with `TableNo = "Job Queue Entry"`, then load the durable run record in the intended company. Validate the run's operation/version/authorization before processing. The GUID is a lookup key, not authorization by itself.

## Background behavior

The Job Queue dispatcher runs the object in a background session; the error handler executes separately after failure. Keep persistent progress outside globals and UI state. Avoid `Confirm`, page dialogs, request pages, upload/download dialogs or assumptions about the user's current page. A noninteractive report invocation is not categorically forbidden; verify its request-page and output behavior.

Allow errors that should fail the run to reach the framework. Catching an error, logging it and returning success can suppress retry and misreport completion. If partial success is intentional, record explicit per-item outcomes and the run-level result.

## Diagnose in order

1. Inspect the entry, associated scheduled task and Job Queue Log Entries: distinguish enqueue failure, no start, execution failure and final exhaustion.
2. Check company, execution identity/permissions, scheduling window/category, parameters, and UI callbacks.
3. Inspect committed work/checkpoints and any external receipt before restart. Classify configuration/business-data errors separately from retryable service failures.
4. Correlate official Job Queue telemetry by job/attempt and time. Use the current documented schema instead of inferring an event's meaning from its name. Add custom business-progress telemetry only where needed.

Use [telemetry design](../../bc-telemetry-generator/SKILL.md) when adding custom traces; do not copy raw errors or parameter payloads into technical metadata.

## Primary sources

- [Job Queue internals and background behavior](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-job-queue).
- [Schedule tasks and handle failed attempts](https://learn.microsoft.com/dynamics365/business-central/admin-job-queues-schedule-tasks).
- [Async processing overview](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-async-overview).
- [Job Queue telemetry](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/administration/telemetry-job-queue-lifecycle-trace).
