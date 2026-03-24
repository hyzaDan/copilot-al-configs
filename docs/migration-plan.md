# Migration Plan

## Goal

Create a Copilot-native repository that is separate from the Claude repository while preserving the strongest AL workflow concepts.

## Target Strategy

- Keep `claude-configs` unchanged as the Claude-specific source.
- Build `copilot-al-configs` as a shared repository for:
  - GitHub Copilot CLI
  - GitHub Copilot VS Code Insiders
- Put shared runtime assets, including agents, in the plugin root.
- Put workspace-level VS Code overlay files in `templates/vscode-workspace/`.

## Taxonomy

The migration uses a stricter vocabulary than the original Claude repository:

- `instructions`: always-on or file-targeted guidance
- `worker agents`: execution personas such as architect, developer, reviewer
- `orchestrators`: workflow entrypoints that coordinate multiple workers or phases
- `skills`: portable capabilities that can be loaded on demand across Copilot runtimes

The old Claude `commands/` directory is treated mainly as orchestration source material, not as a direct skill catalog.

## Phase 1

Focus on the smallest useful slice:
- planning worker + planning orchestrator
- implementation worker + development orchestrator
- review worker
- AL coding standards
- TDD guidance

## Phase 2

Add:
- specialized reviewers
- portable skills for TDD, review, translation, and context bootstrap
- MCP server definitions
- richer VS Code prompt wrappers

## Phase 3

Add:
- expanded test agents
- documentation workflows
- optional hooks and automation

## Content Rules

Migrate concepts, not Claude-specific syntax.

Drop or rewrite these during migration:
- `allowed-tools`
- `capabilities`
- Claude model labels such as `opus` and `sonnet`
- Claude-only workflow wording like `AskUserQuestion` where Copilot-native prompts or tools should be used instead

Reclassify these during migration:
- worker-style Claude agents -> Copilot custom agents
- orchestration-style Claude commands -> orchestrator agents plus thin VS Code prompt launchers
- reusable checklists and procedures -> Copilot skills

Keep and adapt these:
- AL standards
- BC design constraints
- TDD discipline
- review checklists
- workflow boundaries between planning, coding, and review

## Current Vertical Slice

The first implemented vertical slice covers:
- `solution-architect` as a real worker agent
- `al-developer` as a real worker agent
- `al-reviewer` as a real review agent
- `translator` as a dedicated translation worker agent
- `snapshot-debugger` as a dedicated runtime artifact analysis worker agent
- `plan-orchestrator`, `develop-orchestrator`, `test-orchestrator`, and `fix-orchestrator` as real orchestrator agents
- thin VS Code prompt launchers for the four main workflows
- true portable skills extracted from the old repository concepts
- company coding standards integrated into the canonical AL instructions layer
- translation phase wired into `develop-orchestrator` after successful build

Workflow clarification:
- `develop-orchestrator` may execute translation in the integrated feature path once the final successful build is reached.
- If later production-code changes alter user-facing text, translation must be rerun on the final successful build before release.
- Standalone `review` and `translate` prompt launchers improve VS Code workflow clarity even though the canonical behavior still lives in the underlying agents.

## Migrated knowledge sources

Claude BC specialist knowledge merged into Copilot agents and skills:
- `alex-architect` → `solution-architect` architecture guidance
- `sam-coder` → `al-developer` implementation rules and company coding rules
- `roger-reviewer` → `al-reviewer` checklist and `al-coding-standards` skill
- `terry-test` → `test-orchestrator` edge-case categories and coverage policy
- `dean-debug` → `debugging-methodology` skill and `fix-orchestrator` hypothesis workflow
- `pat-performance` → `performance-review` skill
- `sam-security` → `security-review` skill
- `personal-coding-standards.md` → `al.instructions.md` canonical rules
- Company coding standards (cross-project) → `al.instructions.md`, `al-developer`, `al-reviewer`, `al-coding-standards` skill
- Translation workflow → `translator` agent and `translation-phase` skill
