# US shares screen: S&P 500 + Nasdaq-100 + S&P 400

## Summary
- 918 unique US-listed names screened (prices: 16 Nov 2026 intraday, pulled 21:45 IST); 409 pass the quality filter; top 30 below: 22 BUY, 1 BUY BELOW a price, 7 WATCH.
- Leaders: EXEL, EXPE, HRB, AMP, GDDY, DXCM, ANF, RNR, PTC, THC.
- Research verdicts (finance-research, 17 Nov 2026) on all ten leaders: BUY IN STEPS AMP and RNR (RNR instead of Munich Re); SKIP PTC (Schneider cash bid $205; Dassault DSY instead); WATCH EXEL, EXPE, HRB, GDDY, DXCM, ANF, THC. Research wins over the verdicts below; entries in "Research verdicts" and the funding proposal in the [global README](README.md#global-buys-vs-current-plan-proposal-you-decide).
- 3 of the top 30 are non-US companies (not US-situs); the rest add to the US estate-tax exposure (`scout/ideas/us-estate-tax.md`). Chip names (incl. NAND maker SNDK) with corr >= 0.3 to QCOM are kept out of the top 30.
- Money: the 5% for ideas is nearly used (Rs 20.75 L of 21.05 L, `scout/buy-list.md`); any BUY here is a swap candidate at most 1% (about Rs 4.2 L), not new money.
- Screen only, no deep dives yet: 10 of the top 30 are IT (research says do not add tech, `not-included.md`); 3-y growth often starts from a low base; refiners and insurers are cheap on current profits with falling estimates. Check each pick against its filings.

## Research verdicts (17 Nov 2026)
finance-research deep dives (`research/stocks/<ticker>.md`, 16 Nov closes). Other names in the top 30 have no note.

| Ticker | Research | Entry steps | What research changed |
|---|---|---|---|
| [EXEL](../../../research/stocks/EXEL.md) | WATCH | $52 or less after the FDA decision of 3 Mar 2027 (now $67.10) | 3-yr growth from a low base; DCF base $39; corr QCOM 0.10, MSFT 0.04 |
| [EXPE](../../../research/stocks/EXPE.md) | WATCH | Rs 2.1 L at or below $255, Rs 2.1 L at or below $225, after the Q4 guidance (about 11 Feb 2027) | Q4 bookings slowed to +3-5%; corr with MSFT 0.39 |
| [HRB](../../../research/stocks/HRB.md) | WATCH | up to Rs 2 L at or below $44 ($52 after good May 2027 results) | +75% from its Feb 2026 low |
| [AMP](../../../research/stocks/AMP.md) | BUY IN STEPS | 4 shares (about Rs 1.93 L) at or below $530 (now $514.06); 4 more at or below $470 or after good Q4 results (28 Jan 2027) | Corr: research QCOM 0.08, MSFT 0.23 (weekly, 2 yr) vs this screen 0.31 (daily vs QCOM); US-situs; UK alternative St. James's Place |
| [GDDY](../../../research/stocks/GDDY.md) | WATCH | Rs 2.1 L at or below $115, Rs 2.1 L at or below $100, after the 1 Dec investor night | Corr with QCOM 0.27; tech; class action pending |
| [DXCM](../../../research/stocks/DXCM.md) | WATCH | $66 or less (now $81.61) | Medicare bidding cuts prices from 2028; DCF $42-62 |
| [ANF](../../../research/stocks/ANF.md) | WATCH | $118 or less, only if Q3 (24 Nov) margin is 12.5%+ without tariff refunds | P/E 12.5 includes a one-off $1.75/share tariff refund (14.7 without); peak margins |
| [RNR](../../../research/stocks/RNR.md) | BUY IN STEPS | Rs 1.9 L (6 shares) at or below $340 (now $356.59); Rs 1.8 L (6) at or below $315 | Pick over Munich Re (P/B 1.37 vs 2.23; RNR-Munich Re corr 0.41); corr QCOM+MSFT -0.11; not US-situs (Bermuda; not confirmed for this issuer) |
| [PTC](../../../research/stocks/PTC.md) | SKIP (DSY instead) | Dassault DSY: Rs 2.1 L at or below EUR 26 after 17 Nov, Rs 2.1 L at or below 23 | Schneider agreed on 4 Oct 2026 to buy PTC for $205 cash: the screen missed the takeover |
| [THC](../../../research/stocks/THC.md) | WATCH | about Rs 3.8 L at or below $240 after the 2027 guidance (about 10 Feb) | P/E 8.5 is false: $1.47 bn one-off contract-termination revenue; clean P/E 13-16 |

## Method
- Universe: Wikipedia lists (S&P 500, S&P 400, List of NASDAQ-100 companies), read 2026-11-16 20:59 IST; GICS sectors from the S&P lists, ICB for the 15 Nasdaq-only names (mapped by hand to GICS).
- Fundamentals: SEC XBRL companyfacts (TTM = last annual + YTD - prior YTD; EPS split-adjusted with Yahoo split dates); domicile from EDGAR state of incorporation. Prices, splits and forward estimates: yfinance (cached, throttled).
- Value: P/E (P/B for banks) percentile vs own monthly history (up to 10 y, EPS known 60 days after period end) and P/E ratio to the GICS sector median of the survivors. Growth: 3-y TTM EPS CAGR and next-FY consensus EPS growth (estimate). Quality: 3-FY average ROE and ROIC, net debt/EBITDA, 3-FY FCF/net income. Trend: price vs 200-day average, 6- and 12-month return.
- Dropped: TTM or last-FY loss, 3-FY ROE < 12% (ROIC where equity is negative), net debt/EBITDA > 3 or FCF/NI < 0.6 (non-financials). Score = percentile ranks among survivors, weights value 0.3, growth 0.25, quality 0.25, trend 0.2; ties go to non-US companies.
- Verdict: BUY = above the 200-day average and at or below its own median valuation; BUY BELOW X = above its median (X = price at its own median P/E or P/B); WATCH = below the 200-day average, or a chip name with corr >= 0.3. Held names and buy-list names are marked and left out of the top 30.

## Top 30
Columns: value = P/E now (percentile in own history; ratio to sector median); growth = 3-y EPS CAGR / next-FY growth (estimate); quality = 3-FY averages; trend = vs 200-day / 6 m / 12 m; corr = daily returns vs QCOM, 2 years.

| # | Ticker | Name | Sector | Value | Growth 3y / fwd | Quality | Trend | Score | Verdict | US estate tax | Chip | Similar non-US listing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | EXEL | Exelixis | Health Care | P/E 20.4 (own 36%, x0.76 sector); EV/EBITDA 17.5 | 126% / 14% est | ROE 22%, ROIC 24%, ND/EBITDA -0.7, FCF/NI 1.22 | 30% / 37% / 61% | 0.77 | BUY | US-situs | no, corr 0.13 | Ipsen (Euronext Paris, IPN; sells cabozantinib outside the US) |
| 2 | EXPE | Expedia Group | Consumer Discretionary | P/E 15.0 (own 1%, x0.87 sector); EV/EBITDA 8.5 | 46% / 17% est | ROE 71%, ROIC 28%, ND/EBITDA -0.0, FCF/NI 2.19 | -1% / 19% / -4% | 0.75 | WATCH (below 200-day) | US-situs | no, corr 0.22 | none close |
| 3 | HRB | H&R Block | Consumer Discretionary | P/E 9.3 (own 27%, x0.54 sector); EV/EBITDA 7.4 | 16% / 12% est | ROE 786%, ROIC 104%, ND/EBITDA 1.1, FCF/NI 1.04 | 27% / 31% / 16% | 0.73 | BUY | US-situs | no, corr -0.02 | none |
| 4 | AMP | Ameriprise Financial | Financials | P/E 11.7 (own 30%, x0.73 sector); EV/EBITDA 8.8 | 20% / 12% est | ROE 63%, ROIC -, ND/EBITDA fin, FCF/NI fin | 6% / 10% / 14% | 0.72 | BUY | US-situs | no, corr 0.31 | St. James's Place (LSE, STJ); Amundi (Paris, AMUN) |
| 5 | GDDY | GoDaddy | Information Technology | P/E 15.7 (own 38%, x0.57 sector); EV/EBITDA 12.6 | - / 22% est | ROE 221%, ROIC 21%, ND/EBITDA 1.9, FCF/NI 1.21 | 24% / 25% / -13% | 0.72 | BUY | US-situs | no, corr 0.02 | IONOS Group (Xetra, IOS) |
| 6 | DXCM | Dexcom | Health Care | P/E 32.5 (own 5%, x1.20 sector); EV/EBITDA 21.5 | 41% / 16% est | ROE 29%, ROIC 34%, ND/EBITDA 0.3, FCF/NI 1.14 | 10% / 27% / 38% | 0.72 | BUY | US-situs | no, corr 0.20 | none close |
| 7 | ANF | Abercrombie & Fitch | Consumer Discretionary | P/E 12.5 (own 35%, x0.73 sector); EV/EBITDA 7.5 | 76% / -1% est | ROE 41%, ROIC 99%, ND/EBITDA 0.7, FCF/NI 1.00 | 34% / 101% / 102% | 0.72 | BUY | US-situs | no, corr 0.19 | Inditex (Madrid, ITX) |
| 8 | RNR | RenaissanceRe | Financials | P/E 9.2 (own 43%, x0.57 sector); EV/EBITDA 5.3 | 11% / 35% est | ROE 26%, ROIC 25%, ND/EBITDA fin, FCF/NI fin | 13% / 20% / 34% | 0.71 | BUY | no (Bermuda) | no, corr -0.04 | itself Bermuda; Hannover Re (HNR1), Swiss Re (SREN); Munich Re already on the buy list |
| 9 | PTC | PTC Inc. | Information Technology | P/E 19.0 (own 6%, x0.70 sector); EV/EBITDA 20.0 | 59% / 11% est | ROE 14%, ROIC 12%, ND/EBITDA 0.9, FCF/NI 1.61 | 32% / 36% / 12% | 0.71 | BUY | US-situs | no, corr 0.10 | Dassault Systemes (Paris, DSY); Nemetschek (Xetra, NEM) |
| 10 | THC | Tenet Health | Health Care | P/E 8.5 (own 30%, x0.32 sector); EV/EBITDA 5.6 | 99% / -10% est | ROE 63%, ROIC 21%, ND/EBITDA 1.7, FCF/NI 1.01 | 30% / 52% / 49% | 0.71 | BUY | US-situs | no, corr 0.10 | Fresenius (Xetra, FRE; Helios hospitals) |
| 11 | DELL | Dell Technologies | Information Technology | P/E 18.9 (own 44%, x0.69 sector); EV/EBITDA 13.7 | 88% / 18% est | ROE n/m (neg. equity), ROIC 21%, ND/EBITDA 1.3, FCF/NI 1.17 | -6% / 37% / 144% | 0.70 | WATCH (below 200-day) | US-situs | no, corr 0.40 | Lenovo (HKEX 0992), not EU/JP |
| 12 | ADBE | Adobe Inc. | Information Technology | P/E 13.9 (own 2%, x0.51 sector); EV/EBITDA 10.0 | 17% / 12% est | ROE 42%, ROIC 47%, ND/EBITDA -0.1, FCF/NI 1.36 | 1% / -2% / -25% | 0.70 | BUY | US-situs | no, corr 0.14 | none close |
| 13 | QLYS | Qualys | Information Technology | P/E 29.2 (own 17%, x1.07 sector); EV/EBITDA 23.9 | 18% / 8% est | ROE 42%, ROIC 65%, ND/EBITDA -1.2, FCF/NI 1.47 | 27% / 79% / 22% | 0.70 | BUY | US-situs | no, corr 0.15 | Trend Micro (TSE 4704) |
| 14 | PDD | PDD Holdings | Consumer Discretionary | P/E 8.8 (own -, x0.51 sector); EV/EBITDA - | 18% / 21% est | ROE 37%, ROIC 31%, ND/EBITDA -4.1, FCF/NI 1.20 | -13% / -18% / -42% | 0.69 | WATCH (below 200-day) | no (Cayman Islands) | no, corr 0.18 | itself Cayman |
| 15 | GAP | Gap Inc. | Consumer Discretionary | P/E 6.0 (own 2%, x0.35 sector); EV/EBITDA 3.0 | 125% / 9% est | ROE 24%, ROIC 30%, ND/EBITDA -0.5, FCF/NI 1.38 | -11% / -2% / -15% | 0.69 | WATCH (below 200-day) | US-situs | no, corr 0.25 | Inditex (ITX); H&M (Stockholm, HM-B); Fast Retailing (TSE 9983) |
| 16 | IT | Gartner | Information Technology | P/E 13.6 (own 1%, x0.50 sector); EV/EBITDA 9.6 | 6% / 10% est | ROE 135%, ROIC 51%, ND/EBITDA 0.9, FCF/NI 1.26 | 13% / 22% / -17% | 0.69 | BUY | US-situs | no, corr 0.13 | Wolters Kluwer (Amsterdam, WKL); RELX (LSE, REL) |
| 17 | ACN | Accenture | Information Technology | P/E 18.6 (own 11%, x0.68 sector); EV/EBITDA 12.7 | 8% / 8% est | ROE 26%, ROIC 31%, ND/EBITDA -0.2, FCF/NI 1.33 | 34% / 45% / 5% | 0.68 | BUY | no (Ireland) | no, corr 0.07 | itself Irish; Capgemini (Paris, CAP) |
| 18 | ADSK | Autodesk | Information Technology | P/E 34.9 (own 5%, x1.27 sector); EV/EBITDA 25.2 | 24% / 13% est | ROE 50%, ROIC 36%, ND/EBITDA -0.3, FCF/NI 1.67 | 15% / 11% / -9% | 0.68 | BUY | US-situs | no, corr 0.12 | Dassault Systemes (DSY); Nemetschek (NEM) |
| 19 | NBIX | Neurocrine Biosciences | Health Care | P/E 24.8 (own 14%, x0.92 sector); EV/EBITDA 19.0 | 53% / 16% est | ROE 14%, ROIC 16%, ND/EBITDA -0.3, FCF/NI 1.56 | 12% / 6% / 16% | 0.68 | BUY | US-situs | no, corr 0.24 | UCB (Brussels, UCB; neurology) |
| 20 | MORN | Morningstar, Inc. | Financials | P/E 21.9 (own 11%, x1.37 sector); EV/EBITDA 12.9 | 90% / 14% est | ROE 21%, ROIC 18%, ND/EBITDA fin, FCF/NI fin | 33% / 42% / 18% | 0.68 | BUY | US-situs | no, corr 0.04 | LSEG (LSE, LSEG); RELX |
| 21 | TRV | Travelers Companies (The) | Financials | P/E 10.6 (own 9%, x0.67 sector); EV/EBITDA 8.5 | 60% / -15% est | ROE 18%, ROIC 13%, ND/EBITDA fin, FCF/NI fin | 21% / 33% / 43% | 0.68 | BUY | US-situs | no, corr 0.03 | Chubb (CB, Swiss company, US-listed); Tokio Marine (TSE 8766); Zurich (SIX, ZURN) |
| 22 | PCTY | Paylocity | Industrials | P/E 35.6 (own 10%, x1.41 sector); EV/EBITDA 19.4 | 26% / 9% est | ROE 21%, ROIC 29%, ND/EBITDA -0.1, FCF/NI 1.80 | 42% / 62% / 23% | 0.67 | BUY | US-situs | no, corr 0.09 | Sage Group (LSE, SGE) |
| 23 | MPC | Marathon Petroleum | Energy | P/E 8.0 (own 34%, x0.57 sector); EV/EBITDA 5.4 | 24% / -13% est | ROE 26%, ROIC 17%, ND/EBITDA 0.8, FCF/NI 1.35 | 34% / 57% / 111% | 0.67 | BUY | US-situs | no, corr 0.20 | ENEOS (TSE 5020); Idemitsu (TSE 5019) |
| 24 | PGR | Progressive Corporation | Financials | P/E 12.0 (own 21%, x0.75 sector); EV/EBITDA 9.5 | 63% / -12% est | ROE 33%, ROIC 24%, ND/EBITDA fin, FCF/NI fin | 13% / 17% / 14% | 0.66 | BUY | US-situs | no, corr -0.08 | Admiral Group (LSE, ADM); Tokio Marine (TSE 8766) |
| 25 | PEGA | Pegasystems | Information Technology | P/E 20.0 (own 9%, x0.73 sector); EV/EBITDA 31.5 | - / 13% est | ROE 35%, ROIC 42%, ND/EBITDA -1.3, FCF/NI 1.84 | -10% / -5% / -43% | 0.66 | WATCH (below 200-day) | US-situs | no, corr 0.19 | none close |
| 26 | MA | Mastercard | Financials | P/E 34.9 (own 21%, x2.18 sector); EV/EBITDA 26.9 | 19% / 15% est | ROE 191%, ROIC 78%, ND/EBITDA fin, FCF/NI fin | 23% / 32% / 21% | 0.66 | BUY | US-situs | no, corr 0.12 | Adyen (Amsterdam, ADYEN) |
| 27 | NTAP | NetApp | Information Technology | P/E 24.8 (own 67%, x0.91 sector); EV/EBITDA 17.0 | 9% / 11% est | ROE 100%, ROIC 56%, ND/EBITDA -0.5, FCF/NI 1.37 | 14% / 46% / 63% | 0.66 | BUY BELOW 148 | US-situs | no, corr 0.43 | none close |
| 28 | HON | Honeywell Technologies | Industrials | P/E 14.6 (own 5%, x0.58 sector); EV/EBITDA 11.4 | 24% / 17% est | ROE 32%, ROIC 17%, ND/EBITDA 1.0, FCF/NI 0.95 | -3% / -2% / 8% | 0.66 | WATCH (below 200-day) | US-situs | no, corr 0.35 | Siemens (Xetra, SIE); ABB (SIX, ABBN) |
| 29 | EXLS | EXL Service | Industrials | P/E 26.0 (own 9%, x1.03 sector); EV/EBITDA 17.0 | 17% / 13% est | ROE 24%, ROIC 20%, ND/EBITDA 0.4, FCF/NI 1.07 | 32% / 50% / 9% | 0.66 | BUY | US-situs | no, corr 0.09 | Genpact (G, Bermuda company, US-listed) |
| 30 | BKNG | Booking Holdings | Consumer Discretionary | P/E 17.1 (own 3%, x1.00 sector); EV/EBITDA 13.0 | 18% / 17% est | ROE n/m (neg. equity), ROIC 356%, ND/EBITDA 0.4, FCF/NI 1.54 | -9% / 2% / -21% | 0.66 | WATCH (below 200-day) | US-situs | no, corr 0.19 | none close |

Notes on the top 30:
- EXEL: 3-y EPS growth is from a low base (TTM EPS 0.29 three years ago); P/E 20.4, forward 16.0 (Yahoo).
- EXPE: Cheapest in its own 10-y history (P/E 15.0 vs median 32.9), but just under its 200-day average: wait for the trend.
- HRB: ROE is inflated by very small equity (buybacks); ROIC 104% says the same. Seasonal tax business.
- THC: Forward P/E 14.4 vs trailing 8.5 (Yahoo) and next-FY EPS -10% (estimate): trailing EPS may include one-off gains; check the 10-Q.
- MPC: Refiner, cyclical earnings: P/E 8.0 on current profits; next-FY EPS -13% (estimate).
- TRV: Next-FY EPS -15% (estimate).
- PGR: Next-FY EPS -12% (estimate).
- DXCM: Low own-history percentile because its P/E fell from a 10-y median of about 95: de-rating, not a bargain by itself. Same pattern for ADBE, PTC, PCTY, QLYS, ADSK, IT, NBIX, PEGA.
- DELL: AI-server maker, corr 0.40 with QCOM: adds to AI hardware risk, not a diversifier.
- NTAP: Storage hardware, corr 0.43 with QCOM; above its own median P/E.
- HON: SEC TTM EPS 15.14 vs Yahoo 20.17; Honeywell Aerospace (HONA) now listed separately; market cap check failed: verify in the 10-Q before use.
- PDD: Chinese company (Cayman): not US-situs, but China/VIE risk; reports in CNY, P/E from Yahoo; 10-y history not computed. No dividend; 0% withholding (Cayman, US). Risk: 10%/20% PRC withholding if China treats it as tax-resident (20-F; finance-tax, `tax/new-investments.md`, 17 Nov 2026).
- RNR: Bermuda: not US-situs. Overlaps Munich Re on the buy list (reinsurance). Tax: no Bermuda dividend withholding (0%, nothing to credit in India); dividends at slab 35.88%, gains 14.95% after 24 months, 35.88% before; Schedule FA A3 ([new investments](../../../tax/new-investments.md), finance-tax, 17 Nov 2026).
- ACN: Irish plc: not US-situs. Already in scout/buy-list/not-included.md (tech: research says do not add).
- GAP: P/E 6.0 vs own median 12.3, but below its 200-day average; 3-y growth from a low base.
- ANF: Price doubled in 6 months; next-FY EPS flat (estimate).
- GDDY: 3-y EPS growth not computed (no positive EPS three years earlier in XBRL); next FY +22% (estimate).
- MORN: Only 3 analysts for the forward estimate.
- MA: Above the sector median (P/E 34.9), cheap only vs its own history (21st percentile).
- BKNG: Negative equity (buybacks): ROE not meaningful, ROIC used.

## Left out of the top 30
- Held or already in the buy list (rank among survivors): QCOM (12, WATCH (chip)), NVDA (15, WATCH (chip)), MSFT (28, BUY), VRT (43, WATCH (below 200-day)), GOOG (55, WATCH (below 200-day)), GOOGL (163, WATCH (below 200-day)), IBKR (174, WATCH (below 200-day)), AVGO (176, WATCH (chip))
- Chip names, corr >= 0.3 to QCOM, not held (best 10): SNDK (score 0.76, corr 0.37), MU (score 0.71, corr 0.47), CRUS (score 0.59, corr 0.57), ASML (score 0.58, corr 0.50), TER (score 0.57, corr 0.45), MPWR (score 0.55, corr 0.53), LRCX (score 0.55, corr 0.51), NXPI (score 0.54, corr 0.62), AMAT (score 0.52, corr 0.48), KLAC (score 0.49, corr 0.49)
- Missing two or more score parts: none

## Drops
| Reason | Count | Examples |
|---|---|---|
| ROE<12% | 284 | AA, ADC, ADI, ADM, AEE, AEIS, AEP, AGCO |
| loss | 96 | AAL, ACI, ALB, ALGM, ALK, APD, APG, APO |
| net debt/EBITDA>3 | 92 | ABBV, ABT, AES, ALSN, AMT, ARMK, AXTA, BAH |
| FCF/NI<0.6 | 29 | AMZN, AN, ATI, BJ, BURL, BYD, CAVA, CEG |
| no ROE | 4 | ALNY, MSCI, NTNX, VRSN |
| no data: no EPS/NI in XBRL | 3 | HONA, SPCX, VYLR |
| no data: no SEC data | 1 | OZK |
| Kept | 409 | |

## Data errors and checks
- Prices are 16 Nov 2026 intraday. To refresh after the US close: `yf_pull.py refresh`, then `metrics.py`, `score.py`, `report.py` (the refresh joins dividend-adjusted closes at a seam; trend can move by one dividend).
- OZK (Bank OZK) has no SEC XBRL (files with the FDIC): not screened. HONA, SPCX and VYLR (new 2025-26 listings) have no usable EPS/NI history: not screened. ALNY, MSCI, NTNX, VRSN: negative equity and no ROIC: dropped as 'no ROE' (data, not quality).
- 46 filers' companyfacts stop before their latest 10-Q (mostly combined parent/subsidiary filers: utilities, REITs, also C, CLX, CEG): current EPS from Yahoo; quality from the last full years. Examples: AEE, AEP, C, CEG, D, DUK, NEE, SO.
- 17 names report EPS only per share class (or stopped tagging it): EPS history = net income / today's share count (Yahoo EPS now), so buybacks make old P/Es slightly too low. Examples: BRK-B, HSY, KKR, STZ, V, ARES, ERIE.
- 9 names have SEC TTM EPS over 25% above Yahoo (one-off items or a changed fiscal year, e.g. KMB Q3 2026 EPS 5.37 vs 1.0-2.0 in other quarters; FDX June-Sept 2026 transition period; also ASH, BTSG, IFF, MLM, OXY, PDD, VC): P/E uses Yahoo EPS. 14 the other way (e.g. HON, DD, BDX, CRWD): P/E uses SEC EPS, flagged.
- Holding-company reorganisations: XOM and BLK file under new CIKs; merged with the predecessor's XBRL history (CIK 34088, 1364742).
- Debt: 148 names use custom XBRL debt tags (e.g. CAT); net debt from Yahoo totalDebt (includes leases, so net debt/EBITDA is slightly high for them). 43 names: market cap from NI/EPS differs >25% from Yahoo (multi-class, spin-offs): their EV/EBITDA is uncertain; P/E is unaffected.
- Capex not tagged for PSX, APA, FANG: FCF/NI overstated (none in the top 30). 216 names have no operating-income tag: EBIT = pretax + interest.
- Non-USD XBRL: ASML, CCEP, FER (EUR), PDD (CNY), NBIS (old RUB): P/E from Yahoo, no own-history percentile.
- Yahoo records the FedEx Freight spin-off as a 1.241 split (2026-06-01); EPS before it is divided by 1.241 like the prices. 66 names had a one-day move over 40% in 10 years (earnings gaps, e.g. DXCM, APP). In the top 30, SEC and Yahoo EPS agree within 25% except HON (spin-off) and PDD (CNY reporter).
- 39 names have under 5 years of history (recent listings, e.g. ARM, CAVA, CEG): percentile on what exists.
- Similar non-US listings are named by hand from business descriptions, not screened.
- Yahoo calls: 10 price batches, 415 info (503 S&P 500 info re-used from the 15 Nov cache), 410 estimates; no rate-limit errors. SEC: 1,838 requests at about 3 per second.

Raw data: `~/.local/share/superpowers/finance-scout-special/us/` (all_metrics.csv, screen.csv, scripts). Generated 2026-11-16 by scout-screen-us.
