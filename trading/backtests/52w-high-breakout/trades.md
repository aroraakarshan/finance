# Backtest trades: 52-week-high breakout on volume (George and Hwang 2004)

## Summary
- Trade-level detail for 52w-high-breakout: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py 52w-high-breakout`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop | every-signal trades by exit: stop 390, time stop 288, target 199 |
| US | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | budget 2,128 USD, final equity 5,776 USD; trades by exit: stop 316, time stop 237, target 158; signals skipped: max_pos 171, week_limit 46, price_above_cap 8, cash 0 |
| India | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop | every-signal trades by exit: stop 395, time stop 292, target 144, open at end 4 |
| India | 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized | budget 200,000 INR, final equity 113,994 INR; trades by exit: stop 304, time stop 236, target 111, open at end 4; signals skipped: max_pos 228, week_limit 52, price_above_cap 0, cash 0 |

### Worst 5 trades: US, 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| META | 2018-07-25 | 213.67 | 2018-07-26 | 173.23 | stop | -19.0% |
| INTC | 2026-01-22 | 54.21 | 2026-01-23 | 46.86 | stop | -13.6% |
| AMD | 2026-09-22 | 606.57 | 2026-10-15 | 540.00 | stop | -11.1% |
| AMD | 2016-06-20 | 5.39 | 2016-06-24 | 4.82 | stop | -10.7% |
| QCOM | 2026-05-12 | 227.75 | 2026-05-12 | 204.98 | stop | -10.1% |

### Worst 5 trades: US, 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| META | 2018-07-25 | 213.67 | 2018-07-26 | 173.23 | stop | -19.0% |
| INTC | 2026-01-22 | 54.21 | 2026-01-23 | 46.86 | stop | -13.6% |
| AMD | 2026-09-22 | 606.57 | 2026-10-15 | 540.00 | stop | -11.1% |
| AMD | 2016-06-20 | 5.39 | 2016-06-24 | 4.82 | stop | -10.7% |
| QCOM | 2026-05-27 | 243.20 | 2026-06-05 | 218.88 | stop | -10.1% |

### Worst 5 trades: India, 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ULTRACEMCO.NS | 2012-02-07 | 1265.08 | 2012-02-14 | 1127.56 | stop | -11.3% |
| HINDUNILVR.NS | 2020-04-08 | 2155.07 | 2020-04-30 | 1939.56 | stop | -10.4% |
| BHARTIARTL.NS | 2020-05-20 | 571.14 | 2020-05-29 | 519.29 | stop | -9.5% |
| ADANIPORTS.NS | 2014-07-03 | 254.73 | 2014-07-11 | 232.26 | stop | -9.2% |
| TCS.NS | 2014-09-22 | 1026.99 | 2014-10-17 | 936.56 | stop | -9.2% |

### Worst 5 trades: India, 52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| ULTRACEMCO.NS | 2012-02-07 | 1265.08 | 2012-02-14 | 1127.56 | stop | -11.3% |
| HINDUNILVR.NS | 2020-04-08 | 2155.07 | 2020-04-30 | 1939.56 | stop | -10.4% |
| BHARTIARTL.NS | 2020-05-20 | 571.14 | 2020-05-29 | 519.29 | stop | -9.5% |
| BHARTIARTL.NS | 2017-11-02 | 462.40 | 2017-11-08 | 420.87 | stop | -9.4% |
| ADANIPORTS.NS | 2014-07-03 | 254.73 | 2014-07-11 | 232.26 | stop | -9.2% |

## Spot check of 2 trades against the raw cached data
| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPL | 2018-08-30 | 53.12 | close 53.12 > prior 52-week high 52.76, volume 2.0x 50-day average | 2018-08-31 | 53.47 | 53.47 | 51.89 | 2018-09-10 | stop | 52.16 / 52.37 / 51.10 | 51.89 |
| V | 2020-01-13 | 185.76 | close 185.76 > prior 52-week high 185.04, volume 1.6x 50-day average | 2020-01-14 | 187.10 | 187.10 | 182.95 | 2020-01-21 | target | 194.13 / 198.18 / 193.82 | 195.40 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
