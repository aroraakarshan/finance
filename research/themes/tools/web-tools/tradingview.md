# Web tools: TradingView

Checked 2026-11-15. Back to the index: [web-tools.md](../web-tools.md).

## Summary
- Free charts, screeners, Pine backtests and paper trading; NSE real-time needs a paid plan.
- Official MCP (Essential, Rs 995/mo annual, and up): read-only data plus watchlist/alert
  write tools, no order tools; deny the write tools in our sessions.
- Terms: personal use only, no scraping, no stored datasets, no automated decisions.
- Use: user charts and alerts; finance-trader writes Pine strategies for the user. Fit 4.

## Details
- What: charts, screeners (stocks/ETF/crypto/bonds, "150+ exchanges from 50+ countries",
  "500+ fields"), Pine Script indicators and strategy backtests, alerts, paper trading, news.
- Cost (annual billing, India page): Basic free; Essential Rs 995/mo; Plus Rs 2,095/mo;
  Premium Rs 4,195/mo; Ultimate Rs 17,333/mo. USD list (JSON on the page): 14.95 / 34.95 /
  69.95 / Expert 119.95 / 239.95 per month (tradingview.com/pricing, 2026-11-15).
- Limits: alerts Basic 3 price / 0 technical, Essential 20+20, Plus 100+100, Premium 400+400;
  historical bars 5K / 10K / 10K / 20K / 40K; minute history 180 days (Essential) and 365
  days (Plus); annual financials 7 years free, 20 years paid; quarterly 8 years (pricing).
  Webhook alerts, strategy CSV export and chart data export are listed as paid features;
  per-plan ticks are not readable in text: not verified which tier starts each.
- India data: NSE delayed 15 min free, real-time "included in paid plans"; BSE delayed
  15 min free, real-time Rs 422/month extra (tradingview.com/data-coverage, 2026-11-15).
- Paper trading: free for all users, most asset classes (support 43000516466).
- Webhooks: HTTP POST to ports 80/443, 3 s timeout, from 4 fixed IPs, no IPv6; may fail,
  check alert log (support 43000529348). Terms s.3 forbid using webhooks for automated
  trading or algorithmic decisions; a notification to the user is fine.
- Official API: no public market-data API found; the MCP server is the only sanctioned
  machine access. Server `https://mcp.tradingview.com/mcp`, OAuth 2.1 (log in with the
  TradingView account, no API keys), ~100 calls/min, trial plans excluded (/mcp/docs).
  Tools: 8 watchlist (5 write), get_ohlcv (max 5000 bars), run_screener (markets incl.
  india, japan, uk, germany, america), get_financials / history, forecasts, documents
  (annual/quarterly reports, insider transactions), news, earnings / economic / dividend
  calendars, 8 alert tools (create/update/delete/stop/restart). No broker or order tools.
- Copilot CLI can add it: `copilot mcp add --transport http <name> <url>`; OAuth opens a
  browser, token in the OS keychain (Copilot CLI 1.0.112 docs, topic mcp#authentication).
  Write tools (create/delete alerts and watchlists) should be denied in our sessions;
  TradingView itself says to require confirmation before changes (/policies s.27).
- Safety: read-only possible by tool permission, not by token scope (OAuth scope options
  not verified). No broker credentials needed. Maintainer: TradingView Inc. Closed source.
- Terms fit: MCP personal exception covers one user's own AI client answering the user.
  Writing MCP data into repo files every day looks like "build ... a dataset" (s.27):
  keep outputs to derived notes (signal, level, date), not raw price tables.
- Our use: user-side charts and alerts (stage 6 user); finance-trader writes Pine
  strategies in `trading/backtests/` for the user to paste and run (stage 4); finance-scout
  could run India/Japan screens through MCP if the user buys Essential and approves.
- Fit 4: best global charts/screens and an official read-only path; strict terms on reuse.
