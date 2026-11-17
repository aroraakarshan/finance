# QCOM sales: staged limit and stop sell plan

## Summary
- Options not allowed (legal): covered calls and protective puts on QCOM at IBKR look not allowed under FEMA; the bar is on the instrument, and there is no hedging exception ([legal/compliance/derivatives-abroad.md](../../legal/compliance/derivatives-abroad.md); finance-legal's reading, a CA or AD bank to confirm). The trading rules also exclude derivatives.
- Allowed route: sell the shares. For each part, a GTC limit sell at +3% for the part's window, then a plain limit near the close on its last day; a stop at -10% under the shares not yet sold.
- Sale 1: 432 shares in 4 weekly parts of 108 (23 Nov - 18 Dec 2026, two parts after the 9 Dec FOMC; parts 1-3 sold by 11 Dec, part 4 on 16-18 Dec). Sale 2: 195 shares, 1-16 Apr 2027. Keep 134.
- Paper plan only; no orders placed. You decide and trade.

Written 2026-11-15 by finance-trader. Prices: QCOM close 2026-11-13 $172.47, ATR(14) $9.23 (5.4%), 10-day swing low $148.25 (2026-11-05), all from `trading/backtests/engine.py` `setup("QCOM")` on the cached yfinance daily bars to 2026-11-13. USD/INR 94.03 = INR=X close 2026-11-13. Reset each part's prices to its own start-day price (same rules).

## Levels

| Part | Window | Shares | GTC limit sell (spot +3%) | Last day: plain limit near the close | Stop (sell stop, shares still unsold) | Proceeds at spot |
|---|---|---|---|---|---|---|
| Sale 1 p1 | Mon 23 - Wed 25 Nov 2026 (26 Nov closed, 27 Nov half day) | 108 | $177.64 (Rs 16,705) | 25 Nov, at about the last price (now $172.47, Rs 16,218) | $155.22 (Rs 14,596), -10% | $18,627 (Rs 17.52 L) |
| Sale 1 p2 | 30 Nov - Fri 4 Dec | 108 | +3% of 30 Nov price | 4 Dec | -10% of 30 Nov price | $18,627 (Rs 17.52 L) |
| Sale 1 p3 | 7 - Fri 11 Dec (FOMC decision Wed 9 Dec) | 108 | +3% of 7 Dec price | 11 Dec (after FOMC) | same rule | $18,627 (Rs 17.52 L) |
| Sale 1 p4 | Wed 16 - Fri 18 Dec (not 14-15 Dec: its tax then falls in the 15 Mar instalment) | 108 | +3% of 16 Dec price | 18 Dec (after FOMC) | same rule | $18,627 (Rs 17.52 L) |
| Sale 2 | Thu 1 - Fri 16 Apr 2027 | 195 | +3% of 1 Apr price (now $177.64) | 16 Apr | Now $155.22; re-set as below | $33,632 (Rs 31.63 L) |
| Kept | - | 134 | none | none | none | $23,111 (Rs 21.73 L) |

Stop rule: the trading-plan stop in `engine.py` (`plan_stop`): the tighter of 2 x ATR(14) below the price and the 10% cap, or a recent swing low if that is tighter. Here 2 x ATR = $154.00 (-10.7%) and the swing low $148.25 (-14.0%) are both wider, so the 10% cap binds: $155.22. Why not tighter: QCOM moves about 5.4% a day on average (ATR), so a -5% stop ($163.85) would often fire on normal noise; on 13 Nov alone the range was $167.20-177.53.

If the limit fills, cancel that part's stop (and the reverse). If QCOM falls under the stop for Sale 1, the rest of Sale 1 is sold early; that is the plan's aim (cut the concentration), not a loss to chase.

## Gap risk and Sale 2 stops

- A stop becomes a market order when hit; on a gap it fills below its level. The biggest one-day move in the cached QCOM history is 23.2% (engine data check); results are about 3 Feb 2027 (yfinance calendar says 4 Feb), when a gap is most likely. Ex-dividend 3 Dec 2026 (yfinance).
- Sale 2 stop timeline: keep $155.22 (or no stop) until results; re-set it the week after results (about 8 Feb 2027) to the same rule on the new price and ATR; re-set again on 1 Apr when the limit goes in, and raise it if QCOM has risen (never lower it).
- A Sale 2 stop that fires before 1 Apr 2027 moves that sale into tax year 2026-27 (see tax): about Rs 1.73 L more tax (sale 2 tax Rs 1,72,684, [qcom-lots.md](../../tax/employer-stock/qcom-lots.md) 3.4, at the 31 Mar rate) due by 15/31 Mar 2027.

## Tax line

From [tax/employer-stock/](../../tax/employer-stock/index.md) (finance-tax, 2026-11-15): lot choice is FIFO, oldest lots first, IBKR's default, "so no lot selection is needed" ([qcom-lots.md](../../tax/employer-stock/qcom-lots.md) 3.3-3.5). All lots sold are long term, 14.95%. Sale 1 (432 sh): gain Rs 23,66,837, tax **Rs 3,53,842**; Sale 2 (195 sh, tax year 2027-28): gain Rs 11,55,076, tax **Rs 1,72,684** (qcom-lots.md 3.4). Advance tax ([staged-sale.md](../../tax/employer-stock/staged-sale.md) section 5): parts 1-3 sold by 11 Dec (tax Rs 2,65,012) add about Rs 1,98,800 to the 15 Dec instalment (pay about Rs 2,62,300 in all); part 4 sold 16-18 Dec (tax Rs 88,830) goes to 15 Mar (about Rs 2,37,000 in all by 15 Mar). `tax/global-actions-2026-11.md` row 1: no US tax on the sale; proceeds reinvested abroad within 180 days need no new remittance and no TCS (AD bank to confirm).

## Kept shares and share count

| Item | Shares | Source |
|---|---|---|
| QCOM held at IBKR | 761 | `portfolio/summary.md` (IBKR, prices 2026-11-13) |
| Sale 1 + Sale 2 + kept | 432 + 195 + 134 = 761 | `portfolio/plan.md`, [qcom-lots.md](../../tax/employer-stock/qcom-lots.md) 3.4 |
| Kept 134 (FIFO leaves the newest lots) | 2023-11-20: 18; 2024-01-31: 29; 2024-02-20: 23; 2024-05-20: 48; DRIP 2024-09-26 to 2025-12-18: 16.0; gain Rs 3,16,174, tax Rs 47,268 when sold | [qcom-lots.md](../../tax/employer-stock/qcom-lots.md) 3.4 |

Check: match. Only note: `portfolio/plan.md` says Sale 1 "about 430 shares (432)"; STATUS.md already records that 432 is used.
