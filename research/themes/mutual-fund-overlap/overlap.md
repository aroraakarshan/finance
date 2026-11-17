# Mutual fund overlap: pair overlaps and category exposure

## Summary
- Near-duplicates: SBI PSU vs ABSL PSU 61%, UTI Nifty 50 vs ICICI Large Cap 66%; mid caps overlap 18-31%.
- PSU/infra funds are Rs 1.72 L = 6.6% of AngelOne but 0.41% of total; PSU look-through 0.58% of total.
- The whole MF book is 78.1% of AngelOne but 4.87% of total (Rs 4,20,97,035).

Back to the index: [mutual-fund-overlap.md](../mutual-fund-overlap.md). Section numbers (0-6) are kept from the original note; sources [G], [K], [A], [M], [P], [T], [TX] are in [sources.md](sources.md).

## 2. Overlap (computed from full portfolios in [G])
Method: overlap = sum over common stocks of min(weight in A, weight in B), equity lines only, names
normalised. Portfolio months: 2026-10-31 for ICICI LC, NN50, HDFC MC, SBI PSU, Nippon, ABSL PSU, Quant;
2026-09-30 for Invesco MC, Invesco PSU, LIC Infra, UTI N50, PPFAS. Different months add small error.

| Pair | Overlap | Common stocks | Read |
|---|---|---|---|
| SBI PSU vs ABSL PSU | 61% | 19 | near duplicates (SBI 16-17%, NTPC, Power Grid top in both) |
| SBI PSU vs Invesco PSU | 42% | 10 | high |
| Invesco PSU vs ABSL PSU | 36% | 16 | high |
| LIC Infra vs PSU funds | 5-11% | 5-7 | low; but LIC Infra vs UTI N50 is 23% |
| HDFC MC vs Nippon Midcap 150 | 31% | 41 | moderate (same benchmark) |
| HDFC MC vs Invesco MC | 20% | 13 | moderate |
| Invesco MC vs Nippon Midcap 150 | 18% | 21 | moderate |
| Mid caps vs Quant Small Cap | 1-4% | 3-9 | low |
| UTI Nifty 50 vs ICICI Large Cap | 66% | 41 | high; ICICI costs 0.75%/yr more |
| UTI Nifty 50 vs PPFAS | 38% | 31 | moderate |
| ICICI Large Cap vs PPFAS | 33% | 30 | moderate |
| Nifty Next 50 vs ICICI Large Cap | 13% | 21 | low |
| Nifty Next 50 vs UTI Nifty 50 / PPFAS | 1% / 4% | 1 / 7 | none (different index by design) |

Look-through of the whole MF book (equity lines, weighted by your value): about 67% stocks; top names
HDFC Bank 2.6%, ICICI Bank 2.1%, Power Grid 1.4%, SBI 1.35%, ITC 1.2% of the MF book. Government-owned
companies (PSU banks, power, defence, oil, coal, rail; my list) are about Rs 2.4 L = 12% of the MF book
and about 18% of its stock exposure (UTI N50 holds SBI at 3.8%). On the two bases: Rs 2.4 L = 9.3% of
AngelOne, 0.58% of total. PPFAS foreign stocks (about 9% of PPFAS, Rs 0.32 L) = 0.08% of total, so they
add almost nothing to the 45% US-tech exposure ($202,566 x 94.1997 = Rs 1,90,81,656 over the new total; [employer-stock-concentration/concentration.md](../employer-stock-concentration/concentration.md)).

**Thematic risk:** the 3 PSU funds + infra fund = Rs 1.72 L (8.4% of MF book, 6.6% of AngelOne,
0.41% of total). Inside the Indian book it matters; at the total level it is small. PSU stocks move together on one
driver (government policy, divestment, capex cycle, rate cycle for PSU banks) and are cyclical.
Worst fall in direct-plan NAV since 2013 [M]: SBI PSU -47% (Nov 2017 -> Mar 2020, more than 2 years
down before Covid), LIC Infra -40%, Invesco PSU -33%, vs UTI Nifty 50 -38% (Jan -> Mar 2020).
Holding three funds with the same benchmark (BSE PSU TRI) adds no diversification, only cost and paperwork.

## 3. Category exposure of the MF book (2026-11-07 values)
| Bucket | Funds | Rs | % MF book | % AngelOne | % total |
|---|---|---|---|---|---|
| Large cap (Nifty 50 + active large) | UTI N50, ICICI LC | 2,64,517 | 12.9 | 10.1 | 0.63 |
| Next 50 (large-mid) | Kotak NN50 | 1,60,738 | 7.8 | 6.1 | 0.38 |
| Flexi cap | PPFAS | 3,50,728 | 17.1 | 13.4 | 0.83 |
| Mid cap | HDFC MC, Nippon MC150, Invesco MC | 4,88,748 | 23.8 | 18.6 | 1.16 |
| Small cap | Quant SC | 32,733 | 1.6 | 1.2 | 0.08 |
| Thematic PSU/infra | SBI PSU, Invesco PSU, ABSL PSU, LIC Infra | 1,72,415 | 8.4 | 6.6 | 0.41 |
| Arbitrage (parking) | Kotak Arb | 3,02,337 | 14.8 | 11.5 | 0.72 |
| Metals FoF | Silver FoF, Gold-Silver FoF | 2,77,554 | 13.5 | 10.6 | 0.66 |
| Total MF | 15 | 20,49,770 | 100 | 78.1 | 4.87 |

Whole portfolio ([portfolio/summary.md](../../../portfolio/summary.md), commit 0dd3a98 and later; total Rs 4,20,97,035 incl. HDFC + Punjab Gramin Bank savings and FDs
Rs 1,39,85,602 = 33.2% (Punjab Gramin Bank Rs 82 L are estimates), EPF Rs 41,03,127 = 9.75% (locked), physical gold
Rs 12,90,192 = 3.06%; USD/INR 94.1997): US single stocks
46.5% of total, QCOM + MSFT 43.1% (QCOM 29.4%), semiconductors (QCOM, AVGO, NVDA) 30.4% (rupee values from [employer-stock-concentration/concentration.md](../employer-stock-concentration/concentration.md)); Indian equity MFs (the 6 rows above minus arbitrage and metals) Rs 14.70 L = 56.0% of AngelOne
but only 3.49% of total. AngelOne metals (2 FoFs + silver ETFs) Rs 8,29,676 = 31.6% of AngelOne, 1.97% of
total; with physical gold, all metals Rs 21,19,868 = 5.04% of total - see [silver-gold.md](../silver-gold.md) (that note owns the metals decision).
