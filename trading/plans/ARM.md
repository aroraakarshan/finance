# Trade plan: ARM (Arm Holdings, Nasdaq ADS, USD)

## Summary
- Status: no valid setup today (2026-11-13 close $190.53). Paper only; no orders.
- ARM is in a downtrend: below its 50-day and 200-day averages, -43.5% from its 63-day high, and weaker than SPY and SMH over 3 months.
- Trigger that would make a valid setup: a daily close above the prior 50-day high, now $336.98 (+76.9%). A close back above the 50-day SMA ($248.14) is only a watch sign; it is not a tested entry.
- Buying the drop is not a trade the rules allow: see [drop-vs-trend](../backtests/drop-vs-trend/index.md). The long-term view belongs to finance-research: [research/events/2026-11-15/semis-selloff-nvda-arm.md](../../research/events/2026-11-15/semis-selloff-nvda-arm.md).
- Missing before any plan can reach the user: `news/ARM.md` and `research/stocks/ARM.md` do not exist (checked 2026-11-15).

Written 2026-11-15 by finance-trader. Prices: yfinance daily bars to the 2026-11-13 close, computed with `trading/backtests/engine.py` (`setup`, `plan_stop`; same code as `engine.py setup ARM`). USD/INR 94.03 = INR=X close 2026-11-13. ARM is not on `trading/watchlist.md`.

## Setup (2026-11-13)

| Item | Value |
|---|---|
| Trend | Close $190.53; 50-day SMA $248.14 (falling, -$19.73 in 20 days); 200-day SMA $232.82 |
| Momentum | RSI(14) 40.6 |
| Relative strength, 3 months / 12 months | vs SPY -27.7 / +16.5 points; vs SMH -11.7 / -9.2 points |
| Volume | 5.49 m vs 50-day average 5.67 m (0.97x) |
| ATR(14) | $16.22 (8.5% of price) |
| Swing low (10-day) | $163.13 (2026-11-05) |
| Support / resistance | Support $163.13 (20-day low), $100.02 (52-week low, 2026-02-05). Resistance $232.82 (200-day), $248.14 (50-day), $336.98 (50-day high, 2026-09-23); 52-week high $452.70 (2026-06-18) |
| Donchian 50/20 | Last buy signal 2026-09-22; exit signal 2026-11-05 (close below the 20-day low); no signal now |
| Next results | 2027-02-03 after the US close (yfinance earnings dates; earlier reports 2026-02-04 and 2025-02-05, so early February fits) |

## If bought at the 11-13 close (for scale only, not a valid entry)

| Item | Value |
|---|---|
| Stop (tightest of 2 x ATR $158.08, swing low $163.13, 10% $171.48) | $171.48 (10% cap), risk $19.05 = Rs 1,792 a share |
| Shares at Rs 2,000 risk | 1 (Rs 2,000 / Rs 1,792) |
| 20% cap Rs 40,000 | 1 share = Rs 17,916, so the cap allows 2; size = 1 share |
| Fractional shares | Need a user rule change; not assumed |

## Rules today (AGENTS.md, approved for paper trading)

| Rule | Result |
|---|---|
| Entry signal (Donchian 50/20, the only strategy fit for paper trading) | FAIL: no 50-day-high close |
| Stop at entry, max 10% | PASS: $171.48 (exactly 10%) |
| Size and 20% cap | PASS: 1 share |
| Excluded list | PASS: $190, Nasdaq ADS, no derivatives |
| Earnings: no entry within 5 trading days before results | PASS: next results 2027-02-03 |
| News file and score | FAIL: no `news/ARM.md` (not scored) |
| Max 5 open / 3 a week / loss limits | PASS: no paper trades open (`journal/trades.csv` empty) |

## Exits (if a signal comes)
The stop above, recomputed on the signal day; a close below the prior 20-day low -> sell next open; news score -2 -> sell; reduce or exit before the results if the position is above half the normal risk.

## Tax line
Tax: US stock via IBKR; ST <=24m 35.88%, LT 14.95% (no Rs 1.25 L exemption); div WHT 25% (DTAA 25%, W-8BEN) -> FTC in full via Form 44; no STT (small SEC fee on sells); LRS TCS 20% above Rs 10 L/FY (credited against tax); Schedule FA + FSI + TR; US estate situs unsettled (UK company ADS, see below). See tax/new-investments.md#us

- Answer (finance-tax, [tax/global-actions-2026-11.md](../../tax/global-actions-2026-11.md) row 14): an ADS of a UK company is commonly treated as not US-situs for US estate tax, but there is no IRS ruling, so it is unsettled (ask a CA or US estate adviser).
