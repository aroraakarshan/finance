# Real estate: sources

Part of [Real estate](README.md). Written 2026-11-15 by `finance-research`. "Headline" = only the
news title/summary was read (body blocked or not fetched).

## Summary
- Sources for every [R#] tag in the [India](india.md) and [global and Asia](global-asia.md) parts.
- Primary data: yfinance closes, NSE (niftyindices, bhavcopy), AMFI, company releases, FactSet, Japan MoF.
- News figures are from dated Indian, US and Japanese press; secondary, marked where only a headline was read.

| Tag | Source | Date | What |
|---|---|---|---|
| R1 | Yahoo Finance via yfinance (own calc) | closes to 2026-11-13, pulled 2026-11-15 | Prices, 1/3/5/10y returns (Adj Close = total return; LSE lines and indices price only), trailing yields, 5y monthly correlations, FX (USDINR 94.24, JPYINR 0.5879, SGDINR 73.03), US 10y ^TNX 5.154% |
| R2 | niftyindices.com `getpepbHistoricaldataDBtoString` (NIFTY REALTY, NIFTY 50); constituent file `IndexConstituent/ind_niftyrealtylist.csv` | 2015-11-02 to 2026-11-13; read 2026-11-15 | P/E, P/B, yield history; 10 index members |
| R3 | screener.in consolidated pages, DLF, GODREJPROP, LODHA, PRESTIGE, OBEROIRLTY (5 single reads) | read 2026-11-15 | Market cap, quarterly EPS (Sep 2025-Sep 2026), book value, ROE |
| R4 | Anarock Q3 2026, via ETRealty `realty.economictimes.indiatimes.com/.../134536020` | 2026-09-28 | Top-7 sales, launches, unsold stock, prices |
| R5 | PropEquity Q3 2026, via Hindustan Times / BusinessLine (headline) | 2026-09-25/26 | Top-9 sales -6% |
| R6 | Knight Frank 9M CY26, via Business Standard (headline; body 403) | 2026-10-05 | Top-8 sales flat; launches above sales 16 quarters |
| R7 | Moneycontrol "Festive housing demand faces a test" (14050214); BusinessWorld (headline) | 2026-10-12; 2026-10-25 | Inventory +12%, repo hike; luxury unsold +52% |
| R8 | Economic Times (RBI hikes repo to 5.50%); News18 (CPI 6.09%); SBI Research and ICICI Bank via MSN / Free Press Journal (headlines) | 2026-10-07; 2026-11-13 | RBI rates and inflation |
| R9 | PTI via Financial Express "Top listed real estate firms clock Rs 1.95 lakh crore" | 2026-06-24 | FY26 pre-sales by company |
| R10 | Anarock via Hindustan Times "11 listed developers ... Rs 1.82 lakh crore in FY27" | 2026-08-12 | FY27 pre-sales estimates |
| R11 | Moneycontrol "DLF Q2: Rs 738-crore non-cash gain" (14055366); Livemint (FY27 target, headline) | 2026-10-19; 2026-10-17 | DLF Q2 FY27 |
| R12 | Hindustan Times / Moneycontrol (Godrej Q2, FY27 Rs 41,500 cr); Rediff (H2 launches, headline); ETRealty (profit Rs 145.47 cr vs Rs 154 cr elsewhere: different profit lines) | 2026-10-23 to 2026-11-09 | Godrej Properties |
| R13 | Free Press Journal (Lodha Q2 FY27); Whalesbook (Emkay target, headline) | 2026-10-30; 2026-11-03 | Lodha |
| R14 | ETRealty "Prestige pre-sales rise 20% to Rs 7,225 crore" | 2026-10-13 | Prestige |
| R15 | Business Standard (Nifty Realty +14% in Nov, headline); Zee Business (West Asia cost worries, headline) | 2026-11-12; 2026-09-15 | Sector mood |
| R16 | AMFI NAVAll.txt; NSE bhavcopy 2026-11-13; Groww ETF/fund pages (TER, AUM) | 2026-11-13/15 | Indian fund list, NAV, volume, TER |
| R17 | FactSet Earnings Insight (EarningsInsight_111326.pdf, sector forward P/E chart p.34) | 2026-11-13 | S&P 500 sector forward P/E vs 5y/10y |
| R18 | Equinix Q3 2026 press release, PR Newswire 302922554 | 2026-10-28 | AFFO guidance, bookings |
| R19 | Digital Realty (Seeking Alpha / Crypto Briefing headlines); American Tower (RTTNews 3703537) | 2026-10-27/30 | 2026 FFO/AFFO guidance |
| R20 | stockanalysis.com statistics pages: EQIX, PLD, tyo/8801, hkg/0016 (web_fetch) | 2026-11-15 | Shares, debt, P/B, EPS (second source) |
| R21 | justETF real estate ETF list; profiles IE000G6GSP88 (HPRA), IE00B1FZS244 (IASP) | 2026-11-15 (holdings 2026-09-30) | TER, size, listings, returns, country split |
| R22 | Nareit "Triple D", via [opp-real-assets/reits.md](../../themes/opp-real-assets/reits.md) | 2026-09-03 | Implied cap rates |
| R23 | Mitsui Fudosan H1 FY3/27 results summary, note.com (company release of 2026-11-06 not read directly) | 2026-11-09 | Profit, forecast JPY 285 bn |
| R24 | Miki Shoji Tokyo office survey, via R.E.port on note.com | 2026-11-12 | Vacancy 1.75%, rents |
| R25 | Japan MoF JGB yield CSV (jgbcme.csv) | 2026-11-12 | 10y JGB 2.841% |
| R26 | The Smart Investor via Yahoo Singapore "Singapore REITs are down 8%" | 2026-11-11 | S-REIT yields, leverage |
| R27 | SHKP FY2026 earnings call summary on Yahoo Finance (headline) | 2026-09-09 | Underlying profit HKD 22.9 bn |
| R28 | Bloomberg (headline only); MSN (headline) | 2026-11-10; 2026-08-27 | HK home prices |
| R29 | [india-beyond-mf/government-debt.md](../../themes/india-beyond-mf/government-debt.md) | 2026-11-13 | 10y G-sec 7.32% |

Not used: TradingView (terms); Business Standard and BusinessWorld bodies (403); Reuters, Seeking Alpha bodies.
