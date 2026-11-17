# Employer stock concentration: how much is in QCOM, MSFT and US tech

## Summary
QCOM (former employer) is 29.4% and MSFT (current employer) 13.7% of the total: 43.1% together
(79.8% of the broker accounts alone). US tech is 45.3%, semis 30.4%.
238 unvested MSFT shares (about Rs 1.17 Cr gross) come on top.
What to do: bring each stock under 10% of the total; plan in [plan.md](plan.md).

Back to the index: [employer-stock-concentration.md](../employer-stock-concentration.md). Written 2026-11-15 by `finance-research`;
research only, not advice; no orders placed. "not verified" = could not confirm from a source.

## Numbers (values at the 2026-11-13 close, USD/INR 94.1997, FBIL reference rate via rbi.org.in)

Sources: `portfolio/summary.md` (2026-11-15), `scripts.value` run 2026-11-15, sectors from yfinance `info`
(checked 2026-11-15). Total Rs 4,20,97,035 (summary.md as of 2026-11-15, commit 0dd3a98 and later: adds Punjab Gramin Bank FDs
Rs 72 L and savings Rs 10 L (both user estimates, details pending) and EPF Rs 41,03,127 (passbooks 2026-08-19, locked);
US values now at FBIL 94.1997 instead of yfinance 94.0338. Before that, commit 7d88cf8: physical gold 109.1 g Rs 12,90,192 at
IBJA rate of 2026-11-13; FDs now principal + accrued interest Rs 49,31,288 (accrued Rs 1,54,654); US $213,304 incl. INDmoney $14,653 with
$4,574.05 wallet cash; HDFC savings Rs 8,54,314 (13 Nov) + 9 FDs Rs 47,76,634 principal (6.25%, 10 May 2026
-> 10 May 2027); AngelOne as of 8 Nov). Earlier bases: Rs 2,23,19,002, Rs 2,26,82,726 (= market
investments without HDFC and gold), Rs 2,83,13,674, Rs 2,97,58,520. Last column now = broker accounts only (AngelOne,
INDmoney, IBKR, Fidelity: Rs 2,27,18,113 at 94.1997). Recomputed 2026-11-15.
Base used: the full total, including EPF (locked until retirement or job exit) and the Punjab Gramin Bank estimates.
For concentration they count: they are your wealth and a QCOM fall hits the same net worth. They are not money
that can be moved into funds soon, so the broker-only column shows the share of investable market money.
Savings, FDs and physical gold are your money and dilute single-stock risk, so they count;
the FDs are locked until 10 May 2027 at 6.25% but can be broken early (penalty not checked), so they are
treated as investable, not as spending money.

| Holding / group | USD | INR | Share of total | Share of market investments (Rs 2,27,18,113: brokers only) |
|---|---|---|---|---|
| QCOM 761 (former employer, Qualcomm; ETrade RSU/ESPP/DRIP lots, now at IBKR) | $131,250 | Rs 1,23,63,680 | **29.4%** | 54.4% |
| MSFT 116.888 (current employer, Microsoft; Fidelity) | $61,235 | Rs 57,68,341 | **13.7%** | 25.4% |
| QCOM + MSFT | $192,485 | Rs 1,81,32,020 | **43.1%** | 79.8% |
| Semiconductors: QCOM, AVGO, NVDA | $135,940 | Rs 1,28,05,537 | 30.4% | 56.4% |
| US tech: Technology sector (QCOM, MSFT, AVGO, NVDA, CRWD, IONQ, SHLS) + GOOGL | $202,566 | Rs 1,90,81,675 | 45.3% | 84.0% |
| All US single stocks (above + VRT, IBKR, CEG, TRVI, SCLX, SMNR) | $207,936 | Rs 1,95,87,479 | 46.5% | 86.2% |

- Microsoft is the current employer: `portfolio/accounts.md` (Microsoft plan at Fidelity, RSU vests to
  2026-08-31) and the award export `Salary/Microsoft/Stock/StockExport_2026-11-08.xlsx`. Qualcomm is a
  former employer (ETrade Qualcomm plan, emptied Dec 2025).
- Unvested Microsoft awards (not counted above): 238 shares gross in the export's vest schedule
  (22 in rest of 2026, 93 in 2027, 75 in 2028, 48 in 2029-2031; next 17 on 2026-11-15, 5 on 2026-11-30: 3 FY25 + 2 FY26).
  Grants: on-hire 286 sh over 4 years (ends 15 Aug 2028); FY25 48 sh and FY26 56 sh over 5 years ([pay](../../../income/pay.md)).
  At $523.88 that is $124,683 gross = Rs 1,17,45,143 (at 94.1997). Part is withheld for tax at vest (first vest:
  71 gross -> 48.847 net). With these, total MSFT exposure is about $186k gross, plus the salary itself.
- Not in data (so not in the total): PPF, NPS, VPF beyond the passbooks, EPS pension (Rs 77,500), bank accounts other than
  HDFC and Punjab Gramin Bank, property, insurance. If they exist,
  the shares above are lower. Indian mutual funds (e.g. Parag Parikh Flexi Cap) may hold some US tech;
  look-through not done (not verified).
