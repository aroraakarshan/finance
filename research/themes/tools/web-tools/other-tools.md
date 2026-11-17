# Web tools: Finviz, Koyfin, Screener.in, Trendlyne, Tickertape, others

Checked 2026-11-15. Back to the index: [web-tools.md](../web-tools.md).

## Summary
- India: Trendlyne (MCP Rs 299-499/mo) and Screener.in (Premium Rs 4,999/yr) fit best (4).
- Global/US: stockanalysis.com stays (4, web_fetch only); Finviz and Portfolio Visualizer
  only via user exports (3).
- Do not connect agents to Tickertape (its AI link can place US trades).
- Koyfin, Morningstar India, Value Research: manual use only; Investing.com: skip.

## Finviz
- What: US stock/ETF screener, maps, charts, insider and news feeds.
- Cost: Free (delayed, 3 years statements, 20 rows/page); Elite $299.50/yr ($12.42/mo
  annual; Black Friday $149 first year), real-time, 8 years statements, exports, alerts
  (finviz.com/elite, 2026-11-15). Coverage US-listed only: not verified on a page today.
- Export: Elite page markets exports "to setup your own Automated Workflow / AI Agents".
  robots.txt disallows /export, /screener?* query pages and /api/v1/screener-export-csv.
  Terms of service page not found (404 on 3 URLs): not verified.
- Our use: optional US screen export for finance-scout (stage 1) via a user download.
  yfinance + EDGAR already cover most US needs. Fit 3.

## Koyfin
- What: dashboards, fundamentals, estimates, transcripts; "80,000 companies worldwide"
  (koyfin.com/data-coverage). India depth not verified.
- Cost: Free (2Y financials, 1Y estimates, 2 watchlists, 2 screens, limited snapshots);
  Plus $39/mo; Premium $79/mo; advisor plans $209-299/mo (koyfin.com/pricing). No public
  API or MCP found. Terms page is a JavaScript app: not verified.
- Our use: user's manual look-ups for Europe/Japan comps (stage 3). Fit 2: no API.

## Screener.in (already used)
- Cost: free "Hobby" (up to 50 companies in some feature, 10 vs 800 in another, 20/month
  limits); Premium Rs 4,999/yr with "Download Results" and "Excel Automation"
  (screener.in/premium, 2026-11-15; row labels not readable, mapping not verified).
- Quality (from research/sources.md, 2026-11-15): consolidated P/E, ROE, ROCE, 10-year
  financials work; ROE is last full year; its JSON APIs (peers, P/E history, shareholding)
  scored 5. Terms say data is built by automated algorithms and may contain errors.
- Terms: personal, non-commercial viewing; no copying or mirroring (guides/terms).
- Our use: finance-scout and finance-research (stages 1, 3) keep light per-symbol reads;
  for screens over many stocks, the user runs the screen and exports. Fit 4.

## Trendlyne
- What: India screener (DVM scores, "3500+ parameters"), forecasts, shareholding, alerts.
- Cost (INR, offer prices): GuruQ Rs 1,890/yr, StratQ Rs 4,950/yr, Pro Global Rs 7,500/yr,
  Pro Plus Global Rs 10,000/yr (trendlyne.com/subscription/plans).
- MCP: Pro Rs 299/mo (400 calls/day, 2,000/month), Max Rs 499/mo (1,000/day, 10,000/month,
  watchlist write tools); EOD prices, financials, technicals, shareholding, insider trades,
  results, presentations, earnings calls, annual reports. Not included: US data, mutual
  funds, F&O. "Pro and Max plans are for individual use only" (/subscription/mcp/plans).
  Auth method and token scope not verified (docs page did not show it in text).
- Terms: no use "in a searchable, machine-readable database" without written permission
  (trendlyne.com/terms s.6). Owner Giskard Datatech Pvt Ltd.
- Our use: strongest India data path for finance-scout/-research/-news (stages 1-3) if the
  user subscribes; deny watchlist write tools. Fit 4.

## Tickertape
- Cost: Pro Rs 399/month, Rs 899/3 months, Rs 2,999/year (tickertape.in/pricing).
- Terms: copy only for personal, non-commercial use; a connected "AI Application" can read
  holdings and may place US-stock transactions under Global Access, treated as the user's
  own instruction (tickertape.in/meta/terms). Owner Anchorage Technologies (smallcase group).
- Safety: do not connect our agents; order capability conflicts with our no-orders rule.
- Our use: user's own screens only. Fit 2.

## Portfolio Visualizer
- What: allocation backtests, Monte Carlo, optimisation, factor regression. Cost: Free (15 assets, limited history, no month-to-date); Basic $30/mo, Pro $55/mo
  (annual), Excel/CSV/PDF export (portfoliovisualizer.com/pricing). India assets not
  verified (US-centric). Terms: short, "limited, non-transferable licence", no scraping
  clause; owner now SRL Technical Solutions FZCO (terms, last modified 2025-09-25).
- Our use: finance-trader / finance-main manual allocation backtests of US/global ETFs
  (stage 4), user exports CSV. Fit 3.

## stockanalysis.com (already used)
- Cost: free; Pro $79/yr ($9.99/mo) with 1 download/day; Unlimited $16.58/mo annual
  (stockanalysis.com/pro). Global: "150,000+ global stocks and funds".
- Terms: no bots/scripts/scrapers/browser automation; AI agents following robots.txt are
  exempt; no competing database, no AI training; one person per account (terms-of-use).
  robots.txt blocks only /e/ and /p/.
- Our use: keep web_fetch per symbol (stages 1, 3); never log our agents into an account.
  Fit 4.

## Morningstar India, Value Research (mutual funds)
- Morningstar India terms: viewing for personal use; must not "systematically copy ...
  substantial parts of the Site" (morningstar.in/membership/termsofuse.htm). sources.md
  scores its pages 1 (403 to scripts). Fit 2.
- Value Research: homepage readable by web_fetch; Fund Advisor Rs 4,900/yr, Stock Advisor
  Rs 9,990/yr; terms page 404, curl 403 (valueresearchonline.com). sources.md scores 1.
  For fund data, mfapi and AMFI already work. Fit 2.

## Investing.com
- Terms page: sign-up overlay (web_fetch), 403 (curl); terms not verified. Fit 1: skip.
