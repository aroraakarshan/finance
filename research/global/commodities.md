# Commodities: oil, copper, agriculture, broad baskets

Written 2026-11-15 by `finance-research`. Research only, not advice; no orders. Sources [C#] at
the end. "nv" = not verified. Prices: yfinance closes of 2026-11-13 [C1].

## Summary
- Verdict: neutral to skip. JPM forecasts 4.8%/yr for broad commodities (vs 7.5% US large cap)
  with 14-40% volatility, and prices are near records after a +25% year [C1, C7].
- If he wants an inflation/war hedge: 0-3% in CMOD or ICOM (Irish UCITS, BCOM, 0.19%), in steps.
- Skip oil/agriculture ETCs (grey under LRS, war-priced, roll cost), MCX F&O and US DBC.

Gold and silver: see `research/themes/silver-gold.md` and `research/themes/opp-real-assets.md`
(being written); only one line here.

## 1. What it is

- Commodity funds do not hold barrels or tonnes. They hold **futures** and roll them each month
  (or a swap that pays the index return). Return = spot price change + roll yield (negative when
  later contracts cost more, "contango") + interest on the cash collateral.
- Roll cost is real: copper ETC COPA returned 16.8%/yr over 3 years vs 18.4%/yr for the copper
  front-month future; WTI ETC CRUD's largest fall since 2007 is -97% [C1, C2].
- No dividends or earnings; price is set by supply/demand cycles that last years.

## 2. Access for an Indian resident

LRS rule: Overseas Investment Directions 2022 para 1(ix)(a) bar portfolio investment in "any
commodities including Bullion Depository Receipts"; para 1(ix)(e) allow units of a regulated
overseas fund (`research/themes/ibkr-global/rules.md` section 1, [C3]).
- **UCITS commodity ETF** (Irish fund holding a swap) = a regulated fund unit -> fits the
  allowed route best.
- **ETC** (WisdomTree COPA, BRNT etc.: Jersey-issued debt notes linked to a commodity) = listed
  security, but its value is a commodity -> **grey**; no RBI text found either way (nv).
- **US-listed commodity pools** (e.g. DBC): US-situs (US estate tax, `us-estate-tax.md`); skip.
- **India MCX commodity futures/options**: derivatives (F&O). Not for this user now (see
  `research/themes/starter-trading-rules.md`). Gold/silver ETFs in India: see `silver-gold.md`.
- IBKR: LSE, Xetra, Euronext, SIX open (`../themes/ibkr-global/equities.md` 3.1). Whether IBKR blocks ETCs for
  Indian clients (PRIIPs/KID rule): nv.

| Fund (structure) | Ticker (exchange, ccy) | ISIN | TER | Size | Index / note [C2] |
|---|---|---|---|---|---|
| Invesco Bloomberg Commodity UCITS ETF Acc (Irish ETF, swap) | CMOD (LSE USD), CMOP (LSE GBX) | IE00BD6FTQ80 | 0.19% | EUR 3,459 m | Bloomberg Commodity (BCOM); acc |
| iShares Diversified Commodity Swap UCITS ETF (Irish ETF, swap) | ICOM (LSE USD), SXRS (Xetra) | IE00BDFL4P12 | 0.19% | EUR 2,156 m | BCOM; acc |
| UBS CMCI Composite SF UCITS ETF USD acc (Irish ETF, swap) | UC14 (LSE USD), CCUSAS (SIX) | IE00B53H0131 | 0.34% | EUR 1,381 m | UBS CMCI (spreads over maturities) |
| WisdomTree Copper (ETC) | COPA (LSE USD), OD7C (Xetra) | GB00B15KXQ89 | 0.49% | EUR 1,592 m | Bloomberg Copper; max fall -68% |
| WisdomTree Brent Crude Oil (ETC) | BRNT (LSE USD) | JE00B78CGV99 | 0.49% | EUR 864 m | Bloomberg Brent; max fall -83% |
| WisdomTree WTI Crude Oil (ETC) | CRUD (LSE USD) | GB00B15KXV33 | 0.49% | EUR 498 m | max fall -97% |
| WisdomTree Agriculture (ETC) | AIGA (LSE USD) | GB00B15KYH63 | 0.49% | EUR 650 m | Bloomberg Agriculture; max fall -63% |
| WisdomTree Industrial Metals (ETC) | (LSE) nv | GB00B15KYG56 | 0.49% | EUR 1,105 m | Bloomberg Industrial Metals |

BCOM check: CMOD is Invesco (not iShares); both CMOD and ICOM track BCOM [C2].
No UCITS ETF tracks only copper or only oil: single-commodity exposure here means an ETC (nv
beyond justETF search results).

## 3. Valuation / state now

Commodities have no P/E; the guide is price vs history and the futures curve.

| Item | Last (2026-11-13) | 1y | 3y/yr | 5y/yr | 10y/yr | Off peak | Vol 3y [C1] |
|---|---|---|---|---|---|---|---|
| Brent future (BZ=F) | USD 95.84 | +52% | +5.1% | +3.1% | +7.7% | -34% (peak 146, Jul 2008) | 40% |
| Copper future (HG=F) | USD 6.08/lb | +19.5% | +18.4% | +6.4% | +9.1% | -10.6% (record 6.80, 2026-09-09) | 29% |
| Corn future (ZC=F) | 445.5 c/bu | +0.9% | -2.3% | -5.0% | +2.6% | -46% (peak Aug 2012) | 21% |
| CMOD.L (BCOM, USD) | 33.43 | +25.4% | +13.7% | +9.0% | - | -8.5% (peak 2026-09-23) | 14% |
| COPA.L (USD) | 52.12 | +15.2% | +16.8% | +5.8% | +7.6% | -10.6% | 27% |
| DBC (US, for long history) | 30.79 | +38.9% | +13.0% | +10.7% | +9.7% | -20% (peak Jul 2008) | 17% |

- Oil: Brent USD 95.5 on 2026-11-13, second weekly fall, on expectations of a prolonged US
  blockade of Iranian oil rather than wider war; Hormuz shipping still a risk [C4]. Price is
  war-driven, not demand-driven.
- Copper: record in Sep 2026; London copper about USD 14,622/t on 2026-10-10, UBS calls copper
  its "highest conviction" theme with deficit into the early 2030s; Deutsche Bank target
  USD 22,050/t for Q2 2027 [C5]. Goldman (2025-12-11) expected some decline from records in
  2026 [C6, headline only].
- Agriculture: corn near 2016-2020 levels, -46% from 2012 [C1]. Cheap vs past peaks, no trend.
- Gold (IGLN.L, USD): -7.8% in 1y, 26.7% below its 2026-03-02 peak; +15.7%/yr over 5y [C1].
- Futures-curve shape (contango/backwardation) now: nv (no free source).

## 4. Expected return evidence

| Source (date) | Forecast | Note |
|---|---|---|
| J.P. Morgan 2027 LTCMA (2026-10-19) [C7] | Broad commodities 4.8%/yr; gold 5.5% | 10-15 yr, USD. US large cap 7.5%, so commodities forecast below stocks |
| Research Affiliates, GMO, Vanguard, AQR | not fetched (JavaScript sites / no free page) | nv |
| Own history (DBC 10y) [C1] | 9.7%/yr to 2026-11, but -76% max fall (2008-2020) | Long flat-to-down stretches |

Reading: forecast return is about bond-like (4.8%) with stock-like volatility (14-40%). Main use
is as an inflation/war hedge, not for growth.

## 5. Risks

- War- and policy-driven spikes reverse fast: Brent -87% from Jul 2008 to Apr 2020, WTI ETC -97%.
- Roll cost in contango; ETC counterparty/swap risk (collateralised, but a note, not a fund).
- Already near highs: CMOD 8.5% and copper 10.6% below record after a strong year [C1].
- LRS grey for ETCs; tax: no row for ETCs in `tax/investment-types.md` (treat like foreign
  securities: 24 m / 12.5% LTCG / slab; CA to confirm). Irish acc UCITS (CMOD/ICOM): no tax till
  sale, 24 m / 12.5% / slab [tax/investment-types.md section 1].
- Correlation with the user's tech stocks: copper is an AI/data-centre play too, so it is less
  of a diversifier than it looks.

## 6. Instruments for this user and verdict

| Rank | Instrument | Why |
|---|---|---|
| 1 | CMOD or ICOM (LSE USD, BCOM, 0.19%, Irish acc) | Cleanest LRS fit (regulated fund), broad, cheap, no tax till sale |
| 2 | COPA (copper ETC) | Only if he wants a copper view; grey under LRS; near record |
| - | BRNT/CRUD, AIGA | Skip: war-priced oil, weak long-run agriculture, high roll cost |
| - | MCX futures/options, US DBC | Skip: derivatives / US-situs |

**Verdict: neutral to skip.** 4.8%/yr forecast < stocks; after a +25% year and near records
there is no value case. If he wants an inflation/war hedge, 0-3% of the portfolio in CMOD,
bought in steps, is enough; his gold/silver at AngelOne already does part of this job.

## Sources (all read 2026-11-15)

- C1 yfinance: BZ=F, HG=F, ZC=F, DBC, CMOD.L, COPA.L, IGLN.L (closes to 2026-11-13). Worked.
- C2 justETF profiles by ISIN: https://www.justetf.com/en/etf-profile.html?isin=IE00BD6FTQ80 (and
  IE00BDFL4P12, IE00B53H0131, GB00B15KXQ89, JE00B78CGV99, GB00B15KXV33, GB00B15KYH63, GB00B15KYG56).
- C3 RBI OI Directions 2022, as quoted in `research/themes/ibkr-global/rules.md` [S3].
- C4 HDFC Sky, Brent 2026-11-13: https://hdfcsky.com/news/brent-crude-oil-price-today-november-13-2026-brent-slips-0-3percent-to-95-5-per-barrel-as-oil-heads-for-second-weekly-decline
- C5 BigGo Finance (UBS, Deutsche Bank on copper), 2026-10-10: https://finance.biggo.com/news/3f7a5aa1-861d-4c5d-b4e6-20c7abf30ca1
- C6 Goldman Sachs headline 2025-12-11: https://www.goldmansachs.com/insights/articles/copper-prices-forecast-to-decline-from-record-highs-in-2026 (not opened)
- C7 J.P. Morgan 2027 LTCMA press release, 2026-10-19: https://www.prnewswire.com/news-releases/jp-morgan-releases-2027-longterm-capital-market-assumptions-projecting-7-0-return-for-6040-portfolio-over-10-15-years-302912421.html
