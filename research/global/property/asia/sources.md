# Asia property: method, FX and sources

Part of [Asia property](../asia.md).

## Summary
- FX: yfinance closes of 13 Nov 2026 (USD 94.03); prices from Global Property Guide (USD) and Numbeo (secondary).
- Net yields in the parts are estimates from stated assumptions, not data.
- Best sources: IRAS, PwC tax summaries, Google News RSS; several sites blocked (listed below).

## Method and FX

Research only, written 2026-11-15. Indian-side rules (LRS, FEMA, Indian tax) are in `india-rules.md`; this page
covers only what each country does to a foreign (Indian) buyer.

**FX used** (yfinance close 13 Nov 2026; VND and PHP crossed through USD): USD 94.03, SGD 73.03, MYR 22.96,
THB 2.776, JPY 0.588, PHP 1.493, IDR 0.005155, VND 0.003663 (Rs per unit). Rs 1 Cr = 10 million rupees, Rs 1 L = 100,000.

**Price sources**: GPG = Global Property Guide rental-yield pages (free part shows only one area per country,
prices in USD, date shown per country). Numbeo = crowd data, apartment price per sq m city centre / outside centre,
pages updated 8-14 Nov 2026 (secondary). Net yields in the country parts are my estimates from stated assumptions, not data.

**Budget context**: Rs 2.23 Cr total is about USD 237k. Every country below except Thailand (and a cheap Japanese
regional unit) needs more than half of that for one flat, before costs.

## Sources tried

IRAS ABSD/BSD/SSD/property-tax/FTA pages (curl works; 5) - PwC tax summaries individual and corporate pages for all
7 countries (5) - Global Property Guide rental-yield pages (web_fetch works, one free area per country; sq m pages
need JavaScript; 3) - Numbeo property-investment pages (curl works; 3) - yfinance FX (4) - Google News RSS +
decoder (5) - EdgeProp MY, The Edge MY, Thai Examiner, Thaiger, Nation Thailand, Bangkok Post, VIR, Bali Sun,
NusaBali, BaliNews, Asia Property Awards, Asahi, Japan Today (via r.jina.ai), PropertyNet.SG (via r.jina.ai),
Straits Times (via r.jina.ai), Aureada, ASEAN Briefing (4 or 3) - blocked/empty: SLA, PRA SRRV page, NST,
DollarsAndSense, EU Reporter, Japan Times, SCMP body, Tokyo tax office, Vietcetera (binary).
