---
name: al-coding-standards
description: Applies Business Central AL naming, extension, error handling, and file organization standards.
user-invocable: false
---

# AL Coding Standards

Use this skill when implementing or reviewing AL code.

## Naming rules

- Use PascalCase identifiers and avoid underscores, hyphens, and prefix-style affixes.
- Use spaces as word separators in AL object and field names; do not use underscores or camelCase for display names.
- Keep object names and member names in identifier form; captions and user-facing texts may use normal spaced language.
- Keep all object and field names to a maximum of 30 characters.
- Use English for all identifiers
- Use namespaces with the AppSource affix as the base namespace; do not duplicate the affix in object names.
- Keep internal suffixes out of captions, labels, tooltips, and translated user-facing text.

## Affix rules

- In table extensions, use suffix affixes on added fields; in custom tables, avoid unnecessary affixes.
- Never use prefix affixes.

## Extension patterns

- Use `Rec.FieldName` bindings in page extensions.
- Use `addlast` or `addfirst` only; do not use `addafter` or `addbefore`.
- Use appropriate `ApplicationArea` for new fields in page extensions, typically `All`.
- Use `modify("Field Name")` to add triggers to existing fields in table extensions.

## Codeunits and business logic

- Use PascalCase method calls such as `Insert`, `Modify`, and `Delete`.
- Use `DataClassification = CustomerContent` for customer data fields unless a more specific classification is required.
- Do not leave new fields as `ToBeClassified`.
- Use clear error messages with meaningful field or business context.
- Extract repeated business logic into shared procedures or codeunits.
- When codeunits access table data directly, define `Permissions` explicitly when the behavior depends on it.
- Use `then` without `begin`/`end` for single-line `if`/`while`/`for` blocks; reserve `begin ... end` only for multi-line blocks.

## Event subscribers

- Place subscribers in a dedicated codeunit named `"[SourceObjectName] EH [PROJECTSUFFIX]"`.
- Set `SingleInstance = true` on event subscriber codeunits.
- Write `EventName` without quotes in subscriber attributes.

## Permission sets

- Use AL `permissionset` objects, not XML.
- Convention: `*_E*` (Edit/IMD), `*_R*` (Read), `*_X*` (Execute).

## Labels and enums

- Add a `Comment` to labels with placeholders explaining each placeholder.
- If using `FieldCaption`, `TableCaption`, or similar in placeholders, specify the object or field name in the comment.
- Use `CopyStr` only when lengths differ; use `MaxStrLen(destination)` for truncation.
- Do not create empty enum values; if suppressing empty-value warnings, use `#pragma warning disable LC0045` / `#pragma warning restore LC0045`.
- For enum type mismatches, use `Enum::TargetEnum.FromInteger(SourceEnum.AsInteger())`.

## File organization

- Add new objects to the appropriate folder based on object type.

## Translation

- Treat translation as a later dedicated phase; do not mix it into implementation work.
- When new user-facing texts are introduced, handle XLF refresh and translation after a successful build.

## When to apply

- AL implementation
- AL code review
- design review when object naming and placement decisions matter
