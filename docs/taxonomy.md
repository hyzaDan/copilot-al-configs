# Taxonomy

This repository separates conceptual roles from runtime representation.

## Concepts

### Instructions

Always-on or file-targeted guidance.

Examples:
- global AL standards
- test-specific conventions
- project-specific naming and translation rules

### Worker Agents

Execution personas that perform focused work.

Examples:
- `al-solution-architect`
- `al-developer`
- `al-reviewer`

### Orchestrators

Workflow entrypoints that coordinate phases, workers, or approvals.

Examples:
- planning workflow
- development workflow
- testing workflow
- quick-fix workflow

Canonical runtime representation:
- orchestrator agents in `agents/`
- optional thin prompt launchers in `templates/vscode-workspace/.github/prompts/`
- local workspace agents only when a project needs explicit overrides

Prompt launchers are primarily for orchestrators, but the workspace overlay may also expose thin worker launchers when that improves direct UX for common standalone tasks such as review or translation.

### Skills

Portable capabilities that can be loaded on demand across Copilot runtimes.

Examples:
- TDD discipline
- AL coding standards
- review checklist
- translation phase guidance
- project context bootstrap

## Runtime Mapping

### Plugin root

Use plugin root for shared runtime assets consumed by Copilot CLI and Copilot plugin loading:
- `agents/` for worker agents and orchestrator agents
- `skills/`
- `.mcp.json`
- `hooks.json`

### VS Code workspace templates

Use `templates/vscode-workspace/.github/` for target-project customization:
- `copilot-instructions.md`
- `instructions/`
- `prompts/` for thin workflow launchers when helpful for UX
- local `.github/agents/` only for project-specific overrides, not as the default mirrored source

## Anti-patterns

Avoid these migrations:
- treating orchestration workflows as if they were just lightweight skills
- treating checklists as worker personas
- treating prompt wrappers as the canonical owner of workflow behavior
- copying Claude-specific frontmatter and tool labels directly
- mixing always-on policy text into every agent body instead of instructions or skills
