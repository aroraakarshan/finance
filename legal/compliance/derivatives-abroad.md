# Options on foreign shares (covered calls, protective puts)

## Summary
- No permission found: OPI "shall not be made in ... any derivatives unless otherwise permitted by Reserve Bank" (OI Directions para 1(ix)(a)), and OI Rules rule 8 bars any investment abroad not provided for. No RBI text permits options for resident individuals.
- So both (1) covered calls on the 761 QCOM at IBKR and (2) protective puts paid from USD already at IBKR look not allowed under FEMA, even with no new remittance and no margin. This is our reading; RBI has no individual-hedging exception.
- The RBI hedging rules (Risk Management and Inter-Bank Dealings) cover currency risk with AD banks in India, not equity options abroad.
- Allowed alternative for the planned exit: sell the shares (limit or stop orders), which is a permitted transfer of OPI. Ask a CA/AD bank before any option trade (questions below).

Owner: `finance-legal`. Written 2026-11-15 on a question from `finance-trader`. Not legal or tax advice; findings and questions for a CA/AD bank ([questions](../questions.md) C15-C19). The user decides and acts. Tax effects: `finance-tax`, [tax/investment-types.md](../../tax/investment-types.md) section 3 ("Foreign derivatives"). Related: [permitted holdings](fema-lrs.md#permitted-holdings-overseas-portfolio-investment-opi), [180-day rule](fema-lrs.md#180-day-rule-reinvestment-and-dividends).

All texts read 2026-11-15 on rbi.org.in or indiankanoon.org (URLs in [Sources](#sources)).

## The rules that apply

| Rule | Text (short quote) | Para | Source, version |
|---|---|---|---|
| FEMA: dealing in foreign security | "Save as otherwise provided in this Act, rules or regulations ... or with the general or special permission of the Reserve Bank, no person shall (a) deal in or transfer any foreign exchange or foreign security ..." | FEMA s.3(a) | [D1] Act 1999 as on indiankanoon (later amendments not checked) |
| FEMA: capital account transactions | RBI may "prohibit, restrict or regulate ... transfer or issue of any foreign security by a person resident in India" | FEMA s.6(3)(a) | [D1] original 1999 text; s.6 was amended in 2015 (current wording not verified) |
| General bar | "Save as otherwise provided in the Act or these rules or the regulations made or directions issued under the Act, no person resident in India shall make or transfer any investment or financial commitment outside India." | OI Rules rule 8 | [L5] G.S.R. 646(E), 22 Aug 2022 |
| OPI meaning | "investment, other than ODI, in foreign securities, but not in any unlisted debt instruments or any security issued by a person resident in India who is not in an IFSC" | OI Rules rule 2(1)(s) | [L5] |
| Individuals' route | Resident individual may make "OPI, including by way of reinvestment", within the LRS ceiling | OI Rules Schedule III para 1(1), 1(2)(ii) | [L5] |
| No derivatives | "OPI shall not be made in: any unlisted debt instruments; or any security which is issued by a person resident in India who is not in an IFSC; or any derivatives unless otherwise permitted by Reserve Bank; or any commodities including Bullion Depository Receipts" | OI Directions Part I para 1(ix)(a), third item | [L3] A.P. (DIR Series) Circular No. 12, 22 Aug 2022; page shows no later update; the word "derivative" appears only here; no "hedg" anywhere |
| OI Regulations | No mention of derivatives or hedging | OI Regulations (whole text searched) | [L4] FEMA 400/2022-RB, 22 Aug 2022 |
| LRS: margin | "All other transactions which are otherwise not permissible under FEMA and those in the nature of remittance for margins or margin calls to overseas exchanges/ overseas counterparty are not allowed under the Scheme." | LRS MD para 5 | [L2] updated 6 Sep 2024 |
| LRS: what individuals may do | Permissible capital account transactions: foreign currency account, property, ODI and OPI "in accordance with" the OI Rules/Regulations/Directions | LRS MD para 6 | [L2] |
| LRS FAQ | Not available for "Remittance from India for margins or margin calls to overseas exchanges / overseas counterparty" | LRS FAQ Q2 item 2 | [L1] updated 6 Apr 2023 |

## Question 1: covered calls on QCOM already held at IBKR

| Point | Finding | Basis |
|---|---|---|
| Is a written call "OPI in derivatives"? | Not defined. A written call is a derivative contract on a foreign security; para 1(ix)(a) bars OPI "in any derivatives". Writing is not buying a security, but rule 8 bars any investment or transfer abroad not provided for, and no rule or direction provides for options | [L3][L5 r.8] (reading) |
| No new remittance, no margin | The LRS margin bar (para 5) is about remittances from India; it does not make an otherwise barred derivative allowed | [L2 para 5-6] |
| Shares as collateral | Lodging the shares as cover is part of the option position; no FEMA text allows it for individuals | not verified |
| If assigned | Delivery of QCOM = sale (transfer) of OPI, which by itself is allowed; proceeds fall under the 180-day rule | [L5 Sch. III][L2 para 17] |
| Premium received | Foreign exchange received abroad: reinvest or repatriate within 180 days | [L2 para 17][L8 reg 7] |
| Result | Not allowed as we read it; no RBI permission found | - |

## Question 2: protective puts paid from USD already at IBKR

| Point | Finding | Basis |
|---|---|---|
| Buying a put | Acquiring a derivative = OPI in derivatives, barred "unless otherwise permitted by Reserve Bank" | [L3 para 1(ix)(a)] |
| Paid from proceeds/dividends abroad | Reinvestment is allowed only into permitted OPI ("OPI, including by way of reinvestment"); money abroad does not widen what is permitted | [L5 Sch. III para 1(2)(ii)][L2 para 17] |
| Result | Not allowed as we read it | - |

## Is there a hedging exception?

| Text | What it covers | Individuals? | Source |
|---|---|---|---|
| Master Direction - Risk Management and Inter-Bank Dealings (FMRD MD 1/2016-17, updated 1 Oct 2026), Part A Section I | "Contracted/anticipated exposure" means **currency risk** on permissible transactions; AD banks in India may offer FX derivative contracts "for the purpose of hedging" (para 2.3) | Currency risk only, via AD banks; not equity price risk on foreign shares | [R1] |
| FEM (Foreign Exchange Derivative Contracts) Regulations 2000 (FEMA 25/RB-2000) | Basis of the above | Not read separately (not verified) | via [R1] |
| Master Direction - Hedging of Commodity Price Risk and Freight Risk in Overseas Markets (2022, updated 15 Apr 2024) | Commodity and freight risk | Not equity; title only read (not verified in detail) | [R2] |
| OI Directions / Regulations | No hedging paragraph | - | [L3][L4] |

Result: no hedging exception for a resident individual's equity price risk on foreign shares.

## IBKR side

- Research note [not-allowed.md](../../research/themes/ibkr-global/not-allowed.md) says options are "Available at IBKR with options/futures permissions [S22]". S22 there is the IBKR crypto page, so the claim has no matching source; whether IBKR approves US options for this account: not verified.
- The user's account is with Interactive Brokers LLC per the filed CY2025 Schedule FA ([filed returns](schedule-fa.md#filed-returns)); IB India is for Indian markets ([research](../../research/themes/ibkr-global/rules.md)). Broker approval would not make it FEMA-compliant.

## Questions for a CA / AD bank

| # | Question |
|---|---|
| C15 | Is writing covered calls on foreign shares already held (no remittance, no margin) barred by OI Directions para 1(ix)(a) / OI Rules rule 8, or is it outside "investment"? |
| C16 | Is buying puts with USD already abroad (sale proceeds, dividends) barred the same way? |
| C17 | Is there any RBI permission or route (general or specific, e.g. via the AD bank) for a resident individual to hedge price risk on employer shares held abroad? |
| C18 | If the user ever wrote options in the past: consequences and how to regularise (compounding)? |
| C19 | Is a stop-loss or limit sell order on the shares (no derivative) fully within OPI rules? |

## Sources

All read 2026-11-15.
- [D1] FEMA 1999 s.3, s.6: https://indiankanoon.org/doc/165125/ , https://indiankanoon.org/doc/600757/
- [L1] RBI LRS FAQ (updated 2023-04-06): https://www.rbi.org.in/commonman/English/Scripts/FAQs.aspx?Id=1834
- [L2] RBI Master Direction LRS (updated 2024-09-06): https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192
- [L3] RBI OI Directions 2022 (2022-08-22): https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12381
- [L4] OI Regulations 2022: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12380&Mode=0
- [L5] OI Rules 2022: https://rbi.org.in/scripts/bs_viewcontent.aspx?Id=5087
- [L8] FEMA 9(R)/2015-RB reg 7: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=10258&Mode=0
- [R1] Master Direction - Risk Management and Inter-Bank Dealings (updated 2026-10-01): https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10485
- [R2] Master Direction - Hedging of Commodity Price Risk and Freight Risk in Overseas Markets (updated 2024-04-15): https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12427
- Full compliance source list: [sources.md](sources.md).
