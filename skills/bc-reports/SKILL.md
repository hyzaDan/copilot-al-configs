---
name: bc-reports
description: Create or modify Business Central reports, datasets, RDLC layouts and report-selection integration, with complete document joins and verification of rendered output.
---

# Business Central reports

Identify the report/dataset, intended document selection and rendering target. Preserve an existing layout type unless a change is requested or justified by the required output. Use RDLC for required pagination/layout behavior, Word for suitable editable document layouts and Excel for suitable analysis; none is a universal default.

Use the consuming app's IDs, layout organization, runtime and symbols. Prefer report extensions where supported and sufficient. Confirm whether the action should print the current document, selected rows or the current filtered set.

## Make the dataset correct first

Link child dataitems by the complete business identity. For `Sales Header` / `Sales Line`, both document type and number are required:

```al
DataItemLink = "Document Type" = field("Document Type"),
               "Document No." = field("No.");
```

Set `DataItemLinkReference` when the intended parent is not the default one. Choose an actual supported sort key consistent with the requested grouping; a sort order does not replace the join filters. See [report datasets and joins](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-report-dataset).

- Keep filters and grouping aligned with the document identity; equal numbers across types must not merge headers or lines.
- Calculate FlowFields/BLOBs on the record instance supplying the dataset after its relevant filters are set. Static company data can be loaded once; per-record data belongs at the appropriate iteration point. `OnPreReport` is not inherently wrong for a static logo.
- Prefer an image MIME type matching the actual bytes. Do not treat every BLOB as PNG or diagnose every red image placeholder as missing per-record calculation.
- Avoid repeated lookups for invariant data. Keep totals, signs, currency and rounding consistent with the document's business logic.
- Request-page defaults and `SaveValues` should match the workflow. A processing-only/internal report need not be exposed in Tell Me.

Inspect dataset-only output separately from rendering so incorrect values can be distinguished from layout problems.

## Load the relevant detail

- For RDLC changes, read [layout geometry and header data](references/rdlc-layout.md), especially when touching body width, page breaks or `SetData`/`GetData` expressions.
- For configurable report usages or current-document print actions, read [report selection](references/report-selection.md).

## Verify the result

Compile the AL and validate the layout file structure. Render the actual report with representative data: long text, empty/multiple lines, more than one page and a multi-document batch when supported. Check page breaks, repeated headers, totals, images, clipping and unwanted blank pages in the intended print/PDF output. Preview and a successful build do not establish physical print layout correctness; state the rendering checks actually performed.
