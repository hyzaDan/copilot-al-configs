---
name: review
description: Run a standalone AL review pass for correctness, standards, and maintainability
agent: agent
tools: ["read", "search"]
---

Review without editing using `al-bc-solution-review`. Return evidence-based findings ordered by severity and state validation gaps. This prompt reviews inline; select `al-reviewer` separately when an isolated second opinion is useful.

Files or feature to review:
${input:task:Paste changed files, a feature description, or a review target}