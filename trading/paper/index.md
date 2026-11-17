# Paper trading

## Summary
- 2026-11-17: 0 open, 3 pending orders; open risk Rs 5,062 (2.5% of equity; limit 5%).
- Budget equity Rs 200,000 (Rs 2,00,000 + realised paper P&L Rs 0).
- Paper check: 0 of 20 closed trades, 0.0 of 8 weeks since the first fill (no fill yet).
- Rule breaks: 0 (orders are only created inside the AGENTS.md rules).
- Active strategies: Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (US, below bar: user via finance-main 2026-11-16: rules-following test; full-universe rules-sized PF 1.21 (full period) / 1.19 (2020-2026), trading/backtests/short-breakout/universe.md).

Paper only: agents never place orders. Ledger: [trades.csv](trades.csv); strategies allowed below the bar: [allowed.csv](allowed.csv); daily lines for finance-journal: [outbox/](outbox/).

## Active strategies
| Market | Strategy | Backtest | Status | Why |
|---|---|---|---|---|
| US | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop | [short-breakout](../backtests/short-breakout/index.md) | below bar | user via finance-main 2026-11-16: rules-following test; full-universe rules-sized PF 1.21 (full period) / 1.19 (2020-2026), trading/backtests/short-breakout/universe.md |

## Open and pending
| symbol | strategy | approval | status | signal_date | limit | fill_date | fill_price | stop | target | time_stop_date | shares | risk_inr | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BILL | turtle2r | below bar | pending | 2026-11-16 | 57.9182 |  |  | 53.8115 | 66.1315 |  | 5 | 1935 | stop/target are estimates until the fill |
| PG | turtle2r | below bar | pending | 2026-11-16 | 173.8851 |  |  | 167.3462 | 186.9629 |  | 2 | 1232 | stop/target are estimates until the fill |
| CMCSA | turtle2r | below bar | pending | 2026-11-16 | 25.7280 |  |  | 24.2914 | 28.6012 |  | 14 | 1895 | stop/target are estimates until the fill |

## Closed (last 20)
None.

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
