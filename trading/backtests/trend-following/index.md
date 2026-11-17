# Backtest: trend following (Faber SMA200 timing and Donchian 50/20 breakout)

## Summary
- Fit for paper trading in the US only: use Donchian 50/20 with the rules stop. Faber SMA200 on stocks had smaller drops but holds up to 30+ stocks at once, outside the 5-position rule: a long-term or market-filter idea only.
- US, Faber SMA200 monthly, stocks: 13.1% a year, worst drop -17.9% (SPY 13.9%, -33.7%).
- US, Donchian 50/20, rules stop, rules-sized: 13.1% a year, worst drop -23.1% (SPY 13.9%, -33.7%).
- India, Faber SMA200 monthly, stocks: 8.6% a year, worst drop -15.3% (^NSEI 9.8%, -38.4%).
- India, Donchian 50/20, rules stop, rules-sized: 5.1% a year, worst drop -33.0% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py trend-following`; every number on this page is printed by that script.

## Rules (exact)
Two families, run separately for US and India.

A. Faber timing (SMA200, monthly check). On the last trading day of each month, for each asset in the set: if close > its 200-day simple moving average of closes, hold it at weight 1/N (N = all assets in the set) from the next day's open; otherwise that share sits in cash. All held assets are reset to 1/N at each monthly rebalance. Sets: the market's ETFs (US: SPY QQQ IWM EFA EEM TLT GLD; India: NIFTYBEES BANKBEES GOLDBEES) and the market's stock list. Compared with the same set held at 1/N with monthly rebalance.

B. Donchian 50/20 breakout on the stock lists. Entry: close > highest high of the prior 50 trading days (signal day excluded) -> buy next open. Exit: close < lowest low of the prior 20 trading days -> sell next open. Variants: (1) no stop; (2) with the AGENTS.md stop: at the fill, stop = the highest (tightest) of entry - 2 x ATR(14), the 10-day swing low (lowest low of the 10 days up to the signal day, used only if below entry) and entry x 0.90; the stop never moves. Every variant run is shown.

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Faber SMA200 monthly, stocks | 13.1% | -17.9% | 45.5% | 536 | SPY | 13.9% | -33.7% | Outside rules (30+ positions); filter idea | fail: no rules-sized run with the stop | [HTML](../reports/trend-following-faber-US.html) |
| US | 35 names | Donchian 50/20, rules stop, rules-sized | 13.1% | -23.1% | 41.8% | 467 | SPY | 13.9% | -33.7% | Fit for paper trading | pass | [HTML](../reports/trend-following-donchian-US.html) |
| India | 35 names | Faber SMA200 monthly, stocks | 8.6% | -15.3% | 37.0% | 513 | ^NSEI | 9.8% | -38.4% | Outside rules (30+ positions); filter idea | fail: no rules-sized run with the stop | [HTML](../reports/trend-following-faber-India.html) |
| India | 35 names | Donchian 50/20, rules stop, rules-sized | 5.1% | -33.0% | 31.3% | 467 | ^NSEI | 9.8% | -38.4% | Paper test only (weak) | fail: max DD -33.0% | [HTML](../reports/trend-following-donchian-India.html) |

## Verdict
US: Donchian 50/20 with the rules stop is the only tested trend strategy that kept up with buy and hold while cutting the drawdown: rules-sized (Rs 2 L equivalent) it made 13.1% a year with a -23.1% worst drop, against SPY 13.9% and -33.7%, and it held up in both 2010-2019 and 2020-2026 (profit factor about 2 in each). Win rate is low (about 4 in 10); profits come from a few large trends, so expect long runs of small stopped-out losses. India: the same rules made only 5.1% a year with a -33.0% drop against Nifty 9.8% (price index); costs of 0.22% a side and the tight stop hurt, and it was weak in 2010-2019. Faber SMA200 timing roughly halved drawdowns in both markets but gave up a lot of return against holding the same assets; it is better used as a market filter than as a trading strategy. Verdict: fit for paper trading on US large caps; India only as a paper test to collect evidence, not for real money on these results. A trade plan should use exactly: buy at the next open after a daily close above the prior 50-day high; stop at entry = tightest of 2 x ATR(14), 10-day swing low, 10% (GTT/stop order the same day, never moved down); exit at the next open after a close below the prior 20-day low or at the stop; size = 1% risk / (entry - stop), max 20% of budget, max 5 open, max 3 new entries a week; earnings rule applied by hand (not tested).

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US Faber SMA200 monthly, stocks: fail: no rules-sized run with the stop; US Donchian 50/20, rules stop, rules-sized: pass; India Faber SMA200 monthly, stocks: fail: no rules-sized run with the stop; India Donchian 50/20, rules stop, rules-sized: fail: max DD -33.0%.

## Sources
- Faber, M. (2007), "A Quantitative Approach to Tactical Asset Allocation", Journal of Wealth Management (SSRN 962461). Faber uses a 10-month SMA on month-end closes; a 200-day SMA checked monthly is used here (close equivalent, as specified for this test).
- Moskowitz, T., Ooi, Y. H., Pedersen, L. H. (2012), "Time series momentum", Journal of Financial Economics 104(2): an asset's own past 12-month return predicts its next month across asset classes.
- Donchian channel breakout and the Turtle rules (Faith, C. (2007), "Way of the Turtle"): System 2 enters on a 55-day high; the 50-day entry / 20-day exit used here is the common simplified version. Turtles trade intraday breakouts; here signals use the close and fill at the next open.

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [universe.md](universe.md) | Full-universe check (all included scan names) and its backtest bar |
| [../index.md](../index.md) | All strategies compared |
