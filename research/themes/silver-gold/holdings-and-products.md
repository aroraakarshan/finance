# Silver and gold: holdings and product facts

## Summary
- Four products, Rs 8,29,676 (31.6% of AngelOne, 1.97% of total); 88% silver, gold 0.23% of total. Physical gold adds Rs 12,90,192 (3.06%). Your decision 16 Nov: all four are sold.
- Cheapest: ABSL Silver ETF 0.35%; the two FoFs cost ~0.60% and ~0.79% all-in; ICICI FoF lags its ETF ~1%/yr.
- Silver ETFs traded 9-13% above iNAV in Oct 2025 and up to 11% below NAV in Jan-Feb 2026: use limit orders near iNAV.
- Gold and gold-silver FoFs paused new money from 2026-10-16; ETFs stayed open.

Back to the index: [silver-gold](../silver-gold.md). Written 2026-11-15 by `finance-research`, updated 2026-11-15 (see "What changed"). Total-based shares as of `portfolio/summary.md` commit 0dd3a98 and later (2026-11-15; total Rs 4,20,97,035 incl. HDFC and Punjab Gramin Bank savings and FDs (PGB = estimates), EPF (locked) and physical gold; your decision 16 Nov: no extra gold (about 3.5%, band 3-6%), all silver sold; US at 13 Nov close, USD/INR 94.1997). Research only, not advice; no orders placed. "Checked" = date the source was read. "not verified" = could not confirm.

## 1. What is held (AngelOne, as of 2026-11-08, from `portfolio/summary.md`)

AngelOne = Rs 26,24,910 (6.2% of total). Total = Rs 4,20,97,035 (summary.md commit 0dd3a98 and later, 2026-11-15).

| Holding | Plan | Market value | % AngelOne | % total | Gain/loss (8 Nov) |
|---|---|---|---|---|---|
| ABSL Silver ETF (NSE: SILVER) | ETF | Rs 4,23,171 | 16.1% | 1.01% | -0.1% |
| ICICI Pru Silver ETF (NSE: SILVERIETF) | ETF | Rs 1,28,951 | 4.9% | 0.31% | -24.9% |
| ICICI Pru Silver ETF FoF | Direct-Growth (1) | Rs 1,34,114 | 5.1% | 0.32% | -10.1% |
| Motilal Oswal Gold and Silver Passive FoF | Direct-Growth (1) | Rs 1,43,440 | 5.5% | 0.34% | -3.8% |
| **Total** | | **Rs 8,29,676** | **31.6%** | **1.97%** | |

(1) Plan found by matching value/units to AMFI NAVs: ICICI FoF 1,34,114 / 4793.987 = 27.976 = Direct NAV
27.9754 on 2026-11-06 (Regular was 27.33); Motilal 1,43,440 / 5267.969 = 27.229 = Direct NAV 27.2287
(Regular 26.85). Source: https://api.mfapi.in/mf/149775 and /150642 (AMFI NAV feed), checked 2026-11-15.

Metal split (Motilal FoF held 67.9% gold ETF / 32.2% silver ETF on 2026-10-31, source in section 2 below):

| | Value | % of metals | % of AngelOne | % of total |
|---|---|---|---|---|
| Silver | ~Rs 7,32,300 | 88% | 27.9% | 1.74% |
| Gold | ~Rs 97,400 | 12% | 3.7% | 0.23% |
| Physical gold (outside AngelOne; 79.56 g 22K + 29.50 g 18K, IBJA 13 Nov, summary.md) | Rs 12,90,192 | - | - | 3.06% |
| All metals incl. physical | Rs 21,19,868 | gold 65% | - | 5.04% (gold 3.30%) |

Lots, gains and holding periods: see [tax.md](tax.md) (from the `finance-tax` note).

## 2. Product facts

| Product | TER (expense ratio) | Underlying | All-in yearly cost | Exit load | Size (AUM) |
|---|---|---|---|---|---|
| ABSL Silver ETF | 0.35% | physical silver | 0.35% | none (exchange) | Rs 2,385 Cr |
| ICICI Silver ETF | 0.40% | physical silver | 0.40% | none (exchange) | Rs 11,932 Cr |
| ICICI Silver ETF FoF, Direct | 0.20% (Regular 0.66%) | 99.87% ICICI Silver ETF (0.40%) | ~0.60% | 1% if sold within 15 days | Rs 5,184 Cr |
| Motilal Gold+Silver FoF, Direct | 0.20% (AMC, as on 2026-10-31; Groww shows 0.18%); Regular not verified | MO Gold ETF 0.59% + MO Silver ETF 0.59% | ~0.79% (estimate) | Nil | not verified |

Sources (all checked 2026-11-15):
- ABSL ETF: https://groww.in/etfs/aditya-birla-sun-life-silver-etf-962 (secondary; AMC page needs JavaScript)
- ICICI ETF: https://groww.in/etfs/icici-prudential-silver-etf (secondary)
- ICICI FoF: https://groww.in/mutual-funds/icici-prudential-silver-etf-fof-direct-growth (secondary)
- Motilal FoF: https://www.motilaloswalmf.com/mutual-funds/motilal-oswal-gold-and-silver-passive-fund-of-funds
  (TER, exit load Nil, 67.9% gold / 32.16% silver, all "as on 31 Oct 2026")
- Motilal underlying ETFs: https://groww.in/etfs/motilal-oswal-gold-etf-ltd, https://groww.in/etfs/motilal-oswal-silver-etf-ltd
- FoF cost rule: Motilal SID (29 May 2026) says the FoF expense is charged "over and above" the underlying
  scheme's expense, so all-in = FoF TER + ETF TER:
  https://www.motilaloswalmf.com/content/dam/motilal-mf/downloads/mf/sid/2026/may/SID%20-%20Motilal%20Oswal%20Gold%20and%20Silver%20ETFs%20Fund%20of%20Fund.pdf

Motilal FoF split is **not fixed**: the fund manager sets it, reviews quarterly, max 90% in either metal
(same SID). It moved from 65/35 to 68/32 gold/silver between sources. You do not control the mix.

**Tracking.** Published tracking error (Groww, period not stated): ABSL 0.73%, ICICI 0.53%, MO Silver 1.2%,
MO Gold 0.69%. AMFI tracking-difference figures: not verified (page needs JavaScript). Own check from AMFI
NAVs (2025-11-13 -> 2026-11-13, yearly return): ICICI ETF 7.90%, ABSL ETF 8.01%, ICICI FoF Direct 7.02%;
3 years: ICICI ETF 35.45%/yr, ABSL 35.39%/yr, ICICI FoF Direct 34.24%/yr. **The FoF lags its own ETF by
about 0.9-1.2% a year**, more than its 0.20% TER (cash drag and costs). Source: api.mfapi.in, checked 2026-11-15.

**ETF premium/discount and liquidity (verified).**
- Oct 2025: top silver ETFs traded 9-13% above iNAV (physical silver shortage). Livemint 2025-10-14:
  https://www.livemint.com/money/personal-finance/silver-etfs-rule-at-a-premium-to-their-indicative-nav-what-should-investors-do-silver-prices-11760428778996.html
- Kotak, UTI, SBI paused lump sums into silver FoFs (10-13 Oct 2025); ICICI paused its Silver FoF from
  2025-10-15 citing "inflated prices of Silver ETFs", resumed 2025-10-28.
  https://www.moneycontrol.com/news/business/personal-finance/sbi-uti-kotak-why-these-3-mutual-fund-houses-have-stopped-lump-sum-investments-in-silver-etf-fofs-13611672.html ;
  https://economictimes.indiatimes.com/mf/mf-news/icici-prudential-mutual-fund-becomes-fifth-fund-house-to-suspend-fresh-investments-in-silver-etf-fof/articleshow/124575762.cms
- 22 Jan 2026: some silver ETFs fell up to 24% in a day while MCX silver fell 4%:
  https://www.ndtvprofit.com/markets/silver-slumps-etfs-crash-up-to-24-as-geopolitical-risk-premium-fades-10826990
- Own check, closing price vs AMFI NAV (Yahoo + mfapi): ICICI Silver ETF closed 11.0% below NAV on
  2026-01-30 and 5.8% below on 2026-02-02; Nippon SILVERBEES 9.2% / 7.5% below. Last 3 days (11-13 Nov 2026)
  ICICI ETF was within 0.4% of NAV. Closing data only; intraday gaps were larger (Livemint above).
- From 2026-10-16 AMCs paused new money into gold and gold-silver FoFs (rupee/import pressure); silver FoFs
  and ETFs stayed open. Whether the Motilal FoF is paused: not verified (its page shows min SIP "NULL").
  https://www.livemint.com/money/personal-finance/gold-fofs-halt-fresh-investments-but-silver-mutual-funds-remain-open-experts-decode-the-reasons-and-explain-what-to-do-11792231444616.html
- Lesson: on an ETF, always use a limit order near the live iNAV (shown on the AMC/NSE page); never buy
  or sell in a panic day. A FoF always deals at NAV, so it avoids this, but costs more.
