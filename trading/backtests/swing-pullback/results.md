# Backtest results: swing pullback (Connors RSI(2) in an uptrend)

## Summary
- All variants and periods for swing-pullback; the verdict is in [index.md](index.md).
- US, RSI(2), rules stop, rules-sized: 1.4% a year, worst drop -13.7% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py swing-pullback`; every number on this page is printed by that script.

## How to read the tables
How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run (every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | full | 4866 | 65.9% | 1.8% | -2.4% | 0.37% | 1.45 | 5 | 9.6% | -17.1% | 49% | 0.74 |
| US | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | 2010-2019 | 2849 | 65.8% | 1.7% | -2.1% | 0.36% | 1.49 | 5 | 9.5% | -17.1% | 46% | 0.86 |
| US | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | 2020-2026 | 2017 | 66.1% | 2.0% | -2.7% | 0.38% | 1.41 | 5 | 9.7% | -15.8% | 52% | 0.64 |
| US | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | full | 7189 | 43.6% | 2.0% | -1.3% | 0.10% | 1.14 | 2 | 3.8% | -17.1% | 35% | 0.41 |
| US | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | 2010-2019 | 4190 | 43.3% | 1.8% | -1.2% | 0.09% | 1.13 | 2 | 2.3% | -17.1% | 33% | 0.30 |
| US | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | 2020-2026 | 2999 | 43.9% | 2.2% | -1.5% | 0.12% | 1.15 | 2 | 5.9% | -13.6% | 37% | 0.52 |
| US | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | full | 5485 | 64.2% | 1.9% | -2.7% | 0.27% | 1.28 | 4 | 6.5% | -20.6% | 45% | 0.57 |
| US | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | 2010-2019 | 3217 | 64.3% | 1.7% | -2.4% | 0.27% | 1.31 | 4 | 5.7% | -20.6% | 43% | 0.58 |
| US | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | 2020-2026 | 2268 | 64.1% | 2.1% | -3.0% | 0.27% | 1.25 | 4 | 7.6% | -16.5% | 48% | 0.58 |
| India | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | full | 3814 | 57.8% | 1.7% | -2.6% | -0.10% | 0.91 | 6 | -5.9% | -67.0% | 47% | -0.43 |
| India | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | 2010-2019 | 2132 | 59.3% | 1.8% | -2.7% | -0.05% | 0.95 | 6 | -4.1% | -41.0% | 46% | -0.30 |
| India | 35 names | RSI2, no stop (every signal / 5 slots x 20%) | 2020-2026 | 1682 | 55.8% | 1.7% | -2.5% | -0.17% | 0.85 | 6 | -8.6% | -47.5% | 50% | -0.59 |
| India | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | full | 6277 | 34.1% | 1.9% | -1.6% | -0.41% | 0.62 | 2 | -21.7% | -98.4% | 29% | -2.52 |
| India | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | 2010-2019 | 3514 | 34.3% | 2.0% | -1.6% | -0.41% | 0.62 | 2 | -21.1% | -90.9% | 27% | -2.47 |
| India | 35 names | RSI2, with rules stop (every signal / 5 slots x 20%) | 2020-2026 | 2763 | 33.8% | 1.9% | -1.6% | -0.41% | 0.61 | 2 | -22.5% | -82.9% | 32% | -2.58 |
| India | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | full | 4288 | 57.3% | 1.8% | -3.0% | -0.22% | 0.82 | 5 | -9.1% | -81.3% | 44% | -0.78 |
| India | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | 2010-2019 | 2390 | 58.9% | 1.8% | -3.1% | -0.19% | 0.85 | 5 | -7.3% | -57.9% | 42% | -0.61 |
| India | 35 names | RSI2, 2xATR stop only (not rule-compliant, comparison) (every signal / 5 slots x 20%) | 2020-2026 | 1898 | 55.2% | 1.8% | -2.8% | -0.26% | 0.79 | 5 | -11.5% | -58.0% | 46% | -1.01 |

## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)
Budget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).

| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | rules-sized | full | 2100 | 44.3% | 1.9% | -1.3% | 0.11% | 1.14 | 2 | 1.4% | -13.7% | 14% | 0.29 |
| US | 35 names | rules-sized | 2010-2019 | 1202 | 44.0% | 1.7% | -1.2% | 0.09% | 1.13 | 2 | 1.3% | -9.3% | 14% | 0.29 |
| US | 35 names | rules-sized | 2020-2026 | 898 | 44.7% | 2.2% | -1.5% | 0.13% | 1.15 | 2 | 1.4% | -13.7% | 14% | 0.28 |
| India | 35 names | rules-sized | full | 2077 | 36.4% | 1.8% | -1.7% | -0.39% | 0.63 | 2 | -8.8% | -79.3% | 13% | -1.71 |
| India | 35 names | rules-sized | 2010-2019 | 1197 | 36.2% | 1.9% | -1.7% | -0.39% | 0.63 | 2 | -8.9% | -61.6% | 12% | -1.75 |
| India | 35 names | rules-sized | 2020-2026 | 880 | 36.6% | 1.8% | -1.7% | -0.40% | 0.63 | 2 | -8.6% | -46.2% | 14% | -1.65 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: RSI(2), rules stop, rules-sized vs SPY
HTML tearsheet: [reports/swing-pullback-US.html](../reports/swing-pullback-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 1.4% | 13.9% |
| Sharpe (rf=0) | 0.29 | 0.85 |
| Sortino (rf=0) | 0.43 | 1.20 |
| Max drawdown | -13.7% | -33.7% |
| Longest drawdown (calendar days) | 1128 | 708 |
| Volatility (annual) | 5.1% | 17.1% |
| Best month | 5.5% | 12.7% |
| Worst month | -5.4% | -12.5% |
| Months with a gain (of months with a non-zero return) | 53.4% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.10 | 0.41 |

Engine (same run): CAGR 1.4%, max drawdown -13.7%, Sharpe 0.29. quantstats CAGR 1.4% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: RSI(2), rules stop, rules-sized vs ^NSEI
HTML tearsheet: [reports/swing-pullback-India.html](../reports/swing-pullback-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | -9.0% | 10.0% |
| Sharpe (rf=0) | -1.71 | 0.66 |
| Sortino (rf=0) | -2.20 | 0.93 |
| Max drawdown | -79.3% | -38.4% |
| Longest drawdown (calendar days) | 5842 | 1087 |
| Volatility (annual) | 5.4% | 16.4% |
| Best month | 3.2% | 14.7% |
| Worst month | -6.9% | -23.2% |
| Months with a gain (of months with a non-zero return) | 28.9% | 56.2% |
| Calmar (CAGR / max drawdown) | -0.11 | 0.26 |

Engine (same run): CAGR -8.8%, max drawdown -79.3%, Sharpe -1.71. quantstats CAGR -9.0% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

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
