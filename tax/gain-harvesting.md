# Gain harvesting: use the Rs 1.25 L equity exemption every year

## Summary

- Each March, redeem the long-term, load-free lots of your Indian equity funds and buy the same fund back the same day at the same NAV: up to Rs 1.25 L of gain a year becomes tax-free for good (AF s.198), worth up to Rs 18,688 a year (14.95%).
- 2026-27: worth about Rs 2,900 only (Rs 19,176 of load-free long-term gain by 25 Mar 2027 at 13 Nov NAVs). Do it only if the QCOM sale 1 (Nov-Dec 2026) happens, so this year's losses are used against QCOM; if the losses carry forward instead, skip it (it just uses up the loss).
- From 2027-28: about Rs 15,000-18,700 a year if the funds return 8% or more (about Rs 2.3 L of long-term gain by Mar 2028); about Rs 5,900 at today's NAVs. Less in years when Kotak Arbitrage redemptions already use the exemption.
- When: 20-25 Mar each year, once the year's other gains and losses are known; redeem by units, before 3 pm, and pay for the rebuy the same day from savings. Do not harvest Parag Parikh lots under 730 days old (1% load).

Written 2026-11-16 by `finance-tax` (agent `gainharvest`) for `finance-income`. Plan only: no orders; you
trade. Tax year 2026-27 = 1 Apr 2026 - 31 Mar 2027; Income-tax Act 2025 (AF), 1961 section in brackets.
Rates (new regime, income Rs 1-2 Cr, surcharge 15%, cess 4%): LT 12.5% -> 14.95%.

Sources: [Act] Income-tax Act 2025 text (GitHub abaasairam-ai/income-tax-rag, docs-text/income-tax-act-2025.txt,
read 2026-11-16): s.66(31), s.108, s.111, s.197, s.198. [ITR] AY2026-27 ITR-2 JSON schema and validation rules
(work folder copies, 2026-11-15). [Lots] `tax/FY2026-27/angelone-mf-lots.csv` (lots to 2026-11-04). [NAV] mfapi.in
and AMFI NAVAll, NAV date 13 Nov 2026 (latest on 16 Nov morning). [Load] `research/themes/mutual-fund-overlap/funds.md`
table 1 (Groww, 12-13 Nov 2026). Year plan: `tax/employer-stock/staged-sale.md` section 3 and 5.

## 1. What qualifies (AF s.198(1))

| Asset | s.198 Rs 1.25 L exemption? | Why |
|---|---|---|
| Indian listed shares bought and sold on an Indian exchange | Yes | equity share, STT paid on buy and sale (s.198(1)(c)(i)) |
| Indian equity-oriented MF units (UTI Nifty 50, Parag Parikh, HDFC Mid Cap, Quant Small Cap, Kotak NN50, Kotak Arbitrage) | Yes | Schedule VII fund with 65%+ in Indian listed equity (s.198(8)(ii)); STT on redemption |
| REIT / InvIT units (business trusts) | Yes | s.198(1)(b), STT on sale |
| QCOM, MSFT, NXPI, other foreign shares and Irish ETFs | No - s.197, 12.5% on all of it | no STT; not "equity share" with STT paid |
| Gold/silver ETFs and FoFs, debt funds | No | not equity-oriented (s.198(8)) |

The exemption is "income-tax ... on such long-term capital gains exceeding Rs. 125000" (s.198(2)(a)): one
Rs 1.25 L a year for all s.198 gains together, unused part lost (no carry-forward of the exemption).

## 2. Do losses eat the exemption? (AF s.108, s.111)

| Question | Answer | Text |
|---|---|---|
| Must a current-year ST loss be set off? | Yes, against any capital gain of the year | s.108(2)(a): "such loss shall be set off against the income, computed in respect of any other capital asset" |
| Can you keep the loss for later while s.198 gains sit inside the Rs 1.25 L? | No | s.111(1)(a) carries forward only loss that "cannot be wholly set off ... as per section 108" |
| Is the exemption applied before or after set-off? | After: s.198 taxes the LTCG left in total income | s.198(2)(a), (b) work on the total income, which is after set-off |
| Order among gains (s.197 NXPI/QCOM vs s.198 MF)? | Act is silent: no fixed order | s.108(2) names no order; `ca-questions.md` row "Order of set-off" |
| What the ITR lets you do | AY2026-27 ITR-2 Schedule CG table E has ONE column "LTCG 12.5%" for s.112 and s.112A gains together (schema `InLtcg12_5Per`); there is no "112A after set-off" field, so the utility, not you, splits the set-off | [ITR] schema; validation rules 555, 566 |

So: a loss eats the exemption only when there is not enough s.197 (or ST) gain to absorb it. With s.197
gains much larger than the losses (QCOM, section 3), the loss should fall on s.197 gains. After filling the
return, check Schedule SI: the 112A line should show the full s.198 gain with tax only above Rs 1.25 L. If
the utility puts loss on the 112A gains first, that is a discrepancy to raise (the Act allows either order).

## 3. 2026-27: harvest or not?

| Item (approx INR) | Amount | Source |
|---|---|---|
| s.197 LT gain: NXPI | +2,76,457 | `angelone-metals-and-mf-exits.md` section 2 |
| s.197 LT gain: QCOM sale 1 + MSFT Jan lot (planned Nov 2026 - Jan 2027) | about +24.39 L | `employer-stock/staged-sale.md` section 3 |
| Net ST loss: INDmoney to 9 Nov, silver, MF exits, INDmoney 16-25 Nov sales (planned) | about -3.4 L to -3.6 L | metals note sections 2 and 6, migration note section 3 |
| s.198 gains: the 7 MF exits | +20,644 | metals note section 4 |
| Exemption left for harvesting | about Rs 1,04,356 | 1,25,000 - 20,644 |

| Case | Effect of harvesting extra s.198 gain G | Verdict |
|---|---|---|
| A. QCOM sale 1 done this year (plan) | all losses meet s.197 gains; G up to Rs 1.04 L is tax-free now and raises the cost basis | harvest the load-free LT lots: G about Rs 19,176 -> Rs 2,867 saved later |
| B. QCOM sale moved to 2027-28 (losses carry forward) | G eats the carried loss rupee for rupee (s.108, s.111); both are worth 14.95% later, and the loss is more flexible (can meet ST gains at 35.88%, any gain) | skip; start in 2027-28 |

## 4. Long-term gains available (kept funds; NAV 13 Nov 2026; cost incl. stamp duty)

| Fund (lots held) | LT gain now | Load-free LT gain by 25 Mar 2027 | LT gain by 24 Mar 2028, today's NAV | Exit load | Note |
|---|---|---|---|---|---|
| HDFC Mid Cap (50, from 2024-08-05) | 10,843 | 12,234 | 15,657 | 1% within 1 year | LT lots are load-free; 2026-08/09 lots small losses |
| Quant Small Cap (15, 2024-08-05 to 2025-11-03) | 4,322 | 4,322 | 4,322 | 1% within 1 year | all lots LT by 4 Nov 2026 |
| Parag Parikh Flexi Cap (20, from 2025-03-10) | 6,656 | 2,620 (2025-03-10 lot only) | 11,889 (load-free part less) | 2% within 365 d, 1% 366-730 d, on units above 10% per lot | harvest only lots over 730 days: 1% load (about Rs 1,840 on the other LT lots) beats the Rs 631 tax value |
| UTI Nifty 50 (1: 2026-09-23) | 0 (ST +11,843) | 0 | 11,843 | nil | LT from 24 Sep 2027; new SIP/top-up lots later |
| Kotak Nifty Next 50 (1: 2026-09-23) | 0 (ST +963) | 0 | 963 | nil | LT from 24 Sep 2027 |
| Kotak Arbitrage (1: 2026-09-23) | 0 (ST +2,492) | 0 | 2,492 | 0.25% within 30 days | moves to UTI after 24 Sep 2027 are s.198 gains that use the exemption anyway |
| **Total** | **21,821** | **19,176** | **47,167** (39,628 load-free) | | |

With new money (Dec 2026 top-ups about Rs 5.32 L, SIPs Rs 60,000/month, Rs 32,400/month arbitrage -> UTI)
the long-term gain by 24 Mar 2028 (load-free, excl. Kotak Arbitrage) is about Rs 39,600 at 0% return,
Rs 2,26,500 at 8% a year, Rs 3,21,600 at 12% (model on the lot CSV, 2026-11-16).
AngelOne shares: 12 small holdings (ICICIGI, SUZLON, ASTRAL ...; `portfolio/details.md`), about Rs 40,000
value and about +Rs 12,000 gain (account total less the silver ETFs, approx). Lot dates are not on file (the
holdings export is password-protected); a share harvest saves at most about Rs 1,800 and costs STT 0.1% each
side plus DP charges per scrip: optional.

## 5. Costs and mechanics

| Item | Mutual funds | Shares / ETFs / REITs |
|---|---|---|
| Same-day rebuy | Yes: redeem and buy before the 3 pm cut-off; both get that day's NAV if the purchase money reaches the AMC the same day (pay from savings; proceeds arrive T+2) | No: a same-day sell and buy of the same scrip nets at the exchange, is not "settled by actual delivery" and is speculative (AF s.66(31)): the cost does not reset. Sell today, buy next trading day (1 day of price risk) |
| Exit load | nil on LT lots of HDFC, Quant, UTI, Kotak; Parag Parikh 1% up to 730 days | none |
| STT | 0.001% on redemption (Rs 2 on Rs 2 L) | 0.1% on sell and buy (delivery) |
| Stamp duty | 0.005% on the purchase (Rs 10 on Rs 2 L) | 0.015% on the buy |
| New lot | restarts the 12-month clock: next harvest must be more than 12 months after this rebuy | same |
| FIFO | redemption takes oldest units first (s.67(7)(c)); redeem by units, exactly the LT load-free units | same |
| Grandfathering (31 Jan 2018 value) | not relevant: all lots bought after 2018 | same |
| Abuse rules | GAAR not applicable under Rs 3 Cr benefit (Rules r.128(1)(a)); no dividend/bonus date involved (s.175); see `loss-harvesting.md` section 2 | same |
| Market risk | none for funds (same NAV) | one day for shares |

## 6. Rs per year

| Year | Harvestable (load-free LT) | Exemption left | Saving = 14.95% x min | When |
|---|---|---|---|---|
| 2026-27, case A | about 19,176 (13 Nov NAV) | about 1,04,356 | **about Rs 2,867** | 20-25 Mar 2027 |
| 2026-27, case B | - | - | **0 (skip)** | - |
| 2027-28 | 39,600 (0% return) to 2.27 L (8%) | 1.25 L less Kotak Arbitrage LT redemptions (about Rs 20,000-30,000) | **about Rs 5,900 to Rs 15,000-18,700** | 20-25 Mar 2028, after the 2027 harvest's anniversary |
| Later years | grows with SIPs | 0 if arbitrage redemptions of FD money (from May 2028) alone pass Rs 1.25 L | up to Rs 18,688 | each March |

The saving is real only if you would one day sell these funds with gains above each year's exemption; with
Rs 7.2 L a year of SIPs that is likely. The claimed "Rs 15,600" is 12.5% + cess; at your 15% surcharge it is
Rs 18,688 (14.95%).

## 7. Steps each March (you trade)

1. By 15 Mar: list the year's capital gains and losses (all brokers) and other s.198 gains (fund exits, Kotak Arbitrage moves).
2. Room = Rs 1,25,000 - other s.198 gains; skip if losses would carry forward (case B).
3. In AngelOne, per fund, find the LT units with no load (HDFC/Quant/UTI/Kotak: bought more than 12 months ago; Parag Parikh: more than 730 days ago), up to the room.
4. 20-25 Mar, before 3 pm: redeem those units; buy the same rupee amount of the same fund (Direct Growth) from savings the same day.
5. Keep the redemption statement; the rebuy is a new lot (date and cost) for the lot CSV.

## 8. Discrepancies found

| Item | Where | Action |
|---|---|---|
| Losses "carry forward about Rs 27,300-47,000" vs losses absorbed by the QCOM LT gain | `angelone-metals-and-mf-exits.md` summary and section 6, `loss-harvesting.md`, `migration-indmoney-to-ibkr.md` vs `employer-stock/staged-sale.md` section 5 | the carry-forward holds only if QCOM sale 1 slips past 31 Mar 2027; `finance-tax` to align the notes |
| "You fill the set-off table" | `ca-questions.md` row "Order of set-off" | AY2026-27 ITR-2 has one LTCG 12.5% column for s.112 and s.112A; the order between them is the utility's; check Schedule SI after filling |
| Metals note section 6 "12,736 lost to set-off" against exempt MF LTCG | `angelone-metals-and-mf-exits.md` | does not happen if QCOM gains exist the same year (case A) |
| `details.md` cites an "Open Holdings" sheet in the TaxPnL file | `portfolio/details.md` line 102 | the 15 Nov TaxPnL file has no such sheet (Summary, trade details, charges, dividends); `finance` to fix the source line |
