# Owning a business or solar - tax

## Summary
- SaaS with foreign buyers: 6% presumptive tax (AF s.58 Sl.1, 1961 s.44AD) fits, but only in a year you do no Topmate technical calls: the bar is on the person, not per income. Rs 10 L receipts: Rs 21,528 tax at 6% vs Rs 1.44-2.51 L on actual profit.
- GST: register when Topmate + SaaS + bank interest pass Rs 20 L (interest alone was Rs 9.25 L in 2025-26), then file a LUT: foreign sales are zero-rated exports. OIDAR is for foreign sellers, not you. Indian buyers pay 18%.
- Buy assets, not a foreign company, unless the seller insists: assets give a cost you can depreciate (software 40%, other intangibles 25%, goodwill 0%). Shares need ODI filings (Form FC, yearly APR) and risk Indian tax on the company if you run it from India (POEM).
- Rooftop solar: bill savings and net-meter credits are not income; cash from the discom for surplus units is taxable at slab. The PM Surya Ghar subsidy (up to Rs 78,000) is most likely income under AF s.2(49)(w): show it under other sources in the year you get it (up to Rs 27,986 tax; `ca-questions.md`).
- Nothing to do now: this is for later, if you buy a business or a solar system. Microsoft approval comes first (`income/business.md`).

Written 2026-11-15 by `finance-tax` (agent business). Ideas: `income/business.md`; Topmate: [side-income.md](side-income.md).
New regime, slab 35.88% (30% + 15% surcharge + 4% cess; stays while income is under Rs 2 Cr). Sections: 2025 Act (AF),
1961 Act in brackets. "nv" = not verified from a primary text today. Plans only; nothing filed or paid.

## 1. Presumptive tax for SaaS income (AF s.58)

| Question | Answer | Source |
|---|---|---|
| Who can use 6%? | "Eligible assessee": resident individual who (iii) "does not carry on specified profession as defined in section 62(4)", (iv) earns no commission or brokerage, (v) runs no agency business, (ii) claims no Chapter VIII-C deduction | AF s.58(11)(a) |
| Is the bar per income type? | No. It is a condition on the person for the year. Topmate calls on EMIR/RedHawk-SC debugging are technical consultancy (s.62(4)(a); side-income.md section 2), so in a year with any such calls no business income of yours can use 6%. Calls stop -> 6% opens from the next tax year. Old 1961 s.44AD(6)(i) excluded "a person carrying on profession" in the same way (1961 text not re-read today, nv) | AF s.58(11)(a)(iii), s.62(4) |
| Is owning SaaS a "profession"? | Selling subscriptions to software you own, run by a hired operator, is a business (likely view). Writing code for clients is "information technology", a specified profession, and would block 6% | AF s.62(4)(a) |
| Turnover limit | Rs 2 Cr; Rs 3 Cr if cash receipts are at most 5% (Stripe/Paddle/bank = 0% cash) | AF s.58(2) Sl.1 col. D |
| Deemed profit | 6% of receipts by "specified banking or online mode" (account-payee cheque, draft, ECS through a bank, other prescribed electronic modes), 8% of the rest; or more if you earned more | AF s.58(2) Sl.1 col. E; s.66(32) |
| Costs and depreciation | None allowed on top; depreciation is deemed taken, so the purchase price of the assets gives no extra deduction; no loss can be claimed | AF s.58(4), s.58(6) |
| Lock-in | If you use 6% and then declare less in any of the next 5 years, 6% is barred for 5 years and books plus audit become compulsory | AF s.58(7), (8) |
| Books and audit | None while you declare at least 6%. On actual profit: books above Rs 2.5 L income or Rs 25 L receipts; audit above Rs 1 Cr (Rs 10 Cr if cash receipts and payments are each at most 5%) | AF s.62(2)(c)-(d), s.63(1) Sl.1, s.63(2) |
| Advance tax | All of it by 15 Mar (paying earlier is fine) | AF s.408(2) |
| Return | ITR-3 (already used): Schedule BP presumptive business line; Schedule FA for any foreign account or company; Form 67 if foreign tax is withheld | ITR-3 AY2026-27 JSON |

Tax per Rs 10 L of SaaS receipts (illustrative margins, not from data):

| Method | Taxable | Tax at 35.88% |
|---|---|---|
| 6% presumptive (no Topmate calls that year) | Rs 60,000 | Rs 21,528 |
| Actual profit, 40% margin (hired operator) | Rs 4,00,000 | Rs 1,43,520 |
| Actual profit, 70% margin (you run it) | Rs 7,00,000 | Rs 2,51,160 |
| Topmate calls today, 50% presumptive (s.58 Sl.3) on about Rs 15,000 a year | Rs 7,500 | Rs 2,691 |

So once SaaS receipts pass a few lakh, stopping the paid technical calls (about Rs 13,000 net a year) saves far more tax than they earn.

## 2. GST on SaaS

| Point | Rule | For you |
|---|---|---|
| Registration | When aggregate turnover passes Rs 20 L in a year. It counts exports and exempt supplies (bank interest) for the whole PAN | CGST s.22(1), s.2(6). 2025-26: interest Rs 9.25 L + Topmate Rs 0.15 L, so about Rs 10.6 L of SaaS sales fit before the limit |
| Inter-State sales | s.24(i) requires registration for any inter-State taxable supply; exports are inter-State. Notification 10/2017-IT (13 Oct 2017) exempts service suppliers under the threshold (text not re-read, nv) | Check with a GST practitioner before the first foreign sale |
| Export of services | All 5: supplier in India; recipient outside India; place of supply outside India; paid in convertible foreign exchange (or INR where RBI allows); supplier and recipient not just establishments of one person | IGST s.2(6) (CBIC and indiacode copies did not load 2026-11-15; wording from the Act as commonly quoted, nv) |
| Exports are zero-rated | Supply under a LUT without IGST and claim refund of input tax (or pay IGST and claim it back) | IGST s.16(3); CBIC exporter guidance note, section XIII |
| LUT | File each financial year on the GST portal (Form GST RFD-11, nv) before the first export invoice | After registration |
| OIDAR | Registration duty is on persons supplying OIDAR "from a place outside India to a person in India" who is not registered. You supply from India, so sales to foreign buyers are exports, not OIDAR | CGST s.24(xi); IGST s.2(17) (nv, as above) |
| Indian buyers | 18% GST once registered (rate nv for the specific SaaS code) | Charge on the invoice; through Stripe you are the seller |
| Stripe (payment processor) | You sell to each buyer; GST rules above apply buyer by buyer. Keep the FIRC/e-BRC for each foreign payout as proof of foreign exchange | Bank gives FIRC on request |
| Paddle / Lemon Squeezy (merchant of record) | The platform buys from you and resells. Your one buyer is the platform's foreign entity: export (if all 5 tests hold); the platform handles GST on its sales to Indian buyers as a foreign OIDAR supplier | Read the contract: which entity buys, in which currency it pays (nv per platform) |

## 3. Buying a business: assets vs foreign company

| Point | Buy assets (code, domain, customers) | Buy shares of a foreign company (ODI) |
|---|---|---|
| Who owns | You, as a sole proprietor in India | A foreign company you control |
| Your tax cost | Price split in the sale agreement across assets | Price of the shares; no depreciation |
| Depreciation (actual-profit method only) | Computer software 40%, know-how/copyrights/trademarks/licences/similar rights 25% (domain and customer list likely here, nv); half rate if used under 180 days in the year; goodwill 0% | None for you; the company follows its own country's rules |
| Goodwill | Not depreciable (removed by Finance Act 2021 under 1961; same in AF). On sale, cost = price you paid | Inside the share price |
| Yearly income | Business income at slab, or 6% (section 1) | Company profit taxed abroad; dividends to you at slab with foreign tax credit (Form 67) |
| Later sale | Software and intangibles: gain on the block is short-term; goodwill long-term after 24 months; whole business for a lump sum (slump sale) long-term after 36 months, 12.5% | Unlisted foreign shares: long-term after 24 months, 12.5% (14.95% with surcharge and cess); short-term at slab |
| FEMA | Payment abroad for assets: ask the AD bank for the purpose code; under LRS, TCS 20% above Rs 10 L a year (credited back in the ITR) | Schedule III OI Rules: operating foreign company, not in financial services, no subsidiary or step-down subsidiary while you control it (control = 10%+ votes or board/management); within the LRS limit with your other LRS money; no real estate or gambling; no investment back into India that makes more than 2 layers. Form FC through the AD bank before paying; APR every year, CA-certified; late filing fee Rs 7,500+ |
| Schedule FA | Foreign payout accounts only (Stripe/Paddle balances abroad) | The shares, every year you hold them |
| Company residence | n/a | If the key management and commercial decisions are in substance made in India (by you), the company is Indian resident (POEM) and its world income is taxed in India. 1961 had a Rs 50 Cr turnover safe zone (CBDT Circular 8/2017, nv for AF) |
| Approvals | Microsoft outside-work approval (`income/business.md`) | Same, plus ODI paperwork |
| Source | AF s.2(17)(b), s.33(1), (4), (12); Rules 2026 r.25 App. I; s.90(3)-(4); s.77; s.394(1) Sl.7 | AF s.2(101), s.197, s.6(10); OI Rules 2022 r.19, Sch. III para 1; OI Directions 2022 para 3, 17, 18, 22 |

Before signing, ask a CA: Form 15CA/15CB and any TDS on paying a foreign seller (AF s.393; nv for this case).

## 4. Rooftop solar on your own home

| Item | Tax | Source |
|---|---|---|
| Power you use yourself (lower bill) | Not income: there is no receipt and no section taxes it | Act has no such charge |
| Net-metering credits (units carried forward against your bill) | Not income: a bill adjustment, no payment (no ruling found, nv) | - |
| Cash paid by the discom for surplus units (net-billing or year-end settlement) | Income from other sources at slab; small (for example 500 units x Rs 3 = Rs 1,500 -> Rs 538 tax; rates by state, nv) | AF s.92(1) |
| PM Surya Ghar subsidy (Rs 30,000-78,000 by size) | Most likely taxable at slab under other sources (AF s.2(49)(w) with s.92(1)). The only exclusion is a subsidy that reduces the actual cost of a depreciable asset (s.39(1)(d)); a home system has no depreciation, so it does not apply. The clause (ex-1961 s.2(24)(xviii), 2015) was added to override the old capital-receipt case law. No exemption in the Act or the Finance Bill 2026 memo, and no CBDT statement found (read 2026-11-16). Worst case Rs 78,000 x 35.88% = Rs 27,986 | AF s.2(49)(w); subsidy amounts: `income/business.md` (Wikipedia, secondary) |
| Depreciation | None: not a business asset | AF s.33(1) |
| Net-metering rules (who may export, settlement price) | Set by MNRE / Electricity (Rights of Consumers) Rules 2020 and your state commission; pages did not load 2026-11-15 (nv) | Check the discom offer when applying |

## Discrepancies and open points

| Item | Action |
|---|---|
| Brief said the presumptive bar is "per income type": the AF text is a bar on the person | Recorded above; `income/business.md` question 1 is answered here |
| Brief and `income/business.md` treat the solar subsidy as not income: AF s.2(49)(w) says otherwise for non-business assets | Done: `ca-questions.md` (likely taxable) |
| IGST Act text (s.2(6), 2(17), 13, 16) not loaded from a primary site today | Re-read when CBIC/indiacode work; conclusions match CGST s.24(xi) and the CBIC note |
| ODI APR due date and Schedule FA table for company shares | Read OI Regulations 2022 reg. 10 and the ITR-3 schedule before any purchase |

## Sources (read 2026-11-15)
- Income-tax Act 2025 and Rules 2026: github.com/abaasairam-ai/income-tax-rag docs-text/ (s.2(17), 2(49)(w), 2(101), 6(10), 33, 58, 62, 63, 66(32), 77, 90, 92, 197, 394, 408; Rules App. I).
- CGST Act as amended to 30 Sep 2020: cbic-gst.gov.in/pdf/CGST-Act-Updated-30092020.pdf (s.2(6), 22, 24).
- CBIC Guidance Note for Importers and Exporters v2: cbic-gst.gov.in/pdf/Guidance-Note-for-Importers-Exporters-v2.pdf (zero-rating, LUT).
- RBI: FEM (Overseas Investment) Rules 2022, rbi.org.in/scripts/bs_viewcontent.aspx?Id=5087 (r.2 control/ODI, r.19, Sch. III); OI Directions 2022, rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12381 (para 3, 17, 18, 22).
- Not loaded: IGST Act (CBIC 404, indiacode 403), Notification 10/2017-IT, MNRE and Ministry of Power pages (403), pmsuryaghar.gov.in (script-only page).
