# copilot-al-configs

AL development configuration for GitHub Copilot CLI and VS Code Insiders.

This repository keeps its runtime assets at the repository root.

For GitHub Copilot CLI, the official manifest locations are `.github/plugin/plugin.json` and `.github/plugin/marketplace.json`.

This repository also keeps matching `.claude-plugin/` manifests as a compatibility fallback for runtimes that still probe the legacy path.

Install targets:
- Direct plugin install: `copilot plugin install hyzaDan/copilot-al-configs`
- Marketplace add: `copilot plugin marketplace add hyzaDan/copilot-al-configs`
- Git URL: `https://github.com/hyzaDan/copilot-al-configs`
