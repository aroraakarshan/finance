# Study: buy after a sharp drop vs wait for the trend

## Summary
- Buying a sharp drop is not a valid entry under the approved rules; on survivors it made money on average but with deep dips during the hold.
- Buying a 25%+ drop and holding 60 days: mean 11.5%, median 10.4%, 68% positive, worst 10% -16.8% (SPY same days mean 7.4%).
- Waiting for the trend (Donchian 50/20, rules stop): mean 2.3% a trade, 39% positive, losses capped by the stop (worst 10% -5.8%).
- These are today's surviving large caps; real dip-buying also hits stocks that never came back, so the drop numbers are too good.

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py drop-vs-trend`; every number on this page is printed by that script.

## Rules (fixed, not tuned)
- (a) Event: close at least 25% below the highest high of the last 63 trading days. Buy at the next open, sell at the open 20 or 60 trading days later. One event per stock at a time (no new event while a hold is open). Costs 0.05% a side (US).
- (b) Same, but only if the close is still above the 200-day SMA.
- (c) Wait for the trend: Donchian 50/20 with the AGENTS.md stop, every signal (from [trend-following](../trend-following/index.md); same run, original US stock list).
- (d) RSI(2) < 10 dip-buy above the 200-day SMA with the AGENTS.md stop (from [swing-pullback](../swing-pullback/index.md); US ETFs and stocks).
- Universe for (a) and (b): the US stock list plus semis TSM MU ARM SMH SOXX; daily Yahoo data 2010-01-01 to 2026-11-13. Worst dip in hold = lowest low from the entry day to the day before the exit, vs the entry price (the drawdown you sit through; a stop-day gap shows in the return, not here); a dip of 10% or more would have hit any stop allowed by the rules (max 10%), so (a) and (b) as tested, with no stop, are not rule-compliant. SPY same days = SPY open-to-open over the same dates. (c) and (d) count closed trades only.

## Results (full period, every event, net of costs)
| Variant | Universe | Events | Mean | Median | % positive | Worst 10% (10th pct) | SPY same days mean | SPY % positive | Mean worst dip in hold | Worst dip in hold | % that fell 10%+ below entry |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) Drop 25%+ from 63-day high, hold 20 days | US list + semis (37 names) | 424 | 3.7% | 3.1% | 62% | -11.6% | 2.5% | 69% | -9.6% | -44.9% | 38% |
| (a) Drop 25%+ from 63-day high, hold 20 days, without NVDA | US list + semis (37 names) | 396 | 3.7% | 3.0% | 62% | -11.3% | 2.6% | 69% | -9.4% | -44.9% | 37% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 20 days | US list + semis (37 names) | 66 | 3.6% | 1.8% | 61% | -12.1% | 1.7% | 71% | -10.5% | -44.9% | 41% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 20 days, without NVDA | US list + semis (37 names) | 57 | 2.8% | 1.4% | 58% | -12.7% | 1.6% | 70% | -10.3% | -44.9% | 37% |
| (a) Drop 25%+ from 63-day high, hold 60 days | US list + semis (37 names) | 242 | 11.5% | 10.4% | 68% | -16.8% | 7.4% | 79% | -13.4% | -52.3% | 52% |
| (a) Drop 25%+ from 63-day high, hold 60 days, without NVDA | US list + semis (37 names) | 228 | 11.7% | 10.4% | 69% | -16.1% | 7.7% | 80% | -13.1% | -52.3% | 50% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 60 days | US list + semis (37 names) | 36 | 20.3% | 7.7% | 61% | -15.0% | 5.5% | 83% | -13.4% | -35.2% | 53% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 60 days, without NVDA | US list + semis (37 names) | 31 | 20.3% | 4.6% | 61% | -15.6% | 5.2% | 87% | -13.1% | -35.2% | 48% |
| (c) Donchian 50/20, rules stop (reused, original US universe) | 35 names | 1470 | 2.3% | -2.4% | 39% | -5.8% | 1.6% | 58% | -2.4% | -9.9% | 0% |
| (d) RSI(2) dip-buy, rules stop (reused, original US universe) | 35 names | 7189 | 0.1% | -0.3% | 44% | -2.1% | 0.3% | 45% | -0.7% | -9.8% | 0% |

Holds differ: (a)/(b) are fixed 20 or 60 days; (c) averages about 54 days; (d) about 2 days. Compare (c) and (d) mainly on the shape (median, % positive, worst 10%), not the mean.

## By period (2010-2019 vs 2020-2026)
| Variant | Universe | Period | Events | Mean | Median | % positive | Worst 10% | SPY same days mean |
|---|---|---|---|---|---|---|---|---|
| (a) Drop 25%+ from 63-day high, hold 20 days | US list + semis (37 names) | 2010-2019 | 154 | 2.4% | 2.7% | 60% | -14.2% | 2.0% |
| (a) Drop 25%+ from 63-day high, hold 20 days | US list + semis (37 names) | 2020-2026 | 270 | 4.5% | 3.6% | 64% | -10.5% | 2.8% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 20 days | US list + semis (37 names) | 2010-2019 | 19 | 6.1% | 8.7% | 58% | -13.0% | 0.9% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 20 days | US list + semis (37 names) | 2020-2026 | 47 | 2.5% | 1.4% | 62% | -12.0% | 2.0% |
| (a) Drop 25%+ from 63-day high, hold 60 days | US list + semis (37 names) | 2010-2019 | 87 | 8.3% | 9.4% | 71% | -22.0% | 5.6% |
| (a) Drop 25%+ from 63-day high, hold 60 days | US list + semis (37 names) | 2020-2026 | 155 | 13.3% | 10.9% | 66% | -14.2% | 8.5% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 60 days | US list + semis (37 names) | 2010-2019 | 12 | 16.6% | 16.1% | 75% | -9.7% | 4.7% |
| (b) Drop 25%+ from 63-day high, above SMA200, hold 60 days | US list + semis (37 names) | 2020-2026 | 24 | 22.2% | 2.4% | 54% | -18.4% | 5.9% |
| (c) Donchian 50/20, rules stop (reused, original US universe) | 35 names | 2010-2019 | 890 | 1.9% | -2.2% | 40% | -5.1% | 1.3% |
| (c) Donchian 50/20, rules stop (reused, original US universe) | 35 names | 2020-2026 | 580 | 3.0% | -3.1% | 37% | -6.4% | 1.9% |
| (d) RSI(2) dip-buy, rules stop (reused, original US universe) | 35 names | 2010-2019 | 4190 | 0.1% | -0.2% | 43% | -1.9% | 0.2% |
| (d) RSI(2) dip-buy, rules stop (reused, original US universe) | 35 names | 2020-2026 | 2999 | 0.1% | -0.3% | 44% | -2.3% | 0.3% |

## Biases
| Bias | Effect |
|---|---|
| Survivorship: today's large caps only | Stocks that fell 25% and kept falling (delisted, merged, shrunk out of the list) are missing: drop-buying looks better than it was |
| NVDA 2010-2026 is an outlier | Shown with and without NVDA |
| Overlapping events across stocks | Drops cluster in crashes (2020, 2022): events are not independent, so the % positive is less certain than the count suggests |
| No earnings rule, no news filter | Many 25% drops follow results or news; the AGENTS.md earnings and news -2 rules would block some entries |

## Data
Dropped for short history (< 1000 bars): ARM (796). Data problems in the added tickers: none. Other data checks: see [trend-following/data.md](../trend-following/data.md).

## Verdict
On today's surviving large caps and semis, buying a 25% drop made money on average and beat SPY over the same days, but it is not a trade the approved rules allow: the rules need a stop of at most 10% at entry, and a large share of drop-buys fell 10% or more below the entry before recovering, so they would have been stopped out (this stop version was not simulated). The trend filter (b) leaves too few events to trust. Waiting for the trend (Donchian 50/20 with the rules stop) wins less often but keeps each loss small, which is what the rules are built for. For the trading budget: wait for a Donchian 50-day-high close. Buying after a drop is a long-term investing decision (research view, finance-research), not a paper trade under these rules.
