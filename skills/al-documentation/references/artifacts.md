# Choose one artifact

| Requested output | Useful content and BC-specific checks |
| --- | --- |
| User story / requirements | Actor, business outcome, current pain, boundaries, observable acceptance criteria, relevant rejection/edge cases. Resolve ambiguous posting, permissions or ownership decisions; no fixed question count. |
| Technical specification | Map acceptance criteria to affected tables/pages/codeunits/events, data lifecycle, complete keys, validation and transaction rules, permissions and target dependency versions. Allocate IDs only from actual project ranges. Mark unverified signatures. |
| Feasibility / estimate | Compare the few viable BC extension patterns, evidence, effort ranges, assumptions, dependencies and risks. Use supplied rates/workday lengths; never invent a customer price or fixed contingency. Distinguish standard configuration from extension and external-system work. |
| Implementation phase plan | Split at real dependencies into reviewable increments; identify files, source prerequisites, expected behavior and checks. No fixed phase count, no mandatory new approval after implementation is already authorized. Record a blocked decision without pretending it passed. |
| Release note | Select exact baseline and target revision/version; separate implemented behavior from plans. Explain user-visible changes, required setup/permissions, data migration, known limitations and actual validation. A commit title, latest-N-commits sample or object header is not proof of delivered behavior. |
| Change request / CCN | Consolidate agreed scope/change against baseline, affected acceptance criteria, impacts, estimates and outstanding decisions. Link sources and expose contradictions; do not produce every upstream artifact merely to fill a template. |

Only include an API/data handoff inventory when a real consumer needs it. Identify app/version, object/operation, data ownership, identity, required permissions and confirmed availability. An AL source object or successful build does not prove a published endpoint or a registered MCP tool.
