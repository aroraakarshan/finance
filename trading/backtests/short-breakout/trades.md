# Backtest trades: short breakout (Turtle System 1 style, 20-day high / 10-day low)

## Summary
- Trade-level detail for short-breakout: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py short-breakout`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop | every-signal trades by exit: time stop 2103, stop 1398, exit rule 498, open at end 10 |
| US | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | budget 2,128 USD, final equity 10,029 USD; trades by exit: time stop 792, stop 555, exit rule 166, open at end 5; signals skipped: max_pos 7516, week_limit 460, price_above_cap 0, cash 0 |
| US | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop | every-signal trades by exit: time stop 1670, stop 1523, target 709, exit rule 514, open at end 10 |
| US | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | budget 2,128 USD, final equity 7,976 USD; trades by exit: time stop 606, stop 590, target 273, exit rule 169, open at end 4; signals skipped: max_pos 7386, week_limit 665, price_above_cap 6, cash 0 |
| India | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop | every-signal trades by exit: time stop 1609, stop 1129, exit rule 435, open at end 25 |
| India | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | budget 200,000 INR, final equity 151,173 INR; trades by exit: time stop 727, stop 510, exit rule 191, open at end 5; signals skipped: max_pos 4560, week_limit 335, price_above_cap 0, cash 0 |
| India | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop | every-signal trades by exit: time stop 1283, stop 1238, target 518, exit rule 435, open at end 26 |
| India | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | budget 200,000 INR, final equity 164,524 INR; trades by exit: time stop 600, stop 537, target 211, exit rule 186, open at end 4; signals skipped: max_pos 4531, week_limit 433, price_above_cap 0, cash 0 |

### Worst 5 trades: US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ADBE | 2010-09-10 | 32.56 | 2010-09-22 | 25.89 | stop | -20.6% |
| AMD | 2014-07-15 | 4.63 | 2014-07-18 | 3.73 | stop | -19.5% |
| UNH | 2026-01-23 | 347.41 | 2026-01-27 | 288.27 | stop | -17.1% |
| CSCO | 2010-11-05 | 15.49 | 2010-11-11 | 13.07 | stop | -15.7% |
| INTC | 2020-07-21 | 54.84 | 2020-07-24 | 46.49 | stop | -15.3% |

### Worst 5 trades: US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| CSCO | 2010-11-09 | 15.64 | 2010-11-11 | 13.07 | stop | -16.5% |
| AMD | 2026-01-22 | 251.75 | 2026-02-04 | 215.00 | stop | -14.7% |
| META | 2018-07-10 | 202.56 | 2018-07-26 | 173.23 | stop | -14.6% |
| ORCL | 2026-09-09 | 162.94 | 2026-09-14 | 140.90 | stop | -13.6% |
| CRM | 2011-10-31 | 33.10 | 2011-11-18 | 29.30 | stop | -11.6% |

### Worst 5 trades: US, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ADBE | 2010-09-10 | 32.56 | 2010-09-22 | 25.89 | stop | -20.6% |
| AMD | 2014-07-15 | 4.63 | 2014-07-18 | 3.73 | stop | -19.5% |
| UNH | 2026-01-23 | 347.41 | 2026-01-27 | 288.27 | stop | -17.1% |
| CSCO | 2010-11-05 | 15.49 | 2010-11-11 | 13.07 | stop | -15.7% |
| INTC | 2020-07-21 | 54.84 | 2020-07-24 | 46.49 | stop | -15.3% |

### Worst 5 trades: US, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| AMD | 2014-07-15 | 4.63 | 2014-07-18 | 3.73 | stop | -19.5% |
| CSCO | 2010-11-09 | 15.64 | 2010-11-11 | 13.07 | stop | -16.5% |
| META | 2018-07-10 | 202.56 | 2018-07-26 | 173.23 | stop | -14.6% |
| UNH | 2025-04-09 | 538.37 | 2025-04-17 | 463.22 | stop | -14.0% |
| INTC | 2026-01-22 | 54.21 | 2026-01-23 | 46.86 | stop | -13.6% |

### Worst 5 trades: India, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| HDFCBANK.NS | 2010-03-26 | 83.46 | 2010-03-29 | 70.40 | stop | -16.0% |
| TATASTEEL.NS | 2010-03-03 | 38.02 | 2010-03-17 | 33.41 | stop | -12.5% |
| ADANIPORTS.NS | 2025-03-20 | 1174.31 | 2025-04-07 | 1040.48 | exit rule | -11.8% |
| ULTRACEMCO.NS | 2012-02-07 | 1265.08 | 2012-02-14 | 1127.56 | stop | -11.3% |
| AXISBANK.NS | 2010-03-03 | 211.76 | 2010-03-09 | 190.11 | stop | -10.6% |

### Worst 5 trades: India, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ULTRACEMCO.NS | 2012-02-07 | 1265.08 | 2012-02-14 | 1127.56 | stop | -11.3% |
| HDFCBANK.NS | 2010-03-12 | 78.97 | 2010-03-29 | 70.40 | stop | -11.2% |
| KOTAKBANK.NS | 2020-06-04 | 274.39 | 2020-06-12 | 246.54 | stop | -10.5% |
| BAJFINANCE.NS | 2010-05-17 | 4.23 | 2010-05-25 | 3.81 | stop | -10.4% |
| JSWSTEEL.NS | 2011-11-08 | 60.65 | 2011-11-15 | 54.62 | stop | -10.3% |

### Worst 5 trades: India, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| HDFCBANK.NS | 2010-03-26 | 83.46 | 2010-03-29 | 70.40 | stop | -16.0% |
| TATASTEEL.NS | 2010-03-03 | 38.02 | 2010-03-17 | 33.41 | stop | -12.5% |
| ADANIPORTS.NS | 2025-03-20 | 1174.31 | 2025-04-07 | 1040.48 | exit rule | -11.8% |
| ULTRACEMCO.NS | 2012-02-07 | 1265.08 | 2012-02-14 | 1127.56 | stop | -11.3% |
| AXISBANK.NS | 2010-03-03 | 211.76 | 2010-03-09 | 190.11 | stop | -10.6% |

### Worst 5 trades: India, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| KOTAKBANK.NS | 2020-06-04 | 274.39 | 2020-06-12 | 246.54 | stop | -10.5% |
| BAJFINANCE.NS | 2010-05-17 | 4.23 | 2010-05-25 | 3.81 | stop | -10.4% |
| JSWSTEEL.NS | 2011-11-08 | 60.65 | 2011-11-15 | 54.62 | stop | -10.3% |
| ADANIPORTS.NS | 2014-06-09 | 242.64 | 2014-06-12 | 219.80 | stop | -9.8% |
| ADANIPORTS.NS | 2014-07-08 | 263.72 | 2014-07-08 | 239.11 | stop | -9.7% |

## Spot check of 2 trades against the raw cached data
| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2019-04-18 | 48.50 | close 48.50 > prior 20-day high 48.38 | 2019-04-22 | 48.25 | 48.25 | 46.69 | 2019-05-10 | stop | 47.15 / 47.49 / 46.04 | 46.69 |
| CSCO | 2018-09-21 | 38.42 | close 38.42 > prior 20-day high 38.02 | 2018-09-24 | 38.14 | 38.14 | 37.06 | 2018-10-09 | exit rule | 37.86 / 38.26 / 37.66 | 37.86 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
