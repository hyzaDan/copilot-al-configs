---
name: bc-job-queue
description: Implement or diagnose Business Central Job Queue workloads, including parameters, retries, resumable batches and recovery.
---

# Job Queue and resumable batches

Select the execution mechanism for the requested behavior:

| Need | Candidate |
| --- | --- |
| User-managed schedule, recurrence and run logs | Job Queue |
| One-shot scheduled background task without Job Queue administration | Task Scheduler |
| Immediate separate session | StartSession |
| Read-only work tied to an open page | Page background task |

Read the consuming manifest and actual symbols for `Job Queue Entry`, `Job Queue - Enqueue` and `Job Queue Management`. Helper availability and signatures vary; choose a verified scheduling helper or the target's supported enqueue path. Do not hand-code a guessed status transition that bypasses scheduling.

## Define one run

- Specify object, company, execution identity, permissions, schedule and completion condition. A category code can serialize category work; it is not a substitute for workload-level idempotency or cross-system locking.
- Use `TableNo = "Job Queue Entry"` when the codeunit needs the invoking entry's `Rec`. Define a compact, versioned parameter contract and validate it before writes. Use `Record ID to Process` when appropriate; store larger payloads in a durable work record and pass its key.
- Keep business execution independent of UI. `GuiAllowed()` can guard optional progress, but missing decisions/configuration must fail clearly. Reports can run without a request page; interactive callbacks and file dialogs cannot be background dependencies.
- Distinguish recurring success from failure retry. `Maximum No. of Attempts to Run` and `Rerun Delay (sec.)` concern failed attempts; they do not schedule the next successful batch. Returning `BatchLimitReached` does not change the Job Queue entry by itself.
- Define safe retries before increasing attempt counts. Local commits and external effects may already have occurred when a run reports failure. Reconcile uncertain external results before resending.

Read [execution and diagnosis](references/execution.md) for setup/entry patterns. Read [resumable batching](references/batching.md) when a workload exceeds a safe single-run size or must resume after interruption.

## Verification and delivery

Compile in the consuming app. Verify the real background identity and execution path, invalid parameters, concurrent starts, interruption after a committed unit, transient/permanent failure, exhaustion, resume and completion. A foreground “run once” helps debugging but does not prove background compatibility. Report Job Queue state, durable business progress and external receipt separately.
