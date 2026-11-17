# Backtest: gap-up drift (post-earnings-announcement drift proxy)

## Summary
- Buy the day after a big gap-up on heavy volume, out within 20 days. A proxy for earnings drift: gap days were not matched to earnings dates.
- US, Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized: 1.1% a year, worst drop -5.0% (SPY 13.9%, -33.7%).
- India, Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized: 0.2% a year, worst drop -5.4% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py gap-drift`; every number on this page is printed by that script.

## Rules (exact)
Entry: the open gaps up at least 4% above the prior close, volume at least 3 x the average of the prior 50 days, the close is in the top half of the day's range and above the 200-day SMA -> buy the next open. Stop: the gap day's low, or the rules stop if that is tighter (never wider than 10%). Exit: 2R target or after 20 trading days. One variant (fixed). This is a proxy for post-earnings drift: gap days are not matched to earnings dates. Universe: the market's stock list (same as the other backtests). Every variant uses the AGENTS.md stop at the fill: the tightest of entry - 2 x ATR(14), the 10-day swing low (if below entry) and entry x 0.90. Exits are checked in this order each day: stop (fills at the stop, or the open if it gaps below), then target (fills at the target, or the open if it gaps above), then the exit signal or time stop (sell at the next open). The stop is checked before the target on the same day (conservative). Time stop counts trading days held including the entry day.

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | 1.1% | -5.0% | 52.8% | 108 | SPY | 13.9% | -33.7% | see bar | fail: PF 2020-2026 0.98 < 1.2; avg trade 2020-2026 -0.05% | [HTML](../reports/gap-drift-US.html) |
| India | 35 names | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | 0.2% | -5.4% | 50.0% | 54 | ^NSEI | 9.8% | -38.4% | see bar | fail: trades 54 < 100; PF full 1.17 < 1.2 | [HTML](../reports/gap-drift-India.html) |

## Verdict
Gap-up drift is the event-driven short-hold style tested here.

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized: fail: PF 2020-2026 0.98 < 1.2; avg trade 2020-2026 -0.05%; India Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized: fail: trades 54 < 100; PF full 1.17 < 1.2.

## Sources
- Bernard, V. L., Thomas, J. K. (1989), "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?", Journal of Accounting Research 27: prices keep drifting in the direction of an earnings surprise for weeks.
- "Gap and go": trader practice of buying strong gap-ups on volume (no single paper).

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [universe.md](universe.md) | Full-universe check (all included scan names) and its backtest bar |
| [../index.md](../index.md) | All strategies compared |
