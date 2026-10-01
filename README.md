# copilot-al-configs

AL and Business Central development skills and MCP tools for Codex, GitHub Copilot CLI, and VS Code Insiders.

Version `0.1.1` packages 11 shared skills and three MCP connections. Runtime assets stay at the repository root.

## Install in Codex

From this repository's root, using a Codex CLI with `plugin marketplace` and `plugin add` support:

```powershell
codex plugin marketplace add .
codex plugin list --marketplace copilot-al-configs --available --json
codex plugin add copilot-al-configs@copilot-al-configs
```

Start a new Codex session after installation. In the desktop app, restart the app and look for **AL Development** in the **AL Development Plugins** marketplace. Verify that the skills and MCP tools are available in the consuming AL project.

Once these files have been pushed to GitHub, the Git-backed installation is:

```powershell
codex plugin marketplace add hyzaDan/copilot-al-configs --ref main
codex plugin add copilot-al-configs@copilot-al-configs
```

For a local source, edit this repository, then reinstall or refresh the plugin using the consuming host's supported flow; restart the desktop app and start a new session. For a Git-backed source, first run `codex plugin marketplace upgrade copilot-al-configs` to fetch the updated Git snapshot, then refresh the installed plugin. Codex loads an installed cache copy; editing the source does not update an already running session.

The repo marketplace makes the plugin discoverable. Installation and enablement are host settings; this repository does not automatically enable it in every project.

## Install in GitHub Copilot

Copilot manifests remain in `.github/plugin/`, with matching `.claude-plugin/` manifests for legacy discovery.

- Direct plugin install: `copilot plugin install hyzaDan/copilot-al-configs`
- Marketplace add: `copilot plugin marketplace add hyzaDan/copilot-al-configs`
- Git URL: `https://github.com/hyzaDan/copilot-al-configs`

## Package layout

| Path | Purpose |
| --- | --- |
| `plugin.json` | Portable Agent Plugins 1.0 manifest and OpenAI presentation metadata |
| `mcp.json` | Portable MCP configuration, with explicit transport types |
| `skills/` | Shared skills and their supporting references |
| `.codex-plugin/plugin.json` | Codex compatibility manifest for clients using the older layout |
| `.agents/plugins/marketplace.json` | Codex marketplace pointing to the plugin at the repository root |
| `.mcp.json` | Legacy MCP configuration for Copilot and the Codex compatibility layout |
| `.github/plugin/`, `.claude-plugin/` | Copilot and legacy plugin/marketplace manifests |
| `agents/` | Optional Copilot custom agents |

Portable clients discover `skills/` and `mcp.json` automatically. Keep plugin identity/version synchronized across manifests, and keep the MCP server names, commands, arguments, and endpoints equivalent in `mcp.json` and `.mcp.json`; portable HTTP transport is `streamable-http`, while the legacy file uses `http`.

See the official [OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins) for the portable format, compatibility manifests, and marketplace behavior.

## MCP servers and prerequisites

| Server | Connection | Prerequisites |
| --- | --- | --- |
| `al-symbols-mcp` | Local stdio: `npx -y al-mcp-server` | Node.js/npm with `npx` on PATH, initial npm registry access, and the consuming project's AL symbols |
| `context7` | Streamable HTTP: `https://mcp.context7.com/mcp` | Network access; service access/rate limits apply |
| `microsoft.docs.mcp` | Streamable HTTP: `https://learn.microsoft.com/api/mcp` | Network access |

These are connections to existing servers. The plugin does not host or deploy a new MCP service. Keep the consuming AL project's context explicit when querying symbols; installing the plugin alone does not provide its `.app` dependencies.

Build validation requires an available AL compiler/build tool. Runtime tests require the project's configured runner and an identified BC test environment. AL Language and NAB editor tools are separate host capabilities, not servers bundled by this plugin.

### Czech translation

`al-translation-phase` preserves the English-to-Czech workflow and its required isolated `al-translator` worker. That worker is currently defined as a Copilot custom agent with a provider-specific model and NAB tool allowlist. The Codex package declares skills and MCP connections; it does not register the Copilot agents or their model settings.

To execute translation in Codex, the consuming environment must provide an equivalent worker and the required translation tools. Until that integration exists, the skill reports the missing prerequisite. Its XML-editing fallback still runs within the required worker. It must not silently translate in the parent context. See [model routing](docs/model-routing.md).

## Daily use

Use the host's built-in planning and execution modes. AL skills load on demand; no custom orchestrator or full project bootstrap is required for every edit. Verify discovery in the consuming host's plugin/skill diagnostics.

## Skills and optional agents

- Design and implementation: architecture and coding standards.
- Diagnosis and validation: debugging (with snapshot/profile reference), build validation, and AL testing.
- Review: solution review, with performance/security skills only when relevant.
- Tool workflows: symbol lookup and XLF translation.
- Onboarding: project context bootstrap, not an always-on prerequisite.

In Copilot, custom agents are useful for isolated review, runtime artifact analysis, translation, or bounded symbol research. Existing develop/fix/test orchestrator names remain as manual compatibility entrypoints and disable automatic model invocation. The developer and symbol-research workers are hidden from the picker and remain available for delegation in that host.

The symbol worker uses the repository's existing Terra provider identifier. This is not a portable guarantee of model availability or lower cost. See [model routing](docs/model-routing.md) for configuration, forked skills, and verification steps.

See [taxonomy](docs/taxonomy.md) for ownership and [the skill-first audit](docs/skill-first-audit.md) for the earlier Copilot migration. Historical migration documents are not runtime workflow dependencies.

## Verify in a consuming project

1. Confirm **AL Development** is enabled and the 11 skill names are discoverable in a new session.
2. Confirm the three MCP servers initialize and list tools. Make a small documentation query and a bounded symbol query for the intended AL project.
3. Exercise build/test skills only with the actual compiler, runner, and authorized BC environment available.
4. Exercise translation only after the isolated worker and translation tools have been integrated.

Configuration validation and MCP discovery are separate from AL compilation, executed BC tests, and translation. This repository has no BC app or runtime test fixture.
