# Optional Team Conventions

These preferences came from the original agent pack. Apply them when the project adopts them; preserve a different established project policy.

- English names; PascalCase variables and procedures; spaces in quoted object and field names; a conservative 30-character object/field-name budget.
- Namespace-based project identity and suffix affixes on tableextension fields. Avoid duplicating affixes where the applicable analyzer/AppSource rules do not require them.
- Prefer `addfirst` / `addlast` when the desired layout permits it. `addbefore` / `addafter` remain valid for explicit, verified anchors.
- Group subscribers by source in an event-handler codeunit, historically named `[SourceObjectName] EH [PROJECTSUFFIX]`, shortened to fit the applicable name limit.
- Permission-set suffixes `*_E*` for insert/modify/delete, `*_R*` for read, and `*_X*` for execute; folders organized by object type.

For event-handler codeunits, follow the `SingleInstance = true` default and documented-exception rule in [coding standards](../SKILL.md).

These conventions do not mandate unquoted event-name arguments, numeric enum casts, or warning suppression. Use actual AL syntax and behavioral requirements.