# Consumer discretionary: markets and valuation

Part of [consumer discretionary](README.md). Tags: [sources](sources.md).

## Summary

- Last year discretionary lagged the wider market almost everywhere, except Indian autos and Japanese autos.
- India autos: P/E 31.0, right at the 10-year median; US discretionary: forward P/E 24.3, well above its 25-year average 20.3.
- Europe luxury and autos are the beaten-down corner; China consumer the worst over 5 years.
- XDWC is real, Irish, accumulating, TER 0.25%, EUR 394 m; but Amazon 31.6% + Tesla 13.6% of it.

## 1. Mood and recent returns by region

Price returns in local currency to 13 Nov 2026 from yfinance adjusted closes [D1] (indices `^` exclude
dividends; ETFs include them). 3y/5y are totals, not per year.

| Region | Measure (ticker) | 1y | 3y | 5y | Market for comparison (1y / 3y / 5y) |
|---|---|---|---|---|---|
| India | Nifty Auto (^CNXAUTO) | +2.0% | +70.7% | +138.6% | Nifty 50: -2.8% / +29.3% / +38.9% |
| India | Nifty India Consumption (^CNXCONSUM) | -3.2% | +39.4% | +63.5% | same |
| India | Nippon Nifty Auto ETF (AUTOBEES) | +2.7% | +73.6% | n/a (listed Jan 2022) | same |
| US | Consumer Discretionary SPDR (XLY) | +4.3% | +51.8% | +22.8% | S&P 500: +12.2% / +71.4% / +61.5% |
| World | Xtrackers MSCI World Cons. Disc. (XDWC.DE, EUR) | +6.5% | +39.9% | +20.6% | MSCI World (URTH, USD): +13.3% / +74.2% / +62.7% |
| Europe | iShares STOXX 600 Autos & Parts (EXV5.DE) | -16.2% | -17.2% | -24.1% | - |
| Europe | iShares STOXX 600 Personal & Household Goods (EXH7.DE; luxury plus consumer brands) | -1.6% | +12.1% | +4.4% | - |
| Japan | NEXT FUNDS TOPIX-17 Autos (1622.T) | +8.9% | +30.6% | +73.7% | Nikkei 225: +19.2% / +87.6% / +106.5% |
| Other Asia | Global X MSCI China Cons. Disc. (CHIQ, US-listed, reference only) | -29.6% | -5.3% | -44.4% | Hang Seng: -12.7% / +35.6% / -6.7% |

justETF shows the same XDWC figures (1y +6.79%, 3y +39.71%, 5y +20.53%) [D4]: the yfinance data check out.

Mood in one line per region:
- India: volumes at records after the GST cut (Oct 2026 PV 5,19,060, two-wheelers 25,77,810) [D10], but
  carmaker profits squeezed by commodity costs linked to the West Asia war (Maruti Q2 profit -26%) [D12].
- US: earnings strong for Amazon, but the sector trails the S&P 500 by 8 points over the year [D1].
- Europe: luxury hit by China (LVMH Q3 organic +1%, fashion and leather -5%) [D23]; autos hit by
  Chinese competition and tariffs (not checked in detail).
- Japan: Toyota raised its full-year forecast on a weak yen (about 158 per USD) [D15].
- China: EV price war; BYD Jan-Oct sales -2.2% year on year [D17].

## 2. Valuation vs history

| Measure | Now | Own history | vs the market | Source |
|---|---|---|---|---|
| Nifty Auto trailing P/E | 31.0 (13 Nov 2026) | 10y median 31.2; 10y mean 54.7 (pushed up by the 2020-22 profit slump) | Nifty 50 P/E 20.5 (10y median 23.2); auto premium 1.51x vs 1.34x on 10y medians | [D2] |
| Nifty Auto P/B (price / book value) | 4.36 | 5.65 in Nov 2016 (full 10y average not pulled) | Nifty 50 P/B 3.08 | [D2] |
| S&P 500 Cons. Disc. forward 12-month P/E | 24.3 (5 Nov 2026) | 25-year average 20.3 (10-year average not given in the free post) | S&P 500 17.7 (10y avg 19.1) | [D3] |
| XLY (US-listed) P/E | 27.3 trailing, 24.4 forward (13 Nov 2026) | - | - | [D5] |
| XDWC P/E | 23.1 trailing (Yahoo, not verified) | MSCI factsheet not found | - | [D1] |
| LVMH P/E (luxury proxy) | 18.4 trailing, 17.2 forward | 24.1-30.4 at year ends 2021-2025 | - | [D6] |
| Toyota P/E (Japan autos proxy) | 9.3 trailing | not pulled | - | [D1] |
| BYD P/E (China EV proxy) | 16.0 trailing, 11.9 forward | not pulled | - | [D7] |

Read: India autos fairly priced on their own history but at a bigger premium to the Nifty than usual;
US discretionary is expensive; European luxury is cheap vs its own history (because profits are falling:
LVMH net income EUR 10.9 bn in 2025 vs 15.2 bn in 2023 [D1]).

## 3. Global ETF check: XDWC (verified)

| Item | Value [D4], justETF, holdings as of 29 Sep 2026 |
|---|---|
| Name, ISIN | Xtrackers MSCI World Consumer Discretionary UCITS ETF 1C, IE00BM67HP23 |
| Domicile, type | Ireland, accumulating, physical full replication |
| TER, size | 0.25%, EUR 394 m (oldest and largest on this index); launched 14 Mar 2016 |
| Listings | LSE XDWC (USD) and XWDS (GBP); XETRA XDWC (EUR); Borsa Italiana; SIX |
| Top holdings | Amazon 31.61%, Tesla 13.56%, Home Depot 3.84%, Toyota 2.39%, McDonald's 2.20% |
| Countries | US 74.6%, Japan 10.2%, France 3.0%, Switzerland 2.3% |
| Risk | 5y max fall -33.5%; volatility 20.4% (5y) |
| Alternative | SPDR MSCI World Consumer Discretionary (IE00BYTRR640): TER 0.30%, EUR 63 m [D4] |

Concern: 45% in two US mega caps, one of them a cloud/AI company. For someone already heavy in US
tech, XDWC adds less spread than its name suggests; correlation with QCOM/MSFT not computed.

## 4. Indian auto ETFs and index funds

All track the Nifty Auto index (15 large auto and auto-parts stocks). NAV date 13 Nov 2026 [D8];
TER from Groww [D9].

| Fund | Type, NSE symbol | ISIN | TER | Note |
|---|---|---|---|---|
| Nippon India Nifty Auto ETF | ETF, AUTOBEES | INF204KC1337 | 0.24% | Oldest (Jan 2022), 3y +73.6% [D1] |
| ICICI Prudential Nifty Auto ETF | ETF, AUTOIETF | INF109KC10V2 | 0.22% | Listed on Yahoo from Feb 2025 [D1] |
| ICICI Prudential Nifty Auto Index Fund (Direct) | Index fund | INF109KC16J4 | 0.36% | AUM Rs 230.8 cr |
| Nippon India Nifty Auto Index Fund (Direct) | Index fund | INF204KC1EE8 | 0.52% | AUM Rs 45.2 cr, small |
| Tata / HDFC Nifty Auto Index Fund (Direct) | Index fund | INF277KA1AU6 / INF179KC1KQ0 | not pulled | - |
| Nifty EV & New Age Automotive ETFs (ICICI EVIETF, Mirae, Groww) | ETF | INF109K1A153 etc. | not pulled | Different index (EV, batteries, parts); EVIETF only since Jul 2026 on Yahoo |

ETF beats index fund on cost; buy with a limit order and check the price is near NAV. Trading
volume of AUTOBEES not checked.
