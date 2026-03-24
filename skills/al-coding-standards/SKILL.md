---
name: al-coding-standards
description: Applies Business Central AL naming, extension, error handling, and file organization standards.
user-invocable: false
---

# AL Coding Standards

Use this skill when implementing or reviewing AL code.

This skill is a quick reference. The canonical rules source for AL files in the workspace overlay is `templates/vscode-workspace/.github/instructions/al.instructions.md`.

## Naming rules

- Use PascalCase identifiers and avoid underscores, hyphens, and prefix-style affixes.
- Use spaces as word separators in AL object and field names; do not use underscores or camelCase for display names.
- Keep all object and field names to a maximum of 30 characters.
- Let the namespace carry the project affix; do not duplicate it in object names.
- Keep internal suffixes out of captions, labels, tooltips, and translated user-facing text.

## Affix rules

- In table extensions, use suffix affixes on added fields; in custom tables, avoid unnecessary affixes.
- Never use prefix affixes.

## Extension patterns

- Use `Rec.FieldName` bindings in page extensions.
- Use `addlast` or `addfirst` only; do not use `addafter` or `addbefore`.
- Use appropriate `ApplicationArea` for new fields in page extensions, typically `All`.
- Use `modify("Field Name")` to add triggers to existing fields in table extensions.

## Method and data rules

- Use PascalCase method calls such as `Insert`, `Modify`, and `Delete`.
- Use `DataClassification = CustomerContent` for customer data fields unless a more specific classification is required.
- Use clear error messages with meaningful field or business context.
- Extract repeated business logic into shared procedures or codeunits.

## Event subscribers

- Place subscribers in a dedicated codeunit named `"[SourceObjectName] EH [PROJECTSUFFIX]"`.
- Set `SingleInstance = true` on event subscriber codeunits.
- Write `EventName` without quotes in subscriber attributes.

## Permission sets

- Use AL `permissionset` objects, not XML.
- Convention: `*_E*` (Edit/IMD), `*_R*` (Read), `*_X*` (Execute).

## Labels and enums

- Add a `Comment` to labels with placeholders explaining each placeholder.
- Use `CopyStr` only when lengths differ; use `MaxStrLen(destination)` for truncation.
- For enum type mismatches, use `Enum::TargetEnum.FromInteger(SourceEnum.AsInteger())`.

## File organization

- Add new objects to the appropriate folder based on object type.

## When to apply

- AL implementation
- AL code review
- design review when object naming and placement decisions matter
