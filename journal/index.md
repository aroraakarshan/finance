# Journal

## Summary
Every paper and real trade is logged in `trades.csv` and checked against the trading rules
(`AGENTS.md`); breaches go in the monthly review (`reviews/<YYYY-MM>.md`), signal scores in
`signals.md`. Paper trading starts 2026-11-17 (US short breakout). Nothing for you to do.

## How trades are logged
| Column | Source |
|---|---|
| all trade fields | `finance-trader` outbox `trading/paper/outbox/<date>.md` (paper) or what the user reports to `finance-main` (real) |
| `plan` | ledger id in `trading/paper/trades.csv`, plus `trading/plans/<SYMBOL>.md` if any |
| `tax_effect` | standard line below, or the plan's tax line from `finance-tax` |

## Standard tax_effect
From `finance-tax` (`tax/global-actions-2026-11.md`, 2026-11-15):

| Case | tax_effect |
|---|---|
| US stock held <= 24 months | US stock <=24m: ST gain at slab 35.88% (paper: none); loss offsets any capital gain, rest carried 8 yrs; no US tax on gains, dividends 25% US WHT -> Form 44 credit; LRS TCS 20% above Rs 10 L/yr; Schedule FA A3+A2 |

Caveat from `finance-tax`: frequent short trading may count as business income (ITR-3; CBDT
Circular 6/2016; choose once and stay consistent). US shares are US-situs for US estate tax
while held.
