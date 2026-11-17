# MCP market data: key answers, registry and safety

Checked 2026-11-15. Research only: nothing installed, no accounts, no MCP server run.
"MCP" = Model Context Protocol: a server that exposes a data API as tools an AI session can call.
Repo stats from the GitHub API on 2026-11-15 (stars / open issues / last push / licence).

Back to the index: [MCP servers for market data](../mcp-market-data.md)

## Summary
- An MCP adds no new data over our direct scripts; for yfinance and EDGAR it is worse.
- No low-cost source gives verified NSE/BSE fundamentals; keep screener.in and NSE bhavcopy for India.
- Registry has official Alpha Vantage, Twelve Data and Financial Datasets; India-specific servers are unverified.
- All candidates are data-only (no broker scopes); prefer header or OAuth keys, never `?apikey=` URLs.

## Key answers
- What an MCP adds over our scripts: the session can call the API as a tool without us writing
  a script per endpoint, and some servers carry their own API docs. It adds no new data: the
  data, limits and errors are the vendor's. For yfinance and EDGAR (free, already scripted,
  quirks already noted in `research/sources.md`) an MCP wrapper adds little and hides the
  checks we rely on (TZ=UTC for dates, recomputing P/E from company figures).
- Cost side: every tool list is loaded into the session context (FMP community server: 267 tools;
  EODHD: 88), results are not cached to disk, and one remote outage blocks a run. Scripts keep
  a file trail that agents and the journal can re-read.
- India: no low-cost vendor here gives verified NSE/BSE fundamentals. Cheapest verified NSE+BSE
  prices: Twelve Data Grow ($79/mo). Alpha Vantage free has BSE daily prices (`RELIANCE.BSE`).
  EODHD India coverage could not be verified (see below). screener.in (free, score 5) and the
  NSE bhavcopy stay better for India than any paid MCP.
- If we pay for one global fundamentals source later: FMP Ultimate ($99/mo annual, "Global
  coverage", official remote MCP) or EODHD Fundamentals ($59.99/mo) - test India tickers on
  the free tier first.

## Registry check
- Official registry (https://registry.modelcontextprotocol.io/v0/servers?search=..., 2026-11-15):
  official entries found for Alpha Vantage, Twelve Data, Financial Datasets. Massive, EODHD
  and FMP official servers were not found under their names. Many third-party wrappers
  (`pipeworx-io/*`, `mrfentmen/*`) re-wrap the same APIs - unofficial, skip.
- India-specific entries: `com.tapetide/stock-research-mcp` (NSE/BSE quotes, screener, FII/DII)
  and `com.bharatstockapi/bharatstock-mcp` (NSE/BSE, MFs). No repo, owner or data source
  verified; unknown terms. Not verified - do not use without checking where data comes from.
- The `modelcontextprotocol/servers` repo now holds only reference servers; the registry
  replaced its list (not re-checked in detail).

## Safety notes (all candidates)
- All are data-only: no broker login, no trading scopes. Fits the rule that agents never place
  orders. Only EODHD has non-read-only tools (Praams reports, emails out).
- Prefer header or OAuth auth; avoid `?apikey=` URLs (EODHD v1, FMP, AV legacy) - keys end up
  in logs. Keep keys in env vars outside git.
- Remote servers see every query (our watchlist and research topics). Local servers keep
  queries between us and the API vendor.
