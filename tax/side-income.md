# Side income (Topmate calls, newsletter, courses) - tax

## Summary

- Topmate is real but small: HDFC savings shows 35 Topmate payouts of Rs 13,066 in 2025-26 and Rs 8,624 in 2026-27 to 14 Nov (about Rs 14,850 and Rs 9,900 before Topmate's fees). Tax on 2025-26 is about Rs 2,660 (50% presumptive) to Rs 4,690 (actual profit).
- It is not in the filed AY2026-27 return (original or revised): Schedule BP has only the F&O loss of Rs 4,203. AIS/TIS show no Topmate TDS, no GST and no business receipts (Topmate deducts no TDS below Rs 5 L a year). How to handle 2025-26 is your decision (options in section 5).
- 2026-27: report it in the ITR-3 as profession income; simplest is AF s.58 Sl.3 (1961 s.44ADA): 50% of gross is taxable, no books. Add about Rs 2,700 to the 15 Mar 2027 advance tax (Rs 17,940 per Rs 1 L of gross).
- GST: nothing to do while your aggregate turnover (Topmate + bank interest) stays under Rs 20 L; it was about Rs 9.4 L in 2025-26.
- Keep a yearly Topmate earnings export (dashboard) in Drive `Finance/Tax/FY<year>/`; send it to finance-tax each April.

Written 2026-11-15 by `finance-tax` (agent sideinc). New regime, income about Rs 1.06 Cr: slab 35.88% (30% + 15%
surcharge + 4% cess). Sections: 2025 Act (AF) with 1961 in brackets. Not filing figures; nothing filed or paid.
Ideas and employer rules: `income/expertise.md`, `income/side-income.md`, `income/rules.md`.

## 1. What the data shows (checked 2026-11-15)

| Source | What it shows |
|---|---|
| HDFC savings CSV 1 Apr 2025 - 31 Mar 2026 | 35 IMPS credits "TOPMATEPAYOUT" from the Topmate operator (Kavalry Technologies; 11 via its RazorpayX payout account, 24 direct): Rs 13,066, 11 Apr 2025 - 28 Mar 2026; largest Rs 2,200; 12 of Rs 22 |
| HDFC savings CSV 1 Apr - 14 Nov 2026 | 10 credits from the Topmate operator: Rs 8,624 (Apr 3,278, May 1,584, Jun 132, Jul 132, Aug 1,352, Sep 2,146); none after 6 Sep |
| Topmate fees page (checked by Topmate 2 Nov 2026) | Creator keeps 88% of price on own-link sales (10% commission + 2% gateway), 78% on marketplace sales. Payouts up to Jul 2026 are exactly 88% of round prices (Rs 2,200 = 88% of 2,500); from Aug 2026 85.84% (18% GST on the 12% fee: Rs 2,146 = 85.84% of 2,500). So no TDS was taken |
| Gross receipts (price) estimate | 2025-26: Rs 13,066 / 0.88 = about Rs 14,850 (up to Rs 16,750 if some were marketplace sales). 2026-27 to 14 Nov: about Rs 9,900 |
| TIS 2025-26 (generated 7 Nov 2026) | 8 categories: salary, dividend, savings and FD interest, securities sold/bought, credit-card payments, time deposits. No s.194-O / 194J / 194R TDS, no GST turnover, no business receipts |
| AIS 2026-27 (generated 8 Nov 2026) | Salary TDS (AF s.392), Punjab Gramin Bank interest TDS, AY2026-27 self-assessment tax. SFT and other parts: "No Transactions Present" |
| ITR-3 AY2026-27 original (JSON 18 Jul 2026) and revised (upload 8 Nov 2026) | Business: only "F&O and other non-speculative" (code 09028), loss Rs 4,203. No s.44ADA/44AD line, no professional receipts. Schedule OS: interest and dividends only |
| Not checked | Form 26AS (not in Drive); AIS 2025-26 JSON (encrypted, TIS used); other bank accounts (HDFC is the only bank export in Drive; Punjab Gramin Bank folder empty); years before 2025-26 |

Discrepancy: `income/expertise.md` row 1 estimates Rs 1-3 L a year from Topmate; the bank shows about Rs 15,000
gross a year. Most of the 1.2k bookings are free sessions.

## 2. Head of income and how to compute it

| Question | Answer | Source |
|---|---|---|
| Head | "Profits and gains of business or profession": a regular, priced activity. Paid 1:1 advice from personal skill is a profession ("profession" includes vocation); a newsletter or course sold to many buyers is closer to a business | AF s.2(20), s.2(86) |
| Specified profession? | AF s.62(4): legal, medical, engineering, architectural, accountancy, technical consultancy, interior decoration, information technology, company secretary, or notified. Calls on RedHawk-SC/EMIR debugging and Python are technical/engineering advice; that fits "technical consultancy" (likely view). Pure career-guidance calls fit less well (not defined in the Act) | AF s.62(4) |
| Presumptive, profession: AF s.58(2) Sl.3 (1961 s.44ADA) | Resident individual; gross receipts up to Rs 50 L, or Rs 75 L if cash receipts are at most 5%. Taxable = 50% of gross receipts (or more if you claim more). No other expense is allowed. No books, no audit | AF s.58(2) Table Sl.3, s.58(4), s.63(2) |
| Presumptive, business: AF s.58(2) Sl.1 (1961 s.44AD) | 6% of digital receipts (8% of cash); limit Rs 2 Cr (Rs 3 Cr if cash at most 5%). Not open to anyone who carries on a specified profession, earns commission/brokerage or runs an agency. So you cannot use 44ADA for the calls and 44AD for a course in the same year. Opting out within 5 years blocks it for 5 years | AF s.58(11)(a), s.58(7) |
| New regime | s.58 has no regime condition; presumptive works under the new regime | AF s.58 text |
| Actual profit instead | Receipts minus real costs: Topmate commission and gateway fee (12%), GST on the fee, internet/phone share, laptop depreciation (40% block), software, mic. For you that is about 86-88% of gross, so 44ADA (50%) is lower | AF s.58(3) |
| Books | Specified profession: books only if gross receipts exceeded Rs 1.5 L in any of the 3 previous years (not the case). Other profession/business: only above Rs 2.5 L income or Rs 25 L receipts. Keep the Topmate export and bank credits anyway | AF s.62(1)-(2); Rules 2026 r.46(3) |
| Audit | Profession: gross receipts above Rs 50 L. Not needed if income is declared under s.58 | AF s.63(1) Sl.1(c), s.63(2) |
| Loss | A loss is possible only on actual profit; under s.58 no loss can be claimed. Business loss cannot be set off against salary | AF s.58(4) |
| Form | ITR-3 (you already file it for F&O). ITR-4 is barred (income above Rs 50 L, capital gains, foreign assets) | ITR-3 JSON AY2026-27 |

Tax per Rs 1 L of gross receipts:

| Method | Taxable | Tax at 35.88% |
|---|---|---|
| AF s.58 Sl.3 (44ADA), 50% | Rs 50,000 | Rs 17,940 |
| Actual profit, only Topmate fees as cost (88% kept) | Rs 88,000 | Rs 31,574 |
| AF s.58 Sl.1 (44AD) 6% digital, only if no specified profession | Rs 6,000 | Rs 2,153 |

2025-26 (gross about Rs 14,850): 44ADA Rs 2,664; actual (Rs 13,066) Rs 4,688.

## 3. TDS and foreign payments

| Item | Rule | For you |
|---|---|---|
| Topmate as e-commerce operator | AF s.393(1) Table Sl.8(v) (1961 s.194-O): 0.1% of gross sales/services. No TDS for an individual whose gross through the operator is up to Rs 5 L in the year and who gave PAN or Aadhaar (s.393(4) Sl.11) | None deducted (payouts are exact 88%/85.84%); nothing in AIS. If it appears later, claim it in Schedule TDS2 under head BP |
| Fees from a company (institute, client) | AF s.393(1) Table Sl.6(iii) (1961 s.194J): 10% on professional fees above Rs 50,000 a year | Shows in AIS; claim in the ITR |
| Benefits in kind (free gadgets, trips) | AF s.393(1) Table Sl.8(iv) (1961 s.194R): 10% if above Rs 20,000; the value is business income | Only if a sponsor gives goods |
| Foreign buyers via Topmate | Topmate collects in USD and pays you INR from India; you receive no foreign remittance and no FIRC | Same as Indian income |
| Direct foreign clients (Stripe, PayPal, Payoneer, wire) | Business income; get a FIRC/e-BRC from the bank; correct purpose code on the inward remittance (bank asks); bring the money in within the RBI export deadline (check with the bank) | Not used today |

## 4. GST

| Point | Rule | For you |
|---|---|---|
| Threshold | Registration when aggregate turnover in a year exceeds Rs 20 L (Rs 10 L in special category states) | CGST s.22(1) |
| What counts | Aggregate turnover includes exempt supplies, all India by PAN. Bank FD and savings interest is an exempt supply, so a cautious count includes it. Salary, dividends and share sales are not supplies | CGST s.2(6); 2025-26: Rs 9.25 L interest + Rs 0.15 L Topmate = about Rs 9.4 L |
| Sales through an e-commerce operator | CGST s.24(ix) makes suppliers through an operator that collects TCS register regardless of turnover; Notification 65/2017-CT (15 Nov 2017) exempts suppliers of services through an operator below the threshold (CBIC link broken; text not re-read) | No registration needed now |
| TCS by the operator (s.52) | Collected only on supplies made by registered persons | Not collected from you |
| GST on Topmate's own fee | Topmate charges 18% GST on its 12% fee from Aug 2026 (payout arithmetic); you cannot claim it back while unregistered; it is a business cost | Cost only |
| If you register later | Calls, courses, newsletters to Indian buyers: 18%. Buyers abroad, paid in foreign exchange: export, zero-rated under a LUT. OIDAR rules apply to foreign sellers into India, not to you | Plan before receipts plus interest near Rs 20 L |

## 5. Tax year 2025-26 (AY2026-27, filed and revised) - facts only

- Filed returns: Topmate payouts (Rs 13,066 net, about Rs 14,850 gross) are not in the original or the revised ITR-3.
- AIS/TIS: no entry for Topmate, so there is no mismatch notice trigger from AIS; the bank credits are the only record.
- Tax involved: about Rs 2,660 (44ADA) to Rs 4,690 (actual), plus interest at 1% a month.
- If the amounts are not in the filed return, the user decides how to handle it (through finance-main). Options:
  revised return by 31 Mar 2027 (Rs 5,000 fee after 31 Dec 2026; 1961 s.139(5), `ca-questions.md`) or an
  updated return ITR-U later (1961 s.139(8A): additional tax 25%-70% of tax and interest by year).
  The user has already decided not to revise AY2026-27 again for a separate capital-gains item.

## 6. Tax year 2026-27 - what to do

| Step | When | Detail |
|---|---|---|
| Export Topmate earnings for Apr 2026 - Mar 2027 (gross, fees, refunds) | Apr 2027 | Save in Drive `Finance/Tax/FY2026-27/`; bank credits alone give only the net |
| Advance tax | 15 Mar 2027 (or with the 15 Dec instalment) | Gross so far about Rs 9,900; a full year about Rs 15,000 gives Rs 2,700 tax under 44ADA. Formula: gross x 50% x 35.88% = gross x 17.94% (actual-profit method: gross x 0.86 x 35.88%). Add to `FY2026-27/fd-and-advance-tax.md`. AF s.408(2) and s.425(3) let a s.58 filer pay all advance tax by 15 Mar; the existing 15 Dec plan is safe either way |
| ITR-3 TY2026-27 | by 31 Aug 2027 (AF s.263(1)(c): business income, no audit) | Schedule BP, presumptive profession (44ADA line), nature-of-profession code for technical consultancy/IT; gross receipts = prices before Topmate's fee |
| Employer | now | Whether Microsoft allows the paid calls is an HR question (Outside Work Policy), not tax: `income/rules.md` |

## 7. Tax line for the other ideas

From `income/expertise.md` (E#) and `income/side-income.md` (S#). "nv" = not verified from a source today.

| Idea | Head and rate | GST | TDS / foreign |
|---|---|---|---|
| E2 recorded course on own site / Topmate | Business; actual profit, or 44ADA if bundled with technical consultancy; 44AD 6% only if no specified profession | Counts to Rs 20 L; 18% once registered; foreign buyers = export | Topmate 0.1% above Rs 5 L; direct sales none |
| E2 Udemy | Business; slab | Export of services to a foreign platform (if registered) | US tax may be withheld on US sales; claim treaty rate with W-8BEN (nv); credit via Form 67 and Schedule FSI/TR |
| E3 institute trainer, E6 university lectures | Profession; slab (teaching is not in s.62(4), so no 44ADA; actual profit) | Counts to Rs 20 L | 10% TDS above Rs 50,000 (s.393 Sl.6(iii)) |
| E4 paid Substack newsletter | Business; slab | Indian subscribers taxable once registered; foreign = export | Payouts via Stripe to an Indian bank (nv); no US withholding expected for non-US writers (nv) |
| E5 eBook on KDP / publisher | Royalty: business or other sources; slab | Copyright licence; counts to Rs 20 L | Amazon US withholds on US sales; India-US treaty Art.12 cap 15% with W-8BEN (nv); Form 67; Indian publisher TDS 10% (Sl.6(iii)) |
| E7 YouTube ads | Business; slab | Export to Google Asia Pacific (if registered) | Google withholds US tax on US-viewer earnings without/with W-8BEN (nv); FIRC for inward USD |
| E8 GitHub Sponsors | Business (or other sources); slab | Counts to Rs 20 L | Paid via Stripe from the US (nv) |
| E10-E12 expert networks, consulting, corporate training | Technical consultancy: 44ADA possible; slab | Foreign client = export; Indian client 18% once registered | Indian payer 10% (Sl.6(iii)); not allowed by employer rules today |
| E9 patents/awards, S1 referral bonus | Salary; payroll TDS (s.392) | None | None |
| S2 REITs | Interest and taxable dividend at slab; capital repayment lowers cost | None | REIT deducts TDS |
| S3 paid finance guide | Same as E2 | Same as E2 | Same as E2 |
| S5 broker referrals | Commission: business; 44AD barred for commission | Counts to Rs 20 L | Commission TDS by the broker (nv) |
| S6 rental (none today) | House property; 30% standard deduction | Residential rent exempt | Tenant TDS only above the rent limit (nv) |
| Foreign payout balances (PayPal, Payoneer, Stripe, Wise) | Money left in a foreign account at any time in the calendar year goes in Schedule FA (foreign depository/custodial account, nv which table) | - | Bring export receipts home within the RBI deadline (nv) |

## Sources (all read 2026-11-15)

- [Act] Income-tax Act 2025 text: github.com/abaasairam-ai/income-tax-rag docs-text/income-tax-act-2025.txt - s.2(20), 2(86), 58, 62, 63, 263(1)(c), 393(1) Sl.6, 8(iv), 8(v), 393(4) Sl.11, 408, 425.
- [Rules] Income-tax Rules 2026, same repo, r.46 (books for professions).
- [CGST] CGST Act 2017 as amended to 30 Sep 2020, cbic-gst.gov.in/pdf/CGST-Act-Updated-30092020.pdf - s.2(6), 22, 24, 52.
- [Topmate] topmate.io/terms (Kavalry Technologies operates Topmate; GST collected as per law), topmate.io/fees (10%/20% commission, 2% INR transaction charge).
- [Data] Drive `Finance/Banking/HDFC/Savings` CSVs; `Finance/Tax/FY2025-26/Income Tax Site/TIS` (7 Nov 2026); `FY2026-27/Income Tax Site/AIS` PDF (8 Nov 2026); `FY2025-26/ITR` original and revised JSON.
- Not fetched: Notification 65/2017-CT text (CBIC links returned 404/500), Udemy/KDP/YouTube/Substack tax pages, RBI export deadline.
