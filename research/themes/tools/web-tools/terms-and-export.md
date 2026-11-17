# Web tools: terms, agent access and manual export

Checked 2026-11-15. Back to the index: [web-tools.md](../web-tools.md).

## Summary
- TradingView: no scraping at all; only its official MCP, for the user's own use.
- stockanalysis: web_fetch (robots.txt-following agent) is allowed; scripts are not.
- screener.in: viewing-only licence; keep agent reads per symbol and light.
- Manual CSV export into Drive is fine for screener.in, Finviz, stockanalysis, Portfolio
  Visualizer; not for TradingView. Act on the sources.md discrepancies below.

## Key findings (terms)
- TradingView now has an official MCP server (Essential plan and up): read-only screener,
  OHLCV, fundamentals, news, calendars, plus write tools for watchlists and alerts; no order
  tools. Terms allow it only for one person's own AI client, display to that person, no
  database building, no automated decisions (TradingView /mcp/docs and /policies s.27).
- TradingView terms forbid any robot/scraper/automated access to its site (s.3 and the
  "robot, spider, scraper" clause, /policies). Our `research/sources.md` rows that fetch
  tradingview.com/news pages (RNS copies) break this: stop and use RNS/company IR instead.
- stockanalysis.com bans scripts, curl and browser automation but exempts "AI agents ...
  that follow our robots.txt" (terms "Automated access"). web_fetch of /stocks/ pages is
  within that; plain-curl scripts are not.
- screener.in licence is "personal, non-commercial transitory viewing", no copying or
  mirroring (screener.in/guides/terms/). robots.txt does not block /company/ or /api/. Light
  per-symbol agent reads for the user's own notes are a grey zone; bulk pulls are not OK.
- Trendlyne sells an India MCP (Rs 299-499/month) for individuals; its site terms forbid
  putting its data in a machine-readable database without written permission.
- Manual export (user downloads, scripts read the file) is clean for screener.in Premium,
  Finviz Elite, stockanalysis Pro and Portfolio Visualizer. Not for TradingView: its licence
  bans any machine processing of its data outside the MCP exception.

## Manual-export pattern
Right pattern where terms allow processing a downloaded file: user downloads the CSV/XLSX
into Drive, scripts read it, output keeps a source and date. Use it for screener.in Premium,
Finviz Elite, stockanalysis Pro and Portfolio Visualizer. Do not use it for TradingView
exports (licence is display-only; machine processing banned except via MCP). Agents should
never hold logins to these sites.

## Discrepancies to act on
- `research/sources.md` lines 64, 106, 108 (rows naming TradingView news) use TradingView news pages via fetch: against
  TradingView terms; finance-main should drop them for RNS/company IR or the MCP.
- `research/sources.md` line 101 calls screener.in via curl: allowed by robots.txt, but the
  licence is viewing-only; keep it per symbol and low volume.
