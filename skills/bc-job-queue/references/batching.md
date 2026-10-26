# Resumable batching

Batch size should bound lock duration, transaction size, external requests and run time. Measure it for the actual workload; neither a fixed row count nor a blanket `Modify(false)` is a safe performance recipe.

## State and transaction design

Separate a durable logical run from scheduler attempts. For resumable work, useful persisted state includes operation/version, company, eligibility filter or snapshot, immutable ordering/checkpoint, completion/error state, counters, and last progress time. Use a run key only when concurrent logical runs are meaningful.

Choose what new or changed records mean during a run. A high-water mark over an immutable key can define a fixed window; a durable work-item list can define a snapshot. A mutable filtered `FindSet` is not itself a snapshot. Test records that become eligible behind the checkpoint and changes to the processed/filter field.

Concrete processing algorithm, to adapt to the workload's transaction boundary:

1. Claim the run/work unit using the project's concurrency mechanism; reject an overlapping owner.
2. Load the next eligible unit in deterministic order.
3. Re-read/validate it and perform the required business operation with its proper triggers and validation.
4. Persist the business result and its checkpoint together where they share a database transaction. Commit only at the chosen unit boundary, outside callers that require atomic posting.
5. Stop at the row/time budget or when no eligible work remains. Persist `MoreWork` or `Completed` explicitly.
6. Arrange the next successful run through the chosen recurring schedule or a verified continuation mechanism. Make the completion path disable/remove a finite-run schedule safely, or make recurring runs skip completed work without side effects, according to the intended operations model.

If a business service commits internally, a later checkpoint can lag its result. Reconstruct progress from durable results or use an idempotent operation key. Never claim that enclosing code makes an internally committed service atomic.

## External effects

A database transaction cannot roll back a successful external request. Use a persisted operation key/outbox and provider idempotency where available. On timeout after send, record an uncertain result and reconcile it before another attempt. Do not mark work complete before the required external acknowledgment, or interpret a local exception as proof that the provider did nothing.

## Record processing

- Use `Validate` and trigger execution according to the business requirement. `Modify(false)` still writes the record and skips the table modify trigger; choose it only when that omission is intentional and justified.
- Select ordinary fields actually needed by partial-record reads. FlowFields require `CalcFields`/supported auto-calculation; they do not belong in `SetLoadFields`.
- Avoid repeated full-table counts for every row. Expose completed count and elapsed time; an ETA based on changing workload remains an estimate.
- Handle poison records deliberately: stop atomically or persist a failed item with a later repair path. Do not silently advance past lost work.

## Failure scenarios to exercise

Interrupt before a unit commit, after commit but before continuation, and after external acceptance but before local acknowledgment. Run two workers against the same run. Repeat a completed run. Test an empty run and exactly-at-limit run. Confirm that no record is skipped or duplicated and that a finite job reaches its actual terminal state.

Sources: [Job Queue retry semantics](https://learn.microsoft.com/dynamics365/business-central/admin-job-queues-schedule-tasks#handle-job-queue-entry-issues), [database transactions and Commit](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/database/database-commit-method), [Record.Modify](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/record/record-modify-method), [partial records](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-partial-records).
