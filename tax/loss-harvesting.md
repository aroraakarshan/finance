# Loss harvesting on US shares: can you sell and buy back the same day?

## Summary

- Yes. For Indian tax you may sell a US share at a loss and buy it back the same day (or minute); the loss counts. India has no wash-sale rule, and the US 30-day wash-sale rule does not apply to you (no US capital gains tax for a nonresident).
- Caveats: the rebought shares get a new cost and a new 24-month clock; check each lot in rupees first (NVDA and the GOOGL Nov-2025 lot are rupee gains); keep it a normal market order, not a deal with a relative.
- With QCOM sale 1 in 2026-27 (the plan, LTCG about Rs 15.2 L, specific identification), every rupee of 2026-27 loss saves 14.95% this year and nothing carries forward: all silver (-Rs 1,18,047, user decision 16 Nov) about Rs 17,648, SCLX + IONQ about Rs 5,264 (SMNR/SYRS when sold at IBKR, [migration 3.5](migration-indmoney-to-ibkr.md)). If QCOM sale 1 slips past 31 Mar 2027, the INDmoney loss carries forward instead (about Rs 67,300-87,000 with all silver sold; ITR by 31 Jul 2027).
- 16-25 Nov: sell SCLX, SMNR, IONQ (SYRS by 27 Nov) anyway (real loss, may not move to IBKR); do not rebuy at INDmoney before the transfer; rebuy (if wanted, and only shares above $5) at IBKR after it.

Prepared 15 Nov 2026 by `finance-tax` (agent `harvest`). Plan only: no orders. Tax year 2026-27,
new regime, surcharge 15%, cess 4%: LT 14.95%, ST at slab 35.88%, s.111A 23.92%.
Sources: [rules] work-folder rules note (section 3); [mig] `migration-indmoney-to-ibkr.md`;
[ang] `angelone-metals-and-mf-exits.md`; [tt] `FY2025-26/time-technoplast.md`;
[act] Income-tax Act 2025 and Rules 2026, text in github abaasairam-ai/income-tax-rag
`docs-text/` (read 15 Nov 2026; spot-check against the official PDFs).

## 1. US rules do not apply

| Point | Rule | Effect for you |
|---|---|---|
| US wash-sale | IRC s.1091: a loss is disallowed for US tax if the same stock is bought within 30 days before or after | Only a rule for computing US-taxable loss |
| US tax on your share gains | IRC s.871(a)(2): a nonresident alien is taxed on US capital gains only if present in the US 183+ days in the year | You owe no US tax on the sale, so s.1091 is irrelevant |
| Broker forms | Brokers report to nonresidents (W-8BEN on file) on Form 1042-S, not 1099-B; any "wash sale" flag on a broker report is a US computation | Ignore it; compute Indian gain from trade confirmations |

## 2. India: no wash-sale rule

| Test | Text | Applies to a same-day sell and rebuy? |
|---|---|---|
| Set-off and carry-forward | 1961 s.70/71/74/80; 2025 s.108/109/111/121 | No holding or waiting condition anywhere: the loss counts |
| Bond washing | 1961 s.94(1)-(6); 2025 s.175(1)-(7) | Covers sale and buy-back only around INTEREST/dividend dates, moving that income to the owner. Not a loss disallowance; no income date in these sales |
| Dividend stripping | 1961 s.94(7); 2025 s.175(8) | Only if bought within 3 months before a record date, sold within 3 months after, AND the dividend is exempt. Foreign dividends are taxable, so never |
| Bonus stripping | 1961 s.94(8); 2025 s.175(9)-(10) | Bought within 3 months before a record date for free securities, sold within 9 months after, free ones kept. See section 5 |
| GAAR | 1961 Chapter X-A (s.95-102); 2025 Chapter XI (s.178-184) | Not applicable: Rules 2026 r.128(1)(a) (old Rule 10U(1)(a)) excludes arrangements with total tax benefit up to Rs 3 crore in the year. Yours is under Rs 30,000 |
| Judge-made anti-avoidance | McDowell (SC 1985) vs Azadi Bachao Andolan (SC 2003) and Vodafone (SC 2012) | Genuine transactions at market price are respected; only colourable devices are not. An exchange order with delivery is genuine |
| ITAT rulings | Searched 15 Nov 2026 | No ruling on a same-day sell-and-rebuy of shares found or verified; none needed, as no provision disallows it |

Keep it clearly real:

| Do | Do not |
|---|---|
| Sell on the exchange with a limit order; buy back the same way | Pre-arrange a cross trade with a relative, a company you control or your own other account |
| Let the trade settle (T+1) and keep the shares | Sell and buy at an off-market price |
| Keep the trade confirmations of both legs | Treat the rebuy as "the same lot" in your records |

## 3. What a rebuy changes

| Item | Old lot (sold) | New lot (rebought) |
|---|---|---|
| Cost | Original cost (INR) | Rebuy price (INR at its own rate) |
| Holding period | Ends on the sale date | Restarts: long-term only after more than 24 months from the new buy date (1961 s.2(42A); 2025 s.2(101)(a)) |
| Tax effect | Loss booked now | Same shares, lower cost: a bigger gain later |

So harvesting is deferral plus rate arbitrage, not a free saving:

| Loss used against | Value now | Gain added later on the rebought lot |
|---|---|---|
| ST gain at slab | 35.88% | 14.95% if sold after 24 months; 35.88% if sold earlier |
| LT gain (NXPI) | 14.95% | same |
| Carried forward (8 years) | 14.95%-35.88% later, only if used | same |

Example: IONQ (lot 2025-08-01) turns long-term on 2 Aug 2027 if kept; if sold and rebought on
20 Nov 2026, the new lot is long-term only from 21 Nov 2028 [mig s.3.4].

## 4. Check each lot in rupees first

Sale value and cost are each converted at the SBI TT buying rate on the last day of the month
before the month of the transaction (1961 Rule 115; Rules 2026 r.206(1) with Table Sl.6, the TT
buying rate defined in r.207 - verified in [act] 15 Nov 2026; converting cost at its own month is
practice; keep one method every year). If the rupee fell since you bought, a USD loss can be a rupee gain.

| Lot (13 Nov 2026 prices) [mig s.3.3] | USD | INR approx | Harvest? |
|---|---|---|---|
| SCLX 31.43 sh (2025-07-25, 2025-08-04) | -327.60 | -27,863 | Yes |
| SYRS 800 sh (2024-11-27) | -217.76 | -18,310 | Yes, by 27 Nov (long-term from 30 Nov) |
| SMNR 31.43 sh (2026-06-16) | -172.23 | -16,555 | Yes (less if cost = FMV on receipt) |
| IONQ 13.24 sh (2025-08-01) | -116.18 | -7,346 | Yes |
| GOOGL 6.24 sh (2025-11-26) | -164.31 | -2,533 | Only if INDmoney sells this lot specifically (specific identification, user decision 17 Nov; `employer-stock/qcom-lots.md` 3.3); FIFO fallback sells the 2025-11-21 lot first |
| GOOGL 2.92 sh (2025-11-21) | -10.76 | +4,675 | No: rupee gain |
| NVDA all lots (2025-07-30) | -108.58 | +2,557 | No: rupee gain |
| SHLS 45 sh (2024-11-27) | +137.94 | +15,745 | Gain; sell only on or after Mon 30 Nov if at all |

INR figures use yfinance USDINR, about 0.5% off the SBI rate; recompute with SBI TT rates for the ITR.

## 5. Dividend and bonus stripping check on the candidates

| Lot | Record date in the window? | Result |
|---|---|---|
| SCLX | Semnur stock distribution, record date 2026-06-01, received 2026-06-15/16 (STATUS.md) | s.175(9) needs a buy within 3 months before 1 Jun 2026 (from 1 Mar 2026). SCLX lots are Jul-Aug 2025: not met. Loss allowed |
| SMNR | Received in the distribution, not bought before a record date | Not met |
| IONQ, SYRS | No dividend or bonus known | Not met |
| Rebuy | A new lot bought within 3 months before a future bonus/free-share record date and sold within 9 months would be caught | Note the rule if you rebuy |

For contrast, [tt] is a case where s.94(8) did apply: Time Technoplast bought 25 Jul 2025,
1:1 bonus record date 23 Sep 2025, sold 26 Nov 2025: Rs 781 loss ignored and added to the
bonus shares' cost.

## 6. Set-off this year (tax year 2026-27)

| Rule | Text |
|---|---|
| ST loss -> any capital gain; LT loss -> LT gain only | 1961 s.70(2),(3); 2025 s.108(2) |
| No set-off against salary or other heads | 1961 s.71(3); 2025 s.109(2) |
| Carry forward 8 tax years, same ST/LT limits | 1961 s.74; 2025 s.111(1) |
| Only if the loss is in a return filed under s.263(1) by the due date (31 Jul 2027) | 1961 s.80 with s.139(1); 2025 s.121 |

| Position (approx INR, 13 Nov prices) [ang s.2, s.6; mig s.3] | Amount |
|---|---|
| INDmoney ST loss to 9 Nov + fractions at migration | -2,16,582 + 6,448 = -2,10,134 |
| NXPI LT gain (IBKR, 9 Jul 2026) | +2,76,457 |
| LT gain left, taxed at 14.95% | 66,323 (tax Rs 9,915) |
| INDmoney harvest (SCLX, SMNR, IONQ, SYRS) | -51,800 to -70,100 |
| AngelOne: all silver incl. ABSL (16 Nov decision; ETFs 16 Nov close, FoFs NAV 13 Nov) | -1,18,047 |
| QCOM sale 1 + MSFT Jan lot (LT, specific identification, `employer-stock/staged-sale.md` section 3) | about +15.78 L |
| With QCOM sale 1 (the plan) | All losses set off this year; no carry-forward. New losses save 14.95%: all silver 17,648, SCLX + IONQ (-35,209) 5,264, MF ST (-963) 144, less fraction gains (+7,155) 1,070. Excess over NXPI + fractions (about 87,200) plus the MSFT new-vest ST loss (about 18,155, provisional) = about 1,05,400 offsets QCOM: about Rs 15,750; QCOM sale 1 tax about Rs 2,11,000 after losses (Rs 2,26,828 before); advance tax about Rs 1,53,600 by 15 Dec, Rs 1,91,400 by 15 Mar |
| If QCOM sale 1 slips past 31 Mar 2027 | Tax 0; about Rs 67,300-87,000 ST loss carries forward with all silver sold (lower end with the 7 MF exits; SMNR/SYRS excluded until sold) |

With QCOM sale 1 in 2026-27 (`portfolio/plan.md`) the INDmoney harvest saves 14.95% this year.
Only if QCOM sale 1 is postponed does its value become a carry-forward (worth 14.95%-35.88% in a
later year). Either way it is worth doing: the loss is real and these lots may not transfer to IBKR.

## 7. Checklist for the 16-25 Nov INDmoney sales

| Step | What |
|---|---|
| 1 | Refresh the INDmoney holdings and trade export; confirm each lot's INR result (section 4) |
| 2 | Limit-order sells of all SCLX, SMNR, IONQ (whole shares and fractions); SYRS by Fri 27 Nov if any buyer |
| 3 | Sell the other fractions the same days (CRWD, CEG, TRVI, GOOGL, NVDA) [mig s.2]; SHLS fraction only on or after 30 Nov |
| 4 | Do not sell whole NVDA or the GOOGL 2025-11-21 lot for a "loss": they are rupee gains |
| 5 | Rebuy at INDmoney before the ACATS: avoid. It adds a new lot and fractions, trading freezes during the transfer, and fractions may be force-sold |
| 6 | Rebuy only at IBKR after the transfer, only names you want anyway; same-day is fine for tax. AGENTS.md excludes stocks under $5 (rules out SCLX, SMNR, SYRS) |
| 7 | Save each sell and buy confirmation (date, quantity, price, fees) and the SBI TT rate of the month before |
| 8 | Before 15 Dec: recompute 2026-27 tax and pay advance tax due; file the ITR by 31 Jul 2027 to keep any carry-forward |

## 8. Former open points (answers in `ca-questions.md`)

| Point | Why |
|---|---|
| SMNR cost (broker $187 vs FMV on receipt) | Changes the SMNR loss [mig s.8] |
| Order of set-off (ST loss against NXPI LTCG before exempt MF LTCG) | No express rule [rules s.3] |
| Cost converted at the purchase month's rate | Practice, not express text |
| Section references were read from an unofficial text extraction | Spot-check against the official PDFs |
