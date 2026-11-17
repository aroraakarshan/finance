# Schedule FA and Black Money Act

## Summary
- Every foreign account (A2) and holding (A3) must be in Schedule FA for each calendar year it existed, closed ones included.
- Filed returns AY2019-20 to AY2025-26 have no or partial Schedule FA: known, accepted risk (user decision 2026-11-15); AY2026-27 fixed per user.
- Next: the CY2026 Schedule FA in the TY2026-27 return, with all accounts and correct numbers and dates.
- Black Money Act: Rs 10 L penalty per year for a missing or wrong disclosure; the Rs 20 L relief does not apply here.

Owner: `finance-legal`. Written 2026-11-15. Not legal or tax advice: findings and questions for an Indian lawyer/CA ([questions](../questions.md), section "Compliance"). The user decides and acts.

Source tags such as [L1] are listed in [sources.md](sources.md) (all read 2026-11-15). "not verified" = primary text not fetched.

## Schedule FA (Income-tax)

### The rules
- A resident and ordinarily resident must disclose all foreign assets, including shares and
  securities, and the income from them, in the return [B1].
- Period: the calendar year ending in the tax year (CY2026 for TY2026-27) (`tax/` rules note
  s5; ITR instruction text **not verified** this session).
- Tables in the current ITR-2 schema (AY2026-27) [I1]:
  - A1 foreign depository (bank) accounts;
  - A2 foreign custodial accounts: institution, account number, status, opening date, peak
    balance, closing balance, gross amount paid/credited and its nature (I interest, D dividend,
    S sale proceeds, O other, N none);
  - A3 foreign equity and debt interest: entity, date acquired, initial value, peak, closing,
    gross amount paid/credited, gross sale proceeds;
  - A4 cash-value insurance, B financial interest, C immovable property, D other assets,
    E signing authority, F trusts, G other income.
- Broker accounts: one A2 row per account (per nature of amount) and one A3 row per holding
  (per lot in the repository's method) (`tax/migration-indmoney-to-ibkr.md` s5).
- Closed or emptied accounts are shown in each CY they existed, with closing 0.
- Exchange rate: SBI TT buying rate on the peak date and on 31 Dec (`tax/` rules note s5; not
  verified from the instructions).
- Unvested RSUs: common view is no FA row until the shares vest (not verified;  [question](../questions.md) C6).
  The CY2025 FA has an A3 row for the unvested IBKR award shares (dated 2025-12-10).
- ITR-1 is not available to a resident with assets outside India (form eligibility; not
  verified this session).
- Also needed: Schedule FSI (foreign income by country), Schedule TR (tax relief) and Form 67
  (Form 44 under the 2025 Act) before claiming foreign tax credit (`tax/new-investments.md` s3).

### Filed returns

Read from Drive `Tax/FY*/ITR`, 2026-11-15.


| AY (CY covered) | Form | Schedule FA | FSI/TR | Form 67 |
|---|---|---|---|---|
| 2019-20 (CY2018 or FY2018-19) | ITR-1 | none | none | none |
| 2020-21 (CY2019) orig + revised | ITR-1 | none | none | none |
| 2021-22 (CY2020) | ITR-1 | none | none | none |
| 2022-23 (CY2021) | ITR-2 | none | none | none |
| 2023-24 (CY2022) | ITR-2 | none | none | none |
| 2024-25 (CY2023) original | ITR-2 | none | none | - |
| 2024-25 revised (Dec 2024) | ITR-2 | A3: 2 rows (QCOM, NXP, both dated 2023-04-01); no A2 | yes | filed |
| 2025-26 (CY2024), filed 13 Sep 2025 | ITR-2 | A3: 51 rows (QCOM and NXP 1 row each dated 2024-04-01; INDmoney stocks); no A2; no Fidelity/MSFT | yes | filed |
| 2026-27 (CY2025) original 18 Jul 2026 | ITR-3 | A3: 93 rows; no A2 | yes | filed |
| 2026-27 revised 8 Nov 2026 | ITR-3 | A3: 101 rows (QCOM from 2019-08-19, NXP from 2019-02-28); A2: 8 rows (ETrade ..7855, ..8803, IBKR ..4563, Fidelity ..4972, Alpaca ..1593) | yes | revised |

### Status per account and calendar year

Y = shown, P = partly (A3 only, or wrong dates), N = not shown, - = no asset that year.

| Account | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| ETrade NXP ..8803 (+ bank deposit program) | N | N | N | N | P | P | Y | - (closed; CA to confirm) |
| ETrade QCOM ..7855 (+ bank deposit program) | N | N | N | N | P | P | Y | - (closed; CA to confirm) |
| Fidelity ..4972 (MSFT) | - | - | - | - | - | N (ESPP 2024-12-31; account open from Jul 2024) | Y (opening date shown 2025-03-31) | due |
| INDmoney/Alpaca ..2423 | - | - | - | - | - | P (A3 only) | P (A2 shown as ..1593) | due |
| Alpaca ..1593 | - | - | - | - | - | - | - (wrongly used for 2025) | due |
| IBKR ..4563 | - | - | - | - | - | - | Y (opening date shown 2025-12-08) | due |

Points for the CA:
- CY2019-CY2022: no Schedule FA at all, with QCOM and NXP shares held (and QCOM dividends,
  sell-to-cover sales). Whether the dividends and sales of those years were offered to tax is a
  `finance-tax` question (STATUS.md already lists the 2024-05-21 sell-to-cover sale).
- CY2023-CY2024: no A2 rows; acquisition dates 2023-04-01 / 2024-04-01 are not the real dates.
- CY2024: Fidelity account and the MSFT ESPP shares of 2024-12-31 not shown (check when the
  shares were credited).
- CY2025: Alpaca account shown as ..1593 opened 2024-06-10; it was ..2423 in 2025 (number changed
  5 May 2026). IBKR opening date 2025-12-08 vs account open by Apr 2025; Fidelity 2025-03-31 vs
  statements from Jul 2024.
- ETrade "Bank deposit program" (cash sweep at a bank): A1 (bank account) or part of the A2
  custodial row? ([question](../questions.md) C5).

Needed from user: confirm that no other foreign account existed (e.g. a US bank account, NXP or
Qualcomm plan accounts at other brokers, foreign insurance); ETrade bank deposit program
statements; peak values for CY2019-CY2024 (from ETrade statements in Drive).

## Black Money Act 2015

### Penalties
- s.42 (no return) and s.43 (return without, or with wrong, foreign asset/income details):
  penalty Rs 10 lakh, "regardless of the value of asset" [B1].
- From 1 Oct 2024 these do not apply where foreign assets other than immovable property total
  up to Rs 20 lakh (was: bank accounts up to Rs 5 lakh) [B1].
- Prosecution (s.49, s.50): Finance Act 2026 excludes the same Rs 20 lakh cases, retrospective
  from 1 Oct 2024 [B2].
- Tax at 30% on the value of an "undisclosed asset" (s.10) and penalty 3x that tax (s.41): not
  verified from the Act. An undisclosed asset means one whose source the owner cannot explain
  [B3 s.115(1)(j) for the same term in FAST-DS]. Shares bought from salary already taxed in India
  have an explained source, so the main exposure is the s.43 penalty, not s.10 tax (CA to
  confirm).
- No time limit in effect: an undisclosed asset is charged in the year it comes to notice (BMA
  s.4(3), s.72(c)) (`tax/migration-indmoney-to-ibkr.md` s6, not verified).

### Exposure
- Foreign assets were far above Rs 20 lakh in recent years (ETrade QCOM peak Rs 1.25 Cr in CY2025
  per the filed FA; IBKR closing Rs 1.20 Cr). Earlier peaks not computed.
- Returns with no or partial FA: AY2019-20 to AY2025-26 (7 years). At Rs 10 lakh each the
  theoretical maximum is large; penalty is discretionary ("may"), but the risk is real
  (not verified how often it is levied for salary-funded ESOP holdings).

### Known, accepted risk
User decision 2026-11-15: older returns are not to be revised; the current year (AY2026-27,
revised 8 Nov 2026) is fixed (per user, not verified by us). The finding stays on record: no or
partial Schedule FA in AY2019-20 to AY2025-26 ([filed returns](#filed-returns), [status](#status-per-account-and-calendar-year)), with the exposure in [Exposure](#exposure). For
the record only: FAST-DS 2026 (CBDT Notification 114/2026) takes declarations until
31 Dec 2026 [B4].
