# Taxonomy

Default workflow: built-in Plan for planning, built-in Agent for implementation. Custom agents are optional, not mandatory workflow phases.

## Concepts

### Instructions

Always-on or file-targeted guidance.

Examples:
- global AL standards
- test-specific conventions
- project-specific naming and translation rules

### Custom Agents

Use for context isolation, model selection, or tool restrictions. The body links to skills rather than copying their procedures.

- `al-reviewer`: independent read-only review.
- `al-snapshot-debugger`: isolated read-only runtime artifact analysis.
- `al-translator`: selected-language translation with a restricted tool set.
- `al-symbol-researcher`: bounded dependency lookup with concise evidence returned to the parent.
- `al-developer`: optional worker for an independently owned module.

Develop/fix/test orchestrators remain manual compatibility entrypoints with automatic model invocation disabled. They do not require workers, worker counts, or mandatory reviewer sign-off. The old planner/architect in `Backup/` are historical and are not shipped from `agents/`.

### Prompt Files

Optional user-invoked shortcuts in the workspace overlay. They select built-in modes and describe the task, not an orchestration contract. They do not install or embed skills.

### Skills

Portable capabilities that can be loaded on demand across Codex and Copilot runtimes, subject to the workflow's tooling prerequisites.

Examples:
- AL build and test workflows
- AL coding standards
- review checklist
- translation phase guidance
- project context bootstrap

## Runtime Mapping

### Plugin root

Use plugin root for shared runtime assets:
- `plugin.json` for the portable manifest and OpenAI presentation metadata
- `mcp.json` for portable MCP connections
- `.codex-plugin/plugin.json` for the Codex compatibility layout
- `.agents/plugins/marketplace.json` for Codex discovery; its source path resolves from the repository root
- `agents/` for optional workers and compatibility entrypoints
- `skills/`
- `.mcp.json` for Copilot and the Codex compatibility layout
- `hooks.json`

The Codex package registers shared skills and MCP connections. Copilot `.agent.md` files and their provider-specific model settings require a separate host integration. In particular, the translation skill requires its isolated worker; see the [Codex prerequisites](../README.md#czech-translation).

### VS Code workspace templates

Use `templates/vscode-workspace/.github/` for target-project customization:
- `copilot-instructions.md`
- `prompts/` for thin workflow launchers when helpful for UX
- local `.github/agents/` only for project-specific overrides, not as the default mirrored source

## Anti-patterns

Avoid:
- mandatory orchestration for ordinary edits
- treating a checklist as a separate persona
- broad skill descriptions that match every AL task
- loading all skill references or mapping the entire repository before a local change
- assigning `model` to a skill and assuming it changes the executing model
- copying tool schemas or general model behavior into every agent
- confusing team preferences with compiler/AppSource requirements

Keep long or exceptional procedures in linked references. Short focused review skills can remain single files; progressive disclosure does not require splitting every checklist.
