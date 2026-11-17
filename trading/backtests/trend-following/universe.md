# Full-universe check: trend-following

## Summary
- US, Donchian 50/20, rules stop, full universe (679 names): bar fail: max DD -35.2%.
- India, Donchian 50/20, rules stop, full universe (189 names): bar fail: max DD -47.7%.
- Full universe = today's included scan names (S&P 500/400, Nasdaq 100; Nifty 200), each with the history it has: still survivorship-biased, but a much bigger sample than the 35-name lists.

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py universe-bar`; every number on this page is printed by that script.

## Universe
| Market | Names used | Dropped (< 300 bars or no data) | List |
|---|---|---|---|
| US | 679 | 5 | [trading/universe/us.csv](../../universe/us.csv) |
| India | 189 | 8 | [trading/universe/india.csv](../../universe/india.csv) |

Same rules, costs and execution as the 35-name pages; the rules-sized run is the Rs 2 L AGENTS.md simulation. Names listed after 2010 enter when they have 200+ days of data.

## Every signal (one unit each, no capital limit)
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | full universe | Donchian 50/20, rules stop, every signal | full | 26356 | 33.1% | 15.0% | -4.8% | 1.77% | 1.55 | 50 | n/a | n/a | n/a | n/a |
| US | full universe | Donchian 50/20, rules stop, every signal | 2010-2019 | 14532 | 34.5% | 12.5% | -4.3% | 1.51% | 1.54 | 54 | n/a | n/a | n/a | n/a |
| US | full universe | Donchian 50/20, rules stop, every signal | 2020-2026 | 11824 | 31.3% | 18.5% | -5.4% | 2.10% | 1.57 | 46 | n/a | n/a | n/a | n/a |
| India | full universe | Donchian 50/20, rules stop, every signal | full | 6078 | 32.0% | 23.8% | -5.9% | 3.59% | 1.90 | 54 | n/a | n/a | n/a | n/a |
| India | full universe | Donchian 50/20, rules stop, every signal | 2010-2019 | 3073 | 29.8% | 20.7% | -6.0% | 1.98% | 1.47 | 54 | n/a | n/a | n/a | n/a |
| India | full universe | Donchian 50/20, rules stop, every signal | 2020-2026 | 3005 | 34.1% | 26.5% | -5.8% | 5.23% | 2.38 | 53 | n/a | n/a | n/a | n/a |

## Rules-sized Rs 2 L run
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | full universe | Donchian 50/20, rules stop, rules-sized | full | 590 | 34.1% | 18.3% | -6.0% | 2.26% | 1.57 | 50 | 10.4% | -35.2% | 81% | 0.62 |
| US | full universe | Donchian 50/20, rules stop, rules-sized | 2010-2019 | 324 | 36.7% | 15.8% | -5.1% | 2.54% | 1.78 | 54 | 11.5% | -25.3% | 84% | 0.70 |
| US | full universe | Donchian 50/20, rules stop, rules-sized | 2020-2026 | 266 | 30.8% | 22.0% | -7.0% | 1.93% | 1.40 | 44 | 8.7% | -35.2% | 76% | 0.52 |
| India | full universe | Donchian 50/20, rules stop, rules-sized | full | 583 | 28.1% | 24.3% | -6.3% | 2.30% | 1.51 | 49 | 7.0% | -47.7% | 79% | 0.49 |
| India | full universe | Donchian 50/20, rules stop, rules-sized | 2010-2019 | 362 | 25.4% | 20.7% | -6.3% | 0.58% | 1.12 | 47 | 0.2% | -47.7% | 79% | 0.10 |
| India | full universe | Donchian 50/20, rules stop, rules-sized | 2020-2026 | 221 | 32.6% | 29.0% | -6.4% | 5.13% | 2.19 | 53 | 17.4% | -31.5% | 80% | 1.00 |

## Backtest bar (full universe)
| Market | Universe | Version | Bar | Trades by exit | Signals skipped |
|---|---|---|---|---|---|
| US | full universe | Donchian 50/20, rules stop | fail: max DD -35.2% | stop 315, exit rule 270, open at end 5 | max_pos 135851, week_limit 462, price_above_cap 0, cash 0 |
| India | full universe | Donchian 50/20, rules stop | fail: max DD -47.7% | stop 352, exit rule 226, open at end 5 | max_pos 24388, week_limit 71, price_above_cap 4, cash 0 |

### Worst 5 rules-sized trades: US, Donchian 50/20, rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| COHR | 2023-06-15 | 48.58 | 2023-08-16 | 35.74 | stop | -26.5% |
| CDE | 2026-01-23 | 25.82 | 2026-01-30 | 21.52 | stop | -16.8% |
| CYTK | 2022-06-24 | 47.98 | 2022-06-30 | 40.49 | stop | -15.7% |
| UNH | 2025-04-09 | 538.37 | 2025-04-17 | 463.22 | stop | -14.0% |
| HIMS | 2021-02-01 | 19.30 | 2021-02-23 | 16.72 | stop | -13.5% |

### Worst 5 rules-sized trades: India, Donchian 50/20, rules stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BSE.NS | 2024-04-24 | 1068.17 | 2024-04-29 | 899.28 | stop | -16.2% |
| GMRAIRPORT.NS | 2012-01-16 | 25.40 | 2012-02-08 | 22.00 | stop | -13.8% |
| BRITANNIA.NS | 2011-06-06 | 181.12 | 2011-09-09 | 159.68 | stop | -12.2% |
| INDIGO.NS | 2020-11-11 | 1609.33 | 2020-12-22 | 1422.60 | stop | -12.0% |
| HINDALCO.NS | 2016-11-08 | 159.71 | 2016-11-09 | 141.58 | stop | -11.7% |

### Data: US names with a 1-day move or open gap above 40% (74; not repaired)
Most are real (results, March 2020, biotech news). Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).

AMD 2016-04-22 +52%; APA 2020-03-09 -54%; APP 2024-11-07 +46%; BIIB 2020-11-04 +44%; BE 2019-08-13 -42%, 2020-03-19 +42%; CVNA 2020-03-24 +43%, 2022-08-05 +40%; CNC 2025-07-02 -40%; DHR 2016-07-05 +61%; DXCM 2024-07-26 -41%; FANG 2020-03-09 -45%; ECHO 2025-06-16 +49%, 2025-08-26 +70%; FSLR 2013-04-09 +46%; FISV 2025-10-29 -44%; ILMN 2012-01-25 +46%; MRNA 2026-08-19 +177%; NFLX 2013-01-24 +42%; NCLH 2020-03-24 +42%; OXY 2020-03-09 -52%; PCG 2019-01-14 -52%, 2019-01-24 +75%; RDDT 2024-10-30 +42%; HOOD 2021-08-04 +50%; SMCI 2018-10-04 -41%; TRGP 2020-03-09 -53%; TKO 2014-05-16 -44%; VRTX 2012-05-07 +55%, 2013-04-19 +62%; ALNY 2012-07-16 +53%, 2014-01-13 +41%; ARM 2024-02-08 +48%; CRWV 2025-04-01 +42%; FER 2018-05-29 +42%, 2020-03-13 +43%; NBIS 2025-09-09 +49%; PDD 2022-03-16 +56%; AAL 2020-06-04 +41%; AAON 2026-05-07 +46%; ARMK 2020-03-19 +41%; ARWR 2010-03-22 +93%, 2011-11-10 +40%; BYD 2020-03-19 +43%; CELH 2010-12-23 -40%, 2011-03-07 +50%; CORT 2012-02-21 +47%, 2014-05-07 -50%; CTRE 2014-10-29 +68%, 2020-03-19 +54%; CYTK 2014-04-25 -65%, 2020-10-08 -42%; DOCN 2026-05-05 +40%; DOCS 2026-08-07 +88%; DOCU 2021-12-03 -42%; EAT 2020-03-19 +44%; EXEL 2011-11-01 -40%, 2014-09-02 -55%; FLG 2024-01-31 -43%; FLR 2020-03-19 +76%; GKOS 2018-08-29 +40%; GLPI 2020-03-16 -41%; GME 2020-10-08 +44%, 2021-01-13 +57%; HALO 2012-08-02 -50%; HIMS 2026-03-09 +41%; KD 2026-02-09 -55%; LNTH 2016-08-05 +54%; MP 2025-07-10 +51%; MTDR 2020-03-09 -64%; MTG 2011-08-08 -41%, 2012-08-02 -64%; MUR 2020-03-09 -42%; NBIX 2014-01-07 +90%; OHI 2020-03-19 +50%; OPCH 2016-11-08 -48%; OVV 2020-03-09 -72%; PBF 2020-03-13 +48%; PEGA 2020-03-16 -49%; PFGC 2020-03-16 -43%, 2020-03-19 +59%; PK 2020-11-09 +40%; PR 2020-03-09 -63%, 2020-03-19 +48%; RGEN 2012-04-26 -40%; RMBS 2011-11-16 -61%; SGI 2012-06-06 -49%; SHC 2023-01-10 +100%; SIRI 2023-07-20 +42%; VNOM 2020-03-09 -45%; WAL 2023-03-13 -47%, 2023-05-05 +49%

### Data: India names with a 1-day move or open gap above 40% (7; not repaired)
Most are real (results, March 2020, biotech news). Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).

ADANIENT.NS 2015-06-03 +220%; INDUSINDBK.NS 2020-03-26 +45%; MOTILALOFS.NS 2024-01-01 -75%; PATANJALI.NS 2020-01-27 -95%; PNB.NS 2017-10-25 +46%; TMPV.NS 2025-10-14 -40%; VEDL.NS 2026-04-30 -65%
