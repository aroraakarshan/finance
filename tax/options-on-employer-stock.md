# Options on QCOM at IBKR: covered calls and protective puts

## Summary

- Most likely **not allowed** for you under FEMA: RBI's Overseas Investment Directions say a resident's portfolio investment "shall not be made in ... any derivatives unless otherwise permitted by Reserve Bank", and no such permission for individuals was found. Same for RSU/ESPP shares and LRS money.
- Risk if done anyway: FEMA penalty up to 3 times the sum involved (or compounding). Do not write calls or buy puts until an AD bank or a FEMA lawyer confirms in writing.
- If it were done: premium taxed at slab, about Rs 33,700 per $1,000 (35.88%), vs 14.95% on the shares; a lapsed put is a loss you may only be able to use against speculative income.
- Hedging carve-out (AF s.66(31)(c)) may keep protective puts and covered calls out of "speculative", but foreign options never get the Indian-exchange carve-out.
- What to do: keep the plain staged sale in `employer-stock.md` (Rs 2.54 L tax on 432 sh in Nov-Dec 2026); ask the questions in section 5.

Written 2026-11-15 by `finance-tax`. Plan only; no orders. AF = Income-tax Act 2025, 1961 Act in
brackets. USD/INR 94.03 (as `employer-stock.md`). Rates: LT 14.95%, slab 35.88%.

## 1. Sources read

| Source | What it says here | Read |
|---|---|---|
| RBI Master Direction - Overseas Investment (updated 1 Apr 2026), rbi.org.in id=12710, Part I para 1(ix)(a) | "OPI shall not be made in: ... any derivatives unless otherwise permitted by Reserve Bank" | 2026-11-15 |
| Same, para 1(ix)(f) and para 22(2), 22(7) | ESOP/employee-scheme shares (up to 10%, no control) are OPI; ESOP remittances count toward LRS | 2026-11-15 |
| Same, para 1(viii) | "financial commitment" = ODI + debt (not OPI) + non-fund facilities; not relevant to an individual's options | 2026-11-15 |
| RBI Master Direction - LRS (updated 6 Sep 2024), id=10192, para A.5 | "remittance for margins or margin calls to overseas exchanges/ overseas counterparty are not allowed" | 2026-11-15 |
| Same, para A.17; RBI LRS FAQ (updated 6 Apr 2023) Q2, Q4 | Income may be retained and reinvested; realised/unused foreign exchange, unless reinvested, repatriated within 180 days | 2026-11-15 |
| RBI LRS FAQ, introduction | Current account = does not alter assets or liabilities, "including contingent liabilities", outside India | 2026-11-15 |
| AF text (GitHub abaasairam-ai/income-tax-rag, docs-text/income-tax-act-2025.txt) | s.66(31) speculative transaction, (33) specified derivative; s.26(3) speculation business; s.113 losses; s.63 audit; s.58 presumptive; s.2(101), 2(109) | 2026-11-15 |
| US Treas. Reg. 1.1441-2(b)(2)(i) (eCFR) | "Gains derived from the sale of property (including ... option premiums)" are not FDAP | 2026-11-15 |
| OI Rules 2022 (Gazette PDF) | Not read: rbidocs.rbi.org.in PDF is behind a CAPTCHA. Whether the Rules repeat the derivatives bar is **unverified** | tried 2026-11-15 |
| FEMA 1999 s.2(e), 4, 6, 13; FEM (Compounding Proceedings) Rules 2024 | Not re-read (indiacode PDF blocked); wording from memory, **unverified** | - |
| ICAI Guidance Note on Tax Audit (2022 rev.); ClearTax, taxguru, Big-4 commentary; IBKR rules for Indian residents | Not read: search engines and sites blocked automated access. **Unverified** | tried 2026-11-15 |

## 2. FEMA / LRS: allowed?

| Question | Answer | Basis | Confidence |
|---|---|---|---|
| Buy protective puts on QCOM | **No (most likely).** Buying a listed option is OPI in a derivative, barred unless RBI permits; no RBI permission for individuals found | OI MD para 1(ix)(a) | High |
| Write covered calls on owned QCOM | **No (most likely).** Writing an option creates a contingent liability abroad (a capital account transaction); no rule or direction allows it for individuals. Being fully covered (no cash margin) does not create a permission; the derivative bar still applies | OI MD 1(ix)(a); FAQ definition; FEMA s.6 (unverified wording) | Medium-high |
| Send money (LRS) to IBKR for options or margin | **No.** Margin/margin calls are expressly barred; derivatives are not a permitted OPI | LRS MD A.5; FAQ Q2(2) | High |
| Use USD from the QCOM/MSFT sale held at IBKR | Same bar: the source of money does not change what the investment is. Reinvestment is allowed only in permitted OPI (shares, ETFs, regulated funds) | LRS MD A.17; OI MD 1(ix) | High |
| RSU/ESPP shares vs LRS-bought shares | No difference: both are OPI (OI MD 1(ix)(f), 22(2)) and the derivative bar applies to all OPI | OI MD | High |
| Sale proceeds left at IBKR | Repatriate within 180 days unless reinvested in permitted OPI. The text speaks of an "investor who has remitted funds under LRS"; RSU shares had no remittance, so the exact rule for RSU proceeds is **unverified** (general FEMA realisation regulations, 180 days) | LRS MD A.17; FAQ Q4 | Medium |
| Penalty if contravened | Up to 3 times the sum involved where it can be quantified, or up to Rs 2 L; continuing default extra per day; can be compounded with RBI (fee) | FEMA s.13, Compounding Rules 2024 (**unverified**, not re-read) | Medium |

"Sum involved" for a written call (premium, strike value or shares pledged) is not defined - a reason not
to test it. Discrepancy: `tax/new-investments.md` cites the LRS FAQ "behind CAPTCHA, not re-fetched";
the FAQ page itself loaded on 2026-11-15 and confirms the margin bar.

## 3. Indian tax if it were done (for completeness)

AF s.66(31): a "speculative transaction" is a contract for purchase or sale of stocks and shares settled
"otherwise than by the actual delivery", except (a) specified derivatives - only those on a **recognised
stock exchange** through a SEBI-registered broker with PAN on the contract note (s.66(33)), so foreign
options never qualify - and (c) "a contract in respect of stocks and shares entered into by a dealer or
investor therein to guard against loss in his holdings ... through price fluctuations".

| Event | View A: business, speculative | View B: business, hedge (s.66(31)(c)) | View C: capital gains |
|---|---|---|---|
| Call premium received, option lapses | Speculative income at slab 35.88% | Non-speculative business income, slab 35.88% | ST gain at slab (option held < 24 m, s.2(101)); some argue a writer's premium is not from a "transfer" - weak |
| Call assigned (shares delivered at strike) | Option leg: settled by delivery, so arguably not speculative at all; premium at slab | Premium at slab | Two views: (1) premium separate ST gain at slab; (2) premium added to sale consideration of the shares -> taxed at LT 14.95% with the lot. (2) is not settled law (CA) |
| Shares on assignment | LT/ST capital gain per lot at strike price x rate on sale date; same rate as a plain sale (LT 14.95%) | same | same |
| Put bought, lapses | Speculative loss: only against speculative income, 4 years (s.113) | Business loss: against other business income, not salary; 8 years (unverified AF section) | ST capital loss on extinguishment of a right (s.2(109)(b); Grace Collis, SC 2001): against ST or LT gains, 8 years |
| Put exercised (shares sold at strike) | - | - | Put premium likely added to cost of the shares sold or a separate ST loss (CA) |

- Most likely view for a salaried investor hedging his own shares: View B or C. CBDT Circular 6/2016
  (choice between capital gains and business) is about shares and securities and does not cover
  foreign options; **unverified** that a CA will accept View C.
- Covered calls as a "hedge" under (c) are weaker than puts: a call caps the upside and only cushions
  a fall by the premium.
- Business views need ITR-3 and books. Tax audit (s.63 Table Sl.1): turnover over Rs 1 Cr (Rs 10 Cr if
  cash <= 5%). For options the ICAI Guidance Note uses the sum of favourable and unfavourable
  differences. Whether premium received is still added: the request says yes; the 2022 revision is
  reported to have dropped it - **unverified**, ICAI text not read. Either way your turnover would be far
  below Rs 10 Cr.
- Presumptive s.58 (s.44AD): the AF text (Sl.1 "any business other than" goods carriages) does not
  exclude speculation business, but it is useless here (deemed profit, ITR-4 not allowed with salary
  over Rs 50 L anyway - **unverified**).
- Schedule FA (calendar year): the IBKR account in A2 (peak, closing, gross proceeds incl. option
  sales); long puts as a foreign financial interest in A3 is a reasonable reading; written calls are a
  liability and have no A3 line - **unverified**, no CBDT guidance found.
- US tax: option premiums are not FDAP (Treas. Reg. 1.1441-2(b)(2)(i)), so no US withholding for a
  non-resident alien and no FTC to claim. IRC 871(m) dividend-equivalent withholding can apply to deep
  in-the-money options (delta >= 0.8); not to normal out-of-the-money calls (IBKR practice unverified).

## 4. Bottom line

| Item | Covered calls / protective puts | Plain staged sale (`employer-stock.md`) |
|---|---|---|
| Allowed under FEMA? | Most likely no (OI MD 1(ix)(a)) | Yes |
| Tax per $1,000 premium received (Rs 94,030) | Rs 33,738 at 35.88% (net $641); Rs 14,057 only if premium counts as LT sale price (doubtful) | - |
| Value of a $1,000 lapsed put loss | Rs 33,738 if set off at slab (View C vs ST gains); Rs 14,057 vs LT gains; zero now if speculative and no speculative income | - |
| QCOM shares if assigned | LT 14.95% on lot gain at strike, same as a sale; lot chosen by IBKR's default method unless set (check) | LT 14.95%; T1+T2 = Rs 2.54 L with highest-cost lots |
| Extra filing | ITR-3 (business views), Schedule FA detail, possible audit questions | ITR-2 capital gains |
| Penalty risk | Up to 3x sum involved | None |

Not done and still untested: no trade, no IBKR check of option permissions for an Indian-resident
account, no rupee figures for a real strike or premium.

## 5. Questions

| For | Question |
|---|---|
| AD bank (forex desk) / FEMA lawyer | 1. Has RBI "otherwise permitted" any derivative OPI for resident individuals (OI MD 1(ix)(a))? 2. Is writing a fully covered call on ESOP/RSU shares OPI in a derivative or a barred contingent liability? 3. Repatriation deadline for RSU/ESPP sale proceeds held at IBKR, and is reinvesting in ETFs a valid "reinvestment"? 4. If done in error, compounding route and amount |
| CA | 1. View A, B or C for puts/covered calls on own shares; does s.66(31)(c) apply? 2. Call premium on assignment: separate income or sale consideration? 3. Lapsed put loss: set-off and carry-forward. 4. Schedule FA lines for open options. 5. ICAI turnover rule after 2022 (premium included?) |
