## Summary
- Yes: restart the Microsoft ESPP at 15% (the plan maximum) and sell every purchase as soon as the shares post.
- Net after Indian tax: about Rs 6,570 per Rs 1 L contributed (6.6% per purchase), about Rs 64,000 a year at 15% of
  current base pay, before any Fidelity wire fee (Rs 55,000 if each quarterly wire costs $25, fee not verified).
- Keep the USD and send it to IBKR for the UCITS plan; payroll turns rupees into dollars at about market rate, cheaper than a bank wire (about 2%).
- Bringing it to India costs about 1-2% more in bank FX (estimate); never hold the shares (MSFT concentration, ST tax).

Written 2026-11-15 by `finance-research`; research only, not advice; no orders placed. "not verified" = could
not confirm from a source. Tax lines: see finance-tax; the tax numbers here are my own computation.

## 1. Plan facts

| Fact | Value | Source (date) |
|---|---|---|
| Discount | Buy at 90% of the market value on the last Nasdaq trading day of each offering (10% off the end price) | ESPP plan s.5, DEF 14A Annex A (filed 2021-10-14, plan effective 2022-01-01, listed as exhibit 10.4 in the 10-K filed 2026-07-29) |
| Look-back | None: price is set only on the last day, so there is no gain or loss from the price moving during the offering | Plan s.5; own data: paid exactly 90% of FMV in all 3 purchases (table below) |
| Frequency | Quarterly offerings starting 1 Jan, 1 Apr, 1 Jul, 1 Oct; last offering ends 2031-12-31 | Plan s.4; 10-K FY2026 note "Employee Stock Purchase Plan" (filed 2026-07-29) |
| Contribution | Payroll only, 1% to 15% of Compensation; at most 2,000 shares per offering; no interest on the account | Plan s.8.1, s.7.3, s.12, s.11; 10-K FY2026 ("not exceeding 15% of their gross compensation") |
| What Microsoft India deducts | 15% of base pay: Rs 59,375/month = 15% of Rs 47,50,000 base (2024-25) | Payslips Oct 2024-Aug 2025; Compensation Summary 2026-11-08 |
| Current base | Rs 65,33,200 from 2026-10-01, so 15% = Rs 9,79,980/yr = Rs 81,665/month (derived) | Compensation Summary 2026-11-08 |
| $25,000/yr limit | Plan s.21 applies it to every participant ("notwithstanding anything in the Plan"), measured at FMV when the offering starts; lower limits allowed abroad. 15% of base is about $10,400/yr at 94.03, well under it | Plan s.21; yfinance INR=X 2026-11-13 |
| India is in which part of the plan | Non-Statutory (non-423) part likely for India: not verified (plan s.1 allows it; no India appendix found) | Plan s.1 |
| Stop / refund | Can withdraw before the first day of the last month of an offering; whole account refunded. Seen: Jul-Aug 2025 deductions (Rs 1,18,750) came back in the Sep 2025 payslip | Plan s.9.1; Fidelity ESPP Activity 2025 (withdrawal 2025-08-25); payslip 2025-09 |
| Joining again | File the election before the Offering Date; it rolls over each quarter until changed. Next offering 2027-01-01 to 2027-03-31; Fidelity's exact December cut-off: not verified | Plan s.4, s.8.1, s.10 |
| Plan use FY2026 | 5 million shares bought at an average $382.92 | 10-K FY2026 (filed 2026-07-29) |

Your purchases (Fidelity confirmations via `fidelity.purchases()`, Fidelity ESPP Activity 2024/2025 CSVs, read 2026-11-15):

| Purchase | Contributed (payroll) | Shares | Paid/sh | FMV/sh | Discount gain | Payroll INR/USD | yfinance INR=X that day |
|---|---|---|---|---|---|---|---|
| 2024-12-31 | Rs 1,78,125 = $2,082.39 | 5.4894 | $379.35 | $421.50 | $231 | 85.54 | 85.79 |
| 2025-03-31 | Rs 1,78,125 = $2,076.35 | 6.1458 | $337.85 | $375.39 | $231 | 85.79 | 85.54 |
| 2025-06-30 | Rs 1,78,125 = $2,078.38 | 4.6427 | $447.67 | $497.41 | $231 | 85.70 | 85.46 |
| Total | $6,237.12 | 16.2779 | | | $693 (11.1%) | avg +0.10% vs market | |

Contributions were set to 0% on 2025-08-25 (Fidelity ESPP Activity 2025); no purchase since 2025-06-30.

## 2. Net gain of selling at once, per Rs 1 L of salary contributed

Assumptions: USD/INR 94.03 (yfinance INR=X close 2026-11-13); MSFT $523.88 (yfinance 2026-11-13); slab 35.88%
on salary; Rs 1 L buys $1,063 of contributions -> shares worth $1,182 at purchase.

| Line | Rs per Rs 1 L | Basis |
|---|---|---|
| Discount gain (FMV - price paid = 1/9 of contribution) | +11,111 | Plan s.5 |
| Indian perquisite tax at 35.88%, withheld by payroll | -3,987 | `tax/investment-types.md` s.5 (perquisite = FMV - price paid; cost = FMV). Tax line: see finance-tax |
| Payroll INR -> USD conversion | -100 | Own data: payroll rate averaged +0.10% over the yfinance close (table above) |
| Capital gain on the sale | about 0 on average | Shares post 1-2 days after the purchase (`fidelity.py`, confirmations dated the next business day). MSFT 2-trading-day move: s.d. 2.68%, mean +0.12% (yfinance, 2024-11-13 to 2026-11-13) = about +-Rs 3,000 one s.d. before tax, taxed or offset at 35.88% as ST |
| FX mismatch on the sale (my computation) | about 0 | Purchase is on a quarter-end; a sale in the first days of the next month uses the rate of the last day of the previous month (Rule 115 reading in `tax/investment-types.md` s.5), close to the perquisite date rate. Tax line: see finance-tax |
| Fidelity commission | 0 (not verified) | Fidelity retail schedule: $0 online US stock trades (fidelity.com, read 2026-11-15); stock plan accounts "may" use a NetBenefits schedule for sales of company stock (Fidelity fee schedule PDF): not verified |
| SEC Section 31 fee | -2 | $20.60 per $1 M from 2026-04-04 (SEC advisory 2026-02-27); FINRA TAF: negligible (not verified) |
| Cash-flow cost: salary waits for the purchase | -425 to -476 | Deductions at the end of months 1, 2, 3 of the offering wait 2, 1, 0 months = 1 month average (pay dates not verified); arbitrage fund 5.10% (< 12 m) to 5.71% (> 12 m) after tax (`tax/FY2026-27/fd-and-advance-tax.md`) |
| **Net, kept in USD and sent to IBKR** | **about +6,570 (6.6%)** | Before the Fidelity wire fee |
| Fidelity USD wire to IBKR | 0 to -960 | Fee not verified: Fidelity's PDF lists only foreign-currency wires (up to 3%); $25 per quarterly wire (Schwab's level, `research/global/platforms.md`) on a 15% quarter = Rs 2,350 = Rs 960 per Rs 1 L. IBKR incoming wire: no fee found (`platforms.md`) |
| If brought to India instead | -1,100 to -2,200 more | Indian bank FX about 1.5-2% from interbank (ET 2025-12-22, INX GA Aug 2026 via `platforms.md`, for outward; inward spread not verified) plus about Rs 500-1,000 fixed per wire. Never use Fidelity's INR wire (up to 3%, Fidelity fee schedule PDF) |
| US estate tax | 0 | Nothing held; cash left at Fidelity in a money-market sweep may count as US property (not verified), so move it on |

Per purchase: about 6.6% of the money contributed (5.6% with a $25 wire at 15%; about 4.4-5.5% if brought to
India). Annual: at 15% of base (Rs 9.8 L/yr) about **Rs 64,000/yr** net (Rs 55,000 with $25 wires). On the money
actually waiting (about one month's contribution at a time) that is roughly 80%/yr annualised.

Against the arbitrage fund: the same Rs 1 L kept in arbitrage for the one-month wait earns Rs 425-476 after tax
(already deducted above). The ESPP adds about Rs 6,570 on top; after the sale the money is free again. The arbitrage
fund does not get close.

Extra benefit (my computation): payroll moved rupees to dollars at about +0.10% from market, while a bank wire to
IBKR costs about 2% plus Rs 500-1,000 (`platforms.md`). For money that is going abroad to the UCITS plan anyway,
the ESPP route saves about Rs 2,000 per Rs 1 L of FX on top of the discount.

## 3. LRS, TCS and FEMA

| Question | Answer | Source (date) |
|---|---|---|
| Route | Employee scheme shares (ESOP/Employee Benefit Scheme, under 10% of the company, no control) are OPI | RBI FEM (Overseas Investment) Directions 2022, para 1(ix)(f), 22(2) (rbi.org.in id=12381, read 2026-11-15) |
| Does it use the LRS limit? | Yes. "no limit on the amount ... such remittances shall be reckoned towards the LRS limit" ($250,000/FY) | Same Directions, para 22(7). The brief's guess "not LRS" is wrong on the limit; the OPI route has no cap of its own |
| Reporting | Employer files Form OPI; nothing for the employee | Same Directions, para 22(5); OI Regulations reg 10(3) |
| TCS above Rs 10 L | 20% for investment purposes above Rs 10 L/FY; a tax credit (Form 26AS/27D, claim in ITR or advance tax), so a cash-flow cost only | `legal/compliance/fema-lrs.md`, `platforms.md` (Finance Act 2026, read 2026-11-15) |
| Is TCS collected on the employer's ESPP remittance? | Not verified: the employer's bank, not the user's, remits; whether the Rs 10 L threshold is per bank or per person is also not verified. 15% of base (Rs 9.8 L) alone is under Rs 10 L | Open question C2 in `legal/questions.md`. Tax line: see finance-tax |
| Idle sale cash abroad | LRS proceeds idle over 180 days must come home unless reinvested; whether this covers ESOP proceeds: not verified | RBI LRS FAQ Q4; Master Direction LRS para 17; question C4 |

## 4. Concentration

MSFT is already 116.888 shares, about $61,235 (`tax/investment-types.md` s.5, 13 Nov 2026 close). Holding ESPP
shares at 15% would add about $11,600/yr of MSFT (FMV), on top of RSU vests, all short-term (35.88%) for
24 months, and over the $60,000 US estate-tax line already. The concentration plan sells every new ESPP lot
at purchase (`research/themes/employer-stock-concentration.md`, rules-of-thumb.md, plan.md tranche 0).

## 5. How to run it

1. Before the 2027-01-01 offering starts (December cut-off: check in NetBenefits), set contributions to 15%.
2. Each quarter-end (next 2027-03-31): when the shares post (1-2 business days), sell all ESPP shares online at
   Fidelity. Check the trade confirmation for any fee (closes the "not verified" commission line).
3. Wire the USD (not INR) to IBKR; ask Fidelity for its USD wire fee first. If there is a fee, wire twice a
   year instead of quarterly, but keep each batch under 180 days idle.
4. At IBKR, invest within days into the UCITS split in `research/global/README.md` s.3 (45% EXUS, 10% IJPA,
   10% XDEW, 15% AVGS, ...). These are not US-situs.
5. If rupees are needed instead, wire USD to the Indian bank and compare its TT buying rate with interbank.
6. Keep the ESPP perquisite lines (Form 16/12BA; payslips show only the deduction) and each sale for Schedule
   CG; the Fidelity account is already in Schedule FA. Tax line: see finance-tax.
7. Can stop any quarter: withdraw before the first day of the offering's last month for a full refund.

Risks: a 2-day MSFT fall (one s.d. about 2.7%) can eat part of the 11.1% discount; leaving Microsoft mid-
offering (refund terms on termination not checked).

## Sources tried

| Source | Used for | Read |
|---|---|---|
| SEC EDGAR: Microsoft 10-K FY2026 (0001193125-26-323660, filed 2026-07-29), ESPP note and exhibit list | 90%, quarterly, 15%, FY2026 purchases | 2026-11-15 |
| SEC EDGAR: Microsoft DEF 14A 2021-10-14 (0001193125-21-298757), Annex A ESPP plan | Plan s.1, 4, 5, 8-12, 21 | 2026-11-15 |
| SEC EDGAR: Microsoft DEF 14A 2026-10-21 | ESPP shares left (57,250,943 at 2026-06-30); no ESPP proposal found | 2026-11-15 |
| Drive Finance/: Fidelity confirmations (`fidelity.purchases()`), Fidelity ESPP Activity 2024/2025 CSVs | Purchases, contributions, 15% elections, stop 2025-08-25 | 2026-11-15 |
| Drive Finance/Salary/Microsoft: StockExport_2026-11-08.xlsx (RSU only, no ESPP terms), Compensation Summary 2026-11-08, payslips 2024-10 to 2026-10 | Base pay, monthly deduction, refund | 2026-11-15 |
| yfinance (INR=X, MSFT) | FX and prices on purchase dates; 2026-11-13 closes; 2-day volatility | 2026-11-15 |
| Fidelity Brokerage Commission and Fee Schedule PDF; fidelity.com commissions page | $0 online trades; foreign-currency wires up to 3%; stock plan schedule separate | 2026-11-15 |
| SEC Section 31 fee advisory FY2026 (2026-02-27) | $20.60 per $1 M | 2026-11-15 |
| RBI FEM (OI) Directions 2022 (id=12381) | OPI, LRS counting, Form OPI | 2026-11-15 |
| Repository: `tax/investment-types.md` s.4-5, `tax/FY2026-27/fd-and-advance-tax.md`, `legal/compliance/fema-lrs.md`, `research/global/platforms.md`, `research/global/README.md` s.3, employer-stock-concentration notes | Tax rules, arbitrage yield, TCS, wire costs, UCITS plan | 2026-11-15 |
| Not reached: Fidelity NetBenefits stock plan fee schedule and wire FAQ (login / JavaScript), Microsoft India ESPP country appendix | - | 2026-11-15 |
