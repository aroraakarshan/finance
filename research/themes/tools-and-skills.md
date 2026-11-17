# Tools and skills for the finance team: vetted

Written 2026-11-15 by `finance-research`. Docs, repos, pricing and terms read only: nothing was
installed, run, signed up for or connected. Agents never place, change or cancel orders
(`AGENTS.md`); every tool below is judged first on whether it can be strictly read-only. Details,
sources and dates are in the five group notes:

## Summary
- Adopt: IBKR Flex Web Service (free, read-only statements), NSE announcement RSS (poll daily), quantstats reports; optional TradingView paid MCP with write tools denied; Anthropic finance skills as templates only.
- Never connect: AngelOne SmartAPI (its token can trade), Dhan and Groww MCPs, Alpaca live keys, IBKR MCPs with order tools, Tickertape's AI link.
- You create every account and token yourself; keys stay in Keychain or environment variables, never in files.
- Respect site terms: no automated TradingView access; light single-page reads of screener.in and stockanalysis.

| Note | Covers |
|---|---|
| [tools/mcp-brokers-india.md](tools/mcp-brokers-india.md) | IBKR (Flex, TWS API, official MCP, community MCPs), Alpaca, Kite, Upstox, AngelOne SmartAPI, Dhan, Groww, NSE libraries |
| [tools/mcp-market-data.md](tools/mcp-market-data.md) | Financial Datasets, Massive (ex-Polygon), Alpha Vantage, EODHD, Finnhub, FMP, Twelve Data, Tiingo, Yahoo and EDGAR MCPs, MCP registry |
| [tools/agent-skills.md](tools/agent-skills.md) | anthropics/financial-services, anthropics/skills, awesome-copilot, community finance skills, OpenBB |
| [tools/web-tools.md](tools/web-tools.md) | TradingView (+ MCP), Trendlyne (+ MCP), Screener.in, stockanalysis, Finviz, Koyfin, Tickertape, Portfolio Visualizer, Morningstar, Value Research |
| [tools/libraries-and-news.md](tools/libraries-and-news.md) | vectorbt, backtrader, zipline-reloaded, backtesting.py, quantstats, pyfolio, riskfolio, TA-Lib; NewsAPI, GDELT, Finnhub, Marketaux, FinBERT, NSE/BSE feeds |

## 1. Key findings
- An MCP server adds convenience, not data. For Yahoo and SEC EDGAR our scripts are better: they
  keep our checks (TZ=UTC dates, caching, P/E recomputed from company figures).
- India: no cheap source gives verified NSE/BSE fundamentals by API. Screener.in and the NSE daily
  price file stay our best; Twelve Data (Grow, $79/mo) is the only API verified for NSE/BSE.
- Brokers: IBKR Flex Web Service is read-only by design. AngelOne SmartAPI (his Indian broker) has no
  read-only key: its token can trade. IBKR's official MCP drafts orders for approval and has an
  "Autonomous Trading" option that must never be enabled; IBKR says it is "not available in IN".
  Dhan and Groww MCPs place real orders; the code-rabi IBKR MCP has order tools on by default.
- Terms: TradingView forbids automated access to its site (we stopped fetching its news pages);
  stockanalysis allows robots.txt-following AI fetches but bans scripts; screener.in allows viewing
  only. `research/sources.md` now says this.
- Copilot CLI can block any tool by name: `--deny-tool='<server>(<tool>)'` wins over every allow.

## 2. Top 5 to adopt (ranked; the user decides)
| # | What | Cost | Used by (stage) | Why |
|---|---|---|---|---|
| 1 | IBKR Flex Web Service (statements, trades, positions as XML) | free | finance-main, -journal, -tax (stages 5, 7) | Read-only by design; replaces downloading Activity Statements by hand |
| 2 | NSE announcement RSS (`nsearchives.nseindia.com/content/RSS/*.xml`) plus Google/Bing News RSS | free, no key | finance-news, -scout (stages 1, 2) | Live India filings without scraping; already working |
| 3 | quantstats (Python, Apache-2.0) for backtest and portfolio reports | free | finance-trader, -journal (stages 4, 7) | Maintained, works on Python 3.13, drop-in for our engine's returns; finance-trader accepted it for later |
| 4 | TradingView paid plan with its official MCP, data tools only | from Rs 995/mo | user charts/alerts; finance-trader, -scout (stages 1, 4) | Best global + NSE charts and screens; no order tools; personal-use terms |
| 5 | Anthropic `financial-services` skills as templates (comps, DCF, earnings) | free | finance-research (stage 3) | Good methods to copy into our own skills; do not install its 12 paid MCP data connectors |

Alternatives to #4 for India-only data: Trendlyne MCP (Rs 299-499/mo). Paid global fundamentals
(FMP $99/mo, EODHD $59.99/mo) only after testing India tickers on a free key.

## 3. Setup steps the user does (no credentials in any file)
1. IBKR Flex: Client Portal -> Performance and Reports -> Flex Queries -> create an Activity Flex Query
   (trades, positions, cash, dividends); then Flex Web Service -> generate a token. Keep the token in
   macOS Keychain or an environment variable on each Mac, never in the repository. finance-main adds
   a reader script (`scripts/brokers/ibkr.py`) that takes the token from the environment.
2. NSE RSS: nothing to set up; finance-news adds the feed URLs to its scan.
3. quantstats: finance-main adds it to `requirements.txt` when finance-trader asks.
4. TradingView (optional, paid): the user subscribes and signs in to the MCP by OAuth himself; add the
   server to Copilot with `--deny-tool` for every watchlist/alert write tool, so sessions read only.
5. Skills: any new or changed skill goes through the `skills` session into `~/dotfiles` (rules).

## 4. Must stay read-only or off
- Never connect AngelOne SmartAPI, Dhan, Groww, Alpaca live keys, or any IBKR MCP with order tools to a
  session. If an IBKR MCP is ever used: TWS/IB Gateway "Read-Only API" ticked, order tools denied with
  `--deny-tool`, and the official MCP's Autonomous Trading never enabled.
- Tickertape's AI link can place US trades: do not connect it.
- Broker tokens and API keys live only in the user's keychain or environment, never in files.

## 5. Tax
None of these tools has a tax effect; paid subscriptions are personal expenses (no deduction for a
salaried person). No `finance-tax` line needed.


Update 2026-11-15 (finance-scout feed test, scout/sources-notes.md): all NSE RSS feeds return HTTP 200, but each holds only about the last day, so a weekly scan needs daily polling or the NSE filing pages; the insider-trading RSS stops at 2 May 2026 (insider data moved to the XBRL feed api/corporates-pit-gg) and the financial-results RSS is sparse (3 items, newest 3 Nov).
