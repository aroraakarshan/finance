# Backtest results: trend following (Faber SMA200 timing and Donchian 50/20 breakout)

## Summary
- All variants and periods for trend-following; the verdict is in [index.md](index.md).
- US, Faber SMA200 monthly, stocks: 13.1% a year, worst drop -17.9% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py trend-following`; every number on this page is printed by that script.

## How to read the tables
How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run (every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Faber SMA200 monthly, ETFs | full | 108 | 44.4% | 24.9% | -4.9% | 8.34% | 4.07 | 267 | 6.4% | -11.4% | 67% | 0.75 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 10.0% | -27.2% | 100% | 0.79 |
| US | 35 names | Faber SMA200 monthly, ETFs | 2010-2019 | 63 | 39.7% | 23.4% | -5.3% | 6.09% | 2.92 | 283 | 4.8% | -11.4% | 66% | 0.63 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 9.8% | -14.7% | 99% | 0.88 |
| US | 35 names | Faber SMA200 monthly, ETFs | 2020-2026 | 45 | 51.1% | 26.6% | -4.3% | 11.50% | 6.53 | 246 | 8.7% | -10.8% | 69% | 0.89 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 10.2% | -27.2% | 100% | 0.71 |
| US | 35 names | Faber SMA200 monthly, stocks | full | 536 | 45.5% | 51.7% | -7.0% | 19.72% | 6.15 | 262 | 13.1% | -17.9% | 69% | 1.16 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 21.1% | -30.7% | 99% | 1.16 |
| US | 35 names | Faber SMA200 monthly, stocks | 2010-2019 | 311 | 45.7% | 54.2% | -6.5% | 21.23% | 7.03 | 286 | 12.2% | -14.4% | 70% | 1.14 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 20.4% | -20.0% | 99% | 1.27 |
| US | 35 names | Faber SMA200 monthly, stocks | 2020-2026 | 225 | 45.3% | 48.3% | -7.8% | 17.64% | 5.14 | 229 | 14.1% | -17.9% | 69% | 1.17 |
| US | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 21.9% | -30.7% | 100% | 1.06 |
| US | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | full | 1253 | 48.4% | 12.9% | -5.9% | 3.21% | 2.06 | 73 | 15.0% | -26.6% | 88% | 0.91 |
| US | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | 2010-2019 | 757 | 49.0% | 11.0% | -5.0% | 2.81% | 2.09 | 75 | 14.5% | -20.8% | 87% | 1.01 |
| US | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | 2020-2026 | 496 | 47.6% | 15.8% | -7.1% | 3.82% | 2.03 | 71 | 15.3% | -26.6% | 90% | 0.81 |
| US | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | full | 1482 | 39.0% | 12.6% | -4.2% | 2.37% | 1.94 | 54 | 14.2% | -21.6% | 85% | 0.91 |
| US | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | 2010-2019 | 890 | 40.0% | 10.5% | -3.8% | 1.92% | 1.84 | 56 | 12.1% | -21.6% | 84% | 0.92 |
| US | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | 2020-2026 | 592 | 37.5% | 15.9% | -4.6% | 3.05% | 2.05 | 51 | 17.0% | -16.9% | 86% | 0.92 |
| India | 35 names | Faber SMA200 monthly, ETFs | full | 48 | 43.8% | 27.6% | -5.5% | 8.94% | 3.87 | 247 | 6.8% | -16.0% | 64% | 0.80 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 12.8% | -28.8% | 93% | 1.06 |
| India | 35 names | Faber SMA200 monthly, ETFs | 2010-2019 | 31 | 38.7% | 23.5% | -6.3% | 5.20% | 2.34 | 217 | 3.9% | -14.8% | 57% | 0.54 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 11.6% | -17.8% | 88% | 1.07 |
| India | 35 names | Faber SMA200 monthly, ETFs | 2020-2026 | 17 | 52.9% | 33.0% | -3.7% | 15.75% | 10.11 | 303 | 11.0% | -16.0% | 75% | 1.10 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), ETFs | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 14.6% | -28.8% | 100% | 1.07 |
| India | 35 names | Faber SMA200 monthly, stocks | full | 513 | 37.0% | 44.7% | -7.4% | 11.90% | 3.55 | 230 | 8.6% | -15.3% | 64% | 0.94 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 18.0% | -34.3% | 100% | 1.18 |
| India | 35 names | Faber SMA200 monthly, stocks | 2010-2019 | 302 | 34.8% | 44.8% | -8.1% | 10.29% | 2.94 | 233 | 7.4% | -14.7% | 62% | 0.85 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 17.6% | -18.4% | 99% | 1.23 |
| India | 35 names | Faber SMA200 monthly, stocks | 2020-2026 | 211 | 40.3% | 44.5% | -6.3% | 14.20% | 4.78 | 226 | 10.5% | -15.3% | 67% | 1.06 |
| India | 35 names | Equal-weight buy and hold (monthly rebalance), stocks | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 18.5% | -34.3% | 100% | 1.12 |
| India | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | full | 1032 | 42.2% | 14.3% | -6.2% | 2.49% | 1.70 | 75 | 10.6% | -32.1% | 88% | 0.76 |
| India | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | 2010-2019 | 593 | 41.5% | 14.4% | -6.5% | 2.13% | 1.56 | 78 | 10.2% | -32.1% | 87% | 0.75 |
| India | 35 names | Donchian 50/20, stocks, no stop (every signal / 5 slots x 20%) | 2020-2026 | 439 | 43.3% | 14.3% | -5.7% | 2.97% | 1.92 | 71 | 11.3% | -31.8% | 90% | 0.76 |
| India | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | full | 1247 | 31.8% | 14.5% | -4.7% | 1.42% | 1.44 | 52 | 5.7% | -35.6% | 82% | 0.46 |
| India | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | 2010-2019 | 711 | 31.2% | 14.5% | -4.9% | 1.18% | 1.35 | 54 | 4.1% | -35.6% | 81% | 0.36 |
| India | 35 names | Donchian 50/20, stocks, with rules stop (every signal / 5 slots x 20%) | 2020-2026 | 536 | 32.6% | 14.5% | -4.4% | 1.74% | 1.58 | 49 | 8.2% | -32.3% | 85% | 0.58 |

## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)
Budget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).

| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | rules-sized | full | 467 | 41.8% | 12.8% | -4.3% | 2.81% | 2.12 | 56 | 13.1% | -23.1% | 79% | 0.95 |
| US | 35 names | rules-sized | 2010-2019 | 267 | 44.2% | 10.2% | -4.0% | 2.28% | 2.02 | 58 | 12.0% | -23.1% | 80% | 0.96 |
| US | 35 names | rules-sized | 2020-2026 | 200 | 38.5% | 16.7% | -4.7% | 3.52% | 2.21 | 53 | 14.5% | -13.4% | 78% | 0.94 |
| India | 35 names | rules-sized | full | 467 | 31.3% | 15.4% | -4.8% | 1.52% | 1.46 | 54 | 5.1% | -33.0% | 79% | 0.44 |
| India | 35 names | rules-sized | 2010-2019 | 273 | 30.4% | 14.6% | -4.8% | 1.11% | 1.33 | 55 | 3.9% | -33.0% | 77% | 0.36 |
| India | 35 names | rules-sized | 2020-2026 | 194 | 32.5% | 16.3% | -4.7% | 2.10% | 1.66 | 54 | 7.0% | -31.6% | 82% | 0.54 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: Faber SMA200 monthly, stocks vs SPY
HTML tearsheet: [reports/trend-following-faber-US.html](../reports/trend-following-faber-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 13.1% | 13.9% |
| Sharpe (rf=0) | 1.16 | 0.85 |
| Sortino (rf=0) | 1.63 | 1.20 |
| Max drawdown | -17.9% | -33.7% |
| Longest drawdown (calendar days) | 529 | 708 |
| Volatility (annual) | 11.2% | 17.1% |
| Best month | 9.3% | 12.7% |
| Worst month | -6.9% | -12.5% |
| Months with a gain (of months with a non-zero return) | 67.9% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.73 | 0.41 |

Engine (same run): CAGR 13.1%, max drawdown -17.9%, Sharpe 1.16. quantstats CAGR 13.1% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### US: Donchian 50/20, rules stop, rules-sized vs SPY
HTML tearsheet: [reports/trend-following-donchian-US.html](../reports/trend-following-donchian-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 13.2% | 13.9% |
| Sharpe (rf=0) | 0.95 | 0.85 |
| Sortino (rf=0) | 1.39 | 1.20 |
| Max drawdown | -23.1% | -33.7% |
| Longest drawdown (calendar days) | 592 | 708 |
| Volatility (annual) | 14.0% | 17.1% |
| Best month | 16.1% | 12.7% |
| Worst month | -8.2% | -12.5% |
| Months with a gain (of months with a non-zero return) | 58.7% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.57 | 0.41 |

Engine (same run): CAGR 13.1%, max drawdown -23.1%, Sharpe 0.95. quantstats CAGR 13.2% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Faber SMA200 monthly, stocks vs ^NSEI
HTML tearsheet: [reports/trend-following-faber-India.html](../reports/trend-following-faber-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | 8.8% | 10.0% |
| Sharpe (rf=0) | 0.94 | 0.66 |
| Sortino (rf=0) | 1.34 | 0.93 |
| Max drawdown | -15.3% | -38.4% |
| Longest drawdown (calendar days) | 785 | 1087 |
| Volatility (annual) | 9.5% | 16.4% |
| Best month | 9.3% | 14.7% |
| Worst month | -7.9% | -23.2% |
| Months with a gain (of months with a non-zero return) | 62.2% | 56.2% |
| Calmar (CAGR / max drawdown) | 0.58 | 0.26 |

Engine (same run): CAGR 8.6%, max drawdown -15.3%, Sharpe 0.94. quantstats CAGR 8.8% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Donchian 50/20, rules stop, rules-sized vs ^NSEI
HTML tearsheet: [reports/trend-following-donchian-India.html](../reports/trend-following-donchian-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | 5.2% | 10.0% |
| Sharpe (rf=0) | 0.44 | 0.66 |
| Sortino (rf=0) | 0.61 | 0.93 |
| Max drawdown | -33.0% | -38.4% |
| Longest drawdown (calendar days) | 2282 | 1087 |
| Volatility (annual) | 14.0% | 16.4% |
| Best month | 14.8% | 14.7% |
| Worst month | -9.0% | -23.2% |
| Months with a gain (of months with a non-zero return) | 51.7% | 56.2% |
| Calmar (CAGR / max drawdown) | 0.16 | 0.26 |

Engine (same run): CAGR 5.1%, max drawdown -33.0%, Sharpe 0.44. quantstats CAGR 5.2% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

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
