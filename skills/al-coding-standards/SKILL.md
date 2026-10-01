---
name: al-coding-standards
description: 'Use when writing or reviewing AL objects, names, subscribers, permissions, labels, or enum conversions.'
user-invocable: false
---

# AL Coding Standards

Project instructions, supported runtime, and configured analyzers determine the applicable conventions. Team preferences are not platform restrictions. For the historical naming and layout policy, read [team conventions](./references/team-conventions.md) only when adopting it or reviewing a project that already uses it.

## Naming rules

- Use English identifiers, PascalCase variables/procedures, and project-consistent quoted object names.
- Follow project naming limits, namespaces, and configured analyzer rules.
- Namespaces do not replace required AppSource affixes.
- Keep internal suffixes out of captions, labels, tooltips, and translated user-facing text.

## Affix rules

- Follow the project's affix policy and applicable AppSource requirements; do not migrate existing names as incidental cleanup.

## Extension patterns

- Use `Rec.FieldName` bindings in page extensions.
- Choose page extension anchors that exist in the supported Base App version; placement is a UI requirement, not a universal ban on `addafter` / `addbefore`.
- Use appropriate `ApplicationArea` for new fields in page extensions, typically `All`.
- Use `modify("Field Name")` to add triggers to existing fields in table extensions.

## Codeunits and business logic

- Use PascalCase method calls such as `Insert`, `Modify`, and `Delete`.
- Use `DataClassification = CustomerContent` for customer data fields unless a more specific classification is required.
- Do not leave new fields as `ToBeClassified`.
- Use clear error messages with meaningful field or business context.
- Extract repeated business logic into shared procedures or codeunits.
- Add codeunit `Permissions` only for an intentional indirect-permission requirement, not merely because a record is accessed.
- Use `Validate` when field business rules must run; choose trigger execution on record operations deliberately.
- Use `then` without `begin`/`end` for single-line `if`/`while`/`for` blocks; reserve `begin ... end` only for multi-line blocks.

## Event subscribers

- Follow the project's event-handler organization and verify signatures against actual dependency symbols.
- Set `SingleInstance = true` by default on event-handler codeunits. Reusing the instance across subscriber invocations reduces repeated codeunit instantiation overhead.
- Omitting `SingleInstance` requires a concrete, documented reason, such as a required per-invocation state lifetime. Check global variables for state retained between calls; keep handlers stateless where possible. This default applies to event-handler codeunits, not every codeunit.
- Use the subscriber attribute syntax required by the supported AL compiler.

## Permission sets

- Use AL `permissionset` objects, not XML.
- Follow project naming and grant least privilege.

## Labels and enums

- Add a `Comment` to labels with placeholders explaining each placeholder.
- If using `FieldCaption`, `TableCaption`, or similar in placeholders, specify the object or field name in the comment.
- Use `CopyStr` with `MaxStrLen(destination)` only when truncation is intended; do not silently truncate business identifiers.
- A blank/default enum value can be meaningful. Do not suppress analyzer warnings merely to bypass that design decision.
- Map different enums explicitly unless their numeric value contract is known to match.

## File organization

- Add new objects to the appropriate folder based on object type.

## Translation

- Use [translation guidance](../al-translation-phase/SKILL.md) when changed captions, labels, or tooltips require localization, not for every code edit.
