# Pricing migration and regression

Preserve the business key of each legacy price/discount record. Do not identify a destination using only item and customer: price type, source type/number, asset, variant, currency, unit of measure, minimum quantity, date range and amount type can distinguish separate rules.

Map custom values at the supported migration/copy point, where source and destination context are both available. Preserve explicit zeros and blanks when meaningful. Define a conflict policy if a matching price-list line already exists; migration reruns must not duplicate rows or overwrite newer customer changes silently.

Check the target's standard feature migration and its extension events for both price and discount paths. Keep a count/key reconciliation for legacy rows, resulting rows and rejected/conflicting rows. A passing count alone does not prove every rule retained its value or applicability.

For each changed calculation, use representative cases:

- Customer-specific and group/all-customer rules compete; verify the actual best-price and discount rules, without assuming a universal customer-first fallback order.
- Sales and purchase, item/resource/other relevant asset types, variants and units of measure remain separate.
- Starting/ending dates and minimum quantities are tested at the boundary and immediately outside it.
- Currency, VAT-inclusive amounts and rounding yield the intended document amounts.
- Draft/inactive versus active lists, line overrides and overlapping/duplicate candidates behave as intended.
- Changing customer, item, quantity, date or currency causes appropriate recalculation; manually entered prices/discounts retain the intended protection.

The functional [prices and discounts guide](https://learn.microsoft.com/dynamics365/business-central/across-prices-and-discounts) supplies the business behavior to compare with the target environment. Test the actual line calculation entry point, not only a custom lookup helper.
