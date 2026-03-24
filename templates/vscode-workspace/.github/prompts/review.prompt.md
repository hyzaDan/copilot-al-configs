---
name: review
description: Run a standalone AL review pass for correctness, standards, and maintainability
tools: ["read", "search"]
---

Use this prompt as the VS Code launcher for the installed `al-reviewer` agent from this plugin.

Keep this wrapper thin. The canonical review behavior lives in the worker agent definition, not in this prompt body.

Execution intent:
- adopt the `al-reviewer` review contract
- produce findings first, ordered by severity
- cite concrete files and risks where possible
- note residual validation gaps when verification was incomplete

If the environment cannot hand off automatically to the named agent, follow the same review contract manually and keep the output aligned with the `al-reviewer` agent definition.

Files or feature to review:
${input:task:Paste changed files, a feature description, or a review target}