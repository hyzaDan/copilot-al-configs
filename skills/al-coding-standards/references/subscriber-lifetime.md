# Subscriber lifetime

`EventSubscriberInstance = StaticAutomatic` is the default. With `SingleInstance = false` (also default), each subscriber invocation uses its own codeunit instance, disposed afterwards. With `SingleInstance = true`, the instance is retained for the client/company context, including globals. Manual binding has a different lifetime tied to the bound instance; inspect `BindSubscription` and unbinding rather than applying static assumptions.

Choose retained state only deliberately. Check stale caches, operation-specific flags, error paths and company/session boundaries. A stateless subscriber needs no invented exception rationale for the platform default. Measured instantiation cost may justify optimization; the property alone proves no performance benefit.

When reviewing an existing project with an explicit different policy, distinguish a convention deviation from runtime correctness. Do not rewrite unrelated handlers to enforce this package's historical preference.

Sources: [SingleInstance](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/properties/devenv-singleinstance-property), [EventSubscriberInstance](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/properties/devenv-eventsubscriberinstance-property).
