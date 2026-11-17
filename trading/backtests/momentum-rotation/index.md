# Backtest: momentum rotation (top-5 12-1 month momentum with index trend filter)

## Summary
- Beats the index but not an equal-weight hold of the same stocks, and it has no stop: a long-term sleeve at most, not for the trading budget.
- US, Top-5 12-1 momentum, index filter: 17.1% a year, worst drop -38.5% (SPY 13.9%, -33.7%).
- India, Top-5 12-1 momentum, index filter: 13.7% a year, worst drop -22.1% (^NSEI 9.8%, -38.4%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py momentum-rotation`; every number on this page is printed by that script.

## Rules (exact)
At each month-end close: if the market index (US: SPY; India: ^NSEI) closes above its 200-day SMA, rank the market's stock list by 12-1 month return = close 21 trading days ago / close 252 trading days ago - 1 (the latest month skipped), and hold the top 5 at 20% each from the next day's open; all holdings reset to 20% each month. If the index is below its SMA200, hold cash. At least 10 stocks with full history are needed to rank. Variant run: the same without the index filter. No stop (the published rules have none).

## Headline (full period 2010-01-01 to 2026-11-13, costs included)
| Market | Universe | Version that counts | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Top-5 12-1 momentum, index filter | 17.1% | -38.5% | 55.0% | 231 | SPY | 13.9% | -33.7% | Long-term sleeve only (no stop) | fail: no rules-sized run with the stop | [HTML](../reports/momentum-rotation-US.html) |
| India | 35 names | Top-5 12-1 momentum, index filter | 13.7% | -22.1% | 56.9% | 225 | ^NSEI | 9.8% | -38.4% | Long-term sleeve only (no stop) | fail: no rules-sized run with the stop | [HTML](../reports/momentum-rotation-India.html) |

## Verdict
Momentum rotation beat the market index in both markets: US 17.1% a year with the filter (27.8% without) vs SPY 13.9%; India 13.7% with the filter (15.6% without) vs Nifty 9.8% (price index) and NIFTYBEES 10.6%. But it did not beat simply holding the same hand-picked stocks at equal weight (US 21.1%, India 18.0%), and that basket is itself inflated by survivorship (today's winners chosen in 2026), so the true edge is smaller than the gap to the index suggests. The index filter cut the India drawdown (-22.1% vs -36.3%) but in the US it cost return and did not reduce the worst drop (-38.5% vs -32.7%), because the filter re-entered late after sharp falls. Results also weakened in 2020-2026 in the US (win rate and profit factor down). Verdict: this is a monthly allocation method, not a swing trade, and it has no stop, so it does not fit the AGENTS.md trading rules as written (stop on every trade, 1% risk sizing, 5 positions at 20%). Fit for paper trading only as a separate long-term sleeve if finance-main and the user agree; a plan would use exactly: month-end ranking by 12-1 return, top 5 at 20% each, next-open fills, monthly reset, cash when the index is below its 200-day SMA (India) - and a catastrophic stop would have to be added and tested first before any real money.

Backtest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): US Top-5 12-1 momentum, index filter: fail: no rules-sized run with the stop; India Top-5 12-1 momentum, index filter: fail: no rules-sized run with the stop.

## Sources
- Jegadeesh, N., Titman, S. (1993), "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency", Journal of Finance 48(1): 3-12 month winners keep outperforming for 3-12 months.
- Antonacci, G. (2014), "Dual Momentum Investing": relative momentum plus an absolute (trend) filter that moves to cash in bear markets. Antonacci's absolute filter is the 12-month return vs T-bills; the index > 200-day SMA filter (Faber 2007) is used here as specified for this test.

## Pages
| Page | What is in it |
|---|---|
| [results.md](results.md) | All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks |
| [trades.md](trades.md) | Trade counts, exits, skipped signals, worst trades, spot checks |
| [data.md](data.md) | Data source, universe, data problems, known biases |
| [../index.md](../index.md) | All strategies compared |
