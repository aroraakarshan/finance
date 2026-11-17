# Indian rules: nominations, transmission, will

## Summary
Nominees get Indian assets quickly, but they hold them for the legal heirs: the will (or the
personal law) decides who finally owns. So set nominees on every account and make them match the
will. Probate is no longer compulsory anywhere in India (from 20 Dec 2025), and SEBI now allows
simpler demat transmission up to Rs 30 L. India has no inheritance tax.

Part of [Estate and nominations](README.md). Owner `finance-legal`; all sources read 2026-11-15
unless stated; not legal advice. Full source list: [sources.md](sources.md).

## Nomination limits by account

| Account | Max nominees | Rule | Source |
|---|---|---|---|
| Demat, MF folio | 3 | % optional (equal if blank); opt-out allowed; no freeze | SEBI 29 May 2026 |
| Bank deposit | 4 | Simultaneous (with %) or successive | Banking Companies (Nomination) Rules 2025 |
| Bank locker, safe custody | 4 | Successive only | Same, rule 4 |
| EPF | One or more | Must be family if a family exists; marriage voids earlier nomination | EPF Scheme para 61 |
| NPS | One or more | Same family and marriage rules as EPF | PFRDA Exit Regulations 2015 reg. 32 |
| PPF | Not verified | Nomination in the opening form; account closes at death | PPF Scheme 2019 para 14 |

## Demat and MF nomination (SEBI)
- SEBI circular SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2026/12676, 29 May 2026, "Modified Norms for
  Nomination in Demat Accounts and Mutual Fund Folios", in force 1 Sep 2026; applies to existing
  accounts and folios too (para 11):
  - Up to 3 nominees (para 5.1). New single-holder accounts must nominate or sign an opt-out
    (para 4.1); optional for joint accounts (4.2); all joint holders must sign changes (4.3).
  - Mandatory fields: name, relationship, date of birth if minor (para 7a). Share % optional;
    blank = equal shares (7b).
  - Online with e-sign or OTP 2FA; offline wet signature, no witness (para 6.2).
  - Holding statements print nominee names or Yes/No (para 10.1); accounts without a nominee get
    reminders, not a freeze (para 10.2).
  - It supersedes the 10 Jan 2025 "Revise and Revamp" circular (which allowed up to 10 nominees)
    and the 10 Jun 2024 circular that removed the freeze (para 15).
  - https://www.sebi.gov.in/sebi_data/attachdocs/jun-2026/1780397706130.pdf
- Not verified: whether nominations made under the old 10-nominee rule (Mar 2025 - Aug 2026)
  with more than 3 names stay valid. Question E7.

## Transmission of securities (SEBI)
SEBI circular HO/38/13/11(14)2026-MIRSD-POD/I/17111/2026, 23 Jul 2026, in force 30 days after
issue (about 22 Aug 2026):
https://www.sebi.gov.in/legal/circulars/jul-2026/ease-of-doing-investment-and-ease-of-doing-business-simplification-and-standardisation-of-the-framework-for-transmission-of-securities_103030.html

| Case | Documents heirs need | Para |
|---|---|---|
| Nominee registered | Transmission form, nominee's CML, verifiable death certificate, SOA or certificates; the entity is fully discharged | Annexure 4.1 |
| No nominee, quick route (QTP): demat up to Rs 30,000; MF/physical up to Rs 10,000 | Form-cum-undertaking and proof of relationship; only parents, spouse, children, parents-in-law | 3.2, 4.2.2.1 |
| No nominee, simplified: demat up to Rs 30 L per beneficial owner; MF units in SOA form up to Rs 10 L per AMC | + notarised indemnity bond and affidavit-cum-NOC from all legal heirs (or a family settlement deed) | 3.2, 4.2.2.2 |
| No nominee, above the simplified limit | Affidavit-cum-NOC and either copy of will + indemnity, or legal heirship certificate (Tehsildar or equivalent) + indemnity, or succession certificate / letter of administration / court decree | 4.2.2.3 |
| Any case | Probate no longer mandatory | 3.3 |

- SEBI circular SEBI/HO/MIRSD/MIRSD-PoD/P/CIR/2025/130, 19 Sep 2025: "The nominee acts as a
  Trustee ... and transfers the securities to the legal heir"; nominee-to-heir transfers use
  reason code TLH (from 1 Jan 2026) so the nominee is not taxed on them.
  https://www.sebi.gov.in/legal/circulars/sep-2025/ease-of-doing-investment-smooth-transmission-of-securities-from-nominee-to-legal-heir_96711.html
- Practical size check: AngelOne holds about Rs 26.2 L in one demat (stocks Rs 5.75 L) plus MF
  folios per AMC, so without a nominee each would likely fall in the simplified band.

## Nominee vs legal heir
- Supreme Court, Shakti Yezdani v. Jayanand Jayant Salgaonkar, Civil Appeal 7107 of 2017,
  14 Dec 2023, 2023 INSC 1076 (paras 45-47): nomination under Companies Act s.109A (now s.72) and
  Depositories bye-law 9.11 is "for a limited purpose"; it gives the company a discharge but
  "does not override the succession laws ... there is no third mode of succession". Heirs under
  the will or personal law own the shares; the nominee holds them for them.
  https://api.sci.gov.in/supremecourt/2017/3101/3101_2017_7_1501_49073_Judgement_14-Dec-2023.pdf
- SEBI 2025 and 2026 circulars ([transmission](#transmission-of-securities-sebi)) now say the
  same: nominee = trustee for legal heirs.
- Exception: life insurance nominees who are parents, spouse or children
  ([insurance](insurance.md#nomination-and-assignment-rules)).
- Effect: nominations make claims fast; the will decides who finally owns. Nominee and will
  should agree, or the nominee must hand over to different heirs.

## Bank deposits and lockers
- Banking Companies (Nomination) Rules 2025, G.S.R. 790(E), 27 Oct 2025, in force 1 Nov 2025:
  deposits: up to 4 nominees, successively or simultaneously (rule 2(1)); lockers and safe
  custody: up to 4, successive only (rule 4). Simultaneous = defined % each; successive = in order
  of priority. https://thc.nic.in/Central%20Governmental%20Rules/Banking%20Companies%20(Nomination)%20Rules,%202025.pdf
- RBI Nomination Facility Directions 2025 (RBI/2025-26/95, 28 Oct 2025, in force 1 Nov 2025):
  made under the Banking Laws (Amendment) Act 2025, which amended BR Act s.45ZA, 45ZC, 45ZE; if a
  simultaneous nominee dies first, that share is paid as if no nominee (para 10).
  https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12919
- Not verified: Act gazette text (PDF failed to load).

## EPF, EPS, EDLI
- EPF Scheme 1952 para 61 (indiankanoon text): nomination in Form 2; with a family, nominees must
  be family members, else invalid (61(3)); a nomination made before marriage becomes invalid on
  marriage (61(3) proviso); acquiring a family voids a non-family nomination (61(4)).
  https://indiankanoon.org/doc/41895570/
- Not verified: EDLI and EPS nominee rules, UAN e-nomination steps, para 70 payout without a
  nominee, and whether passbooks under Qualcomm/NXP/Microsoft share one UAN.

## NPS
- PFRDA (Exits and Withdrawals under NPS) Regulations 2015, reg. 32: nomination required at
  joining; family-only rule and marriage rule like EPF; nominee receives "to the exclusion of all
  other persons" (still subject to the [nominee vs heir](#nominee-vs-legal-heir) reasoning; not
  tested). https://indiankanoon.org/doc/89344500/
- Not verified: later amendments to reg. 32.

## PPF
- PPF Scheme 2019 (Government Savings Promotion Act 1873): nomination in the opening form
  (Form 1 item 13); on death the account is closed and paid to the nominee or legal heir; it
  cannot be continued (para 14). https://indiankanoon.org/doc/79752053/
- Not verified: number of nominees allowed under the Government Savings Promotion General Rules
  2018 as amended.

## Will, probate, heirs
- Will form: Indian Succession Act 1925 s.63: signed by the testator, attested by two or more
  witnesses who each saw him sign (or got his acknowledgement).
  https://indiankanoon.org/doc/1673132/
- Registration: optional (Registration Act 1908 s.18) - not verified.
- Probate: s.213 (no right as executor or legatee without probate, for s.57(a)/(b) wills -
  Hindu, Buddhist, Sikh, Jain wills made in, or about immovable property in, the old Bengal,
  Madras and Bombay limits) was omitted by the Repealing and Amending Act 2025, No. 37 of 2025,
  assent 20 Dec 2025, Second Schedule; s.3(1) and s.370 amended to match.
  https://prsindia.org/files/bills_acts/bills_parliament/2025/The_Repealing_and_Amending_Act_2025.pdf
  So the user's city no longer makes probate compulsory. Probate may still be useful (disputes,
  property, foreign brokers). Note: indiankanoon still shows the old s.213 text
  (https://indiankanoon.org/doc/1617988/).
- Succession certificate (ISA s.370-372, district court) for debts and securities where there is
  no will or nominee route; legal heir certificate from the state revenue office (Tehsildar).
  Section text of 371-372 not read.
- Personal law decides intestate heirs: Hindu Succession Act 1956 for Hindus, Buddhists, Sikhs,
  Jains; ISA Part V for Christians, Parsis and others; Muslim personal law limits wills (not
  verified). The user's religion is not known: question E1.

## India tax at death
- No estate or inheritance tax in India (secondary source only; `research/themes/us-estate-tax.md`).
- Heirs pay capital gains tax only when they sell; inheritance is not a transfer (1961 s.47(iii),
  cited by SEBI 19 Sep 2025); cost of the previous owner (1961 s.49(1)) and his holding period
  (1961 s.2(42A) Expl. 1(b)) carry over. Income-tax Act 2025 equivalents: s.70 (not a transfer),
  s.73 (cost), s.2(101) (holding period) per `tax/investment-types.md` section 6; exact clauses
  not verified -> `finance-tax`.
