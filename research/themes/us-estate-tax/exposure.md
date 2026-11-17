# US estate tax: Exposure now

Written 2026-11-15 by `finance-research`. Research only, not tax or legal advice; no orders placed.
Part of [US estate tax](../us-estate-tax.md). Sources read 2026-11-15 unless another date is given; "not verified" = no source confirmed it.
Short names: "IRS page" = https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns ; "i706na" = Form 706-NA instructions, https://www.irs.gov/instructions/i706na (rev. 09/2025).

## Summary
Your US-situs assets are $213,304 now (tax about $46,057, Rs 43.3 L) and $337,987 with unvested
Microsoft awards, which vest at death (tax about $87,716, Rs 82.5 L). Each extra $1 of US assets
costs 34 cents at death. Debts help only pro-rata.

## Details

Updated 2026-11-15 after `legal/estate/foreign-assets.md#us-estate-tax-and-brokers` and `legal/estate/sources.md#discrepancies-found` (unvested awards, INDmoney cash).

| Part | Amount | US-situs? |
|---|---|---|
| US shares: IBKR (QCOM, AVGO, VRT, IBKR) $136,621 + Fidelity MSFT $61,235 + INDmoney/Alpaca $10,079 (2026-11-13 closes, `portfolio/summary.md`) | $207,935 | Yes (2104(a)) |
| USD cash: IBKR $795 (`portfolio/summary.md`) + INDmoney US wallet $4,574.05 (dashboard 15 Nov, `STATUS.md`; $876.96 of it not yet explained there) | $5,369 | Unclear, see broker-cash row in [rule.md](rule.md); counted as US-situs here |
| **Current assets** | **$213,304** | $207,935 to $213,304 depending on the cash question |
| Unvested Microsoft awards: 238 shares (143 On-Hire + 39 FY25 + 56 FY26, "Unvested" column of `StockExport_2026-11-08.xlsx`, matches `research/themes/employer-stock-concentration.md`) x $523.88 (MSFT close 2026-11-13) | $124,683 gross (Rs 1.17 Cr) | Yes: under Microsoft's standard award agreement unvested awards "shall become immediately vested" at death, so they add to the US-situs estate (`legal/estate/foreign-assets.md` s.4.12 and s.7; SEC Exhibit 10.28, https://www.sec.gov/Archives/edgar/data/789019/000156459022035087/msft-ex1028_258.htm). The user's own country addendum was not read |
| **Current + unvested awards** | **$337,987** | |

Notes: the award figure is gross, and gross is the base (finance-legal, legal/estate/foreign-assets.md#awards-that-vest-at-death
lines 211-244, questions E15-E17). Under the MSFT award form (SEC Exhibit 10.28 ss.1(b), 6, 9),
shares withheld for tax count as issued and only pay the holder's tax, so the asset is not reduced.
Indian tax is at best a debt deductible pro rata (26 CFR 20.2106-2) and may not be deductible at all
(20.2053-6(f)). Range: gross, no deduction -> about $87.7k (best supported); 36% Indian tax deducted
pro rata -> about $73.6k; net-shares reading -> about $72.5k. Situs is US either way (unvested award
= Microsoft Corp promise, 2104(c); shares, 2104(a)). 17 award shares were due to vest on 2026-11-15; that only moves
value from "unvested" to Fidelity, no change in the total. AngelOne (Rs 26.2 L) is not US-situs. The
tax note's about $192,500 (QCOM $131,250 + MSFT $61,235) counts only held employer stock
(`tax/investment-types.md` section 4); no conflict, different scope.

Rate table, 26 USC 2001(c): up to 10k 18%; 10-20k 20%; 20-40k 22%; 40-60k 24%; 60-80k 26%;
80-100k 28%; 100-150k 30%; 150-250k 32%; 250-500k 34%; 500-750k 37%; 750k-1M 39%; above 1M 40%.

Tax = tentative tax on taxable estate - $13,000 credit.
- Current assets $213,304: $38,800 + 32% x ($213,304 - $150,000) = $38,800 + $20,257 = $59,057;
  less $13,000 -> **tax about $46,057 (21.6%), about Rs 43.3 L**. (Shares only, $207,935: $44,339.)
- Current + unvested awards $337,987: $70,800 + 34% x ($337,987 - $250,000) = $70,800 + $29,916 =
  $100,716; less $13,000 -> **tax about $87,716 (26.0%), about Rs 82.5 L**.
- Each extra $1 of US-situs assets now costs 34 cents at death (with the awards; 32 cents without).

| US-situs estate | Tentative tax | Tax after $13,000 credit | % of estate | Rs (x 94.0338) |
|---|---|---|---|---|
| $60,000 | $13,000 | $0 | 0% | 0 |
| $213,304 (current assets) | $59,057 | $46,057 | 21.6% | Rs 43.3 L |
| $300,000 | $87,800 | $74,800 | 24.9% | Rs 70.3 L |
| $337,987 (current + unvested awards) | $100,716 | $87,716 | 26.0% | Rs 82.5 L |
| $500,000 | $155,800 | $142,800 | 28.6% | Rs 1.34 Cr |
| $1,000,000 | $345,800 | $332,800 | 33.3% | Rs 3.13 Cr |

**Debt caveat (illustration only).** Debts (e.g. a home loan) reduce the taxable estate only by the
US share. If the worldwide estate were $213,304 + AngelOne $27,900 = $241,204 and there were a
Rs 50 L ($53,170) loan, the deduction would be $53,170 x 213,304 / 241,204 = $47,020, taxable estate
$166,284, tax about $31,000 (instead of $46,057). Needs a certified inventory of the whole worldwide estate (i706na Part
IV). Other assets and debts of the user are not known here.
