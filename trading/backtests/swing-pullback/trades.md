# Backtest trades: swing pullback (Connors RSI(2) in an uptrend)

## Summary
- Trade-level detail for swing-pullback: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py swing-pullback`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | RSI2, no stop | every-signal trades by exit: exit rule 4746, time stop 119, open at end 1 |
| US | RSI2, with rules stop | every-signal trades by exit: exit rule 3628, stop 3560, time stop 1 |
| US | RSI2, 2xATR stop only (not rule-compliant, comparison) | every-signal trades by exit: exit rule 4447, stop 1030, time stop 8 |
| US | RSI2 rules-sized | budget 2,128 USD, final equity 2,681 USD; trades by exit: exit rule 1090, stop 1009, time stop 1; signals skipped: max_pos 118, week_limit 6691, price_above_cap 53, cash 0 |
| India | RSI2, no stop | every-signal trades by exit: exit rule 3690, time stop 122, open at end 2 |
| India | RSI2, with rules stop | every-signal trades by exit: stop 3695, exit rule 2577, time stop 5 |
| India | RSI2, 2xATR stop only (not rule-compliant, comparison) | every-signal trades by exit: exit rule 3465, stop 808, time stop 13, open at end 2 |
| India | RSI2 rules-sized | budget 200,000 INR, final equity 42,434 INR; trades by exit: stop 1157, exit rule 918, time stop 2; signals skipped: max_pos 37, week_limit 5319, price_above_cap 26, cash 0 |

### Worst 5 trades: US, RSI2, no stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BAC | 2020-02-25 | 27.77 | 2020-03-10 | 19.88 | time stop | -28.5% |
| AMD | 2018-10-22 | 24.46 | 2018-11-01 | 18.41 | exit rule | -24.8% |
| NVDA | 2026-11-02 | 207.53 | 2026-11-13 | 162.85 | open at end | -21.6% |
| ORCL | 2026-06-10 | 197.08 | 2026-06-25 | 156.23 | time stop | -20.8% |
| HD | 2011-07-28 | 24.90 | 2011-08-11 | 19.80 | time stop | -20.6% |

### Worst 5 trades: US, RSI2, with rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| CRM | 2024-05-24 | 266.20 | 2024-05-30 | 219.50 | stop | -17.6% |
| QCOM | 2019-05-21 | 66.36 | 2019-05-22 | 58.13 | stop | -12.5% |
| NVDA | 2020-03-10 | 6.37 | 2020-03-12 | 5.60 | stop | -12.2% |
| META | 2015-08-21 | 86.69 | 2015-08-24 | 76.30 | stop | -12.1% |
| LLY | 2024-10-25 | 886.23 | 2024-10-30 | 786.52 | exit rule | -11.3% |

### Worst 5 trades: US, RSI2, 2xATR stop only (not rule-compliant, comparison)
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| AMD | 2018-10-22 | 24.46 | 2018-10-25 | 17.92 | stop | -26.8% |
| CRM | 2024-05-24 | 266.20 | 2024-05-30 | 219.50 | stop | -17.6% |
| QCOM | 2019-05-21 | 66.36 | 2019-05-22 | 58.13 | stop | -12.5% |
| NVDA | 2020-03-10 | 6.37 | 2020-03-12 | 5.60 | stop | -12.2% |
| META | 2015-08-21 | 86.69 | 2015-08-24 | 76.30 | stop | -12.1% |

### Worst 5 trades: US, RSI2 rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| QCOM | 2019-05-21 | 66.36 | 2019-05-22 | 58.13 | stop | -12.5% |
| INTC | 2026-10-12 | 102.52 | 2026-10-15 | 92.27 | stop | -10.1% |
| INTC | 2026-07-08 | 108.30 | 2026-07-16 | 97.47 | stop | -10.1% |
| CSCO | 2012-05-07 | 12.37 | 2012-05-10 | 11.17 | stop | -9.8% |
| ADBE | 2020-03-10 | 318.98 | 2020-03-12 | 290.41 | stop | -9.0% |

### Worst 5 trades: India, RSI2, no stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ICICIBANK.NS | 2020-03-09 | 455.57 | 2020-03-24 | 283.22 | time stop | -38.1% |
| TITAN.NS | 2020-03-11 | 1171.24 | 2020-03-25 | 781.18 | time stop | -33.6% |
| BAJFINANCE.NS | 2016-11-01 | 104.95 | 2016-11-16 | 79.85 | time stop | -24.3% |
| RELIANCE.NS | 2020-02-26 | 627.86 | 2020-03-12 | 483.14 | time stop | -23.4% |
| BAJFINANCE.NS | 2020-03-02 | 446.82 | 2020-03-17 | 360.43 | time stop | -19.7% |

### Worst 5 trades: India, RSI2, with rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ADANIPORTS.NS | 2021-06-15 | 776.12 | 2021-06-16 | 698.51 | stop | -10.4% |
| HINDUNILVR.NS | 2020-05-04 | 1887.46 | 2020-05-07 | 1698.71 | stop | -10.4% |
| BAJFINANCE.NS | 2016-11-10 | 91.72 | 2016-11-11 | 82.88 | stop | -10.0% |
| SUNPHARMA.NS | 2015-04-20 | 957.21 | 2015-04-21 | 868.61 | stop | -9.7% |
| BAJFINANCE.NS | 2018-09-24 | 234.86 | 2018-09-24 | 213.55 | stop | -9.5% |

### Worst 5 trades: India, RSI2, 2xATR stop only (not rule-compliant, comparison)
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| WIPRO.NS | 2013-04-10 | 62.62 | 2013-04-22 | 54.89 | stop | -12.7% |
| JSWSTEEL.NS | 2025-04-04 | 1023.65 | 2025-04-07 | 898.41 | stop | -12.6% |
| NESTLEIND.NS | 2020-03-17 | 674.30 | 2020-03-19 | 604.57 | stop | -10.7% |
| BAJFINANCE.NS | 2016-11-15 | 83.86 | 2016-11-15 | 75.48 | stop | -10.4% |
| HINDUNILVR.NS | 2020-05-04 | 1887.46 | 2020-05-07 | 1698.71 | stop | -10.4% |

### Worst 5 trades: India, RSI2 rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| HINDUNILVR.NS | 2020-05-04 | 1887.46 | 2020-05-07 | 1698.71 | stop | -10.4% |
| ADANIPORTS.NS | 2021-06-15 | 776.12 | 2021-06-16 | 698.51 | stop | -10.4% |
| BAJFINANCE.NS | 2018-09-24 | 234.86 | 2018-09-24 | 213.55 | stop | -9.5% |
| INFY.NS | 2012-04-11 | 232.65 | 2012-04-13 | 211.57 | stop | -9.5% |
| INFY.NS | 2022-04-13 | 1507.53 | 2022-04-18 | 1379.15 | stop | -8.9% |

## Spot check of 2 trades against the raw cached data
| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GOLDBEES.NS | 2018-11-09 | 28.01 | close 28.01 > SMA200 27.39, RSI(2) 8.8 < 10 | 2018-11-12 | 28.01 | 28.01 | 27.97 | 2018-11-12 | stop | 28.01 / 28.01 / 27.67 | 27.97 |
| HINDUNILVR.NS | 2019-01-02 | 1561.92 | close 1561.92 > SMA200 1404.99, RSI(2) 8.7 < 10 | 2019-01-03 | 1560.17 | 1560.17 | 1523.98 | 2019-01-10 | exit rule | 1562.27 / 1574.61 / 1557.02 | 1562.27 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
