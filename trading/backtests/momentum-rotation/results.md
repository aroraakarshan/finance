# Backtest results: momentum rotation (top-5 12-1 month momentum with index trend filter)

## Summary
- All variants and periods for momentum-rotation; the verdict is in [index.md](index.md).
- US, Top-5 12-1 momentum, index filter: 17.1% a year, worst drop -38.5% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py momentum-rotation`; every number on this page is printed by that script.

## How to read the tables
How to read the table: each row is a portfolio run. Trades are holding spans (from the open where a name is bought to the open where it is sold; monthly top-ups between are ignored), returns net of costs. Exposure = average share of equity invested.

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Top-5 12-1 momentum, index > SMA200 filter | full | 231 | 55.0% | 22.1% | -8.0% | 8.56% | 3.37 | 106 | 17.1% | -38.5% | 79% | 0.80 |
| US | 35 names | Top-5 12-1 momentum, index > SMA200 filter | 2010-2019 | 137 | 64.2% | 19.5% | -7.5% | 9.83% | 4.67 | 105 | 18.6% | -38.5% | 79% | 0.96 |
| US | 35 names | Top-5 12-1 momentum, index > SMA200 filter | 2020-2026 | 94 | 41.5% | 28.1% | -8.5% | 6.70% | 2.35 | 107 | 14.5% | -34.7% | 80% | 0.63 |
| US | 35 names | Top-5 12-1 momentum, no filter | full | 215 | 62.8% | 28.0% | -7.7% | 14.68% | 6.09 | 134 | 27.8% | -32.7% | 94% | 1.05 |
| US | 35 names | Top-5 12-1 momentum, no filter | 2010-2019 | 130 | 70.0% | 23.1% | -7.0% | 14.07% | 7.66 | 129 | 24.6% | -32.7% | 89% | 1.10 |
| US | 35 names | Top-5 12-1 momentum, no filter | 2020-2026 | 85 | 51.8% | 38.0% | -8.4% | 15.60% | 4.85 | 142 | 32.1% | -31.1% | 100% | 1.02 |
| US | 35 names | Equal-weight buy and hold of the same stocks | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 21.1% | -30.7% | 99% | 1.16 |
| US | 35 names | Equal-weight buy and hold of the same stocks | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 20.4% | -20.0% | 99% | 1.27 |
| US | 35 names | Equal-weight buy and hold of the same stocks | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 21.9% | -30.7% | 100% | 1.06 |
| India | 35 names | Top-5 12-1 momentum, index > SMA200 filter | full | 225 | 56.9% | 14.5% | -6.5% | 5.44% | 2.94 | 91 | 13.7% | -22.1% | 66% | 0.93 |
| India | 35 names | Top-5 12-1 momentum, index > SMA200 filter | 2010-2019 | 133 | 58.6% | 14.1% | -7.1% | 5.32% | 2.81 | 87 | 13.0% | -22.1% | 63% | 0.97 |
| India | 35 names | Top-5 12-1 momentum, index > SMA200 filter | 2020-2026 | 92 | 54.3% | 15.1% | -5.7% | 5.63% | 3.16 | 96 | 14.9% | -18.9% | 72% | 0.91 |
| India | 35 names | Top-5 12-1 momentum, no filter | full | 255 | 54.1% | 19.4% | -7.7% | 6.97% | 2.98 | 113 | 15.6% | -36.3% | 94% | 0.87 |
| India | 35 names | Top-5 12-1 momentum, no filter | 2010-2019 | 146 | 57.5% | 21.4% | -7.9% | 8.94% | 3.66 | 114 | 19.5% | -22.1% | 89% | 1.16 |
| India | 35 names | Top-5 12-1 momentum, no filter | 2020-2026 | 109 | 49.5% | 16.3% | -7.4% | 4.34% | 2.16 | 111 | 10.3% | -36.3% | 100% | 0.56 |
| India | 35 names | Equal-weight buy and hold of the same stocks | full | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 18.0% | -34.3% | 100% | 1.18 |
| India | 35 names | Equal-weight buy and hold of the same stocks | 2010-2019 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 17.6% | -18.4% | 99% | 1.23 |
| India | 35 names | Equal-weight buy and hold of the same stocks | 2020-2026 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 18.5% | -34.3% | 100% | 1.12 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: Top-5 12-1 momentum, index filter vs SPY
HTML tearsheet: [reports/momentum-rotation-US.html](../reports/momentum-rotation-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 17.1% | 13.9% |
| Sharpe (rf=0) | 0.80 | 0.85 |
| Sortino (rf=0) | 1.15 | 1.20 |
| Max drawdown | -38.5% | -33.7% |
| Longest drawdown (calendar days) | 800 | 708 |
| Volatility (annual) | 23.1% | 17.1% |
| Best month | 16.4% | 12.7% |
| Worst month | -21.6% | -12.5% |
| Months with a gain (of months with a non-zero return) | 62.6% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.45 | 0.41 |

Engine (same run): CAGR 17.1%, max drawdown -38.5%, Sharpe 0.80. quantstats CAGR 17.1% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Top-5 12-1 momentum, index filter vs ^NSEI
HTML tearsheet: [reports/momentum-rotation-India.html](../reports/momentum-rotation-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | 14.1% | 10.0% |
| Sharpe (rf=0) | 0.93 | 0.66 |
| Sortino (rf=0) | 1.33 | 0.93 |
| Max drawdown | -22.1% | -38.4% |
| Longest drawdown (calendar days) | 834 | 1087 |
| Volatility (annual) | 15.4% | 16.4% |
| Best month | 19.1% | 14.7% |
| Worst month | -11.4% | -23.2% |
| Months with a gain (of months with a non-zero return) | 63.3% | 56.2% |
| Calmar (CAGR / max drawdown) | 0.64 | 0.26 |

Engine (same run): CAGR 13.7%, max drawdown -22.1%, Sharpe 0.93. quantstats CAGR 14.1% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

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
