# Model Routing and Symbol Research

## Recommended pattern

Use built-in Plan for design and Agent for implementation. Both can discover AL skills without a custom orchestrator. Use a separate worker only when context isolation, a different model, restricted tools, or independent work pays for the delegation overhead.

For symbol discovery:

```text
Parent (selected model)
  -> al-symbol-lookup skill
  -> small lookup: query directly with narrow filters
  -> large/repeated lookup: al-symbol-researcher (Terra)
       -> AL symbol tool / al-symbols-mcp
       -> exact relevant signatures + provenance + uncertainty
  -> parent designs/implements using that bounded result
```

The worker receives the raw tool responses in its context. The parent receives the worker's final result, not a replay of every response. The parent still pays for delegation input and the summary; the worker still consumes tokens. Narrow queries remain the first optimization. No cost or latency reduction is guaranteed without measuring the provider's billing, context forwarding, caching, and invocation overhead.

For English-to-Czech XLF work:

```text
Parent (selected implementation model, e.g. Astra)
  -> successful build evidence + selected cs-CZ scope
  -> al-translator (Luna)
       -> NAB XLF tools and raw translation-unit responses
       -> save en-US -> cs-CZ translations
  -> parent receives saved/remaining counts and ambiguities only
```

This is a required isolation boundary, not a size-based optimization: parent agents do not synchronize, enumerate, or save XLF translation units. If Luna or its tools are unavailable, report the blocked prerequisite instead of silently falling back to the parent model.

## Model configuration

VS Code documents `model` on custom agents, not on ordinary skills. A skill is instructions loaded by the executing model, not an independent model endpoint. Writing `model: Terra` in `SKILL.md` does not establish supported model routing.

The [symbol worker](../agents/al-symbol-researcher.agent.md) uses the same `GPT-5.6 Terra (unify-chat-provider)` identifier already used by this repository's developer/reviewer. The [translation worker](../agents/al-translator.agent.md) uses `GPT-5.6 Luna (unify-chat-provider)` for the isolated XLF boundary above. These are provider-specific configuration values, not a claim that these models are installed, cheaper, or suitable in every environment.

The worker allows `al-symbols-mcp/*` because the installed server's individual tool IDs are not established here. Its read-only instructions are not a sandbox: the wildcard permits whatever that server exposes. For enforced least privilege, inspect the installed tool list and replace the wildcard with the exact read-only lookup tools. The AL Language fallback is already limited to symbol search.

To change the worker model, select an exact available model identifier in the target VS Code installation and update the agent's `model`. VS Code also supports a prioritized model list. Keep fallbacks explicit: silently falling back to an expensive parent would defeat a strict cost budget. If the configured provider is unavailable, configure an available model before relying on this worker; omitting `model` inherits the selected model and does not promise savings.

Try Luna for bounded extraction only after checking signature accuracy on representative cases. Terra is the initial candidate here because its identifier already exists in the repository, not because a benchmark established superiority. Keep architecture, business semantics, and final integration validation with the parent model.

## Experimental forked skills

Current VS Code documentation also describes `context: fork` in skill frontmatter, gated by `github.copilot.chat.skillTool.enabled`. Only the final result returns from the forked context. This is experimental, does not document per-skill `model` selection, and should not be assumed portable to Copilot CLI or another host. This plugin therefore uses an explicit custom worker for model-specific isolation instead of depending on forked skills.

## Verify in the consuming workspace

1. Check customization diagnostics: skill discovery, worker registration, configured model, and tool availability. A missing tool in an agent allowlist can be ignored by the host; the declaration is not proof it is usable.
2. Confirm `al-symbols-mcp` or AL Language symbol search has the intended app/dependency version. Do not run package installation just to test routing without authorization.
3. Delegate a bounded question about a known event and compare returned parameters, `var` modifiers, access, and obsolete status with the source or authoritative symbols.
4. Confirm session diagnostics show the worker using the intended model. Compare total cost/latency and parent context size against a narrow inline query.
5. Test missing symbols, truncated search results, and ambiguous versions; the worker should report uncertainty, not invent an API.

No runtime model-routing or cost benchmark was performed as part of this repository-only migration.

## Sources

- [VS Code custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents): model selection, invocation controls, and tool allowlists.
- [VS Code agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills): supported metadata, progressive loading, and experimental forked context.

Checked on 2026-09-06. Recheck host support before relying on experimental fields or cross-runtime model selection.