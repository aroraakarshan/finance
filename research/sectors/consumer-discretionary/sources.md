# Consumer discretionary: sources

Part of [consumer discretionary](README.md). Retrieved 2026-11-15 unless noted. Score 1-5 as in
[research/sources.md](../../sources.md).

## Summary

- Prices, returns and P/E: yfinance, recomputed and spot-checked with stockanalysis and justETF.
- Index valuation: niftyindices (India, 10 years of daily P/E), FactSet (US sector P/E vs 25-year average).
- Company news: dated articles found through Bing News RSS; company IR for Amazon.

## Sources

| Tag | Source | URL | Date of data |
|---|---|---|---|
| D1 | yfinance (Yahoo): adjusted closes, `info`, quarterly and annual income statements, `earnings_estimate`; FX HKDCNY=X 0.8504 | Python `yfinance` 1.8.0 | Closes to 13 Nov 2026 |
| D2 | niftyindices P/E, P/B history API (Nifty Auto, Nifty 50; 2,480 daily rows each) | niftyindices.com/BackPage/getpepbHistoricaldataDBtoString | 15 Nov 2016 - 13 Nov 2026 |
| D3 | FactSet Earnings Insight, "Lowest forward 12-month P/E ratio for the S&P 500 in more than 3 years" (sector chart) | https://insight.factset.com/lowest-forward-12-month-p/e-ratio-for-the-sp-500-in-more-than-3-years | 5 Nov 2026 (posted 9 Nov) |
| D4 | justETF, Xtrackers MSCI World Consumer Discretionary UCITS ETF 1C | https://www.justetf.com/en/etf-profile.html?isin=IE00BM67HP23 | Holdings 29 Sep 2026; returns to Nov 2026 |
| D5 | stockanalysis, XLY | https://stockanalysis.com/etf/xly/ | 13 Nov 2026 |
| D6 | stockanalysis, LVMH statistics and ratios | https://stockanalysis.com/quote/epa/MC/statistics/ and /financials/ratios/ | 13 Nov 2026 |
| D7 | stockanalysis, BYD statistics | https://stockanalysis.com/quote/hkg/1211/statistics/ | 13 Nov 2026 |
| D8 | AMFI NAV file | https://portal.amfiindia.com/spages/NAVAll.txt | 13 Nov 2026 |
| D9 | Groww ETF and fund pages (TER, AUM) | groww.in/etfs/nippon-india-nifty-auto-etf-netfauto, .../icici-prudential-nifty-auto-etf-iciciauto, groww.in/mutual-funds/nippon-india-nifty-auto-index-fund-direct-growth, .../icici-prudential-nifty-auto-index-fund-direct-growth | 13 Nov 2026 |
| D10 | Business Today, SIAM October 2026 sales | https://www.businesstoday.in/auto/story/auto-industry-posts-record-october-sales-as-passenger-vehicles-cross-5-lakh-mark-2-wheelers-grow-16-567320-2026-11-13 | 13 Nov 2026 |
| D11 | Livemint, GST relief for small cars, bikes | https://www.livemint.com/auto-news/gst-relief-for-small-cars-bikes-set-to-rev-up-auto-demand-11756949554550.html | 4 Sep 2025 |
| D12 | ET Auto, Maruti Q2 FY27 | https://auto.economictimes.indiatimes.com/news/passenger-vehicle/maruti-suzuki-q2-net-profit-falls-26-to-2466-crore/135232780 | 27 Oct 2026 |
| D13 | ET Auto, Tata Motors PV Q2 FY27 | https://auto.economictimes.indiatimes.com/news/passenger-vehicle/tata-motors-pv-posts-5531-crore-net-loss-in-q2-revenue-rises-34/135801566 | 13 Nov 2026 |
| D14 | Livemint, TMCV listing date (headline via Bing News RSS only) | https://www.livemint.com/market/stock-market-news/tata-motors-demerger-tmcv-shares-listing-date-announced-check-details-here-11762828728135.html | 10 Nov 2025 |
| D15 | AP via WTOP, Toyota raises profit projection | https://wtop.com/world/2026/11/toyota-raises-profit-projection-for-the-year-as-sales-hold-up/ | 5 Nov 2026 |
| D16 | TeslaNorth, Tesla Q3 2026 (quotes the Q3 update) | https://teslanorth.com/2026/10/21/tesla-q3-2026-earnings/ | 21 Oct 2026 |
| D17 | CnEVPost, BYD October 2026 sales | https://cnevpost.com/2026/11/01/byd-oct-2026-sales/ | 1 Nov 2026 |
| D18 | Amazon IR, Q3 2026 results | https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report | 29 Oct 2026 |
| D19 | CNBC-TV18, Trent Q2 FY27 | https://www.cnbctv18.com/market/earnings/trent-q2-results-ebitda-jumps-30-pc-margin-beats-estimates-strong-zudio-expansion-20022523.htm | 29 Oct 2026 |
| D20 | Financial Express, DMart Q2 FY27 | https://www.financialexpress.com/market/dmart-q2-results-net-profit-rises-8-5-to-rs-743-crore-revenue-jumps-178-4358144/ | 10 Oct 2026 |
| D21 | Medianama, Eternal Q2 FY27 (links the shareholder letter) | https://www.medianama.com/2026/10/223-eternal-125-crore-profit-q2fy27/ | 22 Oct 2026 |
| D22 | Times Now, Swiggy Q2 FY27 | https://www.timesnownews.com/business-economy/markets/swiggy-q2-fy27-results-net-loss-narrows-to-rs-922-crore-revenue-jumps-36-article-156385747 | 22 Oct 2026 |
| D23 | Il Sole 24 Ore, LVMH Q3 2026 | https://en.ilsole24ore.com/art/lvmh-disappoints-the-market-revenue-down-16-per-cent-at-current-exchange-rates-AJY9odhB | 12 Oct 2026 |
| D24 | RTE (Reuters), Hermes Q3 2026 | https://www.rte.ie/news/business/2026/1022/1596397-hermes-quarterly-results/ | 22 Oct 2026 |
| D25 | Financial Express, Titan Q2 FY27 | https://www.financialexpress.com/business/industry-titan-company-q2-result-profit-jumps-over-two-fold-to-rs-2393-crore-4377913/ | 5 Nov 2026 |
| D26 | CNBC-TV18, Indian Hotels Q2 FY27 | https://www.cnbctv18.com/market/earnings/indian-hotels-q2-results-tata-group-company-net-profit-rises-to-rs-380-crore-revenue-up-21-pc-20016224.htm | 21 Oct 2026 |
| D27 | Citybiz, Marriott Q3 2026 | https://www.citybiz.co/article/927432/marriott-raises-2026-revpar-outlook-after-6-5-third-quarter-growth/ | 2 Nov 2026 |
| D28 | ET BrandEquity (Reuters), Bain luxury outlook | https://brandequity.economictimes.indiatimes.com/news/marketing/luxury-sector-to-revive-in-2026-but-price-hikes-leave-shoppers-betrayed-bain-says/125481977 | 21 Nov 2025 |
| D29 | ET Auto video, FY27 auto outlook (headline only) | https://auto.economictimes.indiatimes.com/videos/h1-analysis-indias-auto-industry-eyes-10-growth-in-fy27-pv-sales-to-cross-5mn-units/134931098 | 13 Oct 2026 |
| D30 | Repository notes for tax and withholding | ../../../tax/investment-types.md; ../../global/eurozone/access-valuation.md (France 12.8%); ../../global/japan.md (Japan 15.315%, treaty 10%); ../../global/china-hong-kong.md (mainland 10%) | 2026-11-15 |

## Gaps (not verified)

- MSCI World Consumer Discretionary P/E and its 10-year average (no factsheet URL found); XDWC P/E is Yahoo's.
- S&P 500 Consumer Discretionary 10-year average P/E (FactSet free post gives the 25-year average only).
- 10-year P/E history for Nifty India Consumption (niftyindices returned nothing for that name), Toyota, BYD, STOXX 600 Autos.
- Indian consensus EPS may be standalone; Amazon LTM EPS not recomputed (Yahoo quarter gap); Titan Q2 profit growth (sources disagree).
- EV GST rate after Sep 2025 (article text cut off); TMCV listing date from a headline only.
- AUTOBEES/AUTOIETF trading volume and AUM; correlation of these names with QCOM/MSFT.
- France-India treaty rate on portfolio dividends.

## Sources tried

| Source | Worked? | Score |
|---|---|---|
| yfinance | Yes; Amazon quarter gap, Tata PV one-off gain, BYD currency mix all needed fixing | 4 |
| niftyindices P/E API | Yes for NIFTY AUTO, NIFTY 50; empty for Nifty India Consumption, Nifty Consumer Durables names tried | 5 |
| FactSet Insight | Yes (text by curl; sector numbers only in a chart image) | 5 |
| justETF | Yes (web_fetch) | 5 |
| stockanalysis | Yes (web_fetch) | 4 |
| AMFI NAV file, Groww pages | Yes | 5 / 4 |
| Bing News RSS | Yes, dated article links | 5 |
| Company IR (Amazon) | Yes | 5 |
| Business Standard | 403 | 1 |
| globalchinaev.com | 429 | 1 |
| cnbctv18 (truncated URL) | 404 when URL cut; full URLs work | 4 |
