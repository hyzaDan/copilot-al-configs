# Pages and bound actions

These are fragments for an existing API page, not standalone objects. Resolve the source table, field names and object names in the consuming project.

For a page keyed by the source table's `SystemId`, expose a read-only GUID field:

```al
ODataKeyFields = SystemId;

// Inside a repeater in the API page layout:
field(id; Rec.SystemId)
{
    Editable = false;
}
```

For a read-only contract also set `InsertAllowed`, `ModifyAllowed` and `DeleteAllowed` to `false`; choose data permissions consistently. For a writable contract use the actual table validation/posting logic and verify delayed insertion behavior rather than writing partial records prematurely.

## Bound action shape

An OData bound action is a `[ServiceEnabled]` procedure. A UI `action`/`OnAction` block does not expose one. Put authorization, input validation and the requested operation in that procedure or a verified business service. Do not invent parameter extraction or response helpers.

After an operation creates a resource, a response context can be populated with the following supported methods:

```al
ActionContext.SetObjectType(ObjectType::Page);
ActionContext.SetObjectId(ResultApiPageId);
ActionContext.AddEntityKey(ResultKeyFieldNo, ResultKeyValue);
ActionContext.SetResultCode(WebServiceActionResultCode::Created);
```

`ActionContext` is a `var WebServiceActionContext` parameter of the service-enabled procedure. The result page ID, key field number and value must describe the resource actually created and its API key. Use the result code appropriate to the actual operation. This fragment deliberately supplies no posting subscriber, page ID or helper implementation.

Find the action name, parameters and namespace in the generated `$metadata`; construct its HTTP request from that metadata. Microsoft also documents bound actions on UI pages published through OData, whose `/ODataV4/...` route differs from custom API routes. Do not mix the two URL forms. A page extension cannot add a bound action to an already exposed page.

For non-idempotent operations, define what a retry after a lost HTTP response does. A transport error is not proof that the transaction failed.

## Primary sources

- [Developing a custom API](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-develop-custom-api): properties, SystemId and navigation examples.
- [API page type](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-api-pagetype): supported page behavior.
- [ServiceEnabled attribute](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/attributes/devenv-serviceenabled-attribute) and [OData bound actions](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-creating-and-interacting-with-odatav4-bound-action): procedure and action-context pattern.
