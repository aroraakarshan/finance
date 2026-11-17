# Mutual fund overlap: what the export says and per-fund facts

## Summary
- All 15 funds are Direct Plan - Growth (AMFI, checked by ISIN), so there is no regular -> direct saving.
- Lot dates now come from finance-tax's AngelOne MF transaction files; the NAV-based inference below is superseded.
- Table 1 lists expense ratio, benchmark, AUM and exit load per fund (Groww, 2026-11-10 to 2026-11-14).
- Kotak Arbitrage shows 2.27% total vs 0.32% base TER; the reason is not verified.

Back to the index: [mutual-fund-overlap.md](../mutual-fund-overlap.md). Section numbers (0-6) are kept from the original note; sources [G], [K], [A], [M], [P], [T], [TX] are in [sources.md](sources.md).

## 0. What the export does and does not say
- Raw xlsx columns: Fund Name, ISIN, Category, Sub Category, Folio No, Source, Units, Invested Value,
  Value, Average NAV, NAV, Unrealized P&L, %. No purchase dates, no SIP flag.
- Plan: all 15 ISINs map to **Direct Plan - Growth** in [A] (checked one by one). So there is no
  regular -> direct saving to collect (that switch would have saved about 0.5-1.1%/yr, see table 1).
- Holding period: **unknown**. Get exact lot dates from a CAMS/KFintech CAS before selling.
  Inference from [M]: average cost must be at or below the NAV of at least one purchase, so the first
  date NAV reached the average cost bounds the latest buy. Clear cases:
  - Kotak Arbitrage: NAV first reached avg 43.345 on 2026-09-28 -> some units bought after that (< 2 months old).
  - Nippon Midcap 150: first reached avg 26.576 on 2026-06-19 -> some units < 6 months old.
  - Silver FoF 2025-12-22, Gold-Silver FoF 2025-12-24 -> some units < 12 months old.
  - HDFC Mid Cap 2025-06-27, Invesco Mid Cap 2025-07-15, PPFAS 2025-06-06 -> some units bought after mid-2025.
  - Others (PSU, infra, ICICI LC, UTI N50, NN50, Quant) first touched avg in May-Jul 2024: inconclusive.
  - Small gains overall (+1.4%) also point to mostly recent buys. Treat as unverified.
  - Superseded: finance-tax has lot dates from AngelOne MF transaction files 2024-07-26 to 2026-11-07,
    FIFO, units reconciled ([tax/angelone-metals-and-mf-exits.md](../../../tax/angelone-metals-and-mf-exits.md) 4, 7). Examples: Kotak NN50 and
    Nippon MC150 are one lot each, 2026-09-23 (my inference for NN50 was inconclusive; Nippon fits);
    Invesco Mid Cap one lot 2025-12-10; ICICI LC, ABSL PSU and others have lots up to 2026-11-02
    (SIPs). A CAS is still wanted to confirm folio lots and any units before 2024-07-26 (same, 7).

## 1. Per-fund facts (direct plan) [G], [K]
TER = total expense ratio as shown by Groww; "base" = Groww's base expense ratio (excludes the extra
costs Groww adds on top; exact split not verified). AUM in Rs crore as shown on 2026-11-15.

| # | Fund (Groww slug) | Benchmark | AUM cr | TER dir (base) | TER reg | TER date | Exit load [G] |
|---|---|---|---|---|---|---|---|
| 0 | ICICI Pru Large Cap (icici-prudential-large-cap-fund-direct-growth) | Nifty 100 TRI | 76,895 | 1.00 (0.72) | 1.48 | 2026-11-12 | 1% within 1 month (since 2026-04-06; earlier: 1% within 1 year) |
| 2 | Kotak Arbitrage (kotak-arbitrage-fund-direct-growth) | Nifty 50 Arbitrage TRI | 76,415 | 2.27 (0.32) | 2.86 | 2026-11-10 | 0.25% within 30 days |
| 3 | Kotak Nifty Next 50 Index (kotak-nifty-next-50-index-fund-direct-growth) | Nifty Next 50 TRI | 1,370 | 0.27 (0.08) | 0.68 | 2026-11-10 | Nil |
| 4 | HDFC Mid Cap (hdfc-mid-cap-fund-direct-growth) | Nifty Midcap 150 TRI | 1,00,687 | 0.73 (0.59) | 1.30 | 2026-11-12 | 1% within 1 year |
| 5 | SBI PSU (sbi-psu-fund-direct-growth) | BSE PSU TRI | 6,191 | 0.97 (0.72) | 1.95 | 2026-11-12 | 0.5% within 30 days |
| 6 | Nippon Nifty Midcap 150 Index (nippon-india-nifty-midcap-150-index-fund-direct-growth) | Nifty Midcap 150 TRI | 2,619 | 0.41 (0.25) | 0.93 | 2026-11-13 | Nil |
| 7 | Invesco India Mid Cap (invesco-india-mid-cap-fund-direct-growth) | BSE 150 MidCap TRI | 15,831 | 0.75 (0.48) | 1.85 | 2026-11-13 | 1% within 1 year on units above 10% |
| 8 | Invesco India PSU Equity (invesco-india-psu-equity-fund-direct-growth) | BSE PSU TRI | 1,308 | 1.19 (0.81) | 2.37 | 2026-11-13 | 1% within 1 year on units above 10% |
| 9 | ABSL PSU Equity (aditya-birla-sun-life-psu-equity-fund-direct-growth) | BSE PSU TRI | 5,705 | 0.74 (0.60) | 1.86 | 2026-11-12 | 1% within 30 days |
| 11 | LIC MF Infrastructure (lic-mf-infrastructure-fund-direct-growth) | Nifty Infrastructure TRI | 1,100 | 1.27 (0.67) | 2.61 | 2026-11-14 | 1% within 90 days on units above 12% |
| 12 | UTI Nifty 50 Index (uti-nifty-fund-direct-growth) | Nifty 50 TRI | 28,985 | 0.25 (0.18) | 0.31 | 2026-11-13 | Nil |
| 13 | Parag Parikh Flexi Cap (parag-parikh-long-term-value-fund-direct-growth) | Nifty 500 TRI | 1,46,785 | 0.68 (0.52) | 1.29 | 2026-11-12 | units above 10%: 2% within 365 days, 1% for 366-730 days [P] |
| 14 | Quant Small Cap (quant-small-cap-fund-direct-plan-growth) | Nifty Smallcap 250 TRI | 33,810 | 0.96 (0.68) | 1.65 | 2026-11-13 | 1% within 1 year |
| 1, 10 | Silver ETF FoF / Gold and Silver FoF | - | - | 0.20 / 0.18 | - | 2026-11-12/13 | 1% within 15 days / Nil - see [silver-gold.md](../silver-gold.md) |

Notes:
- Kotak Arbitrage total TER 2.27% vs base 0.32% in both [G] and [K] (2.3%, 2026-10-31). The gap is
  likely trading costs and levies of the hedge trades now shown in TER; not verified. Its NAV already
  reflects it.
- Exit load applies by the terms on the allotment date of each lot.
- PPFAS cash/debt/REIT about 15% and foreign stocks (Alphabet 4.3%, Microsoft 2.5%, Amazon 2.3%) per
  its 2026-09-30 portfolio [G]. That foreign part overlaps your US stocks (about $213k, 47.7% of total).
