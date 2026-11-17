# Outside work: employer and legal limits

## Summary
- Allowed without approval (expected): passive income (rent, interest, dividends) and personal investing, but never on inside information and only inside any trading window that applies to you.
- Needs approval first (Trust Code: outside work must not harm Microsoft or break your employee agreements; disclose conflicts and get advice or approval): teaching, paid writing, talks, YouTube, consulting outside chips, side business, board or advisory roles.
- Not allowed while employed (expected): paid work for EDA vendors (Synopsys incl. Ansys, Cadence), foundries, chip firms or competitors; expert-network calls on chips, EDA or Microsoft; any use of Microsoft, foundry or vendor data, PDKs or tool licences.
- Before acting, read your own offer letter, employment agreement and the internal Conflicts of Interest and Outside Work policies (section "Check in your own documents"). Much of this note is marked UNVERIFIED until you do.
- Not legal advice. Legal view and lawyer questions: [legal/outside-work.md](../legal/outside-work.md) and [legal/questions.md](../legal/questions.md#outside-work-and-ip) (W1-W9), owned by `finance-legal`.

Employer: Microsoft Corporation (India) Pvt Ltd or Microsoft India (R&D) Pvt Ltd - check offer letter. Location: Bengaluru per his public site, so the Karnataka shops act applies.

## Key public rules (read 2026-11-15)
| Rule | What it says | Source | Verified |
|---|---|---|---|
| Trust Code, Avoid conflicts of interest | Act in Microsoft's best interest; avoid or withdraw where a personal relationship or financial interest in another company might influence job decisions; a conflict can exist even if you think you are not affected; disclose conflicts and get advice or approval; before outside work, make sure it does not harm Microsoft's business interests or break employee agreements you signed. Internal policies named: Conflicts of Interest Policy, Conflicts of Interest Approval Tool, Outside Work Policy (all internal only) | [S1] | verified |
| Trust Code, inside information | Never trade on material nonpublic information (MNPI) of Microsoft or of companies Microsoft does business with, never tip, never recommend trades based on it. Internal: Insider Trading Policy, Restricted Trading Window Policy | [S1] | verified |
| Trust Code, confidential info and IP | Do not use confidential information for non-Microsoft business, keep it confidential after leaving; respect confidentiality of companies Microsoft works with; no third-party copyrighted material without licence | [S1] | verified |
| Trust Code, resources | Company technology may be used for personal reasons only per policy and if it does not interfere with the job; business data is Microsoft property | [S1] | verified |
| Trust Code, public statements | Do not speak on behalf of the company unless authorised; send media and analyst queries to PR or Investor Relations; disclose affiliation when endorsing Microsoft products on social media | [S1] | verified |
| Trust Code, gifts | Gifts, hospitality, travel must be reasonable with a legitimate business purpose; no cash. Internal: Accepting Gifts, Hospitality, and Travel Policy | [S1] | verified |
| Microsoft open source program | Internal guidance at aka.ms/opensource (employees only); some open source activities trigger a business and legal review; each org has an open source attorney. Rules for personal contributions are not public | [S2] | verified (that the rules are internal) |
| Indian Contract Act s.27 | Every agreement restraining anyone from a lawful profession, trade or business is void to that extent (only exception: sale of goodwill) | [S3] | verified |
| Niranjan Shankar Golikari v Century Spinning (SC, 1967) | Courts distinguish restraints during employment from those after it; a term that the employee serves only this employer during the contract is generally enforceable | [S4] | verified |
| Post-employment non-compete | Void under s.27: Percept D'Mark v Zaheer Khan (SC, 2006), negative covenant after the contract term is prima facie void (as quoted by Bombay HC); Superintendence v Murgai (SC, 1980) also cited | [S5], [L10] | verified (via finance-legal; SC 2006 text quoted, not read directly) |
| Copyright Act s.17(c), s.18, s.19 | Employer is first owner only of work made in the course of employment. Other work stays his unless he signed a written assignment (s.18, s.19: written, signed, identifies the work and rights) | [S6], [L6] | verified |
| Patents Act 1970 s.6, s.68 | Silent on private-employee inventions; the contract (written assignment) governs | [L11] | verified (finance-legal) |
| Karnataka Shops and Commercial Establishments Act 1961 (Bengaluru, applies) | No double-employment section (full text searched); managers exempt (s.3(1)(h)) | [L14] | verified (finance-legal) |
| Telangana S&E Act 1988 s.69 (only if posted in Hyderabad) | No work in any establishment on a holiday or leave under the Act; managers with control exempt (s.73(1)(a)); the IT/ITES exemption G.O. does not cover s.69 | [S7], [L13] | verified |
| OSH Code 2020 s.30 | Replaced Factories Act s.60; double-employment ban covers factories and mines only, not him | [L15] | verified (finance-legal) |
| Microsoft trademarks | Naming Microsoft truthfully in plain text (job title) is ok; no logos, nothing implying endorsement or sponsorship, not in a business or domain name | [L2] | verified (finance-legal) |
| Industrial Employment (Standing Orders) | Model standing orders cover "workmen"; a senior engineer is likely not one, and IT firms in some states have exemptions | none read | UNVERIFIED |
| 2022 moonlighting debate | Swiggy announced a moonlighting policy (outside hours, no conflict of interest); Wipro chairman called moonlighting "cheating"; most traditional firms prohibit commercial outside work. Reports that Wipro fired about 300 staff and Infosys warned staff were not read | [S10] | verified (TOI 22 Aug 2022); rest UNVERIFIED |
| Expert networks (GLG etc.) | GLG says it runs conflict and compliance checks on experts; its public expert page does not list the rules. Networks commonly bar current employees from discussing their employer, its customers and suppliers | [S11] | UNVERIFIED (rules not public) |

## Status by activity
Status: allowed / needs approval / not allowed / unknown. Sources in the Sources list, all accessed 2026-11-15.

| Activity | Status | Rule and why | Source | Verified |
|---|---|---|---|---|
| Teaching, courses (EDA, power integrity) | needs approval | Outside work rule; topic overlaps the job and Microsoft's EDA suppliers, so a conflict check is likely. Material must hold no Microsoft, foundry (TSMC, Samsung, Intel) PDK or NDA data, no vendor tool screenshots or decks under NDA, and must be made on own time and own machine (s.17(c), invention clause). No employer tool licences | S1, S6 | rule verified; approval need UNVERIFIED |
| Paid writing, books | needs approval | Outside work and confidentiality rules; publisher contract vs IP assignment clause; book on general EMIR theory is lower risk than on flows you use at work | S1, S6 | rule verified; approval need UNVERIFIED |
| Unpaid blog | allowed with limits (expected) | No confidential data, do not speak for Microsoft, state views are your own; check social media guidelines (internal) | S1 | partly verified |
| Open source (personal) | unknown | Microsoft's personal contribution rules are internal (aka.ms/opensource); code written on employer time or kit is likely Microsoft's | S2, S6 | UNVERIFIED |
| Conference talks | needs approval | Personal talks: confidentiality and no speaking for Microsoft; talks as a Microsoft engineer need authorisation. Fees or travel from EDA vendors fall under gifts and conflict rules | S1 | rule verified; process UNVERIFIED |
| Expert networks (GLG, AlphaSights, Guidepoint) | not allowed for chips, EDA, cloud or Microsoft topics; needs approval otherwise | Clients are investors; anything learned at work about Microsoft or its suppliers can be MNPI; paid outside work. Network rules usually exclude current employer topics | S1, S11 | MNPI rule verified; network rules UNVERIFIED |
| Consulting, freelance for EDA or chip firms | not allowed while employed (expected) | Synopsys (owns Ansys since 17 Jul 2025, verified [L4]) and Cadence are Microsoft suppliers (per the user), chip firms may be competitors or partners: financial interest that can influence job decisions. During-employment exclusivity clauses are enforceable (Golikari). Risk of misuse of confidential data | S1, S4 | rule verified; ban itself UNVERIFIED |
| Topmate paid 1:1 calls (existing) | Topmate: accepted by user 2026-11-15 (no action) | User decision via finance-main | - | - |
| Consulting outside the industry | needs approval | Outside work rule; no use of Microsoft time, equipment or data; Karnataka act has no double-employment rule; if posted in Hyderabad, Telangana s.69 bars work on holidays or leave (managers exempt) | S1, L14, S7 | rule verified; approval need UNVERIFIED |
| Startup, side business | needs approval | Outside work and conflict rules; invention assignment clause may claim related inventions; do not compete with Microsoft or its vendors | S1, S6 | UNVERIFIED (clause text) |
| Board, advisory roles | needs approval | Conflict of interest (financial interest in another company); advisory roles in chips or EDA likely refused | S1 | rule verified; outcome UNVERIFIED |
| Rental, passive income | allowed (expected) | Not outside work; investments in suppliers or competitors may need disclosure if they could influence decisions | S1 | UNVERIFIED (disclosure thresholds) |
| Content, YouTube (monetised) | needs approval | Paid outside work; same confidentiality and no-PDK rules as teaching; disclose affiliation; no Microsoft brand use | S1 | partly verified |
| Investing, trading (incl. MSFT) | allowed with limits | No trading on MNPI of Microsoft or companies it deals with (EDA vendors, foundries, chip suppliers like those in the watchlist); check whether a restricted trading window applies to you; no tips | S1 | rule verified; window scope UNVERIFIED |

## Check in your own documents
| Document | Look for |
|---|---|
| Offer letter and employment agreement (which entity: Microsoft Corporation (India) Pvt Ltd or Microsoft India (R&D) Pvt Ltd) | Exclusive service or full-time devotion clause; outside employment or moonlighting clause; notice period; any non-compete or non-solicit (post-employment non-compete likely void, s.27; during-employment ones enforceable) |
| Invention and confidentiality agreement | Scope of "inventions" assigned: only job-related, or all made during employment incl. own time; prior-inventions list; copyright in written or teaching material; confidentiality after leaving |
| Conflicts of Interest Policy and Outside Work Policy (internal) | Which activities need pre-approval, what counts as a supplier or competitor, honoraria and fee rules, disclosure of investments |
| Conflicts of Interest Approval Tool (named on the public Trust Code page; internal) | File a request before any paid outside work, talk, board or advisory role |
| Insider Trading Policy and Restricted Trading Window Policy (internal) | Whether you are a designated insider, blackout dates, pre-clearance, rules on trading suppliers' shares |
| Open source guidance (aka.ms/opensource, internal) | Rules for personal projects and contributions, approval steps |
| Accepting Gifts, Hospitality, and Travel Policy; Social Media Guidelines (internal) | Speaker fees, vendor-paid travel, posting about work topics |
| HR India handbook or standing orders | Dual-employment rule, leave rules, state Shops and Establishments registration |

Who to ask: your manager first, then HR, then CELA (Microsoft legal) through the internal disclosure process; Trust Code questions via the public "Report a concern" page if needed.

## Sources
All accessed 2026-11-15.
- S1: Microsoft Trust Code (Standards of Business Conduct), https://www.microsoft.com/legal/compliance/sbc/standards (PDF version dated Sept 2026 linked there, not read)
- S2: Microsoft open source program, https://opensource.microsoft.com/program/
- S3: Indian Contract Act 1872 s.27, https://indiankanoon.org/doc/1431516/
- S4: Niranjan Shankar Golikari v Century Spinning (1967), https://indiankanoon.org/doc/452434/
- S5: Superintendence Co of India v Krishan Murgai (1980), https://indiankanoon.org/doc/1186410/ (headnote)
- S6: Copyright Act 1957 s.17, https://indiankanoon.org/doc/1404402/
- S7: Telangana Shops and Establishments Act 1988 s.69, https://indiankanoon.org/doc/134632502/
- S10: Times of India, "Explained: What is moonlighting and if it's legal in India", 22 Aug 2022, https://timesofindia.indiatimes.com/business/india-business/explained-what-is-moonlighting-and-is-it-legal-in-india/articleshow/93704728.cms
- S11: GLG for experts, https://glg.com/for-experts
- L-sources, read by `finance-legal` 2026-11-15 (full list in [legal/outside-work.md](../legal/outside-work.md#sources)):
- L2: Microsoft Trademark and Brand Guidelines, https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks
- L4: Synopsys, "Synopsys Completes Acquisition of Ansys", 17 Jul 2025, https://news.synopsys.com/2025-07-17-Synopsys-Completes-Acquisition-of-Ansys
- L6: Copyright Act 1957 (s.18, s.19), https://indiankanoon.org/doc/1136195/
- L10: VFS Global v Suprit Roy, Bombay HC 2007 (quotes Percept D'Mark v Zaheer Khan, SC 2006), https://indiankanoon.org/doc/1547420/
- L11: Patents Act 1970 (s.6, s.68), https://indiankanoon.org/doc/1937976/
- L13: Cognizant v Asst Commissioner of Labour, Telangana HC 2020 (IT exemption G.O.), https://indiankanoon.org/doc/72700527/
- L14: Karnataka Shops and Commercial Establishments Act 1961, https://indiankanoon.org/doc/126525931/
- L15: OSH Code 2020 s.30, https://indiankanoon.org/doc/93015120/
