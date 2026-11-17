# New investments: Indian tax by market (quick reference for plan tax lines)

## Summary

- Quick reference for the one-line tax note in each trading plan (template and examples in section 1).
- Foreign shares/ETFs in any market: LT after 24 months 14.95%, ST 35.88%; dividends 35.88% with credit only up to the treaty rate (reclaim the excess or lose it).
- Indian listed shares and equity MFs: LT after 12 months 14.95% above Rs 1.25 L a year, ST 23.92%; debt MFs and bond ETFs 35.88% however long held.
- New money sent abroad: TCS 20% above Rs 10 L a year (credited against tax); foreign holdings go in Schedule FA; US-listed assets carry US estate tax.

Written 2026-11-15 by `finance-tax` (standing task 5; Work model stage 5). Plan only: no orders.
Not tax advice; former "CA" items are answered in `ca-questions.md`. Detail and the 1961 -> 2025 Act section
map are in `tax/investment-types.md` (section 6); this file does not repeat them.

Taxpayer: Indian resident (ROR), salaried, income about Rs 1.06 Cr before gains, new regime,
tax year 2026-27 (Income-tax Act 2025, "AF s."; Income-tax Rules 2026, "r.").

| Rate | Base | Effective (15% surcharge + 4% cess) |
|---|---|---|
| STCG, Indian listed equity with STT (AF s.196) | 20% | 23.92% |
| LTCG (AF s.197; AF s.198 above Rs 1.25 L for Indian listed equity) | 12.5% | 14.95% |
| Slab: STCG on everything else, dividends, interest | 30% | 35.88% |
| Crypto / VDA (AF s.194 Table Sl.4) | 30% | 35.88% |

Surcharge is 15% for total income Rs 1-2 Cr. Above Rs 2 Cr it rises to 25% (new-regime cap) on
slab income only (slab -> 39.00%); gains under AF s.196/197/198 and dividends stay capped at 15%.
Surcharge rates checked in the Finance Bill 2026 memo (`ca-questions.md`).

## 1. The plan tax line

Template (one line in `trading/plans/<SYMBOL>.md`):

`Tax: <instrument> via <broker>; ST <=<12|24>m <rate>, LT <rate> [exemption]; div <WHT x% (DTAA y%) -> FTC up to y% | slab, TDS>; <transaction taxes>; <LRS TCS | none>; <Schedule FA | none>; <US estate situs yes|no>; <flags>. See tax/new-investments.md#<market>`

ST/LT: "<=24m" means short-term if held 24 months or less; long-term from the day after.

Examples:

1. US stock (e.g. a NASDAQ share) via IBKR:
   `Tax: US stock via IBKR; ST <=24m 35.88%, LT 14.95% (no Rs 1.25 L exemption); div WHT 25% (DTAA 25%, W-8BEN) -> FTC in full via Form 44; no STT (small SEC fee on sells); LRS TCS 20% above Rs 10 L/FY (credited against tax); Schedule FA + FSI + TR; US estate situs YES. See tax/new-investments.md#us`
2. NSE stock via an Indian broker:
   `Tax: NSE stock; ST <=12m 23.92%, LT 14.95% above Rs 1.25 L/FY (shared with all listed equity and equity MFs); div slab 35.88%, TDS 10%; STT 0.1% buy and sell, stamp 0.015% buy; no LRS/FA; no estate situs. See tax/new-investments.md#india`
3. Japan equity ETF (TSE-listed, e.g. a TOPIX ETF) via IBKR:
   `Tax: Japan ETF via IBKR; ST <=24m 35.88%, LT 14.95%; distributions WHT 15.315% (DTAA 10%) -> FTC only 10%, 5.315% lost unless reclaimed from Japan; no transaction tax; LRS TCS 20% above Rs 10 L/FY; Schedule FA + FSI + TR; no US estate situs. See tax/new-investments.md#japan`

## 2. Per market

Indian tax on foreign shares and ETFs is the same everywhere: LT after 24 months at 14.95%, ST at
35.88%, dividends at 35.88% with FTC (AF s.159, r.76, Form 44). The markets differ in the source
withholding (WHT), transaction taxes and estate exposure.

FTC rule (r.76(7)(a)): credit = lower of (foreign tax at the DTAA rate) and (Indian tax on that
income). Since Indian tax on dividends is 35.88%, the full DTAA-rate tax is creditable. Tax withheld
above the DTAA rate is NOT creditable: reclaim it from that country or lose it.

Codes: "src" = treaty rate applied at source by the broker; "reclaim" = domestic rate withheld,
excess reclaimed by a form to the foreign tax office. Whether IBKR applies treaty rates at source
for Indian residents is **unverified** for every market except the US: check the first dividend
on the IBKR activity statement.

### India

| Instrument | LT after / LT rate | ST rate | Dividend / income | Transaction taxes | Notes |
|---|---|---|---|---|---|
| Listed shares, equity ETFs, REIT/InvIT units | >12 m / 14.95% above Rs 1.25 L per FY (AF s.198) | 23.92% (AF s.196) | Slab 35.88%; TDS 10% (AF s.393) | Shares: STT 0.1% buy and sell, stamp 0.015% buy [Z]. Equity ETF: STT 0.001% on sell only (unverified) | STT not deductible (AF s.72(3)(b)); brokerage and stamp are. Buybacks taxed as capital gains (FA 2026) |
| Unlisted shares (pre-IPO, startups) | >24 m / 14.95%, no exemption (AF s.197) | 35.88% | Slab | No STT; stamp 0.015% on transfer (unverified) | Buying below fair value is taxed as other income on the shortfall (1961 s.56(2)(x); AF s.92 clause unverified). Unlisted-shares disclosure in ITR (AY 2025-26 form; TY 2026-27 unverified). Hard to exit |
| Equity MFs (>65% Indian equity) | >12 m / 14.95% above Rs 1.25 L | 23.92% | IDCW at slab | STT 0.001% on redemption [R]; stamp 0.005% on purchase (unverified) | Rs 1.25 L exemption shared with listed shares |
| Debt MFs and bond ETFs (>65% debt), bought from 1 Apr 2023 | Never LT (AF s.76) | 35.88% any holding | Slab | - | Same rule for unlisted bonds and MLDs |
| Gold/silver ETFs (listed) | >12 m / 14.95% | 35.88% | - | No STT [R] | No FA, no LRS |
| Gold/silver/international FoFs (unlisted units) | >24 m / 14.95% | 35.88% | - | - | Outside AF s.76 (not >65% debt) |
| International ETFs listed in India | >12 m / 14.95% | 35.88% | - | - | No FTC (fund pays foreign tax), no Schedule FA, no LRS/TCS, no US estate tax: simplest route to foreign exposure (often at a premium to NAV) |

### US, Europe, Japan, other Asia (foreign shares and ETFs)

All rows: LT >24 m at 14.95%, ST at 35.88%, dividends at 35.88% less FTC; LRS/TCS on the
remittance; Schedule FA, FSI, TR and Form 44. Source-country tax on portfolio share gains: none
found in these markets (not checked treaty by treaty; unverified).

| Market (anchor) | Div WHT: domestic -> India DTAA | FTC usable | At source or reclaim | Transaction taxes (buy / sell) | Estate exposure | Source |
|---|---|---|---|---|---|---|
| US stocks and US-listed ETFs (#us) | 30% -> 25% with W-8BEN | 25% | src (seen at IBKR and Fidelity) | SEC fee on sells only (tiny) | **US-situs**: US estate tax 18-40% above $60k, no Indian credit | [P-US], [ES] |
| PDD Holdings (Nasdaq ADS) | Cayman Islands company (EDGAR and 2025 20-F); head office Dublin since 2023. No dividend paid or planned (20-F). Cayman: no WHT; US: no WHT (non-US company). Irish dividend WHT: not mentioned in the 20-F (Irish tax residence unverified). If ever treated as a PRC resident enterprise: 10% (enterprises) or 20% (individuals) PRC tax on dividends and possibly gains, treaty relief unclear (20-F) | Nothing now | - | SEC fee on sells | **Not US-situs** (non-US company; ADR situs unsettled, common view not US-situs) | [PDD-20F] |
| UK shares (#europe) | 0% | - | - | Stamp duty/SDRT 0.5% on buys of UK shares [P-UKo]; ETFs and AIM shares exempt (unverified) | UK inheritance tax on UK-situs assets possible (unverified) | [P-UK] |
| Germany | 26.375% -> 10% | 10% | reclaim 16.375% from BZSt (slow) | None found | - | [P-DE] |
| France (e.g. TotalEnergies, Dassault Systemes) | 12.8% for individuals; 25% for companies (PwC non-treaty 0/25) -> 10% (see Europe note) | 10% | If 12.8%: 2.8% lost unless reclaimed. If the nominee chain does not identify you as an individual, 25% may be withheld and 15% is lost unless reclaimed (Forms 5000/5001, unverified). Which rate IBKR gets: **unverified - check the first dividend's withholding line in the IBKR activity statement** (no source found on IBKR or omnibus practice) | FTT 0.4% on buys of French listed shares [P-FRo]; only companies above EUR 1 bn market value (threshold unverified; TTE and DSY far above) | - | [P-FR] |
| Spain (e.g. BBVA) | 19% -> 15% | 15% | reclaim 4% from Spain (process unverified) or lose it; 19% seen on the BBVA Oct 2026 dividend (research/stocks/BBVA.md) | FTT 0.2% on buys of listed Spanish shares with market value above EUR 1 bn on 1 Dec of the prior year [P-ESo]; nothing on sells | - | [P-ES] |
| Netherlands (e.g. Wolters Kluwer, Arcadis) | 15% -> 10% (PwC lists India 10/15, note: "based upon the most-favoured nation principle"; after Nestle (SC 2023) use the treaty's own 10%, portfolio rate unverified against the treaty text) | 10% | reclaim 5% from the Dutch tax office (form IB 92, unverified) or lose it; IBKR's applied rate unverified | None (no stamp duty) [P-NLo] | - | [P-NL] |
| Switzerland | 35% -> 10% (MFN cut to 5% revoked) | 10% | reclaim 25% from Swiss tax office | Swiss turnover tax 0.15%/0.3% only if a Swiss dealer is party (not IBKR; unverified) [P-CHo] | - | [P-CH] |
| Italy | 26% -> 25% portfolio (15% only for >=10% holdings) | 25% | reclaim 1% (not worth it) | FTT 0.2% on buys on a regulated market (0.4% OTC) [P-ITo] | - | [P-IT] |
| Ireland: Irish company shares | 25% -> 10% | 10% | reclaim 15% | Irish stamp duty on Irish shares (1%, unverified) | - | [P-IE] |
| Ireland: UCITS ETFs (LSE/Xetra) | 0% on ETF distributions | - | - | No UK stamp on ETFs (unverified) | **Not US-situs** (the US-estate fix) | [IR] |
| Japan (#japan) | 15.315% listed (15% + 2.1% surtax) -> 10% | 10% | reclaim 5.315% unless IBKR applies 10% (unverified) | None (Japan stamp duty only on paper documents) [P-JPo] | Japan inheritance tax on Japan assets (unverified) | [P-JP], [IR] |
| Hong Kong (#other-asia) | 0% | - | - | Stamp duty 0.2% per deal, 0.1% each side [P-HKo] (split and ETF exemption unverified) | - | [P-HK] |
| Singapore (e.g. iFAST) | 0% (one-tier; India DTAA not needed) | - (nothing to credit) | - | No stamp on scripless SGX trades (unverified) | - | [P-SG] |
| China H-shares in Hong Kong (e.g. WuXi AppTec 2359.HK) | 10% PRC enterprise income tax: H shares held through HKSCC Nominees or any nominee (as at IBKR) are treated as held by a non-resident enterprise and 10% is withheld [HKX-WX] (China law rate for individuals is 20% [P-CNi]) -> India-China DTAA 10% | 10% | none (10% withheld = treaty rate) | HK stamp 0.2% per deal, 0.1% each side [P-HKo] | - | [P-CN], [HKX-WX] |
| Hong Kong-listed Cayman/BVI Chinese companies (e.g. ANTA 2020, NetEase 9999, China Resources Mixc 1209) | 0%: HK has no WHT, and the latest HKEX dividend forms of all three say withholding tax "Not applicable" [HKX-CN]. A company recognised as a PRC tax-resident enterprise (TRE) would withhold 10% from nominee-held shares like H shares; check the "Information relating to withholding tax" box on each new HKEX dividend form -> India-China DTAA 10% if withheld | 10% if withheld, else nothing | none | HK stamp 0.2% per deal [P-HKo] | - | [HKX-CN], [P-HK] |
| South Korea | 22% (20% + 10% local tax) -> 16.5% (15% + local) | 15% (local-tax part unverified) | unverified | Securities transaction tax 0.20% on sells from 1 Jan 2026 [P-KRo] | - | [P-KR] |
| Taiwan | 21% -> 12.5% | 12.5% | unverified | Securities transaction tax 0.3% on sells [P-TWo] (ETF 0.1%, unverified) | - | [P-TW] |
| China A-shares via HK Stock Connect | 10% -> 10% | 10% | 10% at source (unverified for Connect) | Mainland stamp 0.05% on sells (unverified) | - | [P-CN] |
| Australia (e.g. Pro Medicus) | Franked part 0%; unfranked part 30% (0% if declared conduit foreign income) -> 15% | 15% on the unfranked part only | treaty 15% at source if the broker has your treaty residence, else reclaim 15% from the ATO (process unverified); Pro Medicus franking level unverified (check the dividend statement) | None found | - | [P-AU] |
| Poland (e.g. Benefit Systems, LPP; not Zabka, see Luxembourg) | 19% -> 10% | 10% | 10% at source needs a residence certificate with the Polish payer/custodian (unverified); else reclaim 9% from the Polish tax office (process unverified) | Civil-law transactions tax 1% on sales of property rights (shares) [P-PLo]; exemption for exchange trades through brokers not found on PwC (unverified) | - | [P-PL], [P-PLo] |
| Luxembourg company listed in Warsaw (e.g. Zabka, ZAB) | Luxembourg 15% -> India-Luxembourg DTAA 10% (portfolio) [P-LU] | 10% | reclaim 5% from Luxembourg (process unverified) or lose it | Polish civil-law tax: as Poland row (unverified for a Luxembourg company) | - | [P-LU]; domicile research/stocks/ZAB.md. Being taken over (tender ends 2026-12-02): dividends moot |
| Sweden (e.g. Evolution) | 30% non-resident individuals (not 15%) -> 10% | 10% | reclaim 20% from Skatteverket (form SKV 3740, unverified) or lose it; 10% at source only if IBKR registers treaty status (unverified) | No stamp duty on shares (stamp duty only on real estate) [P-SEo] | - | [P-SE] |
| Bermuda (e.g. RenaissanceRe RNR, NYSE-listed) | 0% (no Bermuda WHT; verified PwC 16 Oct 2026); no India-Bermuda DTAA (unverified), none needed | - (nothing to credit) | - | US SEC fee on sells (NYSE trade); no Bermuda transfer tax [P-BMo] | **Not US-situs**: shares of a non-US company (IRC 2104(a) covers US-company stock only; unverified against the code text) | [P-BM], [P-BMo] |
| Guernsey (e.g. FSG, LSE-listed) | 0%: no WHT on dividends to non-residents (non-treaty 0%; WHT only on Guernsey-resident individuals) [P-GG]; no India-Guernsey DTAA needed | - (nothing to credit) | - | UK stamp duty/SDRT: generally none for a non-UK company whose register is kept outside the UK, incl. CREST depository interests over such shares (unverified for FSG; check the contract note) | Guernsey has no inheritance tax; shares of a Guernsey company are not UK-situs for UK IHT (unverified) | [P-GG] |
| Canada (e.g. Fairfax FFH, TSX) | 25% Part XIII -> India-Canada DTAA 25% for portfolio holders (15% only for companies holding 10%+) [P-CA] (treaty Art.10 text not opened) | 25% (capped at Indian tax on it, 35.88%) | Nothing to reclaim (withheld = treaty rate) | None found | No Canadian estate tax; the deemed sale at death for non-residents hits only taxable Canadian property, which listed shares are not unless 25%+ owned (unverified) | [P-CA] |
| Cyprus (e.g. THEON International, Euronext Amsterdam) | 0% (Cyprus has no WHT on dividends to non-residents; only to companies in EU-blacklisted or low-tax places) [P-CY]; India-Cyprus DTAA rate (2016 treaty) not needed (unverified) | - (nothing to credit) | - | None: no Dutch stamp duty or FTT on Euronext Amsterdam [P-NLo]; Cyprus stamp duty abolished from 1 Jan 2026 [P-CYo] | - | [P-CY], [P-CYo] |
| Kazakhstan via LSE GDR (e.g. Kazatomprom, KAP) | 15% general rate (5% only for >=25% holders) -> India-Kazakhstan DTAA 10%. Exemption for dividends on securities listed on a Kazakh exchange (KASE/AIX) with active trading [P-KZ]: KAP shares and GDRs are AIX-listed, and PwC ties the exemption to the security, not the holder, so GDR dividends may be paid gross - **open**: KAP's FY2024/FY2025 dividend notices give no rate; GDR dividends are paid by Citibank "net of the Depositary's fees, taxes, duties and charges, if any" [KAP-RNS]; Citi's notice not reachable | 10% if withheld at 15% (5% lost unless reclaimed via Citibank's treaty process, unverified); nothing if exempt | Check the first dividend (record date late July) on the IBKR statement | No Kazakh transfer or stamp tax [P-KZo]; UK stamp duty/SDRT applies to UK shares, so not to GDRs over Kazakh shares (unverified) | - | [P-KZ], [P-KZo], [KAP-RNS] US estate tax: the GDR has a US ISIN (US depositary bank), but it represents shares of a Kazakh company; the common view is not US-situs (as ADRs of foreign companies, global-actions row 14), unsettled. |

Access: whether IBKR lets an Indian resident trade Korea, Taiwan and China Connect is
**unverified** (finance-research to check). A US-listed ADR of a foreign company carries that
company's home WHT (not US 25%) plus a depositary fee; its US estate-tax situs is unsettled, common view not US-situs (`global-actions-2026-11.md` #14).

Bond funds anywhere (UCITS bond ETFs, US bond ETFs, money-market funds) may fall in AF s.76 ->
always ST at 35.88%: likely (`ca-questions.md`).

## 3. Cross-market rules

| Topic | Rule | Source |
|---|---|---|
| LRS limit | USD 250,000 per person per FY, all purposes together. No margin, no derivatives, no remitting margin calls abroad under LRS; buy only cash equities/ETFs | RBI LRS FAQ / Master Direction ([S], RBI site behind CAPTCHA, not re-fetched) |
| LRS idle cash | Unused remitted funds to be brought back in 180 days; whether that covers broker cash/sale proceeds is unclear | [R] (AD bank in writing) |
| TCS (1961 s.206C(1G) -> AF s.394) | 20% on investment remittances above Rs 10 L per FY (all banks together); below Rs 10 L nil. FA 2026 cut only education/medical to 2% | FA 2026 Memorandum [M] via [IR] |
| TCS is not a cost | Shown in Form 26AS/AIS; credited against the year's tax (advance tax or return) or refunded; can be shown to the employer to reduce salary TDS (Form No. 122, AF s.392(4)) | [R] |
| FX conversion | Capital gains on foreign shares: SBI TT buying rate (1961 Rule 115 -> r.206; r.207 defines the rate); practice: rate on the last day of the month before the sale month and before the purchase month. FTC: TT buying rate on the last day of the month before the tax was deducted (r.76(7)(b)) | [R], [IR] |
| Schedule FA | Every foreign account and holding at any time in the **calendar year** (CY 2026 in the TY 2026-27 return), even if sold or nil | [R] |
| FSI and TR | Foreign income by country, and tax paid/credit claimed | [R] |
| Form 44 (ex-Form 67) | Within 12 months from the end of the tax year (r.76(10),(12)), with an on-time return; accountant must verify it if foreign tax is Rs 1 L or more (r.76(16)) | [R] |
| Set-off (AF s.108) | ST loss against any gain; LT loss only against LT gains; never against salary (AF s.109) | [R] |
| Carry-forward (AF s.111) | 8 tax years, same split, only if the return is filed by the due date (31 Jul for non-audit) | [R] |
| Order of set-off | No fixed order; you fill the Schedule CG set-off table, so put ST losses against the highest-taxed gains first (likely) | [R] |
| Wash sale | None in India: sell to book a loss and rebuy at once is allowed. US wash-sale rule does not apply to a non-resident alien | [R] |
| Lot choice | Demat in India: FIFO by law (AF s.67(7)). Foreign shares: specific-lot choice not settled (FIFO where lots cannot be identified); handled in `employer-stock.md`; one rule every year | [R], `investment-types.md` 5.2 |
| Black Money Act | Undisclosed foreign asset: Rs 10 L penalty; no penalty if non-property foreign assets total up to Rs 20 L (from 1 Oct 2024; likely); FA 2026: no prosecution up to Rs 20 L | [R], [IR] |
| US estate tax | Non-resident alien with US-situs assets above $60,000 at death: Form 706-NA, 18-40%, no Indian credit. US shares and US-listed ETFs count; Irish UCITS, US bank deposits do not | [IRS-E] |
| Advance tax | Tax on a gain is due in the next instalment (15 Jun, 15 Sep, 15 Dec, 15 Mar); no AF s.425 interest if paid in the instalments after the gain | [R] |

## 4. Holding period quick table

| Rule | What | LT rate | ST rate |
|---|---|---|---|
| LT after 12 months | Listed in India: shares, equity MFs, ETFs listed in India, REIT/InvIT units, listed bonds | 14.95% (above Rs 1.25 L for equity with STT) | 23.92% equity with STT; 35.88% others |
| LT after 24 months | Everything else: all foreign shares and ETFs (incl. Irish UCITS), unlisted shares, unlisted FoFs (gold, silver, international), digital gold | 14.95%, no exemption | 35.88% |
| Always ST (AF s.76, ex-s.50AA) | MFs or "funds by whatever name" with >65% debt (bought from 1 Apr 2023), unlisted bonds, market-linked debentures | - | 35.88% |
| Flat (AF s.194 Table Sl.4) | Crypto / VDA | 35.88% | 35.88%, no set-off, no carry-forward |

Short-term asset definition: AF s.2(101) (ex-s.2(42A)).

## 5. Market notes

### India
Cheapest on tax for LT gains (Rs 1.25 L yearly exemption, 12-month clock). No FTC, FA or TCS work.

### US
25% dividend WHT is fully credited, so dividends cost the slab rate, no extra. Main cost is estate
exposure; for long holds above $60k total, prefer Irish UCITS ETFs for broad funds.

### Europe
Prefer Irish UCITS ETFs (0% Irish WHT; the fund still suffers WHT inside). For single shares,
Germany, Switzerland, Spain and France withhold above the treaty rate: either reclaim or accept the loss.
UK buys cost 0.5% stamp; France (0.4%), Spain (0.2%) and Italy (0.2%) charge FTT on buys.

France rate: domestic 12.8% for individuals [P-FR]. The India-France DTAA dividend rate is 10%.
PwC lists India as 5/10/15 with notes that the clause is modified by the most-favoured-nation
(MFN) clause and that a new protocol is signed but not in force [P-FR]. After the Supreme Court
Nestle ruling (Oct 2023: MFN needs an Indian notification), use 10%. Which rate IBKR withholds for
an Indian-resident individual is **unverified - check the first dividend's withholding line in the
IBKR activity statement**.

Worked example, per EUR 100 gross dividend (France at 12.8%; Spain at 19% for comparison):

| Step | France (TTE) | Spain (BBVA) |
|---|---|---|
| Foreign WHT | 12.80 | 19.00 |
| Indian tax at 35.88% | 35.88 | 35.88 |
| FTC (DTAA rate, below Indian tax) | 10.00 | 15.00 |
| Indian tax still payable | 25.88 | 20.88 |
| Total tax | 38.68 (35.88 if 2.80 reclaimed) | 39.88 (35.88 if 4.00 reclaimed) |
| Lost unless reclaimed | 2.80 | 4.00 |

### Japan
No transaction tax; 5.315% of each dividend is lost unless reclaimed. Low-yield growth shares
make this small.

### Other Asia
Hong Kong and Singapore: no WHT. Korea and Taiwan: transaction tax on each sale (0.20%, 0.3%) and
WHT above India's credit if the treaty is not applied at source; avoid frequent trading there.

## 6. Former questions for a CA (answers in `ca-questions.md`)

1. Finance Act 2026 surcharge rates: confirm 15% for Rs 1-2 Cr and the 15% cap on AF s.196/197/198 gains and dividends.
2. Rule 115 -> r.206 or r.207; which TT rate date for cost of foreign shares.
3. Specific-lot identification vs FIFO for foreign shares.
4. Bond UCITS/US bond ETFs/MMFs under AF s.76.
5. Are foreign transaction taxes (UK stamp, FTT, Taiwan/Korea STT, HK stamp) deductible as transfer cost under AF s.72 (only Indian STT is barred)?
6. Unlisted Indian shares bought below fair value: AF s.92 clause and valuation rule.
7. Can an excess-WHT reclaim be skipped and FTC claimed at the treaty rate only (yes per r.76(7)(a)); any issue if the reclaim is never filed?
8. LRS 180-day rule for sale proceeds held at the broker.
9. Korea: is the 10% local income tax creditable as income tax under the treaty?
10. TCS credit against salary TDS: the 2025 Act form and procedure.
11. France: confirm 10% (not 5%) as the DTAA dividend rate for FTC after Nestle, and whether the reclaim of 2.8% is worth filing.

## 7. Sources (all checked 2026-11-15 unless noted)

PwC Worldwide Tax Summaries, withholding-tax pages (URL pattern
`https://taxsummaries.pwc.com/<country>/corporate/withholding-taxes`) and other-taxes pages
(`.../corporate/other-taxes`, marked "o"); "last reviewed" date as shown by PwC:
- [P-US] united-states, 4 Sep 2026. [P-UK]/[P-UKo] united-kingdom, 23 Jul 2026.
- [P-DE] germany, 30 Jun 2026. [P-FR]/[P-FRo] france, 24 Apr 2026. [P-NL]/[P-NLo] netherlands, 29 May 2026.
- [P-ES]/[P-ESo] spain, 30 Jun 2026 (India: 15% dividends; FTT 0.2% above EUR 1 bn).
- [P-CH]/[P-CHo] switzerland, 1 Jul 2026 (India note on the MFN reversal). [P-IT]/[P-ITo] italy, 13 Jul 2026.
- [P-IE] ireland, 11 Aug 2026. [P-JP]/[P-JPo] japan, 7 Aug 2026. [P-HK]/[P-HKo] hong-kong-sar, 22 Jul 2026.
- [P-SG] singapore, 2 Jul 2026. [P-KR]/[P-KRo] republic-of-korea, 4 Jun 2026. [P-TW]/[P-TWo] taiwan, 20 Aug 2026.
- [P-CN] peoples-republic-of-china, 22 Jul 2026. [P-AU] australia, 12 Oct 2026.
- Checked 2026-11-17: [P-PL]/[P-PLo] poland, 11 Aug 2026 (dividends 19%, India 10%; PCC 1%). [P-SE]/[P-SEo] sweden, 22 Sep 2026 (non-treaty 30%, India 10%). [P-BM]/[P-BMo] bermuda, 16 Oct 2026 (no WHT, no transfer tax). [P-CNi] China individual income tax, 22 Jul 2026 (20% flat on dividends). [P-NL] note 32 and [P-AU] re-read 2026-11-17.
- Checked 2026-11-17: [P-CY]/[P-CYo] cyprus, 4 Aug 2026 (no WHT on dividends to non-residents; stamp duty abolished 1 Jan 2026). [P-KZ]/[P-KZo] kazakhstan, 23 Jul 2026 (dividends 15%, India 10%, exemption for KASE/AIX-listed securities; no transfer or stamp taxes).
- Checked 2026-11-17: [PDD-20F] PDD Holdings 20-F for 2025 (filed 2026-04-29) and EDGAR company data (incorporation: Cayman Islands; business address Dublin), https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001737806. [HKX-WX] WuXi AppTec cash dividend announcement 29 Apr 2026, https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0429/2026042900579.pdf. [HKX-CN] HKEX dividend forms: ANTA 26 Aug 2026 (.../sehk/2026/0826/2026082600225.pdf), NetEase 20 Aug 2026 (.../sehk/2026/0820/2026082000505.pdf), China Resources Mixc 31 Aug 2026 (.../sehk/2026/0831/2026083100103.pdf), all "Not applicable". [KAP-RNS] Kazatomprom RNS 25 Jul 2025 (FY2024 payment) and 28 May 2026 (FY2025 approval), https://www.investegate.co.uk/company/KAP.
- Checked 2026-11-17: [P-CA] canada, 12 Jun 2026 (25%; India 15/25). [P-LU] luxembourg, 31 Jul 2026 (15%; India 10% portfolio). [P-GG] guernsey, 21 Sep 2026 (non-resident 0%). PTC is a US company (research/stocks/PTC.md): US row applies, no dividend.
- [Z] Zerodha charges (secondary): https://zerodha.com/charges (STT 0.1% delivery buy and sell; stamp 0.015% buy).
- [M] Finance Bill 2026 Memorandum: https://www.indiabudget.gov.in/doc/memo.pdf
- [IRS-E] https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
- [IR] work note `invrules.md`, [R] work note `rules.md` (finance-tax-migration, Nov 2026): 2025 Act and Rules 2026 text (GitHub abaasairam-ai/income-tax-rag), IRS Pub 515.
- [ES] work note `empstock.md`: 25% US WHT seen on IBKR and Fidelity 1042-S.
- [S] `research/sources.md` (RBI LRS FAQ, 2026-11-15).
- Not opened in this run: IBKR withholding pages, treaty texts (incometaxindia.gov.in returns 403), RBI pages.
