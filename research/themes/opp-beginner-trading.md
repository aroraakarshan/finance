# Beginner trading: what to trade, which methods, what to avoid (proposals)

Written 2026-11-15. Research only, no orders. Everything below is a PROPOSAL and applies only
if the user adopts the rules card in [starter-trading-rules.md](starter-trading-rules.md)
(Rs 2 L budget, max loss Rs 2,000 a trade, stop at entry, limit orders, nothing under $5 / Rs 50,
8 weeks / 20 paper trades first). Those rules and his trade history are not repeated here.
Sources: [../sources.md](../sources.md). Prices: yfinance closes of 2026-11-13; USD/INR 94.03.

## Summary
- Start in India only: Nifty 50 stocks and NIFTYBEES/BANKBEES/JUNIORBEES/GOLDBEES at AngelOne, end-of-day; US large caps/ETFs at IBKR later, if at all (costs, slab tax, estate tax).
- Smallest sensible position: about Rs 20,000 in India (round trip 0.4-0.6%); about $200 in the US with IBKR Tiered pricing ($300+ with Fixed). Below that, fixed fees eat the edge.
- Best-supported part-time methods: trend following (price above a long moving average) and 3-12 month momentum / 52-week high, checked weekly or monthly; long academic records but win rates 30-45% and drawdowns of 20-30%.
- 10-year backtests: a 200-day-MA filter cut drawdowns by about a third but earned 4-6 points a year less than buy-and-hold (cash at 0%); momentum on today's Nifty 50 beat an equal-weight basket by about 3 points a year, but survivorship bias makes it look too good.
- Avoid intraday, F&O, penny/SME stocks, tips and anything leveraged or derivative abroad; paper trade ONE rule set for 8 weeks first.

## Key comparison: own backtests (yfinance, run 2026-11-15, 2016-11-14 to 2026-11-13)

| Test | CAGR | Max drawdown | Win rate | Buy-and-hold |
|---|---|---|---|---|
| NIFTYBEES above 200-day MA, cost 0.15%/side | 8.5% | -21.5% | 45% | 13.2%, -36.3% |
| SPY above 200-day MA, cost 0.30%/side | 9.4% | -27.7% | 29% | 15.1%, -33.7% |
| 12-1 momentum, today's Nifty 50, top 10 (survivorship bias) | 24.9% | -29.1% (monthly) | - | Equal weight 21.7%; NIFTYBEES 13.1% |
| Real fund check: UTI Nifty 200 Momentum 30 vs UTI Nifty 50 (2021-03-12 to 2026-11-13, mfapi.in) | 14.4% vs 10.6% | -31.5% vs -16.6% | - | - |

Method, data fixes and caveats: [methods.md](opp-beginner-trading/methods.md).

## Parts

| Part | Contents |
|---|---|
| [what-to-trade.md](opp-beginner-trading/what-to-trade.md) | Universe and liquidity (India, US, UCITS), round-trip costs at AngelOne and IBKR, minimum position, budget split |
| [methods.md](opp-beginner-trading/methods.md) | Evidence for trend, momentum, 52-week high, breakout, reversal; own backtests; proposed rule sets A-C |
| [avoid-and-learning-path.md](opp-beginner-trading/avoid-and-learning-path.md) | What to avoid with evidence, 12-week learning path and metrics, tax line, not verified / discrepancies |
