# Microsoft ESPP restart: buy and sell at once

## Summary

- The 10% discount nets about USD 71 per USD 1,000 contributed (7.1%) after 35.88% payroll tax.
- User decision 17 Nov 2026: the actual lot sold counts, so sell each purchase the same day choosing that lot (Fidelity "Specific Shares"): gain about 0, net benefit back to about 7.1% (6.1).
- If the officer imposed FIFO (fallback), a same-day sale would be of the oldest MSFT lots: up to Rs 5,100 more tax per USD 1,000 when those are short-term (6.1).
- Report the shares in Schedule FA (Table A3) even if sold the same day; check AIS/26AS for TCS on the remittance.
- Check the payroll FX rate and FMV used for the perquisite on the payslip / Form 16.

Part of [employer stock](index.md). Written 2026-11-15 by `finance-tax`. Plan only; no orders.

## 6. Microsoft ESPP restart: buy and sell at once

Own data (`fidelity.purchases()`, 2026-11-15): purchases on the last trading day of each quarter,
price paid exactly 90% of FMV, FMV = Nasdaq close that day (2024-12-31: paid $379.35, FMV $421.50 =
close; yfinance). So the discount is 10% of the purchase-date close, no look-back.

| Point | Rule |
|---|---|
| Perquisite = FMV - price paid, salary at slab via payroll TDS | AF s.17(1)(d), value per s.17 definition (h) (1961 s.17(2)(vi)); TDS s.392 (1961 s.192) |
| FMV | r.15(6) (1961 Rule 3(8)): average of open and close on a *recognised* (Indian, SCRA s.2(f)) exchange; for a share listed only abroad the text points to a merchant banker. Payroll uses the Nasdaq close (2024-12-31 close 421.50 vs average 423.80). CA |
| Perquisite in INR | Salary: SBI TT buying on the last day of the month before the month it is due (r.206 Table Sl.1). Payroll's actual rate: check the payslip / Form 16 |
| Capital gain on the sale | Sale price - FMV (AF s.73 Table Sl.4); ST at slab 35.88% |
| Rupee mismatch | Sale uses the rate of the last day of the month before the sale month (Sl.6). Same month and payroll on Sl.1 -> same rate, no rupee gain. If payroll uses the purchase-date rate, gain/loss = FMV x (sale-rule rate - payroll rate): Rs 1,111 per Rs 1 gap per $1,000 contributed (tax Rs 399) |
| Timing | Confirmations are dated 1-2 days after purchase (2025-01-02, 04-01, 07-01), so "same day" may be the next trading day. A 31 Mar purchase sold in April falls in the next tax year (31 Mar rate) |

Example per USD 1,000 contributed (USD/INR 94.03, sale at the FMV, fees ignored):

| Item | USD | INR |
|---|---|---|
| Contribution from net salary | 1,000.00 | 94,034 |
| Shares at FMV (1,000 / 0.9) | 1,111.11 | 1,04,482 |
| Perquisite (10% of FMV) | 111.11 | 10,448 |
| Payroll TDS 35.88% | 39.87 | 3,749 |
| Sale at FMV: capital gain | 0 | 0 |
| **Net benefit after tax** | **71.24 (7.1%)** | **6,699** |
| A year at 15% of base pay (Rs 9,79,980, research `espp.md`) | about 742 net | about 69,800 net; TDS about 39,100 |
| Sale 1% below the close | -11.11 ST loss | -1,045 (worth Rs 375 against other gains) |

### 6.1 Same-day sale: which lot

User decision 17 Nov 2026 ([qcom-lots.md](qcom-lots.md) 3.3): the actual lot sold counts. Sell each ESPP
purchase the same day (or the next trading day) choosing that purchase lot at Fidelity ("Specific Shares",
see [staged-sale.md](staged-sale.md) 3.6): cost = FMV, so the gain is about 0 apart from the rupee gap (table
above), and the net benefit is about 7.1% as in the example. Keep the trade confirmation showing the lot.

FIFO fallback, if an officer disagreed: the sale would be of the oldest MSFT lots. Per USD 1,000 contributed
(2.2153 sh at $501.57, yfinance 2026-11-17; SBI TT 93.60):

| Oldest lot left on the sale date | Its gain on 2.2153 sh | Tax if LT (14.95%) | Tax if ST (35.88%) | Extra if ST = loss of benefit |
|---|---|---|---|---|
| ESPP 2024-12-31 (LT from 1 Jan 2027) | 24,445 | 3,655 | 8,771 | 5,116 (5.5% of the contribution) |
| ESPP 2025-06-30 (LT from 1 Jul 2027) | 10,228 | 1,529 | 3,670 | 2,141 (2.3%) |
| RSU 2025-11-17 (LT from 18 Nov 2027) | 4,181 | 625 | 1,500 | 875 (0.9%) |
| RSU 2026-02-17 (LT from 18 Feb 2028) | 23,720 | 3,546 | 8,511 | 4,965 (5.3%) |
| RSU 2026-08-17 or later | about 0 or a loss | 0 | 0 | 0 |

- Oldest lot LT: the tax is on gain payable anyway when that lot is sold; only the timing moves.
- Oldest lot ST: the extra 20.93% on its gain would cut the net benefit to between about 7.1% and 1.6%.
- First purchase under the 1 Jan 2027 offering: 31 Mar 2027 (confirmation 1-2 days later); sold in April it
  falls in tax year 2027-28 at the 31 Mar rate.

Before fees and the month salary waits for the purchase; research `employer-stock-decision/espp.md` nets
those out to about 6.6% (Rs 64,000 a year), less with wire fees or if the dollars come to India.

| Topic | Answer |
|---|---|
| LRS | ESOP/ESPP shares of a foreign employer are OPI; "no limit on the amount ... such remittances shall be reckoned towards the LRS limit" (RBI Master Direction Overseas Investment 2022, para 22(5),(7); employer files Form OPI, OI Regulations reg 10(3)). Counts in the USD 250,000 with IBKR transfers |
| TCS | AF s.394(1) Table Sl.7 (1961 s.206C(1G)): 20% on LRS remittances above Rs 10 L a year (not education/medical). ESPP at 15% (Rs 9.8 L) is just under it alone; with other LRS sends in the same year it may cross (how banks add them up: not verified). Whether Microsoft's bank collects TCS on ESPP remittances: not verified - check AIS/26AS. TCS is credited in 26AS/AIS (claim in the ITR) or declared to payroll in Form No. 122 to cut salary TDS (s.392(4)(a)(v), (4)(b)(ii)) |
| Schedule FA | Calendar year; shares held at any time must be shown even if sold the same day: Table A3 (initial value = FMV, peak, closing 0, sale proceeds), plus the Fidelity account in A2 (already reported for MSFT) |
| US tax | None on the sale for a nonresident alien under 183 days in the US (IRC s.871(a)(2)); W-8BEN on file (Fidelity 1042-S 25% rate), so no withholding; no foreign tax credit needed |
