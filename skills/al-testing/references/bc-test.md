# bc-test Runner Notes

`bc-test` is an optional external CLI, not supplied by this plugin or a built-in AL Language command. Inspect the installed executable's help/version and the project's configuration before constructing a command; there is no portable argument contract assumed here.

Prefer explicit changed test codeunits. Some runner versions auto-detect only the first `app.json` ID range; check which codeunits ran before claiming full coverage. Keep results as an artifact when useful, returning only failures and counts to the main conversation.

Verify the server has matching app and test packages. Rebuild/redeploy changed packages only within the authorized environment workflow. If runtime execution is unavailable, report tests as authored/compiled, not passed.
