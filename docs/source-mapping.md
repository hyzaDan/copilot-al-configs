# Source Mapping

This file maps the current Claude repository to the new Copilot repository.

## Taxonomy Mapping

### Worker Agents

These files describe execution personas and map directly to Copilot agents:

- `profile-al-development/agents/solution-architect.md` -> `agents/al-solution-architect.agent.md`
- `profile-al-development/agents/al-developer.md` -> `agents/al-developer.agent.md`
- `profile-al-development/agents/al-expert-reviewer.md` -> `agents/al-reviewer.agent.md`

Copilot-native worker additions that are not direct one-to-one Claude migrations:

- snapshot and profile runtime investigation -> `agents/al-snapshot-debugger.agent.md`

### Orchestrators

These files are not treated as skills by default. They are workflow entrypoints that coordinate other workers and now map primarily to orchestrator agents:

- `profile-al-development/commands/plan.md` -> `agents/al-plan-orchestrator.agent.md` plus thin launcher `templates/vscode-workspace/.github/prompts/plan.prompt.md`
- `profile-al-development/commands/develop.md` -> `agents/al-develop-orchestrator.agent.md` plus thin launcher `templates/vscode-workspace/.github/prompts/develop.prompt.md`
- `profile-al-development/commands/test.md` -> `agents/al-test-orchestrator.agent.md` plus thin launcher `templates/vscode-workspace/.github/prompts/test.prompt.md`
- `profile-al-development/commands/fix.md` -> `agents/al-fix-orchestrator.agent.md` plus thin launcher `templates/vscode-workspace/.github/prompts/fix.prompt.md`
- `profile-al-development/commands/interview.md` -> future interview orchestrator prompt

Thin VS Code launchers that target worker agents for direct UX:
- standalone review workflow -> `templates/vscode-workspace/.github/prompts/review.prompt.md` -> `agents/al-reviewer.agent.md`
- standalone translation workflow -> `templates/vscode-workspace/.github/prompts/translate.prompt.md` -> `agents/al-translator.agent.md`
- standalone snapshot investigation workflow -> `templates/vscode-workspace/.github/prompts/snapshot-debug.prompt.md` -> `agents/al-snapshot-debugger.agent.md`

### Skills

The goal is to extract true capabilities rather than role names:

- TDD rules and gating concepts -> `skills/al-tdd-discipline/`
- AL coding standards -> `skills/al-coding-standards/`
- reviewer checklist concepts -> `skills/al-bc-solution-review/`
- translation phase guidance -> `skills/al-translation-phase/`
- project-context bootstrap guidance -> `skills/al-project-context-bootstrap/`

## Content That Should Become Instructions

- AL coding standards from `profile-al-development/agents/al-developer.md`
- design constraints from `profile-al-development/agents/solution-architect.md`
- review criteria from reviewer agents

## Content That Should Stay Documentation

- workflow routing
- proportional planning rationale
- task coordination notes
- long-form migration rationale

## Content to Avoid Copying Directly

- Claude plugin marketplace setup
- Claude-only frontmatter fields
- duplicated architecture descriptions from older profile versions

## Runtime Notes

- Copilot CLI consumes plugin-root `agents/`, `skills/`, `.mcp.json`, and `hooks.json`.
- VS Code workspace customization should prefer `.github/instructions/` and optional thin `.github/prompts/` launchers.
- Root `agents/` is the canonical source for worker and orchestrator agents; local `.github/agents/` should exist only when a project needs explicit overrides.
