# Instruction checks

- An agent retains action/search history but not a complete snapshot of every visited page. Explicitly memorize essential key/value pairs before navigating away when later steps need them. Do not assert that all context always disappears.
- Microsoft's documented phrases include `Memorize`, `Set field`, `Use lookup`, `Invoke action`, `Ask for assistance`, `Request a review`, and `Reply`. They help tool use; spelling/format is not a fabricated hard grammar. Match page/action/field names to the actual profile and serialized UI. An unverified name needs evidence, not an automatic blocking finding.
- Keep responsibilities and cross-task rules consistent with ordered task steps. Stop/retry paths must have a meaningful exit and retain the intended record identity. Permissions/profile limitations need configuration or design changes; instruction prose cannot grant access.
- Test guard polarity with at least one permitted and one rejected case. For a required nonblank value: if blank, request the value and stop the dependent action; otherwise continue. Never correct this into “continue when blank.” Preserve business semantics for credit, approval and posting conditions.
- Retain the target agent's review boundary for critical actions/outgoing communications. The current Microsoft BC-agent documentation describes review before outgoing messages; verify target capability/version rather than inferring that a drafted message was sent.

Use the target task timeline to distinguish navigation failure, inaccessible UI, missing data, wrong branch and instruction ambiguity. A static walkthrough provides candidate causes; successful runtime verification requires observed task outcomes.

Sources checked 2026-10-23: [instruction guidance](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/ai/ai-development-toolkit-instructions), [keywords and history](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/ai/ai-development-toolkit-instruction-keywords). These pages describe evolving/preview capabilities; recheck the target version and enabled environment.
