# India market: sources

Written 2026-11-15 by `finance-research`. Market research, not advice; no orders. Proposals are conditional.

## Summary
- Valuation and price data come from niftyindices APIs and factsheets; FX and ETF volume from yfinance; fund costs from Groww.
- News items carry their publisher and date in the line where they are used.

Back to the index: [../opp-india-market.md](../opp-india-market.md).

Every number has a source and date. "not verified" = no source confirmed it. All fetched 2026-11-15.

Source keys:
- [PE] niftyindices P/E-P/B-yield history API `https://www.niftyindices.com/BackPage/getpepbHistoricaldataDBtoString`
  (daily, Nov 2010 to 13-Nov-2026; NSE short names such as `NIFTY SMLCAP 250`, `NIFTY IND DEFENCE`).
  Averages here are MEDIANS: means are skewed by loss years (e.g. Midcap 150 P/E 813 in 2020).
  Trailing P/E, consolidated or standalone basis over time: not verified, so the 10-15 yr numbers are rough.
- [PX] niftyindices price history API `.../BackPage/getHistoricaldatatabletoString` (price index, no dividends), to 13-Nov-2026.
- [FS] niftyindices factsheets `https://www.niftyindices.com/Factsheet/...` dated 2026-10-30 (sector weights, TRI 5y).
- [YF] yfinance `^NSEI`, `INR=X` closes to 13/14-Nov-2026.  [G] Groww fund/ETF page JSON, TER dated 10-13 Nov 2026.
- News found via Google News RSS; publisher and date given in each line.
