---
name: AL Standards
description: Business Central AL naming, structure, and extension rules
applyTo: "**/*.al"
---

- Treat this file as the canonical AL coding-rules source for this Copilot workspace overlay.

## Naming and identifiers

- Use PascalCase for identifiers such as object names, field names, variables, procedures, parameters, and controls.
- Do not use underscores, hyphens, or other special characters in identifiers.
- Use spaces in AL object names and field names as the word separator; do not use underscores or camelCase in display names.
- Keep all AL object and field names to a maximum of 30 characters.
- Use namespaces with the AppSource affix as the base namespace and do not duplicate the affix in object names.
- Keep object names and member names in identifier form, while captions and other user-facing texts may use normal spaced language.

## Affixes and captions

- Keep captions, labels, tooltips, and translated user-facing text free of internal suffixes, affixes, or workspace prefixes.
- Use suffix affixes, never prefix affixes, when affixes are required for extension fields or other collision-prone names.
- Do not add affixes to custom object names when the namespace already provides the project identity.
- In custom tables, fields usually do not need affixes; in table extensions against dependency or base-app tables, added fields must use the project suffix.

## Table and page extensions

- Use `Rec.FieldName` bindings in page extensions.
- Prefer `addlast` or `addfirst` in page extensions; do not use `addafter` or `addbefore`.
- Use appropriate `ApplicationArea` for new fields in page extensions, typically `All`.
- To add triggers to existing fields in table extensions, use the `modify("Field Name")` syntax.
- Use `DataClassification = CustomerContent` for fields containing customer business data unless a more specific classification is clearly required.
- Do not leave new fields as `ToBeClassified`.

## Codeunits and business logic

- Prefer reusable business logic codeunits over duplicated logic in pages, triggers, or multiple objects.
- Keep business logic out of incidental UI code when a codeunit or shared procedure is more appropriate.
- When codeunits access table data directly, define `Permissions` explicitly when the behavior depends on it.
- Use PascalCase AL method calls such as `Insert`, `Modify`, `Delete`, `FindSet`, and `SetRange`.
- Use clear error messages with actionable business or field context rather than generic failures.

## Event subscribers

- Place event subscribers in a dedicated codeunit named `"[SourceObjectName] EH [PROJECTSUFFIX]"`, shortened if needed to fit the 30-character limit.
- Set `SingleInstance = true` on event subscriber codeunits.
- Write the `EventName` parameter in subscriber attributes without quotes (plain text, not string literal).

## Permission sets

- Use AL `permissionset` objects, not XML permission sets.
- Use the convention `*_E*` with caption containing "Edit" for insert/modify/delete permissions, `*_R*` with caption containing "Read" for read permissions, and `*_X*` with caption containing "Execute" for execute permissions.

## Labels and text handling

- When using placeholders in labels, add a `Comment` explaining their content, for example `Label 'Text %1', Comment = '%1 - Customer Name'`.
- If using `FieldCaption`, `TableCaption`, or similar in placeholders, specify the object, field, or variable name in the comment.
- Use `CopyStr` only when source and target lengths differ; always use `MaxStrLen(destination)` as the third parameter for truncation.

## Enums

- Do not create empty enum values. If suppressing empty-value warnings, use `#pragma warning disable LC0045` / `#pragma warning restore LC0045`.
- For enum type mismatches, use `Enum::TargetEnum.FromInteger(SourceEnum.AsInteger())`.

## File organization

- Add new objects to the appropriate folder based on object type.

## Translation

- Treat translation as a later dedicated phase, not something to mix into identifier design or implementation work.
- When new user-facing texts are introduced, the translation phase handles XLF refresh, language selection, and translation after a successful build.
