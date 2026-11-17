# Trade plan: REGN (Regeneron Pharmaceuticals, Nasdaq, USD)

## Summary
- Not ready: 1 share (Rs 93,256 at the $991.73 trigger, USD/INR 94.03 on 2026-11-13) is above the 20% cap of Rs 40,000, and the Rs 2,000 risk buys 0.33 shares.
- No Donchian 50/20 buy signal today (close $955.47 on 2026-11-13); the trigger is a close above $991.73.
- What would change it: a user rule change allowing fractional shares (IBKR offers them; not verified for an Indian resident), or a bigger budget; otherwise REGN stays a long-term buy idea (research verdict WATCH).
- To do now: nothing; recheck only if both the trigger and a rule change happen.

**Status: Not ready: 1 share exceeds the 20% position cap.** Paper only (trading rules approved 2026-11-15 for paper trading; real money needs the paper check and a new approval). No orders.

Written 2026-11-15 by finance-trader. Prices: yfinance daily bars to the 2026-11-13 close (auto-adjusted), downloaded 2026-11-15, computed with `trading/backtests/engine.py` helpers (`load`, `ind`). USD/INR 94.03 = INR=X close 2026-11-13 (yfinance). Inputs: `research/stocks/REGN.md` (WATCH, long-term buying only), `news/REGN.md` (+2, 2026-11-15), `tax/new-investments.md`, [trading/backtests/trend-following/index.md](../backtests/trend-following/index.md).

## Setup (2026-11-13 close $955.47)

| Item | Value | Read |
|---|---|---|
| Trend | 50-day SMA $816.17, 200-day SMA $745.84; both rising (50-day +$25.45, 200-day +$11.78 over 20 days) | Uptrend: close > 50 > 200 |
| Momentum | RSI(14) 68.4 (Wilder) | Strong, just under overbought (70) |
| Relative strength vs SPY | 3 months (from 2026-08-17): REGN +18.7%, SPY -2.1% -> +20.8 points; 12 months (from 2025-11-12): REGN +40.9%, SPY +11.6% -> +29.3 points | Clearly stronger than the market |
| Volume | 1.17 m vs 50-day average 0.84 m (1.40x); 5-day average 1.19x | Above average since the 10-30 results gap |
| ATR(14) | $31.94 (3.3% of price) | |
| Swing low (10-day low) | $887.04 (2026-11-06) | Nearest support |
| Support | $887-902 (11-05/11-06 lows and closes); $816 (50-day SMA and pre-results close 10-29 $818.77); $780.83 (20-day low) | |
| Resistance | $973.36 (closing high 11-03); $991.73 (52-week high, 11-04) | |
| Donchian | Prior 50-day high $991.73; prior 20-day low $780.83 | |
| Donchian 50/20 signal | The last entry signal was on 2026-10-30 (close $927.89 > $859.34). The backtest would have bought 2026-11-02 at the open $927.22 with stop $873.02 (2 x ATR $27.10 of 10-30); not hit (lowest low since $887.04), no exit signal. That entry is past; this plan does not chase it. **No new signal today.** | Wait for the trigger |
| Next catalysts | Cemdisiran FDA decision "in November", day not disclosed; ex/record dividend 2026-11-20 ($0.94); Q4 results 2027-01-28 (Yahoo calendar estimate, not confirmed by the company) | Event risk, see rules |

## Strategy and evidence

US Donchian 50/20 with the AGENTS.md stop, the only strategy treated as fit ([trading/backtests/trend-following/index.md](../backtests/trend-following/index.md)): rules-sized 2010 to 2026-11-13, 467 trades, win rate 41.8%, profit factor 2.12, CAGR 13.1%, max drawdown -23.1%, average 56 calendar days held (SPY buy and hold 13.9%, -33.7%). REGN was not in that backtest's stock list.

## Entry, stop, target (planning values at today's ATR; recompute on the signal day)

| Item | Value |
|---|---|
| Entry trigger | A daily close above the prior 50-day high, now $991.73 |
| Order | Limit buy for the next open, limit = signal-day close x 1.01; no fill if it opens higher (skip, do not chase) |
| Planning entry | $991.73 |
| Stop (rule: tightest of 2 x ATR(14), swing low, 10%) | 2 x ATR: $991.73 - $63.89 = **$927.84**; swing low $887.04; 10%: $892.56 -> stop $927.84 (risk $63.89 = 6.4% per share = Rs 6,008) |
| Target | No fixed target in the tested strategy (it trails with the 20-day low). Review point at 2R = $1,119.51. Analyst mean target $984.96 (yfinance, 2026-11-15) is below the trigger; highest $1,175 = 2.9R |
| Reward/risk | 2.0 at the review point |

## Size (rules)

- Shares = Rs 2,000 / Rs 6,008 = 0.33 -> **0 whole shares** (first 3 months of real money: Rs 1,000 -> 0.17).
- 20% cap: Rs 40,000; 1 share at the trigger = $991.73 x 94.03 = **Rs 93,256** (at today's close Rs 89,846) -> 0.43 shares -> **0 whole shares**.
- Not tradable under the rules. IBKR offers fractional US shares, but whether an Indian resident can use them is not verified (research), and the rules count whole shares; using fractions needs a user rule change. Not assumed here. In local currency the cap is $425 (Rs 40,000 / 94.03).

## Holding period and exits

- Expected hold: weeks to a few months (backtest average 56 days). Short-term for tax (24 months or less).
- Exits, first hit wins: (1) stop $927.84 (GTT/stop order the same day, never moved down); (2) a close below the prior 20-day low -> sell next open; (3) news score -2 in `news/REGN.md` -> sell next open; (4) earnings: no entry from 2027-01-21 (5 trading days before 2027-01-28); an open position above half normal risk is reduced or closed before results; (5) cemdisiran FDA decision (date unknown): not covered by the rules; plan choice is no new entry until the decision is public (rejection or delay = likely gap through the stop); (6) review at 2R; no time stop in the tested strategy.

## Rules checked (AGENTS.md, approved for paper trading)

| Rule | Result |
|---|---|
| Position size: at most 20% of budget (Rs 40,000) | **FAIL**: 1 share Rs 93,256 |
| Risk per trade Rs 2,000 (1%) with whole shares | **FAIL**: 0 shares (0.33) |
| Stop set at entry, tightest of swing low / 2 x ATR, not wider than 10% | PASS: $927.84, 6.4% |
| Limit orders only | PASS: limit entry; stop order only as protection |
| Excluded (under $5, OTC, F&O, margin, leveraged ETFs) | PASS: $955, Nasdaq common stock |
| No averaging down | PASS: one entry only |
| Earnings: no entry within 5 trading days before results | PASS today; next results 2027-01-28 (estimate) -> no entry from 2027-01-21 |
| Max 5 open positions / 5% open risk | PASS: 0 open (`journal/trades.csv` empty, 2026-11-15) |
| Max 3 new entries per week | PASS: 0 this week |
| Loss limits (3 stops in a row, month -4%, budget -10%) | PASS: no trades yet |
| Journal before entry | Pending: send to finance-journal only if a paper entry is made |
| Entry signal present | FAIL today: close $955.47 below trigger $991.73 |

## Tax line

Tax: US stock via IBKR; ST <=24m 35.88%, LT 14.95% (no Rs 1.25 L exemption); div WHT 25% (DTAA 25%, W-8BEN) -> FTC in full via Form 44; no STT (small SEC fee on sells); LRS TCS 20% above Rs 10 L/FY (credited against tax); Schedule FA + FSI + TR; US estate situs YES. See tax/new-investments.md#us

- ask finance-tax: if the user later allows fractional shares at IBKR, does a fractional holding change anything for cost basis, Schedule FA reporting or TCS?
- ask finance-tax: a short trade held over the 2026-11-20 record date gets a $0.94 dividend with 25% WHT; is a dividend under Rs 100 worth claiming FTC via Form 44, or ignored in practice?

## Verdict

Trend and momentum are strong and a breakout trigger is close ($991.73, 3.8% above the close), but the trade cannot be sized under the rules: one share is more than twice the 20% cap and its risk is three times the Rs 2,000 limit. Keep at `researching` / watch; the research verdict (long-term buying only) is the better route for REGN.
