# Broker MCP servers and APIs (IBKR, Alpaca, India)

Checked 2026-11-15. Research only: nothing was installed, run or connected.

## Summary
Agents never place orders, so only tools that cannot trade by design rank high. Best fit: IBKR
Flex Web Service (read-only token, user's IB LLC account) for finance-journal, -main and -tax.
Upstox Analytics Token and hosted Kite MCP are read-only but need new accounts. AngelOne
SmartAPI, Dhan, Groww, Alpaca and most community MCPs can place orders: keep them off or
strip order tools and block them with Copilot CLI --deny-tool.

## Ranked

| # | Candidate | Cost | India? | Read-only possible | Maintainer | Fit |
|---|---|---|---|---|---|---|
| 1 | IBKR Flex Web Service | free | no (US account) | yes, by design | IBKR (official) | 5 |
| 2 | Upstox Analytics Token + MCP | free | yes NSE/BSE | yes, by design | Upstox (official) | 3 |
| 3 | Hellek1/ib-mcp + TWS "Read-Only API" | free | no | yes (no order tools + TWS switch) | community | 3 |
| 4 | TWS API / IB Gateway | free | no | yes, checkbox | IBKR (official) | 3 |
| 5 | Kite MCP hosted (mcp.kite.trade) | free; Connect Rs 500/mo | yes | yes (hosted) | Zerodha (official) | 2 |
| 6 | IBKR official MCP (AI Integration) | free | blocked in IN? | no orders, but instructions | IBKR (official) | 2 |
| 7 | AngelOne SmartAPI (direct, GET only) | free | yes | no (token can trade) | AngelOne (official) | 2 |
| 8 | Alpaca MCP (paper, data toolsets) | free / $99/mo | no | partly (toolsets) | Alpaca (official) | 2 |
| 9 | code-rabi/interactive-brokers-mcp | free | no | yes if flag set (orders default on) | community | 2 |
| 10 | jugaad-data / nsepython | free | yes NSE | n/a (no orders) | community | 2 |
| 11 | IBKR Web API (CP Gateway) | free | no | no (individuals) | IBKR (official) | 2 |
| 12 | Dhan MCP | free | yes | no (orders) | Dhan (official) | 1 |
| 13 | Groww MCP | Rs 499/mo | yes | no (orders) | Groww (official) | 1 |
| 14 | ArjunDivecha / angel-one community MCPs | free | mixed | no (orders) | community | 1 |

## Parts
| Part | What |
|---|---|
| [ibkr.md](mcp-brokers-india/ibkr.md) | Flex Web Service, official MCP, TWS API Read-Only, Web API, community IBKR MCPs |
| [alpaca-and-india.md](mcp-brokers-india/alpaca-and-india.md) | Alpaca MCP; Kite, Upstox, AngelOne SmartAPI, Dhan, Groww, NSE data |
| [safety.md](mcp-brokers-india/safety.md) | Safety layers to keep sessions from placing orders |
| [sources.md](mcp-brokers-india/sources.md) | Sources S1-S37, all checked 2026-11-15 |
