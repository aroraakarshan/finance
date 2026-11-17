# Beginner trading: what to trade and what it costs

Back to the index: [../opp-beginner-trading.md](../opp-beginner-trading.md). Written 2026-11-15; research only, no orders.

## Summary
- Start with Nifty 50 stocks and NIFTYBEES/BANKBEES/JUNIORBEES/GOLDBEES at AngelOne; all are far more liquid than needed.
- US: SPY/QQQ/IWM/sector SPDRs and S&P 100 names at IBKR later, max about $1,000; US-situs for estate tax.
- Round trip on Rs 10-40k: AngelOne stock 0.40-0.69%, equity ETF 0.20-0.50%; IBKR Fixed $2.00, Tiered about $0.72.
- Smallest sensible position: about Rs 20,000 in India, about $200 (Tiered) or $300+ (Fixed) in the US.
- IBKR FX is 0.002% but with a $2 minimum: convert once, not per trade.

## 1. What to trade

| Market | Universe | Liquidity (avg daily traded value, last 60 sessions to 2026-11-13, yfinance) | Note |
|---|---|---|---|
| India | Nifty 50 stocks (list: archives.nseindia.com ind_nifty50list.csv, fetched 2026-11-15) | Lowest: TATACONSUM Rs 144 cr, CIPLA Rs 146 cr; median Rs 387 cr. Cheapest share: TATASTEEL Rs 187 | All 50 are far above the Rs 50 floor |
| India | NIFTYBEES / BANKBEES / JUNIORBEES / GOLDBEES | Rs 209 cr / 41 cr / 30 cr / 328 cr; close Rs 286.6 / 630.7 / 789.0 / 111.9 | GOLDBEES is gold, not equity (different STT and tax) |
| US | SPY, QQQ, IWM; sector SPDRs (XLK, XLF, XLE ...) | $33.0 bn / 27.6 bn / 6.6 bn; XLK 1.7 bn, XLF 1.9 bn, XLE 2.1 bn | SPY $754, QQQ $680: one share is above the $21-risk size, so needs fractional shares (stop orders on fractions not verified) |
| US | S&P 100 large caps | Not measured here (constituent list not fetched) | Same rules: only names above $5, no OTC |
| Global | Irish UCITS (CSPX etc.) at LSE | Not measured | Not US-situs; better for long-term money than trading. See [ibkr-global/equities.md](../ibkr-global/equities.md) 3.2 |

- Bid/ask spreads of the NSE ETFs: NOT MEASURED (NSE quote API returned no data on 2026-11-15,
  a Sunday). Check the live order book in the app before each order; skip if the spread is
  over 0.1%. The 0.1% cut-off is my rule of thumb, not a sourced number.
- US-situs: US stocks and US ETFs count toward the $60,000 US estate-tax threshold; he is
  already above it through employer stock ([us-estate-tax.md](../us-estate-tax.md)). A $2,100
  trading account adds little, but it is one more reason to start in India.
- Budget split (proposal): all Rs 2 L in India at first. A US sleeve (max about $1,000) only
  after the India pass criteria in section 4; with $21 risk a trade, US sizes are tiny.

Round-trip cost (buy + sell, delivery), my calculation from broker price lists fetched 2026-11-15:

| Position | AngelOne stock | AngelOne equity ETF | AngelOne GOLDBEES | IBKR US, Fixed | IBKR US, Tiered (approx) |
|---|---|---|---|---|---|
| Rs 10,000 / $107 | Rs 69 = 0.69% | Rs 50 = 0.50% | Rs 49 = 0.49% | $2.00 = 1.87% | $0.72 = 0.67% |
| Rs 20,000 / $213 | Rs 115 = 0.58% | Rs 75 = 0.38% | Rs 75 = 0.38% | $2.00 = 0.94% | $0.72 = 0.34% |
| Rs 30,000 / $319 | Rs 138 = 0.46% | Rs 78 = 0.26% | Rs 78 = 0.26% | $2.01 = 0.63% | $0.73 = 0.23% |
| Rs 40,000 / $425 | Rs 160 = 0.40% | Rs 80 = 0.20% | Rs 80 = 0.20% | $2.01 = 0.47% | $0.73 = 0.17% |

- AngelOne (angelone.in/exchange-transaction-charges, fetched 2026-11-15): brokerage lower of
  Rs 20 or 0.1% per order (min Rs 5); STT 0.1% buy and sell (delivery); NSE 0.0030699%;
  SEBI Rs 10/crore; stamp 0.015% on buy; GST 18% on brokerage + exchange + SEBI; DP charge
  Rs 20 + GST (Rs 23.6) per scrip per sell day; demat AMC Rs 60 + GST a quarter.
- ETF STT: I used 0.001% on sell for equity ETFs and none for gold ETFs. NOT VERIFIED (AngelOne
  shows one STT line for all "stock investments"); stamp duty on ETF buys assumed same as stocks.
- IBKR (interactivebrokers.com/en/pricing/commissions-stocks.php, fetched 2026-11-15): Fixed
  $0.005/share, min $1.00, max 1% of trade value; Tiered $0.0035/share, min $0.35, plus
  exchange/clearing fees ($0.0002/share clearing); SEC fee 0.0000206 x sale value. Tiered
  total of $0.36 a side is my estimate. Which plan applies to his IB India account: NOT VERIFIED.
- IBKR currency conversion: 0.20 basis point (= 0.002%) of value, minimum $2.00 per order
  (commissions-spot-currencies.php, fetched 2026-11-15). So 0.002% is right, but the $2 minimum
  dominates small conversions: convert once, not per trade.
- Spread and slippage are not in the table. Cost vs risk: on a Rs 30,000 stock trade the Rs 138
  cost is 7% of the Rs 2,000 risk; at Rs 10,000 it is 3.5% of risk but 0.69% of value.
