# Drive index

Generated 2026-11-17 by `python -m scripts.drive_index` from file names in Google Drive
`Finance/` (2308 files; no file opened). Run it after every download. Periods come from the
file names ("Newest" is the newest date in the names; "Added" is when the newest file was saved
to Drive). Gaps are months or years missing inside the covered range, at the series' own cadence;
brokers send quarterly statements in months without activity, so a monthly gap is not always a
missing file. Account numbers show only the last 4 digits.

## Brokers and sources
| Broker / source | Files | Folders | Accounts | Added |
|---|---|---|---|---|
| AngelOne | 37 | Investments/Stocks/AngelOne, Tax/FY*/Angel One | - | 2026-11-15 |
| ClearTax | 1 | Tax/FY*/ClearTax | - | 2026-07-18 |
| ETrade | 193 | Investments/Stocks/ETrade, Tax/FY*/ETrade | ****7855, ****8803 | 2026-11-08 |
| Fidelity | 27 | Investments/Stocks/Fidelity, Investments/Stocks/Fidelity/forms, Tax/FY*/Fidelity | - | 2026-11-16 |
| Guides | 7 | Guides | - | 2026-11-08 |
| HDFC | 41 | Banking/HDFC/CreditCard, Banking/HDFC/FD, Banking/HDFC/Savings | ****2235, ****9102 | 2026-11-15 |
| IBKR | 15 | Investments/Stocks/IBKR, Tax/FY*/IBKR | U****4563 | 2026-11-15 |
| Income Tax Site | 42 | Tax/FY*/Income Tax Site, Tax/FY2026-27 | - | 2026-11-09 |
| INDmoney | 37 | Investments/Stocks/INDmoney, Tax/FY*/INDmoney | - | 2026-11-15 |
| ITR | 59 | Tax/FY*/ITR | - | 2026-11-08 |
| Microsoft | 15 | Tax/FY*/Microsoft | - | 2026-11-08 |
| Portfolio | 1 | Portfolio | - | 2026-11-15 |
| Qualcomm | 3 | Tax/FY*/Qualcomm | - | 2025-08-29 |

## AngelOne
Files per tax folder: FY2024-25 10, FY2025-26 9, FY2026-27 14.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| holdings | CombinedHolding | 2 | as of 2026-11-15 (2 dates, from 2026-11-08) | - | 2026-11-15 |
| holdings | DP transactions and holding | 1 | FY2024-25 | - | FY2024-25 |
| holdings | MF holdings | 2 | as of 2026-11-14 (2 dates, from 2026-11-07) | - | 2026-11-14 |
| statement | ELSS | 3 | FY2024-25..FY2026-27 | - | FY2026-27 |
| statement | Ledger | 4 | FY2024-25..FY2026-27 (FY2026-27 to 2026-11-14) | - | 2026-11-14 |
| tax P&L | MF CapitalGains | 3 | FY2024-25..FY2026-27 | - | FY2026-27 |
| tax P&L | PnLSummary | 4 | FY2024-25..FY2026-27 (FY2026-27 to 2026-11-14) | - | 2026-11-14 |
| tax P&L | TaxPnL | 10 | FY2024-25..FY2026-27 (FY2026-27 to 2026-11-15) | - | 2026-11-15 |
| trades export | MF transactions | 4 | FY2024-25..FY2026-27 (FY2026-27 to 2026-11-14) | - | 2026-11-14 |
| trades export | TradesCharges | 4 | FY2024-25..FY2026-27 (FY2026-27 to 2026-11-15) | - | 2026-11-15 |

## ClearTax
Files per tax folder: FY2025-26 1.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| tax P&L | ClearTax US stocks | 1 | FY2025-26 | - | FY2025-26 |

## ETrade
Files per tax folder: FY2018-19 1, FY2019-20 7, FY2020-21 24, FY2021-22 29, FY2022-23 37, FY2023-24 44, FY2024-25 29, FY2025-26 16, FY2026-27 2.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| 1042-S | 1042-S ****7855 | 7 | CY2019..CY2023, CY2025 | CY2024 | CY2025 |
| ESPP/RSU confirmation | ESPP purchase ****7855 | 8 | 8 dates, 2020-07-31..2024-01-31 | - | 2024-01-31 |
| ESPP/RSU confirmation | ESPP purchase ****8803 | 1 | 1 date, 2019-02-28 | - | 2019-02-28 |
| ESPP/RSU confirmation | RS release ****7855 | 29 | 15 dates, 2019-08-19..2024-05-20 | - | 2024-05-20 |
| other | Bank deposit program ****7855 | 2 | 2 dates, 2023-09-05..2025-12-22 | - | 2025-12-22 |
| other | Bank deposit program ****8803 | 1 | 1 date, 2023-09-05 | - | 2023-09-05 |
| other | Letters and notices ****7855 | 2 | 2 dates, 2022-09-20..2026-11-01 | - | 2026-11-01 |
| other | Letters and notices ****8803 | 3 | 3 dates, 2022-09-20..2026-10-31 | - | 2026-10-31 |
| other | Tax documents ****7855 | 1 | 1 date, 2025-03-12 | - | 2025-03-12 |
| statement | Account statement ****7855 | 44 | from 2019-12, 19 earlier ranges, 2024-08..2024-09, 2024-12, 2025-03, 2025-06, 2025-09, 2025-12 (42 months) monthly | from 2020-01, 18 earlier ranges, 2024-07, 2024-10..2024-11, 2025-01..2025-02, 2025-04..2025-05, 2025-07..2025-08, 2025-10..2025-11 (31 months) | 2025-12-31 |
| statement | Account statement ****8803 | 52 | from 2019-12, 18 earlier ranges, 2024-06..2024-10, 2024-12..2025-01, 2025-03..2025-04, 2025-06..2025-07, 2025-09..2025-10, 2025-12 (50 months) monthly | from 2020-02, 17 earlier ranges, 2024-05, 2024-11, 2025-02, 2025-05, 2025-08, 2025-11 (23 months) | 2025-12-31 |
| statement | Cash management recap ****7855 | 3 | 2023-12, 2024-12, 2025-12 yearly | - | 2025-12-31 |
| statement | Cash management recap ****8803 | 3 | 2023-12, 2024-12, 2025-12 yearly | - | 2025-12-31 |
| tax P&L | GainsLosses ****7855 | 2 | CY2023..CY2024 | - | CY2024 |
| trade confirmation | TradeConfirmation ****7855 | 32 | 16 dates, 2020-08-21..2025-12-22 | - | 2025-12-22 |
| trade confirmation | TradeConfirmation ****8803 | 1 | 1 date, 2025-12-09 | - | 2025-12-09 |
| trades export | BenefitHistory ****7855 | 1 | as of 2026-11-07 | - | 2026-11-07 |
| trades export | BenefitHistory ****8803 | 1 | as of 2026-11-07 | - | 2026-11-07 |

## Fidelity
Files per tax folder: FY2024-25 6, FY2025-26 12, FY2026-27 4.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| 1042-S | 1042-S | 1 | FY2025-26 | - | FY2025-26 |
| other | other | 3 | 1 date, 2026-11-15 | - | 2026-11-15 |
| statement | Statement | 13 | 2024-07, 2024-09..2024-12, 2025-06..2026-09 | 2024-08, 2025-01..2025-05 | 2026-09 |
| statement | TransactionSummary | 2 | FY2024-25..FY2025-26 | - | FY2025-26 |
| statement | Year-end report | 2 | CY2024..CY2025 | - | CY2025 |
| trade confirmation | TradeConfirmation | 4 | 4 dates, 2025-01-02..2025-07-01 | - | 2025-07-01 |
| trades export | ESPP activity | 2 | CY2024..CY2025 | - | CY2025 |

## Guides

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| guide | angelone-download-guide | 1 | no period in name | - | - |
| guide | etrade-download-guide | 1 | no period in name | - | - |
| guide | fidelity-download-guide | 1 | no period in name | - | - |
| guide | ibkr-download-guide | 1 | no period in name | - | - |
| guide | income-tax-download-guide | 1 | no period in name | - | - |
| guide | indmoney-download-guide | 1 | no period in name | - | - |
| guide | itr-filing-guide | 1 | no period in name | - | - |

## HDFC

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| 16A | Form 16A | 3 | FY2025-26 | - | FY2025-26 |
| FD summary | FD summary | 1 | as of 2026-11-15 | - | 2026-11-15 |
| TDS | TDS report | 2 | FY2025-26..FY2026-27 | - | FY2026-27 |
| TDS | TDS summary | 2 | FY2025-26..FY2026-27 | - | FY2026-27 |
| credit card statement | Credit card statement ****2235 | 23 | 2024-12..2026-10 monthly | - | 2026-10 |
| interest certificate | FD interest certificate | 2 | FY2025-26..FY2026-27 | - | FY2026-27 |
| interest certificate | Savings interest certificate ****9102 | 2 | FY2025-26..FY2026-27 | - | FY2026-27 |
| savings statement | Savings statement (PDF/XLS/CSV) ****9102 | 6 | 2025-04..2026-11 | - | 2026-11-14 |

## IBKR
Files per tax folder: FY2025-26 7, FY2026-27 6.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| statement | ActivityStatement | 9 | CY2025..CY2026, FY2025-26..FY2026-27 (CY2026 to 2026-11-13; FY2026-27 to 2026-11-06); 2026-01..2026-03 | - | 2026-11-13 |
| tax P&L | RealizedSummary | 4 | FY2025-26..FY2026-27 (FY2026-27 to 2026-11-06) | - | 2026-11-06 |
| trade confirmation | TradeConfirmation | 2 | 2025-04-01..2026-11-13 (2 cumulative exports) | - | 2026-11-13 |

## Income Tax Site
Files per tax folder: FY2015-16 1, FY2016-17 1, FY2017-18 1, FY2018-19 1, FY2019-20 2, FY2020-21 1, FY2021-22 5, FY2022-23 5, FY2023-24 5, FY2024-25 5, FY2025-26 11, FY2026-27 4.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| AIS/TIS/26AS | 26AS | 14 | FY2015-16..FY2025-26 | - | FY2025-26 |
| AIS/TIS/26AS | AIS | 14 | FY2021-22..FY2026-27 | - | FY2026-27 |
| AIS/TIS/26AS | Foreign assets (portal) | 2 | CY2022..CY2023 | - | CY2023 |
| AIS/TIS/26AS | TIS | 7 | FY2021-22..FY2026-27 | - | FY2026-27 |
| ITR | Form 67 | 1 | FY2025-26 | - | FY2025-26 |
| other | Tax challan | 4 | 4 dates, 2021-05-16..2026-11-09 | - | 2026-11-09 |

## INDmoney
Files per tax folder: FY2024-25 10, FY2025-26 15, FY2026-27 8.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| 1042-S | 1042-S | 1 | CY2025 | - | CY2025 |
| holdings | Holdings | 2 | as of 2026-11-15 (2 dates, from 2026-11-08) | - | 2026-11-15 |
| statement | US statement | 28 | 2024-06, 2024-08..2026-10 monthly | 2024-07 | 2026-10 |
| tax P&L | ConsolidatedTaxReport | 3 | FY2025-26..FY2026-27 (FY2026-27 to 2026-11-08) | - | 2026-11-08 |
| tax P&L | TaxOverview | 1 | FY2024-25 | - | FY2024-25 |
| trades export | Trades | 2 | as of 2026-11-15 (2 dates, from 2026-11-08) | - | 2026-11-15 |

## ITR
Files per tax folder: FY2015-16 2, FY2016-17 3, FY2017-18 3, FY2018-19 3, FY2019-20 6, FY2020-21 4, FY2021-22 4, FY2022-23 4, FY2023-24 10, FY2024-25 6, FY2025-26 14.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| ITR | Filed summary | 1 | AY2026-27 | - | AY2026-27 |
| ITR | Form 67 | 6 | AY2024-25..AY2026-27 | - | AY2026-27 |
| ITR | Form 67 revised | 3 | AY2026-27 | - | AY2026-27 |
| ITR | ITR original | 38 | AY2016-17..AY2026-27 | - | AY2026-27 |
| ITR | ITR revised | 11 | AY2020-21, AY2024-25, AY2026-27 | - | AY2026-27 |

## Microsoft
Files per tax folder: FY2024-25 4, FY2025-26 4, FY2026-27 7.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| other | Employer tax computation | 9 | FY2024-25..FY2025-26; 2026-04..2026-10 monthly | - | 2026-10 |
| other | Form 16 / 12BA | 6 | FY2024-25..FY2025-26 | - | FY2025-26 |

## Portfolio

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| other | other | 1 | no period in name | - | - |

## Qualcomm
Files per tax folder: FY2024-25 3.

| Type | Kind | Files | Periods | Gaps | Newest |
|---|---|---|---|---|---|
| other | Employer tax computation | 1 | FY2024-25 | - | FY2024-25 |
| other | Form 16 / 12BA | 2 | FY2024-25 | - | FY2024-25 |

## Other folders (summary only)
- `Bills/`: 2 files
- `Investments/` (top level): 1 file
- `Investments/Gold/`: 6 files
- `Investments/Research/`: 1742 files
- `Salary/Microsoft/`: 32 files, 28 payslips 2024-07..2026-10, 2 EPF passbooks, StockExport 2026-11-08 (RSU vests, read by fidelity.py)
- `Salary/NXP/`: 6 files, 6 EPF passbooks
- `Salary/Qualcomm/`: 39 files, 26 payslips 2019-07..2021-08, 8 EPF passbooks
- `Tax/Employer document checklists/`: 2 files
