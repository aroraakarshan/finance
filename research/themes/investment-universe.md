# Investment universe: what the user can invest in, and what fits

Written 2026-11-15 by `finance-research`. Proposals only: the user decides and trades; agents
place no orders. Details, numbers and sources are in the linked notes; tax answers are from
`finance-tax` in `tax/investment-types.md` (section numbers below refer to it).

## Summary
- Best fits among about 30 types: Irish accumulating UCITS ETFs at IBKR, EPF/VPF and PPF (5; PPF not chosen, your decision 16 Nov 2026); employer NPS and an arbitrage fund for parking (4).
- Not allowed under LRS: options, futures, event contracts and margin abroad. Crypto, foreign bonds and share lending are grey.
- Foreign bond ETFs and US money market funds may be taxed as always short-term (35.88%): ask a CA first.
- The current ranked action list is `research/global/README.md` section 3.

User (portfolio/summary.md, 2026-11-15): salaried Indian resident, total about Rs 4.21 Cr (incl. bank deposits, EPF and physical gold; version of 2026-11-15).
QCOM 761 (IBKR) 41.5% and MSFT 116.888 (Fidelity) 19.3% = 60.8% in two US stocks; AngelOne Rs 26 L
(15 MFs; metals 31.6% of AngelOne but 3.7% of total); US stocks about $11k (INDmoney, moving to IBKR); wants to learn
trading; no trading rules yet. Tax bracket: 15% surcharge, so slab income 35.88%, foreign
LTCG 14.95% after 24 months, Indian equity STCG 23.92% / LTCG 14.95% (tax section 0).

## 1. First: US estate tax (high priority)
Note: `research/themes/us-estate-tax.md`; tax section 4.
- A non-US person who dies holding US-situs assets (US company shares, US-domiciled ETFs) over
  **$60,000** pays US estate tax at 18-40%. India has no estate tax treaty with the US and gives
  no credit (IRS treaty list; tax section 4).
- Exposure now (us-estate-tax.md, updated 2026-11-15): $213k US-situs -> about **$46,100 (Rs 43 L)** tax at
  death; with the 238 unvested MSFT shares that vest at death, $338k -> about **$87,700 (Rs 82.5 L)**; heirs also need
  Form 706-NA and an IRS transfer certificate before brokers release assets (1.5-3 years).
- Not US-situs: Irish UCITS ETFs, US bank deposits, US Treasuries (portfolio-interest debt).
- Ways out: diversify QCOM/MSFT into accumulating Irish UCITS ETFs at IBKR; sell MSFT at each
  vest; term life cover meanwhile; keep US-situs assets near $60k over time.

## 2. Overview
Access: A = AngelOne, I = IBKR, N = INDmoney, F = Fidelity, new = new account or platform.
LRS: allowed / NOT = not allowed for a resident / grey = unclear (RBI LRS Master Direction
updated 2024-09-06, LRS FAQ, Overseas Investment Directions 2022; see ibkr-global.md).
Fit 1-5 for this user (from the group notes, adjusted for tax).

| Group | Instrument | Access | LRS | Min | Tax (resident, this bracket) | Fit |
|---|---|---|---|---|---|---|
| Abroad | Irish UCITS ETFs, accumulating (CSPX, VUAA, VWRA, SWDA) | I | allowed | 1 share | No tax until sale; 24 m -> 14.95%; US div withholding 15% inside fund; not US-situs | 5 |
| Abroad | US stocks and ETFs | I, N | allowed | 1 share / $1 fractional | Div 25% US + slab with FTC; 24 m -> 14.95%; US-situs | 3 |
| Abroad | Europe stocks (LSE, Euronext, Xetra, SIX) | I | allowed | 1 share | As foreign shares; Germany 26.4% div withholding, reclaim slow | 2 |
| Abroad | Asia stocks (HKEX, TSE, ASX, SGX) | I | allowed | board lot | As foreign shares; Japan 15.3% withholding | 1 |
| Abroad | US Treasury ETFs (listed) | I | allowed | 1 share | Possibly always short-term (AF s.76, >65% debt fund) -> 35.88%; CA | 2 |
| Abroad | US T-bills, Treasuries | I | grey | $100 face | Interest slab; "unlisted bond" always-ST risk; US withholding 0% | 2 |
| Abroad | US corporate/muni bonds, CDs | I | grey | varies | Slab; high always-ST risk; muni exemption does not carry over | 1 |
| Abroad | US money market funds | I (nv) | allowed | fund min | Probably always ST; 25% div withholding | 1 |
| Abroad | Interest on idle USD at IBKR | I | allowed (180-day reinvest/repatriate rule) | 0% on first $10k | Slab | 2 |
| Abroad | SYEP share lending | I (IB LLC only) | grey | cash a/c > $25k | Fee at slab; may count as a sale | 1 |
| Abroad | Fractional shares, mutual fund marketplace | I | allowed | $1 / fund min | As underlying | 2 |
| Abroad | Options, futures, ForecastEx event contracts, margin | I | **NOT** | - | Speculative business income | 1 |
| Abroad | Crypto (IBKR via Paxos/Zero Hash) | I (nv) | grey | $1.75 fee | 30% flat (35.88%), no loss set-off | 1 |
| India | Equity/index MFs, ETFs, stocks | A | - | Rs 100 | 12 m; LTCG 14.95% above Rs 1.25 L; STCG 23.92% | 4 (cut to 4 funds) |
| India | Arbitrage fund (parking) | A | - | Rs 100 | Equity tax: 23.92% ST / 14.95% LT, better than slab for parked cash | 4 |
| India | EPF / VPF | payroll | - | payroll | 8.25% (FY 2025-26); interest on own contribution above Rs 2.5 L/yr taxable | 5 |
| India | NPS Tier 1 (employer 80CCD(2)) | payroll / eNPS | - | Rs 1,000 (nv) | Employer up to 14% of salary deductible in the new regime (the user files under the new regime, decided 2026-11-15); own Rs 50k deduction not available | 4 |
| India | PPF | bank / post office | - | Rs 500 | Interest exempt; 7.1% (Q3 FY27) = about 11% pre-tax at 35.88%; 15-yr lock, Rs 1.5 L/yr cap; no deposit deduction (user on new regime), interest still exempt; not chosen (16 Nov 2026) | 5 |
| India | RBI Floating Rate Savings Bonds | RBI Retail Direct, bank | - | Rs 1,000 (nv) | 8.05% (H2 2026), slab 35.88%; 7-yr lock (nv) | 2 |
| India | G-secs, SDLs, T-bills | RBI Retail Direct (new), NSE goBID | - | nv | Slab; 10y 7.32%, SDL 7.6-8.15%, T-bill 5.9-6.6% (Nov 2026) | 2 |
| India | Tax-free bonds (secondary) | A (exchange) | - | 1 bond | Interest exempt; yields nv | 3 |
| India | Corporate bonds/NCDs, corporate FDs | OBPP (new), issuer | - | Rs 10k | Slab; credit risk, no DICGC for corporate FDs | 2 |
| India | SGB (secondary only; no new issues since Feb 2024) | A | - | 1 g | Redemption exempt only for original subscribers held to maturity (FA 2026) | 2 |
| India | Gold ETF | A | - | 1 unit | 12 m; 12.5% LTCG | 3 (as part of metals cut) |
| India | Digital gold | apps | - | Rs 10 | 24 m; 3% GST; not SEBI/RBI regulated | 1 |
| India | REITs, InvITs | A | - | 1 unit | Mixed (interest slab, some dividend exempt, debt repayment taxed); units as equity | 3 |
| India | Mainboard IPO / SME IPO | A (UPI ASBA) | - | 1 lot / Rs 1-2 L | As listed shares | 2 / 1 |
| India | International FoFs, GIFT City IFSC funds | MF platforms / LRS | allowed | SIP / fractional | 24 m, 12.5%; no FTC | 1 (already US-heavy) |
| India | PMS / AIF | manager | - | Rs 50 L / Rs 1 Cr | Per security / pass-through | 1 |
| India | P2P lending | platforms | - | nv | Slab; defaults not deductible | 1 |

nv = not verified. Group notes: `ibkr-global.md`, `india-beyond-mf.md`,
`employer-stock-concentration.md`, `us-estate-tax.md`, plus `silver-gold.md`,
`mutual-fund-overlap.md`, `starter-trading-rules.md`.

## 3. Ranked shortlist (proposals for the user)

1. **Cut QCOM/MSFT concentration (60.8%) into Irish accumulating UCITS ETFs at IBKR.** One move
   lowers single-stock risk and US estate tax, and defers tax on dividends: the fund pays 15% US
   withholding and reinvests, with no Indian tax until sale (then 14.95% after 24 months), while
   US-stock dividends are taxed each year at 35.88% (25% US withholding credited against it).
   Order (tax section 5.2): QCOM first, highest-Indian-cost long-term lots first; hold each MSFT
   lot until it turns long-term (first 2027-01-01, main lot 2027-08-16), which saves about
   Rs 1.7 L; sell new MSFT vests at once (gain near zero). Tax if all QCOM sold now: about
   Rs 5.8-5.9 L extra; spreading across years only defers it. CA: lot choice vs FIFO.
   Plan and lot table: `employer-stock-concentration.md`.
2. **Term life cover now** for the US estate tax exposure (about Rs 82.5 L including unvested awards;
   suggested cover about Rs 1 Cr) until the
   US-situs total is near $60k (`us-estate-tax.md`).
3. **Use payroll tax buckets:** check employer NPS 80CCD(2) (up to 14% of salary, new regime) and
   VPF (8.25%, keep own contribution interest within Rs 2.5 L/yr). Low effort, safe, tax-efficient.
4. **AngelOne clean-up (tidying, not a risk fix; MFs are 9.2% of total):** 15 MFs -> 4
   (`mutual-fund-overlap.md`; about Rs 0 tax, about Rs 314 exit load if sold on or after 11 Dec).
   Metals are 3.7% of total, gold only 0.4%: if wanted, sell the ICICI Silver ETF, ICICI Silver
   FoF and Motilal FoF into one gold ETF (Rs 1,97,734) and sell ABSL Silver too; no extra gold, gold about
   3.5% of total incl. jewellery, band 3-6% (your decision 16 Nov; `silver-gold.md`). Tax: `tax/angelone-metals-and-mf-exits.md`.
5. **Park cash in an arbitrage fund, not FDs or bonds:** at a 35.88% slab, equity taxation
   (23.92% / 14.95%) beats interest. Keep IBKR USD cash low (0% on the first $10k; LRS 180-day rule).
6. **Learn to trade small and in a cash account:** fixed Rs 2 L budget, limit orders, stops, paper
   trading first (`starter-trading-rules.md`). Indian stocks/REITs at AngelOne or US stocks at
   IBKR; no stocks under $5 / Rs 50.
7. **Safe debt slice:** EPF (locked) plus Kotak Arbitrage for money needed within 3 years; no PPF (your
   decision 16 Nov 2026: no 15-year lock); gold ETF as in item 4.

**Avoid:** options, futures, event contracts and margin abroad (not allowed under LRS); crypto
(35.88%, no loss set-off, LRS grey); foreign bonds, bond ETFs and US money market funds (may be
taxed as short-term whatever the holding period: CA first); SME IPOs, P2P, digital gold, PMS/AIF;
more US single stocks or international FoFs/GIFT funds (already US-heavy); Asian single stocks
(cost and FX).

## 4. Open questions
- CA (tax section 7): AF s.76 for bond ETFs/MMFs/foreign bonds; SYEP as transfer; lot choice vs
  FIFO; accumulating UCITS no deemed income; surcharge bands.
- User: which IBKR entity and account type (cash or margin, Pro) he has (Client Portal);
  employer NPS/VPF options in payroll; tax regime chosen; existing life cover.
- Not verified: IBKR fractional shares and crypto for Indian residents; PRIIPs/KID block on
  UCITS for IB LLC India clients (expected none); RBI Retail Direct details (site needs JavaScript).
