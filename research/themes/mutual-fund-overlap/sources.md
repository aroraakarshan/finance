# Mutual fund overlap: sources and revision history

## Summary
- Main data source is Groww fund pages [G], cross-checked with Kuvera [K], AMFI [A], mfapi [M] and PPFAS [P].
- Tax figures come from finance-tax's lot-level note [TX]; holdings from the AngelOne export of 2026-11-07.
- Four versions on 2026-11-15: first draft, second (two denominators, tax from [TX]), third (total Rs 2,26,82,726), fourth (total Rs 2,83,13,674 incl. HDFC bank), fifth (Rs 2,97,58,520 incl. physical gold, FD interest), sixth (Rs 4,20,97,035 incl. Punjab Gramin Bank, EPF).

Back to the index: [mutual-fund-overlap.md](../mutual-fund-overlap.md). Section numbers (0-6) are kept from the original note; sources [G], [K], [A], [M], [P], [T], [TX] are in [sources.md](sources.md).

Written 2026-11-15. Holdings as of 2026-11-07 (AngelOne_MF_Holdings_2026-11-07.xlsx, read with
`scripts.brokers.angelone.mutual_funds()`). Total MF value Rs 20,49,769 in 15 funds. This is research
and a proposal, not an order. Nothing has been bought or sold.

**Updated 2026-11-15 (second version).** What changed:
- Denominators. Percentages are now shown on two bases: % of AngelOne (Rs 26,24,910, 8 Nov) and % of
  total investments (now Rs 2,26,82,726 = US $213,304 x 94.0338 + AngelOne; [portfolio/summary.md](../../../portfolio/summary.md),
  commit 21a4c78). The first version assumed about $15k in US stocks; the real US figure is
  about Rs 2.01 Cr = 88.4% of total, with QCOM + MSFT 79.8% (Rs 1,81,00,087 from
  [employer-stock-concentration/concentration.md](../employer-stock-concentration/concentration.md) over the new total).
  So the whole MF book is 78.1% of AngelOne but only 9.0% of total.
- Tax and exit loads. My own estimates (Rs 0 to 4,500) are replaced by the lot-level figures in
  [tax/angelone-metals-and-mf-exits.md](../../../tax/angelone-metals-and-mf-exits.md) (finance-tax, 2026-11-15), cited by section. Lot dates are
  now known from AngelOne MF transaction files, so section 0's inference is superseded.
- The fund choice is unchanged; its priority is lower (section 6).

**Updated 2026-11-15 (third version, total base).** [portfolio/summary.md](../../../portfolio/summary.md) (commit 21a4c78) now counts
INDmoney wallet cash ($4,574.05; INDmoney $14,653). New total Rs 2,26,82,726 (was Rs 2,23,19,002),
US $213,304 (was $209,436) x 94.0338 = Rs 2,00,57,786 = 88.4% of total. AngelOne unchanged
(Rs 26,24,910), so % of AngelOne is unchanged. Every "% of total" below is recomputed on the new total
(values as of 13 Nov close for US, 7-8 Nov for AngelOne; wallet cash 15 Nov). Shares fall by about 1.6%
of themselves (e.g. MF book 9.18% -> 9.04%, QCOM + MSFT 81.1% -> 79.8%). No conclusion changes.

## Sources used (all fetched 2026-11-15)
- [G] Groww fund pages `https://groww.in/mutual-funds/<slug>` (page JSON): total and base expense ratio
  with as-of date, AUM, benchmark, exit load and its history, full portfolio. Slugs: see table 1.
- [K] Kuvera mirror `https://mf.captnemo.in/kuvera/<ISIN>`: second source for direct-plan TER.
- [A] AMFI NAV file `https://portal.amfiindia.com/spages/NAVAll.txt` (NAV date 13-Nov-2026): plan of each ISIN.
- [M] NAV history `https://api.mfapi.in/mf/<scheme code>` (Nov 2023 to Nov 2026).
- [P] PPFAS scheme page `https://amc.ppfas.com/schemes/parag-parikh-flexi-cap-fund/` (exit load).
- [T] Income Tax Dept `https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1`
  (AY 2026-27, Sec 112A exemption Rs 1,25,000; page updated 09-Jul-2026).
- AMC factsheets, valueresearchonline and moneycontrol were tried; ICICI AMC is a JS app and VRO /
  moneycontrol blocked the script, so [G] is the main source. Spot checks: [K] TERs agree with [G]
  within 0.07%; PPFAS exit load in [G] matches [P].
- [TX] [tax/angelone-metals-and-mf-exits.md](../../../tax/angelone-metals-and-mf-exits.md) (finance-tax, 2026-11-15), cited by section number.

**Updated 2026-11-15 (fourth version, bank added).** `portfolio/summary.md` commit 1a65a2e adds HDFC
savings Rs 8,54,314 (13 Nov) and 9 FDs Rs 47,76,634 principal (6.25%, 10 May 2026 -> 10 May 2027, interest
accrued not counted). New total Rs 2,83,13,674 (was Rs 2,26,82,726). AngelOne unchanged, so % of AngelOne
and all decided amounts are unchanged. Every "% of total" is recomputed:

| Measure | Rupees | Third version | Fourth version |
|---|---|---|---|
| US-situs ($213,304) | 2,00,57,786 | 88.4% | 70.8% |
| QCOM + MSFT | 1,81,00,087 | 79.8% | 63.9% |
| Semiconductors (QCOM, AVGO, NVDA) | 1,27,82,985 | - | 45.2% |
| All US single stocks | 1,95,52,982 | 86.2% | 69.1% |
| US tech (incl. GOOGL) | 1,90,48,070 | 84.0% | 67.3% |
| HDFC savings + FDs | 56,30,947 | - | 19.9% |
| AngelOne | 26,24,910 | 11.6% | 9.27% |
| MF book | 20,49,769 | 9.04% | 7.24% |
| Equity MFs after the switch | 14,90,317 | 6.57% | 5.26% |
| 7 exits (7 Nov) | 5,20,728 | 2.30% | 1.84% |
| All metals | 8,29,676 | 3.66% | 2.93% |

Rupee values for QCOM/MSFT, semis, single stocks and US tech are from
[employer-stock-concentration/concentration.md](../employer-stock-concentration/concentration.md) (13 Nov close).
Conclusions unchanged: the MF switch is still a tidy-up; QCOM + MSFT is still the main risk; metals stay
below the 5-15% guideline. One new point: the arbitrage parking role is covered by the bank money (plan.md).

**Updated 2026-11-15 (fifth version, gold and FD interest).** `portfolio/summary.md` commit 7d88cf8 adds
physical gold Rs 12,90,192 (109.1 g, IBJA rate 2026-11-13) and FD accrued interest (FDs now Rs 49,31,288,
2026-11-15). New total Rs 2,97,58,520 (was Rs 2,83,13,674). % of AngelOne and decided amounts unchanged.

| Measure | Rupees | Fourth version | Fifth version |
|---|---|---|---|
| US-situs ($213,304) | 2,00,57,786 | 70.8% | 67.4% |
| QCOM + MSFT | 1,81,00,087 | 63.9% | 60.8% |
| Semiconductors (QCOM, AVGO, NVDA) | 1,27,82,985 | 45.2% | 43.0% |
| All US single stocks | 1,95,52,982 | 69.1% | 65.7% |
| US tech (incl. GOOGL) | 1,90,48,070 | 67.3% | 64.0% |
| HDFC savings + FDs | 57,85,602 (was 56,30,947) | 19.9% | 19.4% |
| Physical gold | 12,90,192 | - | 4.34% |
| AngelOne | 26,24,910 | 9.27% | 8.82% |
| MF book | 20,49,769 | 7.24% | 6.89% |
| Equity MFs after the switch | 14,90,317 | 5.26% | 5.01% |
| 7 exits (7 Nov) | 5,20,728 | 1.84% | 1.75% |
| AngelOne metals | 8,29,676 | 2.93% | 2.79% |
| All metals incl. physical gold | 21,19,868 | - | 7.12% |

One conclusion changes: metals including physical gold are 7.12% of total, inside the 5-15% guideline
(before: below it). The decision stays with silver-gold.md (your decision 16 Nov: all silver sold, no extra
gold; metals after the plan = gold only, about 3.5% of total). MF conclusions unchanged.

**Updated 2026-11-15 (sixth version, Punjab Gramin Bank and EPF).** `portfolio/summary.md` commit 0dd3a98
and later adds Punjab Gramin Bank FDs Rs 72,00,000 and savings Rs 10,00,000 (both user estimates,
2026-11-15) and EPF Rs 41,03,127 (passbooks 2026-08-19, locked). USD/INR is now 94.1997 (was 94.0338), so
US rupee values are recomputed from the dollar amounts. New total Rs 4,20,97,035 (was Rs 2,97,58,520).
% of AngelOne and decided amounts unchanged.

| Measure | Rupees | Fifth version | Sixth version |
|---|---|---|---|
| US-situs ($213,304) | 2,00,93,203 | 67.4% | 47.7% |
| QCOM ($131,250) | 1,23,63,711 | - | 29.4% |
| QCOM + MSFT ($192,485) | 1,81,32,029 | 60.8% | 43.1% |
| Semiconductors ($135,940) | 1,28,05,507 | 43.0% | 30.4% |
| All US single stocks ($207,936) | 1,95,87,509 | 65.7% | 46.5% |
| US tech incl. GOOGL ($202,566) | 1,90,81,656 | 64.0% | 45.3% |
| HDFC + Punjab Gramin Bank savings and FDs | 1,39,85,602 | 19.4% (HDFC only) | 33.2% |
| EPF (locked) | 41,03,127 | - | 9.75% |
| Physical gold | 12,90,192 | 4.34% | 3.06% |
| AngelOne | 26,24,910 | 8.82% | 6.24% |
| MF book | 20,49,769 | 6.89% | 4.87% |
| Equity MFs after the switch | 14,90,317 | 5.01% | 3.54% |
| 7 exits (7 Nov) | 5,20,728 | 1.75% | 1.24% |
| AngelOne metals | 8,29,676 | 2.79% | 1.97% |
| All metals incl. physical gold (7-8 Nov) | 21,19,868 | 7.12% | 5.04% |

Conclusions: MF ones unchanged (the switch is a tidy-up; QCOM + MSFT, now 43.1%, is still the main risk).
Metals move to the low end of the 5-15% band; the user decided 15 Nov to hold gold at 5% of the new total
(portfolio/plan.md), which silver-gold.md owns; replaced by your decision 16 Nov: no extra gold, gold about
3.5% (band 3-6%), all silver sold, metals after the plan 3.53%. Liquid bank money is now 33.2% of total, so the arbitrage
parking role matters even less; EPF is in the total but not liquid.

