# Private investing: accreditation and tax of startup shares, iSAFE/CCPS and angel funds

## Summary
- You are not a SEBI accredited investor: income passes the Rs 1 Cr leg, but net worth is Rs 4.21 Cr (needs Rs 5 Cr, about Rs 79 L short); 2026-27 income about Rs 1.38 Cr stays under Rs 2 Cr. Do not push income over Rs 2 Cr for this: it costs about Rs 3.10 L extra surcharge.
- Startup shares, iSAFE and CCPS are unlisted: long-term after 24 months at 14.95%, else 35.88%. An iSAFE is legally a CCPS, so its conversion into equity is not a sale and the CCPS months count. Avoid CCDs and convertible notes: sold or repaid before conversion they are always short-term (s.76).
- Before each cheque, get the startup's valuation report: if you pay more than Rs 50,000 below fair value, the gap is taxed at 35.88% (s.92(2)(m)).
- Angel fund: income is taxed as if you held the startups yourself (s.224), fund deducts 10% TDS; its losses reach you only on units held 12 months or more.
- A failed startup gives a loss only when the shares are sold or cancelled (liquidation, strike-off); file the return on time to carry it 8 years.

Written 2026-11-15 by `finance-tax`. Plan only; not tax advice. "AF s." = Income-tax Act 2025 (text read
2026-11-15, GitHub abaasairam-ai/income-tax-rag `docs-text/income-tax-act-2025.txt`); "nv" = not verified.
Rates: resident, new regime, income about Rs 1.06-1.38 Cr -> 15% surcharge + 4% cess. Routes and
returns: [income/private-investing.md](../income/private-investing.md).

## 1. SEBI accredited investor (individual)

SEBI Master Circular for AIFs para 10.3.1(a) (AIF Regulations 2012 Reg 2(1)(ab)): any one of the tests.
Primary residence is left out of net worth (10.3.3); you rent, so nothing to leave out.

| Test | Threshold | You (2026-11-15) | Pass |
|---|---|---|---|
| (i) annual income | Rs 2 Cr | 2025-26: salary about Rs 1.06 Cr. 2026-27: about Rs 1.38 Cr after QCOM sale 1 + MSFT Jan lot ([staged-sale.md](employer-stock/staged-sale.md) s.3.6); all employer stock sold at today's prices about Rs 1.59 Cr (s.2) | no |
| (ii) net worth + financial assets | Rs 7.5 Cr, of which Rs 3.75 Cr financial | Rs 4.21 Cr | no |
| (iii) income + net worth + financial assets | Rs 1 Cr income AND Rs 5 Cr net worth, of which Rs 2.5 Cr financial | income yes; financial assets yes (below); net worth Rs 4.21 Cr: short about Rs 79 L | no (closest) |
| (iv) securities market exposure | Rs 5 Cr (demat, MF folios, unlisted demat, overseas securities, NPS; 10.3.7) | about Rs 2.2 Cr (income note); FDs, EPF, cash do not count | no |

Your figures (portfolio/targets.md, `scripts.mark` 2026-11-15; Punjab Gramin Bank is your estimate):

| Item | Amount |
|---|---|
| Total marked (net worth) | Rs 4,20,91,028 |
| Financial assets, all (non-financial assets excluded) | Rs 4,08,00,836 |
| Financial assets without EPF (Rs 41,03,127) and Punjab Gramin Bank (Rs 82 L estimate) | Rs 2,84,97,709 |
| Liabilities | none recorded (nv) |

Either way financial assets pass Rs 2.5 Cr; net worth fails Rs 5 Cr. Discrepancy: the "Rs 2.83 Cr
financial assets" figure given for this note is not in the repository; the nearest is Rs 2.85 Cr above.

| Open point | What the text says | Status |
|---|---|---|
| What "annual income" means | Not defined in the Regulations or Master Circular. Proof: "Latest Income Tax Return or ITR Acknowledgement; or a certificate from a practising Chartered Accountant" (Annexure 11) | nv whether gross total income (incl. capital gains) or salary; ask CVL/NDML or the fund manager before relying on gains |
| Which year | "Latest" ITR, so the FY2026-27 return (filed Jul 2027) is the first that could show the QCOM gains | at Rs 1.38 Cr it fails (i) anyway |
| Crossing Rs 2 Cr on purpose | Surcharge on slab income goes 15% -> 25%: about Rs 3.10 L at once ([staged-sale.md](employer-stock/staged-sale.md) s.2) | not worth it |
| When (iii) could pass | Net worth Rs 5 Cr; date depends on returns and savings | unknown; recheck each April with `scripts.mark` |
| Certificate | CVL/NDML agency or the fund manager; valid 3 years (10.2, 10.5) | after a test passes |

## 2. Unlisted shares, iSAFE notes, CCPS, CCDs

| Instrument | Holding to be long-term | Rate | Source |
|---|---|---|---|
| Unlisted equity or preference shares (incl. CCPS, iSAFE) | more than 24 months | LT 12.5% -> 14.95% (AF s.197), no indexation; ST slab 35.88% | AF s.2(101)(a) |
| Same shares after an IPO | more than 12 months, counted from your purchase | AF s.196 23.92% / s.198 14.95% above Rs 1.25 L if sold on exchange with STT | s.2(101)(b)(i); [property-and-alternatives-2026-11.md](property-and-alternatives-2026-11.md) row 12 |
| Unlisted CCD, convertible note, any unlisted debenture | never: sale, redemption or maturity always short-term | 35.88% | AF s.76(1), (2)(b) |

| Event | Tax | Source |
|---|---|---|
| CCPS (incl. iSAFE) converts into equity of the same company | Not a transfer; holding period of the equity includes the CCPS period; cost carries over | AF s.70(1)(zb); s.2(101)(c)(B)(VIII) |
| CCD / debenture converts into shares of the same company | Not a transfer (no s.76 hit on conversion); cost carries over (s.73 Table Sl.3). No clause in s.2(101)(c)(B) adds the debenture period, so the shares' 24 months likely start at conversion | AF s.70(1)(z); nv - ask CA |
| iSAFE (100X.VC) | "takes the legal form of compulsorily convertible preference shares (CCPS)"; converts at the next priced round or after 3 years | 100x.vc/isafe FAQ, fetched 2026-11-15 |

Check per deal: the share certificate / allotment (PAS-3) must say CCPS. An "iSAFE" or SAFE issued
as a CCD or a startup convertible note is debt-like: flag it, it falls under s.76 if sold or repaid
before conversion (whether a convertible note is a "debenture" for s.76 is nv). Unlisted shares held
during the year are listed in ITR-2 (TY 2026-27 form layout nv).

## 3. Buying below fair value (ex-56(2)(x))

AF s.92(2)(m)(iii)(B): "property" (s.92(5)(f): includes shares and securities) received for less than its
fair market value by more than Rs 50,000 -> the whole gap is "income from other sources" at 35.88%.
FMV = "value determined by such method as may be prescribed" (s.92(5)(c); ex-Rule 11UA, 2026 Rules number nv).

| Case | Risk | Why |
|---|---|---|
| CCPS/iSAFE at the round price, with a discount to the next round on conversion | low (nv) | FMV is tested on the date you get the CCPS; the issue price is usually backed by a valuation report. A discount to a future round's price is a conversion term, not a price below today's FMV |
| Issue price below the startup's own valuation report | yes, if gap > Rs 50,000 | Gap = report FMV x shares - price paid |
| Buying existing shares from a founder or employee at a discount | yes | Clear "receipt for inadequate consideration" |
| Advisor or free shares | yes, whole FMV if > Rs 50,000 | s.92(2)(m)(iii)(A) |

Some rulings under the 1961 Act held that a fresh allotment is not a "receipt" of property (nv); do not
rely on it. Action: ask each startup for the valuation report (income-tax and FEMA pricing) dated near
your allotment and keep it. The issuer-side angel tax (1961 s.56(2)(viib)) is gone; this investor-side
rule is not.

## 4. Angel fund (SEBI Category I AIF)

| Point | Rule | Source |
|---|---|---|
| Who it covers | Category I or II AIF under SEBI AIF Regs 2012 (or IFSCA), as trust, company or LLP | AF s.224(10)(a) |
| Your income | Taxed as if you made the fund's investments yourself, same nature and proportion (exit gain on a startup held > 24 months by the fund = LT 14.95%) | s.224(1), (5) |
| Not distributed | Deemed credited to you on 31 Mar of the tax year; taxed then, not again when paid | s.224(7), (8) |
| Fund's business loss | Stays in the fund, carried forward there; never reaches you | s.224(2)(a) |
| Fund's other losses (e.g. capital loss) | Passed to you only for units you have held at least 12 months; otherwise ignored | s.224(2)(b) |
| TDS | 10%, no threshold, on income paid or credited to a resident unit holder (ex-194LBB); claim it in the ITR | s.393(1) Table Sl.4(iii) |
| Statement | Fund gives you a statement of income by nature (ex-Form 64C; 2026 form number nv) - use it for the ITR | s.224(9) |

Keep angel-fund units at least 12 months, or failed-startup losses inside the fund are lost to you.

## 5. Failed startups

| Point | Rule | Source |
|---|---|---|
| When a loss exists | Only on a "transfer": sale, relinquishment or extinguishment of rights. A write-down, a shut-down without cancellation or a value near zero is not a transfer | AF s.2(109)(a), (b); [global-actions-2026-11.md](global-actions-2026-11.md) row 18 |
| Liquidation | Money received less deemed dividend part = sale value; loss in the year of distribution | AF s.68(2) |
| Holding period in liquidation | Stops on the date the company goes into liquidation (LT/ST fixed then) | s.2(101)(c)(A) |
| Strike-off / dissolution with nothing paid | Shares extinguished on dissolution -> loss in that year (zero-consideration loss disputed, SC Vania Silk Mills 1991; nv) | s.2(109)(b) |
| Simpler route | Sell the shares to anyone for a token price (needs company consent / ROFR, nv); keep the transfer deed | s.2(109)(a) |
| Set-off same year | ST loss vs any capital gain; LT loss only vs LT gain | AF s.108(2) |
| Carry forward | Capital gains only (LT loss only vs LT gain), 8 tax years | s.111(1)(a), (2) |
| Return on time | Loss carried forward only if the return is filed by the due date (s.263(1)) | s.121 |

## Actions
| When | What |
|---|---|
| Before each cheque | Confirm CCPS (not CCD/note) in the term sheet; get the valuation report; keep PAS-3 and share certificate |
| Each April | Recheck test (iii) net worth with `scripts.mark`; ask CVL/NDML in writing what "annual income" means |
| Each ITR | List unlisted shares; add angel-fund statement income; file by the due date if any loss |

## Sources (fetched 2026-11-15)
- SEBI Master Circular for AIFs, paras 10.2-10.3, Annexure 11: https://www.sebi.gov.in/sebi_data/attachdocs/nov-2026/1793875212889.pdf
- SEBI AIF Regulations 2012 (amended 15 Oct 2026), Reg 2(1)(ab): https://www.sebi.gov.in/sebi_data/attachdocs/oct-2026/1792668513871.pdf
- Income-tax Act 2025 text: s.2(101), 2(109), 68, 70(1)(z)/(zb), 73, 76, 92(2)(m)/(5), 108, 111, 121, 224, 393(1) Sl.4(iii)
- 100X.VC iSAFE FAQ: https://www.100x.vc/isafe ; CVL accreditation page gave no text (JavaScript only)
