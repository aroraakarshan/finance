# Beginner trading: what to avoid, 12-week path, tax, open points

Back to the index: [../opp-beginner-trading.md](../opp-beginner-trading.md). Written 2026-11-15; research only, no orders.

## Summary
- Avoid intraday (71% lose), F&O (87.7-93% lose across SEBI studies), penny/SME stocks, tips, short-term mean reversion, derivatives abroad.
- Weeks 1-8 paper trade one rule set; weeks 9-12 real money in India at Rs 1,000 risk a trade; week 12 review.
- Pass: expectancy above 0 after costs over 20+ trades, drawdown within limits, average loss no larger than 1.1 R, every trade with a stop.
- Tax: Indian shares/equity ETFs up to 12 months 20% STCG; US shares/ETFs up to 24 months at slab (35.88% for him).
- Still not verified: ETF STT/stamp, IBKR plan, NSE ETF spreads, two paper findings.

## 3. What to avoid (evidence)

| Avoid | Evidence |
|---|---|
| Intraday (India) | SEBI study 2024-07-24 (FY23): 71% of individual intraday traders lost; 80% of those with 500+ trades a year. Also taxed as speculative income at slab. Details and links: [starter-trading-rules/research-and-tax.md](../starter-trading-rules/research-and-tax.md) |
| Indian F&O ("not yet", not "never") | SEBI: 89% lost in FY22 (2023-01-25); 93% over FY22-FY24, losses over Rs 1.8 lakh crore (2024-09-23); about 91% in FY25, net loss Rs 1,05,603 crore (2025-07-07); 87.7% in FY26, net loss Rs 91,685 crore (2026-08). Links in the rules file section 3. Livemint 2026-08-21 headline: 89% of investors under 30 lost in FY26 (headline only) |
| Penny and SME stocks | His own record: 9 names bought under $5, net -$1,627 (rules file section 1). SME manipulation: SEBI banned 7 unregistered finfluencers in a Rs 20 crore social-media SME scheme (Livemint 2026-05-25, Business Standard 2026-05-25, NDTV Profit 2026-05-22; headlines only, SEBI order not read) |
| Tips, Telegram, finfluencers | Same case as above. Rule: no trade whose reason is someone else's call |
| Short-term mean reversion in single stocks | Profits below trading costs (Avramov, Chordia & Goyal 2004, above) |
| Options, futures, margin abroad | Not allowed under RBI LRS / Overseas Investment Directions (rules file, item 7) |
| Leveraged or inverse ETFs | Excluded by the rules card |

## 4. 12-week learning path

| Weeks | Do | Tool | Pass to move on |
|---|---|---|---|
| 1 | Pick ONE rule set (A, B or C); write it on one page; set up journal | TradingView free charts (free-plan limits NOT VERIFIED) | Written rules, journal template |
| 1-8 | Paper trade the rules, decisions only after market close | IBKR free trial / paper: real market prices incl. commissions, data delayed 10-15 min (interactivebrokers.com/en/trading/free-trial.php, fetched 2026-11-15); paper for an existing live account NOT VERIFIED. Or a spreadsheet | Rules card paper criteria: 8 weeks and 20+ trades, no rule breaks, no loss over 1.2 x planned risk, result not worse than -5% of budget |
| 9-12 | Real money in India only, 0.5% risk (Rs 1,000) a trade, max 3 positions | AngelOne limit orders; GTT for exits (stop-loss GTT for delivery NOT VERIFIED, check in app) | Same criteria on real trades |
| 12 | Review all trades | Journal | Decide keep / change / stop |

Metrics to compute every 4 weeks (in R = planned risk per trade):
- Win rate = winners / closed trades. Not a goal on its own: trend methods win 30-45%.
- Average win and average loss (in R and in Rs, after costs).
- Expectancy = win rate x avg win - loss rate x avg loss. Pass: above 0 after costs over 20+ trades.
- Max drawdown of the budget. Pass: no worse than -5% (paper) / -4% in any month (rules card).
- Average loss no larger than 1.1 R (shows stops are honoured); zero trades without a stop.
Twenty trades are too few to prove an edge; they can only show whether the rules are followed.

## 5. Tax (one line)
India listed shares/equity ETFs held up to 12 months: 20% STCG; intraday = speculative at slab;
US shares/ETFs short-term (up to 24 months) at slab, 35.88% for him - see
[../../tax/investment-types.md](../../../tax/investment-types.md) (gold ETF tax not checked here).

## 6. Not verified / discrepancies
- ETF STT and stamp duty rates; IBKR plan for his account; NSE ETF spreads; S&P 100 list.
- Jegadeesh-Titman 1993 and Sullivan-Timmermann-White 1999 findings beyond the abstracts.
- Yahoo NSE data errors (2019 ETF prints, TMPV demerger) mean any yfinance India backtest must
  be checked for jumps before use.
- The task brief gives SEBI F&O loss shares as "91-93%"; the FY22 study says 89% and FY26 87.7%.
