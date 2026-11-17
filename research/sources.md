# Research sources

Scored list of sources. Start each task here and use the highest score for the need.
After each task: add new sources, raise or lower scores, note failures. One line each.
Score: 5 best, 1 do not use (for direct fetch by script/agent, no browser).

## Summary
- Scored list (1-5) of every data source the research team has tried; start each task here and use the highest score for the need.
- Best by area: AMFI and mfapi (India MFs); niftyindices, NSE daily price file and announcement RSS (India markets); SEC EDGAR and company IR (fundamentals); central bank APIs (rates); Google and Bing News RSS (news).
- Do not use: TradingView pages (terms), Yahoo `info` EPS for non-US stocks, web search engines.

| Source | Access | Good for | Market | Cost | Reliability / notes | Score | Last used |
|---|---|---|---|---|---|---|---|
| AMFI NAV file | `https://portal.amfiindia.com/spages/NAVAll.txt` (old amfiindia.com URL only redirects) | All scheme NAVs, ISIN, Direct/Regular plan check | India | free | Official, daily, easy to parse | 5 | 2026-11-15 |
| mfapi.in | `https://api.mfapi.in/mf/search?q=`, `/mf/<scheme code>` | MF scheme codes, full NAV history (returns, drawdowns, buy-window from avg cost) | India | free | Unofficial AMFI mirror; clean JSON, fast | 5 | 2026-11-15 |
| Groww fund/ETF pages | `groww.in/mutual-funds/<slug>`, `groww.in/etfs/<slug>`; embedded page JSON via curl | Expense ratio (total and base), AUM, benchmark, exit load history, full portfolio | India | free | Current (TER dated within days); secondary source; one regular-plan link was wrong. Blog/tax pages useless | 4 | 2026-11-15 |
| Groww search API | `groww.in/v1/api/search/v3/query/global/st_query?query=` | Find Groww slug for a fund | India | free | Undocumented, may change | 4 | 2026-11-15 |
| Kuvera via captnemo mirror | `https://mf.captnemo.in/kuvera/<ISIN>` | Cross-check TER, AUM | India | free | Unofficial; exit load empty, AUM units unclear. Direct `api.kuvera.in` by ISIN returns `[]` | 4 | 2026-11-15 |
| Yahoo Finance (yfinance) | Python `yfinance`; e.g. `SI=F`, `GC=F`, `^NSEI`, `INR=X`, `GOLDBEES.NS`, `SILVERBEES.NS` | Price history, volatility, drawdown, FX | both | free | Closes only; futures rolls not adjusted; ^NSEI is price index (no dividends). `SILVER1.NS` is NOT ABSL Silver ETF (use `SILVER.NS`). Cache and throttle (429). Dates: `Ticker.calendar` converts timestamps to the machine's local timezone (after-close US earnings show a day late in IST; ex-dividend dates are midnight UTC, a day early in New York time). Run date lookups with TZ=UTC, use `get_earnings_dates()` for earnings, or company IR | 4 | 2026-11-15 |
| SEBI circulars and studies | sebi.gov.in PDFs (find via search, guessed URLs 404) | Fund category rules, F&O and intraday loss studies | India | free | Primary | 5 | 2026-11-15 |
| RBI (rbi.org.in) | LRS FAQ, Master Directions, Overseas Investment Directions 2022 | LRS limits, no derivatives/margin abroad | India | free | Primary. `rbidocs.rbi.org.in` hits CAPTCHA | 5 | 2026-11-15 |
| indiabudget.gov.in | Finance Bill / memorandum / speech PDFs | Capital gains rates, Sec 50AA, TCS, new Income-tax Act 2025 | India | free | Primary but Bill text, not enacted Act | 4 | 2026-11-15 |
| incometax.gov.in | e-filing help pages | Sec 112A limit, ITR rules | India | free | Official but partial; many pages 404 | 3 | 2026-11-15 |
| incometaxindia.gov.in | CBDT pages, tutorial PDFs | Tax rules | India | free | 403 to scripts | 1 | 2026-11-15 |
| AMC sites: PPFAS, Motilal Oswal | `amc.ppfas.com`, `motilaloswalmf.com` (scheme pages, SID PDFs) | Exit load, TER, fund-of-funds asset split, offer document | India | free | Primary; Motilal URLs fragile (`...-fund-of-funds`) | 4 | 2026-11-15 |
| AMC sites: ICICI Pru, ABSL; AMFI web pages | icicipruamc.com, mutualfund.adityabirlacapital.com, amfiindia.com pages | TER, tracking difference | India | free | Need JavaScript; no data by fetch | 1 | 2026-11-15 |
| Value Research | valueresearchonline.com | Fund data, overlap | India | free/login | Blocked or JavaScript-only for scripts | 1 | 2026-11-15 |
| Moneycontrol | moneycontrol.com | Fund pages (blocked); news articles (work) | India | free | Fund pages near-empty; news fine, secondary for tax | 2 | 2026-11-15 |
| ClearTax | cleartax.in/s/... | Tax explainers | India | free | 410/blocked | 1 | 2026-11-15 |
| Indian news: Livemint, Economic Times, Business Standard, NDTV Profit, New Indian Express | article pages | Events (ETF premiums, FoF subscription pauses, price moves) | India | free/some paywall | Fine for dated events; secondary for rules | 3 | 2026-11-15 |
| World Gold Council | gold.org/goldhub | Gold allocation research | global | free | Industry body (biased toward gold) | 4 | 2026-11-15 |
| Broker docs: Alpaca, IBKR | docs.alpaca.markets, interactivebrokers.com | Order types (stop, bracket, OCO) | US | free | Fine, undated | 4 | 2026-11-15 |
| Broker docs: INDmoney, AngelOne | indmoney.com/us-stocks, github.com/angel-one SmartAPI | Order types, GTT, TCS | both | free | INDmoney fine; AngelOne knowledge centre 404/JavaScript | 3 | 2026-11-15 |
| eCFR / SEC / Investor.gov | ecfr.gov, sec.gov, investor.gov | US rules (penny stock definition), microcap risks | US | free | Primary; SEC microcap guide old (2013) | 5 | 2026-11-15 |
| FINRA | finra.org | Penny stock spreads | US | free | Pages 404 | 1 | 2026-11-15 |
| Academic papers | faculty.haas.berkeley.edu (Barber/Odean PDFs), ideas.repec.org, api.semanticscholar.org | Retail trading evidence | global | free | Authors' PDFs fine; SSRN blocked by Cloudflare (use RePEc/Semantic Scholar for abstracts) | 4 | 2026-11-15 |
| Bing search | `bing.com/search?q=` | Finding pages | global | free | Poor or no results (use Bing News RSS instead) | 1 | 2026-11-15 |
| DuckDuckGo / Google search | html.duckduckgo.com, google.com | Finding pages | global | free | Captcha / JavaScript; blocked | 1 | 2026-11-15 |
| r.jina.ai proxy | `r.jina.ai/<url>` | Read JavaScript pages as text | global | free | Works for some sites (Appreciate, Schwab); not for data-heavy apps (Research Affiliates, DBS) | 3 | 2026-11-15 |
| Own exports (Google Drive Finance/) | `scripts.brokers.*`, `scripts.pnl` | Holdings, trades, P&L | both | own | Accurate; no purchase dates (MF) or bid/ask; US exports have cost only | 4 | 2026-11-15 |
| Cornell LII US Code | `law.cornell.edu/uscode/text/26/<section>` | US tax law text (estate tax 2101-2106, 871) | US | free | Primary, current | 5 | 2026-11-15 |
| IRS pages and treaty PDFs | irs.gov (nonresident estate tax, 706-NA instructions, treaty list, Pub 515, `irs.gov/pub/irs-trty/<country>.pdf` with pypdf) | Estate tax, withholding, treaties | US | free | Primary; some form pages 404 (Form 5173), estate FAQ URL moves | 5 | 2026-11-15 |
| TreasuryDirect | treasurydirect.gov | T-bill rules | US | free | Primary | 5 | 2026-11-15 |
| IBKR pricing and product pages | interactivebrokers.com/en/pricing/..., /en/accounts/fees/pricing-interest-rates.php, /en/trading/... | Commissions, interest, SYEP, bonds, crypto | global | free | Primary, current. FAQ (ibkr.com/faq) and ibkrguides KB need JavaScript/404; deceased-account pages not found | 5 | 2026-11-15 |
| IBKR India | interactivebrokers.co.in | IB India entity scope | India | free | Works | 4 | 2026-11-15 |
| iShares UK / justETF | ishares.com/uk/individual/en/products/<id>/ (short URLs 403), justetf.com | UCITS ETF TER, domicile, distribution | global | free | iShares primary; justETF secondary | 5 | 2026-11-15 |
| GOV.UK | gov.uk | UK stamp duty on shares | UK | free | Primary | 5 | 2026-11-15 |
| Google News RSS | `news.google.com/rss/search?q=<query>`; article links decoded through Google's batchexecute endpoint | Finding dated news when search engines block | both | free | Best working search route; decoding can hit 429 when many agents run | 5 | 2026-11-15 |
| RBI press release archive | rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx (monthly archive by form post) | FRSB rates, T-bill auctions, SGB | India | free | Primary. curl gets empty shell; web_fetch works | 5 | 2026-11-15 |
| RBI Retail Direct | rbiretaildirect.org.in | G-sec retail access | India | free | Needs JavaScript | 1 | 2026-11-15 |
| National Savings Institute | nsiindia.gov.in | PPF and small-savings rates | India | free | Primary | 4 | 2026-11-15 |
| DICGC | dicgc.org.in | Deposit insurance | India | free | Needs JavaScript | 1 | 2026-11-15 |
| NSE API / Yahoo for SGB symbols | nseindia.com/api, query1.finance.yahoo.com | SGB prices | India | free | Blocked / no data | 1 | 2026-11-15 |
| More Indian news: Times of India, The Hindu/BusinessLine, Business Today | article pages | Dated events, rates | India | free | Fine | 4 | 2026-11-15 |
| Secondary India sites: Upstox news, Fortune India, Outlook Money, ICICI Direct research, NiftyTrader | article pages | IPO stats, events | India | free | Fine, secondary | 3 | 2026-11-15 |
| Low-value India sites: Multibagg AI, DSIJ | article pages | IPO data | India | free | Secondary, unclear method | 2 | 2026-11-15 |
| Moneylife, KPMG reports | moneylife.in, kpmg.com | Analysis | India | free | Cloudflare / text not extractable | 1 | 2026-11-15 |
| Crossref API | `api.crossref.org/works?query=` | Paper metadata and abstracts | global | free | Works; 429 if rushed | 4 | 2026-11-15 |
| J.P. Morgan "Agony and Ecstasy" PDF | chase.com privatebanking eotm PDF | Single-stock risk | US | free | Primary | 5 | 2026-11-15 |
| everycrsreport.com | CRS reports | Enron/401k history | US | free | Primary copies | 5 | 2026-11-15 |
| Personal-finance sites: Schwab, Kiplinger, Fidelity, Morningstar | various | Rules of thumb | US | free | 403/404 to scripts | 1 | 2026-11-15 |
| Vanguard research PDFs | corporate.vanguard.com | Plan data | US | free | Downloads, text did not extract | 2 | 2026-11-15 |
| SEC EDGAR full-text search | efts.sec.gov | Filing search | US | free | 403 (submissions API still works, see EDGAR row in skill) | 1 | 2026-11-15 |
| Policybazaar | policybazaar.com | Term insurance prices | India | free | Secondary, undated | 3 | 2026-11-15 |
| Income-tax Act 2025 text (via finance-tax) | GitHub abaasairam-ai/income-tax-rag docs-text | New Act and Rules 2026 section text | India | free | Unofficial copy; used by finance-tax | 3 | 2026-11-15 |
| SEC EDGAR submissions API + filings | data.sec.gov/submissions/CIK##########.json, sec.gov/Archives (User-Agent header) | 8-K events, 10-Q dates, deregistration | US | free | Primary | 5 | 2026-11-15 |
| Company newsrooms / investor relations (e.g. NVIDIA, Constellation) | company press-release and IR pages | Earnings dates (the source for dates), results, guidance, management changes | US | free | Primary | 5 | 2026-11-15 |
| US market news: Yahoo Finance articles, Opening Bell Daily (TradingView removed: terms forbid automated access) | article pages | Daily moves, events | US | free | Fine; TradingView one stale page | 3 | 2026-11-15 |
| Low-value US sites: TradingKey, Simply Wall St, 24/7 Wall St | article pages | Event colour | US | free | Secondary | 2 | 2026-11-15 |
| Reuters, Seeking Alpha, FinancialContent | article pages | News | US | free/paywall | Body blocked (headline only) | 1 | 2026-11-15 |
| Vanguard VCMM return forecasts | corporate.vanguard.com/.../vemo-return-forecasts.html | 10-yr expected returns by asset and region | global | free | Primary, current (Oct 2026) | 5 | 2026-11-15 |
| GMO 7-year asset class forecast | gmo.com/globalassets/articles/gmo-7-year-asset-class-forecast/<yyyy>/...pdf | Real return forecasts (value, small, regions) | global | free | Primary; some numbers only in chart images (Advisor Perspectives copies the chart) | 5 | 2026-11-15 |
| AQR capital market assumptions PDF | aqr.com/-/media/... (table A1) | Expected returns by region/asset | global | free | Primary; annual (Dec/Jan data) | 5 | 2026-11-15 |
| BlackRock CMA spreadsheet | blackrock.com/blk-inst-c-assets/...xlsx | Expected returns by region | global | free | Primary, downloadable | 5 | 2026-11-15 |
| Research Affiliates Excel download | download.researchaffiliates.com/asset-allocation/excel?... | 10-yr expected returns and CAPE by country | global | free | Primary; the interactive site needs JavaScript but the Excel works | 5 | 2026-11-15 |
| J.P. Morgan LTCMA | am.jpmorgan.com/.../ltcma/ page; press release on prnewswire.com | Long-term return assumptions | global | free/login | Summary and press release fine; full PDF and matrices need login (country figures not public) | 3 | 2026-11-15 |
| J.P. Morgan Guide to the Markets PDFs | am.jpmorgan.com / cdn.jpmorganfunds.com | Forward P/E vs history by region | global | free | Primary; Asia guide works, some regional guides blocked | 4 | 2026-11-15 |
| multpl | multpl.com/shiller-pe | US CAPE history | US | free | Reliable | 4 | 2026-11-15 |
| Siblis Research | siblisresearch.com/data/cape-ratios-by-country/, emerging-markets-valuations | CAPE and P/E by country | global | free/partly paid | Mostly works; some pages paywalled | 4 | 2026-11-15 |
| worldperatio.com | worldperatio.com/area/<country>/ | P/E vs averages by country | global | free | Secondary, no Gulf data | 3 | 2026-11-15 |
| MSCI index factsheets | msci.com/documents/10199/<uuid> | Index P/E, yield, sector weights | global | free | Works when the UUID is known; no search, index pages empty shells | 3 | 2026-11-15 |
| FactSet Earnings Insight | insight.factset.com, advantage.factset.com PDFs | S&P 500 and sector forward P/E vs averages | US | free | Primary; guessed PDF URLs 404 | 5 | 2026-11-15 |
| Ken French data library | mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Factor returns (value, size, momentum, quality) | global | free | Primary | 5 | 2026-11-15 |
| Star Capital, Yardeni archive | starcapital.de, archive.yardeni.com | CAPE, MSCI P/E | global | free | Star Capital gone (redirects); Yardeni archive stale (2023) | 1 | 2026-11-15 |
| niftyindices APIs | niftyindices.com/BackPage/getpepbHistoricaldataDBtoString, getHistoricaldatatabletoString (NSE short index names, 1-year range per request; reply is now a plain list, not {"d": ...}, Nov 2026); factsheet PDFs | Nifty index P/E, P/B, yield and price history | India | free | Primary; factsheet file names vary | 5 | 2026-11-15 |
| CCIL tenor-wise yields | ccilindia.com/web/ccil/tenorwise-indicative-yields | G-sec, T-bill, SDL yields | India | free | Primary, daily | 5 | 2026-11-15 |
| US Treasury yield CSV | home.treasury.gov resource-center interest-rates | Nominal and real Treasury curves | US | free | Primary, daily | 5 | 2026-11-15 |
| FRED CSV | fred.stlouisfed.org/graph/fredgraph.csv?id=<series> | Yields, TIPS, credit spreads | US | free | web_fetch works, curl stalls; several ids return a zip; ICE spread series only ~3 yrs now | 4 | 2026-11-15 |
| Central bank data APIs | Bank of England IADB, Bundesbank API, Japan MoF JGB CSV, Bank of Canada Valet, Banco Central do Brasil SGS | Government bond yields, policy rates | global | free | Primary; RBA CSV blocked to curl (web_fetch works) | 5 | 2026-11-15 |
| PwC tax summaries | taxsummaries.pwc.com/<country>/corporate/withholding-taxes | Dividend withholding and treaty rates by country | global | free | Reliable secondary | 5 | 2026-11-15 |
| IBKR exchange list JSON | interactivebrokers.com/webrest/exchanges/ (behind products-exchanges.php); regional commission pages | Which exchanges IBKR offers | global | free | Primary; the exchange search page itself needs JavaScript; per-entity eligibility not shown | 5 | 2026-11-15 |
| ETF issuer holdings files | ssga.com holdings xlsx; ftportfolios.com EtfHoldings.aspx | Full ETF holdings (overlap checks) | US | free | Primary; iShares holdings CSV returns HTML | 5 | 2026-11-15 |
| World Gold Council | gold.org (Gold Demand Trends) | Central bank buying, ETF flows | global | free | Primary data; industry body (pro-gold views) | 5 | 2026-11-15 |
| Commodity/REIT data: Kitco, Nareit, NBER papers | kitco.com, reit.com, nber.org | Gold prices, REIT valuation, commodity research | global | free | Fine | 4 | 2026-11-15 |
| Cafemutual | cafemutual.com | Indian MF/AIF industry news | India | free | Fine | 4 | 2026-11-15 |
| Broker charges pages | angelone.in/exchange-transaction-charges, zerodha.com/charges | Indian trading costs | India | free | AngelOne fine; Zerodha lacks ETF STT detail | 4 | 2026-11-15 |
| AQR Century of Trend Following | aqr.com research page and PDF | Trend-following evidence | global | free | Primary | 5 | 2026-11-15 |
| Crypto news: CoinDesk, MediaNama | coindesk.com, medianama.com | Crypto policy and platform changes | both | free | Fine | 4 | 2026-11-15 |
| Global platform pages: Vested pricing, Appreciate (via r.jina.ai), Schwab International, Wise help | vestedfinance.com/in/pricing/, appreciatewealth.com, international.schwab.com/pricing, wise.com/help | LRS platform costs and limits | both | free | Fine; guessed /pricing URLs 404 | 4 | 2026-11-15 |
| NSE IX Global Access, Saxo India, eToro/moomoo help, IEA | nseixga.com, home.saxo/en-in, iea.org | Platform/energy data | global | free | JavaScript-only / Not Found / Cloudflare | 1 | 2026-11-15 |
| Regional news: Business Times SG, Nation Thailand, Viet Nam News, Korea Herald, Taipei Times, KEIA, nippon.com, swissinfo, CNBC, The Guardian | article pages | Country events | global | free | Fine | 4 | 2026-11-15 |
| More blocked news: NDTV Profit, ANI, Investing.com, Jakarta Post, SCMP, Bloomberg, WSJ | article pages | News | global | free/paywall | 403 or headline only | 1 | 2026-11-15 |
| screener.in | `screener.in/company/<NSE symbol>/consolidated/` (curl) | India consolidated P/E, ROE, ROCE, 10-yr financials | India | free | Works (via finance-scout); ROE is last full year; terms allow viewing only: keep reads light, one stock at a time, no bulk scraping | 4 | 2026-11-15 |
| stockanalysis.com statistics | `stockanalysis.com/stocks/<t>/statistics/`, `/quote/<exchange: lon, epa, bme, tyo, hkg>/<code>/statistics/` | P/E, EV/EBITDA, ROE, margins, D/E as text; second source for Yahoo | global | free | Works with web_fetch (plain curl returns an empty page); some HK pages 404 (2359: use the A-share page /quote/sha/603259); 8309 quarterly rows duplicated (Nov 2026); terms allow AI agents that follow robots.txt (web_fetch) but ban scripts: no curl/bulk scraping | 4 | 2026-11-15 |
| Index member lists | `indexes.nikkei.co.jp/en/nkave/index/component?idx=nk225` (read_html); Wikipedia index pages; `archives.nseindia.com/content/indices/ind_nifty500list.csv` | Screen universes | global | free | Nikkei and NSE files primary (5); Wikipedia may lag (3); Nasdaq-100 page has no table | 4 | 2026-11-15 |
| SEBI circulars list, RBI drafts page | `sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=1&ssid=7&smid=0`; `rbi.org.in/Scripts/DraftNotificationsGuildelines.aspx` | New rules and drafts | India | free | Works (finance-scout); titles and dates | 5 | 2026-11-15 |
| Company investor-relations sites (results, presentations, annual reports) | e.g. astellas.com/en/investors, smtg.jp/en/investors, konami.com/ir/en, bbva.com, ckah.com/financial-reports, greatship.com upload PDFs | Stock deep dives: segment data, guidance, true EPS | global | free | Primary; best source for EPS when Yahoo is wrong. Some block scripts (TotalEnergies 403 -> r.jina.ai; Computacenter IR 403 -> RNS via LSE or PR wire (not TradingView: terms)) | 5 | 2026-11-15 |
| screener.in APIs | screener.in/api/... (peers, P/E and P/B history, shareholding) | India peer tables, valuation history | India | free | Works; terms allow viewing only: keep reads light, one stock at a time, no bulk scraping | 5 | 2026-11-15 |
| TradingView news (RNS, PR Newswire copies) | tradingview.com/news | UK RNS statements, company press releases | global | free | DO NOT USE: TradingView terms forbid any automated access (tradingview.com/policies, checked 2026-11-15). For UK RNS use company IR or the LSE RNS page; for press releases use PR Newswire/Business Wire directly | 1 | 2026-11-15 |
| HKEX securities list | HKEX ListOfSecurities.xlsx | HK board lots, ISINs | HK | free | Primary | 5 | 2026-11-15 |
| Yahoo `info` fundamentals | yfinance `Ticker.info` (trailingEps, forwardEps, P/E, enterpriseValue) | Screens | global | free | Unreliable for non-US: wrong EPS for 8309 and 9766 (Nov 2026), wrong forward EPS for Japan, P/E mixing currencies (2359, TTE); `enterpriseValue` can be plainly wrong, `Operating Income` is adjusted (see market-data skill). Always recompute from company figures | 2 | 2026-11-15 |
| Bing News RSS | `bing.com/news/search?format=rss&q=<query>` | Dated news with direct article links (no decoding) | global | free | Works when Google News link decoding hits 429; Bing web search itself is useless | 5 | 2026-11-15 |
| Global Property Guide | globalpropertyguide.com (web_fetch or r.jina.ai; curl 403) | Property prices, rental yields, buying costs by country | global | free/partly paid | First city free; per-sq-m pages JavaScript or paid; some date typos (Cyprus "Q3 2027") | 4 | 2026-11-15 |
| Numbeo property pages | numbeo.com/property-investment/in/<City> | Crowd-sourced price/rent per city | global | free | Secondary; US yields unrealistic; gaps for small cities | 3 | 2026-11-15 |
| Government property and foreign-buyer pages | IRAS (iras.gov.sg), foreigninvestment.gov.au, LINZ, Revenue NSW/Victoria SRO, revenue.ie, GOV.UK API, budget.canada.ca, EDB Mauritius residency.mu, Florida/Texas statutes | Foreign buyer rules, stamp duties | global | free | Primary; firb.gov.au, ATO, canada.ca CMHC, dubailand.gov.ae, u.ae, citizensinformation.ie blocked or 404 | 5 | 2026-11-15 |
| PwC tax summaries, individual pages | taxsummaries.pwc.com/<country>/individual | Non-resident rental and capital gains tax | global | free | Reliable secondary; no pages for some small countries | 5 | 2026-11-15 |
| Gulf property press: Gulf News, Saudi Gazette, EnterpriseAM, Argaam, IMI Daily, Gulf Times, Savills/JLL PDFs | article pages and PDFs | Gulf prices, rules | Gulf | free | Fine; Arabian Business, AGBI, Muscat Daily, DarGlobal blocked | 4 | 2026-11-15 |
| OI Rules 2022 web text | rbi.org.in/scripts/bs_viewcontent.aspx?Id=5087 | Overseas investment rules (r.21 property) | India | free | Primary; no CAPTCHA (rbidocs PDF has one) | 5 | 2026-11-15 |
| RBI FEMA notifications, property FAQ | rbi.org.in/Scripts/NotificationUser.aspx?Id=..., FAQView.aspx?Id=117 | FEMA 7(R), 9(R), 3(R); property abroad FAQ | India | free | Primary | 5 | 2026-11-15 |
| NSE daily price file (bhavcopy) | nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_<yyyymmdd>_F_0000.csv.zip | Closing prices for SGBs, ETFs, all NSE lines | India | free | Primary; works where the NSE API is blocked | 5 | 2026-11-15 |
| IBJA rates | ibjarates.com | Daily gold/silver benchmark (999) | India | free | Primary for SGB premium checks | 5 | 2026-11-15 |
| NPS Trust | npstrust.org.in (scheme returns file `all-scheme-return-download?todatereturn=DD-MM-YYYY`, NAV excel) | NPS returns by fund manager, NAVs, charges | India | free | Primary; monthly PDFs lag | 5 | 2026-11-15 |
| PFRDA | pfrda.org.in | NPS rules, circulars, corporate model | India | free | Primary | 5 | 2026-11-15 |
| Insurer annuity pages | licindia.in brochures, hdfclife.com | Annuity rates | India | free | LIC brochure works (some URLs 503); HDFC page undated; SBI Life 404 | 4 | 2026-11-15 |
| India alternatives press: Capitalmind, Finshots, Cafemutual, Upstox, ICICI Direct | article pages | P2P, OBPP, unlisted shares, AIF news | India | free | Fine | 4 | 2026-11-15 |
| Platform sites (Grip, Wint, GoldenPi, Jiraaf, KredX, TradeCred, hBits, Precize, LetsVenture, Royalty Exchange, SongVest) | company sites | Product terms, stated yields | both | free | Marketing; stated not realised returns; PropShare, LenDenClub, Altifi, JKBX blocked | 3 | 2026-11-15 |
| NSE announcement RSS | nsearchives.nseindia.com/content/RSS/*.xml | Live NSE corporate announcements and filings | India | free | Primary, no key; holds only about the last day, so poll daily (or use NSE filing pages for a week). Insider-trading RSS stops at 2 May 2026 (use XBRL api/corporates-pit-gg); results RSS sparse (finance-scout test 2026-11-15). BSE notices RSS also works; BSE announcements API 403 | 5 | 2026-11-15 |
| GitHub API and PyPI JSON | api.github.com/repos/<owner>/<repo>; pypi.org/pypi/<pkg>/json | Vetting tools: stars, issues, last release, licence, Python support | global | free | Works; GitHub unauthenticated limit 60/hour shared by all agents | 5 | 2026-11-15 |
| IBKR API docs | interactivebrokers.com/docs/... (.md pages: Flex Web Service, TWS settings, Web API) | Read-only Flex statements, TWS Read-Only API | global | free | Primary; campus Flex URL 404 | 5 | 2026-11-15 |
| India broker API docs | kite.trade, mcp.kite.trade, upstox.com/developer, smartapi.angelone.in (via r.jina.ai), docs.dhanhq.co | Broker APIs and MCPs, read-only options | India | free | Primary; AngelOne SmartAPI docs need JavaScript | 4 | 2026-11-15 |
| Data vendor pricing pages | twelvedata.com/pricing (+ api.twelvedata.com exchanges), eodhd.com, massive.com, financialdatasets.ai, alphavantage.co (via r.jina.ai), FMP (via r.jina.ai; direct 403), tiingo.com | API cost and coverage | global | free | Primary; check India coverage by testing a free key | 4 | 2026-11-15 |
| MCP registry | registry.modelcontextprotocol.io | Finding official MCP servers | global | free | Works | 4 | 2026-11-15 |
| Site terms of use | tradingview.com/policies, screener.in terms, stockanalysis.com terms, trendlyne.com terms | Whether agents may fetch a site | global | free | Primary; check before adding a new web source | 5 | 2026-11-15 |
| GDELT DOC 2.0 API | api.gdeltproject.org | Global news search | global | free | Rate-limited every query (1 req/5 s) | 2 | 2026-11-15 |
| EIA Short-Term Energy Outlook | eia.gov/outlooks/steo/ | Oil price forecasts | global | free | Primary, monthly | 5 | 2026-11-15 |
| JPX PER/PBR by industry | jpx.co.jp/english/markets/statistics-equities/misc/04.html | Japan sector valuations | Japan | free | Primary; trailing only; older files store values as formulas | 5 | 2026-11-15 |
| Hang Seng factsheets | hsi.com.hk/static/uploads/contents/en/dl_centre/factsheets/hsciE.pdf | HK/China sector P/E and yields | HK/China | free | Primary; data API 404 | 5 | 2026-11-15 |
| J.P. Morgan Guide to the Markets regional PDFs | cdn.jpmorganfunds.com/.../guide-to-the-markets-asia.pdf, -uk.pdf | Regional sector valuations (read from charts) | global | free | Works on cdn.jpmorganfunds.com; am.jpmorgan.com paths 404 | 5 | 2026-11-15 |
| iShares STOXX Europe 600 sector ETFs (Xetra) | yfinance EXV1-EXV9, EXH1-EXH9, EXI5 (.DE) | Europe sector returns | Europe | free | Works; Yahoo ETF P/E not checked against iShares | 4 | 2026-11-15 |
| NEXT FUNDS TOPIX-17 ETFs | yfinance 1617.T-1633.T | Japan sector returns | Japan | free | Works; thin trading; a near-zero print on 31 Mar 2026 | 4 | 2026-11-15 |
| Yahoo for Indian fundamentals | yfinance Ticker.info, quarterly statements (.NS) | Indian EBITDA, dividend yield | India | free | Wrong for Indian companies (EBITDA far too low, yields wrong, e.g. ONGC, Coal India, Nov 2026): use screener.in | 1 | 2026-11-15 |

## Gaps (no working source yet)
- Official SEBI meaning of "base" vs "total" expense ratio (Groww shows both).
- ICICI/ABSL ETF tracking difference from the AMC itself.
- MF purchase dates: need CAMS/KFintech consolidated statement (login, user download).
- Enacted 2026-27 capital gains rates under the new Income-tax Act (only Bill text and news so far).
