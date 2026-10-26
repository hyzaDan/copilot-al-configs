# Propagation chain checklist

Use only the branches relevant to the requested field. These are discovery starting points, not guaranteed `TransferFields` paths or subscriber signatures.

| Business flow | Records to trace |
|---|---|
| Sales | Header/line to shipment, invoice, credit memo, return receipt and archive; then journal/ledger records only if the field belongs there. |
| Purchase | Header/line to receipt, invoice, credit memo, return shipment and archive. |
| Item posting | Document line to Item Journal Line, then Item Ledger Entry, Value Entry and capacity entries as applicable. Value entries may be created again by cost adjustment. |
| Financial posting | Document/header to Gen. Journal Line, then G/L and customer/vendor entries; account for balancing and summarized entries. |
| Transfer/warehouse | Source line, shipment/receipt or warehouse document, posted counterpart and item journal; track split quantities and line mapping. |
| Archive/copy/correction | Source version and line identity, new record initialization, reverse sign or reset rules, and whether the custom value is historical evidence or editable input. |

For every edge, answer:

1. Which source value is authoritative at this moment, and can it be blank intentionally?
2. Is the target new, temporary, already persisted, aggregated or reused in a loop?
3. Does the existing copy include the custom field, and can later code overwrite it?
4. Which operation persists it, with which field/table validation?
5. Does a failed transaction roll back the value and any auxiliary writes?

Keep a concise source-to-destination map with the implementation when several paths are involved. Do not add unused ledger fields simply because those tables appear in this checklist.
