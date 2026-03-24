---
name: al-translation-phase
description: Guides the AL translation phase — when to translate, how to handle XLF files, and quality expectations for localized texts.
user-invocable: true
---

# Translation Phase

Use this skill after implementation and core review are complete and the app builds successfully.

## Purpose

- separate translation from implementation so that code is stable before localizing
- guide XLF synchronization, batch translation, and quality validation
- define when and how to invoke the `al-translator` agent or perform translation manually

## When to translate

- only after a successful build that produced an up-to-date `.g.xlf` file
- never during active implementation or while the code is still under review
- when the `al-develop-orchestrator` or user explicitly triggers the translation phase

## Translation workflow summary

1. Build the app (`al_build` or `buildAlPackage`) to generate the current `.g.xlf`.
2. For each target language XLF file in `Translations/`:
   a. Synchronize with `refreshXlf`.
   b. Load glossary (`glossary.tsv` + `getGlossaryTerms`).
   c. Load existing translations as style reference (`getTranslatedTextsMap`).
   d. Fetch untranslated texts in batches of up to 100 (`getTextsToTranslate`).
   e. Translate, validate, and save each batch (`saveTranslatedTexts`).
   f. Repeat until no untranslated texts remain.
   g. Final `refreshXlf` to confirm completion.
3. Report a per-language summary and list challenging translations for review.

## Translation quality rules

- preserve all placeholders (`%1`, `%2`) in position and format
- preserve formatting, special characters, XML tags, and backslashes
- respect `maxLength` constraints — measure and shorten before saving
- do not copy source text as translation unless justified (proper noun, universal abbreviation, technical term)
- apply glossary terms exactly when they match
- keep translated texts free of project suffixes, affixes, or workspace identifiers
- maintain consistency with existing translations in the project

## Available NAB AL Tools

- `refreshXlf` — sync XLF with generated `.g.xlf`
- `getTextsToTranslate` — fetch untranslated texts
- `saveTranslatedTexts` — save translations with state
- `getTranslatedTextsMap` / `getTranslatedTextsByState` — existing translations
- `getGlossaryTerms` — glossary for target language
- `getTextsByKeyword` — search texts by keyword
- `buildAlPackage` — compile and generate `.g.xlf`

## When NAB tools are unavailable

Fall back to direct XLF file editing:
- open the target XLF file
- locate `<trans-unit>` elements without `<target>` or with `state="needs-translation"`
- add or update `<target>` elements with the translation
- set `state="needs-review-translation"` on new translations

## Related agents

- `al-translator` — the dedicated translation worker that executes this workflow
- `al-develop-orchestrator` — triggers the translation phase after successful build
