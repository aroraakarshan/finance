# Backtest trades: trend following (Faber SMA200 timing and Donchian 50/20 breakout)

## Summary
- Trade-level detail for trend-following: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py trend-following`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | Donchian 50/20, stocks, no stop | every-signal trades by exit: exit rule 1236, open at end 17 |
| US | Donchian 50/20, stocks, with rules stop | every-signal trades by exit: exit rule 759, stop 711, open at end 12 |
| US | Donchian rules-sized | budget 2,128 USD, final equity 17,025 USD; trades by exit: exit rule 256, stop 206, open at end 5; signals skipped: max_pos 6019, week_limit 25, price_above_cap 0, cash 0 |
| India | Donchian 50/20, stocks, no stop | every-signal trades by exit: exit rule 1013, open at end 19 |
| India | Donchian 50/20, stocks, with rules stop | every-signal trades by exit: stop 658, exit rule 570, open at end 19 |
| India | Donchian rules-sized | budget 200,000 INR, final equity 463,365 INR; trades by exit: stop 246, exit rule 216, open at end 5; signals skipped: max_pos 3596, week_limit 10, price_above_cap 0, cash 0 |

### Worst 5 trades: US, Donchian 50/20, stocks, no stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| INTC | 2025-02-19 | 25.98 | 2025-04-09 | 18.07 | exit rule | -30.5% |
| NVDA | 2022-03-30 | 28.19 | 2022-04-18 | 21.11 | exit rule | -25.2% |
| ADBE | 2026-06-02 | 267.98 | 2026-06-12 | 202.40 | exit rule | -24.5% |
| CRM | 2026-06-02 | 200.15 | 2026-06-18 | 152.46 | exit rule | -23.9% |
| GE | 2018-10-09 | 63.29 | 2018-10-30 | 48.75 | exit rule | -23.1% |

### Worst 5 trades: US, Donchian 50/20, stocks, with rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ADBE | 2010-09-10 | 32.56 | 2010-09-22 | 25.89 | stop | -20.6% |
| AMD | 2014-07-15 | 4.63 | 2014-07-18 | 3.73 | stop | -19.5% |
| UNH | 2026-01-23 | 347.41 | 2026-01-27 | 288.27 | stop | -17.1% |
| ORCL | 2026-05-29 | 207.51 | 2026-06-11 | 178.39 | stop | -14.1% |
| UNH | 2025-04-09 | 538.37 | 2025-04-17 | 463.22 | stop | -14.0% |

### Worst 5 trades: US, Donchian rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| UNH | 2025-04-09 | 538.37 | 2025-04-17 | 463.22 | stop | -14.0% |
| ORCL | 2026-09-09 | 162.94 | 2026-09-14 | 140.90 | stop | -13.6% |
| AAPL | 2026-07-28 | 339.48 | 2026-07-31 | 304.32 | stop | -10.4% |
| INTC | 2026-09-22 | 120.15 | 2026-10-08 | 108.14 | stop | -10.1% |
| AMD | 2017-06-22 | 14.10 | 2017-06-29 | 12.69 | stop | -10.1% |

### Worst 5 trades: India, Donchian 50/20, stocks, no stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| TITAN.NS | 2013-05-13 | 271.74 | 2013-06-12 | 209.98 | exit rule | -23.1% |
| INFY.NS | 2012-02-17 | 245.03 | 2012-04-16 | 201.65 | exit rule | -18.1% |
| HDFCBANK.NS | 2022-04-05 | 779.85 | 2022-04-19 | 646.12 | exit rule | -17.5% |
| INFY.NS | 2011-07-08 | 250.68 | 2011-08-08 | 208.90 | exit rule | -17.0% |
| ICICIBANK.NS | 2016-04-22 | 215.72 | 2016-05-05 | 180.41 | exit rule | -16.7% |

### Worst 5 trades: India, Donchian 50/20, stocks, with rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| TATASTEEL.NS | 2025-03-06 | 140.55 | 2025-04-07 | 122.56 | stop | -13.2% |
| HDFCBANK.NS | 2010-03-23 | 79.31 | 2010-03-29 | 70.40 | stop | -11.6% |
| JSWSTEEL.NS | 2025-03-06 | 1004.51 | 2025-04-07 | 898.41 | stop | -11.0% |
| HINDUNILVR.NS | 2020-04-08 | 2155.07 | 2020-04-30 | 1939.56 | stop | -10.4% |
| HDFCBANK.NS | 2020-06-04 | 478.95 | 2020-06-12 | 432.34 | stop | -10.1% |

### Worst 5 trades: India, Donchian rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| TATASTEEL.NS | 2025-03-06 | 140.55 | 2025-04-07 | 122.56 | stop | -13.2% |
| HDFCBANK.NS | 2010-03-23 | 79.31 | 2010-03-29 | 70.40 | stop | -11.6% |
| JSWSTEEL.NS | 2025-03-06 | 1004.51 | 2025-04-07 | 898.41 | stop | -11.0% |
| HINDUNILVR.NS | 2020-04-08 | 2155.07 | 2020-04-30 | 1939.56 | stop | -10.4% |
| NESTLEIND.NS | 2020-04-17 | 854.27 | 2020-05-13 | 768.84 | stop | -10.4% |

## Spot check of 2 trades against the raw cached data
| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ORCL | 2018-07-17 | 43.31 | close 43.31 > prior 50-day high 43.07 | 2018-07-18 | 43.22 | 43.22 | 41.64 | 2018-08-02 | stop | 41.67 / 42.58 / 41.30 | 41.64 |
| MSFT | 2017-12-15 | 79.37 | close 79.37 > prior 50-day high 78.64 | 2017-12-18 | 79.62 | 79.62 | 77.13 | 2018-02-09 | exit rule | 78.87 / 81.28 / 76.61 | 78.87 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
