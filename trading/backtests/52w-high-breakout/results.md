# Backtest results: 52-week-high breakout on volume (George and Hwang 2004)

## Summary
- All variants and periods for 52w-high-breakout; the verdict is in [index.md](index.md).
- US, 52-week high on 1.5x volume, 2R target, 20 days, rules-sized: 6.1% a year, worst drop -10.7% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py 52w-high-breakout`; every number on this page is printed by that script.

## How to read the tables
How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run (every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | full | 877 | 48.8% | 6.1% | -4.1% | 0.90% | 1.43 | 17 | 7.4% | -19.9% | 40% | 0.76 |
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 532 | 49.4% | 5.0% | -3.7% | 0.65% | 1.35 | 18 | 4.8% | -12.0% | 42% | 0.61 |
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 345 | 47.8% | 7.8% | -4.7% | 1.29% | 1.53 | 15 | 11.1% | -19.9% | 37% | 0.93 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | full | 835 | 40.0% | 5.7% | -4.5% | -0.43% | 0.84 | 18 | -3.5% | -47.5% | 39% | -0.34 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 428 | 38.8% | 5.5% | -4.6% | -0.70% | 0.75 | 18 | -5.8% | -47.5% | 36% | -0.64 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 407 | 41.3% | 6.0% | -4.4% | -0.15% | 0.94 | 18 | -0.1% | -33.2% | 45% | 0.04 |

## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)
Budget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).

| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | full | 711 | 48.8% | 6.3% | -4.1% | 0.94% | 1.44 | 17 | 6.1% | -10.7% | 35% | 0.79 |
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | 2010-2019 | 421 | 48.9% | 5.0% | -3.8% | 0.54% | 1.28 | 18 | 3.5% | -10.7% | 39% | 0.51 |
| US | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | 2020-2026 | 290 | 48.6% | 8.1% | -4.7% | 1.52% | 1.63 | 15 | 9.8% | -10.0% | 29% | 1.14 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | full | 655 | 40.6% | 5.7% | -4.7% | -0.45% | 0.84 | 18 | -3.3% | -45.0% | 36% | -0.37 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | 2010-2019 | 347 | 38.9% | 5.4% | -4.7% | -0.78% | 0.73 | 19 | -4.7% | -41.1% | 33% | -0.59 |
| India | 35 names | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | 2020-2026 | 308 | 42.5% | 5.9% | -4.6% | -0.09% | 0.97 | 18 | -1.2% | -33.5% | 40% | -0.10 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: 52-week high on 1.5x volume, 2R target, 20 days, rules-sized vs SPY
HTML tearsheet: [reports/52w-high-breakout-US.html](../reports/52w-high-breakout-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 6.1% | 13.9% |
| Sharpe (rf=0) | 0.79 | 0.85 |
| Sortino (rf=0) | 1.20 | 1.20 |
| Max drawdown | -10.7% | -33.7% |
| Longest drawdown (calendar days) | 753 | 708 |
| Volatility (annual) | 7.9% | 17.1% |
| Best month | 9.2% | 12.7% |
| Worst month | -4.6% | -12.5% |
| Months with a gain (of months with a non-zero return) | 57.4% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.57 | 0.41 |

Engine (same run): CAGR 6.1%, max drawdown -10.7%, Sharpe 0.79. quantstats CAGR 6.1% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: 52-week high on 1.5x volume, 2R target, 20 days, rules-sized vs ^NSEI
HTML tearsheet: [reports/52w-high-breakout-India.html](../reports/52w-high-breakout-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | -3.4% | 10.0% |
| Sharpe (rf=0) | -0.37 | 0.66 |
| Sortino (rf=0) | -0.50 | 0.93 |
| Max drawdown | -45.0% | -38.4% |
| Longest drawdown (calendar days) | 5776 | 1087 |
| Volatility (annual) | 8.3% | 16.4% |
| Best month | 8.9% | 14.7% |
| Worst month | -8.1% | -23.2% |
| Months with a gain (of months with a non-zero return) | 38.6% | 56.2% |
| Calmar (CAGR / max drawdown) | -0.07 | 0.26 |

Engine (same run): CAGR -3.3%, max drawdown -45.0%, Sharpe -0.37. quantstats CAGR -3.4% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

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
