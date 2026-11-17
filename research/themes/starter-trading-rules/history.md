# Starter trading rules: numbers and trade history

Back to the index: [../starter-trading-rules.md](../starter-trading-rules.md).

## Summary
The budget base is market investments without employer stock, bank money, EPF or physical gold: Rs 44.6 L of Rs 4.21 Cr total (2026-11-15).
INDmoney history (98 trades, split-adjusted): realised -$542, IONQ +$2,131 carried the result, losers were not cut.
Each finding below maps to a rule in [rules.md](rules.md). Decide which US holdings count as "trading".

## Numbers used

Numbers used below (portfolio/summary.md as of commit 58caa59, 2026-11-15; US values at the
2026-11-13 close; INDmoney wallet cash 2026-11-15; HDFC savings 2026-11-13, FDs 2026-11-15, physical gold 2026-11-13; Punjab Gramin Bank 2026-11-15 (user estimate); EPF 2026-08-19; USD/INR 94.1997 (summary.md; earlier versions of this note used 94.0338, the `INR=X` close
2026-11-13; AngelOne as of 2026-11-08):

| Part | USD | INR | Share |
|---|---|---|---|
| Employer-plan stock: QCOM 761 (IBKR) $131,250 + MSFT 116.888 (Fidelity) $61,235 | $192,485 | Rs 1,81,32,029 | 43.1% (QCOM $131,250 = Rs 1,23,63,711 = 29.4%) |
| IBKR stock award (vests Dec 2026) | $1,295 | Rs 1,21,989 | 0.3% |
| AngelOne stocks, ETFs, mutual funds | - | Rs 26,24,910 | 6.2% |
| INDmoney $14,653 (positions $10,079 + wallet cash $4,574.05) + IBKR AVGO $3,470 + VRT $606 + cash $795 | $19,524 | Rs 18,39,155 | 4.4% |
| HDFC savings Rs 8,54,314 (13 Nov) + 9 FDs Rs 49,31,288 principal plus accrued interest (6.25%, 2026-05-10 to 2027-05-10) | - | Rs 57,85,602 | 13.7% |
| Physical gold (109.1 g, IBJA rate 2026-11-13) | - | Rs 12,90,192 | 3.1% |
| Punjab Gramin Bank FDs Rs 72 L + savings Rs 10 L (user estimates, 2026-11-15) | - | Rs 82,00,000 | 19.5% |
| EPF (Qualcomm and Microsoft accounts, passbooks 2026-08-19; locked) | - | Rs 41,03,127 | 9.7% |
| **Total investments** | $213,304 + AngelOne + HDFC + gold + Punjab Gramin Bank + EPF | **Rs 4,20,97,035** (rows add to Rs 31 less: rounding) | 100% |
| **Budget base: AngelOne + non-employer US holdings and cash (excludes employer stock, the unvested award, HDFC and Punjab Gramin Bank savings and FDs, EPF, physical gold)** | | **Rs 44,64,065** | 10.6% |

Trade history: `scripts.brokers.indmoney.trades()` and `python -m scripts.pnl indmoney`
(split-adjusted: CERO, HSDT, SCLX reverse splits; CRWD, KLAC splits; SAVA -> FLNA), run
2026-11-15: 98 trades, 2024-08-07 to 2026-11-05. GEV sold 2026-11-09 (about -$291) is after
the export and not in these numbers.

## Open decisions for the user

- The non-employer US holdings and cash ($19,524, about Rs 18.4 L, incl. $4,574 INDmoney
  wallet cash) are about 9 times the proposed
  budget. Decide which positions are long-term and which are "trading"; only the trading
  part falls under these rules.
- Employer-plan stock (QCOM + MSFT) is 43.1% of all investments (QCOM alone 29.4%). That concentration is a bigger
  risk than any trading rule here; reducing it is a separate long-term decision, and sale
  proceeds should go to long-term funds, not the trading budget.

## What his history shows

INDmoney (Alpaca) US account, 2024-08-07 to 2026-11-05, split-adjusted. Source: script runs above.

| Finding | Number | Rule it motivates |
|---|---|---|
| Market orders | 97 of 98 trades | Limit orders only |
| Fees | $158.30 = 0.27% of $59,500 traded | Fewer trades; trade size limits |
| Realised result | -$542 total (fees not in P/L); 11 stocks won, 19 lost; median closed stock -22.0% | Paper trading first; small budget |
| One stock carried the result | IONQ +$2,131; without it -$2,673. IONQ = 52% of all gains ($4,073) | Do not size up after one big win |
| Gross losses | 19 losers lost $4,616 (about Rs 4.34 L) | Max loss per trade |
| Losses not cut | 16 of 19 losers were sold more than 20% down; 6 more than 50% down (HSDT -98.8%, FLNA -82.7%, CERO -78.1%, GWH -74.7%, SNTI -61.0%, PRFX -53.6%) | Stop-loss set at entry |
| Losers held as long as winners | Median first-buy to last-sell: losers 249 days, winners 239 days | Stop-loss; time stop in review |
| Largest single loss | FLNA (was SAVA) -$737 = Rs 69,400 = 35% of the proposed Rs 2 L budget, 1.6% of the Rs 44.6 L budget base | Max loss per trade Rs 2,000 |
| Averaging down | FLNA bought at $3.89 then $2.25; SNTI $7.88 then $2.99; CERO $18.54 then $5.98 (split-adjusted); together -$1,213 | No averaging down |
| Low-priced stocks | 14 of 62 buys under $5 split-adjusted (6 under $1). 9 closed names bought under $5: net -$1,627 (8 losers -$1,981, 1 winner PROC +$354) | Exclude under $5 / Rs 50 |
| Position size | Buys: median $499, 75th pct $991, max $2,010; 16 buys of about $1,000 | Size from risk, not a fixed ticket |
| Bursts of trading | 98 trades on 43 days; Nov 2024: 21, Jul 2025: 17, Aug 2025: 14; most in one day 9 (2025-07-30) | Max 3 new trades per week |
| Mass exits | 6 sells on 2026-11-05 (BSX, IONR, FLNA, KLAC, PSI, URA), all losses | Loss limits and pause; written plan for exits |

Not measured: slippage of the market orders (the export has no bid/ask at order time).

Discrepancies found (also for STATUS.md, which this task did not edit):
- Open-position cost: $10,167 from the trade file (average cost) vs $10,226 in the holdings
  export (broker first in, first out); explained in summary.md, small.
- The first version of this file (earlier on 2026-11-15) used pre-split data (+$210 realised,
  13 won / 17 lost, 18 buys under $5); all numbers above are now split-adjusted.
- BSX bought at $104-107 (2025) and sold at $45.77 (2026-11-05): price drop or split not verified.

## Sources
- portfolio/summary.md (commit 58caa59, 2026-11-15) for holdings, values and USD/INR.
- `scripts.brokers.indmoney.trades()` and `python -m scripts.pnl indmoney`, run 2026-11-15.
