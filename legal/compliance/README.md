# Compliance (FEMA/LRS, Schedule FA, Black Money Act)

## Summary
- Foreign holdings (US shares, ETFs, employer ESPP/RSU) are permitted under FEMA; two grey items (IBKR deposit award, gold ETCs) are questions for a CA.
- To do: CY2026 Schedule FA with every account, bank LRS/Form 26AS records, IBKR idle cash age, W-8BEN dates, a power of attorney for incapacity.
- Older-year Schedule FA gaps (AY2019-20 to AY2025-26) are a known, accepted risk (user decision 2026-11-15); the current year is fixed per user.

Owner: `finance-legal`. Written 2026-11-15. Not legal or tax advice: findings and questions for an Indian lawyer/CA ([questions](../questions.md), section "Compliance"). The user decides and acts.

Sources: each rule has a source tag listed in [sources.md](sources.md); all read 2026-11-15. "not verified" = the primary text was not fetched; the rule comes from a repository note or general knowledge and must be checked. Account numbers: last 4 digits only. Tax effects (rates, FTC, lot cost) belong to `finance-tax`; these notes link to its files.

## Status

| Area | Status | Main point |
|---|---|---|
| LRS limit (USD 250k per FY) | unknown | No remittance records in the repository or Drive (`Banking/` holds only an empty `HDFC/FD` folder). Likely far below the limit, but not shown |
| Permitted holdings (OPI) | OK, 2 grey items | US-listed shares, ETFs and employer ESPP/RSU are OPI. Grey: IBKR stock award for a cash deposit; ETCs (gold) |
| 180-day rule on idle cash | gap to check | IBKR cash $795 (age unknown); dividends kept as cash |
| Reporting by the user under FEMA | OK | No Form OPI for resident individuals; employer reports ESOP; bank reports each remittance (Form A2) |
| TCS on LRS | unknown | Check Form 26AS per FY against remittances |
| Schedule FA, CY2018-CY2022 | accepted risk | Returns AY2019-20 to AY2023-24 have no Schedule FA; AY2019-20 to AY2021-22 were filed on ITR-1. User decision 2026-11-15: older returns not revised ([accepted risk](schedule-fa.md#known-accepted-risk)) |
| Schedule FA, CY2023-CY2024 | accepted risk | Partial: only A3 rows, no A2 (custodial accounts), wrong acquisition dates, Fidelity missing in CY2024. Same user decision |
| Schedule FA, CY2025 | done per user | Revised AY2026-27 return (8 Nov 2026); user says this year is fixed (not verified by us); no action |
| Schedule FA, CY2026 | to do | Due with the TY2026-27 return; do not copy the INDmoney draft (`tax/migration-indmoney-to-ibkr.md` s5) |
| Black Money Act exposure | accepted risk | Rs 10 L penalty possible per year of non-disclosure; Rs 20 L relief does not apply (assets far above); user accepts it for older years ([accepted risk](schedule-fa.md#known-accepted-risk)) |
| Powers of attorney | gap | None recorded; Indian POA ends on incapacity or death [C1] |
| W-8BEN (US) | unknown | Valid to end of the 3rd calendar year after signing [U1]; dates per broker not recorded |

## Top actions

Top actions (user, with a CA):
1. CY2026 Schedule FA in the TY2026-27 return: every account in [Accounts in scope](#accounts-in-scope), from the start
   (`tax/migration-indmoney-to-ibkr.md` s5).
2. Collect bank LRS/Form A2 records and Form 26AS (TCS) for FY2018-19 onward ([LRS use per FY](fema-lrs.md#reporting-and-lrs-use-per-fy)).
3. Check the IBKR idle cash age and W-8BEN dates at IBKR, Fidelity and Alpaca.
4. Power of attorney for incapacity ([powers of attorney](poa-and-us-forms.md#powers-of-attorney)).

## Topic notes

| Note | What it covers |
|---|---|
| [fema-lrs.md](fema-lrs.md) | LRS limit, permitted holdings (OPI), 180-day rule, gifts and inheritance, reporting and LRS use per FY, TCS |
| [schedule-fa.md](schedule-fa.md) | Schedule FA tables, filed returns, status per account and year, Black Money Act, accepted risk |
| [property-abroad.md](property-abroad.md) | Review of the research note on buying property abroad (rule 21, borrowing, 180 days, FA, succession) |
| [poa-and-us-forms.md](poa-and-us-forms.md) | Powers of attorney; W-8BEN, 1042-S, US estate tax link |
| [derivatives-abroad.md](derivatives-abroad.md) | Options on foreign shares (covered calls, protective puts): not permitted for resident individuals as we read FEMA; no hedging exception |
| [insider-trading.md](insider-trading.md) | Trading in suppliers and vendors: Microsoft's public insider policy, US/EU/India insider law, per-name verdicts for the expertise-edge ideas (own sources I1-I12) |
| [odi-private.md](odi-private.md) | Startup and business stakes abroad (ODI): foreign startup shares, SAFEs (grey), card payment, buying a foreign SaaS company or its assets, filings (Form FC, UIN, APR) |
| [india-retail-rules.md](india-retail-rules.md) | Indian buyback small-shareholder quota (one PAN, clubbed across demat accounts), IPO retail and quota rules, family members applying (own bank/UPI, mule accounts, benami), tax-free bonds on the exchange vs OTC (own sources R1-R8) |
| [sources.md](sources.md) | All sources with URLs and dates |

## Accounts in scope

From `portfolio/accounts.md`, `portfolio/summary.md` (values 2026-11-13) and the filed returns.

| Account | Held | Calendar years with an asset | Notes |
|---|---|---|---|
| ETrade (Morgan Stanley) NXP plan ..8803 | NXPI ESPP | CY2019 (bought 2019-02-28) - CY2025 | Emptied Dec 2025; "Bank deposit program" file 2023-09-05 |
| ETrade (Morgan Stanley) QCOM plan ..7855 | QCOM RSU/ESPP, DRIP | CY2019 (first release 2019-08-19) - CY2025 | Emptied Dec 2025 (ACATS to IBKR); "Bank deposit program" files 2023-09-05..2025-12-22 |
| Fidelity NetBenefits ..4972 | MSFT RSU/ESPP | CY2024 (statements from 2024-07-22; first ESPP 2024-12-31) - now | $61.2k |
| INDmoney/Alpaca ..2423 | US stocks, cash | CY2024 (first trade 2024-08-07) - CY2026 (to 5 May 2026) | Number changed 5 May 2026 |
| INDmoney/Alpaca ..1593 | US stocks, wallet cash $4,574 | CY2026 (from 5 May 2026) | Moving to IBKR; close by 31 Dec 2026 |
| IBKR ..4563 | QCOM 761, AVGO, VRT, IBKR award, cash $795 | CY2025 (opened by Apr 2025) - now | Entity (IB LLC vs IB India) unknown; filed FA says "Interactive Brokers LLC" |

## Needed from user and next steps

Needed from user:
1. Bank LRS/Form A2 records per FY since FY2018-19, INDmoney add-money history, IBKR deposit
   history; Form 26AS/AIS TCS lines per FY.
2. Any other foreign account ever held (bank, insurance, other plan brokers).
3. IBKR: entity, age and source of the $795 cash; W-8BEN dates at IBKR, Fidelity, Alpaca.
4. Fidelity: date the 2024-12-31 ESPP shares were credited.

Next steps:
- `finance-legal`: send these notes and the questions to `finance-main`.
- Update [Schedule FA status](schedule-fa.md#status-per-account-and-calendar-year) after each filing; update [LRS use per FY](fema-lrs.md#reporting-and-lrs-use-per-fy) when bank data arrives.
