# Industrials: sources and gaps

Written 2026-11-15 by `finance-research`. Back to the index: [README.md](README.md).

## Summary
- Where each source tag in the parts comes from, with URL and date. News items marked "headline" were read
  from the headline only; treat their numbers as not verified.
- Gaps lists what could not be verified; treat those numbers as missing.

## 7. Sources
Data
- [Y] Yahoo Finance via yfinance 1.8.0: daily closes to 13-Nov-2026, trailing EPS, net income, market cap,
  consensus EPS (`earnings_estimate`, read 2026-11-15). Trailing P/E recomputed and checked against market cap /
  net income; L&T trailing EPS checked as the sum of 4 reported quarters (37.80 + 29.96 + 38.70 + 23.36).
- [SA] stockanalysis.com statistics and ratio-history pages (web_fetch, 2026-11-15): LMT, BAE (lon/BA), Saab
  (sto/SAAB.B), Safran (epa/SAF), Mitsui (tyo/8031), Mitsubishi Corp (tyo/8058), L&T (nse/LT).
- [JE] justETF profiles, 2026-11-15: XDWI https://www.justetf.com/en/etf-profile.html?isin=IE00BM67HV82 (holdings
  as of 29-Sep-2026); DFNS https://www.justetf.com/en/etf-profile.html?isin=IE000YYE6WK5.
- [G] Groww ETF and fund pages (embedded page data), 2026-11-15: groww.in/etfs/motilal-oswal-nifty-india-defence-etf,
  /etfs/groww-nifty-india-defence-etf, /etfs/icici-prudential-nifty-infrastructure-etf,
  /mutual-funds/motilal-oswal-nifty-india-defence-index-fund-direct-growth.
- [NSE] NSE daily price file 13-Nov-2026: https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20261113_F_0000.csv.zip
- [OIM] [opp-india-market](../../themes/opp-india-market.md) and its [sectors part](../../themes/opp-india-market/sectors.md)
  (niftyindices P/E data 13-Nov-2026; Nifty Capital Goods factsheet 30-Oct-2026).
- [OST] [opp-sectors-themes](../../themes/opp-sectors-themes.md): areas and backdrop-scorecard parts (CSIS 2026-07-06,
  PIB 2026-11-11, Bloomberg headline 2026-11-04, ITA trailing P/E).
- [FS] FactSet Insight 2026-11-09 (sector forward P/E vs 10-year average, as of 2026-11-05), as quoted in
  [backdrop-scorecard](../../themes/opp-sectors-themes/backdrop-scorecard.md):
  https://insight.factset.com/lowest-forward-12-month-p/e-ratio-for-the-sp-500-in-more-than-3-years
- Tax lines: [tax/investment-types.md](../../../tax/investment-types.md), [tax/new-investments.md](../../../tax/new-investments.md)
  (withholding by country: US 25%, UK 0%, France 12.8% -> 10%, Japan 15.315% -> 10%).

News (found through Bing News RSS; date = publication date)
- N1 Financial Express, L&T Q2 FY27, 2026-10-27: https://www.financialexpress.com/business/industry-lampt-q2-results-net-profit-jumps-32-to-rs-5202-crore-order-inflows-rise-28-4370653/
- N2 Financial Express, HAL, 2026-11-13: https://www.financialexpress.com/market/hal-should-you-buy-or-hold-brokerages-split-on-tejas-ramp-up-rs-2-5-lk-cr-order-backlog-4383666/
- N3 CNBC-TV18, BHEL Q2, 2026-10-14 (headline): https://www.cnbctv18.com/market/bhel-q2-results-all-round-beat-revenue-growth-margin-expands-order-inflow-execution-psu-share-price-move-200 ; Adani order, Whalesbook 2026-11-04 (headline)
- N4 BusinessWorld, Mazagon Dock Q2, 2026-10-26/27 and BDL Q2, 2026-11-11 (headlines): https://www.businessworld.in/article/mazagon-dock-q2-profit-falls-54-to-rs-344-crore-as-margins-collapse-630885 , https://www.businessworld.in/article/bharat-dynamics-q2-revenue-jumps-45-profit-falls-15-to-rs-183-cr-633304 ; TradeBrains order-book headline 2026-11-02
- N5 BusinessWorld / Business Standard, Hitachi Energy India Q2, 2026-11-11/12 (headlines): https://www.businessworld.in/article/hitachi-energy-india-q2-results-order-backlog-hits-record-rs-33-335-cr-as-grid-investment-drives-demand
- N6 CNBC-TV18, ABB India Q3 2026-11-13 and Siemens Q2 2026-11-06 (headlines): https://www.cnbctv18.com/market/stocks/abb-india-share-price-q3-results-net-profit-rises-8-as-revenue-grows-19-record-orders-lift-backlog-20
- N7 Business Standard / CNBC-TV18 / Free Press Journal, Cummins India Q2, 2026-11-04 (headlines)
- N8 Financial Express, BEL order book, 2026-10-13; MSN/Business Standard, BEL guidance, 2026-11-03 (headlines; bodies 403)
- N9 Yahoo UK / MarketScreener, BAE trading update, 2026-11-11/12 (headlines): https://uk.finance.yahoo.com/news/bae-systems-lifts-free-cash-072300447.html
- N10 Eurasia Business News, Rheinmetall guidance cut, 2026-11-06: https://eurasiabusinessnews.com/2026/11/06/rheinmetall-shares-plunge-after-german-defence-giant-cuts-2026-forecasts/
- N11 Yahoo Finance, Lockheed USD 292 bn backlog, 2026-10-23 (headline)
- N12 MSN / Top1Markets, RTX record backlog and raised guide, 2026-10-20/11-01 (headlines)
- N13 PR Newswire, General Dynamics Q3, 2026-10-30; MSN USD 220 bn backlog headline: https://www.prnewswire.com/news-releases/general-dynamics-reports-third-quarter-2026-financial-results-302924010.html
- N14 StockTitan (GE 8-K), 2026-10-20; Yahoo "GE sinks 2%" 2026-10-20; MarketScreener / Reuters, Safran Q3, 2026-10-22 (headlines)
- N15 MSN / Aerotime, Saab Q3 orders and backlog, 2026-10-23/27 (headlines)
- N16 Yahoo Finance / MarketScreener, Thales 9-month sales, 2026-10-21 (headlines)
- N17 Yahoo Finance (Investing.com), Mitsubishi Heavy H1, 2026-11-06: https://finance.yahoo.com/markets/stocks/articles/mitsubishi-heavy-shares-slide-8-060459972.html
- N18 TradingKey 2026-09-01, MSN 2026-09-03, Moneycontrol 2025-03-18 (Berkshire and Japan trading houses; headlines)
- N19 Air Data News, Airbus October deliveries, 2026-11-06: https://www.airdatanews.com/airbus-delivers-74-aircraft-in-october-needs-249-more-to-meet-2026-target/
- N20 Bursa (citing CNBC and SIPRI), 2026-11-06: https://www.bursa.ro/the-rearmament-paradox-military-budgets-rise-as-major-arms-manufacturers-shares-plunge-84149064
- N21 Seoul Economic Daily, Hanwha Q3, 2026-10-29; FN News, Korean defence slide, 2026-11-05 (headlines)
- N22 News18, Budget 2026 capex, 2026-01-31: https://www.news18.com/business/economy/budget-2026-spending-push-govt-capex-to-be-increased-to-rs-12-2-lakh-crore-in-fy27-says-fm-9871416.html ; Whalesbook 2026-11-02 (headline)
- N23 Financial Express, Railway Budget 2026, 2026-02-01 (headline)
- N24 BusinessLine, RBI private capex estimate, 2026-09-25 (headline): https://www.thehindubusinessline.com/economy/indias-private-capex-estimated-at-32-lakh-crore-in-2026-27-rbi/article71510206.ece
- N25 News18 and NDTV, NATO 5%, 2026-07-10: https://www.news18.com/world/nato-pushes-for-5-of-gdp-spending-for-defence-how-many-members-are-following-this-10204696.html
- N26 The Hawk 2026-11-02 and Business Standard 2026-11-03, India defence budget and 2029 targets (headlines)
- N27 Moneycontrol / MSN, IndiGo Q2 FY27, 2026-10-29 (headlines)

## Gaps (not verified)
- MSCI World Industrials and Europe industrials P/E and their 10-year averages (no free source found); the US
  FactSet figure is used as a proxy for XDWI.
- Nifty India Defence and Capital Goods 10-year history (indices too new); TERs of INFRABEES, CPSEETF, MANUFGBEES,
  Mirae and SBI defence ETFs.
- Hanwha Aerospace and Hyundai Rotem: Yahoo shows falls of 58% and 73% from 2026 highs with no split recorded;
  check on KRX before relying on them. Korean shares are not offered for the user's IBKR account (not verified).
- Order-book amounts for ABB India, Siemens, Cummins, BDL (articles not read in full).
- Whether Yahoo EPS for Safran, Airbus and Thales is adjusted or reported (forward P/E uses analysts' adjusted EPS).
