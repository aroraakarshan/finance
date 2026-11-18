# Paper trading

## Summary
- 2026-11-17: 2 open, 0 pending orders; open risk Rs 3,127 (1.5% of equity; limit 5%).
- Budget equity Rs 203,841 (Rs 2,00,000 + realised paper P&L Rs 3,841).
- Paper check: 1 of 20 closed trades, 0.0 of 8 weeks since the first fill (2026-11-17).
- Rule breaks: 0 (orders are only created inside the AGENTS.md rules).
- Active strategies: Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (US, below bar: user via finance-main 2026-11-16: rules-following test; full-universe rules-sized PF 1.21 (full period) / 1.19 (2020-2026), trading/backtests/short-breakout/universe.md).

Paper only: agents never place orders. Ledger: [trades.csv](trades.csv); strategies allowed below the bar: [allowed.csv](allowed.csv); daily lines for finance-journal (named by the US signal close; newest first): [2026-11-17](outbox/2026-11-17.md), [2026-11-16](outbox/2026-11-16.md), [2026-11-13](outbox/2026-11-13.md).

## Active strategies
| Market | Strategy | Backtest | Status | Why |
|---|---|---|---|---|
| US | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop | [short-breakout](../backtests/short-breakout/index.md) | below bar | user via finance-main 2026-11-16: rules-following test; full-universe rules-sized PF 1.21 (full period) / 1.19 (2020-2026), trading/backtests/short-breakout/universe.md |

## Open and pending
| symbol | strategy | approval | status | signal_date | limit | fill_date | fill_price | stop | target | time_stop_date | shares | risk_inr | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PG | turtle2r | below bar | open | 2026-11-16 | 173.8851 | 2026-11-17 | 171.3400 | 164.8011 | 184.4178 | 2026-12-08 | 2 | 1232 | stop and target set from the fill 2026-11-17 |
| CMCSA | turtle2r | below bar | open | 2026-11-16 | 25.7280 | 2026-11-17 | 25.4350 | 23.9984 | 28.3082 | 2026-12-08 | 14 | 1895 | stop and target set from the fill 2026-11-17 |

## Closed (last 20)
| symbol | strategy | fill_date | fill_price | exit_date | exit_price | exit_reason | r_multiple | pnl_inr |
|---|---|---|---|---|---|---|---|---|
| BILL | turtle2r | 2026-11-17 | 56.7600 | 2026-11-17 | 64.9734 | target | 1.99 | 3841 |

## How orders are handled
| Step | Rule |
|---|---|
| Order | Limit = signal close x 1.005, for the next session only |
| Fill | At the open if the open <= limit; else at the limit if the day's low <= limit; else cancelled (no chasing) |
| At the fill | Rules stop recomputed from the fill (tightest of 2 x ATR(14), 10-day swing low, 10%; gap-drift also the gap-day low); target 2R where the strategy has one; shares cut so risk <= Rs 2,000 |
| Each day | Stop first (stop price, or the open on a gap below), then target, then the strategy exit or time stop (next open); news score -2 -> next open |
| New orders | Only strategies that pass the full-universe backtest bar; <= 5 open + pending, <= 3 new a week, open risk <= 5%, 20% cap, whole shares, earnings > 5 trading days away (no date = skip), news not -2 |
| Ranking | Strategies by full-universe profit factor (higher first), then the strategy's own signal strength (same score as the backtests) |
| Loss limits | 3 stops in a row -> 1 week pause; month loss 4% -> no new trades; budget -10% -> stop |
| Costs | US 0.05% a side, India 0.22% a side (as in the backtests) |
