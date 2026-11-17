# Buy list: method

## Summary
- How `scout/buy-list.md` is ranked: four checks (diversification, valuation, momentum and market mood, research), 0-2 points each, equal weights; only ideas beyond `portfolio/plan.md` are ranked.
- Scores per item, the price data used, and how the scout correlation differs from research.
- Back to the [buy list](../buy-list.md).

## Checks
Four checks, 0-2 points each, equal weights: `journal/signals.md` has no closed trades and no scores
yet (2026-11-15). Ties: more diversification first, then the research score, then funds before stocks,
then the lower correlation.

What is ranked: only ideas beyond `portfolio/plan.md` (the 9-fund split, SIPs and gold are your decisions; PPF declined 2026-11-16;
they are scored below only as a check). No count limit on single stocks: plan.md and `portfolio/targets.md` set
none; the bands decide (each single stock at most 10%; class bands in the buy list's band check). Size and funding: the rule in `portfolio/targets.md` "Money for new ideas" (ecab32c: 1% per idea including funds, 5% in all), applied in the buy list's "Money and timing". 

| Check | 2 points | 1 point | 0 points |
|---|---|---|---|
| Diversification away from QCOM/MSFT/semis | Corr below 0.4, not US-situs and not tech | One of these fails (e.g. US companies, tech, tech tenants) | Two fail |
| Valuation (research notes) | Cheap vs own history or peers | Fair; cheap only on peak profits; or up to 20% above own history | More than 20% above own history |
| Momentum and market mood | Price over 5% above its 200-day average | Within 5% of it, or no price | Over 5% below; or news -1/-2 on the stock. Market brief: rate-sensitive items lose 1 point while "Fed and rates" is -2 |
| Research verdict | Research core buy (README s3, or a sector note's core fund/ETF in a sector the cross-sector ranking rates attractive) | Single stocks; "small", "in steps" or neutral; or a sector rated avoid overall but neutral in that market | Watch, wait for a lower price, small only, avoid in that market, or "do not add" for this user (tech) |

Market brief used: `news/market/2026-11-15.md` (finance-news, week to 13 Nov 2026): Fed and rates -2 (December
Fed hike priced, US 10y 5.15%), semis -1, India flows +1 (foreign buying, but CPI 6.09% and an RBI hike expected
4 Dec); yen near 160/$ (intervention risk for Japan names); Stoxx 600 record as money leaves US tech. Effect:
REITs 6 -> 5 (out of the list, to Watch), XDWU 5 -> 4, HPRA 5 -> 4. No other score changed.

| Rank | Item | Diversification | Valuation | Momentum | Research | Total |
|---|---|---|---|---|---|---|
| 1 | BANKBEES | 2 (corr 0.04) | 2 (P/B 1.84 vs 10-yr avg 2.61) | 2 (+7.7%) | 2 (India private banks: attractive) | 8 |
| 2 | XDWF | 2 (corr 0.17) | 1 (US fin fwd 15.1 vs 12.9, +17%) | 2 (+6.6%) | 2 (financials: attractive) | 7 |
| 3 | FMCGIETF | 2 (corr 0.11) | 2 (P/E 32.9 vs median 41.9) | 1 (-3.1%) | 2 (India FMCG: attractive) | 7 |
| 4 | 7203 Toyota | 2 (corr -0.22) | 2 (P/E 9.3) | 2 (+10.6%) | 1 (single stock; Japan autos attractive) | 7 |
| 5 | MUV2 Munich Re | 2 (corr -0.15) | 2 (P/E 11.3, ROE 20%) | 2 (+15.8%) | 1 (single stock; Europe insurers attractive) | 7 |
| 6 | STARHEALTH | 2 (corr 0.22) | 2 (P/E 32.0 vs median 39.4) | 2 (+8.6%) | 1 (buy small) | 7 |
| 7 | 8031 Mitsui | 2 (corr -0.22) | 2 (fwd 13.5) | 1 (-1.8%) | 1 | 6 |
| 8 | ULVR Unilever | 2 (corr -0.19) | 1 (fwd 17.7-20.4) | 2 (+7.2%) | 1 | 6 |
| 9 | NH | 2 (corr -0.13) | 2 (EV/EBITDA 20.5 vs 22.8) | 1 (+1.4%) | 1 (buy small) | 6 |
| 10 | 9433 KDDI | 2 (corr -0.09) | 2 (fwd 13.7) | 1 (+4.4%) | 1 | 6 |
| 11 | BPCL | 2 (corr 0.01) | 2 (P/E 9.3, FY28 7.5) | 1 (-4.0%) | 1 (oil-fall hedge) | 6 |
| 12 | COALINDIA | 2 (corr 0.07) | 2 (P/E 7.45, net cash) | 1 (-2.5%) | 1 | 6 |
| 13 | LT | 2 (corr 0.17) | 1 (fwd 23.0) | 2 (+5.6%) | 1 | 6 |
| 14 | HINDALCO | 2 (corr 0.33) | 2 (P/E 10.9) | 1 (-3.5%) | 1 | 6 |
| 15 | AZN | 2 (corr -0.30; research -0.02 monthly, -0.12 weekly) | 1 (fwd P/E 16.2, peer median) | 1 (+4.0%) | 1 (strong candidate; Rs 1.5-3 L) | 5 (size does not change the score) |
| plan | EXUS / IJPA / AVGS | 2 | 2 | 1 | 2 | 7 each |
| plan | XDWH | 2 | 0 (fwd 19.8 vs 15.7, +26%) | 2 (+14.3%) | 2 (health care: attractive) | 6 |
| plan | XDW0 | 2 (corr -0.34) | 1 (cheap on peak profits) | 2 (+7.1%) | 1 (energy: neutral to avoid) | 6 |
| plan | XDEW | 1 (US) | 1 | 2 (+5.9%) | 2 | 6 |
| plan | FLXC / LTAM | 2 | 2 | 0 (-10.1% / -6.5%) | 1 | 5 each |
| - | SHEL Shell | 2 (corr -0.32) | 1 (P/E 8.5 on peak profits) | 2 (+11.6%) | 1 | 6 (same exposure as XDW0) |
| - | HINDUNILVR | 2 (corr 0.01) | 2 | 1 (-4.8%) | 1 | 6 (same exposure as FMCGIETF) |
| - | ACN | 1 (IT services) | 2 (fwd 15.7) | 2 (+33.6%) | 0 (tech: do not add) | 5 |
| - | ITBEES | 1 (Indian IT) | 2 (P/E 19.4 vs avg 25.0) | 2 (+5.5%) | 0 (tech: do not add) | 5 |
| - | REITs | 1 (tech tenants) | 2 (P/NAV 0.88-0.94) | 1 (+6.3%, rates -2) | 1 (real estate avoid; India neutral) | 5 |
| - | DTE | 2 (corr 0.08) | 2 (fwd 10.7) | 0 (-5.7%) | 1 | 5 |
| - | MC LVMH | 2 (corr 0.23) | 2 (P/E 18.4 vs 24-30) | 0 (-12.2%) | 1 | 5 |
| - | POWERGRID, NTPC | 2 | 2 | 0 (-7.6%, -8.4%) | 1 | 5 |
| - | BHARTIARTL | 2 (corr -0.18) | 0 (P/E 38.3) | 2 (+12.2%) | 1 | 5 |
| - | AUTOBEES | 2 (corr 0.15) | 1 (P/E at median) | 1 (+4.4%) | 1 | 5 |
| - | SAP | 1 (software) | 1 (fwd 25.2) | 2 (+28.8%) | 0 (tech: do not add) | 4 |
| - | XDWU | 2 (corr -0.23) | 1 (US part +10%) | 0 (+1.2%, rates -2) | 1 (utilities: neutral) | 4 |
| - | HPRA | 2 (corr -0.03) | 1 (fair) | 0 (0.0%, rates -2) | 1 | 4 |
| - | XDWM | 2 (corr 0.20) | 1 (fwd 17.4 vs 17.8) | 1 (-1.5%) | 1 (materials: mostly avoid) | 5 |
| - | 4568 | 2 (corr 0.23; research 0.16) | 1 (true P/E 17.4) | 1 (+4.6%) | 0 (watch: Enhertu overlap with AZN; the lot-size reason no longer applies) | 4 |
| - | XDWI | 2 (corr 0.21) | 0 (+26% over history) | 1 (-3.0%) | 1 (industrials: avoid) | 4 |
| - | GDIG | 2 (corr 0.27) | 1 | 0 (-11.6%) | 1 | 4 |
| - | 8801 Mitsui Fudosan | 2 (corr 0.02) | 1 (fwd 15.3, P/B 1.30) | 0 (+0.6%, rates -2) | 0 (Japan real estate: avoid) | 3 |
| - | C38U CICT | 2 (corr -0.18) | 1 (yield 4.6%) | 0 (+0.1%, rates -2) | 0 (Asia real estate: avoid) | 3 |
| - | 8309 | 2 (corr -0.03) | 1 (true P/E 12.5; P/B 1.37 at a 5-yr high) | 2 (+18.3%; Japan banks +9.5% in the week, market brief) | 0 (pullback only, P/B 1.1-1.2) | 5 (16th, below AZN on research score) |
| - | HAL, BAE, Safran | 2 | 0 | 0-2 | 0 (small only) | 2-4 |

Data: yfinance daily closes (auto-adjusted) to 2026-11-13, pulled 2026-11-15 with a disk cache
(`~/.local/share/superpowers/finance-scout-buylist/cache/`). Lines: EXUS.L, IJPA.L, AVGS.L, XDEW.L, XDWH.L,
XDW0.L, XDWF.L, XDWU.L, XDWI.L, FLXC.L, LTAM.L, BANKBEES.NS, FMCGIETF.NS, HINDUNILVR.NS, ITBEES.NS, AUTOBEES.NS,
PHARMABEES.NS, MINDSPACE.NS, COALINDIA.NS, BPCL.NS, HINDALCO.NS, XDWM.L, GDIG.L, HPRA.L, 8801.T, C38U.SI, SHEL.L, STARHEALTH.NS, NH.NS, NTPC.NS, POWERGRID.NS, LT.NS, HAL.NS, BHARTIARTL.NS, 7203.T,
8031.T, 8309.T, 4568.T, 9433.T, MUV2.DE, SAP.DE, DTE.DE, MC.PA, SAF.PA, ULVR.L, AZN.L, BA.L, ACN, QCOM, MSFT.
Prices match the research notes where quoted (e.g. LT Rs 4,143.8, Mitsui JPY 5,100, Bharti Rs 2,106, DTE EUR
26.60, KDDI JPY 2,850, Mindspace Rs 497.97). FX: JPY/INR 0.5879, EUR/INR 103.85 (yfinance, 13 Nov 2026).
Valuations are quoted from the research notes, not from Yahoo. Sector inputs: `research/sectors/README.md` (cross-sector
ranking, main input) and its 11 sector folders. BAGMANE.NS has no Yahoo data; Bagmane price from the NSE bhavcopy (Rs 106.18, 13 Nov 2026; `scout/sources-notes.md`).

Correlation basis (two methods, same conclusion: low or negative for every fund here, no verdict changes):

| | Scout (this list) | finance-research |
|---|---|---|
| Period | 53 weeks to 2026-11-13 | 5 years |
| Frequency | Weekly (Friday closes) | Monthly |
| Compared with | One basket: 68% QCOM + 32% MSFT (their split in your holding) | QCOM and MSFT separately |
| Instrument | The listed line itself (EXUS.L, XDWH.L, XDW0.L, FLXC.L etc., 8309.T, TTE.PA), yfinance auto-adjusted closes in the line's own currency, no FX conversion | UCITS sector ETFs |
| Examples | Health care -0.19, energy -0.34 | Health care about 0.2, energy about 0 |

