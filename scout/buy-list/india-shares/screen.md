# India shares screen: Nifty 200 (+ KVB, STARHEALTH, NH) - 2026-11-16

Written 2026-11-16 by `finance-scout` (scout-screen). Mechanical screen, not advice; the user decides.
Refined 2026-11-16 evening (EPS outliers) and 2026-11-17 (unadjusted bonus/split/demerger prices; research corrections for HDFCBANK, BAJAJ-AUTO, M&M, DIXON, MCX, COFORGE).

## Summary
- 203 stocks screened; 72 dropped on the quality and data rules, 131 scored and ranked.
- Top 5: GVT&D, KALYANKJIL, APLAPOLLO, POWERINDIA, TRENT. Many top names sit at the low end of their own P/E range, but own history is only about 3.6 years.
- User's names in the top 20: TRENT (5). Failing a quality or data rule: ETERNAL, HINDALCO, RELIANCE, SWIGGY, TMCV, TMPV, TATASTEEL, TITAN, STARHEALTH.
- Data: Yahoo Finance (yfinance 1.8.0) statements and estimates pulled 2026-11-16 20:59-21:14 IST; prices NSE
  bhavcopy close 2026-11-16. Of 16 EPS outliers, 1 was a Yahoo error (VBL, fixed); the rest are real earnings swings.

## Method
- Universe: `trading/universe/india.csv` (NSE `ind_nifty200list.csv`, built 2026-11-15, 200 names) plus KARURVYSYA,
  STARHEALTH, NH. Price: NSE bhavcopy close 2026-11-16 (`BhavCopy_NSE_CM_0_0_0_20261116_F_0000.csv`, EQ/BE series).
- Value (30%): current P/E (P/B for Financial Services) as a percentile of its own monthly history (annual EPS or
  book known 60 days after year end; 2.6-3.8 years available, not 5-10) and vs the median of its NSE sector here.
- Growth (25%): EPS CAGR over the last 3 fiscal years (annual diluted EPS) and forward growth = Yahoo forwardEps /
  trailingEps - 1 (ESTIMATE). Quality (25%): ROE 3y average, ROCE 3y (non-financials), D/E, OCF/PAT 3y. Trend (20%):
  price vs 200-day average, 6- and 12-month return. Each part = percentile rank among scored names; missing = 0.5.
- Drops: loss in TTM or in any of the last 3 years; ROE 3y below 12%; D/E above 1.5 or OCF/PAT 3y below 0.6
  (non-financials only); under 12 months of prices. Promoter pledge NOT checked (no scriptable source used).
  OCF/PAT is consolidated, except for groups with a lending arm (loan growth counts as operating outflow): there the
  standalone figure is used as a manual override from research (BAJAJ-AUTO, M&M); see Data errors.

## Top 20
| Rank | Symbol | Sector | Score (V/G/Q/T) | Price | Valuation | Growth | Quality (3y) | Trend |
|---|---|---|---|---|---|---|---|---|
| 1 | GVT&D | Capital Goods | 0.72 (0.56/0.81/0.88/0.62) | 4,337.0 | P/E 77.0 (0th pct of 2.6y; sector med 46.8) | EPS 3y -/yr, fwd +44% (est) | ROE +37%, ROCE +43%, D/E 0.01, OCF/PAT 1.55 | vs 200d +3%, 6m +0%, 12m +41% |
| 2 | KALYANKJIL | Consumer Durables | 0.67 (0.67/0.75/0.37/0.96) | 708.1 | P/E 45.7 (16th pct of 3.6y; sector med 61.4) | EPS 3y +46%/yr, fwd +31% (est) | ROE +18%, ROCE +14%, D/E 0.97, OCF/PAT 1.45 | vs 200d +50%, 6m +97%, 12m +39% |
| 3 | APLAPOLLO | Capital Goods | 0.67 (0.58/0.66/0.68/0.82) | 2,250.2 | P/E 47.7 (7th pct of 3.6y; sector med 46.8) | EPS 3y +23%/yr, fwd +37% (est) | ROE +22%, ROCE +25%, D/E 0.09, OCF/PAT 1.65 | vs 200d +11%, 6m +20%, 12m +25% |
| 4 | POWERINDIA | Capital Goods | 0.67 (0.50/0.97/0.61/0.60) | 30,885.0 | P/E 114.3 (0th pct of 3.6y; sector med 46.8) | EPS 3y +115%/yr, fwd +86% (est) | ROE +16%, ROCE +18%, D/E 0.02, OCF/PAT 1.95 | vs 200d +3%, 6m -4%, 12m +48% |
| 5 | TRENT | Consumer Services | 0.66 (0.49/0.85/0.62/0.73) | 3,203.7 | P/E 90.1 (14th pct of 3.6y; sector med 74.3) | EPS 3y +57%/yr, fwd +44% (est) | ROE +35%, ROCE +31%, D/E 0.37, OCF/PAT 1.19 | vs 200d +14%, 6m +16%, 12m +4% |
| 6 | HEROMOTOCO | Automobile and Auto Components | 0.65 (0.83/0.44/0.72/0.55) | 5,359.5 | P/E 17.9 (7th pct of 3.6y; sector med 34.9) | EPS 3y +27%/yr, fwd +7% (est) | ROE +25%, ROCE +31%, D/E 0.04, OCF/PAT 1.26 | vs 200d +3%, 6m +7%, 12m +5% |
| 7 | MAHABANK | Financial Services | 0.63 (0.40/0.69/0.63/0.92) | 92.0 | P/B 2.1 (81th pct of 3.6y; sector med 2.8) | EPS 3y +33%/yr, fwd +30% (est) | ROE +23% | vs 200d +19%, 6m +19%, 12m +59% |
| 8 | APOLLOHOSP | Healthcare | 0.63 (0.64/0.78/0.41/0.69) | 8,771.0 | P/E 56.1 (0th pct of 3.6y; sector med 49.8) | EPS 3y +33%/yr, fwd +40% (est) | ROE +18%, ROCE +16%, D/E 0.90, OCF/PAT 1.61 | vs 200d +8%, 6m +8%, 12m +15% |
| 9 | SOLARINDS | Chemicals | 0.62 (0.36/0.80/0.62/0.81) | 18,820.0 | P/E 75.2 (16th pct of 3.6y; sector med 32.2) | EPS 3y +30%/yr, fwd +46% (est) | ROE +30%, ROCE +30%, D/E 0.29, OCF/PAT 1.21 | vs 200d +9%, 6m +13%, 12m +41% |
| 10 | LGEINDIA | Consumer Durables | 0.62 (0.47/0.77/0.59/0.68) | 1,722.9 | P/E 60.8 (no history; sector med 61.4) | EPS 3y -/yr, fwd +41% (est) | ROE +22%, ROCE +29%, D/E 0.06, OCF/PAT 1.02 | vs 200d +9%, 6m +10%, 12m +7% |
| 11 | HAL | Capital Goods | 0.61 (0.59/0.45/0.81/0.58) | 4,789.0 | P/E 33.4 (33th pct of 3.6y; sector med 46.8) | EPS 3y +16%/yr, fwd +21% (est) | ROE +26%, ROCE +32%, D/E 0.00, OCF/PAT 1.31 | vs 200d +7%, 6m +4%, 12m +5% |
| 12 | NATIONALUM | Metals & Mining | 0.61 (0.73/0.51/0.74/0.37) | 318.9 | P/E 8.2 (14th pct of 3.6y; sector med 12.0) | EPS 3y +59%/yr, fwd +2% (est) | ROE +26%, ROCE +31%, D/E 0.01, OCF/PAT 1.15 | vs 200d -13%, 6m -22%, 12m +43% |
| 13 | LICI | Financial Services | 0.60 (0.59/0.44/0.96/0.37) | 400.0 | P/B 2.9 (5th pct of 3.6y; sector med 2.8) | EPS 3y +17%/yr, fwd +20% (est) | ROE +49% | vs 200d -1%, 6m +2%, 12m -11% |
| 14 | DIXON | Consumer Durables | 0.60 (0.30/0.93/0.65/0.58) | 12,890.0 | P/E 88.9 (37th pct of 3.6y; sector med 61.4) | EPS 3y +48%/yr, fwd +89% (est) | ROE +25%, ROCE +37%, D/E 0.21, OCF/PAT 1.21 | vs 200d +6%, 6m +16%, 12m -13% |
| 15 | HINDCOPPER EPS-check | Metals & Mining | 0.59 (0.51/0.86/0.67/0.30) | 430.6 | P/E 28.3 (0th pct of 3.6y; sector med 12.0) | EPS 3y +46%/yr, fwd +52% (est) | ROE +21%, ROCE +25%, D/E 0.03, OCF/PAT 1.41 | vs 200d -17%, 6m -29%, 12m +30% |
| 16 | LODHA | Realty | 0.59 (0.81/0.65/0.14/0.76) | 1,192.8 | P/E 27.5 (5th pct of 3.6y; sector med 41.0) | EPS 3y +89%/yr, fwd +19% (est) | ROE +14%, ROCE +14%, D/E 0.42, OCF/PAT 0.65 | vs 200d +17%, 6m +37%, 12m -2% |
| 17 | RADICO | Fast Moving Consumer Goods | 0.59 (0.42/0.80/0.31/0.95) | 4,665.0 | P/E 78.5 (14th pct of 3.6y; sector med 43.6) | EPS 3y +40%/yr, fwd +40% (est) | ROE +15%, ROCE +16%, D/E 0.24, OCF/PAT 1.05 | vs 200d +26%, 6m +35%, 12m +47% |
| 18 | INDHOTEL | Consumer Services | 0.59 (0.48/0.62/0.43/0.92) | 886.0 | P/E 57.1 (51th pct of 3.6y; sector med 74.3) | EPS 3y +28%/yr, fwd +24% (est) | ROE +17%, ROCE +18%, D/E 0.22, OCF/PAT 1.26 | vs 200d +27%, 6m +37%, 12m +29% |
| 19 | IRCTC | Consumer Services | 0.59 (0.87/0.53/0.70/0.10) | 451.6 | P/E 27.5 (7th pct of 3.6y; sector med 74.3) | EPS 3y +11%/yr, fwd +36% (est) | ROE +37%, ROCE +45%, D/E 0.02, OCF/PAT 0.78 | vs 200d -13%, 6m -16%, 12m -35% |
| 20 | WAAREEENER | Capital Goods | 0.59 (0.83/0.69/0.59/0.08) | 2,441.0 | P/E 19.0 (12th pct of 2.2y; sector med 46.8) | EPS 3y +97%/yr, fwd +21% (est) | ROE +33%, ROCE +30%, D/E 0.26, OCF/PAT 1.04 | vs 200d -14%, 6m -20%, 12m -25% |

`EPS-check` = Yahoo TTM EPS differs from the last annual EPS by over 60%; checked against the last 4 quarters (see Data
errors): for the names shown here it is a real earnings swing, not a Yahoo error. Score = weighted total (value/growth/quality/trend sub-scores, 0-1).

## User's names
| Symbol | Rank or drop | Price | Valuation | Growth | Quality (3y) | Trend |
|---|---|---|---|---|---|---|
| RELIANCE | dropped: ROE 3y 9% < 12% | 1,344.8 | P/E 22.2 (14th pct of 3.6y; sector med 8.3) | EPS 3y +7%/yr, fwd +22% (est) | ROE +9%, ROCE +11%, D/E 0.44, OCF/PAT 2.41 | vs 200d +2%, 6m -1%, 12m -9% |
| TCS | 36 of 131 | 2,405.0 | P/E 16.9 (7th pct of 3.6y; sector med 23.5) | EPS 3y +6%/yr, fwd +13% (est) | ROE +51%, ROCE +61%, D/E 0.11, OCF/PAT 1.01 | vs 200d +2%, 6m +10%, 12m -16% |
| TMPV | dropped: loss | 262.4 | P/E - (no history; sector med 34.9) | EPS 3y -/yr, fwd - (est) | ROE +49%, ROCE +12%, D/E 0.73, OCF/PAT 1.02 | vs 200d -21%, 6m -22%, 12m -35% |
| TMCV EPS-check | dropped: under 12 months of prices (new listing); statements may be pre-demerger | 428.2 | P/E 25.0 (no history; sector med 46.8) | EPS 3y -/yr, fwd +37% (est) | ROE +23%, ROCE +25%, D/E 0.44, OCF/PAT 3.81 | vs 200d -, 6m -, 12m - |
| TATASTEEL | dropped: loss; ROE 3y 3% < 12% | 182.3 | P/E 19.6 (35th pct of 2.6y; sector med 12.0) | EPS 3y +6%/yr, fwd - (est) | ROE +3%, ROCE +8%, D/E 0.90, OCF/PAT 8.03 | vs 200d -5%, 6m -16%, 12m +3% |
| TITAN | dropped: D/E 2.0 > 1.5; OCF/PAT 3y 0.57 < 0.6 | 4,910.0 | P/E 62.0 (0th pct of 3.6y; sector med 61.4) | EPS 3y +16%/yr, fwd +12% (est) | ROE +34%, ROCE +18%, D/E 1.95, OCF/PAT 0.57 | vs 200d +10%, 6m +19%, 12m +31% |
| TRENT | 5 of 131 | 3,203.7 | P/E 90.1 (14th pct of 3.6y; sector med 74.3) | EPS 3y +57%/yr, fwd +44% (est) | ROE +35%, ROCE +31%, D/E 0.37, OCF/PAT 1.19 | vs 200d +14%, 6m +16%, 12m +4% |
| SWIGGY | dropped: loss; ROE 3y -31% < 12% | 190.7 | P/E - (no history; sector med 74.3) | EPS 3y -/yr, fwd - (est) | ROE -31%, ROCE -24%, D/E 0.14, OCF/PAT - | vs 200d -29%, 6m -26%, 12m -52% |
| ETERNAL | dropped: ROE 3y 2% < 12% | 371.1 | P/E 700.2 (84th pct of 2.6y; sector med 74.3) | EPS 3y -/yr, fwd +489% (est) | ROE +2%, ROCE +2%, D/E 0.15, OCF/PAT 1.27 | vs 200d +31%, 6m +51%, 12m +21% |
| STARHEALTH EPS-check | dropped: ROE 3y 10% < 12% | 568.0 | P/B 4.4 (56th pct of 3.6y; sector med 2.8) | EPS 3y -3%/yr, fwd +66% (est) | ROE +10% | vs 200d +8%, 6m +12%, 12m +16% |
| NH | 70 of 131 | 1,895.3 | P/E 44.6 (56th pct of 3.6y; sector med 49.8) | EPS 3y +10%/yr, fwd +64% (est) | ROE +25%, ROCE +17%, D/E 1.29, OCF/PAT 1.54 | vs 200d +3%, 6m +4%, 12m +5% |
| BPCL | 82 of 131 | 305.3 | P/E 8.3 (44th pct of 3.6y; sector med 8.3) | EPS 3y +129%/yr, fwd +8% (est) | ROE +29%, ROCE +24%, D/E 0.54, OCF/PAT 1.67 | vs 200d -3%, 6m +3%, 12m -15% |
| COALINDIA | 119 of 131 | 397.5 | P/E 7.3 (77th pct of 3.6y; sector med 8.3) | EPS 3y -1%/yr, fwd +4% (est) | ROE +39%, ROCE +43%, D/E 0.12, OCF/PAT 0.88 | vs 200d -4%, 6m -8%, 12m +13% |
| LT | 44 of 131 | 4,140.0 | P/E 31.9 (5th pct of 3.6y; sector med 38.0) | EPS 3y +16%/yr, fwd +39% (est) | ROE +16%, ROCE +12%, D/E 1.15, OCF/PAT 1.00 | vs 200d +5%, 6m +6%, 12m +8% |
| HINDALCO | dropped: ROE 3y 11% < 12% | 923.3 | P/E 10.7 (26th pct of 3.6y; sector med 12.0) | EPS 3y +10%/yr, fwd +30% (est) | ROE +11%, ROCE +11%, D/E 0.73, OCF/PAT 1.48 | vs 200d -6%, 6m -16%, 12m +17% |
| KARURVYSYA | 55 of 131 | 390.2 | P/B 2.7 (98th pct of 3.6y; sector med 2.8) | EPS 3y +31%/yr, fwd +14% (est) | ROE +18% | vs 200d +25%, 6m +36%, 12m +58% |

Tata Motors: after the 2025 demerger NSE lists TMPV (Tata Motors Passenger Vehicles, the old entity) and TMCV (Tata
Motors Ltd, commercial vehicles, listed Nov 2025). TMCV has under a year of prices and Yahoo statements that may be
the pre-demerger group, so it is not ranked (on its numbers alone it would score 0.69, about rank 2: not reliable).

## Drops (72)
- Loss (12): e.g. GMRAIRPORT, GLENMARK, GODREJCP, INDIGO, MEESHO, PAYTM, SWIGGY, TMPV.
- ROE 3y below 12% (53): e.g. ADANIENSOL, ADANIGREEN, AMBUJACEM, AUROPHARMA, BANKINDIA, BHEL, BIOCON, COFORGE.
- D/E above 1.5 (13): e.g. ADANIENSOL, ADANIGREEN, ASHOKLEY, GRASIM, INDIGO, JSWENERGY, JUBLFOOD, POWERGRID.
- OCF/PAT 3y below 0.6 (13): e.g. ASHOKLEY, BEL, COCHINSHIP, GODFRYPHLP, GODREJPROP, GRASIM, MAZDOCK, PATANJALI.
- New listings (under 12 months of prices): GROWW, ICICIAMC, LENSKART, MEESHO, TMCV, VAML.
- Counts overlap (a stock can fail several rules). Full list: work folder `screen_raw.csv`.

## Data errors and checks
- EPS outliers: 16 names had Yahoo TTM EPS more than 60% away from the last annual EPS. Checked against the sum of
  the last 4 quarters (Yahoo quarterly statements, quarter to 2026-09-30, pulled 2026-11-16):
  - Yahoo error, fixed: VBL trailingEps 2.89 vs 4-quarter sum 10.27 (annual 8.98); the screen now uses 10.27
    (P/E 42.6, rank 48).
  - Units: INFY (and HCLTECH) statements are in USD on Yahoo (annual EPS 0.80 USD vs TTM 75.10 INR); ratios and
    own-history percentiles are unaffected, the flag was spurious.
  - Real swings, Yahoo consistent (quarterly sum = trailingEps): ADANIENSOL, AMBUJACEM, BHEL, NYKAA, GAIL, GMRAIRPORT,
    HINDCOPPER, HINDPETRO (FY26 84.81 to TTM 6.75), IDFCFIRSTB, INDUSINDBK, MFSL, SAIL, STARHEALTH, TMCV (demerger).
  - Still single source (Yahoo); consolidated vs standalone not confirmed against NSE filings.
- Unadjusted prices fixed 2026-11-17 (NSE corporate-actions API, ex-dates Nov 2025 to Nov 2026, read 2026-11-17; plus a
  scan of every name for one-day moves over -25%/+40% not matched by the Nifty). Prices before the date are scaled:
  - TRENT: 1:2 bonus (ex 2026-06-04); Yahoo history before 2026-01-01 was not adjusted (-33% step on 2026-01-01).
    Fixed (x 2/3): 12m return -31% -> +4% (finance-research: 1y +9.6% to its date), rank 10 -> 6. EPS was adjusted.
  - MOTILALOFS: 3:1 bonus; Yahoo history before 2024-01-01 not adjusted (-74.6% step). Fixed (x 1/4): own-history
    percentile 72nd -> 91st, rank 24 -> 27.
  - VEDL: demerger (ex 2026-04-30), not adjusted by Yahoo (-65% that day). Prior prices scaled by the ex-day ratio net
    of the Nifty (0.354, approximate): 12m -49% -> +44%, vs 200d -38% -> -4%, rank 93 -> 61.
  - HINDUNILVR: ice-cream demerger (ex 2025-12-05), -5.6% net that day; scaled the same way: 12m -16% -> -11%,
    rank 92 -> 89. Statement EPS for VEDL and HINDUNILVR still includes the demerged businesses.
  - Checked and already adjusted by Yahoo (no step at the ex-date; EPS and share counts adjusted): HDFCAMC (1:1 bonus
    2025-11-26), MCX (split 10 to 2, 2026-01-02), KOTAKBANK (split 5 to 1, 2026-01-14), LICI (1:1 bonus 2026-05-29).
  - Not fixed: TMPV demerger (ex 2025-10-14, -40% step) affects only its own history (dropped anyway: loss);
    POLICYBZR -36% on 2026-09-24 with no NSE bonus/split/demerger listed: unexplained, check (dropped anyway: ROE 6%).
- TATASTEEL forward estimate suspect: Yahoo forwardEps Rs 19.5 gives forward P/E about 9.3 and "fwd +110%" growth,
  but reported H1 plus the quarter estimates give FY27 EPS near Rs 11.4, about 15-16x (finance-research,
  `research/stocks/TATASTEEL.md` s5; possibly standalone vs consolidated, not confirmed). The screen no longer uses its
  forward EPS; it is dropped anyway (ROE 3y 3%), so the ranking does not change.
- Research corrections 2026-11-17 (finance-research deep dives; inputs overridden, then re-ranked):
  - HDFCBANK: ROE 13.5-14.4% (FY25 14.4%, FY26 13.7%, TTM 13.5%), not Yahoo's 10-11%: the ROE drop misfired; ROE 13.9%
    used, now ranked. Research: BUY IN STEPS, max Rs 830 at the 17 Nov open ([HDFCBANK](../../../research/stocks/HDFCBANK.md)).
  - BAJAJ-AUTO: standalone OCF/PAT 0.93 (consolidated 0.30 is Bajaj Auto Credit loan growth): the drop misfired;
    clean P/E 26.4, not 22.6 (Rs 1,599 Cr KTM one-off gain). Research: BUY IN STEPS, first step only, max Rs 10,800
    ([BAJAJ-AUTO](../../../research/stocks/BAJAJ-AUTO.md)).
  - M&M: standalone OCF/PAT 1.31 (consolidated 0.22 is Mahindra Finance loan growth): the drop misfired. Research:
    BUY IN STEPS, Rs 3 L total, max Rs 3,400 ([MM](../../../research/stocks/MM.md)).
  - DIXON: clean P/E about 89 (clean EPS Rs 145), not 45: Yahoo EPS 286.5 includes Aditya Infotech stake gains and
    the minorities' share; clean EPS growth about 48%/yr, ROE about 25% (FY26 28.1%, H1 FY27 22.2%) used. Research: NOT fit
    for a buy now; WATCH, buy in steps at or below Rs 10,500 / 9,500 ([DIXON](../../../research/stocks/DIXON.md)).
  - MCX: Yahoo EPS (57.97) and P/B (book Rs 195) are wrong: TTM EPS 70.55 (P/E 53), P/B 27.1 on Sep-2026 book, top 6%
    of 10 years, used. Research: NOT fit for a buy now; WATCH, buy in steps at or below Rs 3,000 / 2,700
    ([MCX](../../../research/stocks/MCX.md)).
  - COFORGE: row stale after the Encora deal: ROE about 10% on today's book (not 20%), D/E 0.27 (not 0.08), and
    "fwd +47%" compared next year with the last 12 months; this year's growth is +22%. Inputs fixed: it now fails the
    ROE rule (was rank 6). Research: WATCH, not for the 17 Nov open (Rs 2,010); Rs 50k at or below Rs 1,800 and Rs 50k
    at or below Rs 1,650 or after Q3 (about 21 Jan 2027) if organic growth >= 2.5% q/q and EBIT margin >= 16%
    ([COFORGE](../../../research/stocks/COFORGE.md)).
  - NATIONALUM: no input change (Yahoo figures are right; the screen does not model the cycle). Peak-margin
    caution: P/E 8.2 is on peak margins (47%, about twice the 10-year norm); alumina is at $398, down from about $810,
    with new refinery supply coming, so earnings are likely to fall. Research: WATCH, not for the 17 Nov open
    (Rs 318.95); Rs 1 L at or below Rs 270 and Rs 1 L at or below Rs 240; Hindalco stays research's preferred metals
    buy ([NATIONALUM](../../../research/stocks/NATIONALUM.md)).
  - Knock-on: DIXON's higher P/E raises the Consumer Durables median, so LGEINDIA looks cheaper vs its sector (rank
    23 -> 11). Scores from rank 9 to 25 are within 0.05, so small input changes move ranks.
- Still near a rule edge (not overridden): POWERGRID D/E 1.5, BANKINDIA and PATANJALI ROE 12%, HINDALCO ROE 11%,
  TITAN D/E 2.0 (gold metal loans count as debt), BEL OCF/PAT 0.44.
- Manual checks (screener.in `/company/<SYMBOL>/consolidated/`, one page at a time, viewing only; no scripts):
  - Top 20: GVT&D, KALYANKJIL, APLAPOLLO, POWERINDIA, TRENT, HEROMOTOCO, MAHABANK, APOLLOHOSP, SOLARINDS, LGEINDIA, HAL, NATIONALUM, LICI, DIXON, HINDCOPPER, LODHA, RADICO, INDHOTEL, IRCTC, WAAREEENER.
  - User's names: RELIANCE, TCS, TMPV, TMCV, TATASTEEL, TITAN, TRENT, SWIGGY, ETERNAL, STARHEALTH, NH, BPCL, COALINDIA, LT, HINDALCO, KARURVYSYA.
  - Rule-edge drops: POWERGRID, BANKINDIA, PATANJALI, HINDALCO, TITAN, BEL.
  - Check for each: consolidated TTM EPS and P/E, 3-year ROE, debt/equity, CFO/PAT, promoter pledge (shareholding).
- Own-history valuation covers only 2.6-3.8 years (Yahoo annual statements), not the 5-10 years asked.
- Raw data: `~/.local/share/superpowers/finance-scout-special/work/screen_raw.csv` (not in the repository).
