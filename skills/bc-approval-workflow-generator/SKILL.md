---
name: bc-approval-workflow-generator
description: Add or change approval workflows for Business Central entities using the standard Workflow and Approvals engines, including status transitions and enforcement outside the UI.
---

# Approval workflows

Start from the entity's existing approval support. Extend the standard flow when available; add a custom status field only when the entity needs one. Use the consuming app's naming, allocated IDs, dependencies and target symbols. Resolve the exact publishers and `var` parameters before writing subscribers.

## Define the approval contract

- Identify the complete record identity, related lines, approval routing and operations restricted while pending or approved: editing, deleting, posting, releasing or other business actions. Reuse decisions already supplied by the user or project.
- Map send, approve, reject, cancel and reopen to explicit transitions. Approval of one entry need not mean the entire workflow is approved; handle sequential approvers and remaining entries through the standard engine.
- Choose one status field and enum and use them consistently in tables, subscribers, filters and pages. Declare the entity record wherever template conditions or field numbers use it.
- Decide whether business changes after approval require cancellation/reapproval and what happens to approval history on deletion. Do not silently delete history to allow an otherwise forbidden operation.

## Connect the standard engine

Use separate responsibilities for entity operations and workflow-library registration; they can share a codeunit when that fits the project.

| Responsibility | Implementation decision |
|---|---|
| Send/cancel | Validate the entity and workflow availability, then raise the entity event consumed by Workflow Management. Avoid duplicate pending requests. |
| Workflow library | Register stable event codes, response codes, supported predecessors, and table relations through the library extension events. |
| Approval entry | Resolve the entity by record identity and supply approver/amount/currency arguments only where meaningful for this entity. |
| Responses | Apply pending, release, rejection and cancellation according to the state contract; ignore events for other table types. |
| Navigation | Resolve the appropriate card page from the approved record's type. |
| Template | Add an optional category/template that uses the registered events and responses; do not enable or overwrite a user's workflow as a generation side effect. |

Workflow libraries are rebuilt during application upgrades. Register custom events, responses and relations through their recreation extension points, rather than inserting them only once during installation. See Microsoft's [workflow extension walkthrough](https://learn.microsoft.com/dynamics365/business-central/dev-itpro/developer/devenv-walkthrough-workflow-events-responses).

## Enforce the contract

Page `Editable` and action visibility improve the UI but do not guard API, job queue or other AL writes. Enforce restrictions in the relevant table/business operations and cover related line inserts, edits and deletes. A table `OnModify` check alone also does not cover code that deliberately skips that trigger; inspect the actual write paths and permission model.

Use standard record restriction support where its hooks cover the operation. The built-in restriction responses do not automatically protect every custom activity; Microsoft describes the supported [record restriction behavior](https://learn.microsoft.com/dynamics365/business-central/across-how-to-restrict-and-allow-usage-of-a-record). Keep internal approval status transitions possible without opening an unrestricted bypass for normal callers.

## Verify

Compile against the target symbols. Exercise no enabled workflow, missing approver, duplicate send, cancel, rejection, sequential approval and reopening. Check restricted writes through both UI and a non-UI path, including lines. Verify library recreation retains the custom entries. Report compilation and executed workflow scenarios separately.
