# Startup stakes and owning a small business (employer, contract, succession)

## Summary
- Startup stake: Microsoft's public Trust Code asks you to disclose a financial interest in another company that could influence your job and get advice or approval. Chip, EDA, power or design-IP startups are likely suppliers, customers or competitors, so disclose before investing. Whether formal pre-approval is required is internal.
- Investing: Indian private placements need a named PAS-4 offer letter, payment from your own bank account, allotment within 60 days and a PAS-3 filing. Insist on a shareholders' agreement with tag-along, information rights and pre-emptive rights ([checklist](#b3-shareholders-agreement-checklist)).
- Succession: nominate on Form SH-13 (or in demat), but the nominee holds for your heirs (Shakti Yezdani 2023). Shares and SAFE/convertible rights pass under your will, so list them in it.
- Small online business: owning one is outside business, so disclose it. Code written by a hired operator belongs to the operator unless assigned in writing; code you write yourself may be caught by your invention clause.
- Purchase contract: escrow, verified revenue (direct analytics and Stripe/bank access), IP and domain assignment, indemnity with a holdback, and a reasonable seller non-compete (s.27 Exception 1, sale of goodwill).

Owner: `finance-legal`. Written 2026-11-15. Not legal advice. Request from `finance-income` ([private-investing.md](../income/private-investing.md), [business.md](../income/business.md)). Foreign stakes and foreign businesses (FEMA ODI): [odi-private.md](compliance/odi-private.md), not covered here. Questions: [P1-P8](questions.md#startup-stakes-and-small-business). Topmate is closed ([accepted](outside-work.md#accepted-risk-topmate)). Sources R1-R14 at the end, read 2026-11-15; "not verified" = primary text not read.

## B1. Employer rules on a startup stake
| Item | What the public text says | Source |
|---|---|---|
| Conflicts | Avoid or withdraw where a personal relationship or financial interest in another company might influence job decisions; a conflict can exist even if you are sure it does not affect you; disclose conflicts and get advice or approval | R1 |
| Tools named | Conflicts of Interest Policy, Conflicts of Interest Approval Tool, Outside Work Policy (all internal) | R1 |
| Insider policy (Ex 19.1) | Covers MNPI about publicly traded companies only; an unlisted startup is not covered, but Microsoft confidential information may never be used for it (Trust Code) | R2, R1 |
| Board or advisor seat | Outside work; must not harm Microsoft or break signed agreements | R1 |
| Thresholds, pre-approval vs notice, family holdings | Not public | needed from user |

Where the line falls for your role (assessment, not a rule):

| Startup type | Likely relation to Microsoft | Conflict for you |
|---|---|---|
| EDA or signoff tools (IR-drop, EM, PDN) | Possible vendor to your own team | high: you could influence tool choice; disclose, likely refused |
| Design IP, power IP, VR or packaging | Possible supplier to Microsoft silicon | medium-high: disclose |
| AI accelerator or chip maker | Possible competitor or customer | medium: disclose |
| Deep tech unrelated to chips or cloud | None known | low: check the internal policy anyway |

Trading in listed suppliers: [insider-trading.md](compliance/insider-trading.md). Outside work and IP: [outside-work.md](outside-work.md).

## B3. Shareholders' agreement checklist
| Clause | What to want as a small holder | Red flag |
|---|---|---|
| ROFR / ROFO | Applies to founders' sales too; short notice period | Only on investors; long lock that blocks every sale |
| Tag-along | Sell on the same terms if founders or a majority sell | Missing |
| Drag-along | Only above a high threshold and minimum price; same price per share for all | Low threshold; you bear warranties and costs |
| Information rights | Yearly audited accounts, cap table, notice of new rounds | None, or only for large holders |
| Pre-emptive rights | Right to keep your percentage in new rounds | Waived, or major investors only |
| Anti-dilution | Same protection as other investors of your class (broad-based weighted average is usual) | Full ratchet for others only |
| Transfer restriction, lock-in | Clear exit routes (secondary sale, buyback) | Total ban, or board consent "at discretion" |
| Liquidation preference | 1x non-participating for your class, same rank as peers | Senior participating preferences above you |
| Exit | Target window for sale or IPO; put option or buyback if missed | None |
| iSAFE / CCPS terms | Valuation cap, discount, conversion trigger and long-stop date | No cap; conversion only at company discretion |

Company-law points (unlisted Indian company):

| Rule | What it says | Source | Verified |
|---|---|---|---|
| s.42 private placement | Offer only by private placement offer letter to persons named beforehand; payment by banking channel, not cash; allot within 60 days of receiving money or refund within 15 days (then 12% interest); money kept in a separate bank account; non-compliant offer is a public offer | R3 | yes (indiankanoon copy, pre-2017 text; 2017 substitution not read) |
| PAS Rules r.14 | Special resolution per offer with price basis and valuer; at most 200 offerees per FY per kind of security (equity, preference, debenture counted separately); Form PAS-4 addressed to you by name; record in PAS-5; payment from your own bank account; return of allotment PAS-3 within 15 days | R4 | yes |
| s.62(1)(c) | Shares to any persons need a special resolution and a price set by a registered valuer's report | R5 | yes |
| s.55 | Irredeemable preference shares not allowed; redeemable within 20 years. CCPS convert instead of being redeemed | R6 | yes (CCPS practice not verified) |
| iSAFE | A market name for an agreement for CCPS; no separate statutory form | none | not verified |
| Convertible note | Exempt from deposit rules only for a DPIIT startup taking Rs 25 L or more in one tranche, converted or repaid within 10 years | none | not verified |

## B4. Nomination and succession
| Item | Rule | Source | Verified |
|---|---|---|---|
| Nomination | s.72: any holder of securities may nominate; SCD Rules r.19: Form SH-13, company records it within 2 months; nominee may register himself or transfer | R7, R8 | yes |
| Nominee status | Nominee holds for the legal heirs; nomination does not override the will or personal law ([nominee vs legal heir](estate/india-rules.md#nominee-vs-legal-heir)) | Shakti Yezdani 2023 | yes (see india-rules.md) |
| Transmission | s.56(2): company registers transmission by operation of law on intimation; heirs show a death certificate, the will or a succession certificate as the articles and board require | R9 | s.56(2) yes; documents per company not verified |
| Demat for private companies | PAS r.9B (2023): private companies other than small companies must issue securities only in demat, within 18 months of the FY ending on or after 31 Mar 2023; holders must dematerialise before transfer or new subscription | R10 (secondary) | rule text and any later extension not verified |
| Demat nomination | If held in demat, the depository nomination rules apply ([demat nomination](estate/india-rules.md#demat-and-mf-nomination-sebi)) | india-rules.md | yes |
| SAFE, iSAFE before conversion, convertible notes | Contract rights, not shares: no SH-13; they pass under the will or personal law; check the contract allows transfer to heirs | none | not verified |
| What heirs need | Copies of SHA, share certificates or demat statement, SAFE agreements, company contacts, cap-table entry; listed in the family sheet ([template](estate/family-info-template.md)) | - | - |

## C1. Employer rules on owning a small online business
| Point | View | Source |
|---|---|---|
| Outside business | Trust Code: outside work must not harm Microsoft or break signed agreements; disclose conflicts; Outside Work Policy is internal. Owning a business run by a hired operator is still a business interest | R1 |
| Operator writes the code | A contractor is not under a contract of service, so s.17(c) does not apply: the operator owns the code unless he assigns it in a signed writing (s.18, s.19). Take an IP assignment from the operator and from the seller | R11, R12 |
| You write code yourself | Your own time and kit: yours under s.17(c), unless your invention clause assigns it ([IP clauses](outside-work.md#clauses-to-look-for)) | R11 |
| Subject matter | Avoid products in Microsoft's lines or using Microsoft or vendor confidential information | R1 |

## C3. Purchase contract checklist
| Clause | What to want | Red flag |
|---|---|---|
| Escrow | Money held by a neutral escrow agent until assets transfer and an inspection period ends (Flippa offers FlippaPay and Escrow.com) | Direct payment to the seller |
| Revenue and traffic proof | Read-only access to analytics, Stripe or payment processor and bank statements for 12-24 months; check against tax filings | Screenshots or PDFs only |
| Warranties | Revenue, no undisclosed debts, licences valid, no IP claims, accounts and customers genuine | "As is" sale |
| Indemnity and caps | Indemnity for breach of warranty, a cap near the price, survival 12-24 months, part of the price held back | Cap below 20% of the price; no holdback |
| IP assignment | Written assignment of code, content, domain, trademarks and accounts; operator and freelancer assignments; open-source licence list | Seller keeps the code or domain |
| Transition support | Defined hours for 30-90 days, handover of supplier and customer contacts | None |
| Seller non-compete | Reasonable time and market | Unlimited; or no non-compete at all |
| Governing law | Indian law and courts for an Indian seller; foreign seller: the contract's law decides, and an Indian court may not enforce a foreign judgment easily | Foreign law with no review |

Seller non-compete: Contract Act s.27 voids restraints of trade, except that "one who sells the goodwill of a business may agree with the buyer to refrain from carrying on a similar business, within specified local limits, so long as the buyer ... carries on a like business therein, provided that such limits appear to the Court reasonable" (R13). For an online business, "local limits" means defining the market (products, customers) and a time limit; whether a worldwide online limit is "reasonable" is a lawyer question (P7).

## Needed from you
| Item | Why |
|---|---|
| Internal Conflicts of Interest Policy: thresholds, notice vs pre-approval, family holdings | B1, C1 |
| Your invention and IP clause text | C1 |
| For each startup: SHA draft, PAS-4, cap table, whether it is a small company | B3, B4 |
| For a business: seller country, asset vs share purchase | C3; ODI note |

## Differences from income notes
| Note says | Finding |
|---|---|
| private-investing.md: "file the Microsoft conflict-of-interest pre-clearance" | Public text says disclose and get advice or approval; "pre-clearance" is used only for officers' Microsoft trades (Ex 19.3). Whether a stake needs pre-approval is internal |
| private-investing.md: 200-person limit from a secondary source | Verified in PAS r.14(2), counted per kind of security |
| private-investing.md: "no board/advisor seat without approval" | Not in the public text; follows from the outside-work rule; internal policy decides |
| business.md: operator-run business | Needs an IP assignment from the operator (not covered there) |

## Sources
All read 2026-11-15.
- R1: Microsoft Trust Code, https://www.microsoft.com/en-us/legal/compliance/sbc/standards
- R2: Microsoft General Insider Trading Policy, Ex 19.1 to FY2026 10-K, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-ex19_1.htm
- R3: Companies Act 2013 s.42, https://indiankanoon.org/doc/91454896/
- R4: Companies (Prospectus and Allotment of Securities) Rules 2014 r.14, https://indiankanoon.org/doc/7075979/
- R5: Companies Act 2013 s.62, https://indiankanoon.org/doc/80189292/
- R6: Companies Act 2013 s.55, https://indiankanoon.org/doc/121078868/
- R7: Companies Act 2013 s.72, https://indiankanoon.org/doc/162447399/
- R8: Companies (Share Capital and Debentures) Rules 2014 r.19, https://indiankanoon.org/doc/80572297/
- R9: Companies Act 2013 s.56, https://indiankanoon.org/doc/167981014/
- R10: taxguru, rule 9B dematerialisation for private companies (secondary), https://taxguru.in/company-law/dematerialisation-securities-private-companies.html
- R11: Copyright Act 1957 s.17, https://indiankanoon.org/doc/1404402/
- R12: Copyright Act 1957 s.18, s.19, https://indiankanoon.org/doc/1136195/
- R13: Indian Contract Act 1872 s.27, https://indiankanoon.org/doc/1431516/
- R14: Flippa escrow page (FlippaPay and Escrow.com), https://flippa.com/escrow
