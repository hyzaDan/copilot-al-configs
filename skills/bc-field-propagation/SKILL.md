---
name: bc-field-propagation
description: Trace and implement custom-field propagation through Business Central posting, journal, archive and document-copy paths, choosing TransferFields or explicit assignments from the actual flow.
---

# Field propagation

Trace the field from its authoritative source to each required persisted destination. Use the target app's source and dependency symbols, not a static event-name catalog. Retain existing business transformations until their purpose is understood.

## Map the paths

For each requested path, record source, intermediate record, destination, copy point, later overwrites and persistence point. Include header versus line identity, partial posting, combined documents, archives, copy-document and reversal/correction paths when relevant. The [chain checklist](references/chain-checklist.md) gives useful starting points without assuming a particular publisher.

Decide what a value means when several source rows produce one target row, or one source row produces several entries. Copying an arbitrary current header/line is not a merge policy.

## Choose the transfer mechanism

| Observed code path | Approach |
|---|---|
| `TransferFields` copies the actual source to the actual destination before persistence, with no later overwrite | Use compatible field numbers/types where that fits the schema. No extra copy is needed for that path. |
| Explicit mapping or a different intermediate record | Use an existing transfer procedure or an event with the needed source and destination context. |
| Transformation or destination validation required | Assign or `Validate` intentionally at a point where subsequent base code will preserve the result. |

`TransferFields` matches **field numbers**, not names. Compatible types and sufficient target length matter; enum compatibility at runtime does not prove equal business meaning. Its primary-key option can replace destination key fields. It assigns values without executing field `OnValidate` triggers. See [TransferFields semantics](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/record/record-transferfields-table-boolean-method).

Explicit assignment does not require matching field IDs. Preserve existing field IDs and schema compatibility; do not renumber fields merely to make copying convenient. Avoid suppressing type mismatches to hide a schema error.

## Respect persistence and event timing

- Confirm the event's exact signature, `var` arguments, temporary state and position relative to insert/modify. Passing a record by value does not update the publisher's variable.
- A change to a `var` record before the publisher persists it usually needs no extra write. After persistence, determine whether the publisher later writes the record or an explicit modify is required.
- `Modify(false)` **does persist**; it skips the table `OnModify` trigger. It does not execute field validation. Choose validation and table triggers for the required behavior, not as a universal performance shortcut.
- A posting routine or event may execute more than once per document or line. Avoid counters, duplicate rows and irreversible side effects in a simple copy subscriber.
- Finding `TransferFields` nearby is not enough to remove a subscriber. Establish equivalent source, destination, ordering, transformation and validation before deleting it.

## Verify

Compile and exercise representative paths using different nonblank source values. Assert persisted destination values after reload, not only the in-memory event argument. Cover partial/multiple posting and rollback where affected. State which destinations and execution paths remain untested.
