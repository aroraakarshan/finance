# Stock screens 2026-11-15: method and data problems

## Summary
- How the 2026-11-15 screens were built: index lists, Yahoo data, the four screens, filters and
  selection.
- Data problems found: wrong Yahoo EPS for some Japan and HK lines, P/E currency mismatches, one-off
  growth; check a ratio here before trusting it in the picks table.

## Method
- Weights: `journal/signals.md` exists but has no closed trades or scores yet, so the four
  screens are weighted equally.
- Universe (lists read 2026-11-15): India Nifty 500 (`archives.nseindia.com/content/indices/ind_nifty500list.csv`,
  501 rows incl. one placeholder `DUMMYHEG`); US S&P 500 (Wikipedia list, 503); Europe Euro Stoxx 50 +
  FTSE 100 + SMI (Wikipedia lists, 170 unique; Roche is `ROP.SW` on Yahoo, not `ROG.SW`); Japan Nikkei 225
  (`indexes.nikkei.co.jp` component page, 225); other Asia Hang Seng (85) + STI (30) + ASX 50 (49)
  (Wikipedia lists, 164). Nasdaq-100 skipped (its Wikipedia page gave no constituent table; nearly all
  members are in the S&P 500 anyway).
- Skipped: Korea and Taiwan. `research/themes/ibkr-global.md` s3.1 covers LSE, Euronext, Xetra, SIX,
  HKEX, TSE, ASX and SGX only. `STATUS.md` (Needed from user, 2026-11-15): IB India clients cannot
  trade Korea; the account's IBKR entity (IB LLC or IB India) is still unknown, so Korea access is
  open. Taiwan access not verified.
- Data: Yahoo Finance via yfinance 1.8.0. Prices: daily closes to Fri 2026-11-13 (last trading day),
  2 years. Fundamentals: Yahoo `info` pulled 2026-11-15 02:55-03:21 IST (cached, throttled; no 429s).
  FX: yfinance `<CUR>USD=X` closes of 2026-11-13.
- Screens (ranks are percentiles inside each market; combined score = mean of the four, 0-1):
  - Growth: revenue growth and EPS growth y/y (Yahoo `revenueGrowth`, `earningsGrowth`: latest quarter
    vs the same quarter a year earlier). Pass: both > 10%.
  - Momentum: 6- and 12-month return minus the local index (India ^CRSLDX Nifty 500, US ^GSPC, UK ^FTSE,
    Switzerland ^SSMI, other Europe ^STOXX50E, Japan ^N225, HK ^HSI, SG ^STI, AU ^AXJO), and close vs
    200-day average. Pass: close above 50- and 200-day averages and both relative returns > 0.
  - Value: P/E and EV/EBITDA ranked inside the same sector in the same market (whole market if the
    sector has under 4 names; banks/insurers on P/E only). Pass: P/E below the sector median.
    Own 5-year P/E history: NOT done (no free history source in this run).
  - Quality: ROE, operating margin, debt/equity (D/E not used for financials). Pass: ROE > 15%,
    operating margin > 15%, D/E < 100%.
- Ratios in one currency (skill `market-data`, Yahoo bullet, commit 027ae1f): Yahoo P/E divides the price by
  EPS with no FX conversion. For European/UK lines of USD reporters (SHEL, RIO, TTE) Yahoo EPS is in USD, so
  this run converts the price to USD first (verified by skill-session against filings, 2026-11-15; an
  interim scout note that undid this was wrong and is withdrawn). HKEX/ASX/SGX lines: EPS in the quote
  currency for USD reporters (HSBC, AIA, NEM.AX), but in CNY for HK-listed mainland companies (2359), which
  this run missed. London quotes in pence are divided by 100. EV/EBITDA = (price x shares + debt - cash) /
  EBITDA in the reporting currency; dropped for HK/AU/SG lines that report in another currency.
- Filters: holdings excluded (10 US tickers found in the S&P 500: GOOGL, GOOG, AVGO, CEG, CRWD, IBKR,
  MSFT, NVDA, QCOM, VRT; Time Technoplast is not in Nifty 500). Price under Rs 50 (India) or under
  USD 5 equivalent (elsewhere) excluded (`AGENTS.md`): India 10, Europe 13, Japan 8, other Asia 60
  (HK 46, SG 18, AU 6). Only listed cash equities (LRS allowed, `research/themes/ibkr-global.md` s3.1).
- Selection: top combined score per market, at least 2 of 4 screens passed, at most one name per
  sector per market; 3 per market, then two dropped for data problems (below): 14 names.
- Scored / eligible: India 406 / 396, US 431 / 423, Europe 142 / 129, Japan 189 / 180, other Asia
  137 / 77. Names without all four inputs were not scored (mostly banks without EBITDA or growth).
- Second source (read 2026-11-15): India: screener.in consolidated page (P/E, ROE); others:
  stockanalysis.com statistics page (P/E, EV/EBITDA, ROE, operating margin, D/E).
- Code and cache: work folder `~/.local/share/superpowers/finance-scout-screens/` (not in git).

## Data problems found
- Kioxia (285A.T, Japan rank 3) dropped: Yahoo EPS is wrong (our P/E 12.2 on Yahoo EPS vs stockanalysis
  3.73; net income / shares gives 5.4); cause unknown. The 3:1 split of 2026-09-29 IS in Yahoo (prices
  adjusted, no one-day move over 25% since June; skill-session 2026-11-15); the earlier "missed split"
  explanation is withdrawn.
- CK Infrastructure (1038.HK, other Asia rank 3) dropped: EPS growth +389% is a one-off, Yahoo
  EV/EBITDA 168 vs stockanalysis 9.06 (EBITDA without associates); revenue growth only +7%.
- Yahoo P/E without FX (skill warning) on European/UK lines of USD reporters: true P/E Shell about 11.4
  (Yahoo 8.65), Rio Tinto about 15 (11.45), TTE 10.5 on Yahoo's stale EPS 8.62 (9.53 unconverted; 9.2 on the last 4 quarters, `research/stocks/TTE.md`) (skill-session vs filings 2026-11-15).
  stockanalysis.com repeats the same error (Shell 8.60, Rio 11.32, TTE 9.24), so its agreement with Yahoo
  proves nothing; it is not a second source for these P/Es. The run's conversion was right, so European
  ranks and passes are unchanged (rechecked with the fixed script: top 3 CCC, TTE, BBVA as before).
- HKEX: Yahoo EPS currency depends on the company. USD reporters (HSBC, AIA, Techtronic) had EPS in HKD
  (converting gave P/E 1.5-3.2); HK-listed mainland companies report in CNY and Yahoo EPS is CNY
  (2359: Yahoo P/E 18.9 = HKD price / CNY EPS; company basis 17.8, `news/2359.md`). The run treated all
  HKEX EPS as HKD, so 2359 (and likely other CNY reporters such as 2020, 2269, 9633, 2057, 0300, 3968; not checked) had P/E about
  15-18% too high.
- Yahoo EPS wrong for 8309 (193.84 vs company TTM 142.76 after the 4:1 split) and 9766 (1,322 vs 979.42)
  (`news/8309.md`, `news/9766.md`, TDnet). Yahoo net income / shares matches the filings for both.
- Marks and Spencer (MKS.L): EPS in pence for a GBP-reporting company gave P/E 0.37 and EPS growth
  +4,100% (Yahoo and recompute); P/E under 2 is dropped as a unit error.
- Yahoo ROE is trailing 12 months; screener.in shows the last full year (GESHIP 26% vs 15.9%,
  CHENNPETRO 51% vs 32%). Indian P/E matched the consolidated figures for all three Indian picks.
- Growth uses one quarter y/y: cyclical peaks (refiners, shipping, memory) dominate the growth and
  value ranks. The value screen has no own-history check.
- AngelOne holdings check: GESHIP, CHENNPETRO and MAHABANK are not held. AngelOne holds ICICIGI,
  DALBHARAT, FINPIPE, KPIL, TECHNOE, TIMETECHNO, AZAD, ELGIEQUIP, KIRLPNU, TEGA, SUZLON, ASTRAL and
  ETFs SILVER, SILVERIETF (`portfolio/summary.md` "AngelOne stocks and ETFs (holdings list)", commit
  fdf8efa; from the AngelOne Tax P&L FY2026-27 Open Holdings sheet to 2026-11-15).
- Index lists from Wikipedia may lag recent index changes.

Back to [Stock screens 2026-11-15](screens-2026-11-15.md) and [Ideas](../ideas.md).
