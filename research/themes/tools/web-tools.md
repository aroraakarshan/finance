# Web research tools: screeners, charts, backtests (checked 2026-11-15)

Which web tools to use for screens, charts, alerts and backtests, and what their terms allow
our agents to do. No accounts made. Prices as seen 2026-11-15 (some are sale prices).

## Summary
- Best fits (4): TradingView (official MCP, Rs 995/mo+), Trendlyne (India MCP, Rs 299/mo+),
  Screener.in and stockanalysis.com (already used).
- TradingView forbids scraping: drop the sources.md rows that fetch its news pages.
- Agents get read-only tools only; no logins to these sites; no Tickertape AI link.
- For bulk data, the user exports CSV into Drive and scripts read it (not TradingView).

## Ranking
| Candidate | Cost | India? | Read-only possible | Maintainer | Fit |
|---|---|---|---|---|---|
| TradingView (+ official MCP) | Free; MCP from Rs 995/mo | Yes, NSE 15-min free, RT paid | Yes, deny write tools | TradingView Inc. | 4 |
| Trendlyne (+ MCP) | Rs 1,890-10,000/yr; MCP Rs 299-499/mo | Yes (MCP India only) | Yes, deny watchlist writes | Giskard Datatech | 4 |
| Screener.in | Free; Rs 4,999/yr | Yes | Yes (no account for agents) | Screener.in | 4 |
| stockanalysis.com | Free; $79/yr | Some (global listings) | Yes (web_fetch only) | Vefir ehf. | 4 |
| Finviz | Free; $299.50/yr | No (US) | Yes (user export) | Finviz.com | 3 |
| Portfolio Visualizer | Free; $30-55/mo | Not verified | Yes (user export) | SRL Technical Solutions | 3 |
| Koyfin | Free; $39-79/mo | Claimed, not verified | Yes (manual only) | Koyfin | 2 |
| Tickertape | Free; Rs 2,999/yr | Yes | No for AI link (can trade) | Anchorage Technologies | 2 |
| Morningstar India | Free | Yes (MF) | Manual only | Morningstar | 2 |
| Value Research | Free; Rs 4,900-9,990/yr | Yes (MF) | Manual only | Value Research | 2 |
| Investing.com | Free | Yes | Not verified | Investing.com | 1 |

## Parts
| Part | Contents |
|---|---|
| [web-tools/tradingview.md](web-tools/tradingview.md) | Plans, limits, NSE/BSE data, webhooks, paper trading, official MCP tools and terms |
| [web-tools/other-tools.md](web-tools/other-tools.md) | Finviz, Koyfin, Screener.in, Trendlyne, Tickertape, Portfolio Visualizer, stockanalysis, Morningstar, Value Research, Investing.com |
| [web-tools/terms-and-export.md](web-tools/terms-and-export.md) | Key terms findings, manual-export pattern, discrepancies to act on |

Sources: URLs and check dates are given inline in each part.
