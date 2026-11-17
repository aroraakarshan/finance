# FAST-DS 2026 and the missing Schedule FA (AY2019-20 to AY2025-26)

User decision 2026-11-15: not pursued (older returns not revised; accepted risk in `legal/compliance/schedule-fa.md#known-accepted-risk`). Work stopped; two unapplied corrections: the AY2026-27 revised-return deadline is 31 Mar 2027 per Finance Bill 2026 (Rs 5,000 fee after 31 Dec 2026), not 31 Dec 2026; the Alpaca A2 "closing Rs 167" error is unconfirmed (A2 may mean cash only).

## Summary

- Not pursued: by user decision of 2026-11-15 the older returns are not revised and FAST-DS 2026 is not used (risk accepted in `legal/compliance/schedule-fa.md#known-accepted-risk`).
- Kept only as a record of the figures (Sl.2 value about Rs 1.6 Cr, fee Rs 1 lakh, left-out US dividends about Rs 1.71 lakh); nothing to do.

Owner: `finance-tax`. Written 2026-11-15. Not tax or legal advice: figures and options for a CA.
The user decides; nothing is filed or paid by an agent. Builds on `legal/compliance/schedule-fa.md#status-per-account-and-calendar-year` and `#black-money-act-2015`.
Account numbers: last 4 digits only.

Number tags: [Y] = computed 2026-11-15 from the repository readers (`etrade.events()`,
`acquisitions()`, `transfers()`, `fidelity.lots()`, `indmoney.trades()`) and yfinance closes,
dividends and `INR=X`; INR is **approximate** (yfinance mid rate, not the SBI TT buying rate or the
RBI reference rate). [F] = filed ITR JSON/PDF in Drive `Tax/FY*/ITR`, read 2026-11-15.
Source tags [S1]-[S7] are listed in section 7.

## 1. Short answer

- FAST-DS 2026 exists and fits this case. Table Sl.2(b): a foreign asset bought from income
  already taxed in India but not shown in Schedule FA -> **flat fee Rs 1 lakh**, if the
  aggregate value of all Sl.2 assets is at most **Rs 5 crore** [S2 s.117; S3 r.5(1)].
- The user's Sl.2 value at the valuation date (31 Mar 2026) is about **Rs 1.6 crore** (up to
  about Rs 2.0 crore if every Fidelity lot is added) [Y]: well under the cap.
- Source is taxed: RSU and ESPP perquisites were in salary in every year (table 3.3) [F][Y].
- Some **income** was also left out: US dividends of FY2018-19 to FY2022-23, about **Rs 1.71
  lakh** [Y]. That is Sl.1(b) (60% of the income, about Rs 1.03 lakh) or an updated return
  (only AY2022-23 and AY2023-24 are still open).
- Deadline: Form 1 by **31 Dec 2026**; pay within 2 months from the end of the month of the
  order (up to 2 more months at 1%/month) [S3 r.2(4), r.7].
- Likely total: Rs 1 lakh (Sl.2(b)) + Rs 0.3-1.03 lakh for the dividends. Against this: a
  possible Rs 10 lakh BMA s.43 penalty per year, for up to 7 years.

## 2. The scheme (verified from primary text)

| Point | Rule | Source |
|---|---|---|
| Law | Finance Act 2026 (4 of 2026) Chapter IV. Bill clauses 114-128 = Act sections 130-144 (the rules cite s.131(1)(l), s.132, s.133 table, s.135, s.139, s.140, s.143 for bill clauses 115(1)(l), 116, 117, 119, 123, 124, 127). Enacted Act text not fetched; numbering inferred from the rules | [S2][S3] |
| In force | Rules from 16 Aug 2026; last date 31 Dec 2026 | [S3 r.1(2), r.2(4)] |
| Who | A resident in the previous year (or a non-resident who was resident in the year of the income or asset) | [S2 cl.115(1)(a)] |
| Cases | No return filed; asset or income not disclosed in a return filed before 16 Aug 2026; or income escaped assessment | [S2 cl.116] |
| Sl.1 (a) undisclosed asset (no explained source) or (b) undisclosed foreign income | 30% of asset value at 31 Mar 2026 + 30% of the income + 100% of that tax (= 60%). Cap: Sl.1 total at most Rs 1 crore | [S2 cl.117][S3 r.4 ill.1] |
| Sl.2 (a) bought while non-resident, or (b) bought from income offered to tax in India, but not shown in the FA schedule | Fee Rs 1 lakh (one fee for all Sl.2 assets: Form 1 item 6 "Nil or Rs 1 lakh"). Cap: Sl.2 total at most Rs 5 crore | [S2 cl.117][S3 r.5(1), ill.3, Form 1] |
| Both in one Form 1 | Yes: Part C rows 4(i)-4(vi), Part D item 7 = 60% of Sl.1 + fee | [S3 Form 1] |
| Value | Quoted shares: higher of cost and the average of high and low on 31 Mar 2026. Sold before 31 Mar 2026: higher of cost and sale price, less any amount reinvested in a new declared asset. USD at RBI reference rate on 31 Mar 2026. Value may differ up to 20% from the officer's without making the declaration void | [S3 r.3(1)(c), 3(2)-(4), 5(2)] |
| Immunity | No further tax, penalty or prosecution under the Black Money Act for what is declared, for FY2025-26 and earlier; declared income not taxed again under the 1961 Act or BMA | [S2 cl.120, 123] |
| Not covered | Proceeds of crime under PMLA proceedings; years with a completed BMA assessment; anything not declared; false particulars make it void; no refund; no rectification or set-off of past assessments | [S2 cl.118(3), 121, 122, 124] |
| How | Electronically, Form 1 on the e-filing portal (DSC if the return needs DSC, else EVC) -> order Form 2 within a month of the end of the month -> pay -> Form 3 with proof -> Form 4 certificate | [S2 cl.119][S3 r.6-9] |
| Portal | Notification listed on incometax.gov.in Latest News 1 Sep 2026; no FAQ or utility found on 2026-11-15 | [S4] |

Other relief in the law:

| Change | Effect here | Source |
|---|---|---|
| BMA s.42/43 penalty does not apply if foreign assets (other than immovable property) total at most Rs 20 lakh; from 1 Oct 2024 (was bank accounts up to Rs 5 lakh) | Only CY2019 and CY2020 were below Rs 20 lakh (table 3.2). Whether it covers years before 1 Oct 2024: not verified (CA) | [S5] |
| BMA s.49/50 prosecution: same Rs 20 lakh exclusion, retrospective from 1 Oct 2024 | Same years only | [S1 p.27-28] |
| Updated return (1961 Act s.139(8A)): 48 months from end of the AY; extra tax 25/50/60/70% of tax + interest by year | AY2022-23 open to 31 Mar 2027 (70%); AY2023-24 to 31 Mar 2027 at 60%, then 70% to 31 Mar 2028. AY2019-20 to AY2021-22 closed (48 months ended 31 Mar 2024/2025/2026) | [S6] |
| ITR-U limits: no loss return, no lower tax, no higher refund; needs extra tax | So it cannot be used only to add Schedule FA (portal rule that zero extra tax is refused: not verified). Here there is extra income (dividends) for both open years | [S1 p.24-25][S6] |
| Revised return | Time-barred for AY2019-20 to AY2025-26 (AY2026-27 already revised 8 Nov 2026) | `legal/compliance/schedule-fa.md#known-accepted-risk` |
| Do nothing | s.43 penalty Rs 10 lakh per year possible ("may"), no time limit in practice; AEOI data from US brokers already reaches the department [S1 p.27] | - |

## 3. Figures

### 3.1 What was filed [F]

| AY (FA period) | Form | FA filed | Foreign income filed |
|---|---|---|---|
| 2019-20 (FY2018-19 / CY2018) | ITR-1 | none (ITR-1 has no FA; ITR-1 not allowed with a foreign asset [S7]) | none; other sources Rs 0 |
| 2020-21 (CY2019) orig + revised | ITR-1 | none | none (OS = bank interest only) |
| 2021-22 (CY2020) | ITR-1 | none | none (OS = deposit interest only) |
| 2022-23 (CY2021) | ITR-2 | none | none: no dividends, no CG, no FSI |
| 2023-24 (CY2022) | ITR-2 | none | none |
| 2024-25 (CY2023) revised | ITR-2 | A3: QCOM, NXP only, dated 2023-04-01, initial value 0; no A2 | dividends Rs 1,60,970; STCL Rs 19,552 (FY2023-24, matches [Y] Rs 1,64,357 / -19,683) |
| 2025-26 (CY2024) | ITR-2 | A3: QCOM, NXP dated 2024-04-01, 49 INDmoney rows; no A2; no Fidelity | dividends Rs 2,18,519; CG = INDmoney only (QCOM sell-to-cover of FY2024-25 missing) |
| 2026-27 (CY2025) revised 8 Nov 2026 | ITR-3 | A2 8 rows + A3 101 rows | dividends Rs 2,66,361 |

### 3.2 Per calendar year, per account (shares only, approx INR) [Y]

Cash at the brokers (dividends paid in cash before DRIP started in Sep 2024, sale proceeds) is
not in these values: ETrade cash statements are needed. Peak = highest daily close x shares x
INR=X.

| CY | Account / security | Shares 31 Dec | Initial value (Indian cost of shares held at 31 Dec) | Peak (date) | Closing 31 Dec | Gross dividends | Gross sale proceeds |
|---|---|---|---|---|---|---|---|
| 2019 | ETrade ..7855 QCOM | 7 | 37,280 | 46,981 (8 Nov) | 44,042 | 624 | 21,217 |
| 2019 | ETrade ..8803 NXPI | 13.574 | 84,509 | 1,25,326 (25 Dec) | 1,23,186 | 1,194 | 0 |
| 2020 | QCOM | 101 | 8,64,253 | 12,22,746 (20 Nov) | 11,25,265 | 9,210 | 2,83,849 |
| 2020 | NXPI | 13.574 | 84,509 | 1,67,162 | 1,57,855 | 1,522 | 0 |
| 2021 | QCOM | 254 | 26,71,767 | 36,56,130 (15 Dec) | 34,57,253 | 37,769 | 6,06,927 |
| 2021 | NXPI | 13.574 | 84,509 | 2,44,485 | 2,30,136 | 2,256 | 0 |
| 2022 | QCOM | 449 | 48,29,207 | 46,36,146 (30 Nov) | 40,88,994 | 84,067 | 8,88,035 |
| 2022 | NXPI | 13.574 | 84,509 | 2,35,191 | 1,77,692 | 3,635 | 0 |
| 2023 | QCOM | 645 | 68,60,802 | 78,33,753 (28 Dec) | 76,77,654 | 1,43,041 | 7,77,202 |
| 2023 | NXPI | 13.574 | 84,509 | 2,63,370 | 2,56,595 | 4,557 | 0 |
| 2024 | QCOM | 750.805 | 83,66,134 | 1,41,28,410 (18 Jun) | 98,94,511 | 2,06,070 | 6,02,484 |
| 2024 | NXPI | 13.574 | 84,509 | 3,29,929 | 2,42,038 | 4,615 | 0 |
| 2024 | Fidelity ..4972 MSFT | 0 in account (5.4894 bought 31 Dec, confirmed 2 Jan 2025) | 1,98,491 | - | 0 (statement) | 0 | 0 |
| 2024 | Alpaca ..2423 (about 18 stocks) | - | - | not reliable (reverse-split prices) | 8,79,309 [Y]; filed A3 sum 7,20,317 [F] | 0 | 3,53,049 |
| 2025 | QCOM (to IBKR 16-19 Dec) | 0 | 85,27,150 | 1,25,27,417 (27 Oct); filed 1,25,23,280 | 0 | 2,33,415; filed 2,31,991 | 30,074 |
| 2025 | NXPI (to IBKR 8 Dec) | 0 | 84,509 | 2,89,925 | 0 | 3,584 | 11,778 |
| 2025 | Fidelity MSFT | 77.948 | 34,09,730 | 34,56,659 (9 Dec) | 33,84,052 | 12,098 | 0 |
| 2025 | Alpaca ..2423 | - | - | about 13.6 L (rough) | 12,46,847 | 4,051 | 12,56,559 |
| 2025 | IBKR ..4563 (filed [F]) | QCOM 761, NXPI 13, IBKR award | - | 1,26,27,947 | 1,20,24,250 | - | 2,407 |

Initial value uses Indian cost (FMV at release or purchase, x INR=X on that date), from the lots
that left ETrade in Dec 2025. Sell-to-cover shares are in the sale proceeds column, not in
"Shares 31 Dec". Peak and closing for A2 (account level) = the same figures plus any cash.

### 3.3 Totals and the Rs 20 lakh test (approx INR) [Y]

| CY | Peak, all foreign shares | Closing 31 Dec | Above Rs 20 L? | RSU/ESPP perquisite in that FY: [Y] vs filed [F] |
|---|---|---|---|---|
| 2019 | 1,69,730 | 1,67,229 | no | FY2018-19 13,239 vs 13,177; FY2019-20 58,582 vs 60,427 |
| 2020 | 13,74,196 | 12,83,119 | no (cash unknown) | FY2020-21 13,95,924 vs 14,17,395 |
| 2021 | 38,92,915 | 36,87,389 | yes | FY2021-22 21,00,678 vs 21,59,780 |
| 2022 | 48,30,990 | 42,66,686 | yes | FY2022-23 22,13,610 vs 22,49,997 |
| 2023 | 80,94,928 | 79,34,248 | yes | FY2023-24 28,04,214 vs 28,34,746 |
| 2024 | about 1.44 Cr | about 1.12 Cr | yes | FY2024-25 12,35,512 vs not split out in the JSON |
| 2025 | about 1.71 Cr | about 1.67 Cr (with IBKR filed) | yes | - |

The perquisites match within 1-3%: the shares were bought from income taxed in India (Sl.2(b)).

### 3.4 Income left out of the returns [Y]

| FY (AY) | US dividends (ex-date basis) | Sell-to-cover gain/loss | Route still open |
|---|---|---|---|
| 2018-19 (2019-20) | 235 | - | FAST-DS Sl.1(b) only |
| 2019-20 (2020-21) | 2,284 | -1,505 | Sl.1(b) only |
| 2020-21 (2021-22) | 17,586 | -6,932 | Sl.1(b) only |
| 2021-22 (2022-23) | 48,607 | -11,506 | Sl.1(b) or ITR-U (70%) |
| 2022-23 (2023-24) | 1,02,200 | -15,880 | Sl.1(b) or ITR-U (60%) |
| 2024-25 (2025-26) | filed | -4,137 (QCOM 21 May 2024 sale not in CG) | none needed (a loss; ITR-U cannot cut tax) |
| Total | **1,70,912** | losses only | |

US tax of 25% was withheld on these dividends (treaty rate; check 1042-S). Sl.1(b) gives no
credit for it; an ITR-U can claim it with Form 67. Rough ITR-U cost for both open years, at 34.3%
less 25% credit, plus interest and the 60-70% extra: about Rs 30,000-35,000 (not computed
exactly). Sl.1(b) for all five years: 60% x 1,70,912 = **Rs 1,02,547**.

### 3.5 Value at the valuation date, 31 Mar 2026 [Y]

Prices: average of high and low on 31 Mar 2026 (QCOM 127.535, NXPI 194.20, MSFT 367.985);
USD/INR 94.356 (yfinance; the rule needs the RBI reference rate).

| Asset (Sl.2(b)) | Rule | USD | INR approx |
|---|---|---|---|
| QCOM 761 shares (at IBKR; ETrade lots of 2019-2025) | higher of cost 107,955 and market 97,054 | 107,955 | 1,01,86,201 |
| NXPI 13 shares (at IBKR) | market (cost 1,187) | 2,525 | 2,38,211 |
| QCOM sold to cover tax, 2019-2024 (289 shares) | higher of cost and sale price, r.3(2) | 40,742 | 38,44,248 |
| MSFT ESPP 5.4894 shares of 31 Dec 2024 | cost 421.50 > market | 2,314 | 2,18,319 |
| Alpaca holdings (A3 shown, A2 not) | higher of average cost and market | 14,128 | 13,33,089 |
| **Total** | | **167,664** | **about 1.58 Cr** |
| If all Fidelity lots to 31 Mar 2026 are added | cost 44,039 | | about 1.98 Cr |

All cases are far below Rs 5 crore. "Cost" here is the Indian cost (FMV at release, s.49(2AA));
if the CA uses cost paid (0 for RSU), QCOM falls to its market value and the total is lower.

### 3.6 Errors in the filed FA (for the CA)

- CY2023 (AY2024-25 rev.): QCOM peak = closing Rs 80.7 L, dividends 1,59,035 and proceeds
  9,31,322 are FY2023-24 figures, not CY2023 ([Y] CY2023 proceeds 7,77,202).
- CY2024 (AY2025-26): QCOM peak shown = closing (98.3 L); [Y] peak about 1.41 Cr on 18 Jun 2024;
  proceeds 0 vs 6,02,484; NXPI peak 0; dates 2024-04-01.
- CY2025 revised: Alpaca A2 closing Rs 167 vs Alpaca shares about Rs 12.5 L at 31 Dec 2025 [Y]
  (A2 may have been cash only; check).

## 4. Recommendation (user decides; CA must review)

1. **File one FAST-DS Form 1 before 31 Dec 2026** (aim by 15 Dec so the order and payment fit):
   - Sl.2(b): QCOM and NXPI (ETrade ..7855, ..8803, including sold-to-cover shares), the
     Fidelity ..4972 account and the 31 Dec 2024 MSFT lot, and the Alpaca ..2423 account;
     years 2018-19 to 2024-25; resident. Fee **Rs 1,00,000**.
   - Dividends FY2018-19 to FY2022-23: either Sl.1(b) in the same Form 1 (**Rs 1,02,547**, one
     step, full immunity), or Sl.1(b) only for FY2018-19 to FY2020-21 (60% x 20,105 = Rs 12,063)
     plus ITR-U for AY2022-23 and AY2023-24 (cheaper, needs Form 67, two more filings).
2. Pay the amount in the Form 2 order within 2 months from the end of its month; file Form 3;
   keep the Form 4 certificate.
3. Documents: ETrade RS release, ESPP and trade confirmations and statements (Oct 2019 on;
   earlier from the confirmations), ETrade transfer statements of Dec 2025, IBKR statements,
   Fidelity confirmations and statements (Jan-Jun 2025 missing), INDmoney trade file, Form 16 for
   FY2018-19 to FY2024-25 (perquisite proof), 1042-S, filed ITRs, prices on 31 Mar 2026, RBI
   reference rate of 31 Mar 2026, PAN and address (passport only if non-resident in a year).
4. Going forward (AY2026-27 return of CY2025 is already revised; CY2026 for the next return): one
   A2 row per account and nature (D, S), one A3 row per lot with the real acquisition date and
   Indian cost, peak and closing at the SBI TT buying rate, closed accounts with closing 0, and
   FSI/TR with Form 44 (Form 67). Follow `tax/migration-indmoney-to-ibkr.md` s5; do not use the
   INDmoney draft.

## 5. Questions for the CA

1. Sl.2(b) for all assets, or Sl.2(b) plus Sl.1(b) for the dividends, or ITR-U for AY2022-23 and
   AY2023-24? Can one Form 1 hold both Sl.1 and Sl.2 (Form 1 suggests yes)?
2. Do assets already shown in a later return (CY2025) or partly shown (CY2023-24 A3, Alpaca A3)
   still need declaring, given the immunity covers only what is declared?
3. Should sold-to-cover shares (held 1-2 days) be declared, and at what value?
4. Cost for valuation: Indian cost (FMV at release) or amount paid?
5. ETrade cash (dividends before Sep 2024, the "Bank deposit program"): A1 or A2, and is it a
   separate asset to declare? Its balances are unknown.
6. Does the Rs 20 lakh relief apply to CY2019-CY2020 defaults (before 1 Oct 2024)?
7. AY2019-20 to AY2021-22 were filed on ITR-1 while holding foreign assets: any effect beyond FA?
8. Does FAST-DS (no FTC) or ITR-U (FTC) apply to dividends already taxed 25% in the US?

## 6. Untested or not verified

- INR uses yfinance `INR=X`, not SBI TT buying or RBI reference rates.
- Dividends use ex-dates and shares held the day before; checked against the filed figures
  (FY2023-24, FY2024-25, CY2025 QCOM: within 1%), not against 1042-S for earlier years.
- Alpaca peaks: reverse-split price adjustments make yfinance peaks wrong (PRFX, SST, CERO).
- ETrade before Oct 2019 has no statements; holdings come from confirmations only.
- Enacted Finance Act 2026 text and any CBDT FAQ were not fetched; ITR-U interest not computed.

## 7. Sources (read 2026-11-15)

- [S1] Finance Bill 2026 Memorandum, pages 24-29 (updated return, FAST-DS, BMA s.49/50):
  https://www.indiabudget.gov.in/doc/memo.pdf
- [S2] Finance Bill 2026, Chapter IV, clauses 114-128 (pages 94-101):
  https://www.indiabudget.gov.in/doc/Finance_Bill.pdf
- [S3] CBDT Notification 114/2026, G.S.R. 732(E), 14 Aug 2026, FAST-DS Rules 2026, rules 1-9 and
  Forms 1-4: https://www.incometax.gov.in/iec/foportal/sites/default/files/2026-08/Notification%20114.pdf
- [S4] incometax.gov.in Latest News (entry 01-Sep-2026):
  https://www.incometax.gov.in/iec/foportal/latest-news
- [S5] Finance (No.2) Bill 2024 Memorandum, BMA s.42/43 (page 58):
  https://www.indiabudget.gov.in/budget2024-25/doc/memo.pdf
- [S6] Budget 2025-26 Memorandum, item VIII, s.139(8A) 48 months:
  https://www.indiabudget.gov.in/budget2025-26/doc/memo.pdf
- [S7] incometax.gov.in, Returns applicable for salaried individuals AY2026-27 (ITR-1 not for a
  person with a foreign asset; rule for earlier years not checked):
  https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1
