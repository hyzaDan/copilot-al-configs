# RDLC layout changes

Read the actual report geometry and grouping before editing XML or using a designer. Do not substitute fixed margins, row heights or paper dimensions from an unrelated report.

## Geometry

- Keep body width plus left/right margins within page width. Include positioned items and nested tablix/rectangle widths; an off-page or hidden item can still affect pagination.
- Ensure each container's height covers the greatest child `Top + Height` plus intended padding. Check header/footer heights against the usable page height, not just the last-added textbox.
- Normalize units before calculating: 1 inch = 2.54 cm and 1 point = 1/72 inch. Font size is not a required row height; padding, wrapping and `CanGrow` can change rendered height.
- Rebalance columns according to content needs. Proportional shrinkage is an option, not a guarantee of legibility or fit; verify totals and accumulated rounding.
- Inspect group/page-break rules, keep-together behavior, repeated tablix headers and whitespace. Multi-document page numbering depends on group resets and the renderer; test the requested `Page X of Y` scope rather than assuming it is global or per document.

Microsoft's [pagination guidance](https://learn.microsoft.com/sql/reporting-services/report-design/pagination-in-reporting-services-report-builder-and-ssrs) explains the relationship between physical page size, margins and report items.

## Existing SetData/GetData patterns

Some BC RDLC layouts use custom embedded code to pass grouped values to headers/footers. Inspect that report's implementation: delimiter, indexing base, group identifiers, evaluation order and reset logic are not a universal platform contract.

Create a small index map before changing a positional payload. Appending new fields normally preserves existing consumers. Inserting/reordering is valid only if every affected `GetData` reference is updated consistently and verified. A shifted index can print the wrong customer's value without a compiler error.

Check escaping when payload values can contain the delimiter, and avoid carrying prior-document state into the next group. Test at least two documents with visibly different header values and a page break. Do not introduce a SetData mechanism into a layout that already has a simpler correct binding.
