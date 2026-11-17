# Full-universe check: short-breakout

## Summary
- US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, full universe (679 names): bar fail: PF full 1.17 < 1.2; PF 2020-2026 1.14 < 1.2; max DD -29.0%.
- US, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, full universe (679 names): bar fail: PF 2020-2026 1.19 < 1.2.
- Full universe = today's included scan names (S&P 500/400, Nasdaq 100; Nifty 200), each with the history it has: still survivorship-biased, but a much bigger sample than the 35-name lists.

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py universe-bar`; every number on this page is printed by that script.

## Universe
| Market | Names used | Dropped (< 300 bars or no data) | List |
|---|---|---|---|
| US | 679 | 5 | [trading/universe/us.csv](../../universe/us.csv) |

Same rules, costs and execution as the 35-name pages; the rules-sized run is the Rs 2 L AGENTS.md simulation. Names listed after 2010 enter when they have 200+ days of data.

## Every signal (one unit each, no capital limit)
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, every signal | full | 68115 | 45.7% | 5.9% | -4.3% | 0.36% | 1.16 | 16 | n/a | n/a | n/a | n/a |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, every signal | 2010-2019 | 38504 | 47.1% | 5.0% | -3.8% | 0.37% | 1.18 | 16 | n/a | n/a | n/a | n/a |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, every signal | 2020-2026 | 29611 | 43.8% | 7.2% | -5.0% | 0.36% | 1.13 | 16 | n/a | n/a | n/a | n/a |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, every signal | full | 74826 | 46.3% | 5.8% | -4.4% | 0.33% | 1.14 | 15 | n/a | n/a | n/a | n/a |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, every signal | 2010-2019 | 41931 | 47.6% | 4.9% | -3.8% | 0.32% | 1.16 | 15 | n/a | n/a | n/a | n/a |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, every signal | 2020-2026 | 32895 | 44.6% | 7.0% | -5.1% | 0.33% | 1.12 | 14 | n/a | n/a | n/a | n/a |

## Rules-sized Rs 2 L run
| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | full | 1796 | 46.7% | 8.1% | -6.1% | 0.54% | 1.17 | 16 | 7.0% | -29.0% | 70% | 0.51 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2010-2019 | 1055 | 49.1% | 6.9% | -5.6% | 0.55% | 1.19 | 16 | 7.7% | -29.0% | 75% | 0.57 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized | 2020-2026 | 741 | 43.2% | 10.0% | -6.7% | 0.54% | 1.14 | 15 | 5.9% | -22.6% | 63% | 0.43 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | full | 1921 | 48.1% | 8.0% | -6.1% | 0.66% | 1.21 | 14 | 9.8% | -24.1% | 68% | 0.70 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2010-2019 | 1101 | 50.0% | 6.8% | -5.5% | 0.62% | 1.23 | 15 | 8.4% | -24.1% | 72% | 0.64 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized | 2020-2026 | 820 | 45.5% | 9.8% | -6.9% | 0.70% | 1.19 | 13 | 11.5% | -19.8% | 61% | 0.77 |

## Backtest bar (full universe)
| Market | Universe | Version | Bar | Trades by exit | Signals skipped |
|---|---|---|---|---|---|
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop | fail: PF full 1.17 < 1.2; PF 2020-2026 1.14 < 1.2; max DD -29.0% | time stop 925, stop 673, exit rule 195, open at end 3 | max_pos 191042, week_limit 9315, price_above_cap 2, cash 0 |
| US | full universe | Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop | fail: PF 2020-2026 1.19 < 1.2 | time stop 730, stop 704, target 299, exit rule 183, open at end 5 | max_pos 181545, week_limit 18973, price_above_cap 0, cash 0 |

### Worst 5 rules-sized trades: US, Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BIIB | 2020-11-05 | 348.00 | 2020-11-09 | 230.82 | stop | -33.7% |
| NFLX | 2012-07-06 | 1.20 | 2012-07-25 | 0.92 | stop | -23.4% |
| GME | 2025-05-23 | 30.60 | 2025-06-12 | 23.57 | exit rule | -23.1% |
| GAP | 2025-05-23 | 27.38 | 2025-05-30 | 21.86 | stop | -20.2% |
| VTR | 2015-07-28 | 46.87 | 2015-08-18 | 37.49 | time stop | -20.1% |

### Worst 5 rules-sized trades: US, Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop
| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |
|---|---|---|---|---|---|---|
| BIIB | 2020-11-05 | 348.00 | 2020-11-09 | 230.82 | stop | -33.7% |
| NFLX | 2012-07-06 | 1.20 | 2012-07-25 | 0.92 | stop | -23.4% |
| ADBE | 2010-09-10 | 32.56 | 2010-09-22 | 25.89 | stop | -20.6% |
| VTR | 2015-07-28 | 46.87 | 2015-08-18 | 37.49 | time stop | -20.1% |
| COIN | 2023-03-20 | 76.76 | 2023-03-23 | 61.85 | stop | -19.5% |

### Data: US names with a 1-day move or open gap above 40% (74; not repaired)
Most are real (results, March 2020, biotech news). Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).

AMD 2016-04-22 +52%; APA 2020-03-09 -54%; APP 2024-11-07 +46%; BIIB 2020-11-04 +44%; BE 2019-08-13 -42%, 2020-03-19 +42%; CVNA 2020-03-24 +43%, 2022-08-05 +40%; CNC 2025-07-02 -40%; DHR 2016-07-05 +61%; DXCM 2024-07-26 -41%; FANG 2020-03-09 -45%; ECHO 2025-06-16 +49%, 2025-08-26 +70%; FSLR 2013-04-09 +46%; FISV 2025-10-29 -44%; ILMN 2012-01-25 +46%; MRNA 2026-08-19 +177%; NFLX 2013-01-24 +42%; NCLH 2020-03-24 +42%; OXY 2020-03-09 -52%; PCG 2019-01-14 -52%, 2019-01-24 +75%; RDDT 2024-10-30 +42%; HOOD 2021-08-04 +50%; SMCI 2018-10-04 -41%; TRGP 2020-03-09 -53%; TKO 2014-05-16 -44%; VRTX 2012-05-07 +55%, 2013-04-19 +62%; ALNY 2012-07-16 +53%, 2014-01-13 +41%; ARM 2024-02-08 +48%; CRWV 2025-04-01 +42%; FER 2018-05-29 +42%, 2020-03-13 +43%; NBIS 2025-09-09 +49%; PDD 2022-03-16 +56%; AAL 2020-06-04 +41%; AAON 2026-05-07 +46%; ARMK 2020-03-19 +41%; ARWR 2010-03-22 +93%, 2011-11-10 +40%; BYD 2020-03-19 +43%; CELH 2010-12-23 -40%, 2011-03-07 +50%; CORT 2012-02-21 +47%, 2014-05-07 -50%; CTRE 2014-10-29 +68%, 2020-03-19 +54%; CYTK 2014-04-25 -65%, 2020-10-08 -42%; DOCN 2026-05-05 +40%; DOCS 2026-08-07 +88%; DOCU 2021-12-03 -42%; EAT 2020-03-19 +44%; EXEL 2011-11-01 -40%, 2014-09-02 -55%; FLG 2024-01-31 -43%; FLR 2020-03-19 +76%; GKOS 2018-08-29 +40%; GLPI 2020-03-16 -41%; GME 2020-10-08 +44%, 2021-01-13 +57%; HALO 2012-08-02 -50%; HIMS 2026-03-09 +41%; KD 2026-02-09 -55%; LNTH 2016-08-05 +54%; MP 2025-07-10 +51%; MTDR 2020-03-09 -64%; MTG 2011-08-08 -41%, 2012-08-02 -64%; MUR 2020-03-09 -42%; NBIX 2014-01-07 +90%; OHI 2020-03-19 +50%; OPCH 2016-11-08 -48%; OVV 2020-03-09 -72%; PBF 2020-03-13 +48%; PEGA 2020-03-16 -49%; PFGC 2020-03-16 -43%, 2020-03-19 +59%; PK 2020-11-09 +40%; PR 2020-03-09 -63%, 2020-03-19 +48%; RGEN 2012-04-26 -40%; RMBS 2011-11-16 -61%; SGI 2012-06-06 -49%; SHC 2023-01-10 +100%; SIRI 2023-07-20 +42%; VNOM 2020-03-09 -45%; WAL 2023-03-13 -47%, 2023-05-05 +49%
