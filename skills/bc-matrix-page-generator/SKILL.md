---
name: bc-matrix-page-generator
description: Design and implement Business Central matrix pages with entity/period axes, bounded column slots, navigation, aggregation, drilldown and optional matching Excel export.
---

# Matrix pages

Resolve the row axis, column axis, measures, filters, period definition and required editability from the task and existing pages. Reuse available answers. Choose temporary versus persisted buffers based on reuse, volume and ownership; do not create persistent calculated data merely to display a page.

## Represent the axes explicitly

AL page controls are declared at compile time. A dynamic matrix normally binds a bounded set of column controls to values, captions and visibility for the current window; runtime data does not create an arbitrary number of page fields.

- Give each row and column a stable key plus display order. Use a deterministic tie-breaker when ranking entities, so equal totals do not jump between pages.
- Keep the visible slot index separate from the underlying entity/period key. Navigation changes the mapping, not the meaning of the measure.
- At a partial last window, clear unused captions, values, drilldown keys and visibility. Handle zero rows/columns and first/last navigation explicitly.
- Reset or clamp the window after filters change; a previously valid offset may no longer exist.

The target application's `Matrix Management` codeunit or existing matrix pages can provide compatible navigation patterns. Inspect their symbols and semantics before reuse; they are not a promise of an arbitrary dynamic-column framework.

## Define periods and aggregation

Use explicit period start/end boundaries and the intended business calendar: ISO-style weeks, calendar months and accounting periods are not interchangeable. Handle partial first/last periods, leap days and inclusive AL date filters. For language-independent formulas, use supported `DateFormula`/`CalcDate` behavior rather than localized formula text; see [CalcDate](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/methods-auto/system/system-calcdate-dateformula-date-method).

Aggregate by the complete row key, column key and measure. Distinguish no data from zero when the business meaning differs. Totals for balances, ratios or averages may require independent aggregation; do not automatically sum displayed cells. Include currency/unit conversions and rounding only where defined by the measure.

## Bound the work

- Use a query, aggregation or indexed buffer appropriate to the volume. Keep `OnAfterGetRecord` limited to loading the current row's visible values; avoid rebuilding the whole matrix per row.
- For a bounded dataset, calculate once and page over the buffer. For a large dataset, calculate/cache bounded windows instead of materializing everything; invalidate cached values when their input filters change.
- Prevent one unbounded source scan per cell. Estimate rows × columns and choose keys/aggregation before adding UI pagination.
- Temporary records avoid persistent cleanup but still consume memory. Shared persistent buffers require explicit ownership, freshness and cleanup behavior.

## Keep actions consistent

Drilldown must reconstruct the same entity, period and business filters used for its cell. If cells are editable, define the actual write target and validation/locking; an aggregate is not directly editable without an allocation rule.

For requested Excel export, reuse the matrix's axis definitions and calculation logic. State whether export covers the current window or all filtered columns. Preserve headers, ordering, number formats and totals, and bound memory for large exports. A normalized table is a different output and should be chosen intentionally.

Verify first/last/partial windows, changed filters, period edges, non-additive totals, drilldown and export agreement with the displayed values. Compile and test the actual page; a design checklist alone is not a completed matrix implementation.
