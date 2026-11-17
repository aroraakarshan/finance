# Staged sales: Rs 2 Cr step, MSFT timing, rupee rate and advance tax

## Summary

- Same long-term rate (14.95%) in both years: staging QCOM only defers tax and keeps each year under Rs 2 Cr (about Rs 70 L of room left in 2026-27).
- Advance tax (specific identification, after the 2026-27 losses): pay about Rs 1,53,600 by 15 Dec 2026 (incl. Rs 1,09,400 for QCOM parts 1-3) and about Rs 1,91,400 by 15 Mar 2027; sell part 4 on 16-18 Dec so its Rs 81,000 waits for 15 Mar (section 5).
- MSFT (user decision 17 Nov: the actual lot sold counts): sell each new vest at once by choosing that lot - the 17 Nov sale of 10.9 sh of the 15 Nov vest is a small ST loss (about Rs 18,155, tax 0, provisional); sell older lots as each turns long-term (3.6).
- Sale value uses the SBI TT buying rate of the last day of the month before the sale (31 Oct 2026 = 94.36).

Part of [employer stock](index.md); section numbers as in the index. Written 2026-11-15 by `finance-tax`. Plan only; no orders.

## 2. The Rs 2 Cr step

The surcharge rate is set by total income including capital gains. Above Rs 2 Cr the surcharge on
slab income (salary, interest, dividends, STCG) goes from 15% to 25%; on LT gains it stays capped at 15%.

| 2026-27 figure | Amount |
|---|---|
| Slab tax on Rs 1.13 Cr | Rs 29.83 L |
| Extra cost of crossing Rs 2 Cr (10% more surcharge on Rs 29.83 L, plus cess) | **Rs 3.10 L at once** |
| Marginal relief band: tax above Rs 2 Cr cannot exceed the income above Rs 2 Cr | first about Rs 3.48 L over Rs 2 Cr is taxed at about 104% |
| LT gain that fits under Rs 2 Cr | about Rs 86.6 L |
| All employer stock at today's prices (QCOM 761 sh 38.38 L, [qcom-lots.md](qcom-lots.md) 3.2 + MSFT 7.45 L) | Rs 45.8 L -> total about Rs 1.59 Cr |

So no plan below reaches Rs 2 Cr. If a price jump ever brings a year near it, move part of the sale
past 31 Mar rather than cross by a little: crossing by Rs 1 L costs Rs 1.04 L of tax.

## 3. Staged sales vs hold (MSFT; QCOM in [qcom-lots.md](qcom-lots.md))

### 3.6 MSFT

User decision 17 Nov 2026: specific identification for foreign shares at foreign brokers
([qcom-lots.md](qcom-lots.md) 3.3). So a sale is of the lot you choose at Fidelity (Specific Shares; FIFO is
only the fallback if the officer disagrees).

| MSFT sale | Lot | Tax |
|---|---|---|
| A new vest, sold at once | that vest lot | small ST gain or loss: price move since the vest plus the rupee gap (vest-date rate vs month-end rate before the sale) |
| Older lots | each lot on or after its LT date (acquisition + 24 months + 1 day), table below | 14.95% |

Sold 17 Nov 2026: 10.9 sh of the 15 Nov 2026 vest lot (Fidelity dates the lot 16 Nov 2026; cost basis $523.88/sh = vest FMV). Figures provisional until the confirmation's fill price.

| Item | Value | Source |
|---|---|---|
| Vest FMV | $523.88 = Nasdaq close Fri 13 Nov 2026 | Microsoft uses the close of the last trading day before the vest date: every vest in the stock export matches it (2025-08-15 vest = 14 Aug close 522.48; 2025-11-15 = 14 Nov close 510.18; 2026-02-15 = 13 Feb close 401.32; 2026-08-15 = 14 Aug close 495.40). The export dates the lot on the settlement day (16 or 17 Nov) |
| Net shares | about 11.541 (18 gross less 6.459 withheld, as for the earlier on-hire vests) | not yet in the stock export; check the release confirmation |
| INR cost | 523.88 x 93.80 (SBI TT buying 13 Nov, last rate before Sun 15 Nov) = Rs 49,140/sh | the payslip's INR perquisite is better evidence; at 94.36 (r.206 Sl.1, 31 Oct) it would be Rs 49,433/sh |
| Sale value | $502.84 (yfinance 2026-11-17, intraday) x 94.36 (31 Oct, r.206 Sl.6) = Rs 47,448/sh | actual fill price on the confirmation |
| Result for 10.9 sh | Proceeds about $5,484 x 94.36 = Rs 5,17,470; cost 10.9 x $523.88 = $5,710.29 x 93.80 = Rs 5,35,625: **ST loss about Rs 18,155** (provisional until the confirmation's fill price); at 93.60 (16 Nov) Rs 17,013, at 94.36 (payroll rule) Rs 21,353; **tax 0** | the loss meets the QCOM LT gain (section 5): about Rs 2,714 less tax (range Rs 2,543-3,192) |
| Same 10.9 sh under FIFO (fallback; at $501.57) | ESPP 2024-12-31: 5.489 + 2025-03-31: 5.411, ST gain about Rs 1,45,900, tax about Rs 52,300 | `lots/msft.py` |

Fidelity steps (every MSFT sale):

| Step | What |
|---|---|
| 1 | On the sell order choose the lot method "Specific Shares" and pick the lot (17 Nov: the 15 Nov 2026 vest, dated 16 Nov by Fidelity, 10.9 sh, cost $523.88); older lots per the table below |
| 2 | If the ticket offers no lot choice, call Fidelity Stock Plan Services before the trade settles (next US business day) to name the lot; a lot named after settlement does not count for Fidelity's records |
| 3 | Check the trade confirmation (or the closed-lot / realized gain view) shows that lot's acquisition date and cost; keep it with the vest release confirmation |

Fidelity's help pages could not be read (fidelity.com returned 403/400 on 2026-11-17), so the exact screen
names above are not verified; "Specific Shares" is the name the user gave.

Older lots (MSFT $501.57, yfinance 2026-11-17 12:16 ET; sale rate 93.60 estimate; cost = FMV x SBI TT on the
acquisition date). Plan: sell each lot on or after its LT date; 10.9 sh of the 15 Nov 2026 vest were sold on 17 Nov (any remainder of that lot is a new ST lot).

| LT from | Lot | Tax year | Shares | Gain (INR) | LT tax | Tax if sold now (ST) |
|---|---|---|---|---|---|---|
| 2027-01-01 | ESPP 2024-12-31 | 26-27 | 5.4894 | 60,574 | 9,056 | 21,734 |
| 2027-04-01 | ESPP 2025-03-31 | 27-28 | 6.1458 | 92,192 | 13,783 | 33,079 |
| 2027-07-01 | ESPP 2025-06-30 | 27-28 | 4.6427 | 21,434 | 3,204 | 7,691 |
| 2027-08-16 | RSU 2025-08-15 | 27-28 | 48.847 | 70,265 | 10,505 | 25,211 |
| 2027-11-18 | RSU 2025-11-17 | 27-28 | 11.541 | 21,782 | 3,256 | 7,815 |
| 2027-12-02 | RSU 2025-12-01 | 27-28 | 1.282 | 3,859 | 577 | 1,385 |
| 2028-02-18 | RSU 2026-02-17 | 27-28 | 11.541 | 1,23,573 | 18,474 | 44,338 |
| 2028-03-03 | RSU 2026-03-02 | 27-28 | 1.112 | 12,484 | 1,866 | 4,479 |
| 2028-05-16 | RSU 2026-05-15 | 28-29 | 11.541 | 90,077 | 13,467 | 32,320 |
| 2028-06-02 | RSU 2026-06-01 | 28-29 | 1.923 | 8,545 | 1,278 | 3,066 |
| 2028-08-18 | RSU 2026-08-17 | 28-29 | 11.541 | -1,916 | 0 | 0 |
| 2028-09-01 | RSU 2026-08-31 | 28-29 | 1.282 | -2,292 | 0 | 0 |
| Total (without the 15 Nov 2026 vest, sold 17 Nov) | | | 116.888 | 5,00,579 | **75,466** (loss lots 0) | 1,81,117 |

The Jan 2027 lot is LT from 1 Jan 2027 (tax about Rs 9,100 in 2026-27 if sold Jan-Mar).
Lots and FMVs: `fidelity.holdings()` (2026-11-17).

Year totals with this plan (specific identification; 16-17 Nov inputs): 2026-27 LT gain about Rs 15.78 L
(QCOM sale 1 + MSFT Jan lot) and an MSFT ST loss of about Rs 18,155 (provisional); tax about Rs 2,35,900 before the loss
set-off (about Rs 2,20,100 after, section 5); income about Rs 1.30 Cr, about Rs 70 L under Rs 2 Cr. 2027-28 LT
gain about Rs 14.0 L (QCOM sale 2 + MSFT lots LT from Apr 2027 to Mar 2028), tax about Rs 2,09,300 (income about
Rs 1.3 Cr if salary stays about Rs 1.06 Cr - not known yet). Both far under Rs 2 Cr.

## 4. Rupee rate

| Leg | Rate | Rule |
|---|---|---|
| Sale value | SBI TT buying rate on the last day of the month before the sale month: Nov 2026 sale -> 31 Oct 2026 = **94.36**; Dec sale -> 30 Nov 2026; Apr 2027 sale -> 31 Mar 2027 (both unknown; 93.60 = SBI 16 Nov used from 17 Nov; 93.80 in the 13 Nov tables) | r.206(1), Table Sl.6; TT buying rate defined in r.207(3)(b) as the State Bank of India's rate (1961 Rule 115) |
| Cost (QCOM) | FMV taxed as perquisite, in INR. Best evidence: the INR perquisite in Form 16 / payslip (none found for 2019-2024). Used: SBI TT buying on the acquisition date. The salary rule (r.206 Sl.1: last day of the month before) would add only Rs 8,769 to the total cost | AF s.73(1) Table Sl.4 (1961 s.49(2AA)) |
| FBIL / RBI reference rate | The rules name SBI's TT buying rate, not FBIL. FBIL's reference rate (RBI archive) is a market mid rate and only a proxy where SBI's rate is missing. Market rates (yfinance) were 0.2-0.8% above SBI TT buying on the dates checked | here only the 2019-08-19 lot (7 sh) uses yfinance 71.13: the SBI archive starts Jan 2020; effect under Rs 100 of tax |
| Source | SBI daily card rates archive (GitHub sahilgupta/sbi-fx-ratekeeper, CSV fetched 2026-11-15); 31 Oct 2026 = 94.36 matches INDmoney's tax report | MSFT and ESPP figures still use yfinance 94.03 |

## 5. Losses and advance tax (2026-27)

- Set-off: 2026-27 losses (about Rs 3.71 L: INDmoney to 9 Nov -2,16,582, all silver incl. ABSL -1,18,047 (user decision 16 Nov;
  ETFs 16 Nov close, FoFs NAV 13 Nov; `../angelone-metals-and-mf-exits.md` section 3A), SCLX + IONQ
  -35,209, MF ST -963; 13 Nov prices) offset QCOM sale 1 directly once the NXPI gain (Rs 2,76,457) and
  the INDmoney fraction gains (about +7,155) are used: about Rs 87,200 meets QCOM. The 17 Nov MSFT sale of
  the new vest (17 Nov, 10.9 sh) adds an ST loss of about Rs 18,155 (3.6; provisional until the fill price), so about Rs 1,05,400
  meets QCOM, saving about Rs 15,750 (14.95%). Nothing carries forward. QCOM sale 1 tax (qcom-lots.md 3.4, 16 Nov inputs): Rs 2,26,828
  before losses, about Rs 2,11,000 after (FIFO fallback Rs 3,28,245 / about Rs 3,12,400). SMNR/SYRS, if
  sold at IBKR by 31 Mar 2027, save about Rs 5,200 more (`tax/migration-indmoney-to-ibkr.md` section 3.5).
- AF s.404 (1961 s.208): advance tax if tax after TDS is Rs 10,000 or more. AF s.408 (1961 s.211):
  15%/45%/75%/100% by 15 Jun/Sep/Dec/Mar. AF s.425(1) (1961 s.234C): 1% a month on a shortfall
  (3 months for Jun/Sep/Dec, 1 for Mar). AF s.425(4) (1961 s.234C proviso): no interest on a shortfall
  caused by capital gains if their full tax is paid "in any of the remaining instalments ... or by
  the 31st day of March". The ITR Schedule 234C splits gains by the period they arise, so a gain on
  16 Sep - 15 Dec is counted in the 15 Dec instalment (75% of its tax due then) and a gain on 16 Dec -
  15 Mar only in the 15 Mar instalment (safe reading).

Base (no QCOM): `tax/FY2026-27/fd-and-advance-tax.md` section 5 planning, Rs 1,50,000 paid 9 Nov 2026. QCOM
tax by part from [qcom-lots.md](qcom-lots.md) 3.4 (specific identification, 16 Nov inputs).

| Item | Pay by 15 Dec 2026 | Pay by 15 Mar 2027 |
|---|---|---|
| Base: FD/savings interest, dividends, NXPI net gain | about Rs 63,500 | about Rs 71,200 |
| QCOM P1-P3 sold by 11 Dec (tax Rs 1,45,858) | **+ Rs 1,09,400** (75%) | + Rs 36,500 (25%) |
| QCOM P4 sold 16-18 Dec (tax Rs 80,970) | 0 | + Rs 81,000 |
| MSFT: 17 Nov new-vest sale (loss) | 0 | 0 |
| MSFT Jan lot (LT from 1 Jan 2027), if sold Jan-Mar | 0 | + Rs 9,100 |
| Total before the Nov-Dec losses | about Rs 1,72,900 | about Rs 1,97,800 |
| Losses: all silver, SCLX + IONQ, MF ST, MSFT new vest (tax Rs 25,670 less: NXPI base 9,915 + QCOM 15,750), 75% / 25% | - Rs 19,300 | - Rs 6,400 |
| **Total, plan** | **about Rs 1,53,600** | **about Rs 1,91,400** |
| If P4 is sold 14-15 Dec instead | + Rs 60,700 | - Rs 60,700 |
| For comparison: QCOM at FIFO (fallback) | about Rs 2,28,700 | about Rs 2,17,700 |

The losses row includes the silver effect on the base (fd note: Rs 56,000 / Rs 68,700). Sell P4 on 16-18 Dec, not
14-15 Dec, so its tax moves to 15 Mar with no interest.
Alternative: declare the gain to payroll in Form No. 122 (r.204; AF s.392(4)(a)(iv), ex Form 12BAA,
s.192(2B)) so salary TDS for Dec-Mar covers it; ask payroll if they accept capital gains.
