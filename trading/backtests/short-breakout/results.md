# Backtest results: short breakout (Turtle System 1 style, 20-day high / 10-day low)

## Summary
- All variants and periods for short-breakout; the verdict is in [index.md](index.md).
- US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized: 9.6% a year, worst drop -23.6% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py short-breakout`; every number on this page is printed by that script.

## How to read the tables
How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run (every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | full | 4009 | 47.7% | 5.2% | -3.7% | 0.53% | 1.28 | 16 | 12.4% | -24.2% | 81% | 0.82 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 2393 | 49.8% | 4.5% | -3.3% | 0.57% | 1.35 | 17 | 13.8% | -19.2% | 80% | 1.03 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 1616 | 44.6% | 6.3% | -4.2% | 0.47% | 1.20 | 16 | 10.1% | -24.2% | 82% | 0.61 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | full | 4426 | 48.6% | 5.0% | -3.7% | 0.51% | 1.26 | 15 | 11.8% | -23.5% | 79% | 0.80 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 2622 | 50.2% | 4.4% | -3.3% | 0.53% | 1.32 | 15 | 12.7% | -22.5% | 79% | 0.97 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 1804 | 46.3% | 6.0% | -4.3% | 0.47% | 1.20 | 14 | 10.1% | -23.5% | 80% | 0.62 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | full | 3198 | 43.5% | 5.5% | -4.2% | 0.02% | 1.01 | 17 | -2.3% | -54.0% | 78% | -0.10 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 1845 | 43.3% | 5.4% | -4.4% | -0.13% | 0.95 | 17 | -5.3% | -49.6% | 78% | -0.34 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 1353 | 43.8% | 5.6% | -4.0% | 0.22% | 1.10 | 16 | 2.3% | -43.1% | 79% | 0.23 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | full | 3500 | 44.6% | 5.3% | -4.2% | 0.02% | 1.01 | 15 | -2.8% | -59.1% | 78% | -0.14 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 2002 | 44.7% | 5.3% | -4.4% | -0.08% | 0.97 | 15 | -5.1% | -58.2% | 77% | -0.31 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 1498 | 44.5% | 5.3% | -4.0% | 0.14% | 1.06 | 15 | 0.6% | -46.2% | 78% | 0.11 |

## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)
Budget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).

| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | full | 1518 | 47.3% | 5.8% | -3.9% | 0.67% | 1.32 | 16 | 9.6% | -23.6% | 71% | 0.79 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2010-2019 | 865 | 51.1% | 4.9% | -3.4% | 0.80% | 1.47 | 17 | 11.5% | -17.1% | 73% | 1.01 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2020-2026 | 653 | 42.3% | 7.2% | -4.4% | 0.49% | 1.19 | 15 | 6.6% | -23.6% | 68% | 0.53 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | full | 1642 | 48.2% | 5.4% | -4.0% | 0.52% | 1.25 | 14 | 8.2% | -23.6% | 68% | 0.71 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2010-2019 | 933 | 50.5% | 4.6% | -3.5% | 0.60% | 1.34 | 15 | 9.1% | -17.4% | 71% | 0.83 |
| US | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2020-2026 | 709 | 45.3% | 6.5% | -4.6% | 0.43% | 1.17 | 14 | 6.6% | -23.6% | 64% | 0.55 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | full | 1433 | 42.6% | 5.4% | -4.1% | -0.02% | 0.99 | 17 | -1.6% | -42.3% | 72% | -0.07 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2010-2019 | 834 | 42.7% | 5.3% | -4.2% | -0.17% | 0.93 | 17 | -2.9% | -42.3% | 71% | -0.19 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2020-2026 | 599 | 42.6% | 5.7% | -3.9% | 0.18% | 1.08 | 16 | 0.2% | -41.9% | 72% | 0.08 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | full | 1538 | 44.1% | 5.2% | -4.1% | 0.01% | 1.00 | 15 | -1.2% | -49.0% | 71% | -0.04 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2010-2019 | 890 | 44.6% | 5.2% | -4.3% | -0.03% | 0.99 | 16 | -0.9% | -45.7% | 71% | -0.02 |
| India | 35 names | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2020-2026 | 648 | 43.4% | 5.3% | -3.9% | 0.05% | 1.02 | 15 | -1.5% | -47.6% | 71% | -0.07 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized vs SPY
HTML tearsheet: [reports/short-breakout-turtle-US.html](../reports/short-breakout-turtle-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 9.6% | 13.9% |
| Sharpe (rf=0) | 0.79 | 0.85 |
| Sortino (rf=0) | 1.17 | 1.20 |
| Max drawdown | -23.6% | -33.7% |
| Longest drawdown (calendar days) | 570 | 708 |
| Volatility (annual) | 12.6% | 17.1% |
| Best month | 11.3% | 12.7% |
| Worst month | -8.6% | -12.5% |
| Months with a gain (of months with a non-zero return) | 55.9% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.41 | 0.41 |

Engine (same run): CAGR 9.6%, max drawdown -23.6%, Sharpe 0.79. quantstats CAGR 9.6% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### US: Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized vs SPY
HTML tearsheet: [reports/short-breakout-turtle2r-US.html](../reports/short-breakout-turtle2r-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 8.2% | 13.9% |
| Sharpe (rf=0) | 0.71 | 0.85 |
| Sortino (rf=0) | 1.03 | 1.20 |
| Max drawdown | -23.6% | -33.7% |
| Longest drawdown (calendar days) | 740 | 708 |
| Volatility (annual) | 12.1% | 17.1% |
| Best month | 9.5% | 12.7% |
| Worst month | -7.3% | -12.5% |
| Months with a gain (of months with a non-zero return) | 56.4% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.35 | 0.41 |

Engine (same run): CAGR 8.2%, max drawdown -23.6%, Sharpe 0.71. quantstats CAGR 8.2% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized vs ^NSEI
HTML tearsheet: [reports/short-breakout-turtle-India.html](../reports/short-breakout-turtle-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | -1.7% | 10.0% |
| Sharpe (rf=0) | -0.07 | 0.66 |
| Sortino (rf=0) | -0.10 | 0.93 |
| Max drawdown | -42.3% | -38.4% |
| Longest drawdown (calendar days) | 3219 | 1087 |
| Volatility (annual) | 12.5% | 16.4% |
| Best month | 13.1% | 14.7% |
| Worst month | -9.3% | -23.2% |
| Months with a gain (of months with a non-zero return) | 43.6% | 56.2% |
| Calmar (CAGR / max drawdown) | -0.04 | 0.26 |

Engine (same run): CAGR -1.6%, max drawdown -42.3%, Sharpe -0.07. quantstats CAGR -1.7% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized vs ^NSEI
HTML tearsheet: [reports/short-breakout-turtle2r-India.html](../reports/short-breakout-turtle2r-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | -1.2% | 10.0% |
| Sharpe (rf=0) | -0.04 | 0.66 |
| Sortino (rf=0) | -0.05 | 0.93 |
| Max drawdown | -49.0% | -38.4% |
| Longest drawdown (calendar days) | 4307 | 1087 |
| Volatility (annual) | 12.2% | 16.4% |
| Best month | 16.3% | 14.7% |
| Worst month | -9.0% | -23.2% |
| Months with a gain (of months with a non-zero return) | 45.5% | 56.2% |
| Calmar (CAGR / max drawdown) | -0.02 | 0.26 |

Engine (same run): CAGR -1.2%, max drawdown -49.0%, Sharpe -0.04. quantstats CAGR -1.2% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

## Costs and execution
- Signals use the daily close; every fill is at the NEXT trading day's open. Indicators use only data up to the signal day (breakout levels use the prior 50/20 days, excluding the signal day).
- Costs per side, applied to the fill price: US 0.05% slippage, $0 commission (IBKR Lite / Alpaca style). India 0.22% = 0.10% slippage + 0.12% charges (STT 0.1% on delivery buy and sell, exchange fee about 0.003%, SEBI fee, stamp duty 0.015% on buy, GST 18% on fees, DP charge about Rs 16 per sell; zero-brokerage delivery assumed; averaged over both sides).
- Protective stops (where used) fill at the stop price, or at the open if the day opens below the stop (gap), minus costs.
- Cash earns 0%. Dividends are in the adjusted prices (as if reinvested, before tax). No taxes.
- Sharpe ratio: daily returns, risk-free rate 0, annualised with sqrt(252).
- Period splits: in-sample 2010-2019 and out-of-sample 2020-01-01 to 2026-11-13. Sub-period numbers are slices of one continuous run (positions carried across the split), trades are split by entry date. Indicator warm-up (200 days, or 252 days for 12-1 momentum) means the strategies are in cash for most of 2010; benchmarks start on the first bar.

## Benchmarks (buy and hold, adjusted close, no costs; ^NSEI is a price index without dividends, NIFTYBEES includes them)
| Market | Benchmark (buy and hold) | Period | CAGR | Max DD | Sharpe (rf=0) |
|---|---|---|---|---|---|
| US | SPY | full | 13.9% | -33.7% | 0.85 |
| US | SPY | 2010-2019 | 13.3% | -19.3% | 0.92 |
| US | SPY | 2020-2026 | 14.6% | -33.7% | 0.78 |
| India | ^NSEI | full | 9.8% | -38.4% | 0.66 |
| India | ^NSEI | 2010-2019 | 8.8% | -27.9% | 0.64 |
| India | ^NSEI | 2020-2026 | 11.1% | -38.4% | 0.70 |
| India | NIFTYBEES.NS | full | 10.6% | -36.3% | 0.72 |
| India | NIFTYBEES.NS | 2010-2019 | 9.5% | -27.3% | 0.65 |
| India | NIFTYBEES.NS | 2020-2026 | 12.3% | -36.3% | 0.83 |

Sanity check: engine buy-and-hold CAGR vs direct (last adjusted close / first adjusted close) ^ (1/years) - 1: SPY engine 13.88% vs direct 13.88%; ^NSEI engine 9.76% vs direct 9.76%; NIFTYBEES.NS engine 10.61% vs direct 10.61%
