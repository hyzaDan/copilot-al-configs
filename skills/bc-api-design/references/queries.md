# Query contracts

`QueryType = API` publishes a read-only endpoint. Set the API publisher/group/version and entity names as contract values. Expose only the columns and filter controls needed by consumers.

## Joins and filters

Choose join direction and cardinality before selecting columns. A one-to-many child multiplies rows; adding another one-to-many child can multiply aggregates again. Decide what a result row represents, including whether parents with no children must appear.

This fragment belongs in a `Sales Line` dataitem below a parent dataitem named `Header` over `Sales Header`. It demonstrates complete document identity and a single combined filter declaration:

```al
DataItemLink = "Document Type" = Header."Document Type",
               "Document No." = Header."No.";
SqlJoinType = InnerJoin;
DataItemTableFilter = Type = const(Item), Quantity = filter(<> 0);
```

Verify those fields and enum/option members in target symbols. Link on every part of the business identity; a document number alone can collide across document types. Keep multiple fixed conditions in one `DataItemTableFilter`. Its fixed filters intersect with consumer/AL filters; callers cannot loosen them.

## Aggregation

Use `Method = Sum`, `Count` or another supported aggregate only after defining the grouping. Non-aggregated columns become grouping columns; adding an ID/name can silently change the grain. Do not expose one arbitrary source record's `SystemId` as the identity of an aggregate row.

For a sum over ledger entries, test at least: two entries for one parent, a parent with no entries, negative amounts, filtered-out entries, and an extra joined child with multiple matches. Compare the resulting groups and totals with the intended independent calculation. Treat `DataAccessIntent = ReadOnly` as a target/environment-dependent optimization, not a guarantee of a replica or transactional freshness.

## Primary sources

- [API query type](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-api-querytype).
- [Filtering in query objects](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-query-filters).
- [DataItemLink property](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/properties/devenv-dataitemlink-query-property).
- [Query aggregate methods](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-query-totals-grouping).
