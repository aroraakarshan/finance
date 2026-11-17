# Backtest: 52-week-high breakout on volume (George and Hwang 2004)

## Summary
- Buy a new 52-week high on heavy volume, out within 20 days. Read the bar line below each market before using it.
- US, 52-week high on 1.5x volume, 2R target, 20 days, rules-sized: 6.1% a year, worst drop -10.7% (SPY 13.9%, -33.7%).
- India, 52-week high on 1.5x volume, 2R target, 20 days, rules-sized: -3.3% a year, worst drop -45.0% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py 52w-high-breakout`; every number on this page is printed by that script.

## Rules (exact)
Entry: close above the highest high of the prior 252 trading days (a new 52-week high) with volume at least 1.5 x the average of the prior 50 days -> buy next open. Exit: rules stop, 2R target, or after 20 trading days. One variant (fixed). Universe: the market's stock list (same as the other backtests). Every variant uses the AGENTS.md stop at the fill: the tightest of entry - 2 x ATR(14), the 10-day swing low (if below entry) and entry x 0.90. Exits are checked in this order each day: stop (fills at the stop, or the open if it gaps below), then target (fills at the target, or the open if it gaps above), then the exit signal or time stop (sell at the next open). The stop is checked before the target on the same day (conservative). Time stop counts trading days held including the entry day.

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | 6.1% | -10.7% | 48.8% | 711 | SPY | 13.9% | -33.7% | see bar | pass | [HTML](../reports/52w-high-breakout-US.html) |
| India | 35 names | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | -3.3% | -45.0% | 40.6% | 655 | ^NSEI | 9.8% | -38.4% | see bar | fail: PF full 0.84 < 1.2; PF 2020-2026 0.97 < 1.2; avg trade 2010-2019 -0.78%; avg trade 2020-2026 -0.09%; CAGR -3.3%; max DD -45.0% | [HTML](../reports/52w-high-breakout-India.html) |

## Verdict
A short-hold version of 52-week-high momentum.

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US 52-week high on 1.5x volume, 2R target, 20 days, rules-sized: pass; India 52-week high on 1.5x volume, 2R target, 20 days, rules-sized: fail: PF full 0.84 < 1.2; PF 2020-2026 0.97 < 1.2; avg trade 2010-2019 -0.78%; avg trade 2020-2026 -0.09%; CAGR -3.3%; max DD -45.0%.

## Sources
- George, T. J., Hwang, C.-Y. (2004), "The 52-Week High and Momentum Investing", Journal of Finance 59(5): stocks near their 52-week high keep outperforming. The paper ranks monthly and holds 6 months; this test is a short-hold breakout version with a volume filter, as specified.

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [universe.md](universe.md) | Full-universe check (all included scan names) and its backtest bar |
| [../index.md](../index.md) | All strategies compared |
