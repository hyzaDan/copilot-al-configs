---
name: bc-agent-instructions-debugger
description: 'Use when reviewing or diagnosing instructions for a Business Central AI agent, using its profile, permissions, task timeline and observed failures.'
---

# BC agent instruction diagnosis

Identify the target BC version/capability, instruction revision, agent profile, available pages/actions and failing task. These are Business Central AI agents, distinct from development-host agents. Inspect the task timeline and serialized page/tool evidence when available; missing evidence is uncertainty, not a confirmed defect.

Follow the failing task's data and decisions: which value is read, retained, validated, used after navigation, and acted upon. Read [instruction checks](./references/instruction-checks.md) for BC-specific state, keywords and guard logic. Do not treat a natural-language walkthrough as execution evidence.

Report concrete conflicts with location, reachable failure and smallest correction. Responsibilities/guidelines/task steps are helpful structure, not a parser contract requiring exact headings or seven guidelines. Do not invent a runtime crash because a heading or bold keyword is absent.

When repairs are requested, apply them within scope and keep explanations in the report, not inline diagnostic arrows in the deployed instruction text. Preserve intended business rules. Verify the corrected decision branches on the target agent with an authorized task; report static checks separately if runtime is unavailable.
