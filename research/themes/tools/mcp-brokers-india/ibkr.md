# Broker MCPs: Interactive Brokers

## Summary
Use the IBKR Flex Web Service (read-only token, no order endpoint) for statements, fills and
dividends; it fits the user's IB LLC account. IBKR's official MCP only drafts orders for user
approval but may not be available to Indian residents ("not verified"). Never enable IBKR
Autonomous Trading. Community MCPs: only Hellek1/ib-mcp has no order tools; code-rabi places
orders unless IB_READ_ONLY_MODE=true.

Index: [Broker MCP servers and APIs](../mcp-brokers-india.md). Sources [S#]: [sources.md](sources.md).

Checked 2026-11-15; sources [S#] in sources.md. Nothing was installed, run or connected. Agents
never place, change or cancel orders (AGENTS.md), so a tool ranks high only if orders are
impossible by design (read-only credential), not just hidden by a setting. User (from
`portfolio/accounts.md`): IBKR = Interactive Brokers LLC, Individual, Cash; AngelOne (India);
INDmoney (broker Alpaca). No Zerodha, Upstox, Dhan or Groww account. No derivatives/margin abroad (LRS).

## Interactive Brokers
**1. IBKR Flex Web Service (official, read-only by design)**
- What: small HTTP API that runs a Flex Query (report template made once in Client Portal)
  and returns the report: trades, positions, cash, dividends and other statement data, the
  same as the manual Flex report [S1]. Two calls: SendRequest (token + query id, optional
  date range fd/td or period) then GetStatement with the reference code [S2].
- Cost: no fee on the docs pages [S1][S2] ("not verified"). Coverage: what the account holds
  (US now); history depth per request "not verified". Limit: 1 request/s, 10/min [S2].
- Safety: token only reads reports; there is no order endpoint in this service [S1][S2].
  Token validity is chosen at creation (6 hours to 1 year) and can be locked to given IPs [S3].
  Token goes in the URL: keep it in an env var, out of logs, history and the repository.
- Use: stage 7 `finance-journal` (fills, fees, realized P&L to check trades against the
  rules), `finance-main` (portfolio update instead of manual downloads), `finance-tax`
  (dividends, withholding, FA). A short script in `scripts/brokers/ibkr` is enough; no MCP
  needed. The community server code-rabi (below) also wraps Flex.
- Fit: **5** - only tool here that is read-only by design and matches an account the user has.

**2. IBKR official MCP / "AI Integration" (official, hosted)**
- What: IBKR runs an MCP server; any MCP client can add `https://api.ibkr.com/v1/api/mcp-public`
  and log in through IBKR's own screen (OAuth style; password never goes to the AI) [S4][S5].
  Tools: portfolio, positions, balances, orders status, watchlists, price alerts, research [S4].
- Orders: standard mode does not place orders; the AI creates non-binding "instructions" that
  the user must Review & Submit in an IBKR app [S4][S6]. Separate opt-in "Autonomous Trading"
  lets the AI trade without approval in a funded "AI Partition" (needs 10 approved AI trades
  first) - must never be enabled for these sessions [S4]. Whether the instruction tools can be
  switched off: "not verified". Revoke in Client Portal > Manage Third-Party Consents [S6].
- Availability: the page says "AI Integration is not available in IN or JP" [S4]. Whether this
  blocks an Indian resident with an IB LLC account: "not verified" (ask IBKR or try the connector).
- Cost: no IBKR fee [S4]. Use (if allowed): `finance-main`/`finance-journal` read positions
  and orders; deny the instruction tools in the client (see Safety layers).
- Fit: **2** - official and approval-gated, but India availability unclear and not read-only.

**3. TWS API / IB Gateway with "Read-Only API" (official setting)**
- TWS/Gateway Global Configuration > API > Settings has a "Read-Only API" checkbox; IBKR's
  setup page tells traders to disable it to place orders, so leaving it ticked blocks orders
  from any API client [S7]. Use as the safety layer under any TWS-based MCP (Hellek1 below).
  Fit **3** (needs TWS/Gateway running and logged in on the Mac, 2FA each login).

**4. IBKR Web API (Client Portal Gateway) (official)**
- REST API, free for all IBKR clients; individuals authenticate via the Java Client Portal
  Gateway (browser SSO) [S8][S9]. No per-user read-only switch for individuals found: IBKR's
  "block a user from placing trades" (Pre-Trade Compliance) is for institutional clients [S10].
  Fit **2** - a session here can trade.

**5. Community IBKR MCP servers (all unofficial)**
| Repo | Stars / open issues / last push / licence [S11] | Orders? |
|---|---|---|
| code-rabi/interactive-brokers-mcp (npm `interactive-brokers-mcp`) | 228 / 8 / 2026-07-21 / MIT | **Places orders by default.** `IB_READ_ONLY_MODE=true` skips registering place_order, confirm_order and alert create/activate [S12]. Optional headless login puts IB username, password and TOTP secret in env vars [S13]. Bundles its own Java Gateway that keeps running after exit [S13]. Has Flex tools (`IB_FLEX_TOKEN`). Fit **2** |
| Hellek1/ib-mcp (ib_async + FastMCP) | 19 / 5 / 2026-11-10 / BSD-3 | No order tools; README says read-only (contracts, history, fundamentals, news, portfolio) [S14]. Needs TWS/Gateway; pair with "Read-Only API". Small project. Fit **3** |
| ArjunDivecha/ibkr-mcp-server | 35 / 1 / 2025-07-23 / MIT | **Places, modifies, cancels orders** (MAX_ORDER_SIZE only) [S15]. Fit **1** |
| seriallazer/ibkr-mcp-server | 65 / 5 / 2026-03-19 / none | README describes a FastAPI portfolio app, not a clear MCP server [S16]. Fit **1** |
