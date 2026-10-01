# Skill-First Audit

Date: 2026-09-06. Goal: built-in Plan and Agent as defaults, with domain skills discovered on demand and custom agents used exceptionally.

The supplied article is a prompt-design motivation, not evidence of a particular model's abilities or billing. Changes target redundant instructions and concrete AL/tooling risks across models; no Astra/Sol/Terra/Luna performance comparison was performed.

## Findings and changes

| Finding | Decision |
| --- | --- |
| Mandatory developer workers for even trivial fixes, fixed team sizes, universal review sign-off | Remove those gates; retain manual compatibility agents as thin skill-backed entrypoints |
| Prompt launchers referenced archived planning agents and blocked execution tools | Route to built-in `plan` / `agent`; keep read-only restrictions only for review/artifact analysis |
| Multi-root build safety lived only in the development orchestrator | Extract `al-build-validation` with an exceptional-diagnostics reference |
| Test and snapshot expertise lived primarily in agent bodies | Extract `al-testing`; move artifact analysis into debugging reference |
| Architecture discovery matched nearly every AL task | Narrow to actual design/extension-point decisions and remove generic planning scaffolding |
| Team preferences presented as platform requirements | Separate optional naming/layout conventions; event-handler codeunits default to SingleInstance with a documented reason required for exceptions; remove universal numeric enum conversion and warning-suppression rules |
| Translation had duplicate procedures, all-language versus Czech-only conflict, and unneeded build/review gates | One skill owns English-to-Czech-only scope, current XLF evidence, bounded queries, save states, and quality; worker has no publish/debug tools |
| Symbol tool output could fill the parent context | Add narrow-query skill and an optional Terra worker returning exact signatures and provenance |
| Historical migration documentation described obsolete runtime ownership | Label history; document current ownership separately |

## Skill decisions

Retain the small solution/performance/security review skills: their AL-specific triggers differ, so merging them would load unrelated guidance. Tighten their descriptions and remove blind optimization rules. Context bootstrap remains optional for onboarding, not a prerequisite for edits.

Add only three skills: build validation, AL testing, and symbol lookup. Do not add generic development, orchestration, persistence, or TDD-recipe skills. Put longer/exceptional details in references. Existing agent names remain for compatibility; a later breaking release can remove unused manual entrypoints without losing domain knowledge.

`Backup/`, historical documents, and empty hook configuration do not automatically consume skill-body context. Leave them out of runtime references rather than deleting history or inventing hooks. MCP definitions and plugin manifests are unchanged.

## Boundaries retained

- Build results must identify the intended project and current source state.
- Publishing and mutating tests require an identified authorized environment.
- Event-handler codeunits default to `SingleInstance = true` to reuse instances; omitting it requires a concrete documented reason and review of state lifetime.
- Translation is English (`en-US`) to Czech (`cs-CZ`) only. Other language files are neither synchronized nor translated.
- Partial symbol results are not proof of API absence; signatures must remain exact through summarization.
- Team conventions remain available, but projects must explicitly adopt them if they are required policy.

## Verification and limits

Static validation passed for 11 skills, 8 agents, 7 prompts, 41 local Markdown links, and 3 root JSON configurations. YAML was parsed with duplicate-key rejection; checks covered skill/directory names, prompt modes, opt-in orchestrators, and obsolete exact-name runtime references. Editor diagnostics cached one formerly missing link; its target was verified independently on disk.

Compared with the pre-change HEAD, agent definitions decreased from 855 to 90 lines (including the new symbol worker), prompt launchers from 140 to 72, and skill entrypoints from 371 to 364 despite three new skills. Linked references and documentation are additional on-demand text; these figures are not token counts or billing measurements.

This repository has no BC app or configured test fixture for exercising AL behavior. Live skill discovery, model selection, MCP availability, cross-host support, runtime translation execution, and actual token/cost savings require a consuming-workspace smoke test. See [model routing](model-routing.md) for the test cases and official documentation.