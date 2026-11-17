# Communication services: sources

Part of [communication services](README.md). All read 2026-11-15 unless a date is given.

## Summary

- Prices and correlations from Yahoo (yfinance); stock ratios from stockanalysis and screener.in; sector P/E vs history from FactSet.
- News from Bing News RSS, then the article itself where it opened.
- Not found: a Nifty Media P/E or price history, and 10-year P/E averages outside the US.

## Source list

| Tag | Source | Used for |
|---|---|---|
| C1 | Yahoo Finance via yfinance (auto-adjusted closes to 2026-11-13; monthly returns Nov 2021-Nov 2026 for correlations) | Returns, prices, correlations |
| C2 | stockanalysis.com statistics pages (GOOGL, META, TMUS, VZ, NFLX, ETR:DTE, TYO:9432/9433/9434, HKG:0700, SGX:Z74), data from S&P Global, updated 2026-11-15 | P/E, EV/EBITDA, cash flow, share counts |
| C3 | screener.in consolidated pages (BHARTIARTL, JPL, NAUKRI, ETERNAL, IDEA) and the Bharti P/E chart API, 2026-11-13 prices | Indian P/E, EPS, P/E history |
| C4 | FactSet Earnings Insight, 13 Nov 2026 (advantage.factset.com/.../EarningsInsight_111326.pdf), text and charts | US sector forward P/E vs 5y/10y, 2026-27 growth |
| C5 | justETF profile IE00BM67HR47 (holdings as of 29 Sep 2026) | XWTS facts: Irish, accumulating, TER 0.25%, EUR 361 m, 60 holdings, listings |
| C6 | Moneycontrol, "Jio shares make blockbuster debut...", 28 Oct 2026 | Jio IPO price, listing, targets |
| C7 | Livemint, "DoT freezes Vodafone Idea's AGR dues...", 9 Jan 2026 | Vi AGR schedule |
| C8 | Hindu BusinessLine, "Vodafone Idea Q2 loss widens...", 12 Nov 2026 | Vi Q2 FY27 |
| C9 | Fortune India, "Telcos may hike tariffs 15% in December...", 22 Oct 2026 (Ambit Capital note of 21 Oct) | Tariff forecast |
| C10 | CNBC-TV18, "Bharti Airtel Q2 Results...", 5 Nov 2026 (year-on-year figures from other headlines the same day) | Airtel Q2 FY27 |
| C11 | Goodreturns, "Alphabet Q3 Results...", 29 Oct 2026 | Alphabet Q3 2026 |
| C12 | Fortune India, "Meta plans up to $95 billion equity raise...", 27 Oct 2026 | Meta capex and share sales |
| C13 | Livemint, Netflix 17 Jul 2026 (guidance) and 27 Feb 2026 (WBD exit) | Netflix |
| C14 | Zacks via Yahoo Finance, "T-Mobile Falls 18.2% in 3 Months...", 30 Oct 2026 | T-Mobile Q3 2026 |
| C15 | Simply Wall St via Yahoo Finance, Tencent, 4 Nov 2026; Yahoo headline 11 Nov 2026 (US remote AI-chip curbs) | Tencent |
| C16 | Yahoo `Ticker.info` (forward P/E, EPS, ETF P/E, FX), 2026-11-15 | Second source; marked "not verified" where used alone |
| C17 | tax/investment-types.md, tax/new-investments.md | Tax lines, withholding rates |
| C18 | Bing News RSS headlines only (bodies not read): Jio DRHP 19 Jun 2026, SEBI nod 28-29 Aug 2026; Sunil Mittal 12 Nov 2026; Alphabet -10% 28-29 Oct 2026; India CPI above 6% (BusinessLine, 12-13 Nov 2026) | Dated events |

## Sources tried

| Source | URL | Result | Score (1-5) |
|---|---|---|---|
| yfinance | Python package | Worked; KDDI forward EPS wrong, Tencent mixes HKD/CNY, ^CNXMEDIA has one day | 4 |
| stockanalysis | stockanalysis.com/stocks/..., /quote/(tyo, etr, hkg, sgx)/... (web_fetch) | Worked for all 11 pages, incl. SGX:Z74 | 4 |
| screener.in | screener.in/company/<SYM>/consolidated/ (5 light reads) and /api/company/467/chart/ | Worked | 5 |
| FactSet Earnings Insight PDF | advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_111326.pdf | Worked (111326 and 110626 exist; 110926 404); sector P/E only in chart images | 5 |
| FactSet Insight blog | insight.factset.com | Worked; sector numbers only in images | 4 |
| justETF | justetf.com/en/etf-profile.html?isin=IE00BM67HR47 | Worked | 5 |
| niftyindices P/E API | niftyindices.com/Backpage.aspx/getpepbHistoricaldataDBtoString | Blocked: returns the HTML home page even with a session cookie | 2 |
| Bing News RSS | bing.com/news/search?format=rss&q=... | Worked | 5 |
| Moneycontrol, Livemint, BusinessLine, CNBC-TV18, Fortune India, Goodreturns | article pages | Worked | 4 |
| Yahoo Finance articles (Zacks, Simply Wall St) | finance.yahoo.com/markets/stocks/articles/... | Worked | 3 |
| MSN | msn.com/en-us/money/... | Blocked: raw page shell, no text | 1 |
