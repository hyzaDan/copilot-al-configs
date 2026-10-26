# Baseline behavior evaluation

Date: 2026-10-23. Evaluator: independent baseline agent.

Only the snapshot at `the immutable 0.2.0 baseline snapshot outside skill discovery` was used. Skills were discovered from their metadata before their bodies were selected. No current repository skill contents, audit report, or before/after conclusions were loaded. The integration notes were read because the selected imported skills explicitly require them. Links from those notes to the audit, import manifest, and other unrelated material were not followed. This is a static behavior evaluation; no AL source, BC server, Job Queue entry, translation, or email was changed, built, executed, or sent.

## Case A — small tooltip change

### Baseline answer

The minimal change is one property value in the existing `PostingDate` control:

```diff
- ToolTip = 'Old';
+ ToolTip = 'Explains the posting date.';
```

Keep the existing pageextension, quoted object names, suffix `XYZ`, field binding, and all other properties unchanged. The tooltip stays in the project's `en-US` source language. Czech translation remains in the separate phase after the released source build, as your project policy requires.

Verification should be proportional: inspect the diff to confirm that only this tooltip changed; during the normal source-build step compile the intended AL project with its configured analyzers, and inspect the tooltip in the intended page when that build is available. No new AL test codeunit is needed for this literal-only change. I have not edited or built anything, so no compile or UI result is claimed.

### Selected guidance and evidence

- `skills/al-coding-standards/SKILL.md`: selected through its metadata for AL names and user-facing text. Lines 9–19 give project-policy precedence, preserve project naming, and prohibit incidental affix migration. Its final translation link routed to the next skill.
- `skills/al-translation-phase/SKILL.md`: selected for the changed tooltip. Lines 11–23 describe the source-build prerequisite, en-US to cs-CZ scope, and worker routing. No translation workflow was started because the request explicitly defers translations.
- The historical `team-conventions.md` was not loaded: the request neither adopts that policy nor identifies the project as using it. Build skill and documentation generators were not loaded merely to describe a later normal verification step.

### Evaluator notes — not part of the baseline answer

The small-change route remained small. User policy resolved translation timing without a permission question, mandatory translation, name cleanup, architecture document, deployment, or invented test evidence. The translation skill was read only because the coding skill routes changed localized text there; its worker workflow was not triggered.

## Case B — restartable campaign propagation and one summary per logical job

### Baseline answer

Use Job Queue: it supplies the visible schedule, run history, and manual restart path this workload needs. Keep the runnable codeunit small and put the mapping/transform in a reusable business procedure. Reuse the existing subscriber's custom transformation; do not replace or delete it merely because a nearby standard routine uses `TransferFields`.

The different source and destination field IDs are valid for explicit assignment. They prevent treating these fields as an automatic same-ID `TransferFields` mapping; changing established IDs is not a prerequisite for this design. Preserve the declared types and lengths and decide deliberately whether destination business validation must run.

For new invoices, apply the transformed value in the verified posting flow at the point where the invoice record will actually be persisted. For a backfill of existing posted invoices, use the authorized posted-data update path and verified order-to-invoice linkage. These are materially different operations, so the final implementation must establish which is intended. Do not infer the source sales document from `No.` alone: use company context plus `Document Type` and `No.`, and the complete line identity if line-level data is involved. Partial or combined invoicing also needs an explicit campaign rule.

For restartability, persist a logical run ID and its bounded input selection before processing. Let `Parameter String` carry a small, versioned run-ID contract and parse it at entry; a runnable `TableNo = "Job Queue Entry"` pattern is appropriate once verified for the target. Persist work-item identity, progress, outcome, and enough mapping provenance to avoid reprocessing completed work or silently changing the transform on restart. Keep each database change and its completed-work marker in the same transaction where the actual posting/update flow permits it. Do not add `Commit` inside the subscriber. Prevent two workers from claiming the same work, and distinguish transient retryable failures from configuration and business-data failures.

Persist one summary notification request keyed by logical run ID when the run reaches its agreed terminal state. Send it through the supported Email module after business processing, with persisted notification status and reconciliation for an uncertain send result. A database `Sent` flag written after an external send cannot alone guarantee exactly one delivered email across a crash: retrying may duplicate delivery, while setting it before the send can lose delivery. The target email API's persistence/deduplication behavior must be verified; otherwise promise one durable summary request and explicit handling of uncertain delivery, not proven exactly-once delivery. Do not send the summary from a per-document posting subscriber.

Set attempts and delay intentionally. `Maximum No. of Attempts to Run` counts failure attempts; it is not the number of successful batches. If work is split over successful invocations, implement completion and rescheduling explicitly. On restart, resume the same logical run and unfinished notification state rather than generating a fresh summary identity.

Operations can inspect Job Queue Entries and Log Entries. For telemetry, correlate the logical run with the platform job ID and distinguish enqueued (`AL0000E24`), started (`AL0000E25`), finished (`AL0000E26`), retryable failure (`AL0000HE7`), and final failure (`AL0000JRG`). Record counts and status without raw campaign/document data in system telemetry.

The smallest remaining inputs are:

1. The target BC/app version and target symbols or source, plus the current subscriber and source/destination field definitions. This establishes the real publisher, parameter modifiers, persistence timing, Job Queue APIs, and Email APIs.
2. Whether this job handles new postings or backfills existing invoices, which documents it selects, and the rule for partial/combined invoices and an already populated destination campaign.
3. The summary recipients and whether "once per job" means one logical run across all retries, including terminal partial failure. I recommend that interpretation; recurrence starts a new logical run.

Before implementation is accepted, verify successful propagation with the existing transform, same document number across different document types, partial/combined invoice behavior, restart after a committed item, competing workers, terminal failures, and the send-result uncertainty window. No symbols or test runner are available here, so the design is provisional at API boundaries. I have generated no event signatures and claim no compile, runtime, or email result.

### Selected guidance and evidence

- `skills/bc-job-queue/SKILL.md`: selected for visible queue scheduling, parameter contracts, restart/retry, and diagnosis. Line 30 requires target-symbol verification before final AL. Lines 80–126 address parameters, background safety, and retries; lines 135–158 address in-client and telemetry diagnosis.
- `skills/bc-job-queue/references/code-patterns.md`: read for the entry codeunit, enqueue, foreground/restart, and telemetry scaffolds. The file begins by requiring target signature verification, so its concrete sample calls were not asserted as available target APIs.
- `skills/bc-field-propagation/SKILL.md`: selected for source-to-posted-invoice field mapping and the existing subscriber.
- `skills/bc-field-propagation/references/pattern-a-table-map.md` and `references/pattern-b-event-map.md`: read because the selected skill expressly says to read both. Their tables were treated as discovery hints, not verified target publisher signatures.
- `docs/upstream-skill-integration.md`: required by both imported skills. Common rules give project scope precedence and prohibit unverified APIs. Line 57 corrects the same-field-ID and subscriber-deletion rules; line 73 addresses complete sales-document identity; line 89 corrects batch attempts/completion assumptions. Its corrections qualify the imported examples.
- `skills/al-solution-architecture/SKILL.md`: selected through metadata for lifecycle, data model, posting, and integration trade-offs. Lines 17–26 require proportionality, consequential questions only, and verified dependency APIs.
- `skills/al-symbol-lookup/SKILL.md`: followed from the integration/design routing to define the missing API evidence. No symbol tool was used because this test case explicitly provides none.
- `skills/al-testing/SKILL.md`: selected to describe meaningful regression verification and preserve the distinction between authored scenarios, compilation, and executed tests.
- `bc-batch-processing` metadata was inspected but its body was not loaded: the Job Queue skill and required integration correction already covered this design's retry/completion question; no large-volume performance requirement was supplied.

### Evaluator notes — not part of the baseline answer

The baseline produced an explicit-assignment design despite the propagation skill's body saying the IDs must always match and the request should otherwise be rejected. That result depends on following the skill's mandatory integration-note link. The same integration notes prevent removal of the custom-transform subscriber. API uncertainty remains explicit; no publisher signature was invented. The logical-run and notification ledger are architectural reasoning for the stated restart/once requirements, not assertions that the bundled samples already implement those guarantees.

No full architecture document, invented object ID, release pipeline, deployment, or fixed interview was added. The design can proceed usefully while three consequential inputs remain unresolved. The exact identity, posting semantics, and email uncertainty are still required before producing production code.

## Case C — correct code and false-positive resistance

### Baseline answer

No actionable proven defect is established by this snippet under the facts supplied. The subscriber signature, declarations, record semantics, and field metadata are given as valid; I would not invent syntax or runtime failures from the omitted detail.

| Proposed requirement | Require it here? | Reason |
|---|---|---|
| `SingleInstance = true` | No mandatory fix in this evidence-only review | The loaded coding skill explicitly defaults event-handler codeunits to `SingleInstance` and asks for a documented reason to omit it. That is a convention in the guidance, not proof that this stateless `StaticAutomatic` codeunit is defective. No company rule or measured cost is supplied. I would identify this guidance tension, not report a performance defect or block approval. |
| `InherentPermissions` / `InherentEntitlements` | No | The imported reviewer says to require them, but its mandatory integration notes expressly correct that universal requirement. The snippet establishes no missing permission grant or failed access. |
| `Balance` in `SetLoadFields` | No | The integration correction says FlowFields must not be put in `SetLoadFields`. `Name` is the ordinary loaded field; `Balance` is explicitly calculated through `CalcFields`. No extra partial-record finding is supported. |
| Automatic rollback after every test | No | No test runner configuration was supplied. The integration notes distinguish `Disabled`, `Codeunit`, and `Function` isolation; per-test rollback cannot be presumed or required from this snippet. |
| Full architecture documentation | No | A focused review of this pattern provides no basis for that extra deliverable. |

There are no proven naming, performance, extensibility, or SaaS defects in the supplied scope. AppSource readiness, manifest ranges, packaging, permission-set completeness, and runtime tests cannot be determined from this excerpt; they are outside this finding, not failures. Nothing was compiled or executed. No fix list is warranted.

### Selected guidance and evidence

- `skills/bc-al-code-reviewer/SKILL.md`: selected from its code-review metadata. Its required `references/convention-stack.md` was loaded for the relevant naming, performance, extensibility, and SaaS checks. No AppSource-readiness assessment was requested, so `references/appsource-blockers.md` was not loaded.
- `skills/bc-al-code-reviewer/references/convention-stack.md`: contains the broad PF-01 rule and FlowField sample around lines 188–209, SR-01/SR-02 universal permission requirements at lines 400–423, and other generic review checks. These are subject to the required integration corrections.
- `docs/upstream-skill-integration.md`: line 53 corrects the FlowField, JIT, subscriber-signature, and universal inherent-permission claims. Line 77 states that test isolation determines rollback boundaries. Common rules say the existing `al-*` skills own review and testing.
- `skills/al-bc-solution-review/SKILL.md`: selected from its metadata and integration routing. Lines 26–29 require findings to cite evidence and a failure scenario, distinguish conventions from platform rules, and disclose incomplete verification.
- `skills/al-coding-standards/SKILL.md`: followed for the subscriber/naming question. Line 9 distinguishes project conventions and platform restrictions. Lines 43–44 explicitly prescribe default `SingleInstance` plus an exemption rationale. This tension is exposed above rather than erased from the baseline.
- `skills/al-testing/SKILL.md`: selected for the explicit rollback question; it asks for deterministic isolated setup and actual runner/environment evidence, not a blanket rollback assertion.
- No performance skill was loaded solely because `SetLoadFields` appears; the supplied case gives no meaningful runtime-cost risk. No architecture generator was loaded to answer whether a document is required.

### Evaluator notes — not part of the baseline answer

The actual baseline response has zero proven findings. This is not evidence that every baseline rule is sound: the loaded coding skill still contains a default `SingleInstance` mandate, and the imported reviewer still contains incorrect blanket requirements and a FlowField example. The outcome relies on respecting the explicit user scope, the local solution-review evidence requirement, and the mandatory integration corrections. A reader that stops at the imported review body or obeys the SingleInstance paragraph as a platform requirement would get a different answer.

The answer deliberately reports the SingleInstance policy tension instead of silently pretending that the old guidance is already the desired guidance. It does not label the correct code a defect simply to obey an imported checklist.

## Read boundary and execution evidence

The tool activity consisted of snapshot file discovery, metadata searches, reading the selected skill/reference files listed above, and writing this report. No browser, public documentation fetch, symbol lookup, test runner, BC call, delegation, application edit, or deployment was performed. Metadata discovery initially returned a truncated aggregate; the selected skill bodies and relevant evidence were read separately. The selected field-propagation body's truncated middle was recovered with a bounded line read. No conclusions were borrowed from the parent's findings.
