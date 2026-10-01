# bc-test Runner Notes

These commands require an installed compatible `bc-test` CLI and configured BC test server; they are not built-in AL Language commands. Check installed help and project configuration before using these forms:

```text
bc-test 50200
bc-test 50200-50210
bc-test -o .dev/test-results.json -f json
bc-test --failures-only
```

Prefer explicit changed test codeunits. Some runner versions auto-detect only the first `app.json` ID range; check which codeunits ran before claiming full coverage. Keep results as an artifact when useful, returning only failures and counts to the main conversation.

Verify the server has matching app and test packages. Rebuild/redeploy changed packages only within the authorized environment workflow. If runtime execution is unavailable, report tests as authored/compiled, not passed.