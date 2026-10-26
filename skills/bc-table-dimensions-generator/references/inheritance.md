# Dimension inheritance decisions

Choose the source rule from the business requirement; these strategies are not interchangeable.

| Rule | Implementation shape |
|---|---|
| Several sources contribute | Build the complete source list, including unchanged fields, and use the target's standard merge/default-priority path with the correct source code. |
| One source wins, with fallback | Resolve the highest-priority available source explicitly and recompute when any field in that chain changes, including when the primary source is cleared. |
| Header dimensions plus line defaults | Supply the inherited parent set and the line's sources through the supported dimension-management operation, preserving the intended conflict priorities. |

For standard merging, inspect `AddDimSource` and `GetRecDefaultDimID` or the supported equivalent. The complete source list prevents contributions from unchanged fields from disappearing. Source ordering/current-field context can affect the result; follow the target standard pattern, not a guessed parameter list.

Define the outcome when every source is blank and when a source changes after a user manually edited dimensions. Recompute, preserve and clear are different behaviors. Refresh globals from the final set, even if no sources remain.

## Header-to-line changes

Capture the old header set before editing. For lines that carry their own dimensions, consider `GetDeltaDimSetID(LineSet, NewHeaderSet, OldHeaderSet)` to apply the parent change while preserving line-specific dimensions. Verify the target helper's semantics for conflicting dimensions and validate the resulting combinations. Directly replacing every line set with the new header set discards line contributions.

Filter lines by the complete parent identity. For each affected line, update its set and global fields together, with the intended business validation. Apply the requested interaction rule: an interactive confirmation, silent configured policy or a returned conflict for a non-UI caller. Do not call UI confirmation from an unconditional table/API path.

Test two lines with different additional dimensions, a changed/removed header dimension, a source-priority conflict and a line that should remain untouched. An unchanged header set should not trigger unnecessary cascading writes.
