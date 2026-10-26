---
name: bc-business-events-generator
description: Implement Business Central external business events for Power Automate or other consumers, including event contracts and transaction semantics.
---

# External business events

Use an external business event for a meaningful business transition. For ordinary AL extension hooks, use the appropriate AL event; an `IntegrationEvent` alone does not create an external event catalog entry. Check whether an existing catalog event already covers the requested transition.

## Establish the contract and source

1. Read the consuming manifest, dependency symbols and integration setup. `ExternalBusinessEvent` starts at AL runtime 11.0; that does not prove the required catalog, subscriber permissions or Dataverse components are configured. Check feature availability for the actual deployment.
2. Define precisely what happened, its company/entity identity, minimal payload and compatibility/version policy. Identify the consumer and the permissions needed to subscribe. Keep secrets and unnecessary personal/business details out of payloads.
3. Discover the source publisher and exact subscriber signature in [target symbols](../al-symbol-lookup/SKILL.md). Trace UI, API, batch, preview, cancellation and partial-posting paths relevant to the event. Do not fabricate a posting event or substitute a similarly named event without checking semantics.
4. Publish the empty-body external event procedure and invoke it only when the required transition occurred. Preserve transaction boundaries; do not add `Commit()` merely to accelerate a notification.

Read [event patterns and verification](references/event-patterns.md) for the concrete publisher shape, delivery boundary and stock-threshold decisions.

## Validate the whole route

Compile against the actual target. Exercise successful commit, rollback/preview, repeated invocation and the applicable non-UI entry point. Verify catalog discovery, authorized subscription and consumer receipt separately. Catalog refresh, tenant configuration, deployment and enabling a flow are external changes; execute them only within the user's requested scope.

Report source/event selection, payload, deduplication expectation, and which stages were observed. A local subscriber execution or catalog listing is not evidence of external delivery.
