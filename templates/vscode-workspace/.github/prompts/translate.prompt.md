---
name: translate
description: Run the AL translation workflow for XLF files after a successful build
tools: ["read", "search", "edit"]
---

Use this prompt as the VS Code launcher for the installed `al-translator` agent from this plugin.

Keep this wrapper thin. The canonical translation workflow lives in the worker agent definition, not in this prompt body.

Execution intent:
- adopt the `al-translator` workflow contract
- synchronize XLF files from the latest successful build
- preserve placeholders, formatting, and glossary consistency
- report translation status and any ambiguous texts needing review

If the environment cannot hand off automatically to the named agent, follow the same translation contract manually and keep the output aligned with the `al-translator` agent definition.

Build or translation task:
${input:task:Describe the build status, target languages, or translation scope}