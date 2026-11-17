# Materials: sources

Part of [materials](README.md). All read 2026-11-15 unless dated otherwise.

## Summary
- Prices, returns, recomputed P/Es: Yahoo via yfinance [Y]; index P/E and P/B history: niftyindices [NI];
  US sector P/E: FactSet [FS]; fund facts: justETF [JE], Groww [GR], AMFI/mfapi [AMFI][MF].
- News from Bing News RSS; many article pages 403 (BusinessWorld, Business Standard, mining.com, globalcement).
- Not verified: MSCI World Materials, Europe and Japan sector P/E vs 10-year history; gold-miner UCITS TERs.

## Data
| Tag | Source | What |
|---|---|---|
| [Y] | Yahoo Finance via yfinance (`.venv`), TZ=UTC, 2 s throttle | Prices to 12-13 Nov 2026 (Indian stocks to 12 Nov); 1y/3y/5y from `history(auto_adjust=True)`; P/E = `marketCap` / sum of last 4 quarterly `Net Income Common Stockholders` (FX to reporting currency); `forwardPE`, `priceToBook`; 60-month correlations |
| [NI] | niftyindices.com `BackPage/getpepbHistoricaldataDBtoString` | Daily P/E, P/B, yield of NIFTY METAL, NIFTY 50, NIFTY COMMODITIES (Nov 2015 - 13 Nov 2026), NIFTY CHEMICALS (from Mar 2025) |
| [FS] | FactSet Earnings Insight 13-Nov-2026, https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_111326.pdf | S&P 500 sector forward P/E (chart p.34: Materials 17.4, 5-yr 18.0, 10-yr 17.8); Q3 2026 materials earnings growth by industry |
| [SC] | screener.in consolidated pages (one read each): JSWSTEEL, HINDALCO | P/E 21.0 and 9.11; JSW quarterly profit rows |
| [SA1] | stockanalysis.com/etf/pick/ | PICK P/E 14.40, fwd 11.33, 52-week high 69.02 (US-listed) |
| [SA2] | stockanalysis.com/quote/tyo/4063/statistics/ | Shin-Etsu P/E 21.05, fwd 17.47, EV/EBITDA 9.88 |
| [SA3] | stockanalysis.com/quote/asx/BHP/statistics/ | BHP P/E 21.08, fwd 15.67, EV/EBITDA 7.05 |
| [SA4] | stockanalysis.com/etf/copx/ | COPX fwd 10.95, 52-week high 99.99 (US-listed) |
| [SA5] | stockanalysis.com/etf/gdx/ | GDX P/E 12.84, fwd 11.41, 52-week high 117.18 (US-listed) |
| [SA6] | stockanalysis.com/quote/etr/BAS/statistics/ | BASF P/E 8.24, fwd 20.63, EV/EBITDA 8.49 |
| [SA] | stockanalysis.com/etf/xlb/ | XLB fwd P/E 16.85, top holdings |
| [JE1] | https://www.justetf.com/en/etf-profile.html?isin=IE00BM67HS53 | XDWM TER, size, holdings, returns (data 29-Sep / mid-Nov 2026) |
| [JE2] | https://www.justetf.com/en/etf-profile.html?isin=IE00BDFBTQ78 | GDIG TER, size, holdings, returns |
| [JE3] | https://www.justetf.com/en/how-to/invest-in-materials.html | List of 18 materials UCITS ETFs (copper miners, MSCI World Materials) |
| [JE4] | https://www.justetf.com/en/how-to/invest-in-goldmines.html | Gold miner UCITS ETFs by size |
| [GR] | groww.in/etfs/<slug> page JSON (`fundamentalsData`); Groww search API | Nifty Metal ETF TER, AUM, tracking error, NSE symbols |
| [AMFI] | https://portal.amfiindia.com/spages/NAVAll.txt (13-Nov-2026) | List of metal, chemical, cement, commodity ETFs and funds |
| [MF] | api.mfapi.in/mf/<code> (119279, 119277, 152769, 151207) | Fund NAV returns |

## News (date of article)
| Tag | Source |
|---|---|
| [N1] | News18, 8-Sep-2026, LME copper record $14,533: https://www.news18.com/business/economy/copper-prices-hit-all-time-high-of-14530-what-is-driving-the-rally-in-global-markets-10316308.html |
| [N2] | New Indian Express, 31-Dec-2025, 12/11.5/11% safeguard duty: https://www.newindianexpress.com/business/2025/Dec/31/india-imposes-1112-safeguard-duty-on-select-steel-imports-for-three-years |
| [N3] | SunSirs, 12-Nov-2026, China Oct steel exports: https://www.sunsirs.com/commodity-news/petail-37625.html ; Telegraph India, 15-Dec-2025 (headline), export licences: https://www.telegraphindia.com/business/china-moves-to-licence-steel-exports-to-rein-in-record-flows-support-prices-globally-prnt/cid/2137879 |
| [N4] | Business Standard / New Indian Express, 9-10 Nov 2026 (headlines), China trade surplus over $1 trn: https://www.newindianexpress.com/business/2026/Nov/10/china-records-trade-surplus-over-1-trillion-dollar-for-second-straight-year-as-exports-surge-35-per-cent |
| [N5] | BusinessLine (PTI), 16-Oct-2026, worldsteel India +7.9%/+8%: https://www.thehindubusinessline.com/markets/commodities/india-remains-fastest-growing-major-steel-market-as-demand-rises-79-in-2026/article71574307.ece ; SMM (headline) world 1,722 Mt: https://news.metal.com/ru/newscontent/104171736-worldsteel-global-steel-demand-flat-at-1722-mt-in-2026-up-17-in-2027 |
| [N6] | Zawya (Reuters), 13-Nov-2026, Goldman copper $15,400 and risks; LME $13,612: https://www.zawya.com/en/business/goldman-sachs-flags-risks-to-15400t-copper-price-forecast-for-2027-2267818 |
| [N7] | Distribution Strategy, 10-Nov-2026 (headline): https://distributionstrategy.com/2026/11/border-states-copper-prices-rise-35-steel-31-as-data-center-demand-strains-supplies/ |
| [N8] | mining.com, 12-Nov-2026 (headline only, 403): https://www.mining.com/copper-shortage-or-surplus-banks-split-on-2027-outlook/ |
| [N9] | Business Today, 12-Jun-2026 (headline), Vedanta demerger listings: https://www.businesstoday.in/markets/stocks/story/vedanta-demerger-listing-date-out-for-oil-gas-power-aluminium-and-iron-steel-firms-536452-2026-06-12 |
| [N10] | CNBC-TV18, 6-Nov-2026, Hindalco Q2: https://www.cnbctv18.com/market/earnings/hindalco-q2-results-profit-more-than-doubles-revenue-jumps-43-pc-20028885.htm ; Investywise (headline) Rs 91,708 cr; Moneycontrol 14-Nov-2026 (headline) Novelis China sale |
| [N11] | Moneycontrol 15-Oct-2026 and Free Press Journal 29-Sep-2026 (headlines), steel policy 600 Mt; Hindustan Times 23-Sep-2026 (headline), Punjab duty waiver plea |
| [N12] | Upstox, 9-Nov-2026, steel Q2 results: https://upstox.com/news/market-news/stocks/tata-steel-jsw-steel-sail-steel-stocks-deliver-strong-q2-show-despite-cost-overhang-margin-growth-in-focus-next/article-203232/ ; Moneycontrol 9-Nov-2026 (headline) Tata Steel UK caution |
| [N13] | mining.com.au 12-Nov-2026 and mining.com 9-Nov-2026 (headlines), aluminium backwardation |
| [N14] | Business Standard, 2-Nov-2026 (headline), NMDC October output +18% |
| [N15] | Financial Times, 1-Nov-2026 (headline only): https://www.ft.com/content/2962ad57-cee1-4a63-82ba-17acfc09d812 |
| [N15b] | BusinessLine Statistalk, 13-Oct-2026: https://www.thehindubusinessline.com/opinion/columns/statistalk/indian-chemicals-from-market-darlings-to-a-slow-recovery/article71580689.ece |
| [N15c] | The Hindu 22-Sep-2026, Zee Business 9-Oct-2026, fibre2fashion 6-Oct-2026 (headlines), anti-dumping probes |
| [N16] | Zee Business, 22-Oct-2026, SRF Q2 and broker views: https://www.zeebiz.com/market-news/news-srf-shares-hit-52-week-low-after-q2-results-why-jefferies-morgan-stanley-and-ubs-remain-cautious-404334 |
| [N17] | CNBC-TV18, 5-Nov-2026, PI Industries Q2: https://www.cnbctv18.com/market/pi-industries-share-price-q2-review-sharp-margin-contraction-weak-agri-exports-drag-earnings-20027560.htm |
| [N18] | CNBC-TV18 (headlines): Deepak 29-Oct-2026, Navin 30-Oct-2026, Aarti 30-Oct-2026; Indian Chemical News 30-Oct-2026 (Aarti volumes) |
| [N20] | xenospectrum, 1-Nov-2026 (headline), Shin-Etsu wafer prices |
| [N21] | Malay Mail (AFP), 28-Oct-2026, BASF outlook: https://www.malaymail.com/news/money/2026/10/28/chemicals-giant-basf-raises-2026-profit-outlook-for-second-time-on-iran-war-price-hikes/241000 |
| [N22] | ET Realty / Investywise 19-Oct-2026 (UltraTech); Moneycontrol and Trade Brains 29-Oct to 13-Nov-2026 (Ambuja); BusinessLine 22-Oct-2026 (Shree); Global Cement 12-Nov-2026 (headline, 403) - all headlines |
| [N23] | ET Realty 29-Oct-2026 (headline) Asian Paints Q2; Moneycontrol 30-Oct-2026 (headline) brokers; Financial Express 21-May-2026 (headline) Nomura |
| [N24] | CNBC-TV18, 13-Nov-2026, Grasim Q2 and Birla Opus: https://www.cnbctv18.com/market/grasim-q2-results-chemicals-birla-opus-decorative-paints-volume-growth-guidance-share-price-move-20033480.htm ; Financial Express 9-Sep-2025 (6.6% share), Moneycontrol 11-Feb-2026 (break-even) - headlines |

## Gaps (not verified)
- MSCI World Materials index P/E and its 10-year average (MSCI factsheet URL unknown); Europe and Japan materials
  P/E vs history.
- TERs of VanEck Gold Miners UCITS, iShares Gold Producers UCITS, Indian chemical and cement ETFs, smaller Nifty
  Metal ETFs; whether DSP World Mining FoF accepts lump sums now.
- Glencore dividend withholding for an Indian holder.
