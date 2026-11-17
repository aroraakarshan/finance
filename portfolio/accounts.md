# Accounts

Gaps in documents before Oct 2019 are not chased.

The user: "I did not have trade before Oct 2019". Earlier acquisitions in the data are
employer-plan acquisitions (ESPP purchases, RSU releases), not trades of his own.
Account numbers: last 4 digits only. Checked 2026-11-15 against the files named below.

| Account / broker | Market | Opened / first activity | Closed / moved | How shares came in | Notes |
|---|---|---|---|---|---|
| ETrade (Morgan Stanley), Qualcomm plan, ending 7855 | US (QCOM) | First RSU release 2019-08-19 (employer plan, not a trade) | Emptied; 761 QCOM moved to IBKR Dec 2025 (ACATS in 2025-12-16 and 2025-12-19) | RSU, ESPP, dividend reinvestment; sell-to-cover at release | `scripts.brokers.etrade` |
| ETrade (Morgan Stanley), NXP plan, ending 8803 | US (NXPI) | ESPP purchase 2019-02-28 (employer plan, not a trade) | Emptied; 13 NXPI moved to IBKR 2025-12-08, fraction 0.575 sold 2025-12-09 | ESPP | `scripts.brokers.etrade` |
| Fidelity (NetBenefits), Microsoft plan, ending 4972 | US (MSFT) | Statements from 2024-07-22; first acquisition ESPP 2024-12-31 | Open | RSU (net shares), ESPP; no sales yet | `scripts.brokers.fidelity`. Filed CY2025 Schedule FA shows opening 2025-03-31; statements start 2024-07-22 and the first ESPP is 2024-12-31 (CY2024 FA has no Fidelity row): both dates noted, CA to fix (`legal/compliance/schedule-fa.md#status-per-account-and-calendar-year`) |
| INDmoney (broker Alpaca) | US | First trade 2024-08-07 | Open; transfer to IBKR planned (`portfolio/migration-indmoney-to-ibkr.md`) | Own buys | `scripts.brokers.indmoney` |
| Interactive Brokers, ending 4563 | US | First activity 2025-12-08 (ACATS in of NXPI from ETrade); first trade 2025-12-11. Opening date not in the statements: the CY2025 Activity Statement starts at NAV 0 with no entry before 2025-12-08; 2025-04-01 is only the start of the exported trade confirmation range, not the opening. Filed CY2025 Schedule FA date 2025-12-08 matches the first activity | Open | Own buys; shares moved in from ETrade (Dec 2025); IBKR stock award for a cash deposit (Dec 2025) | `scripts.brokers.ibkr`. Statements show Interactive Brokers LLC, account type Individual, capabilities Cash |
| AngelOne | India: stocks, ETFs, mutual funds | Opening date not recorded; tax documents in Drive from FY2024-25 | Open | Own buys, SIPs | `scripts.brokers.angelone` (file password) |

Drive `Finance/Banking/` (checked 2026-11-15) holds 23 HDFC card statements (Dec 2024 - Oct 2026),
savings statements (Apr 2025 - 14 Nov 2026), an FD summary and TDS/16A files (`income/cost-cuts.md`).
Gap: no LRS/remittance records (needed for the LRS check in `legal/compliance/fema-lrs.md#reporting-and-lrs-use-per-fy`).
