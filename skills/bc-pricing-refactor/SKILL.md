---
name: bc-pricing-refactor
description: Refactor Business Central legacy pricing customizations to price lists and the Price Calculation interfaces, including source mapping, custom fields, engine registration and behavioral regression cases.
---

# Pricing refactor

Identify the target BC version, installed dependencies, enabled pricing experience and existing calculation customizations. Feature availability and migration behavior vary by version; do not infer activation from a table's presence or prescribe a historical release boundary. Inspect the target symbols and actual calculation path.

## Choose the smallest relevant change

Inventory references to `Sales Price`, `Sales Line Discount`, purchase equivalents, legacy price calculation codeunits, pricing pages and migration subscribers. Classify them as data reads, writes, UI or calculation behavior.

| Need | Likely change |
|---|---|
| Move standard/custom price data | Map source records to `Price List Header` / `Price List Line`; preserve semantics and custom values. |
| Add a criterion or source | Extend the appropriate source/asset model and supported engine hooks. |
| Change the price algorithm | Implement a compatible `Price Calculation` handler when a smaller extension point cannot meet the behavior. |
| Expose custom fields | Extend the actual price-list pages and validation paths. |

Do not replace a working standard engine with a simplified `FindFirst` price lookup. Eligibility and best-price selection involve source, asset, price/amount type, status, dates, currency, variant, unit of measure, minimum quantity, discounts, VAT and rounding.

## Understand engine registration

The `Line With Price` abstraction supplies the document/journal context. `Price Calculation Mgt.` chooses an implementation through `Price Calculation Setup`, including method, type, product type, defaults and detailed exceptions. A new implementation is registered through the **Price Calculation Handler** enum and supported setup extension point. `Price Calculation Method` identifies the method; it is not a substitute for the implementation handler.

Copy the full interface contract from target symbols, including parameter direction and return values. An empty method that compiles is not a completed pricing implementation. Check setup registration for supported sales/purchase and asset combinations; do not replace the user's default engine just by registering a new option. See Microsoft's [price calculation extensibility model](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-extending-best-price-calculations).

For a new source type, inspect `Price Source`, the common source enum and the applicable sales/purchase/project subset and conversion paths. Extend only relevant domains and verify mappings; a visible enum value alone does not supply source resolution.

## Migrate and preserve meaning

Use [migration and regression decisions](references/migration-and-regression.md) when moving persisted data. Confirm what the target's standard feature migration actually transfers before adding custom migration code. Discover the real publisher and whether its destination is already inserted; do not invent event names or append `Modify(false)` indiscriminately.

Price-list headers provide defaults, while supported line overrides depend on fields and settings in the target version. Do not impose a blanket one-currency-per-header rule without checking those semantics. Validate and activate lists through the supported business operations rather than merely changing a status field.

Feature enablement and production data migration are separate external actions requiring the user's task scope. Describe a tested rollout and recovery path when requested; source edits and compilation do not establish that migration or activation occurred.

## Verify

Compare old and intended new outcomes using identical document context. Include overlapping candidates, missing candidates, date/quantity boundaries, currency/UOM changes, discounts and user-entered prices. Check custom source selection, engine defaults/exceptions and migration reruns. Report the target symbols used, compiled code and executed pricing scenarios separately.
