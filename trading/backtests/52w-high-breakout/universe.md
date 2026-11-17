# Full-universe check: 52w-high-breakout

## Summary
- US, 52-week high on 1.5x volume, 2R, 20 days, full universe (679 names): bar fail: PF 2020-2026 1.08 < 1.2.
- India, 52-week high on 1.5x volume, 2R, 20 days, full universe (189 names): bar fail: PF full 1.02 < 1.2; PF 2020-2026 1.04 < 1.2; CAGR -0.5%; max DD -35.4%.
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
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | full | 12416 | 45.4% | 6.4% | -4.7% | 0.37% | 1.15 | 17 | n/a | n/a | n/a | n/a |
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | 2010-2019 | 7254 | 46.7% | 5.4% | -4.0% | 0.39% | 1.18 | 18 | n/a | n/a | n/a | n/a |
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | 2020-2026 | 5162 | 43.6% | 7.9% | -5.5% | 0.35% | 1.11 | 16 | n/a | n/a | n/a | n/a |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | full | 4729 | 42.7% | 8.6% | -6.0% | 0.22% | 1.07 | 16 | n/a | n/a | n/a | n/a |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | 2010-2019 | 1967 | 40.3% | 8.1% | -6.0% | -0.29% | 0.92 | 17 | n/a | n/a | n/a | n/a |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, every signal | 2020-2026 | 2762 | 44.4% | 8.9% | -6.0% | 0.59% | 1.18 | 16 | n/a | n/a | n/a | n/a |

## Rules-sized Rs 2 L run
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | full | 1432 | 47.5% | 7.2% | -5.4% | 0.58% | 1.21 | 18 | 6.9% | -23.2% | 68% | 0.60 |
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | 2010-2019 | 789 | 50.2% | 6.2% | -4.6% | 0.81% | 1.35 | 18 | 9.8% | -17.8% | 71% | 0.86 |
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | 2020-2026 | 643 | 44.2% | 8.5% | -6.2% | 0.29% | 1.08 | 16 | 2.7% | -23.2% | 65% | 0.27 |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | full | 1289 | 42.7% | 8.6% | -6.3% | 0.07% | 1.02 | 17 | -0.5% | -35.4% | 55% | 0.02 |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | 2010-2019 | 681 | 41.7% | 8.6% | -6.1% | 0.01% | 1.00 | 17 | -1.5% | -35.4% | 50% | -0.08 |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days, rules-sized | 2020-2026 | 608 | 43.9% | 8.7% | -6.6% | 0.14% | 1.04 | 16 | 0.8% | -34.3% | 62% | 0.13 |

## Backtest bar (full universe)
| Market | Universe | Version | Bar | Trades by exit | Signals skipped |
|---|---|---|---|---|---|
| US | full universe | 52-week high on 1.5x volume, 2R, 20 days | fail: PF 2020-2026 1.08 < 1.2 | stop 622, time stop 542, target 264, open at end 4 | max_pos 14721, week_limit 1191, price_above_cap 0, cash 0 |
| India | full universe | 52-week high on 1.5x volume, 2R, 20 days | fail: PF full 1.02 < 1.2; PF 2020-2026 1.04 < 1.2; CAGR -0.5%; max DD -35.4% | stop 617, time stop 397, target 270, open at end 5 | max_pos 5229, week_limit 491, price_above_cap 16, cash 0 |

### Worst 5 rules-sized trades: US, 52-week high on 1.5x volume, 2R, 20 days
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| HIMS | 2025-02-20 | 65.08 | 2025-02-21 | 53.51 | stop | -17.9% |
| MSTR | 2021-01-08 | 56.51 | 2021-01-11 | 47.21 | stop | -16.5% |
| GILD | 2012-02-06 | 18.53 | 2012-02-17 | 15.70 | stop | -15.4% |
| DXCM | 2015-08-07 | 23.12 | 2015-08-24 | 19.65 | stop | -15.1% |
| GEN | 2019-07-09 | 12.71 | 2019-07-15 | 10.92 | stop | -14.1% |

### Worst 5 rules-sized trades: India, 52-week high on 1.5x volume, 2R, 20 days
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| COLPAL.NS | 2011-06-30 | 365.35 | 2011-07-28 | 312.22 | stop | -14.9% |
| HINDZINC.NS | 2016-11-02 | 121.51 | 2016-11-09 | 105.07 | stop | -13.9% |
| ADANIENSOL.NS | 2021-09-13 | 1781.00 | 2021-09-22 | 1560.80 | stop | -12.7% |
| NATIONALUM.NS | 2016-12-08 | 39.51 | 2016-12-15 | 34.79 | stop | -12.3% |
| MUTHOOTFIN.NS | 2025-03-20 | 2375.94 | 2025-04-07 | 2106.20 | stop | -11.7% |

### Data: US names with a 1-day move or open gap above 40% (74; not repaired)
Most are real (results, March 2020, biotech news). Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).

AMD 2016-04-22 +52%; APA 2020-03-09 -54%; APP 2024-11-07 +46%; BIIB 2020-11-04 +44%; BE 2019-08-13 -42%, 2020-03-19 +42%; CVNA 2020-03-24 +43%, 2022-08-05 +40%; CNC 2025-07-02 -40%; DHR 2016-07-05 +61%; DXCM 2024-07-26 -41%; FANG 2020-03-09 -45%; ECHO 2025-06-16 +49%, 2025-08-26 +70%; FSLR 2013-04-09 +46%; FISV 2025-10-29 -44%; ILMN 2012-01-25 +46%; MRNA 2026-08-19 +177%; NFLX 2013-01-24 +42%; NCLH 2020-03-24 +42%; OXY 2020-03-09 -52%; PCG 2019-01-14 -52%, 2019-01-24 +75%; RDDT 2024-10-30 +42%; HOOD 2021-08-04 +50%; SMCI 2018-10-04 -41%; TRGP 2020-03-09 -53%; TKO 2014-05-16 -44%; VRTX 2012-05-07 +55%, 2013-04-19 +62%; ALNY 2012-07-16 +53%, 2014-01-13 +41%; ARM 2024-02-08 +48%; CRWV 2025-04-01 +42%; FER 2018-05-29 +42%, 2020-03-13 +43%; NBIS 2025-09-09 +49%; PDD 2022-03-16 +56%; AAL 2020-06-04 +41%; AAON 2026-05-07 +46%; ARMK 2020-03-19 +41%; ARWR 2010-03-22 +93%, 2011-11-10 +40%; BYD 2020-03-19 +43%; CELH 2010-12-23 -40%, 2011-03-07 +50%; CORT 2012-02-21 +47%, 2014-05-07 -50%; CTRE 2014-10-29 +68%, 2020-03-19 +54%; CYTK 2014-04-25 -65%, 2020-10-08 -42%; DOCN 2026-05-05 +40%; DOCS 2026-08-07 +88%; DOCU 2021-12-03 -42%; EAT 2020-03-19 +44%; EXEL 2011-11-01 -40%, 2014-09-02 -55%; FLG 2024-01-31 -43%; FLR 2020-03-19 +76%; GKOS 2018-08-29 +40%; GLPI 2020-03-16 -41%; GME 2020-10-08 +44%, 2021-01-13 +57%; HALO 2012-08-02 -50%; HIMS 2026-03-09 +41%; KD 2026-02-09 -55%; LNTH 2016-08-05 +54%; MP 2025-07-10 +51%; MTDR 2020-03-09 -64%; MTG 2011-08-08 -41%, 2012-08-02 -64%; MUR 2020-03-09 -42%; NBIX 2014-01-07 +90%; OHI 2020-03-19 +50%; OPCH 2016-11-08 -48%; OVV 2020-03-09 -72%; PBF 2020-03-13 +48%; PEGA 2020-03-16 -49%; PFGC 2020-03-16 -43%, 2020-03-19 +59%; PK 2020-11-09 +40%; PR 2020-03-09 -63%, 2020-03-19 +48%; RGEN 2012-04-26 -40%; RMBS 2011-11-16 -61%; SGI 2012-06-06 -49%; SHC 2023-01-10 +100%; SIRI 2023-07-20 +42%; VNOM 2020-03-09 -45%; WAL 2023-03-13 -47%, 2023-05-05 +49%

### Data: India names with a 1-day move or open gap above 40% (7; not repaired)
Most are real (results, March 2020, biotech news). Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).

ADANIENT.NS 2015-06-03 +220%; INDUSINDBK.NS 2020-03-26 +45%; MOTILALOFS.NS 2024-01-01 -75%; PATANJALI.NS 2020-01-27 -95%; PNB.NS 2017-10-25 +46%; TMPV.NS 2025-10-14 -40%; VEDL.NS 2026-04-30 -65%
