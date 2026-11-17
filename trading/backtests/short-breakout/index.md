# Backtest: short breakout (Turtle System 1 style, 20-day high / 10-day low)

## Summary
- Short-hold breakout (days to 3 weeks). Read the bar line below each market before using it.
- US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized: 9.6% a year, worst drop -23.6% (SPY 13.9%, -33.7%).
- US, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized: 8.2% a year, worst drop -23.6% (SPY 13.9%, -33.7%).
- India, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized: -1.6% a year, worst drop -42.3% (^NSEI 9.8%, -38.4%).
- India, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized: -1.2% a year, worst drop -49.0% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py short-breakout`; every number on this page is printed by that script.

## Rules (exact)
Entry: close above the highest high of the prior 20 trading days -> buy next open. Exit: close below the lowest low of the prior 10 trading days -> sell next open; or the rules stop; or a 15-day time stop. Variant 2 adds a target at 2R (entry + 2 x (entry - stop)). Both variants are shown. Universe: the market's stock list (same as the other backtests). Every variant uses the AGENTS.md stop at the fill: the tightest of entry - 2 x ATR(14), the 10-day swing low (if below entry) and entry x 0.90. Exits are checked in this order each day: stop (fills at the stop, or the open if it gaps below), then target (fills at the target, or the open if it gaps above), then the exit signal or time stop (sell at the next open). The stop is checked before the target on the same day (conservative). Time stop counts trading days held including the entry day.

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 9.6% | -23.6% | 47.3% | 1518 | SPY | 13.9% | -33.7% | see bar | fail: PF 2020-2026 1.19 < 1.2 | [HTML](../reports/short-breakout-turtle-US.html) |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 8.2% | -23.6% | 48.2% | 1642 | SPY | 13.9% | -33.7% | see bar | fail: PF 2020-2026 1.17 < 1.2 | [HTML](../reports/short-breakout-turtle2r-US.html) |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | -1.6% | -42.3% | 42.6% | 1433 | ^NSEI | 9.8% | -38.4% | see bar | fail: PF full 0.99 < 1.2; PF 2020-2026 1.08 < 1.2; avg trade 2010-2019 -0.17%; CAGR -1.6%; max DD -42.3% | [HTML](../reports/short-breakout-turtle-India.html) |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | -1.2% | -49.0% | 44.1% | 1538 | ^NSEI | 9.8% | -38.4% | see bar | fail: PF full 1.00 < 1.2; PF 2020-2026 1.02 < 1.2; avg trade 2010-2019 -0.03%; CAGR -1.2%; max DD -49.0% | [HTML](../reports/short-breakout-turtle2r-India.html) |

## Verdict
Short breakouts are the fastest in-and-out style tested here.

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized: fail: PF 2020-2026 1.19 < 1.2; US Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized: fail: PF 2020-2026 1.17 < 1.2; India Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized: fail: PF full 0.99 < 1.2; PF 2020-2026 1.08 < 1.2; avg trade 2010-2019 -0.17%; CAGR -1.6%; max DD -42.3%; India Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized: fail: PF full 1.00 < 1.2; PF 2020-2026 1.02 < 1.2; avg trade 2010-2019 -0.03%; CAGR -1.2%; max DD -49.0%.

## Sources
- Faith, C. (2007), "Way of the Turtle", McGraw-Hill: System 1 enters on a 20-day breakout and exits on a 10-day low (original stop 2N = 2 x ATR(20); here replaced by the AGENTS.md stop, and a 15-day time stop added as specified for this test).
- Donchian channel breakouts (R. Donchian, 1960s).

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [universe.md](universe.md) | Full-universe check (all included scan names) and its backtest bar |
| [../index.md](../index.md) | All strategies compared |
