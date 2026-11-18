# Target allocation

## Summary
Where your money should end up once the plan is done (QCOM by Apr 2027, vested MSFT by Sep 2028), with a band for each part.
`python -m scripts.mark` checks every day and fills in section Current below; a part outside its
band becomes an alert in [trading/alerts.md](../trading/alerts.md) (only "for information" while
the plan is still fixing it). US shares and single stocks stay far outside until the QCOM sales.
US and non-US equity count the global funds by the countries they hold (look-through); REITs are a class of their own.
New ideas from the scout buy list are paid for only as in section Money for new ideas.
Change a target or band here; the next run uses it.

## Targets
Shares are of your total (all accounts, savings, FDs, physical gold, EPF and Punjab Gramin Bank; the last two from `portfolio/manual-assets.csv`). Counts = the `asset` values in
[trading/positions.csv](../trading/positions.csv) that make up the part. Look-through: each global fund of the plan
counts by the countries it holds (table below), so US equity includes the US part of the funds. Classes and bands
approved by you on 2026-11-15.

| Class | Counts | Target | Band | Fix in progress | Source |
|---|---|---|---|---|---|
| US equity (look-through) | US equity | 25% | 18-32% | QCOM sales Nov-Dec 2026 and Apr 2027; MSFT lots to Sep 2028 (plan section 3) | [plan](plan.md) sections 4-5: 134 QCOM (about Rs 21.7 L), other US stocks (about Rs 14.5 L), XDEW and the US part of AVGS, XDWH, XDW0; [global moves](../research/global/README.md) section 3; your decision of 2026-11-15 |
| Non-US equity (look-through) | Non-US equity | 37% | 30-45% | QCOM sales Nov-Dec 2026 and Apr 2027, and the MSFT lots to Sep 2028, buy these funds (plan section 3) | [plan](plan.md) section 4: EXUS, IJPA, FLXC, Latin America and the non-US part of AVGS, XDWH, XDW0; [global moves](../research/global/README.md) section 3; your decision of 2026-11-15 |
| India equity | India equity | 8% | 5-12% | Dec top-ups, SIPs; the maturing FD money goes here first (from 10 May 2027) | [plan](plan.md) section 4: 4 core funds + Nifty Next 50, SIPs of Rs 60,000 a month (about Rs 7.2 L a year, about 1.7% of the total a year) and Rs 6 L from the FDs into UTI Nifty 50: check the band each quarter and cut or pause the SIPs before it goes over 12%; your decision of 2026-11-15 |
| REITs | REIT | 2% | 0-4% | | [global moves](../research/global/README.md) move 7 (Mindspace, Bagmane); funded only by the rule below; your decision of 2026-11-15 |
| Gold | Gold | about 3.5% | 3-6% | GOLDIETF Rs 1,97,734 from the silver sales in 2 parts (18-20 Nov, by 9 Dec 2026); no top-ups (your decision of 2026-11-16) | [gold](../research/themes/silver-gold.md); your decision of 2026-11-16: about 3.5% counting jewellery and gold funds, band 3-6%, no top-ups (replaces 5%, 4-6%) |
| Safe money (all) | Cash, Cash (USD), Arbitrage, FD, EPF | 21% | 15-25% | Punjab Gramin Bank FDs at maturity and HDFC FDs from 10 May 2027 into the plan monthly over 12-24 months | [global moves](../research/global/README.md) move 5 and section 3; savings, Rs 6 L emergency money, FDs (HDFC held to 2027-05-10; Punjab Gramin Bank, estimate), EPF (locked), arbitrage, USD cash or IB01 (5% of each sale); your decision of 2026-11-15 |
| Single stock (largest) | largest single stock | 10% at most | 0-10% | QCOM to about 7% after the Apr 2027 sale; MSFT lots sold to Sep 2028 (under 10% from Aug 2027) (plan section 3) | [QCOM/MSFT decision](../research/themes/employer-stock-decision.md): each single stock at most 10% |

Look-through weights (US share by country; the rest is non-US), from [global moves](../research/global/README.md)
section 3, 2026-11-15; the same table is `FUND_US` in `scripts/mark.py`:

| Fund | US share | Note |
|---|---|---|
| XDEW S&P 500 Equal Weight | 100% | |
| AVGS Global Small Cap Value | about 55% | not verified (active fund, no published split) |
| XDWH World Health Care | about 72% | |
| XDW0 World Energy | about 61% | |
| EXUS, IJPA, FLXC (or ICHN), Latin America (LTAM) | 0% | |

Not in a class: silver (all being sold: ABSL Silver ETF and the 2 FoFs on 18 Nov, ICICI Silver ETF by 9 Dec; your decision of 2026-11-16) and paper trades.
The Rs 6 L emergency money and the FDs (all 9 held to 2027-05-10) are part of safe money; the FD maturity alert
(30 days before) stays.

## Money for new ideas (scout buy list)
Ideas from [scout/buy-list.md](../scout/buy-list.md) are bought only with this money, so the bands above hold
(your decision of 2026-11-15):
1. Foreign ideas: up to 10% of each QCOM/MSFT sale, taken from the EXUS share (EXUS 45% of the sale -> at least 35%).
2. Indian ideas and REITs: from the May 2027 FD money, up to Rs 10 L of the arbitrage parking, as long as safe
   money stays at 18% or more of the total; after that from yearly new savings beyond the SIPs (you set the amount).
3. Caps: each idea at most 1% of the total (about Rs 4.2 L at Rs 4.21 Cr); all ideas together at most 5% (about Rs 21 L). The Rs 2 L
   trading budget is separate.
4. Before May 2027 an Indian idea can only use part of the unassigned money (about Rs 16.6 L: HDFC savings Rs 10.5 L,
   ABSL Silver ETF money Rs 4.2 L, rest of the silver money Rs 1.9 L; pending your decision), or wait.

## Event bets (single binary events)
Small bets on one dated yes/no event: a drug approval date (FDA), a Phase 3 trial result, a takeover vote or a
large contract decision (your decision of 2026-11-18). Reason: the quality screens leave out loss-making event
stocks, so moves like SELLAS (SLS, +156% on 17 Nov 2026 after a Phase 3 success) were missed.
1. Source: the catalyst calendar of `finance-scout` ([scout/events/calendar.md](../scout/events/calendar.md));
   `finance-research` checks each bet before it goes to you.
2. Caps: each bet at most 0.5% of the total (about Rs 2.1 L at Rs 4.21 Cr); all open event bets together at most
   3% (about Rs 12.6 L). Separate from the 5% cap for new ideas and from the Rs 2 L trading budget.
   Biotech (drug approval and trial result bets) open at the same time: at most 1.5% of the total (about
   Rs 6.2 L at Rs 4.16 Cr; your decision of 2026-11-18).
3. Each bet states: the event date, what happens if it wins and if it loses, how often such events succeeded in
   the past (base rate), and the exit rule: sell after the event either way, unless research says hold.
   Event bets have no stop loss (held through the event; the size cap limits the loss), so they are not trades
   under the trading rules card (stop on every trade) and do not count in the Rs 2 L trading budget.
4. You approve each bet before any order.
5. Approved 2026-11-18 (all biotech, Rs 3.5 L in all, 0.84% of the total; notes in `research/events/bets/`):

   | Bet | Size | Limit | Buy | Event | Account |
   |---|---|---|---|---|---|
   | Cogent (COGT) | Rs 1 L (about 38 shares) | $28.00 or less | this week, after checking why it fell 12% (10-17 Nov) | FDA 30 Nov (GIST) and 30 Dec (NonAdvSM) | INDmoney USD wallet |
   | Immunic (IMUX) | Rs 1 L (about 144 shares) | $7.40 or less | this week | Phase 3 MS topline, Dec 2026 | INDmoney USD wallet |
   | Mineralys (MLYS) | Rs 1.5 L (about 109 shares) | $14.60 or less | week of 14 Dec (by Fri 18 Dec) | FDA 22 Dec | not yet chosen |

   Declined: PolyPid (PYPD), Hitech Corp, Jindal Photo. Conditional, each needs a new yes from you when its
   condition is met: Shriram Finance (if BSE adds it to the Sensex), Castrol India (Rs 185 or less), Delivery Hero
   (EUR 35.50 or less), easyJet (660p or less).

<!-- generated by scripts.mark: start -->
## Current (2026-11-18)

Written by `python -m scripts.mark` on 2026-11-18; total marked Rs 4,16,33,634 (Rs 4.16 Cr); positions in [trading/positions.csv](../trading/positions.csv).

| Class | Target | Band | Current | Share | State |
|---|---|---|---|---|---|
| US equity (look-through) | 25% | 18-32% | Rs 1,91,71,416 | 46.0% | above (fix in progress) |
| Non-US equity (look-through) | 37% | 30-45% | Rs 0 | 0.0% | below (fix in progress) |
| India equity | 8% | 5-12% | Rs 15,14,315 | 3.6% | below (fix in progress) |
| REITs | 2% | 0-4% | Rs 0 | 0.0% | inside |
| Gold | about 3.5% | 3-6% | Rs 12,82,227 | 3.1% | inside |
| Safe money (all) | 21% | 15-25% | Rs 1,88,99,373 | 45.4% | above (fix in progress) |
| Single stock (largest) | 10% at most | 0-10% | Rs 1,20,69,773 (QCOM) | 29.0% | above (fix in progress) |

| Asset (positions.csv `asset`) | Value | Share |
|---|---|---|
| US equity | Rs 1,91,71,416 | 46.0% |
| FD | Rs 1,21,33,819 | 29.1% |
| EPF | Rs 41,03,127 | 9.9% |
| Cash | Rs 18,54,314 | 4.5% |
| India equity | Rs 15,14,315 | 3.6% |
| Gold | Rs 12,82,227 | 3.1% |
| Silver | Rs 7,66,303 | 1.8% |
| Cash (USD) | Rs 5,05,267 | 1.2% |
| Arbitrage | Rs 3,02,847 | 0.7% |
<!-- generated by scripts.mark: end -->
