# Event playbook: what to do when markets move

Written 2026-11-15 by finance-trader. Rules from [AGENTS.md](../AGENTS.md) Trading rules (approved
2026-11-15 for paper trading only), the [money plan](../portfolio/plan.md), the
[starter trading rules](../research/themes/starter-trading-rules.md) and the [backtests](backtests/index.md).
Agents never place orders; you do.

## Summary
- Big news is not a reason to act. First check: is it a holding, does it have a plan, does the plan say what to do?
- Your long-term plan (fund switches, QCOM/MSFT sales on fixed dates, staged buys) goes on unchanged in most events.
- Trades follow the rules card: stop set at entry, max loss Rs 2,000 a trade, limit orders, never add below entry.
- Your own history is why: 98 INDmoney trades realised -$542; 16 of 19 losers sold more than 20% down; averaging down cost -$1,213.
- Until the paper check passes (8 weeks, 20 trades) every trade in this note is a paper trade.

## Who does what
| Step | Session | What it gives you |
|---|---|---|
| Detect | finance-news | Dated news, score -2..+2, catalysts; alert on bad news in a holding |
| Verdict | finance-research | Is the business or the outlook really changed? Note in `research/stocks/` |
| Setup | finance-trader | Entry, stop, target, size in `trading/plans/`; marks plans hit, stopped or changed |
| Tax line | finance-tax | Tax on the sale or buy (holding period, short or long term, LRS) |
| Decide | finance-main, then you | Daily short list (ready / watch / exit); you place the order |

## 1. A stock or sector falls sharply (sell-off, "buy the dip")
| | Rule |
|---|---|
| Check | Why it fell (news file); is it a holding or a researched watchlist name with a plan? |
| Who | news detects; research says if the business changed; trader updates the plan; tax line before any sale |
| Do | Buy the dip only in a name that already has a research note and a plan, in 2-3 stages, each with its own stop and size |
| Do not | Never add to a losing trade (no averaging down); no new name found in the sell-off itself; no buying before results (5-day rule) |
| Evidence | Averaging down in FLNA, SNTI, CERO lost -$1,213; RSI(2) dip-buying failed with the rules stop (US 1.4%/yr, India -8.8%/yr), [swing-pullback](backtests/swing-pullback/index.md) |

## 2. A stock or sector rallies hard (chasing)
| | Rule |
|---|---|
| Check | Is it on the watchlist with a plan? How far above the plan's entry? Would the stop be wider than 10%? |
| Who | news detects; trader checks the setup; research only if it is a new name |
| Do | Enter only on the plan's trigger (close above the prior 50-day high) with a limit order; if the stop must be over 10% wide, skip |
| Do not | No market orders; no buying a name you have not researched because it is in the news; no bigger size after one big win |
| Evidence | Donchian 50/20 breakouts with the rules stop: US 13.1%/yr, worst drop -23.1% vs SPY 13.9% / -33.7%; India only 5.1%/yr ([trend-following](backtests/trend-following/index.md)); IONQ +$2,131 was 52% of all gains |

## 3. Central bank hikes or cuts (Fed, RBI, ECB, BoJ)
| | Rule |
|---|---|
| Check | Was it expected? Usual effect (not a rule): hike -> bonds and growth stocks down, home currency up, gold down; cut -> the opposite. A Fed hike tends to lift USD/INR; an RBI hike tends to lower it; a BoJ hike can make yen-funded trades unwind fast |
| Who | news detects; research updates [fixed income and cash](../research/themes/opp-fixed-income-cash.md); tax only if the plan changes |
| Do | Keep the plan: staged buys go on their dates; keep bond duration short while rates rise |
| Do not | No panic sale of funds; no switch of the whole FD money at once; no rate bets (derivatives are excluded) |
| Evidence | Research 2026-11-15: rates are rising in both countries (RBI repo 5.50%, Fed 3.75-4.00%, more hikes expected), so keep duration short; no backtest of rate events here |

## 4. Results surprise or guidance cut in a holding
| | Rule |
|---|---|
| Check | Size of the miss, the guidance change, the market's reaction, the score change |
| Who | news detects and rescores; research decides if the 1-3 year estimate changes; trader updates stop and target; tax line before a sale |
| Do | Before results: no new entry within 5 trading days; cut a trade above half the normal risk. After: if the stop is hit, exit; if research cuts the case, follow the exit rule in the plan |
| Do not | No moving a stop down to "give it room"; no buying more because it is cheaper |
| Evidence | Earnings rule in AGENTS.md (applied by hand, not backtested); losers were held as long as winners (median 249 vs 239 days) |

## 5. Currency shock (USD/INR)
| | Rule |
|---|---|
| Check | The move in %, the reason (Fed, RBI, oil, outflows); which holdings it touches |
| Who | news detects; research checks [cash and currencies](../research/global/cash-and-currencies.md); tax on any USD you bring home |
| Do | Nothing in most cases: about two-thirds of your money is in USD, so a weaker rupee raises its INR value. QCOM and MSFT sales go on their dates; park USD waiting to be invested in IB01, not idle cash |
| Do not | No FX trading (not allowed under LRS); no timing the QCOM sales on the rupee |
| Evidence | The rupee lost about 3.5% a year vs USD over 10 years (research 2026-11-15); you are 81% USD already, so more USD adds little hedge |

## 6. Oil or war shock
| | Rule |
|---|---|
| Check | Oil price move, which markets are hit (India imports oil: rupee and Indian stocks usually fall on high oil); holdings in energy, shipping, defence |
| Who | news detects; research says if the shock changes a thesis; trader updates stops on open trades |
| Do | Keep the plan; the energy fund (XDW0) and gold in the plan are there for this; stops on trades stay where they are |
| Do not | No buying war or oil "theme" names without a note and a plan; no full exit from long-term funds |
| Evidence | Gold is a hedge but not a safe one: it fell 27% from its Jan 2026 high ([gold research](../research/themes/silver-gold.md)); the energy fund moves almost opposite to your tech shares ([plan](../portfolio/plan.md)) |

## 7. Market-wide fall of 10% or 20%
| | Rule |
|---|---|
| Check | Index fall from its high (Nifty, S&P 500); your mix vs the plan targets (4 Indian funds 54.5 / 8.7 / 18.1 / 18.7%, gold 5%) |
| Who | news detects; research checks valuations; finance-main computes the gap to targets; tax line for each switch |
| Do | At -10%: keep going, buy on plan dates. At -20%: rebalance back to targets by buying what fell, in 3-4 monthly stages, from cash already set aside (planned buys, maturing FDs) |
| Do not | No selling long-term funds in the fall; no emergency money or FDs broken early; trading: loss limits still apply (3 stops -> 1 week pause, month -4% -> stop) |
| Evidence | Worst falls: SPY -33.7%, Nifty -38.4% (2010-2026, [backtests](backtests/index.md)); momentum's index filter re-entered late after sharp falls; timing exits is not tested to help |

## 8. A stop or target is hit
| | Rule |
|---|---|
| Check | Did the stop or GTT order fill, and at what price? Loss above 1.2 x planned risk? |
| Who | trader marks the plan stopped or hit; journal logs exit and lesson; tax line for the realised gain or loss |
| Do | Stop hit: accept the exit. Target hit: exit or trail the stop up, as the plan says |
| Do not | No re-buying the same day to "win it back"; no moving the stop down; no cancelling a GTT before it fills |
| Evidence | Donchian wins about 4 trades in 10; profits come from a few big trends, so expect runs of small stopped losses; your 6 worst losses were 53-99% |

## 9. News score -2 on a holding
| | Rule |
|---|---|
| Check | The reasons and sources in `news/<SYMBOL>.md`; does the plan have a news exit? |
| Who | news scores and alerts; research gives the verdict within a day; trader applies the news exit; tax line before selling |
| Do | Trades: exit as the plan says (news exit at -2). Long-term holdings: wait for the research verdict, then decide; check the tax line (holding-period dates) |
| Do not | No sale on a headline before the research verdict; no buying more |
| Evidence | Rule in the plans since 2026-11-15; [journal signals](../journal/signals.md) will score if -2 calls were right (no result yet) |

## 10. IPOs
| | Rule |
|---|---|
| Check | Price band vs listed peers; offer for sale (money to sellers) or new money; overlap with what you own |
| Who | scout finds it; research writes a note in `research/ipo/`; trader sizes a listing-day trade; tax line |
| Do | Apply only with a research note that says yes, at most one minimum lot inside the trading budget |
| Do not | No SME IPOs; no US IPO allocations (adds US-situs stock); no buying in the first days after listing without a plan |
| Evidence | SME IPOs 2026: median return 3.9%, about half below issue ([universe](../scout/universe.md)); [MCL note](../research/ipo/MCL.md): default skip |

## Daily and weekly routine
Nothing runs on a timer: each session does these steps each trading day while it is open (`cns finance-main` starts the team).

| When | Who | What happens | What you get |
|---|---|---|---|
| Each trading day | finance-news | Filings, results, rating changes for holdings and watchlist; scores; catalysts in the next 10 days | `news/daily/<date>.md`; alerts on a 2-point score change, a catalyst within 5 days or bad news in a holding |
| Each trading day | finance-trader | Rechecks open plans and paper trades against prices and news; marks hit, stopped, expired | `ready` and `exit` rows to finance-main |
| Each trading day | finance-main | Builds the short list | Ready / watch / exit, one line each with the plan path |
| Each week | finance-scout | Scans 5 markets, new products, IPOs, rule and tax changes | Ranked ideas in the weekly brief |
| Each week | finance-news, journal | Compare scores with results; journal 15-minute review | Weekly brief from finance-main |
| Each month | finance-journal | Rules check and P&L vs budget | `journal/reviews/<YYYY-MM>.md` |

## Backtest bar
Scored by `.venv/bin/python trading/backtests/engine.py all` (35 names) and `engine.py universe-bar` (full universe), last run 2026-11-16 (daily Yahoo data 2010-01-01 to 2026-11-13). Paper trades in a market may use only strategies that pass on the FULL universe: none. Both universes are today's index members, so every result is biased upwards (survivorship). Items 1 and 2: every variant run is shown on the strategy pages; Faber and momentum have no rules-sized run with a stop.

A strategy may open paper trades in a market only if ALL of these hold for that market (scored on the rules-sized run: AGENTS.md stop and sizing, costs, 5 open, 3 new a week, 20% cap, whole shares):

| # | Test |
|---|---|
| 1 | Fixed published parameters, every variant shown |
| 2 | A rules-sized run with the stop and costs |
| 3 | At least 100 trades over the full period |
| 4 | Profit factor >= 1.2 for the full period AND for 2020-2026 |
| 5 | Positive average net trade in 2010-2019 and in 2020-2026 |
| 6 | Rules-sized CAGR > 0 |
| 7 | Rules-sized max drawdown no worse than -25% |

| Strategy | Version | Market | Universe | Bar | Failing items | Trades | PF full | PF 2020-2026 | Avg trade | CAGR | Max DD | Avg calendar days held |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [trend-following](backtests/trend-following/index.md) | Faber SMA200 monthly, stocks | US | 35 names | fail | no rules-sized run with the stop | - | - | - | - | - | - | - |
| [trend-following](backtests/trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | US | 35 names | PASS | - | 467 | 2.12 | 2.21 | 2.81% | 13.1% | -23.1% | 56 |
| [trend-following](backtests/trend-following/index.md) | Faber SMA200 monthly, stocks | India | 35 names | fail | no rules-sized run with the stop | - | - | - | - | - | - | - |
| [trend-following](backtests/trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | India | 35 names | fail | max DD -33.0% | 467 | 1.46 | 1.66 | 1.52% | 5.1% | -33.0% | 54 |
| [momentum-rotation](backtests/momentum-rotation/index.md) | Top-5 12-1 momentum, index filter | US | 35 names | fail | no rules-sized run with the stop | - | - | - | - | - | - | - |
| [momentum-rotation](backtests/momentum-rotation/index.md) | Top-5 12-1 momentum, index filter | India | 35 names | fail | no rules-sized run with the stop | - | - | - | - | - | - | - |
| [swing-pullback](backtests/swing-pullback/index.md) | RSI(2), rules stop, rules-sized | US | 35 names | fail | PF full 1.14 < 1.2; PF 2020-2026 1.15 < 1.2 | 2100 | 1.14 | 1.15 | 0.11% | 1.4% | -13.7% | 2 |
| [swing-pullback](backtests/swing-pullback/index.md) | RSI(2), rules stop, rules-sized | India | 35 names | fail | PF full 0.63 < 1.2; PF 2020-2026 0.63 < 1.2; avg trade 2010-2019 -0.39%; avg trade 2020-2026 -0.40%; CAGR -8.8%; max DD -79.3% | 2077 | 0.63 | 0.63 | -0.39% | -8.8% | -79.3% | 2 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | US | 35 names | fail | PF 2020-2026 1.19 < 1.2 | 1518 | 1.32 | 1.19 | 0.67% | 9.6% | -23.6% | 16 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | US | 35 names | fail | PF 2020-2026 1.17 < 1.2 | 1642 | 1.25 | 1.17 | 0.52% | 8.2% | -23.6% | 14 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | India | 35 names | fail | PF full 0.99 < 1.2; PF 2020-2026 1.08 < 1.2; avg trade 2010-2019 -0.17%; CAGR -1.6%; max DD -42.3% | 1433 | 0.99 | 1.08 | -0.02% | -1.6% | -42.3% | 17 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | India | 35 names | fail | PF full 1.00 < 1.2; PF 2020-2026 1.02 < 1.2; avg trade 2010-2019 -0.03%; CAGR -1.2%; max DD -49.0% | 1538 | 1.00 | 1.02 | 0.01% | -1.2% | -49.0% | 15 |
| [52w-high-breakout](backtests/52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | US | 35 names | PASS | - | 711 | 1.44 | 1.63 | 0.94% | 6.1% | -10.7% | 17 |
| [52w-high-breakout](backtests/52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R target, 20 days, rules-sized | India | 35 names | fail | PF full 0.84 < 1.2; PF 2020-2026 0.97 < 1.2; avg trade 2010-2019 -0.78%; avg trade 2020-2026 -0.09%; CAGR -3.3%; max DD -45.0% | 655 | 0.84 | 0.97 | -0.45% | -3.3% | -45.0% | 18 |
| [gap-drift](backtests/gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | US | 35 names | fail | PF 2020-2026 0.98 < 1.2; avg trade 2020-2026 -0.05% | 108 | 1.56 | 0.98 | 1.05% | 1.1% | -5.0% | 11 |
| [gap-drift](backtests/gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized | India | 35 names | fail | trades 54 < 100; PF full 1.17 < 1.2 | 54 | 1.17 | 1.36 | 0.39% | 0.2% | -5.4% | 14 |
| [trend-following](backtests/trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | US | full (679 names) | fail | max DD -35.2% | 590 | 1.57 | 1.40 | 2.26% | 10.4% | -35.2% | 50 |
| [trend-following](backtests/trend-following/index.md) | Donchian 50/20, rules stop, rules-sized | India | full (189 names) | fail | max DD -47.7% | 583 | 1.51 | 2.19 | 2.30% | 7.0% | -47.7% | 49 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | US | full (679 names) | fail | PF full 1.17 < 1.2; PF 2020-2026 1.14 < 1.2; max DD -29.0% | 1796 | 1.17 | 1.14 | 0.54% | 7.0% | -29.0% | 16 |
| [short-breakout](backtests/short-breakout/index.md) | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | US | full (679 names) | fail | PF 2020-2026 1.19 < 1.2 | 1921 | 1.21 | 1.19 | 0.66% | 9.8% | -24.1% | 14 |
| [52w-high-breakout](backtests/52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | US | full (679 names) | fail | PF 2020-2026 1.08 < 1.2 | 1432 | 1.21 | 1.08 | 0.58% | 6.9% | -23.2% | 18 |
| [52w-high-breakout](backtests/52w-high-breakout/index.md) | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | India | full (189 names) | fail | PF full 1.02 < 1.2; PF 2020-2026 1.04 < 1.2; CAGR -0.5%; max DD -35.4% | 1289 | 1.02 | 1.04 | 0.07% | -0.5% | -35.4% | 17 |
| [gap-drift](backtests/gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R, 20 days, rules-sized | US | full (679 names) | fail | PF full 1.08 < 1.2; PF 2020-2026 0.98 < 1.2; avg trade 2020-2026 -0.08%; max DD -25.8% | 1201 | 1.08 | 0.98 | 0.24% | 3.5% | -25.8% | 13 |
| [gap-drift](backtests/gap-drift/index.md) | Gap-up 4%+ on 3x volume, 2R, 20 days, rules-sized | India | full (189 names) | fail | PF full 1.04 < 1.2; PF 2020-2026 1.14 < 1.2; avg trade 2010-2019 -0.47% | 310 | 1.04 | 1.14 | 0.14% | 0.3% | -21.0% | 11 |
