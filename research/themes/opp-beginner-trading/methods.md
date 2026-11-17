# Beginner trading: methods with evidence and own backtests

Back to the index: [../opp-beginner-trading.md](../opp-beginner-trading.md). Written 2026-11-15; research only, no orders.

## Summary
- Trend following, 12-1 momentum and the 52-week high have long academic records; short-term reversal does not survive costs.
- 200-day-MA filter, 10 years: smaller drawdowns (NIFTYBEES -21.5% vs -36.3%) but lower return (8.5% vs 13.2% a year).
- Momentum on today's Nifty 50: 24.9% vs 21.7% equal weight, inflated by survivorship bias; real Momentum 30 fund 14.4% vs 10.6%, drawdown -31.5%.
- Win rates 30-45%: a few big wins pay for many small losses, so honouring stops matters most.
- Pick ONE rule set (A ETF trend, B monthly momentum, C 52-week-high swing) to paper trade.

## 2. Methods with evidence (all decidable after market close)

| Method | Evidence | Fit for him |
|---|---|---|
| Time-series trend (hold while price is above its own past) | Moskowitz, Ooi & Pedersen, "Time series momentum", JFE 104 (2012) 228-250: positive in each of 58 liquid futures; returns persist 1-12 months, partly reverse later. Hurst, Ooi & Pedersen, "A Century of Evidence on Trend-Following Investing", JPM 44(1) (2017) 15-29: 67 markets 1880-2016, consistently profitable; average Sharpe about 0.4 per market (gross); positive in 8 of the 10 worst 60/40 drawdowns | Partial: the papers go long AND short in futures across many markets with volatility scaling. He can only go long, cash, few markets. Long-only on 1-2 index ETFs is a much weaker version |
| Cross-sectional momentum (buy recent 12-month winners) | Jegadeesh & Titman, J. Finance 48 (1993) 65-91 (winners minus losers over 3-12 months; abstract not retrieved, details NOT VERIFIED here). India: IIMA data library (faculty.iima.ac.in/iffm/Indian-Fama-French-Momentum/) publishes an Indian momentum factor | Good: monthly, long-only top names works on Nifty 50; has crashes (see 2.1) |
| 52-week high (buy stocks near their 1-year high) | George & Hwang, J. Finance 59 (2004) 2145-2176: nearness to the 52-week high "explains a large portion of the profits from momentum" and does not reverse later. India: Raju (2023, SSRN 4587697, abstract via Crossref), Oct 2004-Aug 2023: robust, "more stable alpha than academic momentum" | Good: simple screen, natural stop below the breakout |
| Breakout / moving-average rules | Brock, Lakonishok & LeBaron, J. Finance 47 (1992) 1731-1764 (Dow 1897-1986). Sullivan, Timmermann & White, J. Finance 54 (1999) 1647-1691 re-test these rules for data snooping; that the best rule fails after 1986 is widely cited but NOT VERIFIED from the abstract | Use only as an entry trigger inside momentum / 52-week-high, not alone |
| Short-term reversal / swing mean reversion | Jegadeesh, J. Finance 45 (1990) 881-898: last month's losers beat winners, 2.49% a month between extreme deciles, 1934-1987. Avramov, Chordia & Goyal (SSRN 555968, 2004): reversals are largest in illiquid stocks and "profits are smaller than the likely transactions costs" | Poor: needs frequent trades, works where costs are high; skip |

Typical shape of these methods (from the backtests below): win rate 30-45%, a few large wins
pay for many small losses. That is the opposite of his history (losses held, median -22%), so
the stop rule matters more than the entry signal.

### 2.1 Own backtests (yfinance, run 2026-11-15, 2016-11-14 to 2026-11-13)
Method: daily adjusted closes; signal at a close, trade at the next close; out-of-market cash
earns 0% (real liquid fund / T-bill interest would add, not computed); no tax.
Data fixes: NIFTYBEES/BANKBEES/GOLDBEES had bad Yahoo prints on 2019-12-19/20 (about -90%,
then +900%); removed. TMPV shows an unadjusted -40% on 2025-10-14 (Tata Motors demerger)
and TRENT -33% on 2026-01-01 (cause not verified); left in.

| Test | CAGR | Max drawdown | Trades | Win rate, avg win / avg loss | Buy-and-hold |
|---|---|---|---|---|---|
| NIFTYBEES above 200-day MA, cost 0.15%/side | 8.5% | -21.5% | 43 round trips, in market 78% | 45%, +6.8% / -1.5% | 13.2%, -36.3% |
| SPY above 200-day MA, cost 0.30%/side (IBKR Fixed, small size) | 9.4% | -27.7% | 25, in 84% | 29%, +15.0% / -2.9% | 15.1%, -33.7% |
| Same, cost 0.05%/side | 10.7% | -24.2% | 25 | 29%, +15.5% / -2.4% | 15.1%, -33.7% |
| 12-1 momentum, today's Nifty 50, top 10 equal weight, monthly, 0.20%/side on turnover | 24.9% | -29.1% (monthly) | one-way turnover 25% a month | yearly: 2017 +69, 2018 0, 2019 +16, 2020 +22, 2021 +61, 2022 +7, 2023 +45, 2024 +56, 2025 +9, 2026 -3 | Equal-weight today's 50: 21.7%, -27.9%; NIFTYBEES 13.1%, -28.8% |

- Survivorship bias: the basket uses today's 50 names, i.e. the past winners. Equal weight of
  them beat NIFTYBEES by 8.6 points a year, which is mostly this bias. Only the 3.2-point gap
  momentum vs equal weight is a fair comparison, and even that is inflated.
- Real-index check (mfapi.in NAVs, 2021-03-12 to 2026-11-13): UTI Nifty 200 Momentum 30 Index
  Fund (Direct) 14.4% a year, max drawdown -31.5% (2024-09-27 to 2025-04-07); UTI Nifty 50
  Index Fund (Direct) 10.6%, -16.6%. Calendar years momentum vs Nifty 50: 2022 -5 vs +5,
  2023 +41 vs +21, 2024 +21 vs +10, 2025 -5 vs +12, 2026 to date -1 vs -3.
- The 200-DMA filter did what trend following promises (smaller drawdowns) at a cost in return
  over a strong decade; after Indian STCG on every exit it would look worse.

### 2.2 Proposed rule sets (only if the rules card is adopted; pick ONE to paper trade)
- A. ETF trend (least time): NIFTYBEES (and optionally GOLDBEES, BANKBEES). Check every Friday
  evening: hold if the close is above the 200-day MA, sell next day with a limit order if not.
  Size by the rules card (stop = 200-DMA or 10%, whichever is closer).
- B. Monthly momentum: last trading day of each month, rank Nifty 50 by 12-month return skipping
  the last month; hold the top 5 at about Rs 30,000-40,000 each (rules card caps 5 positions /
  Rs 40,000). Exit at the monthly rank-out or the 10% hard stop. Conflict: the rules card wants a
  swing-low/ATR stop on every trade; momentum research uses no stops. User decides.
- C. 52-week-high swing: Nifty 50 stock closes at a new 52-week high on above-average volume;
  buy next day with a limit at most 1% above the close; stop below the last swing low (max 10%);
  exit on a close below the 50-day MA. Rules (A-C) are my proposals; parameters not optimised.
