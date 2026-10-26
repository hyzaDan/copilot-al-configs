# Reusable context and decisions

Keep context in the repository's existing location. Record app identity/version/runtime, relevant dependency versions, object ranges and allocation method, project naming rules, affected module boundaries, build/test commands actually available, and source paths. Exclude credentials, customer payloads and unsupported assumptions. Revalidate version-sensitive facts before reuse.

A handoff needs: immediate next action, incomplete work, evidence of completed checks, consequential open decisions, and files/source revision. Separate authored, compiled, runtime-tested, and deployed states. Link to existing artifacts instead of copying them.

Write an ADR only for a consequential choice: context/constraint, alternatives, decision, reason, consequences, status and date. A proposal is not an approved decision. For BC data/lifecycle decisions use [architecture](../../al-solution-architecture/SKILL.md); document counts and directory names are project choices, not fixed framework requirements.
