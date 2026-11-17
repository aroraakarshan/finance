# MCP market data: Finnhub, FMP, Yahoo, EDGAR, Twelve Data, Tiingo

Checked 2026-11-15. Research only: nothing installed, no accounts, no MCP server run.
"MCP" = Model Context Protocol: a server that exposes a data API as tools an AI session can call.
Repo stats from the GitHub API on 2026-11-15 (stars / open issues / last push / licence).

Back to the index: [MCP servers for market data](../mcp-market-data.md)

## Summary
- Twelve Data is the only vendor with verified NSE+BSE access by plan (Grow $79/mo); fit 3.
- FMP has an official remote MCP; Ultimate $99/mo is "Global" but India is not verified; fit 3.
- Yahoo MCPs add nothing over our direct yfinance; edgartools is useful as a Python library.
- Finnhub (global $3,500/mo) and Tiingo (no India) do not fit; fit 1.

## Candidates 5-10

### 5. Finnhub
- No official MCP. Community: `cyanheads/finnhub-mcp-server` (registry), `cfdude/mcp-finnhub`
  11 / 0 / 2026-11-01 / MIT; `SalZaki/finnhub-mcp` 7 stars / 183 open issues - avoid.
- Cost: free 60 calls/min, US fundamentals, 1 yr company news; global = All-In-One $3,500/mo.
  https://finnhub.io/pricing (2026-11-15)
- Coverage: free = US only. Fit 1: global fundamentals priced for firms.

### 6. Financial Modeling Prep (FMP) - official remote MCP exists
- Official: remote `https://financialmodelingprep.com/mcp`, key in `X-API-Key` header
  (preferred) or `?apikey=`; OAuth connectors for Claude/ChatGPT; wraps all REST endpoints.
  No public repo for it. https://site.financialmodelingprep.com/developer/docs/mcp-server
  (2026-11-15). Community: `imbenrabi/Financial-Modeling-Prep-MCP-Server` 149 / 1 /
  2026-11-05 / Apache-2.0 (267 tools; can load only chosen toolsets, which saves context).
- Cost: Basic $0 (250 calls/day, 5 yrs, many endpoints limited to ~87 US symbols); Starter
  $19/mo annual (US); Premium $49/mo (US, UK, Canada, 30 yrs); Ultimate $99/mo annual
  ($139 monthly) "Global coverage", transcripts, ETF holdings, bulk.
  https://site.financialmodelingprep.com/pricing-plans (via r.jina.ai, 2026-11-15)
- Coverage: India (.NS/.BO) on Ultimate not verified (demo key rejected).
- Use: finance-research and finance-scout. Fit 3: one paid key for global fundamentals; India
  must be tested.

### 7. Yahoo Finance MCPs (community, yfinance-based)
- `Alex2Yang97/yahoo-finance-mcp` 370 / 12 / 2026-09-19 / MIT (unofficial; wraps yfinance via
  `uvx`). Also `wshobson/maverick-mcp` 728 / 10 / 2026-11-13 / MIT (bigger analysis kit).
  https://github.com/Alex2Yang97/yahoo-finance-mcp
- Cost free; no key. Coverage = Yahoo (all 5 markets incl. `.NS`/`.BO`).
- Versus our direct yfinance: same data, same 429s, same wrong non-US EPS/P/E (sources.md
  score 2 for `Ticker.info`) and the same local-timezone date trap - but the agent cannot set
  TZ=UTC or cache. Yahoo terms do not allow this use officially (not verified in detail).
- Fit 1: nothing gained; keep the direct scripts.

### 8. SEC EDGAR MCPs (community)
- `stefanoamorelli/sec-edgar-mcp` 387 / 13 / 2026-11-01 / AGPL-3.0 (copyleft; fine for
  personal local use). Needs `SEC_EDGAR_USER_AGENT`; returns filing URLs.
  https://github.com/stefanoamorelli/sec-edgar-mcp
- `dgunning/edgartools` 2854 / 33 / 2026-11-15 / MIT: Python library with a local MCP server
  in its `ai` extra, plus hosted `app.edgar.tools/mcp`. Parses XBRL statements, 8-K items,
  Form 4. https://github.com/dgunning/edgartools
- Versus our direct EDGAR (submissions API, score 5): adds XBRL parsing into statements; the
  full-text search (efts.sec.gov) still returns 403 for us, so MCPs using it may fail too.
- Use: finance-news (8-K/10-Q, stage 2), finance-research (stage 3). Fit 3 for edgartools as
  a Python library (no MCP needed); MCP itself optional.

### 9. Twelve Data - official
- Remote `https://mcp.twelvedata.com/mcp` with OAuth login (no key pasted); or local with
  `TWELVE_DATA_API_KEY` in a chmod 600 `.env`. Repo: 86 / 6 / 2026-10-01 / no licence file
  shown by the API. https://github.com/twelvedata/mcp
- Cost: Basic free 8/min, 800/day (internal non-display use, US real-time); Grow $79/mo
  (27 markets, EOD global, fundamentals); Pro $229/mo (76 markets); Ultra $999/mo.
  https://twelvedata.com/pricing (2026-11-15)
- Coverage verified from `api.twelvedata.com/exchanges?show_plan=true` (2026-11-15): NSE (XNSE)
  and BSE (XBOM) need Grow; Tokyo (XJPX) needs Pro. Fundamentals depth for India not verified.
- Fit 3: only vendor with verified NSE+BSE access by plan; Japan needs $229.

### 10. Tiingo (brief)
- No official MCP; community `major7apps/tiingo-mcp` 12 / 1 / 2026-11-09 / MIT.
- Cost: free tier; Power $30/mo individual. Coverage "US & Chinese stocks", 30+ yrs prices.
  https://www.tiingo.com/about/pricing (2026-11-15). Fit 1: no India/Europe/Japan.
