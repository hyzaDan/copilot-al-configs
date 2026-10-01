# copilot-al-configs

AL development configuration for GitHub Copilot CLI and VS Code Insiders.

This repository keeps its runtime assets at the repository root.

For GitHub Copilot CLI, the official manifest locations are `.github/plugin/plugin.json` and `.github/plugin/marketplace.json`.

This repository also keeps matching `.claude-plugin/` manifests as a compatibility fallback for runtimes that still probe the legacy path.

Install targets:
- Direct plugin install: `copilot plugin install hyzaDan/copilot-al-configs`
- Marketplace add: `copilot plugin marketplace add hyzaDan/copilot-al-configs`
- Git URL: `https://github.com/hyzaDan/copilot-al-configs`

## Daily use

Use built-in **Plan** for design and **Agent** for implementation, fixes, and tests. AL skills load on demand; no custom orchestrator or full project bootstrap is required for every edit.

The optional prompt files in `templates/vscode-workspace/.github/prompts/` select these built-in modes. Copy the workspace overlay only when you want those shortcuts and project-specific instructions. Installing the plugin does not automatically copy the overlay into your project. Verify skill/agent discovery in the consuming host's customization diagnostics.

## Skills and optional agents

- Design and implementation: architecture and coding standards.
- Diagnosis and validation: debugging (with snapshot/profile reference), build validation, and AL testing.
- Review: solution review, with performance/security skills only when relevant.
- Tool workflows: symbol lookup and XLF translation.
- Onboarding: project context bootstrap, not an always-on prerequisite.

Custom agents are useful for isolated review, runtime artifact analysis, translation, or bounded symbol research. Existing develop/fix/test orchestrator names remain as manual compatibility entrypoints and disable automatic model invocation. The developer and symbol-research workers are hidden from the picker and remain available for delegation.

The symbol worker uses the repository's existing Terra provider identifier. This is not a portable guarantee of model availability or lower cost. See [model routing](docs/model-routing.md) for configuration, forked skills, and verification steps.

See [taxonomy](docs/taxonomy.md) for ownership and [the skill-first audit](docs/skill-first-audit.md) for what was removed, retained, and left unverified. `Backup/` and the original migration document are historical, not runtime workflow dependencies.
