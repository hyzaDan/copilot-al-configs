---
name: bc-attachments-generator
description: Integrate Business Central document attachments, links and notes with custom entities, including complete record-key mapping and safe delete, rename and posting behavior.
---

# Attachments, links and notes

Use the standard attachment infrastructure supported by the consuming app's symbols. Check whether the target entity is already supported before adding mapping subscribers. Allocate only the objects actually needed; visibility settings and new enum values are optional design choices.

## Establish identity before writing lifecycle code

Map the source's complete primary key to the attachment owner identity. Standard `Document Attachment` uses fields including `Table ID`, `No.`, `Document Type` and `Line No.`; inspect additional keys and mapping used for the target entity. See the [table contract](https://learn.microsoft.com/dynamics365/business-central/application/base-application/table/microsoft.foundation.attachment.document-attachment).

- A master record may need only table and number, with explicit neutral type/line values. A header and its lines must remain distinct. Equal numbers on an order and invoice must not collide.
- Use the same owner mapping for creation, FactBox filtering, details, opening the source record, copy, rename and delete. Centralize it where practical so these paths cannot drift.
- If the custom composite key cannot be represented losslessly, design a supported stable mapping or extension. Truncating a key or treating its first field as `No.` is not a solution.
- A source row must have a durable identity before attaching persistent content; define the behavior for unsaved or temporary records.

## Wire the UI and mapping

Inspect the current attachment FactBox/detail page and table publishers for source `RecordRef` resolution and initialization. Generate only subscribers needed by this table, with exact target signatures and a table-type guard. Resolve page controls by their declared names in the target symbols; do not assume control numbers from a different page.

Match the FactBox `SubPageLink` to the full owner mapping and test navigation between rows. Links and notes use record-link identity, not the document attachment's number/type mapping; handle them separately when they are in scope. Their visibility does not grant or revoke data access. Microsoft's [attachment UI overview](https://learn.microsoft.com/dynamics365/business-central/ui-how-add-link-to-record) distinguishes these attachment types and document flow behavior.

## Preserve ownership through changes

- Prefer existing standard copy/delete/rename helpers when they support this entity. Verify their filtering and trigger behavior before calling them.
- Before deleting attachments, filter by every owner discriminator, including the line value even for a header. Avoid broad `DeleteAll` based only on table and number for document tables.
- Rename should preserve the attachment content and metadata for exactly the renamed owner, transactionally with the source change. Do not blindly implement rename as copy-and-delete: duplicate IDs, media ownership and rollback need verified semantics.
- Posting/copying may create a different document type or split source lines. Define destination mapping, duplicate prevention and whether the source keeps its attachment. Respect standard document-flow options where applicable.
- Do not commit inside a lifecycle subscriber or act on temporary records. Choose trigger execution to preserve the attachment API's cleanup behavior.

## Verify

Use two documents with the same number and different types, plus separate header and line attachments. Confirm upload, navigation, source opening, rename, delete, rollback and any requested posting/copy flow affect only the intended owner. Check restricted users can perform the intended actions without gaining broader attachment access. Compilation alone does not prove ownership or media cleanup.
