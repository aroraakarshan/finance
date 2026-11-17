# MCP servers for market data

Checked 2026-11-15. Research only: nothing installed, no accounts, no MCP server run.
"MCP" = Model Context Protocol: a server that exposes a data API as tools an AI session can call.
Repo stats from the GitHub API on 2026-11-15 (stars / open issues / last push / licence).

## Summary
- An MCP server adds no new data over our direct scripts; keep yfinance and EDGAR scripts as they are.
- No low-cost source gives verified NSE/BSE fundamentals: keep screener.in and the NSE bhavcopy for India.
- Cheapest verified NSE+BSE prices: Twelve Data Grow ($79/mo). Alpha Vantage free has BSE daily prices.
- If paying later for global fundamentals: FMP Ultimate ($99/mo) or EODHD ($59.99/mo); test India tickers on a free key first.

## Ranked table
| Candidate | Cost | India? | Read-only possible | Maintainer | Fit |
|---|---|---|---|---|---|
| Twelve Data | free 800/day; Grow $79/mo for NSE/BSE | yes, verified (Grow) | yes | official | 3 |
| FMP | free 250/day US; Ultimate $99/mo global | not verified | yes | official remote; community local | 3 |
| EODHD | free 20/day; $59.99/mo fundamentals | not verified | yes (disable 3 report tools) | official | 3 |
| edgartools / SEC EDGAR MCP | free | no (US filings) | yes | community (edgartools MIT; sec-edgar-mcp AGPL) | 3 |
| Alpha Vantage | free 25/day; premium paid | BSE prices yes; fundamentals not verified | yes | official | 2 |
| Financial Datasets | $20 per 1k; $200/mo | no | yes | official | 2 |
| Massive (ex-Polygon) | free 5/min; $29+/mo | no | yes | official | 2 |
| Yahoo Finance MCP | free | yes (Yahoo data) | yes | community, unofficial | 1 |
| Finnhub | free US; $3,500/mo global | no on free | yes | community | 1 |
| Tiingo | free; $30/mo | no | yes | community | 1 |

## Parts
| Part | Covers |
|---|---|
| [overview.md](mcp-market-data/overview.md) | Key answers (MCP vs our scripts, India, paid options), MCP registry check, safety notes |
| [official-vendors.md](mcp-market-data/official-vendors.md) | 1-4: Financial Datasets, Massive (ex-Polygon), Alpha Vantage, EODHD |
| [other-vendors.md](mcp-market-data/other-vendors.md) | 5-10: Finnhub, FMP, Yahoo Finance MCPs, SEC EDGAR MCPs, Twelve Data, Tiingo |
