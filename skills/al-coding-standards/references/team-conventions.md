# Optional Team Conventions

These preferences came from the original agent pack. Apply them when the project adopts them; preserve a different established project policy.

- English names; PascalCase variables and procedures; spaces in quoted object and field names; a conservative 30-character object/field-name budget.
- Namespace-based project identity and suffix affixes on tableextension fields. Avoid duplicating affixes where the applicable analyzer/AppSource rules do not require them.
- Prefer `addfirst` / `addlast` when the desired layout permits it. `addbefore` / `addafter` remain valid for explicit, verified anchors.
- Group subscribers by source in an event-handler codeunit, historically named `[SourceObjectName] EH [PROJECTSUFFIX]`, shortened to fit the applicable name limit.
- Permission-set suffixes `*_E*` for insert/modify/delete, `*_R*` for read, and `*_X*` for execute; folders organized by object type.

- Omit `begin`/`end` around a single statement when matching the team's existing style.

The former package-wide `SingleInstance = true` default is retired. A project can explicitly adopt it, but review its state lifetime; absence alone is not a defect. See [subscriber lifetime](./subscriber-lifetime.md).

These conventions do not mandate unquoted event-name arguments, numeric enum casts, or warning suppression. Use actual AL syntax and behavioral requirements.
