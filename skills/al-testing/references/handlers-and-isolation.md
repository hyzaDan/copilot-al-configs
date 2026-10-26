# Test handlers and isolation

- Use `Subtype = Test`, `[Test]` procedures, and the project's installed assertion/test libraries. Verify library signatures and supported handlers against its dependency symbols; these libraries are not bundled here.
- Keep Given/When/Then focused on the behavior. Expected rejection tests should assert the relevant error as well as absence of unintended writes; do not accept any unrelated error as success.
- Register required UI handlers with `[HandlerFunctions]`, match their actual signatures, and assert meaningful prompts/responses. Do not silence unexpected UI with catch-all handlers. Avoid real mail or external service calls; use the project's test seams.
- `TestIsolation` belongs to the test runner: `Disabled` (default) performs no automatic rollback; `Codeunit` rolls back after the codeunit; `Function` rolls back after each test method. The latter two roll back even explicitly committed database changes within that isolation scope. External services and session-level state are not thereby reset.
- Where supported, `RequiredTestIsolation` can express a test codeunit's minimum; verify target runtime support and runner compatibility. Inspect `TestPermissions` and the actual execution identity for least-privilege tests.
- Test fresh installation and upgrade by exercising their actual lifecycle paths in a disposable authorized environment. A test that merely calls a setup helper or finds an existing row does not prove installation behavior.

Sources: [TestIsolation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/properties/devenv-testisolation-property), [test codeunits](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-test-codeunits-and-test-methods), [handler methods](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-creating-handler-methods).
