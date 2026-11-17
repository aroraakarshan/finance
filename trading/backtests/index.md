# Backtests

## Summary
- Pass the backtest bar on the 35-name lists: Donchian 50/20, rules stop, rules-sized in US (13.1% a year, worst drop -23.1%), 52-week high on 1.5x volume, 2R target, 20 days, rules-sized in US (6.1% a year, worst drop -10.7%).
- All other strategy x market pairs fail at least one test (14 of 16); the failing items are in [trading/playbook.md](../playbook.md#backtest-bar).
- Binding test, the FULL scan universe (about 680 US and 190 India names, [playbook](../playbook.md#backtest-bar)): no strategy passes, so no paper trades are opened yet.
- Momentum rotation and Faber timing have no stop, so they sit outside the trading rules (long-term ideas only).
- All numbers: daily Yahoo data 2010-01-01 to 2026-11-13, costs included, run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py all`.

## Versions that count vs benchmark (full period, costs included)
| Strategy | Version that counts | Market | Universe | CAGR | Max DD | Win rate | Trades | Benchmark | Bench CAGR | Bench max DD | Fit | Backtest bar | Tearsheet |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [trend-following](trend-following/index.md) | Faber SMA200 monthly, stocks | US | 35 names | 13.1% | -17.9% | 45.5% | 536 | SPY | 13.9% | -33.7% | Outside rules (30+ positions); filter idea | fail | [HTML](reports/trend-following-faber-US.html) |
| [trend-following](trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | US | 35 names | 13.1% | -23.1% | 41.8% | 467 | SPY | 13.9% | -33.7% | Fit for paper trading | PASS | [HTML](reports/trend-following-donchian-US.html) |
| [trend-following](trend-following/index.md) | Faber SMA200 monthly, stocks | India | 35 names | 8.6% | -15.3% | 37.0% | 513 | ^NSEI | 9.8% | -38.4% | Outside rules (30+ positions); filter idea | fail | [HTML](reports/trend-following-faber-India.html) |
| [trend-following](trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | India | 35 names | 5.1% | -33.0% | 31.3% | 467 | ^NSEI | 9.8% | -38.4% | Paper test only (weak) | fail | [HTML](reports/trend-following-donchian-India.html) |
| [momentum-rotation](momentum-rotation/index.md) | Top-5 12-1 momentum, index filter | US | 35 names | 17.1% | -38.5% | 55.0% | 231 | SPY | 13.9% | -33.7% | Long-term sleeve only (no stop) | fail | [HTML](reports/momentum-rotation-US.html) |
| [momentum-rotation](momentum-rotation/index.md) | Top-5 12-1 momentum, index filter | India | 35 names | 13.7% | -22.1% | 56.9% | 225 | ^NSEI | 9.8% | -38.4% | Long-term sleeve only (no stop) | fail | [HTML](reports/momentum-rotation-India.html) |
| [swing-pullback](swing-pullback/index.md) | RSI(2), rules stop, rules-sized | US | 35 names | 1.4% | -13.7% | 44.3% | 2100 | SPY | 13.9% | -33.7% | Not fit (rules stop) | fail | [HTML](reports/swing-pullback-US.html) |
| [swing-pullback](swing-pullback/index.md) | RSI(2), rules stop, rules-sized | India | 35 names | -8.8% | -79.3% | 36.4% | 2077 | ^NSEI | 9.8% | -38.4% | Not fit (costs and stop) | fail | [HTML](reports/swing-pullback-India.html) |
| [short-breakout](short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | US | 35 names | 9.6% | -23.6% | 47.3% | 1518 | SPY | 13.9% | -33.7% | see bar | fail | [HTML](reports/short-breakout-turtle-US.html) |
| [short-breakout](short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | US | 35 names | 8.2% | -23.6% | 48.2% | 1642 | SPY | 13.9% | -33.7% | see bar | fail | [HTML](reports/short-breakout-turtle2r-US.html) |
| [short-breakout](short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | India | 35 names | -1.6% | -42.3% | 42.6% | 1433 | ^NSEI | 9.8% | -38.4% | see bar | fail | [HTML](reports/short-breakout-turtle-India.html) |
| [short-breakout](short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | India | 35 names | -1.2% | -49.0% | 44.1% | 1538 | ^NSEI | 9.8% | -38.4% | see bar | fail | [HTML](reports/short-breakout-turtle2r-India.html) |
| [52w-high-breakout](52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | US | 35 names | 6.1% | -10.7% | 48.8% | 711 | SPY | 13.9% | -33.7% | see bar | PASS | [HTML](reports/52w-high-breakout-US.html) |
| [52w-high-breakout](52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | India | 35 names | -3.3% | -45.0% | 40.6% | 655 | ^NSEI | 9.8% | -38.4% | see bar | fail | [HTML](reports/52w-high-breakout-India.html) |
| [gap-drift](gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | US | 35 names | 1.1% | -5.0% | 52.8% | 108 | SPY | 13.9% | -33.7% | see bar | fail | [HTML](reports/gap-drift-US.html) |
| [gap-drift](gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | India | 35 names | 0.2% | -5.4% | 50.0% | 54 | ^NSEI | 9.8% | -38.4% | see bar | fail | [HTML](reports/gap-drift-India.html) |

Benchmarks are buy and hold (SPY with dividends; ^NSEI is a price index without dividends). Win rate and trades: rules-sized trades for the rules-sized strategies, holding spans for Faber and momentum. Each strategy page has all variants, periods, trades and data checks.

## Other studies
| Study | Question |
|---|---|
| [drop-vs-trend](drop-vs-trend/index.md) | Buy after a 25%+ drop, or wait for a trend signal? |

## Daily setup check
`.venv/bin/python trading/backtests/engine.py setup SYM1 SYM2 ... [--date YYYY-MM-DD]` prints one row per symbol: trend, RSI, relative strength vs the local index, Donchian trigger, rules stop, shares at Rs 2,000 risk and the Rs 40,000 cap, and whether the approved rules allow an entry today. Prices for it are kept in a separate live cache so these backtests stay reproducible.
