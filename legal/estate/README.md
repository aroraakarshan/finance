# Estate and nominations

## Summary
No will is known and no nominee is confirmed on any account, so heirs would face slow claims
in India and a US estate tax of about $46k-$87.7k with US accounts frozen for 1.5-3 years.
Do first: check and set nominees on AngelOne, mutual fund folios, EPF and banks; get the
father-paid term policy details; fill the [family information sheet](family-info-template.md);
then see an Indian lawyer about a will ([questions](../questions.md), "Estate and nominations").

Owner: `finance-legal`. Written 2026-11-15. Not legal advice: findings and questions for an
Indian lawyer/CA; the user decides and acts. Every rule names its source and the date it was read
(all 2026-11-15 unless stated); "not verified" = no primary source was read. Values from
`portfolio/summary.md` (2026-11-13 closes). No passwords, PAN, Aadhaar or full account numbers.
The user is an Indian citizen resident in India: India first; the US estate tax is one item.

## Gaps

| # | Gap | Why it matters | Next step (user) |
|---|---|---|---|
| G1 | No will known | Without a will, Indian assets pass by the personal law that applies (not known: [needed from user](#needed-from-user)) and heirs need legal heir / succession certificates; foreign brokers will ask for a court or official document | Decide heirs and executor; get a will drafted by an Indian lawyer that covers Indian and foreign assets (questions E1-E5) |
| G2 | Nominations unknown on every account | Nomination is the fastest route for heirs in India (demat, MF, bank, EPF, NPS, insurance). Without it, heirs need more documents and time | Check and set nominees: AngelOne demat, each MF folio, EPF (UAN), bank, insurance ([needed from user](#needed-from-user)) |
| G3 | US accounts: $213,304 US-situs (13 Nov; $337,987 with unvested Microsoft awards) | US estate tax $46,057 (Rs 43.3 L), or $87,716 (Rs 82.5 L) with the awards, and a frozen account for an estimated 1.5-3 years until an IRS transfer certificate (`research/themes/us-estate-tax.md`). Unvested Microsoft awards vest at death and add to it ([awards](foreign-assets.md#awards-that-vest-at-death)) | Follow the research note's plan (term cover, move to Irish UCITS); write the 706-NA note in the family sheet |
| G4 | Old EPF accounts (Qualcomm, NXP) may not be merged under one UAN | Each old account needs its own claim and its own valid nomination; a nomination made before marriage becomes invalid on marriage | Check on the UAN portal; transfer old accounts; file e-nomination ([EPF rules](india-rules.md#epf-eps-edli)) |
| G5 | No family information sheet | Heirs may not know that IBKR, Fidelity, INDmoney/Alpaca, ETrade or the old EPF accounts exist | Fill [family-info-template.md](family-info-template.md) (keep the filled copy outside git) |
| G6 | A term policy on the user's life exists, paid by his father; details unknown (finance-main, 2026-11-15) | If the father is the policyholder, the claim goes to the father (or his estate), not to the user's heirs, and the user cannot nominate. Then it does not help pay the US estate tax (about $46k, or about $87.7k / Rs 82.5 L if unvested awards vest at death; `research/themes/us-estate-tax.md`) | Get the policy details from the father ([list](insurance.md#term-policy-paid-by-the-father)); decide whether cover is enough (user decision); check employer group life nominee |

## Good news

Found 2026-11-15, all verified:

| Point | Rule | Details |
|---|---|---|
| Probate no longer compulsory anywhere in India | Repealing and Amending Act 2025 (No. 37 of 2025, assent 20 Dec 2025) omitted ISA s.213; SEBI dropped mandatory probate for transmission (23 Jul 2026) | [will and probate](india-rules.md#will-probate-heirs) |
| Simpler demat transmission | Simplified documents up to Rs 30 L per beneficial owner; "quick" route up to Rs 30,000 (SEBI, 23 Jul 2026) | [transmission](india-rules.md#transmission-of-securities-sebi) |
| No Irish inheritance tax on Irish UCITS units | s.75 CATCA 2003, if neither side is Irish domiciled or ordinarily resident | [Ireland](foreign-assets.md#ireland-irish-ucits-etfs) |
| Inherited foreign shares do not use the heirs' LRS limit | RBI OI Directions 2022 para 17(4) | [FEMA](foreign-assets.md#fema-foreign-shares-inherited-by-indian-residents) |

## Indian accounts

"Set now?" is unknown for every account: the user must check ([needed from user](#needed-from-user)). Joint holders: none known.

| Account | Nominee option and current rule | Set now? | Joint | What heirs do | Documents heirs need | Gap | Next step |
|---|---|---|---|---|---|---|---|
| AngelOne demat (stocks, ETFs; Rs 5.75 L on 8 Nov) | Up to 3 nominees, % shares optional (equal if blank), opt-out allowed; existing accounts too; no freezing (SEBI 29 May 2026, in force 1 Sep 2026; [rule](india-rules.md#demat-and-mf-nomination-sebi)) | Unknown | Unknown | Nominee claims through the DP (AngelOne / CDSL or NSDL) and receives the shares as trustee for the legal heirs; nominee then moves them to heirs with reason code TLH ([transmission](india-rules.md#transmission-of-securities-sebi), [nominee vs heir](india-rules.md#nominee-vs-legal-heir)) | With nominee: transmission form, nominee's demat CML, death certificate. Without: + indemnity and affidavit-cum-NOC up to Rs 30 L; above that will or legal heir certificate or succession certificate | Nominee unknown; how older nominations carry over to the 2026 rule not verified (E7) | AngelOne app -> Profile -> Nominee: confirm names and % |
| AngelOne MF folios (15 funds, Rs 20.5 L on 7 Nov) | Same SEBI rule per folio. Each AMC folio has its own nomination; AngelOne may have set it at purchase | Unknown per folio | Unknown | Nominee claims at the RTA (CAMS or KFintech) per folio; same trustee rule | Same as demat (SOA instead of CML for SOA-form units) | 15 folios; nominee may differ per folio; MF plan to exit 7-8 funds (STATUS.md item 7) | CAMS/KFintech portal or MF Central: list folios and nominees; fix any "not registered" |
| EPF: Microsoft (current), NXP, Qualcomm (passbooks in Drive `Salary/`) | Form 2 / e-nomination; nominee must be family if a family exists; marriage cancels an earlier nomination (EPF Scheme para 61, [rule](india-rules.md#epf-eps-edli)) | Unknown | No | Nominee/family claims PF (Form 20), EPS pension (Form 10D) and EDLI (Form 5 IF) at EPFO | Death certificate, claim forms via employer, bank details; without nominee: heirs per para 70 (not verified) | Old accounts may sit under separate member IDs or UANs | UAN portal: check one UAN holds all three; transfer old ones; e-nominate; check EPS/EDLI nominee |
| NPS (employer NPS available, not used: STATUS.md) | If opened: nomination required at joining; family rule like EPF (PFRDA Exit Regulations 2015 reg. 32, [rule](india-rules.md#nps)) | Unknown: user checking with Microsoft HR whether a PRAN / employer NPS account exists (2026-11-15) | No | Nominee claims through CRA (Protean/KFin) | Death certificate, claim form | A PRAN may exist without a nominee | If a PRAN exists: log in to the CRA and set nominees; if NPS is opened later, nominate at once |
| PPF (not known) | Nomination in the opening form; account closes at death, nominee or legal heir paid (PPF Scheme 2019 para 14, [rule](india-rules.md#ppf)) | Unknown | Not allowed | Nominee or heir claims at bank/post office | Death certificate, claim form | Not known if any | User to confirm whether any PPF exists |
| Bank accounts (an SBI account is implied by SBI TT rates; not confirmed); FDs; lockers | Up to 4 nominees, simultaneous (with %) or successive, for deposits; successive only for lockers and safe custody (Banking Companies (Nomination) Rules 2025, in force 1 Nov 2025, [rule](india-rules.md#bank-deposits-and-lockers)) | Unknown | Unknown | Nominee claims; bank pays the nominee (bank gets a valid discharge) | Death certificate, claim form, KYC; without nominee: bank's no-nominee procedure (RBI settlement of claims directions 2025, not read) | Accounts not listed anywhere | List every bank account (last 4 digits) in the family sheet; set 1-4 nominees in netbanking |
| Term life on the user's life, premium paid by his father (insurer, cover, term unknown) | Only a holder of a policy "on his own life" can nominate (s.39(1)). If the user is the policyholder: nominee per policy, and a parent, spouse or child nominee is beneficially entitled (s.39(7)). If the father is the policyholder: no s.39 nomination by the user; claim goes to the father as owner ([insurance](insurance.md#term-policy-paid-by-the-father)) | Unknown | - | Nominee (user-owned) or the father / his estate (father-owned) claims from insurer | Death certificate, policy, claim form, claimant ID | Who owns the policy, sum assured, expiry, nominee all unknown | Ask the father; if father-owned, consider an absolute assignment to the user (s.38) and then a new nomination (E18-E20) |
| Other life insurance of the user's own | Same s.39 rules ([insurance](insurance.md#nomination-and-assignment-rules)) | Unknown | - | Nominee claims | As above | None known | Confirm none, or list in family sheet |
| Health insurance (employer and own) | Nominee usually only for refunds; not an estate asset | Unknown | - | Claim pending bills | Policy, bills | - | List in family sheet |
| Microsoft India: group term life, gratuity, final salary, leave encashment | Group life: insurer's nominee on the employer benefits portal (not verified). Gratuity: nomination (Form F under Payment of Gratuity Act s.6; may now be under the Code on Social Security 2020; not verified) ([employer](insurance.md#employer-group-life-and-gratuity)) | Unknown | - | HR pays nominee/heirs | Death certificate, HR claim forms | Unknown | Ask HR / benefits portal: group life cover amount and nominee; gratuity nominee form |
| Property, loans, other (not known) | Property passes by will or personal law; nomination in a housing society is not ownership (not verified) | - | - | - | Title documents, will | Not known | User to list ([needed from user](#needed-from-user)) |

## Foreign accounts

| Account | Beneficiary / TOD option | Set now? | Joint | What heirs do | Documents heirs need | Gap | Next step |
|---|---|---|---|---|---|---|---|
| IBKR, ending 4563 (QCOM 761, AVGO, VRT, IBKR shares, $136.6k + $795 cash; IBKR award 15.84 sh vests Dec 2026) | Not verified; IBKR entity (IB LLC or IB India) unknown (STATUS.md); IBKR pages returned 404 | Unknown | No | Executor/heir contacts IBKR estate team; IBKR will hold assets until an IRS transfer certificate (US-situs over $60k, [US](foreign-assets.md#us-estate-tax-and-brokers)) | Death certificate, will/succession document, executor ID, transfer certificate; possibly US probate/ancillary letters (not verified) | US estate tax and long freeze; entity unknown | Find entity in account settings; ask IBKR (in writing) for its non-US estate checklist and whether TOD is offered to Indian residents |
| Fidelity NetBenefits, Microsoft plan (MSFT 116.888 sh, $61.2k; unvested RSU/ESPP) | Beneficiary designation for stock plan: not verified (Fidelity pages 403). Award agreement: awards pass only by will or law of descent | Unknown | No | Heirs contact Microsoft stock plan / Fidelity; unvested stock awards vest immediately at death ([awards](foreign-assets.md#awards-that-vest-at-death)) | Death certificate, will/heirship document, transfer certificate | Unvested awards add to US estate (238 shares, $124,683 gross: estate $337,987) | Check NetBenefits for a beneficiary option; note grant schedule (StockExport in Drive) in family sheet |
| INDmoney / Alpaca, ending 1593 ($10.8k incl. GEV cash; wallet cash $4,574 per STATUS.md) | Not verified | Unknown | No | Heirs contact INDmoney (India) and Alpaca (US custodian) | As IBKR; plus INDmoney's Indian claim process (not verified) | Two firms in the chain; moving to IBKR by Dec 2026 (`portfolio/migration-indmoney-to-ibkr.md`) | Finish the move to IBKR; then close the account so heirs have one US broker |
| ETrade (Morgan Stanley), QCOM ending 7855 and NXP ending 8803 | - | - | No | If still open with any balance or bank-sweep cash, heirs must claim it | Same as IBKR | Shares moved Dec 2025; "Bank deposit program" entry dated 2025-12-22 in `portfolio/drive-index.md`; open or closed not known | Log in: confirm $0 and close both accounts, or list them in the family sheet |
| US estate tax, all US accounts together | One row: $213,304 US-situs (shares $207,935 + cash $5,369; 13 Nov closes, USD/INR 94.0338), tax $46,057 (Rs 43.3 L); with 238 unvested MSFT ($124,683 gross) $337,987 -> $87,716 (Rs 82.5 L), Form 706-NA within 9 months of death, IRS transfer certificate before brokers release assets (`research/themes/us-estate-tax.md`, finance-research 2026-11-15) | - | - | Executor files 706-NA (or asks for a transfer certificate if at or below $60k) | US tax ID for estate (not verified), worldwide estate inventory, valuations | See G3 | Plan in the research note, sections 4-5 |
| Irish UCITS ETFs (planned at IBKR: `tax/global-actions-2026-11.md`) | Same as IBKR account | - | - | Same as IBKR, but no US estate tax and no transfer certificate for these | As IBKR | Irish CAT: exempt under s.75 if conditions hold ([Ireland](foreign-assets.md#ireland-irish-ucits-etfs)); gold ETCs (e.g. IGLN) are not fund units, not covered | Prefer UCITS fund units over ETCs for holdings meant for heirs; ask E10 |

## Needed from user

| Item | Where to check |
|---|---|
| Marital status; spouse, children (ages), parents living | - (decides EPF/NPS family rule, insurance s.39(7), heirs) |
| Religion / personal law | - (Hindu Succession Act or ISA or other) |
| City and state of residence; property there | - (stamp duty, legal heir certificate office) |
| Will exists? Where kept? Executor? | - |
| AngelOne demat nominee(s) and % | AngelOne app -> Profile -> Nominee details; or CDSL/NSDL statement (prints nominee or Yes/No) |
| MF folio nominees (15 funds) | CAMS / KFintech investor portals or MF Central; CAS statement |
| EPF: one UAN or several; nominee; old Qualcomm and NXP accounts transferred? | UAN member portal -> Service history, e-nomination |
| Bank accounts (bank, type, last 4 digits), FDs, lockers, nominees | Each bank's netbanking -> nomination |
| PPF, NPS, other small savings | Bank / post office; NPS CRA login |
| Term policy paid by the father: insurer, policy last 4, sum assured, expiry, policyholder vs life assured, nominee | Ask the father; policy document / insurer's customer portal |
| NPS / PRAN (employer NPS) | Microsoft HR (user checking, 2026-11-15) |
| Life and health insurance; employer group life cover and nominee; gratuity nominee | Policy documents; Microsoft benefits portal / HR |
| IBKR entity and any beneficiary/TOD setting | IBKR Settings -> Account Settings |
| Fidelity beneficiary option for the stock plan | NetBenefits -> profile / beneficiaries |
| ETrade accounts 7855 and 8803 open or closed | ETrade / Morgan Stanley at Work login |
| Joint holders on any account | Account statements |
| Property, loans, credit cards, debts | - (debts also cut the US estate only pro rata) |

## Next steps

| # | Step (user) |
|---|---|
| 1 | Check and set nominations (about 1 hour, all online): AngelOne demat, MF folios, EPF e-nomination, banks. Nominees should match the intended heirs ([nominee vs heir](india-rules.md#nominee-vs-legal-heir)) |
| 2 | EPF: merge old Qualcomm/NXP accounts under the current UAN (G4) |
| 3 | Fill [family-info-template.md](family-info-template.md); keep it outside git with the will |
| 4 | Life cover: get the father's term policy details ([list](insurance.md#term-policy-paid-by-the-father)); if the father owns it, discuss an assignment with him and a lawyer; then decide whether total cover is enough for family needs and the US estate tax (user decision). NPS: confirm with Microsoft HR whether a PRAN exists and nominate if so |
| 5 | Meet an Indian lawyer with [questions](../questions.md) (Estate and nominations); make a will covering Indian and foreign assets; name an executor (and a guardian if minor children) |
| 6 | Close the INDmoney/Alpaca account after the IBKR move and the ETrade accounts if empty, so heirs deal with fewer US firms |
| 7 | Ask IBKR and Fidelity, in writing, for their estate checklist for an Indian-resident account holder and whether TOD/beneficiary is offered (the agent does not contact them) |
| 8 | Review this folder yearly, after marriage/children, and whenever an account opens or closes |

## Topic notes

| Note | What it covers |
|---|---|
| [india-rules.md](india-rules.md) | SEBI nomination and transmission, nominee vs heir, bank, EPF, NPS, PPF, will/probate/heirs, India tax at death |
| [insurance.md](insurance.md) | Insurance Act s.38/s.39, the father-paid term policy, cover needed, employer group life and gratuity |
| [foreign-assets.md](foreign-assets.md) | FEMA inheritance, US estate tax and brokers, Microsoft awards vesting at death, Irish CAT |
| [sources.md](sources.md) | Every source with date, items not verified, discrepancies found |
| [family-info-template.md](family-info-template.md) | Blank sheet for the family: accounts, contacts, what to do first after a death |
