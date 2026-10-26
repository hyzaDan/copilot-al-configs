---
name: bc-api-design
description: Design Business Central custom API pages, read-only API queries, and OData bound actions with stable contracts.
---

# Business Central API design

Choose the API object from the requested contract:

| Need | Object |
| --- | --- |
| CRUD for an entity, navigation properties, a business operation | API page |
| Read-only joins or aggregation across tables | API query |

Read the consuming project's manifest, existing APIs and dependency symbols before assigning IDs, names, properties or action signatures. Allocate IDs through the project's policy across all relevant source directories. Preserve an established public contract; a sample `v2.0` is not a platform requirement.

## Contract decisions

- Define publisher, group, version, entity/entity-set names, field types, nullability, writable fields and permissions. Use stable machine names; localize captions separately. API pages/queries cannot be extended with page/query extensions; use a separate API when necessary.
- Prefer `SystemId` as the single GUID key for API pages. A composite key needs an actual consumer requirement and compatibility checks. Document the expected company and environment in requests.
- Build a custom endpoint from the actual service base plus `/api/{publisher}/{group}/{version}/companies({companyId})/{entitySetName}`. Do not substitute the standard Microsoft `/api/v2.0` route for a custom API.
- Put validation and business operations on the appropriate server paths. UI editability and hiding fields do not enforce business rules on other write paths. Treat ETags and `If-Match` as concurrency behavior to verify for updates/deletes.
- For nested resources, establish complete header/line identity and navigation links. Test supported create/update operations independently; do not infer deep PATCH support from a successful deep insert.

## Implement only the selected mode

- For page behavior and bound actions, read [page and action patterns](references/pages-and-actions.md).
- For joins, filters and aggregates, read [query patterns](references/queries.md).

Use [symbol lookup](../al-symbol-lookup/SKILL.md) for referenced tables, fields and platform methods. Do not add optional properties such as `AboutText` unless the target compiler supports them and they serve the contract.

## Evidence to collect

Compile in the consuming project. Check `$metadata` and representative requests in an authorized environment: key lookup, filtering, page navigation, invalid input, permissions and stale ETag. For queries, check row count and totals against independently filtered source data, including duplicate joins and missing children. For actions, verify state changes, returned entity identity and failure/rollback behavior. Report generated source, compilation and HTTP/runtime observations separately.
