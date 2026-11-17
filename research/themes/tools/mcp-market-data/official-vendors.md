# MCP market data: Financial Datasets, Massive, Alpha Vantage, EODHD

Checked 2026-11-15. Research only: nothing installed, no accounts, no MCP server run.
"MCP" = Model Context Protocol: a server that exposes a data API as tools an AI session can call.
Repo stats from the GitHub API on 2026-11-15 (stars / open issues / last push / licence).

Back to the index: [MCP servers for market data](../mcp-market-data.md)

## Summary
- Financial Datasets and Massive (ex-Polygon) are US-only; fit 2.
- Alpha Vantage free is 25 requests/day with BSE daily prices; fit 2.
- EODHD is the cheapest global fundamentals ($59.99/mo) but India coverage is not verified; fit 3.
- Test India tickers on a free key before paying for EODHD.

## Candidates 1-4

### 1. Financial Datasets (financialdatasets.ai) - official
- Does: US fundamentals, prices, SEC filings, insider/13F, news; screener; remote MCP
  `https://mcp.financialdatasets.ai/` (registry entry `ai.financialdatasets/mcp`, published
  2026-11-04). Old local repo `financial-datasets/mcp-server`: 2326 / 16 / 2025-06-05 / MIT -
  stale 17 months; use the remote one. https://github.com/financial-datasets/mcp-server
- Cost: $20 one-time for 1,000 requests; Personal $200/mo (100k); Professional $1,000/mo.
  https://www.financialdatasets.ai/pricing (2026-11-15)
- Coverage: 27,000+ US tickers incl. delisted; international = annual fundamentals for UK and
  France only. No India, Japan, other Asia. (pricing page, registry entry, 2026-11-15)
- Safety: read-only data; API key in `X-API-KEY` header or `.env`. No broker scopes.
- Use: finance-research (stage 3) for US names. Fit 2: good US data but costly and US-only.

### 2. Massive (formerly Polygon.io) - official
- Rebrand verified: `polygon.io` 301-redirects to `massive.com`; repo `polygon-io/mcp_polygon`
  moved to `massive-com/mcp_massive` (2026-11-15).
- Does: 3 generic tools (search / call any endpoint / SQL query on stored results). Hosted at
  `https://mcp.massive.com` or local `uv tool install`. Repo: 402 / 15 / 2026-11-03 / MIT.
  https://github.com/massive-com/mcp_massive
- Cost: Basic $0 (5 calls/min, 2 years, end of day); Starter $29/mo (5 yrs, 15-min delay);
  Developer $79/mo. https://massive.com/pricing (2026-11-15)
- Coverage: "All US Stocks Tickers"; options, crypto, FX. No India/Europe/Japan stocks.
- Data: corporate actions and reference data even on free tier; fundamentals not checked.
- Safety: read-only; key in env `MASSIVE_API_KEY`. No broker link.
- Use: finance-trader backtests (stage 4) on US names. Fit 2: US only; yfinance covers our need.

### 3. Alpha Vantage - official
- Does: every AV function as a tool. Remote `https://mcp.alphavantage.co/mcp` with OAuth
  (key entered in a browser page); local `uvx marketdata-mcp-server <KEY>` (key on the command
  line - visible in process list). Old `?apikey=` URL deprecated. Repo: 227 / 3 / 2026-10-03 /
  MIT. https://github.com/alphavantage/alpha_vantage_mcp
- Cost: free 25 requests/day; premium for more and for real-time US.
  https://www.alphavantage.co/premium/ (2026-11-15)
- Coverage: global daily prices; docs show `RELIANCE.BSE` (BSE). NSE suffix and India
  fundamentals not verified. https://www.alphavantage.co/documentation/ (2026-11-15)
- Safety: read-only. Fit 2: 25/day is too small for screens; free BSE prices are a small plus.

### 4. EODHD (EOD Historical Data) - official
- Does: 88 tools, 85 read-only; 3 "Praams report" tools are not read-only (they trigger
  report generation and email) - leave them off. Embedded API docs as MCP resources.
  Remote v1 `https://mcp.eodhd.com/v1/mcp?apikey=` (key in URL, logged) or v2 OAuth; local
  Python with `EODHD_API_KEY` env. Repo: 24 / 11 / 2026-10-22 / MIT.
  https://github.com/EodHistoricalData/EODHD-MCP-Server,
  https://eodhd.com/financial-apis/mcp-server-for-financial-data-by-eodhd (2026-11-15)
- Cost: free 20 calls/day, 1 yr history; EOD All-World $19.99; EOD+Intraday $29.99;
  Fundamentals $59.99; All-in-one $99.99/mo. Fundamentals cost 10 calls each.
  https://eodhd.com/pricing (2026-11-15)
- Coverage: "60+ exchanges", fundamentals since 2000 for non-US. India: NOT VERIFIED - the
  public exchange list (https://eodhd.com/list-of-stock-markets, 2026-11-15) shows 63 entries
  with no NSE, BSE, Tokyo, Hong Kong or London (but LSE is used in their own docs, so the
  page is incomplete); the demo key returned "Forbidden". Check `RELIANCE.NSE` on a free key
  before paying.
- Use: finance-scout screens (stage 1) and finance-research (stage 3), all 5 markets if India
  holds. Fit 3: best price for global fundamentals; India unknown, small repo.
