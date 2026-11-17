# Trade plan: NVDA (NVIDIA, Nasdaq, USD) - new entries only

## Summary
- Status: no valid setup today (2026-11-13 close $162.85). Paper only; no orders. Two approved rules block any new entry: results on 2026-11-17 (earnings rule) and news score -2.
- NVDA is in a sharp downtrend: below its 50-day and 200-day averages, at its 52-week low, RSI(14) 24.9, volume 2.5x normal.
- Trigger that would make a valid setup: after the results and with the news score above -2, a daily close above the prior 50-day high, now $243.37 (+49.4%). A close back above the 50-day SMA ($214.63) after the results is only a watch sign; it is not a tested entry.
- This plan covers new trading entries only. The existing 7.4949 shares in INDmoney (`news/NVDA.md`) are a holding decision for finance-main, not part of this plan.
- Evidence on buying the drop: [drop-vs-trend](../backtests/drop-vs-trend/index.md); fundamental view: [research/events/2026-11-15/semis-selloff-nvda-arm.md](../../research/events/2026-11-15/semis-selloff-nvda-arm.md).

Written 2026-11-15 by finance-trader. Prices: yfinance daily bars to the 2026-11-13 close, computed with `trading/backtests/engine.py` (`setup`, `plan_stop`; same code as `engine.py setup NVDA`). USD/INR 94.03 = INR=X close 2026-11-13. News: [news/NVDA.md](../../news/NVDA.md) (score -2, 2026-11-15).

## Setup (2026-11-13)

| Item | Value |
|---|---|
| Trend | Close $162.85; 50-day SMA $214.63 (falling, -$8.33 in 20 days); 200-day SMA $203.92 |
| Momentum | RSI(14) 24.9 (oversold) |
| Relative strength, 3 months / 12 months | vs SPY -25.4 / -27.3 points; vs SMH -9.5 / -53.1 points |
| Volume | 363.8 m vs 50-day average 148.2 m (2.45x) |
| ATR(14) | $9.98 (6.1% of price) |
| Swing low (10-day) | $148.80 (2026-11-12), also the 52-week low |
| Support / resistance | Support $148.80. Resistance $203.92 (200-day), $214.63 (50-day), $243.37 (50-day and 52-week high, 2026-10-06) |
| Donchian 50/20 | Last buy signal 2026-10-05; exit signal 2026-11-10; no signal now |
| Next results | 2026-11-17 after the US close (yfinance earnings dates, company release per `news/NVDA.md`); options imply about 8% |

## If bought at the 11-13 close (for scale only, not allowed)

| Item | Value |
|---|---|
| Stop (tightest of 2 x ATR $142.89, swing low $148.80, 10% $146.57) | $148.80 (swing low), risk $14.05 (8.6%) = Rs 1,321 a share |
| Shares at Rs 2,000 risk | 1 |
| 20% cap Rs 40,000 | 1 share = Rs 15,313, cap allows 2; size = 1 share |
| Fractional shares | Need a user rule change; not assumed |

## Rules today (AGENTS.md, approved for paper trading)

| Rule | Result |
|---|---|
| Entry signal (Donchian 50/20) | FAIL: no 50-day-high close |
| Earnings: no entry within 5 trading days before results | FAIL: results 2026-11-17; first allowed entry 2026-11-18 |
| News score -2 | FAIL: -2 (CEO resignation, 10 downgrades); no entry while -2 |
| Stop at entry, max 10% | PASS: $148.80, 8.6% |
| Size and 20% cap | PASS: 1 share |
| Excluded list | PASS |
| Max 5 open / 3 a week / loss limits | PASS: no paper trades open |

## Exits (if a signal comes later)
The stop recomputed on the signal day; a close below the prior 20-day low -> sell next open; news score -2 -> sell; reduce or exit before the next results if the position is above half the normal risk.

## Tax line
Tax: US stock via IBKR; ST <=24m 35.88%, LT 14.95% (no Rs 1.25 L exemption); div WHT 25% (DTAA 25%, W-8BEN) -> FTC in full via Form 44; no STT (small SEC fee on sells); LRS TCS 20% above Rs 10 L/FY (credited against tax); Schedule FA + FSI + TR; US estate situs YES. See tax/new-investments.md#us

- Answer (finance-tax, [tax/global-actions-2026-11.md](../../tax/global-actions-2026-11.md) row 15): the new lot is not pooled with the INDmoney lot. Each buy has its own INR cost and its own 24-month clock; pick the lot at sale at IBKR. A trading lot sold within weeks is short-term at 35.88%. CA to confirm.
