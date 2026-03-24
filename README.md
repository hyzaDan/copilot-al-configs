# copilot-al-configs

AL development configuration for GitHub Copilot CLI and VS Code Insiders.

This repository keeps its runtime assets at the repository root.

For Git-based plugin installation, Copilot currently uses a compatibility layer that may treat a GitHub repository either as a direct plugin source or as a plugin marketplace. Because of that, this repository includes both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` while keeping the root layout unchanged.

Git install targets:
- Repository root: `hyzaDan/copilot-al-configs`
- Full URL: `https://github.com/hyzaDan/copilot-al-configs`

CLI fallback:
- `/plugin install hyzaDan/copilot-al-configs`
