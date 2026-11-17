# Trading in suppliers and vendors (insider rules)

## Summary
- Microsoft's public insider policy (filed with the SEC, 2026) applies to all employees. It bars trading any public company, including customers, partners and competitors, while you hold material nonpublic information (MNPI) about it that you learned through your job. For regular employees it has no restricted list, pre-clearance or blackout window; those apply only to officers and staff Microsoft notifies (they cover Microsoft shares).
- The law says the same. In the US, Rule 10b-5 and the misappropriation theory (O'Hagan) cover trades on US exchanges through IBKR wherever you live. In the EU, MAR covers Infineon on Xetra, including from India. In India, SEBI PIT covers only securities listed in India.
- Verdicts: Synopsys skip (you use its RedHawk-SC daily at work). Infineon, MPS and Vicor: ask Microsoft's insider-trading contact first (power-delivery vendors in an open patent case that touches hyperscalers). FormFactor: ok with care.
- Simple rule: skip any company whose products, deals, roadmaps or selection you touch at work; for the rest, trade only on public sources and keep a dated note of them.
- Needed from you: whether Microsoft has ever told you that you are a designated insider, and which power and EDA vendors you deal with at work.

Owner: `finance-legal`. Written 2026-11-15. Not legal advice. Request from `finance-scout` (expertise-edge ideas in `~/.local/share/superpowers/finance/opportunities/expertise-edge.md`). Questions: [T1-T6](../questions.md#trading-in-suppliers-insider-rules). Related: [outside-work.md](../outside-work.md). Sources I1-I12 below, all read 2026-11-15; "not verified" = primary text not read.

## Microsoft policy (public parts)
| Item | What the filed policy says | Source |
|---|---|---|
| Who is covered | General Insider Trading Policy: "This policy applies to all employees" | I1 |
| Other companies | No buying or selling securities of any publicly traded company while holding MNPI about it acquired through your role at Microsoft, "including but not limited to a customer or partner of Microsoft or an economically-linked company such as a competitor". Also bars gifting and other economic exposure, including prediction markets or event contracts | I1 |
| Examples of material information | Financial results; significant product plans, developments or problems; changes in the terms of a significant contract with a major customer or partner, or gaining or losing one; acquisitions; litigation; cybersecurity incidents | I1 |
| Tipping | Do not disclose MNPI, and do not recommend or suggest trades in a company you hold MNPI about, even without disclosing it | I1 |
| Confidential information | No prediction-market positions using confidential information about Microsoft, customers, vendors, partners or competitors (wider than MNPI) | I1 |
| Trading windows | Restricted Trading Window Policy: only officers (CVP and above) and other designated employees with regular access to MNPI; covers Microsoft securities only; "you will know you are an Insider ... because you will be notified" | I1, I2 |
| Pre-clearance | Only Section 16 officers, directors and senior officers who are notified; Microsoft securities only | I2, I3 |
| Restricted list of other companies | None in the public text. Any internal list, country supplement (section 8 is blank in the filed copy) or team rule is internal | I1 |
| Penalties | Discipline up to termination; civil and criminal fines and prison under the law | I1 |

## Law
| Law | What it says | Applies to you when | Source | Verified |
|---|---|---|---|---|
| US Rule 10b-5 | Bans fraud or deceit in connection with the purchase or sale of any security | US-listed shares (SNPS, MPWR, VICR, FORM) bought or sold via IBKR | I4 | yes |
| US Rule 10b5-1(b) | A trade is "on the basis of" MNPI if the trader was aware of it when trading | Same | I5 | yes |
| US v O'Hagan, 521 US 642 (1997) | Misappropriation theory: trading on confidential information taken in breach of a duty to its source (e.g. your employer) violates 10b-5, even if you owe nothing to the traded company | Vendor information you learn through Microsoft | I6 | yes (syllabus) |
| Morrison v National Australia Bank, 561 US 247 (2010) | s.10(b) covers securities listed on US exchanges and other US transactions; where you live does not matter | US-listed names; not Infineon on Xetra | I7 | yes (syllabus) |
| EU MAR, Regulation 596/2014 | Art 8, 14: no insider dealing, recommending or disclosure; Art 8(4)(c) covers anyone with inside information from employment; Art 2(4) applies to acts in a third country | Infineon (Xetra) and its ADR | I8 | yes |
| SEBI PIT Regulations 2015 | Reg 4(1): no insider shall trade securities "listed or proposed to be listed on a stock exchange" while holding UPSI; "insider" includes anyone holding UPSI, however obtained (reg 2(1)(g)) | Only Indian-listed securities; our reading is that "stock exchange" means a recognised Indian exchange | I9, I10 | text yes; scope reading not verified |

## What you may not use
| Never trade on | Why it is risky |
|---|---|
| EDA vendor roadmaps, beta features, bug or quality issues shared under NDA (RedHawk-SC, Voltus) | Product plans and problems are listed as material (I1); vendor confidential |
| Licence, renewal or pricing talks with Synopsys or Cadence | Changes in a significant contract are listed as material (I1) |
| Microsoft silicon plans, volumes, schedules, unannounced tape-outs | Microsoft MNPI; also moves suppliers' shares |
| Which power, module or test vendor Microsoft chose or is evaluating | Gaining or losing a major customer is material (I1) |
| Microsoft's response to Vicor's patent claims (licence or not) | Litigation and contract information (I1, I11) |
| Fine: conference papers, patents, ITC and court filings, company releases, teardowns, your own general engineering judgment | Public or your own skill, not MNPI |

## Per-name verdicts
Microsoft's public disclosures (Maia, Cobalt) name no power or test vendor that we found; anything beyond your own role is unknown.

| Name | Link to your work | Verdict | Reason |
|---|---|---|---|
| Synopsys (SNPS, Nasdaq) | Owns Ansys since 17 Jul 2025 (I12); you use RedHawk-SC daily at work (from you); you likely see its support, roadmap and licence matters (assumption) | skip | You cannot separate public facts from what you see at work; holding it also makes vendor decisions you influence look conflicted |
| Infineon (IFX, Xetra) | Power stages and VR modules for AI boards; whether Microsoft silicon uses them is unknown; respondent in Vicor's ITC case (I11) | ask first | If your PDN signoff work shows the VR or package vendor, skip; MAR applies from India |
| Monolithic Power Systems (MPWR, Nasdaq) | Same product area; supplier to Microsoft unknown; respondent in Vicor's ITC case (I11) | ask first | Same as Infineon |
| Vicor (VICR, Nasdaq) | Power modules; complainant in the ITC case started 9 Oct 2026; says hyperscalers using respondents' parts will need a Vicor licence (I11) | ask first | Microsoft's exposure or licence talks would be MNPI if you hear of them |
| FormFactor (FORM, Nasdaq) | Probe cards and test; no link to power-integrity signoff known | ok with care | Trade on public sources only; skip if you learn Microsoft test or vendor plans |
| Cadence (CDNS; not in the list) | Voltus, the other signoff tool you use | skip | Same as Synopsys |

"Ask first" = email Microsoft's insider-trading contact (named only internally, I1) before buying, and keep the reply; or skip.

## Needed from you
| Item | Why |
|---|---|
| Have you ever been told you are subject to the Restricted Trading Window Policy (a designated insider)? | Windows and pre-clearance (I2) |
| Which vendors you deal with at work (tools, support, evaluations, licences) | Per-name verdicts |
| Whether your work shows Microsoft's VR, package or power-module vendors | Infineon, MPS, Vicor |
| Any internal restricted list or team rule on vendor shares (internal policy site) | Not public |
| Current holdings in these names, if any | Whether a sell needs the same check |

## Sources
All read 2026-11-15.
- I1: Microsoft General Insider Trading Policy, Exhibit 19.1 to the FY2026 10-K (filed 2026-07-29), https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-ex19_1.htm
- I2: Microsoft Restricted Trading Window Policy, Exhibit 19.2, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-ex19_2.htm
- I3: Microsoft Insider Trading Compliance and Preclearance Policies for Section 16 Officers and Directors, Exhibit 19.3, https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-ex19_3.htm
- I4: 17 CFR 240.10b-5, https://www.law.cornell.edu/cfr/text/17/240.10b-5
- I5: 17 CFR 240.10b5-1, https://www.law.cornell.edu/cfr/text/17/240.10b5-1
- I6: United States v O'Hagan, 521 US 642 (1997), syllabus, https://www.law.cornell.edu/supct/html/96-842.ZS.html
- I7: Morrison v National Australia Bank, 561 US 247 (2010), https://www.law.cornell.edu/supremecourt/text/08-1191
- I8: EU Market Abuse Regulation 596/2014, Art 2(4), 8, 14, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0596
- I9: SEBI (Prohibition of Insider Trading) Regulations 2015, reg 2, https://indiankanoon.org/doc/15987491/ (indiankanoon copy; latest SEBI amendments not checked)
- I10: Same, reg 4, https://indiankanoon.org/doc/63173976/
- I11: Vicor press release, "USITC institutes investigation of Vertical Power Delivery (VPD) modules ...", 12 Oct 2026, https://www.vicorpower.com/press-room/2026/usitc-institutes-investigation-of-vertical-power-delivery-vpd-infrigment
- I12: Synopsys, "Synopsys Completes Acquisition of Ansys", 17 Jul 2025, https://news.synopsys.com/2025-07-17-Synopsys-Completes-Acquisition-of-Ansys
