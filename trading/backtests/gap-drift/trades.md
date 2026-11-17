# Backtest trades: gap-up drift (post-earnings-announcement drift proxy)

## Summary
- Trade-level detail for gap-drift: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py gap-drift`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop | every-signal trades by exit: stop 48, target 46, time stop 16 |
| US | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | budget 2,128 USD, final equity 2,574 USD; trades by exit: stop 47, target 45, time stop 16; signals skipped: max_pos 0, week_limit 0, price_above_cap 2, cash 0 |
| US | earnings check | 1 recent gap days with cached earnings dates (others would need downloads): CVX 2026-01-05 no earnings within 1 day |
| India | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop | every-signal trades by exit: stop 24, time stop 15, target 15 |
| India | Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized | budget 200,000 INR, final equity 205,588 INR; trades by exit: stop 24, time stop 15, target 15; signals skipped: max_pos 0, week_limit 0, price_above_cap 0, cash 0 |
| India | earnings check | 1 recent gap days with cached earnings dates (others would need downloads): KOTAKBANK.NS 2025-01-20 earnings 2025-01-18 |

### Worst 5 trades: US, Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| AMD | 2013-07-12 | 4.48 | 2013-07-19 | 3.99 | stop | -11.0% |
| CRM | 2026-08-28 | 250.03 | 2026-09-28 | 224.97 | time stop | -10.1% |
| AMD | 2016-04-25 | 3.81 | 2016-04-25 | 3.43 | stop | -10.1% |
| COST | 2020-03-03 | 281.57 | 2020-03-12 | 255.43 | stop | -9.4% |
| UNH | 2020-03-05 | 250.41 | 2020-03-12 | 227.95 | stop | -9.1% |

### Worst 5 trades: US, Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| AMD | 2013-07-12 | 4.48 | 2013-07-19 | 3.99 | stop | -11.0% |
| CRM | 2026-08-28 | 250.03 | 2026-09-28 | 224.97 | time stop | -10.1% |
| AMD | 2016-04-25 | 3.81 | 2016-04-25 | 3.43 | stop | -10.1% |
| COST | 2020-03-03 | 281.57 | 2020-03-12 | 255.43 | stop | -9.4% |
| UNH | 2020-03-05 | 250.41 | 2020-03-12 | 227.95 | stop | -9.1% |

### Worst 5 trades: India, Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, every signal
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BHARTIARTL.NS | 2017-11-02 | 462.40 | 2017-11-08 | 420.87 | stop | -9.4% |
| TITAN.NS | 2017-06-06 | 527.53 | 2017-06-27 | 489.34 | stop | -7.6% |
| SBIN.NS | 2017-10-26 | 299.11 | 2017-10-31 | 280.41 | stop | -6.7% |
| CIPLA.NS | 2020-08-11 | 764.45 | 2020-08-24 | 716.97 | stop | -6.6% |
| ADANIPORTS.NS | 2019-05-21 | 390.83 | 2019-05-22 | 366.69 | stop | -6.6% |

### Worst 5 trades: India, Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop, rules-sized
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BHARTIARTL.NS | 2017-11-02 | 462.40 | 2017-11-08 | 420.87 | stop | -9.4% |
| TITAN.NS | 2017-06-06 | 527.53 | 2017-06-27 | 489.34 | stop | -7.6% |
| SBIN.NS | 2017-10-26 | 299.11 | 2017-10-31 | 280.41 | stop | -6.7% |
| CIPLA.NS | 2020-08-11 | 764.45 | 2020-08-24 | 716.97 | stop | -6.6% |
| ADANIPORTS.NS | 2019-05-21 | 390.83 | 2019-05-22 | 366.69 | stop | -6.6% |

## Spot check of 2 trades against the raw cached data
| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CAT | 2017-04-25 | 85.80 | open gap +6.3%, volume 3.4x, close 85.80 in top half of 83.81-86.18, > SMA200 72.59 | 2017-04-26 | 85.29 | 85.29 | 83.81 | 2017-05-01 | stop | 84.34 / 84.62 / 83.32 | 83.81 |
| AMD | 2016-07-22 | 5.84 | open gap +9.8%, volume 4.1x, close 5.84 in top half of 5.45-5.97, > SMA200 3.01 | 2016-07-25 | 5.93 | 5.93 | 5.45 | 2016-07-25 | target | 5.93 / 6.95 / 5.92 | 6.89 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
