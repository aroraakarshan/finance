# Broker MCPs: safety layers

## Summary
Agents must never place orders. Prefer credentials that cannot trade; then remove order tools
on the server; then block them in Copilot CLI with --deny-tool; keep credentials in env vars
or typed at the prompt; never enable a hosted MCP with trading scope.

Index: [Broker MCP servers and APIs](../mcp-brokers-india.md). Sources [S#]: [sources.md](sources.md).

## Safety layers (use all that apply)
1. Prefer credentials that cannot trade: IBKR Flex token, Upstox Analytics Token, Kite hosted MCP.
2. Server-side tool removal: `EXCLUDED_TOOLS` (Kite), `ALPACA_TOOLSETS`, `IB_READ_ONLY_MODE=true`
   (code-rabi); TWS "Read-Only API" ticked.
3. Client-side block in Copilot CLI 1.0.112: `--deny-tool='<server>(place_order)'` (deny wins
   over every allow, even `--allow-all`), `--excluded-tools` hides tools, `--secret-env-vars`
   masks credentials from shell and MCP environments [S37].
4. Credentials only as environment variables or typed at the prompt; never in the repo; no
   stored TOTP secrets or broker passwords for agents.
5. No hosted third-party MCP with trading scope; never enable IBKR Autonomous Trading.
