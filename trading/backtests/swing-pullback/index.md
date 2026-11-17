# Backtest: swing pullback (Connors RSI(2) in an uptrend)

## Summary
- Not fit: the required stop cuts most trades in 2 days, and in India costs eat the edge; do not put it in trade plans.
- US, RSI(2), rules stop, rules-sized: 1.4% a year, worst drop -13.7% (SPY 13.9%, -33.7%).
- India, RSI(2), rules stop, rules-sized: -8.8% a year, worst drop -79.3% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py swing-pullback`; every number on this page is printed by that script.

## Rules (exact)
Universe: the market's ETFs and stocks. Entry: close > 200-day SMA and RSI(2) < 10 (Wilder smoothing) -> buy next open. Exit: close > 5-day SMA -> sell next open; time stop: sell at the next open after 10 trading days in the trade. Variants: (1) no stop (published rules); (2) with the AGENTS.md stop: at the fill, stop = the highest (tightest) of entry - 2 x ATR(14), the 10-day swing low (if below entry) and entry x 0.90; (3) 2 x ATR(14) stop only, capped at 10% (not compliant with the AGENTS.md rule, which takes the tighter of the two; shown only for comparison). The with-stop version (2) is the one that counts under the rules. Candidates on the same day are ranked by lowest RSI(2).

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | RSI(2), rules stop, rules-sized | 1.4% | -13.7% | 44.3% | 2100 | SPY | 13.9% | -33.7% | Not fit (rules stop) | fail: PF full 1.14 < 1.2; PF 2020-2026 1.15 < 1.2 | [HTML](../reports/swing-pullback-US.html) |
| India | 35 names | RSI(2), rules stop, rules-sized | -8.8% | -79.3% | 36.4% | 2077 | ^NSEI | 9.8% | -38.4% | Not fit (costs and stop) | fail: PF full 0.63 < 1.2; PF 2020-2026 0.63 < 1.2; avg trade 2010-2019 -0.39%; avg trade 2020-2026 -0.40%; CAGR -8.8%; max DD -79.3% | [HTML](../reports/swing-pullback-India.html) |

## Verdict
Not fit for paper trading under the AGENTS.md rules. With the required stop the swing-low part sits only a little below the entry after a pullback, so about half the trades are stopped out within 2 days; rules-sized the US made 1.4% a year and India lost 8.8% a year with a -79.3% worst drop. Without a stop (Connors' published rules) the US version made 9.6% a year in the 5-slot portfolio with a -17.1% worst drop, below SPY's 13.9%, while India lost money even without a stop: the average edge per trade is smaller than India's round-trip cost of about 0.44%. The 2 x ATR-only stop did better than the rule stop in the US but worse than no stop. Verdict: do not paper-trade this in India. In the US it would need a change to the stop rule for mean-reversion trades (a wider or time-based stop), which only the user can approve; until then it should not go into trade plans. If the rule is changed, a plan would use exactly: close > 200-day SMA and RSI(2) < 10, buy next open, sell next open after a close above the 5-day SMA or after 10 days, 2 x ATR(14) stop capped at 10%.

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US RSI(2), rules stop, rules-sized: fail: PF full 1.14 < 1.2; PF 2020-2026 1.15 < 1.2; India RSI(2), rules stop, rules-sized: fail: PF full 0.63 < 1.2; PF 2020-2026 0.63 < 1.2; avg trade 2010-2019 -0.39%; avg trade 2020-2026 -0.40%; CAGR -8.8%; max DD -79.3%.

## Sources
- Connors, L., Alvarez, C. (2008), "Short Term Trading Strategies That Work", TradingMarkets: buy pullbacks (RSI(2) under 10, or under 5) in stocks above their 200-day average, exit on a close above the 5-day average; Connors argues stops hurt this kind of strategy.

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [../index.md](../index.md) | All strategies compared |
