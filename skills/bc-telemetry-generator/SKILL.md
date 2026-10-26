---
name: bc-telemetry-generator
description: Add Business Central AL telemetry and matching KQL with stable event schemas, minimal payloads and explicit metric units.
---

# AL telemetry and matching queries

Define the diagnostic question first: what event or measurement would distinguish the relevant outcomes? Reuse existing platform/feature telemetry when it already answers that question. Add a helper only when it usefully centralizes a repeated contract.

## Event contract

- Give each event a stable project-unique identifier, fixed meaning, severity, dimension names/types/units and owner. Renaming a dimension can break dashboards; evolve the contract deliberately.
- Keep messages static and dimensions limited to technical values needed for diagnosis. Raw error text, URLs with parameters, tokens, names, company/customer/document identifiers and user-entered values are not automatically `SystemMetadata`. Remove sensitive data at the producer; changing the classification alone does not provide a working custom telemetry pipeline.
- Use allowlisted failure categories or codes instead of `GetLastErrorText()` as a dimension. A hash of a business identifier may remain linkable sensitive data; prefer omission unless correlation is required and justified.
- Select `TelemetryScope` for the actual authorized destination. `ExtensionPublisher` and `All` send to different configured resources; do not default all integrations to the broadest scope.
- Verify the runtime's `Session.LogMessage` or feature-telemetry API. Define numeric units explicitly and serialize numeric values culture-independently. `Format(Duration)` produces display text, not a millisecond counter.

Read [producer and KQL](references/producer-and-kql.md) for a matching numerical example and the platform's `AL`/`al` prefixes.

## Verification

Compile the producer and inspect the payload before emission. In an authorized configured environment, confirm a known event arrives at the intended resource, inspect actual dimension names/types, and run the matching query. Exercise at least two locales, success/failure paths and missing/malformed metrics. Distinguish source compilation, successful emission and query results. Do not provision telemetry resources or widen destinations merely to validate source changes.
