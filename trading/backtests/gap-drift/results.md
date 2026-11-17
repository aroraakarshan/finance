# Backtest results: gap-up drift (post-earnings-announcement drift proxy)

## Summary
- All variants and periods for gap-drift; the verdict is in [index.md](index.md).
- US, Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized: 1.1% a year, worst drop -5.0% (SPY 13.9%, -33.7%).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py gap-drift`; every number on this page is printed by that script.

## How to read the tables
How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run (every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).

## Results by variant and period
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | full | 110 | 52.7% | 5.6% | -4.0% | 1.08% | 1.57 | 11 | 1.4% | -6.0% | 4% | 0.45 |
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 75 | 57.3% | 5.3% | -3.5% | 1.54% | 2.03 | 11 | 2.3% | -4.8% | 5% | 0.75 |
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 35 | 42.9% | 6.5% | -4.7% | 0.09% | 1.03 | 9 | 0.0% | -6.0% | 2% | 0.03 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | full | 54 | 50.0% | 5.3% | -4.6% | 0.39% | 1.17 | 14 | 0.2% | -5.8% | 3% | 0.12 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2010-2019 | 31 | 54.8% | 4.1% | -4.8% | 0.05% | 1.02 | 17 | 0.0% | -4.7% | 3% | 0.02 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop (every signal / 5 slots x 20%) | 2020-2026 | 23 | 43.5% | 7.5% | -4.2% | 0.86% | 1.36 | 11 | 0.5% | -5.8% | 2% | 0.23 |

## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)
Budget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).

| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | full | 108 | 52.8% | 5.6% | -4.0% | 1.05% | 1.56 | 11 | 1.1% | -5.0% | 3% | 0.52 |
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | 2010-2019 | 75 | 57.3% | 5.3% | -3.5% | 1.54% | 2.03 | 11 | 2.0% | -4.1% | 4% | 0.80 |
| US | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | 2020-2026 | 33 | 42.4% | 6.5% | -4.9% | -0.05% | 0.98 | 9 | -0.1% | -5.0% | 2% | -0.02 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | full | 54 | 50.0% | 5.3% | -4.6% | 0.39% | 1.17 | 14 | 0.2% | -5.4% | 2% | 0.10 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | 2010-2019 | 31 | 54.8% | 4.1% | -4.8% | 0.05% | 1.02 | 17 | 0.2% | -3.6% | 3% | 0.10 |
| India | 35 names | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | 2020-2026 | 23 | 43.5% | 7.5% | -4.2% | 0.86% | 1.36 | 11 | 0.2% | -5.4% | 2% | 0.10 |

## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)

### US: Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized vs SPY
HTML tearsheet: [reports/gap-drift-US.html](../reports/gap-drift-US.html)

| Metric (quantstats, 35 names) | Strategy | SPY |
|---|---|---|
| CAGR | 1.1% | 13.9% |
| Sharpe (rf=0) | 0.52 | 0.85 |
| Sortino (rf=0) | 0.80 | 1.20 |
| Max drawdown | -5.0% | -33.7% |
| Longest drawdown (calendar days) | 2264 | 708 |
| Volatility (annual) | 2.2% | 17.1% |
| Best month | 3.9% | 12.7% |
| Worst month | -1.5% | -12.5% |
| Months with a gain (of months with a non-zero return) | 54.4% | 67.5% |
| Calmar (CAGR / max drawdown) | 0.23 | 0.41 |

Engine (same run): CAGR 1.1%, max drawdown -5.0%, Sharpe 0.52. quantstats CAGR 1.1% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

### India: Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized vs ^NSEI
HTML tearsheet: [reports/gap-drift-India.html](../reports/gap-drift-India.html)

| Metric (quantstats, 35 names) | Strategy | ^NSEI |
|---|---|---|
| CAGR | 0.2% | 10.0% |
| Sharpe (rf=0) | 0.10 | 0.66 |
| Sortino (rf=0) | 0.14 | 0.93 |
| Max drawdown | -5.4% | -38.4% |
| Longest drawdown (calendar days) | 2297 | 1087 |
| Volatility (annual) | 1.9% | 16.4% |
| Best month | 5.3% | 14.7% |
| Worst month | -2.5% | -23.2% |
| Months with a gain (of months with a non-zero return) | 46.4% | 56.2% |
| Calmar (CAGR / max drawdown) | 0.03 | 0.26 |

Engine (same run): CAGR 0.2%, max drawdown -5.4%, Sharpe 0.10. quantstats CAGR 0.2% counts years as trading days / 252; the engine uses calendar days / 365.25. Max drawdown is the same calculation in both.

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
