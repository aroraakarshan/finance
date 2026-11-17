# Cash abroad and currencies (USD, EUR, GBP, SGD vs INR)

Market research, not advice. Written 2026-11-15.

## Summary
- Idle foreign cash must be reinvested or brought back within 180 days (LRS FAQ Q4); FX trading, forex margin and binary options are not allowed (Q2).
- IBKR Pro pays USD 3.38% only above $10k (13 Nov 2026); IB01 (T-bills, about 4.32%) pays more, from the first dollar, and the Acc line defers tax.
- The rupee weakened about 3.5% a year against the dollar over 10 years (USD/INR rose) and the 12-month forward premium is 4.38% (Oct 2026): USD cash earns about 7-8.7% in INR before 35.88% tax.
- What to do: park USD waiting to be invested in IB01, not idle cash; skip EUR/GBP/SGD cash unless buying assets in those currencies. The user is already 81% USD, so more USD adds little hedge.

Indian cash options (FDs, liquid funds, RBI
bonds) and US T-bill/MMF detail: [opp-fixed-income-cash](../themes/opp-fixed-income-cash.md).
IBKR account rules: [ibkr-global](../themes/ibkr-global.md): [rules](../themes/ibkr-global/rules.md) section 1, [cash and bonds](../themes/ibkr-global/cash-and-bonds.md) 3.4, 3.5.

## 1. Rules for an Indian resident (RBI)

- LRS FAQ Q4 (updated 6 Apr 2023), exact text: "The investor who has remitted funds under LRS can
  retain and reinvest the income earned from his investments made under the Scheme. However, the
  received/realised/unspent/unused foreign exchange, unless reinvested, shall be repatriated and
  surrendered to an authorised person within a period of 180 days from the date of such receipt/
  realisation/purchase/acquisition or date of return to India, as the case may be." [RBI-FAQ]
  - So: the clock is 180 days from when the cash arrives (remittance, sale proceeds, dividends).
    Idle cash must be reinvested (e.g. into a listed ETF) or brought back. Whether a money-market
    ETF counts as "reinvested" is not stated (reading: a listed fund is an investment - not verified).
- Q23: no prior approval needed to open and hold a foreign currency bank account abroad under
  LRS [RBI-FAQ]. Q13: remittance can be in any freely convertible currency [RBI-FAQ].
- NOT allowed (FAQ Q2) [RBI-FAQ]: "Remittance for trading in foreign exchange abroad";
  "Remittance from India for margins or margin calls to overseas exchanges / overseas
  counterparty". So: no FX trading or speculation at IBKR, no forex/CFD margin accounts, no
  binary options. Converting USD to EUR to buy a EUR-listed ETF is a normal investment step;
  repeated round trips for profit would be FX trading (reading, not RBI text).
- RBI Alert List of unauthorised forex platforms: latest update found 19 Nov 2025, 7 added,
  95 entities in total (e.g. Starnet FX, CapPlace, Mirrox, Trive, NXG Markets, NordFX); RBI says
  the list is not exhaustive [BL]. No 2026 update found in news (RBI page itself not reached).
- RBI Oct 2026 FX measures: limit for FX derivatives without underlying exposure cut from
  $100 m to $5 m; new 20% reserve (FERR) on bank FX derivative contracts above $2 m [MC]. These
  are for companies/banks, but show RBI is actively defending the rupee.

## 2. Where idle foreign cash can earn (rates as of 13 Nov 2026 unless noted)

| Option | Currency | Yield now | Notes |
|---|---|---|---|
| IBKR cash, Pro | USD | 3.38% above $10k (BM 3.88% - 0.5%) | Full rate only if NAV > $100k; Lite 2.38% [IB] |
| IBKR cash, Pro | EUR | 1.985% above EUR 10k | Lite 0.985% [IB] |
| IBKR cash, Pro | GBP | 3.475% above GBP 8k | Lite 2.475% [IB] |
| IBKR cash, Pro | SGD | 0.668% above SGD 14k (BM - 1%) | Lite 0% [IB] |
| IBKR cash | INR | 0% | [IB] |
| IB01 iShares USD Treasury 0-1yr (Acc), IE00BGSF1X88 | USD | ~T-bill rate: 3m bill 4.32% (12 Nov) [F] | TER 0.07%, EUR 18,560 m [J]; 1y return +3.7% USD [Y] |
| ERND iShares USD Ultrashort Bond (Dist), IE00BCRY6227 | USD | not verified | TER 0.09%, EUR 587 m [J] |
| XEON Xtrackers EUR Overnight Rate Swap 1C, LU0290358497 | EUR | ~EUR STR 2.44% (12 Nov) [F] | Swap-based; TER 0.10%, EUR 23,573 m [J]; 1y +2.1% EUR [Y] |
| CSH2 Amundi Smart Overnight Return (Acc), LU1190417599 | EUR | ~EUR STR | TER 0.10%, EUR 7,369 m [J] |
| ERNE iShares EUR Ultrashort Bond (Dist), IE00BCRY6557 | EUR | not verified | TER 0.09%, EUR 3,390 m [J] |
| GBP ultrashort (ERNS) | GBP | SONIA 3.98% (11 Nov) [F] | ISIN not verified |
| DBS SGD fixed deposit | SGD | not verified (rates page needs JavaScript) | Non-resident account opening: not verified [DBS] |

- Fed funds 3.88% (12 Nov 2026) vs 3m T-bill 4.32%: bills pay about 0.9 points more than IBKR
  Pro USD cash, and all of the first $10k [F][IB].
- US money-market funds: US-situs, 25% US withholding, probably always-ST; skip (see ibkr-global/cash-and-bonds.md 3.4).

Tax (one line each, tax/investment-types.md): IBKR interest at slab 35.88%, taxed yearly;
money-market/ultrashort UCITS: AF s.76 may make gains always short-term (35.88%), but an Acc ETF
defers tax until sale; distributing lines pay at slab every year; IB01 is Irish (not US-situs).

## 3. Currency views vs INR

| Currency vs INR | Now | 1y change | 5y %/yr | 10y %/yr | 20y %/yr |
|---|---|---|---|---|---|
| USD | 93.91 (6 Nov) [F]; 94.24 (14 Nov) [Y] | +5.9% | +4.8% | +3.5% | +3.8% |
| EUR | 104.75 | +2.4% | +4.1% | +3.5% | +3.1% |
| GBP | 125.57 | +8.1% | +4.6% | +4.1% | +2.0% |
| SGD | 73.25 | +7.8% | +5.9% | +4.3% | +4.8% |
| JPY (per 100) | 59.35 | +2.4% | -1.9% | -0.9% | +2.3% |

Cross rates built from FRED dollar rates on 6 Nov 2026 [F]. Positive = foreign currency rose vs INR.

- 2026 path (Yahoo): USD/INR 89.96 at 1 Jan, record 96.88 on 23 Jul, 94.24 on 14 Nov [Y]. 1y
  forward hit 100 in May 2026 with spot 96.8 [TOI headline]. Axis Bank flags 100 by June 2027 risk
  [FE headline, 12 Nov 2026; body not read].
- Forward premium: 12-month USD/INR premium 4.38% at end Oct 2026 (3.36% end Sep); near-month
  8-8.5% annualised in Oct after RBI measures [MC]. FBIL reference rate: not checked.
- Reading: the forward premium (about 4.4%) is the market's price for the INR fall, roughly the
  rate gap India vs US. Past INR fall vs USD was 3.5-4.8%/yr (10y-5y). Holding USD cash at 3.4-4.3%
  plus ~3.5-4.4% INR fall gives about 7-8.7% in INR before tax, close to an Indian deposit; the
  gain is only the INR move, which is not guaranteed (INR rose about 1% in Oct 2026 [TradingView
  headline]).
- JPM 2027 LTCMA and Vanguard both expect slow USD depreciation vs other major currencies
  [JPM][V]: EUR/GBP cash could gain vs USD, but they pay less (EUR 1.985% at IBKR).

### Why USD assets are partly an INR hedge

- India imports oil and runs a current-account deficit; when oil or global risk spikes, INR falls
  and USD assets rise in INR value (USD/INR record 96.88 in Jul 2026 [Y]).
- The user already has 81% in QCOM+MSFT (USD). The INR hedge is already large; more USD cash adds
  little diversification. The concentration problem is the stocks, not the currency
  ([employer-stock-concentration](../themes/employer-stock-concentration.md)).

## 4. Risks

- Rule risk: 180-day repatriation; FX trading/margin ban; RBI can tighten LRS when INR is weak.
- Tax drag: every cash yield is taxed at 35.88%; FX gains on cash are also taxable (treatment of
  currency gain on a foreign bank balance not verified - CA).
- IBKR: first $10k (USD) earns 0%; NAV under $100k cuts the rate [ibkr-global/cash-and-bonds.md 3.5].

## 5. Verdict (conditional; the user decides)

| Need | Best instrument | Verdict |
|---|---|---|
| USD waiting to be invested (< 180 days) | IBKR cash if > $10k; else IB01 | Use IB01 for amounts held > 1 month (higher yield, Acc defers tax) |
| Long-term USD cash pile | IB01 | Neutral: beats IBKR cash, but equity UCITS taxed at 14.95% after 24 m win post-tax |
| EUR/GBP cash | XEON / CSH2 (EUR) | Skip unless buying EUR/GBP assets soon; lower rates, extra FX cost |
| SGD fixed deposit | DBS | Skip: not verified for non-residents; IBKR SGD 0.67% is low |
| FX trading, forex margin, binary options, Alert List platforms | - | NOT allowed (LRS Q2) |

## Sources (read 2026-11-15)

- [RBI-FAQ] LRS FAQ (updated 6 Apr 2023): https://www.rbi.org.in/commonman/English/Scripts/FAQs.aspx?Id=1834
- [BL] BusinessLine 19 Nov 2025: https://www.thehindubusinessline.com/money-and-banking/rbi-adds-seven-entities-to-its-alert-list-of-unauthorised-forex-trading-platforms/article70299766.ece
- [MC] Moneycontrol 11 Nov 2026: https://www.moneycontrol.com/news/business/banks/high-forward-costs-force-importers-to-concentrate-on-dollar-hedges-14076886.html
- [IB] IBKR interest rates (rates as of 13 Nov 2026): https://www.interactivebrokers.com/en/accounts/fees/pricing-interest-rates.php
- [F] FRED: DFF, DGS3MO, ECBESTRVOLWGTTRMDMNRT, IUDSOIA, DEXINUS, DEXUSEU, DEXUSUK, DEXSIUS, DEXJPUS
- [J] justETF profiles by ISIN; [Y] Yahoo via yfinance (IB01.L, XEON.DE, INR=X)
- [DBS] https://www.dbs.com.sg/personal/rates-online/singapore-dollar-fixed-deposits.page (rates JavaScript-only)
- [JPM] [V]: see [bonds-global](bonds-global.md) sources. Headlines only (Google News RSS): TOI 21 May
  2026, Financial Express 12 Nov 2026, TradingView 5 Nov 2026.
