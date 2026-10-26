# Event pattern and semantics

For a target exposing `EventCategory::Sales`, the following method illustrates a small external event contract. The category and procedure name must fit the consuming project; omit customer names and document numbers when the consumer can resolve the record by ID.

```al
[ExternalBusinessEvent('salesdocumentready', 'Sales document ready',
    'A sales document reached the agreed ready state.', EventCategory::Sales)]
procedure SalesDocumentReady(DocumentId: Guid)
begin
end;
```

The body is intentionally empty: invoking the method raises the external event. Supply an existing or project-defined category, and consider `RequiredPermissions` where the subscription requires additional table permissions. Resolve that attribute and enum from target symbols. The subscriber that calls this procedure depends on the actual business transition; no generic posting signature is supplied here.

## Transaction boundary

The documented platform behavior sends notifications after the current transaction commits. A rollback prevents the notification; a long transaction delays it. A publisher reached before later posting validation can still be rolled back. Do not confuse notification scheduling with the consumer's successful processing.

Define consumer deduplication using a stable occurrence identity appropriate to the operation. A record GUID alone is insufficient when the same record legitimately emits the event multiple times. Do not promise exactly-once delivery or infer ordering from the local call sequence without target-specific evidence.

## Stock thresholds

An item modification is not a dependable signal of inventory movement. `Inventory` is a FlowField, and calculating it does not make the item's modify trigger the correct publisher.

For a requested threshold crossing:

- Choose the relevant movement/ledger lifecycle and location, variant and date filters.
- Establish the business quantity (physical, available, projected, or another defined measure).
- Calculate the FlowField with those filters at the chosen point, or use the appropriate ledger query.
- Compare a durable prior threshold state with the new state so unrelated changes and repeated movements do not emit duplicate crossings. Decide how concurrent postings serialize that transition and how reversal/recovery behaves.
- Test both crossing directions, partial posting, rollback and concurrent movements. Do not add a transaction commit to make the quantity appear final.

## Primary sources

- [ExternalBusinessEvent attribute](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/attributes/devenv-externalbusinessevent-attribute): supported syntax and runtime.
- [Business events overview](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/business-events-overview): catalog, configuration, empty-body publishers and commit/rollback behavior. The article includes preview limitations; verify current target support instead of freezing its example component versions.
- [FlowFields overview](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-flowfields): calculated-field behavior.
