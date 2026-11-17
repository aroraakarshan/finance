# Energy: sources, gaps and discrepancies

Written 2026-11-15 by `finance-research`. Back to [README](README.md).

## Summary

- Prices and company numbers: Yahoo (yfinance), checked against screener.in (India) and SEC XBRL (Exxon, Chevron).
- Valuation history: niftyindices (India, 10 years), FactSet (US sector), own calculation (single stocks).
- Forecasts and events: EIA (primary), OGJ, and Indian/global news found through Bing News RSS; many are headlines only.
- Gaps and data errors found are listed below; treat "not verified" numbers as missing.

## Sources (read 2026-11-15)

- [Y] Yahoo Finance via yfinance (project `.venv`): closes to 2026-11-13, adjusted history, quarterly and annual statements, balance sheets, `earnings_estimate`; FX `GBPUSD=X`, `EURUSD=X`, `NOKUSD=X`, `JPYUSD=X`, `INR=X`. Throttled 2-3 s; one 429 on the crumb, data still returned.
- [SC] screener.in consolidated pages (one read each): https://www.screener.in/company/<SYMBOL>/consolidated/ for RELIANCE, ONGC, OIL, BPCL, IOC, HINDPETRO, COALINDIA, GAIL (PETRONET page returned nothing).
- [NI] niftyindices P/E, P/B, yield history API: https://www.niftyindices.com/BackPage/getpepbHistoricaldataDBtoString (Nifty Energy and Nifty 50 Nov 2015-Nov 2026; Nifty Oil and Gas Jan 2020-Nov 2026).
- [FS1] FactSet Earnings Insight 2026-11-13: https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_111326.pdf
- [FS2] FactSet Insight 2026-11-09 (data 2026-11-05): https://insight.factset.com/lowest-forward-12-month-p/e-ratio-for-the-sp-500-in-more-than-3-years
- [ED] SEC EDGAR companyfacts, Exxon CIK 34088 and Chevron CIK 93410: https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
- [EIA] US EIA Short-Term Energy Outlook, released 2026-11-10: https://www.eia.gov/outlooks/steo/
- [OGJ] Oil and Gas Journal, "Morningstar holds 2027 Brent forecast at $71/bbl", 2026-11-12: https://www.ogj.com/general-interest/economics-markets/news/55418528/morningstar-holds-2027-brent-forecast-at-71-bbl-as-persian-gulf-supply-recovers
- [SBI] Moneycontrol (ANI), SBI report on crude, 2026-11-13: https://www.moneycontrol.com/news/business/crude-oil-at-70-a-barrel-in-2027-sbi-sees-relief-as-us-iran-peace-prospects-improve-14079212.html
- [GS] Goldman Sachs forecasts, headlines only: Financial Express 2026-11-01 (https://www.financialexpress.com/market/goldman-sachs-raises-brent-dec-target-to-105-why-27-risk-premium-may-push-oil-to-130-4374991/), MSN 2026-11-01 ($140 risk), Cryptonomist 2026-11-02 (2027 $88).
- [ETE] ET EnergyWorld (PTI), "IOC, BPCL, HPCL clock Rs 30,106 cr Q2 profit", 2026-11-01: https://energy.economictimes.indiatimes.com/news/oil-and-gas/ioc-bpcl-hpcl-clock-30106-cr-q2-profit-nearly-39-of-last-years-annual-earnings/135424037
- [JE] justETF, XDW0 profile (holdings as of 2026-09-29, calendar returns): https://www.justetf.com/en/etf-profile.html?isin=IE00BM67HM91
- [GW] Groww ETF pages (TER, AUM, tracking error, P/E): https://groww.in/etfs/mirae-asset-nifty-energy-etf, /icici-prudential-nifty-oil-gas-etf, /reliance-mutual-fund-cpse-etf
- [NSE] NSE daily price file 2026-11-13: https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20261113_F_0000.csv.zip (ETF symbols, closes, traded value)
- [AMFI] AMFI NAV file 2026-11-13: https://portal.amfiindia.com/spages/NAVAll.txt (fund names, ISINs, NAVs)
- [NEWS] Bing News RSS (https://www.bing.com/news/search?format=rss&q=...), headlines and dates only unless named: News18 2026-04-22 (Hormuz ship seizure); Livemint 2026-07-19 (war timeline, article read); Eastern Herald 2026-09-08 (EIA shut-ins); BusinessLine 2026-10-31 and Moneycontrol 2026-11-01 (OPEC+); MSN/Mint 2026-11-10 ("war effectively over"); MSN 2026-11-12 (tankers hit); Moneycontrol 2026-11-13 (Houthi attacks, Brent above $95); biggo 2026-11-10 (EIA 2027 average $86); Yahoo Finance 2026-11-07 (Exxon +38%, Chevron +39% in 2026); MSN 2026-10-29 (Shell and Total highest profit since 2022); Upstream 2026-11-02 and Xinhua 2026-11-03 (Aramco Q3); ad-hoc-news 2026-10-30 (Shell capex trimmed); ET EnergyWorld 2026-11-01 (Reliance shares); Moneycontrol 2026-10-29/30 (Coal India Q2, broker cuts); BusinessWorld 2026-11-01 (Petronet profit +51%); Business Standard 2026-11-02 (Petronet Qatar cargoes); BusinessLine 2026-11-11 (World Bank Indian coal output); Moneycontrol 2026-11-03 (six days of coal stock); MSN 2026-11-15 (MCL price band due).
- [TAX] [tax/investment-types.md](../../../tax/investment-types.md), [tax/new-investments.md](../../../tax/new-investments.md); withholding rates from research/global country notes (UK, eurozone, Japan, Middle East).
- Linked notes: [TTE.md](../../stocks/TTE.md), [APA.md](../../stocks/APA.md), [CHENNPETRO.md](../../stocks/CHENNPETRO.md), [MCL.md](../../ipo/MCL.md), [opp-sectors-themes](../../themes/opp-sectors-themes.md).

## Gaps (not verified)

- Exact start date of the 2026 Iran war; EIA's annual 2027 Brent average (only the Q4 2027 $77 was read).
- 10-year average forward P/E for S&P 500 energy (FactSet gives it in a chart only); 10-year EV/EBITDA averages for European, Japanese and Gulf majors (only 4 year-ends from Yahoo).
- MSCI World Energy index P/E; Nifty Energy constituent weights; CPSE ETF weights.
- TER of the Axis Nifty Energy Index Fund and the active energy funds; Petronet dividend yield.
- Whether Indian consensus EPS on Yahoo is consolidated or standalone.

## Discrepancies found

- Yahoo quarterly EBITDA for Indian companies is far below screener's operating profit + other income (ONGC LTM Rs 81,466 Cr vs Rs 1,21,406 Cr; Reliance Rs 1,56,151 Cr vs Rs 2,15,996 Cr). Used screener for Indian LTM EBITDA.
- Yahoo `dividendYield` for Indian stocks disagrees with screener (Coal India 10.16% vs 6.57%; ONGC 9.44% vs 5.89%). Used screener.
- Yahoo `forwardEps` is off for Shell (4.48 vs +1y estimate 6.00) and Inpex (268 vs 436). Used `earnings_estimate`.
- Groww shows OILIETF P/E 11.3; niftyindices shows Nifty Oil and Gas P/E 9.89 on 2026-11-13.
- BPCL P/E: screener 9.33, Yahoo 8.3 (different profit line).
- TotalEnergies: this note P/E 8.9, EV/EBITDA 4.2 (Yahoo) vs [TTE.md](../../stocks/TTE.md) 9.2 / 4.5 (stockanalysis).
