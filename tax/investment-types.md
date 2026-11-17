# Investment types: Indian tax for a resident salaried individual, tax year 2026-27

## Summary

- Reference: Indian tax per investment type for 2026-27 at your rates (LT 14.95%, Indian equity ST 23.92%, slab and crypto 35.88%).
- Biggest flags: bond/money-market ETFs and foreign bonds may be short-term at 35.88% however long held (likely: plan on it, `ca-questions.md`); SGBs bought on the market are taxed on redemption; crypto 35.88% with no loss set-off.
- Prefer Irish UCITS ETFs to US-listed ETFs: no US estate tax (US assets above $60,000) and no withholding on distributions vs 25% US withholding on dividends.
- Employer stock: sell QCOM first, highest-cost long-term lots first (all QCOM: about Rs 5.9 L extra tax); hold each MSFT lot until it turns long-term (saves about Rs 1.7 L; about Rs 1.08 L net after the losses).

Written 2026-11-15 by `finance-tax` for `finance-research`. Plan only: no orders. Not tax advice;
former "CA" items are answered in `ca-questions.md`.

Tax year 2026-27 = 1 Apr 2026 - 31 Mar 2027, under the Income-tax Act 2025 ("AF s.") and the
Income-tax Rules 2026 ("r."); the 1961 section is given first where useful. Section numbers come
from the 2025 Act and Rules 2026 text (repo abaasairam-ai/income-tax-rag) unless marked
"(unverified)" [IR]. Employer-stock figures: yfinance closes of 13 Nov 2026, FX approx [ES].

Rates used (income about Rs 1.06 Cr before gains [ES 0.1], so a 15% surcharge applies; on
s.111A/112/112A gains the surcharge is capped at 15%; 4% cess):

| Rate | Base | With 15% surcharge + 4% cess |
|---|---|---|
| LTCG (AF s.197 / s.198) | 12.5% | 14.95% |
| STCG on listed Indian equity with STT (AF s.196) | 20% | 23.92% |
| Slab (STCG on foreign assets, interest, dividends) | 30% | 35.88% |
| Crypto (AF s.194 Table Sl.4) | 30% | 35.88% |

Surcharge rates checked in the Finance Bill 2026 memo (`ca-questions.md`). Above Rs 2 Cr total
income the surcharge on slab income rises to 25%; LTCG stays at 15% [ES 0.1].

## 0. Short answer

1. **Bond ETFs, money-market funds and foreign bonds**: s.50AA / AF s.76 may make every gain
   short-term at 35.88%, whatever the holding period ("Mutual Fund by whatever name" with >65%
   debt; "unlisted bond"). Likely caught: plan on always-ST (`ca-questions.md`) [IR].
2. **IBKR share lending (SYEP)**: foreign lending is outside the SEBI/RBI SLB exclusion (AF
   s.70(1)(zg)), so it may count as a sale and reset the holding period. IBKR says IB India
   clients are not eligible anyway [IR].
3. **SGB**: from 2026-27 the redemption exemption applies only to original subscribers who hold
   to maturity (Finance Act 2026). Secondary-market buyers are taxed on redemption [IR].
4. **Crypto**: 30% flat (35.88% here), only cost deductible, losses cannot be set off or carried
   forward [IR].
5. **US estate tax**: US shares and US ETFs above $60,000 at death -> US estate tax 18-40%, with
   no Indian credit (no treaty) [IR].
6. **Irish UCITS ETFs** are not US-situs (no US estate tax), and Ireland withholds nothing on their
   distributions to you; US-listed ETFs suffer 25% US withholding on dividends [IR].
7. All foreign shares/ETFs: long-term after 24 months at 14.95%, short-term at 35.88%; no Rs 1.25 L
   exemption; FTC via AF s.159, r.76, Form 44 within 12 months of year end [IR].
8. **Employer stock**: sell QCOM (98% LT by value) before MSFT (100% ST today); holding MSFT lots
   to LT saves about Rs 1.7 L at 13 Nov 2026 prices [ES]. See section 5.

## 1. Held via IBKR (foreign)

LT = long-term after; FTC = foreign tax credit (AF s.159 / r.76 / Form 44); FA = Schedule FA
(calendar year); FSI/TR = foreign income and tax relief schedules.

| Item | Indian tax on income | LT after / LT rate / ST rate | Foreign withholding and FTC | Reporting | Flags (CA) |
|---|---|---|---|---|---|
| Irish UCITS ETF, distributing | Dividend, other sources (AF s.92), slab. No interest deduction against dividends (AF s.93(2), FA 2026) | 24 m / 12.5% (AF s.197) / slab | Ireland 0%, so no FTC | FA A3; CG schedule | Bond UCITS: AF s.76(5)(b) risk (all gains ST) |
| Irish UCITS ETF, accumulating | None until sale (no deemed-distribution rule found) | 24 m / 12.5% / slab | None | FA A3 (income accrued nil) | "No deemed income" inferred from absence of a rule |
| US stocks and ETFs | Dividends at slab | 24 m / 12.5% / slab | US 25% with W-8BEN (DTAA Art.10); FTC up to Indian tax on it | FA A3, FSI, TR, Form 44 | US-situs (section 4). US bond ETF: AF s.76 risk |
| Japan stocks | Dividends at slab | 24 m / 12.5% / slab | 15.315% withheld; treaty 10%; FTC capped at 10%, reclaim rest from Japan | FA A3, FSI, TR, Form 44 | IBKR's applied rate: check the first dividend |
| Germany stocks | Dividends at slab | 24 m / 12.5% / slab | 26.375% withheld; treaty 10%; reclaim 16.375% from BZSt | FA A3, FSI, TR, Form 44 | Reclaim slow, paper-heavy |
| Hong Kong stocks | Dividends at slab | 24 m / 12.5% / slab | 0% | FA A3 | - |
| Canada stocks | Dividends at slab | 24 m / 12.5% / slab | Canada withholds 25%; India-Canada DTAA rate 25% for portfolio holders, so the full 25% is credited (capped at Indian tax), nothing to reclaim | FA A3, FSI, TR, Form 44 | Other countries: see `new-investments.md` per-market table |
| US Treasuries, T-bills | Interest at slab | 24 m / 12.5% / slab (T-bill sale always ST) | 0% (portfolio interest; <=183-day OID exempt, IRS Pub 515) | FA A3 | Discount: interest vs gain unsettled; "unlisted bond" AF s.76(2)(b) risk |
| US corporate bonds | Interest at slab | Possibly always ST (AF s.76(2)(b)) | 0% if registered (Pub 515), else 15% (Art.11) | FA A3 | High AF s.76 risk |
| US municipal bonds | Interest taxable at slab (US exemption does not carry over) | As corporate bonds | 0% | FA A3 | - |
| US bank CDs | Interest at slab | Usually held to maturity | 0% (bank deposits incl. CDs, Pub 515) | FA A1 or A3 | - |
| US money-market funds | Dividends at slab | 24 m / 12.5% / slab, but probably always ST (>65% debt, AF s.76) | 25%; 871(k) interest dividends exempt if designated (IBKR practice not verified) | FA A3, FSI, TR | Probably caught by AF s.76 |
| IBKR interest on cash | Interest at slab | - | Usually exempt for a nonresident (likely); check 1042-S | FA A2; FSI if tax withheld | - |
| SYEP (share lending) | Fee and substitute dividends at slab | **May be a transfer** (outside AF s.70(1)(zg)) | US tax on substitute dividends (Pub 515) | FA A3, FSI, TR | IB India clients not eligible |
| IBKR crypto | 30% (AF s.194 Table Sl.4) | Flat 30%, any holding period | None; 1% TDS (AF s.393(1) Table Sl.8(vi)) only on Indian payers | Schedule VDA; FA placement unclear | Indian residents may not be eligible |

## 2. India investments

| Item | Indian tax on income | LT after / LT rate / ST rate | Reporting | Flags (CA) |
|---|---|---|---|---|
| Sovereign Gold Bonds | 2.5% interest at slab, no TDS | Redemption exempt (AF s.70(1)(x)) only for original subscribers held to maturity (FA 2026). Exchange sale: 12 m / 12.5% / slab | CG schedule | Does the 5-year early redemption count? Probably not |
| RBI Floating Rate Savings Bonds | Interest at slab; TDS (AF s.393(1) Table Sl.5(i), above Rs 10,000) | Not transferable | - | - |
| G-secs/T-bills (RBI Retail Direct) | Interest at slab | Listed: 12 m / 12.5% / slab | CG / other sources | T-bill discount: interest vs gain unsettled |
| Listed corporate bonds/NCDs | Interest at slab; TDS 10% | 12 m / 12.5% / slab | - | Unlisted bonds and MLDs: always ST (AF s.76(2)) |
| Tax-free bonds (secondary) | Interest exempt (1961 s.10(15)(iv)(h); Schedule II row unverified) | Listed: 12 m / 12.5% / slab | Exempt income | - |
| Corporate FDs | Interest at slab; TDS (AF s.393(1) Table Sl.5) | - | - | - |
| PPF | Exempt (Schedule II Sl.3); deposit deduction AF s.123 old regime only | - | Exempt income | - |
| NPS Tier 1 | New regime: only employer NPS, up to 14% of basic (AF s.124(1)-(2), s.202(2)(a)(xii)); keep PF + NPS within Rs 7.5 L (about 12.3% of basic now; saves about Rs 1.36 L/yr), see `tax/FY2026-27/employer-nps.md` | Exit 60% lump sum exempt (Schedule II); annuity at slab (AF s.124(6)) | - | PFRDA allows up to 80% lump sum (FAQ Mar 2026); tax text still 60% |
| NPS Tier 2 | No deduction (private sector) | Unclear | - | CA |
| EPF/VPF | New regime: no deduction (AF s.123 old regime only); interest on employee contribution above Rs 2.5 L/yr taxable at slab (Schedule II Sl.4; old Rule 9D -> r.277), already passed, so VPF earns about 5.3% after tax; see `tax/FY2026-27/employer-nps.md` | - | Other sources | Employer PF+NPS+super above Rs 7.5 L is a perquisite (AF s.17(1)(h)) |
| REIT/InvIT units | SPV interest at slab; SPV dividend exempt if SPV not in s.115BAA (Schedule V); debt repayment taxed (AF s.92(2)(k)) | 12 m / 12.5% above Rs 1.25 L (AF s.198) / 20% (AF s.196) | - | Other receipts reduce cost (AF s.72(4)) |
| Indian listed shares, IPOs | Dividends at slab (TDS 10%) | 12 m / 12.5% above Rs 1.25 L / 20% | - | Buybacks now taxed as capital gains (FA 2026) |
| Indian international FoFs | - | Unlisted: 24 m / 12.5% / slab | - | Outside AF s.76 (">65% debt" test); no FTC |
| Listed international ETFs (India) | - | 12 m / 12.5% / slab | - | No FTC (fund pays foreign tax) |
| GIFT City IFSC funds | Distributions at slab | 24 m / 12.5% / slab | Probably not FA | Whether IFSC = "recognised exchange in India" unsettled |
| PMS | Per underlying security | Per security | - | Fees generally not deductible |
| AIF Cat I/II | Pass-through (AF s.224) | Per income type | - | Cat III taxed at fund level |
| P2P lending | Interest at slab; TDS (unverified) | Defaults not deductible | - | - |
| Digital gold | - | 24 m / 12.5% / slab | - | 3% GST; not SEBI/RBI regulated |

## 3. Crypto and foreign derivatives

| Item | Tax | Losses | Withholding | Reporting | Flags |
|---|---|---|---|---|---|
| Crypto (VDA, AF s.2(111)) | 30% + surcharge + cess = 35.88% (AF s.194 Table Sl.4); only cost deductible | No set-off against anything, no carry-forward | 1% TDS only with an Indian payer | Schedule VDA; FA (Table A3 or D) common, no CBDT ruling | FA placement |
| Foreign derivatives | Business income; may be **speculative** (non-speculative carve-out covers only Indian exchanges) | Speculative losses only against speculative income, 4-year carry-forward (AF s.113) | Possible US 871(m) on dividend equivalents | ITR-3 | RBI LRS bars sending margin abroad |

## 4. US estate tax

| Item | Rule |
|---|---|
| Who | A nonresident alien who dies holding US-situs assets |
| Threshold | Form 706-NA if US-situs assets > **$60,000**; rates 18-40% (IRS) |
| India | No estate tax; no credit for US estate tax (no treaty; AF s.159/160 cover income tax only) |
| US-situs | US shares (incl. QCOM, MSFT), US-listed ETFs |
| Not US-situs | Irish UCITS ETFs, US bank deposits (IRC 2105(b)(1)), portfolio-interest debt (IRC 2105(b)(3)) |
| Exposure today | QCOM approx $131,250 + MSFT approx $61,235 [ES, 13 Nov 2026 closes] = about $192,500, over 3x the threshold |

Selling employer stock into Irish UCITS removes this risk; probate friction remains below $60k.

## 5. Employer stock concentration (QCOM, MSFT)

Moved to [employer-stock.md](employer-stock.md) (2026-11-15): staged QCOM/MSFT sale plan, lot order,
Rs 2 Cr surcharge step, advance tax for the sales and the Microsoft ESPP restart.

## 6. Section mapping (1961 -> 2025 Act / Rules 2026)

| 1961 | 2025 Act / Rules 2026 | Topic |
|---|---|---|
| s.2(42A) | s.2(101) | Short-term capital asset |
| s.2(47) | s.2(109) | Transfer |
| s.2(47A) | s.2(111) | Virtual digital asset |
| s.17(2)(vii) | s.17(1)(h) | Employer PF/NPS above Rs 7.5 L |
| s.45(2A) | s.67(7) | Demat beneficial owner, FIFO |
| s.47 | s.70 | Not a transfer: SGB (x), SLB (zg) |
| s.48 | s.72 | Cost deductions |
| s.49(2AA) | s.73 Table Sl.4 | ESOP/RSU cost = FMV taxed as perquisite |
| s.50AA | s.76 | Specified MF / MLD / unlisted bonds always ST |
| s.56 / s.57 | s.92 / s.93 | Other sources |
| s.70 / 71 / 74 | s.108 / 109 / 111 | Loss set-off, carry-forward |
| s.80C | s.123 + Schedule XV | Old regime only |
| s.80CCD | s.124 | NPS |
| s.90 / s.91 | s.159 / s.160 | Foreign tax credit |
| s.111A / 112 / 112A | s.196 / 197 / 198 | 20% / 12.5% / 12.5% above Rs 1.25 L |
| s.115BAC | s.202 | New regime |
| s.115BBH | s.194 Table Sl.4 | Crypto 30% |
| s.115UB | s.224 | AIF pass-through |
| s.194A, 194S | s.393 | TDS |
| s.206C(1G) | s.394 | TCS on LRS |
| s.211 / 234C | s.408 / 425 | Advance tax, interest |
| Rule 9D | r.277 | EPF interest |
| Rule 115 | r.206 | SBI TT buying rate (defined in r.207) on the last day of the month before the transfer month (r.206 Table Sl.6; read 2026-11-15) |
| Rule 128, Form 67 | r.76, Form 44 | FTC; Form 44 within 12 months of year end |

## 7. Former questions for a CA (answers in `ca-questions.md`)

1. Do bond UCITS/US bond ETFs, US MMFs and foreign bonds fall in AF s.76 (always ST)?
2. Is foreign share lending (SYEP) a transfer?
3. Specific-lot identification vs FIFO for QCOM at IBKR; method A vs method B cost for past
   sell-to-cover sales.
4. Indian cost: use Form 16 perquisite values instead of yfinance FX (Qualcomm Form 16s not found).
5. Surcharge rates in the Finance Act 2026 First Schedule; confirm the 15% band and the Rs 2 Cr step.
6. Rule 115 -> r.206 or r.207.
7. Accumulating UCITS: confirm no deemed income.
8. SGB: does premature redemption after 5 years still count as "held till maturity"?
9. Crypto on a foreign exchange: which Schedule FA table?
10. T-bill discount: interest or capital gain if sold before maturity?

## 8. Sources

- [IR] work note `invrules.md` (finance-tax-migration, 2026-11-15): Income-tax Act 2025 and Rules
  2026 text, GitHub abaasairam-ai/income-tax-rag (`docs-text/income-tax-act-2025.txt`,
  `docs-text/income-tax-rules-2026.txt`).
- [ES] work note `empstock.md` (2026-11-15): ETrade, Fidelity, IBKR exports in Drive `Finance/`;
  yfinance closes 13 Nov 2026; yfinance INR=X (approx, not SBI TT rates); ITR AY2026-27 JSON;
  payslip Oct 2026; Microsoft Compensation Summary 2026-11-08.
- Work note `rules.md` (mid-Nov 2026): rates, surcharge cap, section map.
- Finance Bill 2026 Memorandum: https://www.indiabudget.gov.in/doc/memo.pdf
- IRS Publication 515: https://www.irs.gov/publications/p515
- IRS, nonresident estate tax: https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns
- IBKR SYEP: https://www.interactivebrokers.com/en/pricing/stock-yield-enhancement-program.php
- India-US DTAA (incometaxindia.gov.in; returned 403, articles from earlier notes).
- Not verified: Japan/Germany treaty details, IBKR withholding on interest and MMF dividends,
  TY 2026-27 ITR schedule layouts (cited from the AY 2025-26 ITR-2).
