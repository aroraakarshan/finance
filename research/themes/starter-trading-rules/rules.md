# Starter trading rules: proposed rules with reasons

Back to the index: [../starter-trading-rules.md](../starter-trading-rules.md).

## Summary
Fixed Rs 2 L budget, max loss Rs 2,000 (1%) a trade, stop below swing low or 2 x ATR capped at 10%, size = risk / (entry - stop).
Limit orders only; no stocks under $5 / Rs 50, OTC, F&O, margin or derivatives abroad (RBI LRS); no averaging down.
Paper trade 8 weeks and 20 trades first, with the pass criteria in item 13. Sources are inline and listed at the end.

## Proposed rules

1. **Trading budget: fixed cap Rs 2,00,000; base = market investments excluding employer stock, bank money, EPF and physical gold.**
   - Why not 5% of Rs 4.21 Cr (Rs 21.0 L): 43.1% of that total is employer-plan stock (QCOM,
     MSFT). It is one concentrated position to manage down over time, not money free to
     trade, and its value swings with two share prices.
   - Why this base: AngelOne (Rs 26.25 L) plus non-employer US holdings and cash (Rs 18.39 L)
     = Rs 44.64 L is what he could actually move. The Rs 2 L cap was set at 5% of the earlier
     base (Rs 40.97 L); counting INDmoney wallet cash raised the base, so Rs 2 L is now about
     4.5% (5% would be Rs 2.23 L). The cap stays at Rs 2 L; the conclusion does not change.
   - Why HDFC savings (Rs 8.54 L) and FDs (Rs 49.31 L with accrued interest) are left out: they
     are the safe part (cash buffer and fixed deposits to 2027-05-10, 13.7% of the total together),
     not risk money. Counting them would raise 5% of the base to Rs 5.12 L; the cap stays at Rs 2 L.
   - Physical gold (Rs 12.90 L, 3.1% of the total) is left out too: it is not cash in a
     trading account.
   - Punjab Gramin Bank (Rs 82 L estimate, 19.5%) is left out: it is safe money, and plan.md
     (decided 2026-11-15) already gives it jobs: savings to GOLDIETF on 15 Dec 2026 and 15 Jan
     2027, FDs at maturity to Indian and world funds over 12-24 months.
   - EPF (Rs 41.03 L, 9.7%) is left out: it is locked retirement money, not available to trade.
   - Counting every bank deposit and EPF would make 5% of the base Rs 11.3 L; the cap stays Rs 2 L.
   - Why a fixed rupee cap: the base itself moves with markets; a fixed number does not grow
     by accident, and it is a sum he could lose fully without changing any life goal.
   - Why small: realised result -$542 after 98 trades, 19 of 30 stocks lost, and without
     IONQ -$2,673. Most retail traders lose ([research-and-tax.md](research-and-tax.md)). Raise to at most Rs 4 L only after
     6 months of following the rules with a positive result after costs.
2. **Max loss per trade: 1% of budget = Rs 2,000 / $21; 0.5% = Rs 1,000 / $11 for the first
   3 months.** A run of 10 losses then costs 5-10% of the budget, not the account. His worst
   single loss ($737 = Rs 69,400) was about 35 times Rs 2,000. The 1% figure is a common practitioner rule
   of thumb, not a research result.
3. **Stop-loss method.** Options:
   - Fixed % (e.g. 8%): simple, ignores how much the stock normally moves.
   - ATR-based (2 x ATR(14)): adjusts to volatility. ATR from J. Welles Wilder, "New Concepts
     in Technical Trading Systems", 1978.
   - Below the recent swing low: tied to the chart reason for the trade.
   Proposal: below swing low or 2 x ATR, capped at 10%. If the stop must be wider, skip the
   trade. Placement (checked 2026-11-15):
   - Alpaca: stop, stop-limit, trailing stop, bracket and OCO orders; a stop becomes a market
     order when triggered, so a gap can fill below the stop (docs.alpaca.markets/docs/orders-at-alpaca, undated).
   - INDmoney app: "Limit Orders & Stop Loss" listed (indmoney.com/us-stocks, undated).
   - IBKR: stop, stop-limit, trailing and bracket orders (interactivebrokers.com/en/trading/ordertypes.php).
   - AngelOne: GTT exists in its SmartAPI library (github.com/angel-one/smartapi-python
     README). Stop-loss GTT / OCO GTT for equity delivery NOT VERIFIED; check in the app.
4. **Position sizing: shares = max loss / (entry - stop); cap 20% of budget per position.**
   - India: budget Rs 2,00,000, max loss Rs 2,000. Buy at Rs 500, stop Rs 460 -> risk Rs 40
     a share -> 50 shares = Rs 25,000 (12.5% of budget). Stop hit = -Rs 2,000 plus costs.
   - US: max loss $21. Buy at $80, stop $74 -> $6 a share -> 3 shares = $240.
   - Cap: if the formula gives more than Rs 40,000, buy Rs 40,000.
5. **Max 5 open positions.** 5 x 1% = 5% of budget at risk at once; with a full-time job, 5
   is about what can be checked each evening.
6. **Limit orders only.** 97 of 98 past orders were market orders. The SEC says microcap
   stocks "tend to be low priced and trade in low volumes" and are "less liquid"
   (sec.gov "Microcap Stock: A Guide for Investors", last reviewed 2013-09-18). That wider
   spreads make market orders cost more on such stocks is likely but NOT VERIFIED from a
   primary source here.
7. **Exclusions.**
   - Under $5: the SEC "penny stock" rule excludes stocks priced $5 or more (17 CFR
     240.3a51-1(d), ecfr.gov, current). Under Rs 50 has no official basis; it is the user's
     existing choice.
   - OTC/pink sheets: same liquidity reason (SEC microcap guide above).
   - No F&O: SEBI found 89% of individual F&O traders lost in FY22 (study 2023-01-25),
     93% over FY22-FY24 with losses over Rs 1.8 lakh crore (2024-09-23), about 91% in FY25
     with net loss Rs 1,05,603 crore (2025-07-07), and 87.7% in FY26 (2026-08 study). Links in [research-and-tax.md](research-and-tax.md).
   - No derivatives or margin abroad: RBI LRS Master Direction para 5 (updated 2024-09-06):
     remittances "for margins or margin calls to overseas exchanges/ overseas counterparty
     are not allowed" (rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192). Overseas
     Investment Directions 2022 (A.P. (DIR Series) Circular No. 12, 2022-08-22): portfolio
     investment "shall not be made in ... any derivatives unless otherwise permitted by
     Reserve Bank" (rbi.org.in/Scripts/NotificationUser.aspx?Id=12381&Mode=0).
8. **No averaging down.** FLNA, SNTI and CERO lost $1,213 together after adding lower.
   Adding to a winner is allowed only with a new stop that keeps total risk within 1%.
9. **Earnings rule.** Results can gap a stock past the stop (a triggered stop fills at market).
   Practitioner rule, no study cited here.
10. **Max 3 new trades a week.** Past bursts of 14-21 trades a month; SEBI found 80% of
    intraday traders with more than 500 trades a year lost vs 71% overall (2024-07-24);
    Barber & Odean found the most active traders earned least ([research-and-tax.md](research-and-tax.md)).
11. **Loss limits.** 3 stops in a row -> pause 1 week; -4% of budget in a month -> stop for the
    month; -10% of budget -> stop and review rules. Practitioner rules, not research results.
12. **Journal every trade** in `journal/` (finance-journal agent checks it against these rules).
13. **Paper trading: 8 weeks and at least 20 trades.** Pass only if all hold:
    every trade had a stop and size from the formula before entry; no rule breaks; no loss
    larger than 1.2 x planned risk; journal complete; result not worse than -5% of budget.
    Paper accounts exist at Alpaca and IBKR (NOT VERIFIED here; check). A spreadsheet works too.
14. **Review cadence.** Weekly 15 min; monthly rules and P&L check; after each quarter decide
    keep, change or stop. Stop trading if two quarters in a row are negative after costs.

## Sources
- Wilder, "New Concepts in Technical Trading Systems", 1978 (ATR).
- docs.alpaca.markets/docs/orders-at-alpaca; indmoney.com/us-stocks; interactivebrokers.com/en/trading/ordertypes.php; github.com/angel-one/smartapi-python (all checked 2026-11-15).
- sec.gov "Microcap Stock: A Guide for Investors" (2013-09-18); 17 CFR 240.3a51-1 (ecfr.gov).
- RBI LRS Master Direction (rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192, 2024-09-06); Overseas Investment Directions 2022 (rbi.org.in/Scripts/NotificationUser.aspx?Id=12381&Mode=0).
- SEBI and academic studies: see [research-and-tax.md](research-and-tax.md).
