# Tax paid after the year, refunds, and US dollar cash

## Summary
- The Rs 8,28,900 (13 Sep 2025) and Rs 3,06,140 (18 Jul + 8 Nov 2026) self-assessment payments included interest of Rs 81,255 and Rs 24,895 for missed advance tax (s.234B/C). Over 3 years: Rs 1,20,523.
- Cause: no advance tax on interest, dividends and gains, plus in 2024-25 the job change (two employers under-deducted about Rs 4.83 L). Salary TDS was exact in the other two years.
- Now: pay about Rs 63,500 by 15 Dec 2026 and the rest by 15 Mar 2027 (`fd-and-advance-tax.md`). That avoids s.234B and keeps s.234C at about Rs 4,500. Pay tax by UPI or net banking: the card payment cost Rs 2,924.
- Refunds: only Rs 180 (AY2024-25), paid 7 Jan 2025. Nothing is pending. Open the AY2026-27 revised intimation (password-protected) and check the refund status on the e-filing site; both need your login.
- US dollar cash at IBKR/Fidelity goes in Schedule FA A2 as part of the account. Converting it to rupees may be a small capital gain (unsettled; keep the bank advice). Cash from each sale/dividend not reinvested within 180 days must come home (FEMA; `legal/compliance/fema-lrs.md`).

Written 2026-11-15 by `finance-tax` (agent `payments`). Sources: ITR JSONs and 143(1) intimations in Drive
`Finance/Tax/FY2023-24..FY2025-26/ITR`, challan receipts, AIS/26AS (generated 7-8 Nov 2026), HDFC
savings exports 1 Apr 2025 - 14 Nov 2026, HDFC card statement Aug 2026. Sections: 1961 Act for past
years. For 2026-27, the 2025 Act (AF) section comes first and the 1961 section is in brackets.

## 1. Tax paid after the year end

| Return | Total tax and interest | TDS | Tax relief (FTC) | Self-assessment tax: date, amount | s.234A | s.234B | s.234C | Total interest |
|---|---|---|---|---|---|---|---|---|
| AY2024-25 revised (FY2023-24) | 22,38,186 | 20,47,993 | 40,240 | 26 Jul 2024 Rs 1,75,370; 21 Dec 2024 Rs 15,000 | 0 | 7,737 | 6,636 | 14,373 |
| AY2025-26 (FY2024-25) | 21,08,292 | 12,79,393 | 53,560 | 13 Sep 2025 Rs 8,28,900 (net banking) | 0 | 44,856 | 36,399 | 81,255 |
| AY2026-27 original (FY2025-26) | 37,46,414 | 34,73,971 | 6,064 | 18 Jul 2026 Rs 2,72,440 (credit card) | 0 | 9,996 | 12,504 | 22,500 |
| AY2026-27 revised, 8 Nov 2026 | 37,80,111 | 34,73,971 | 65,815 | above + 8 Nov 2026 Rs 33,700 (tax 31,305 + interest 2,395, UPI) | 0 | 12,544 | 12,351 | 24,895 |

- Advance tax paid in all three years: 0 (ITR `TaxesPaid.AdvanceTax`).
- The 143(1) intimations accepted these interest figures, with Rs 1-3 rounding differences. Net payable is 0 in every intimation.
- s.234A is 0 because each return was filed by its due date. AY2025-26 was filed 13 Sep 2025, inside the extended due date of 15 Sep 2025.
- Rs 8,28,900 = tax about Rs 7,47,645 + interest Rs 81,255. Its challan is not in Drive, so the challan split is unknown. It does not matter: the ITR sets the whole payment against tax plus interest.
- Rs 2,75,364.37 on the card (18 Jul 2026) vs Rs 2,72,440 on the challan. The Rs 2,924.37 extra (1.07%) is a card or gateway fee, and you cannot claim it as tax paid.

Why the tax was due after the year. Salary tax below is computed from the ITR at the slab rates
with surcharge and 4% cess:

| Year | Salary tax vs employer TDS | Tax left on other income | What the other income was |
|---|---|---|---|
| FY2023-24 | Rs 19,89,441 = TDS (exact) | about Rs 1,75,800 | Interest Rs 6.39 L, dividends Rs 1.61 L |
| FY2024-25 | Rs 16,99,205 vs TDS Rs 12,15,835: **Rs 4,83,370 short** | about Rs 2,64,300 | Interest Rs 7.72 L, dividends Rs 2.19 L, gains Rs 1.46 L |
| FY2025-26 | Rs 33,84,619 = TDS (exact) | about Rs 2,81,200 | Interest Rs 9.25 L, dividends Rs 2.66 L, small gains |

- FY2024-25: Qualcomm (Rs 25.8 L) and Microsoft (Rs 37.6 L) each deducted tax as if it were your only employer. Each used the lower slabs, and neither applied the 10% surcharge. Whether you gave Microsoft your Qualcomm salary (Form 12B) is not known.
- The rest of the gap each year is interest, dividends and gains. Advance tax was due on these from 15 Jun, and none was paid.

## 2. Does the 2026-27 plan avoid the interest?

| Charge | Rule | Plan in `fd-and-advance-tax.md` (tax after TDS about Rs 2.85 L) | Result |
|---|---|---|---|
| s.234C, 15 Jun and 15 Sep (AF s.425) | 1% a month for 3 months on the shortfall from 15% / 45% | Nothing paid by 15 Sep | About Rs 4,100-4,500, already fixed |
| s.234C, 15 Dec | 75% by 15 Dec | Rs 1,50,000 paid 9 Nov (challan, minor head 100, verified) + about Rs 63,500 = Rs 2,13,500 | 0 if paid in full |
| s.234C, 15 Mar | 100% by 15 Mar, 1% on the shortfall | About Rs 71,200 | 0 if paid in full |
| s.234B (AF s.424) | None if at least 90% of the final tax after TDS is paid by 31 Mar | 100% of the estimate | Avoided if the estimate holds |

- Margin: 10% of Rs 2.85 L is about Rs 28,500. These could use it up:
  - Punjab Gramin Bank interest (no FD list yet)
  - a QCOM sale (add about Rs 1.59 L by 15 Dec, `employer-stock.md`)
  - silver sale timing
  - salary TDS: the Oct payroll used a 10% surcharge. If it stays at 10%, about Rs 1.4 L is left (computed). Last year payroll ended exact at 15%.
- Before 15 Mar 2027, re-estimate with the Feb payroll sheet and PGB certificates, and pay the full estimate. Overpaying only delays a refund, which comes with interest (1961 s.244A). Underpaying costs 1% a month.
- Expected interest for 2026-27: about Rs 4,500, against Rs 24,895, Rs 81,255 and Rs 14,373 in the last three years.

Lesson for every year: salary TDS does not cover interest, dividends or gains. Each quarter,
pay advance tax on the expected non-salary income: 15% by 15 Jun, 45% by 15 Sep, 75% by 15 Dec
and 100% by 15 Mar. A gain needs to be covered only from the instalment after it arises.
Always pay by UPI or net banking.

## 3. Refunds

| Return | Refund claimed | 143(1) result | Paid | s.244A interest |
|---|---|---|---|---|
| AY2024-25 original | Rs 10 | Intimation 10 Aug 2024: net 0 (Rs 10 balance not issued) | - | - |
| AY2024-25 revised | Rs 180 | Intimation 2 Jan 2025: refund Rs 180 "with 244A interest" | 7 Jan 2025, ECS to bank (AIS FY2024-25 Part B4) | 0: no interest when the refund is under 10% of the tax (1961 s.244A(1)(a) proviso) |
| AY2025-26 | 0 | Intimation 13 Sep 2025: net 0 | - | - |
| AY2026-27 original | 0 | Intimation 21 Sep 2026: net 0 | - | - |
| AY2026-27 revised | 0 (JSON: refund 0, balance 0) | Intimation in Drive is password-protected, not read | - | - |

- No refund is pending. AIS (FY2025-26 and FY2026-27, Part B4) and 26AS (Part VII) show no refunds. The HDFC savings exports from 1 Apr 2025 to 14 Nov 2026 show no refund credit.
- You do: open the AY2026-27 revised intimation and confirm "no demand, no refund". On incometax.gov.in, check Services > Know Your Refund Status and Pending Actions > Response to Outstanding Demand. Both need your login.

## 4. US dollar cash at IBKR and Fidelity

| Question | Answer | Basis | Status |
|---|---|---|---|
| Where cash goes in Schedule FA | Table A2 (custodial account), one row per account and nature of amount: D dividend, S sale proceeds, I interest. Cash is part of the account; no separate cash row. Not Table A1 (A1 is for bank accounts). Period: the calendar year (CY2026 for the 2026-27 return). | ITR schema `DtlsForeignCustodialAcc`; `../migration-indmoney-to-ibkr.md` s.5; `../ca-questions.md` A2 row | likely |
| Peak and closing balance | Use the account value (shares + cash) from the statement, in rupees at the SBI TT buying rate on the peak date and on 31 Dec. Each share also has its own A3 row. | `../ca-questions.md` A2 row | likely |
| Gross amount credited | Dividends, sale proceeds and cash interest credited in the calendar year (gross, before US tax) | same | likely |
| Interest on IBKR cash | Taxed at slab (35.88%). Add an I row in A2. | `../investment-types.md` | resolved |
| Dollars -> rupees: is it taxed? | The law text says: foreign currency is "property of any kind", so it is a capital asset (AF s.2(22)(a); 1961 s.2(14)). It is not stock-in-trade or personal effects, and converting it is an exchange, so a transfer (AF s.2(109); 1961 s.2(47)). The rupee difference between when the dollars came in and when you convert them is a capital gain or loss: short-term at slab if held 24 months or less. Cost = the rupee value at which those dollars entered your income (sale proceeds and dividends at the r.206 SBI TT rate). AF s.43 (FX gains as income) covers business income only. In practice individuals rarely report this. No CBDT circular or ruling for individuals was found (only the Act text was searched). | [Act] s.2(22), s.2(109), s.43 (read 2026-11-15) | unsettled - CA if a conversion is large |
| Size of the effect | Small. A 1% rupee move on a year's ESPP ($10,400, about Rs 9.8 L) is about Rs 9,800 of gain or loss, and about Rs 3,500 of tax. | computed | - |
| What to keep | For each conversion: the bank advice or FIRA (the credit and the rate), and the date and rupee value of the dollars when they came in. | - | do |
| Leaving sale money at IBKR (FEMA) | RBI LRS FAQ Q4: income may stay abroad and be reinvested. Unspent foreign exchange from LRS remittances must come home within 180 days. Updated 15 Nov 2026 per `legal/compliance/fema-lrs.md` C29-C31: ESPP shares are bought under LRS (OI Master Direction para 22(7)); RSU shares are OPI and individuals may hold OPI "including by way of reinvestment" (OI Rules Sch. III para 1(2)(ii)); sale or dividend cash not reinvested must come home within 180 days of each sale/dividend (FEMA 9(R)); broker cash is not a bank account, so park it only briefly between buys. | `../ca-questions.md` row "RSU/ESPP sale money kept at IBKR; LRS 180-day rule" | AD bank in writing |

## 5. Discrepancies

| # | What | Action |
|---|---|---|
| 1 | Card Rs 2,75,364.37 vs challan Rs 2,72,440 (18 Jul 2026): Rs 2,924.37 fee. `income/cost-cuts.md` row 1 says the fee is "nv"; it is now confirmed. | `finance-income`: update row 1 and D13 |
| 2 | `tax/index.md` row for `fd-and-advance-tax.md` says "pay about Rs 15,000 by 15 Mar 2027"; the note says about Rs 63,500 by 15 Dec and Rs 71,200 by 15 Mar | `finance-tax`: fix the index row |
| 3 | AY2026-27 Schedule FA A2: IBKR, Fidelity and E*Trade show the account value (IBKR closing Rs 1,20,24,250), but Alpaca shows closing Rs 167 (cash only?) while it still held shares at 31 Dec 2025 | Use one basis (account value) in the CY2026 return; revising AY2026-27 is your decision (fee after 31 Dec 2026) |
| 4 | Challan for the 13 Sep 2025 Rs 8,28,900 is not in Drive (the bank debit and the ITR match) | Download it from e-Pay Tax > Payment History |
| 5 | AY2026-27 revised intimation is password-protected; not read | You open it (section 3) |
