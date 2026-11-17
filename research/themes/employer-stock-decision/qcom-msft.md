# QCOM and MSFT: keep or sell, how much, when

## Summary
QCOM is fairly priced against its closest peer, but its base case for the next 2 years is about flat, against roughly +6-7% a year for a world ETF. Proposal: keep about 5% of the Rs 4.21 Cr total (134 shares) and sell the rest in two steps, about 430 shares in Nov-Dec 2026 and 195 in Apr 2027.
MSFT has better prospects, but your job and 238 unvested shares already tie you to Microsoft. Proposal: sell each held lot on its long-term date (the first on 2027-01-01), down to about 0% held by Sep 2028, and sell new vests at once.
Tax on all QCOM is about Rs 5.66 L (14.95%) in either year, much less than the bear case (-33%). Switching inside IBKR (sell QCOM, buy UCITS in USD) needs no currency conversion.
This is a proposal; you decide and place the trades.

Written 2026-11-15 by `finance-research`; research only, not advice. Index: `employer-stock-decision/` (written by finance-main).
Prices: 2026-11-13 close (QCOM $172.47, MSFT $523.88), USD/INR 94.0338 for the analysis; total Rs 4,20,97,035 at USD/INR 94.1997 (FBIL) incl. Punjab Gramin Bank
estimates and EPF (`portfolio/summary.md`, 2026-11-15, version of 2026-11-15 and later; was Rs 2,97,58,520 when first written).

## 1. Valuation (USD; yfinance, fetched 2026-11-15; LTM = last 4 quarters)

Comps (method: equity-analysis skill `references/comps.md`). Fwd P/E = Yahoo `forwardPE` (next fiscal year +1).

| Company | Mkt cap $bn | EBITDA margin | ROE | EV/EBITDA | P/E LTM | Fwd P/E | FCF yield |
|---|---|---|---|---|---|---|---|
| **QCOM** | 185 | 27.2% | 44.8% | 16.4 | 13.5 (NM: one-off tax gain) | 14.1 | 4.7% |
| AVGO | 1,656 | 58.8% | 38.4% | 32.3 | 43.3 | 17.9 | 2.4% |
| TXN | 277 | 52.8% | 36.9% | 25.8 | 39.2 | 26.1 | 2.6% |
| NXPI | 67 | 39.0% | 26.7% | 13.9 | 20.7 | 14.4 | 5.0% |
| ADI | 193 | 50.6% | 12.3% | 28.4 | 46.6 | 24.1 | 2.6% |
| MediaTek (2454.TW, TWD statements) | 200 | 23.1% | 22.8% | 46.9 | 68.1 | 26.6 | 1.2% |
| Peer median (25th-75th) | | | | 28.4 (25.8-32.3) | | 24.1 (17.9-26.1) | |
| **MSFT** | 3,890 | 64.4% | 30.3% | 17.4 | 27.3 | 21.7 | 1.5% |
| GOOGL | 3,636 | 67.7% | 34.7% | 11.0 | 15.5 (one-off gains) | 19.2 | 0.5% |
| AMZN | 2,883 | 23.1% | 12.7% | 18.4 | 37.1 | 24.4 | 0.3% |
| ORCL | 391 | 52.6% | 28.1% | 13.5 | 20.9 | 11.3 | NM (negative FCF) |
| CRM | 179 | 37.8% | 25.2% | 12.6 | 18.6 | 13.6 | 8.5% |
| ADBE | 95 | 39.7% | 61.9% | 9.3 | 13.0 | 8.9 | 11.2% |
| Peer median (25th-75th) | | | | 12.6 (11.0-13.5) | | 13.6 (11.3-19.2) | |

Revenue growth column left out: the quarterly history was too short to compute it. Percentiles of 5 peers are rough.

DCF (equity-analysis `scripts/dcf.py`, run 2026-11-15). Inputs: risk-free 5.15% (^TNX, 2026-11-13); equity risk premium
4.46% (US, Damodaran ctryprem page, updated 2026-01-05); beta from 5-year weekly returns, Blume-adjusted; mid-year discounting.

| | QCOM | MSFT |
|---|---|---|
| Growth path | FY27 +5.3%, FY28 +15.5% (consensus), then 5%, 3.5%, 3% | FY27 +19.3%, FY28 +20.5% (consensus), then 15%, 11%, 8%, 6%, 4% |
| EBIT margin, tax | 25% (FY24-26: 25.8%, 27.9%, 20.1%); tax 15% (history distorted by one-offs) | 46% (FY26 46.8%); tax 18.4% |
| Reinvestment | capex 3.7%, D&A 3.9%, NWC 16.6% of revenue | capex 20% (FY26 34.9%, assumed to fall), D&A 13% |
| WACC, terminal g | 10.62% (beta 1.35), 2.5% | 9.96% (beta 1.09), 3.0% |
| Base value / share | **$125** (terminal value 70% of EV) | **$355** (terminal value 67%) |
| Grid (WACC +/-1%, g +/-0.5%) | $106-152 | $298-443 |
| Bull flex | $178 (margin 28%, beta 1.1, g 3%) | $587 (margin 48%, capex 15%, beta 0.9, g 3.5%) |
| Exit at today's EV/EBITDA | 14x: $167 | 17.4x: $637 |
| Reading | The price ($172) needs the bull case: data-center and auto growth with margins back near 28% | The price ($524) needs a long AI runway or a lower discount rate; analysts' mean target is $636 |

- **QCOM:** about 41% cheaper than its peers on forward P/E (14.1 vs 24.1), but in line with NXPI, its closest peer (auto and IoT,
  14.4). Its margins are about half those of the AI and analog chip makers, so the discount is earned. Fair range about $125-218
  (DCF base to the 25th-percentile peer P/E x FY28 EPS $12.21).
- **MSFT:** dearer than its peers (EV/EBITDA 17.4 vs 12.6), which is justified by about 19% growth and a 64% EBITDA margin. The
  software peers trade lower on worry that AI tools will replace their products. The DCF base of $355 is below the price.

## 2. Two-year returns (to Nov 2028; price = EPS x P/E + dividends; own assumptions)

| Case | QCOM | MSFT | World ETF (VWRA/EXUS type) |
|---|---|---|---|
| Bull | FY29 EPS $12.8 x 17.9 + $7.4 dividends = $236: **+37%** (17%/yr). Data center reaches $5B, auto keeps growing | NTM EPS $29.2 x 25 + $7.8 = $738: **+41%** (19%/yr). Azure keeps growing 40%+ | about +30% (14%/yr) |
| Base | EPS $11.5 x 14 + $7.4 = $168: **-2%** (-1%/yr). Apple modem loss offsets the growth | EPS $27.8 (FY28 $24.19 consensus +15%) x 21.7 + $7.8 = $611: **+17%** (8%/yr) | **+13% (6-7%/yr)**: Vanguard 10y dev. ex-US 5.3-7.3%, US 4.8-6.8%; J.P. Morgan global 7.5%; BlackRock world ex-US 7.5-7.8% |
| Bear | EPS $9.0 (FY27 level) x 12 + $7.4 = $115: **-33%** | EPS $22 x 16 + $7.8 = $360: **-31%**. AI capex does not pay back, multiple drops toward peers | about -22% (URTH worst 1-year in 10 years, -22.1%) |
| Volatility, 10y | 40.4% | 27.9% | 17.3% (URTH) |

Sources for the forecasts: `research/themes/opp-global-regions/outlook-risks.md` section 4 (Vanguard VCMM 2026-10-21, J.P. Morgan
LTCMA 2027 2026-10-19, BlackRock CMA Aug 2026; GMO and AQR are lower for the US, e.g. GMO US large -7.3% real). Volatility:
`../employer-stock-concentration/risk.md`. In rupees, add the rupee's fall to all three columns (4.8%/yr over the last 5 years, not a forecast).
A single stock's bear case can be lasting: about 40% of Russell 3000 stocks fell 70%+ and never recovered (J.P. Morgan 2014, risk.md).

## 3. News and analyst mood (`news/QCOM.md`, `news/MSFT.md`, both 2026-11-15)

| | QCOM: score -1 | MSFT: score +1 |
|---|---|---|
| Last results | Q4 FY26 (to 2026-09-27) beat by 1 cent; Q1 FY27 guide below consensus; handsets -26%; stock -9.5% on 11-05 | FQ1 FY27 beat; Azure +48%; commercial RPO +73% to $677B; FQ2 guide above consensus |
| Analysts | 8 of 10 actions since 10-21 cut targets; mean target $186, median $175; consensus "hold" (2.6) | 15 of 17 raised targets; mean $636, median $631; "strong buy" (1.4) |
| Positives | Auto +89% to $1.99B; $5B FY27 data-center target; Alphabet $548M stake | AI cloud demand; buyout offer to about 60,000 staff to cut costs |
| Risks | Apple's own modems; margin squeeze until 2H FY27; $4B of new debt | Anthropic office tools (-2.3% on 11-11); outage 11-12/13; CFO and CMO sales |
| Next events | Ex-dividend 2026-12-03 ($0.92); results about 2027-02-03 (Yahoo date, not confirmed) | Ex-dividend 2026-11-19 ($0.98); results 2027-01-27 (not confirmed) |

## 4. Tax cost of each path (`tax/employer-stock.md`; lot table `../employer-stock-concentration/lots-and-tax.md`)

Rates: long-term after 24 months + 1 day at 14.95% all-in, short-term at 35.88%. Lots: finance-tax "method A" (net shares per
release), highest Indian cost first; prices 13 Nov 2026.

| Path | Rupee gain | Tax | Note |
|---|---|---|---|
| Sell all QCOM (now or later) | Rs 37.87 L (746.845 LT shares) | **Rs 5.66 L** (Rs 5,66,142) | Same total in either FY; staging only moves it between years |
| Proposed QCOM step A (432 sh, Nov-Dec 2026) | Rs 16.99 L | **Rs 2.54 L** (Rs 3.51 L if FIFO; CA to confirm lot choice) | FY2026-27. Sold by 15 Dec: about Rs 1.59 L more advance tax by 15 Dec and Rs 1.14 L by 15 Mar; after 15 Dec: all by 15 Mar |
| Proposed QCOM step B (195 sh, Apr 2027) | Rs 11.27 L | Rs 1.68 L | FY2027-28 |
| Keep 134 QCOM | Rs 9.89 L not realised | about Rs 1.48 L deferred | Lowest Indian cost lots, plus DRIP lots that are still short-term |
| Hold QCOM | 0 now | 0 now | Same rate later; the rupee effect below |
| Sell all MSFT now (short-term) | Rs 7.45 L | Rs 2.67 L | 35.88% |
| MSFT on long-term dates | same gain | Rs 1.11 L | Saves about **Rs 1.56 L**; a 2.7% MSFT fall wipes that out |
| New MSFT vests sold at once | about 0 | about 0 | Indian cost = value at vest |

- **Staging across FY2026-27 and FY2027-28** only delays the tax: both years pay the same rate, and foreign shares get no yearly
  exemption. Delaying step B's Rs 1.68 L of tax by about 9 months is worth about Rs 8,000 at the 6.25% FD rate. The
  base-case return gap between QCOM and a world ETF (about 8%/yr on $33k for 5 months) is worth about Rs 1 L. Speed matters more
  than staging. Rs 2 Cr surcharge step: about Rs 86.6 L of extra gains still fit in 2026-27, so it does not bind.
- **Rupee effect:** each Rs 1 rise in USD/INR adds about Rs 19,600 of tax on all 761 QCOM (14.95% x $131,250;
  `tax/global-actions-2026-11.md` row 12), and about Rs 9,155 on MSFT once long-term. The same Rs 1 adds about Rs 1.9 L to the
  value of QCOM + MSFT, so the rupee is no reason to wait or to hurry.
- Lot choice vs FIFO and method A vs B: CA question; set "Specific Lot" at IBKR before the order and keep the lot report
  (`tax/employer-stock.md`; `tax/global-actions-2026-11.md` row 15).

## 5. Cost of moving the money

| Route | Cost | Time | Notes |
|---|---|---|---|
| Inside IBKR: sell QCOM, buy a UCITS ETF in USD (e.g. EXUS, LSE, USD, TER 0.15%; VWRA, TER 0.14%) | Commission only (IBKR stock commission not checked); **no FX** | Same day; T+1 settlement in the US (not checked here) | `opp-global-regions/instruments-tax.md`. No US estate tax on UCITS ETFs; no Indian tax until sale (accumulating fund) |
| MSFT from Fidelity to IBKR by ACATS/DTC | IBKR: no fee for incoming or outgoing ACATS (IBKR other-fees page, checked 2026-11-15). Fidelity's fee for moving shares out: not verified (pages 403). Plan shares may first need to move to a Fidelity brokerage account (not verified) | QCOM's ETrade -> IBKR ACATS in Dec 2025 took days (`STATUS.md`) | Not a sale: no tax, and cost and dates carry over (`tax/migration-indmoney-to-ibkr.md` item 1). After the move you can choose lots at IBKR |
| Sell at Fidelity, wire USD to IBKR | Fidelity wire fee: not verified. IBKR deposit fee: not checked | 1-2 days (not verified) | Simple for new vests |
| Sell at Fidelity, send to India | Fidelity wire fee not verified; the Indian bank's FX spread was not checked (each 0.5% on $61k is about Rs 28,800) | Not verified | Only if you need rupees. Sale money kept abroad must be reinvested or brought home within 180 days (RBI LRS FAQ Q4; `../employer-stock-concentration/proceeds.md`) |
| IBKR withdrawal to India | Two free withdrawals a month, then USD 10 per wire (IBKR other-fees page, 2026-11-15) | - | Plus the Indian bank's FX spread |

## 6. Answer: how much to keep (% of Rs 4,20,97,035)

| Stock | Keep | Value kept | Why | When to sell the rest |
|---|---|---|---|---|
| QCOM | **about 5% (134 shares; was ~7% of the Rs 2.98 Cr total)**: method A lots 2020-08-20 (40.845), 2023-05-20 (43), 2020-07-31 (29), 2019-08-19 (7) and the DRIP lots | about Rs 21.8 L ($23.1k) | Fairly priced and no longer your employer, but the base case (-1%/yr) is below a world ETF (6-7%/yr) with more than twice the volatility. The lots kept have the lowest Indian cost, so keeping them defers about Rs 1.48 L of tax | **Step A, Nov-Dec 2026:** the 432 shares of old tranches 1 and 2, before the results around 2027-02-03 (tax Rs 2.54 L). **Step B, Apr 2027:** 195 shares (rest of 2022-05-20, 2023-11-20, 2022-11-20; tax Rs 1.68 L). Leave the DRIP shares until they turn long-term |
| MSFT (vested) | **about 0% by Sep 2028**; 13.7% now, 6.1% after 2027-08-16, 4.7% after 2027-11-18 | - | Better outlook than QCOM, but your salary and 238 unvested shares (about Rs 1.17 Cr gross, `../employer-stock-concentration/concentration.md`) already tie you to Microsoft | Each lot on its long-term date (first 2027-01-01, the 48.8-share lot on 2027-08-16, the last 2028-09-01). New vests and ESPP shares sold at once. Sell earlier if you value lower risk over about Rs 1.56 L of tax |

Where the money goes: inside IBKR into Irish UCITS ETFs (EXUS for non-US developed markets, or VWRA for the whole world). MSFT
sale money goes from Fidelity to IBKR by wire; or move the held lots once by ACATS, after checking Fidelity's fee.
Microsoft trading-window rules for employees were not checked.

## 7. What changes in the existing plan (`../employer-stock-concentration/plan.md`)

| Item | Old plan | Now |
|---|---|---|
| QCOM tranche 2 (190 sh) | Apr 2027 | Moved into Nov-Dec 2026 with tranche 1 (step A, 432 sh). Waiting a year only defers tax; the return gap is bigger |
| QCOM tranche 3 (195 sh) | Oct 2027 | Moved to Apr 2027 (step B) |
| QCOM end state | 134 sh, flagged as "oversells the 10% target" | Same 134 sh, now the intended level (~7% of Rs 2.98 Cr; ~5.2% of Rs 4.21 Cr) |
| Tranche-1 lot list | 6 dates said to be 242 sh (true in the FIFO table; 196 sh under method A) | Method A lots from `tax/employer-stock.md` in `../employer-stock-concentration/plan.md` |
| MSFT | Lots sold on long-term dates until Nov 2027 (40.2 sh left, 6.7% of Rs 2.98 Cr) | Same dates, and continue with the later lots until about 0 vested shares (Sep 2028) |
| New vests, lot order, proceeds | Sell at vest; highest-cost lots first; UCITS at IBKR | Unchanged |

Re-base 2026-11-15 to Rs 4.21 Cr (Punjab Gramin Bank Rs 82 L estimate, EPF Rs 41 L): QCOM is now 29.4% and MSFT 13.7%;
the 10% cap is about Rs 42.1 L (about 259 QCOM shares). The 134-share keep (about 5.2%) and both QCOM steps stay as
decided: they rest on QCOM's weak base case against a world ETF (sections 2 and 6), not on the cap. No conclusion changes.
