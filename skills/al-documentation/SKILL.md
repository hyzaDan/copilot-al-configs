---
name: al-documentation
description: 'Use when explicitly authoring BC requirements, user stories, technical specifications, feasibility analyses, change requests, implementation plans, or release notes.'
---

# AL documentation

Choose the requested artifact and existing project format. A code edit does not automatically need a story/spec/analysis/architecture/plan chain. Preserve supplied decisions and authorization; ask only about consequential missing business facts.

Read [artifact guidance](./references/artifacts.md) for the selected document. Ground object names, IDs, dependencies, events and release claims in actual source/symbols and selected revision range. Clearly label proposed design, assumptions, estimates and unverified integration points.

Write in the user's language, keeping technical identifiers stable. Reuse the project's output location, numbering and templates if present. Use Markdown by default; no Word renderer, schema registry or external delivery framework is bundled. Do not fabricate customer details, human authorship, approval dates, rates, test results or deployment status.

Map acceptance criteria to the relevant technical behavior and verification. Include only needed setup, permission, migration, localization and operational impacts. For architecture decisions use [AL architecture](../al-solution-architecture/SKILL.md); for cross-session context use [context records](../al-project-context-bootstrap/references/context-and-decisions.md).

Before delivery, check consistency of source references, scope, acceptance criteria and evidence. Report unresolved decisions that would change implementation. Documentation completion does not establish business approval or runtime acceptance.
