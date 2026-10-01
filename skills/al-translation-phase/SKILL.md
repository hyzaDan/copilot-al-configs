---
name: al-translation-phase
description: 'Use for AL XLF synchronization and English-to-Czech translation (en-US to cs-CZ) after changed captions, labels, or tooltips.'
user-invocable: true
---

# Translation Phase

Use applicable NAB translation/review instructions when supplied by the environment. They define detailed tool and XLF rules; do not load every workflow for a single translation task.

## Source and scope

Confirm a successful build produced `.g.xlf` for the intended project and current user-facing source. Reuse that evidence when still valid; translation-only edits do not require another build. If AL texts changed or provenance is unknown, use [build validation](../al-build-validation/SKILL.md) to regenerate before synchronization. Reviewer sign-off is not a translation prerequisite.

Translate only from English (`en-US`) to Czech (`cs-CZ`). Ignore all other target languages: do not synchronize, translate, create, or modify their XLF files, and do not ask the user to select languages. Verify source and target language metadata rather than relying only on filenames. If the English source or Czech target is missing, report the prerequisite instead of substituting another language. Never translate the generated `.g.xlf` itself.

## Routing

XLF synchronization and Czech translation are isolated worker tasks. A primary Agent prepares the successful-build evidence and selected Czech scope, then invokes `al-translator`; it does not call `refreshXlf`, read bulk XLF units, or save translations in its own context. The Luna worker retains raw tool responses and returns only saved/remaining counts and genuine ambiguities to the parent.

This routing requirement applies to a parent Agent. When the active agent is `al-translator`, execute the workflow below directly. If that worker or its required tools are unavailable, report the blocked prerequisite; do not silently perform XLF work with the parent model.
## NAB workflow

1. Synchronize only Czech (`cs-CZ`) target files with `refreshXlf` when needed to align with current English generated source.
2. Load English-to-Czech glossary terms and relevant existing Czech translations. Prefer `getTextsByKeyword` or bounded state queries over a complete translation map.
3. Fetch untranslated units with `getTextsToTranslate` in manageable batches (up to 100, smaller for long texts), retaining context and length constraints.
4. Validate and save with `saveTranslatedTexts`. Use `targetState="translated"` for completed translations unless project/review instructions require a review state; never mark uncertain work as final or signed-off.
5. Re-query remaining work without skipping units as the pending set shrinks. Stop when the selected Czech scope is done or unresolved ambiguity needs review. Report saved and remaining Czech counts, not full maps; other languages are out of scope, not unfinished work.

## Quality

- Preserve placeholder identities and multiplicity (`%1`, `%2`), formatting tokens, XML markup, and meaningful whitespace. Grammatical reordering is allowed unless the format or project requires fixed positions.
- Respect `maxLength`; use BC glossary terminology and consistent existing translations.
- Keep internal project affixes out of user-facing text. Identical source/target is acceptable only when justified, such as a product name.
- Preserve reviewed translations outside the selected scope; expose genuine ambiguity instead of inventing certainty.

If NAB tools are unavailable, use XML-aware editing that preserves namespaces, unit IDs, notes, and unrelated formatting. Mark newly supplied translations `needs-review-translation` unless project instructions specify otherwise, and validate XML, placeholders, and lengths. Do not regex-rewrite whole XLF files.
