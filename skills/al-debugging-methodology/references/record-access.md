# Record access and subscriber diagnosis

| Symptom | Discriminating checks |
| --- | --- |
| Normal field unexpectedly loaded | `SetLoadFields` accepts normal fields only. Accessing an omitted normal field may trigger JIT loading; it does not silently yield zero. Inspect later accesses and concurrent modification errors before changing the load set. |
| FlowField value absent | Verify filters/FlowFilters and `CalcFields` or `SetAutoCalcFields` where needed. Do not put FlowFields or FlowFilters in `SetLoadFields`. `SetLoadFields(Name)` followed by `CalcFields(Balance)` is valid when those fields have the corresponding classes. |
| Validation not run | Assignment and `Validate` differ. `Modify(false)` still persists the record but skips its `OnModify`; using `true` does not replace explicit field validation. Choose each trigger intentionally. |
| Subscriber did not run | Match the exact publisher/signature and installed dependency version, then inspect publisher conditions, binding, skip-on-missing-license/permission options, `IsHandled` and runtime trace. A mismatched signature is not a documented silent-ignore mechanism. |
| Data copied incorrectly | Confirm complete keys and company, copying time relative to insertion, explicit mapping versus `TransferFields`, and existing transforms. Follow [field propagation](../../bc-field-propagation/SKILL.md) for posting/archive flows. |

Fix the demonstrated cause and verify through the failing entry point. Do not assign numerical confidence without evidence or equate a compiling subscriber with an executed event.

Sources: [partial records and JIT](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-partial-records), [SetLoadFields](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/record/record-setloadfields-method), [Modify](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/record/record-modify-method).
