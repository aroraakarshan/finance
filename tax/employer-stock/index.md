# Employer stock (QCOM, MSFT): staged sales and the Microsoft ESPP

## Summary

- User decision 17 Nov 2026: for foreign shares at foreign brokers report the actual lot sold (specific identification); FIFO is the fallback if the officer disagrees. Risk: an adverse 2026 ITAT ruling (Megasolis); if FIFO were imposed, about Rs 1.01 L more tax on QCOM plus interest and a possible 50% penalty. Keep broker lot records and the FIFO figure ([qcom-lots.md](qcom-lots.md) 3.3).
- QCOM: sell the long-term lots with the highest Indian cost first, matched with Specific Lot at IBKR on each sale day ([qcom-lots.md](qcom-lots.md) 3.4-3.5). Sale 1 (432 sh) tax about Rs 2,26,800 before losses, about Rs 2,06,500 after; sale 2 (195 sh, Apr 2027) about Rs 1,57,700.
- Advance tax: about Rs 1,50,200 by 15 Dec 2026 and Rs 1,90,200 by 15 Mar 2027 (after the AngelOne sales of 18 Nov); sell QCOM part 4 on 16-18 Dec. Rs 2 Cr stays far (about Rs 70 L of room) ([staged-sale.md](staged-sale.md) 5).
- MSFT: sell each new vest at once choosing that lot (Fidelity Specific Shares): the 17 Nov sale of 10.9 sh of the 15 Nov vest is a small ST loss (about Rs 18,155, tax 0, provisional until the fill price); older lots as each turns long-term ([staged-sale.md](staged-sale.md) 3.6).
- ESPP: sell each purchase the same day choosing that lot: about 7.1% net after payroll tax ([espp.md](espp.md)); report the shares in Schedule FA.

Written 2026-11-15 by `finance-tax`; lot choice decided 2026-11-15 without a CA (user has none). Plan
only; no orders; the user decides and trades. Sections: 2025 Act (AF) and Income-tax Rules 2026 (r.),
1961 Act in brackets. Lot data: work note `empstock.md` (2026-11-15), method A (Indian cost = FMV taxed
at vest/purchase, QCOM $141.86/sh); INR at SBI TT buying rates ([staged-sale.md](staged-sale.md) section 4). Supersedes
`tax/investment-types.md` section 5.

## Parts

| Part | Sections | What |
|---|---|---|
| [qcom-lots.md](qcom-lots.md) | 3.1-3.5 | QCOM lots (761 sh), lot methods vs FIFO, the law and the decision, lots per sale part, IBKR steps |
| [staged-sale.md](staged-sale.md) | 2, 3.6, 4, 5 | Rs 2 Cr step, MSFT long-term dates, rupee rate, losses and advance tax 2026-27 |
| [espp.md](espp.md) | 6 | Microsoft ESPP restart: perquisite, TDS, LRS/TCS, Schedule FA, US tax |
| this page | 1, 7 | Inputs, open points, sources |

## 1. Inputs

| Item | Value | Source, date |
|---|---|---|
| QCOM | 761 sh at IBKR, $172.47 = $131,250 | `ibkr.holdings()` run 2026-11-15; yfinance close 2026-11-13 (last US close) |
| MSFT | 116.888 sh at Fidelity (3 ESPP + 9 RSU lots), $523.88 = $61,235 | `fidelity.holdings()` run 2026-11-15; yfinance close 2026-11-13. Vests of 15/30 Nov 2026 not yet in data |
| USD/INR | QCOM: SBI TT buying, 94.36 (31 Oct 2026) and 93.80 (13 Nov 2026, latest, for 30 Nov 2026 and 31 Mar 2027). MSFT and ESPP: 94.03 | SBI rates archive ([staged-sale.md](staged-sale.md) section 4); yfinance INR=X close 2026-11-13 |
| Income 2026-27 before these sales | Salary Rs 1,05,79,048 + other income about Rs 7,64,000 (FD, PGB FD, savings interest, US dividends) = about Rs 1.13 Cr | `empstock.md` 0.1; `tax/FY2026-27/fd-and-advance-tax.md` section 5 |
| Rates (new regime, 15% surcharge, 4% cess) | LT 12.5% -> 14.95%; slab 30% -> 35.88% | Surcharge bands are in the Finance Act 2026 schedule, not read (CA) |

## 7. Open points and discrepancies

| # | Item | Action |
|---|---|---|
| 1 | Lot choice: specific identification, highest-cost long-term lots first (user decision 17 Nov 2026; FIFO fallback; FIFO decision of 15 Nov replaced; 3.3). Method A vs B (sell-to-cover matching) kept as A. Surcharge rates (Finance Act 2026 not read) | `finance-tax`: recheck if a ruling on foreign-broker lots appears; follow any appeal of Megasolis |
| 2 | `empstock.md` headroom "about Rs 93 L" left out about Rs 7.6 L of other income: about Rs 86.6 L | corrected here |
| 3 | Sale rate: earlier 95.15 (yfinance 30 Oct) and 94.03 (13 Nov); SBI TT buying for 31 Oct 2026 is 94.36. INR cost now SBI TT on the acquisition date: total Rs 84.84 L vs Rs 85.27 L with yfinance (`empstock.md`); all-QCOM gain Rs 38.38 L (was LT 37.87 L + ST 0.28 L) | corrected here; refresh P2-P4 and sale 2 with the 30 Nov 2026 / 31 Mar 2027 SBI rates |
| 4 | Earlier tranches T1 242 / T2 190 / T3 195 replaced by the plan's 432 (4 x 108) + 195; research plan tranche 1 lot list (196 sh) no longer used | `finance-research` to align with 3.4 |
| 5 | `employer-stock-concentration/plan.md` and `employer-stock-decision.md` / `qcom-msft.md` point to `tax/investment-types.md` section 5, now moved here | `finance-research` to relink |
| 6 | Payroll FX rate and FMV rule for the ESPP perquisite; TCS on ESPP remittances | check payslip, Form 16, AIS |
| 7 | 2027-28 income (bonus, RSU) unknown; Rs 2 Cr check redone in Apr 2027 | `finance-tax` |
| 8 | CIT v. Bai Shirinbai K. Kooka (SC, 23 Feb 1962) read 2026-11-17: about the cost of investment shares converted to stock-in-trade (majority: market value on conversion); nothing on FIFO or lot identification | cited in 3.3 as not deciding the point |
| 9 | Advance-tax base was Rs 1,65,100; `tax/FY2026-27/fd-and-advance-tax.md` now plans Rs 2,84,600 (15 Dec pay Rs 63,500, 15 Mar Rs 71,200) | section 5 uses the new base |
| 10 | `portfolio/plan.md` says "after your CA confirms which shares to sell" and taxes Rs 2.54 L / Rs 1.68 L | `finance-main`: no CA; specific identification with Specific Lot at IBKR (3.4-3.5); Rs 2.27 L / Rs 1.58 L at 16 Nov inputs |
| 11 | IBKR's lot-level records (dates per release) not yet seen; $312 gap between IBKR cost and method A (`empstock.md` 1.3) | user: 3.5 step 1 before P1 |
| 12 | 15 Nov 2026 MSFT vest (Fidelity lot date 16 Nov, cost $523.88): 10.9 sh sold 17 Nov, proceeds about $5,484 provisional; loss uses 93.80 (13 Nov) | update from the release confirmation and payslip; record the actual sale fill |

## Sources

Act and Rules text: GitHub abaasairam-ai/income-tax-rag `docs-text/income-tax-act-2025.txt` (as
amended by Finance Act 2026) and `income-tax-rules-2026.txt` (official PDF of 22 Jun 2026), read
2026-11-15: s.17, 67, 73, 392, 394, 404, 408, 424, 425, 439; r.15(6), 204, 206, 207. RBI Master Direction -
Overseas Investment (Directions 2022, rbi.org.in id 12381), fetched 2026-11-15. Prices and FX:
yfinance, 2026-11-13 closes; SBI TT buying rates: GitHub sahilgupta/sbi-fx-ratekeeper
`csv_files/SBI_REFERENCE_RATES_USD.csv` (fetched 2026-11-15, to 2026-11-13). Lots: `empstock.md` (2026-11-15)
and `etrade.acquisitions()` (run 2026-11-15). Rulings: Indian Kanoon docs 4842525 (Megasolis, ITAT Mumbai
2026-05-05) and 51561346 (Prannoy Roy, ITAT Delhi 2019-06-14), read 2026-11-15. IBKR guides linked in 3.5,
read 2026-11-15.
