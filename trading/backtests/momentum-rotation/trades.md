# Backtest trades: momentum rotation (top-5 12-1 month momentum with index trend filter)

## Summary
- Trade-level detail for momentum-rotation: exits, skipped signals, worst trades, spot checks.
- Verdict and headline numbers: [index.md](index.md).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py momentum-rotation`; every number on this page is printed by that script.

## Trade counts, exits and skipped signals
| Market | Version | Detail |
|---|---|---|
| US | Top-5 12-1 momentum, index > SMA200 filter | months in cash 42 of 203; holding spans by exit: rebalance 226, open at end 5; average names changed per month 1.43 |
| US | Top-5 12-1 momentum, no filter | months in cash 13 of 203; holding spans by exit: rebalance 210, open at end 5; average names changed per month 1.13 |
| India | Top-5 12-1 momentum, index > SMA200 filter | months in cash 69 of 203; holding spans by exit: rebalance 225; average names changed per month 1.68 |
| India | Top-5 12-1 momentum, no filter | months in cash 13 of 203; holding spans by exit: rebalance 250, open at end 5; average names changed per month 1.34 |

### Worst 5 trades: US, Top-5 12-1 momentum, index > SMA200 filter
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| AMD | 2018-10-01 | 30.69 | 2018-11-01 | 18.41 | rebalance | -40.1% |
| INTC | 2026-05-01 | 93.20 | 2026-11-13 | 59.66 | open at end | -36.1% |
| NVDA | 2022-04-01 | 27.26 | 2022-05-02 | 18.47 | rebalance | -32.3% |
| CAT | 2026-05-01 | 893.06 | 2026-11-02 | 630.00 | rebalance | -29.5% |
| NVDA | 2021-12-01 | 33.08 | 2022-03-01 | 24.19 | rebalance | -26.9% |

### Worst 5 trades: US, Top-5 12-1 momentum, no filter
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| NVDA | 2021-12-01 | 33.08 | 2022-06-01 | 18.65 | rebalance | -43.7% |
| HD | 2022-01-03 | 368.51 | 2022-04-01 | 267.43 | rebalance | -27.5% |
| NVDA | 2011-07-01 | 0.36 | 2011-10-03 | 0.28 | rebalance | -22.6% |
| AMD | 2022-04-01 | 110.48 | 2022-05-02 | 85.66 | rebalance | -22.5% |
| AVGO | 2019-05-01 | 26.64 | 2019-06-03 | 21.00 | rebalance | -21.3% |

### Worst 5 trades: India, Top-5 12-1 momentum, index > SMA200 filter
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BHARTIARTL.NS | 2020-08-03 | 523.47 | 2020-11-02 | 412.13 | rebalance | -21.6% |
| TITAN.NS | 2019-07-01 | 1294.56 | 2019-08-01 | 1028.64 | rebalance | -20.9% |
| TITAN.NS | 2018-05-02 | 951.55 | 2018-10-01 | 778.63 | rebalance | -18.5% |
| ULTRACEMCO.NS | 2016-11-01 | 3757.86 | 2017-01-02 | 3112.68 | rebalance | -17.5% |
| ASIANPAINT.NS | 2016-10-03 | 1072.58 | 2016-12-01 | 888.69 | rebalance | -17.5% |

### Worst 5 trades: India, Top-5 12-1 momentum, no filter
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BAJFINANCE.NS | 2019-10-01 | 396.31 | 2020-05-04 | 214.19 | rebalance | -46.2% |
| ICICIBANK.NS | 2020-01-01 | 517.82 | 2020-05-04 | 344.32 | rebalance | -33.8% |
| DRREDDY.NS | 2015-09-01 | 799.97 | 2016-01-04 | 577.00 | rebalance | -28.2% |
| ULTRACEMCO.NS | 2020-03-02 | 4044.50 | 2020-04-01 | 3084.46 | rebalance | -24.1% |
| ONGC.NS | 2026-05-04 | 287.01 | 2026-07-01 | 226.70 | rebalance | -21.4% |

## Spot check of 2 trades against the raw cached data
| Market | Ticker | Entry fill date | Signal (month-end) date | 12-1 return on signal date (engine) | 12-1 return recomputed from raw cache | Fill (next open, raw cache) | Engine entry price |
|---|---|---|---|---|---|---|---|
| US | AVGO | 2019-05-01 | 2019-04-30 | 34.48% | 34.48% | 26.64 | 26.64 |
| India | HINDUNILVR.NS | 2019-01-02 | 2018-12-31 | 31.51% | 31.51% | 1568.75 | 1568.75 |

The rows above were also checked by hand on 2026-11-15 against the cache csv files (signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.
