# Foreign assets and heirs

## Summary
Indian-resident heirs may receive the user's foreign shares by inheritance without using their
LRS limit, but must then show them in Schedule FA. US shares above $60,000 bring a US estate tax
(about $46,057 / Rs 43.3 L now, $87,716 / Rs 82.5 L if unvested Microsoft awards vest at death, which the award form
says they do) and a long freeze until an IRS transfer certificate. Irish UCITS fund units carry
no Irish inheritance tax for Indian-resident heirs. Broker death procedures are still unverified.

Part of [Estate and nominations](README.md). Owner `finance-legal`; sources read 2026-11-15 unless
marked; not legal advice. US details: `research/themes/us-estate-tax.md` (finance-research).

| Asset | Tax at death | Transfer route | Section |
|---|---|---|---|
| US shares and US ETFs (IBKR, Fidelity, Alpaca) | US estate tax above $60k (18-40%) | Broker after IRS transfer certificate | [US](#us-estate-tax-and-brokers) |
| Unvested Microsoft awards | Vest at death; add to US estate | Shares to legal representative within 90 days | [Awards](#awards-that-vest-at-death) |
| Irish UCITS ETF units | None in Ireland (s.75 CATCA) for non-Irish disponer and heirs; not US-situs | Broker (IBKR) | [Ireland](#ireland-irish-ucits-etfs) |
| Any foreign security to Indian-resident heirs | India: none (see [India tax](india-rules.md#india-tax-at-death)) | FEMA: inheritance, outside LRS | [FEMA](#fema-foreign-shares-inherited-by-indian-residents) |

## FEMA: foreign shares inherited by Indian residents
- RBI Foreign Exchange Management (Overseas Investment) Directions 2022 (A.P. (DIR Series)
  Circular No. 12, 22 Aug 2022), para 17(4): "Acquisition of foreign securities by way of
  inheritance or gift in accordance with paragraph 2 of Schedule III of OI Rules shall not be
  reckoned towards the LRS limit and hence, shall not require reporting under LRS." Para 22(2):
  inheritance is classed as ODI or OPI by the nature of the holding.
  https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12381
- OI Rules 2022 Schedule III para 2 itself: not read (RBI PDF blocked by a browser check).
- Heirs must then show the foreign assets in Schedule FA every year and follow the rules in
  [compliance](../compliance/README.md) ([Schedule FA](../compliance/schedule-fa.md)). A non-resident heir is a different case: question E11.

## US estate tax and brokers
One item; details in `research/themes/us-estate-tax.md`.
- US estate tax on US-situs assets above $60,000: about $46,057 (Rs 43.3 L) on $213,304
  (shares $207,935 + cash $5,369; 13 Nov closes, USD/INR 94.0338); with 238 unvested MSFT
  ($124,683 gross) $337,987 -> $87,716 (Rs 82.5 L); 706-NA due 9 months
  after death; brokers need an IRS transfer certificate (26 CFR 20.6325-1) before releasing.
- New finding: Microsoft "Stock Award Agreement under the 2017 Stock Plan" (form filed as
  Exhibit 10.28 to the 10-Q of 25 Oct 2022), s.6: "if Awardee is, at the time of death, in
  Continuous Status as a Participant, outstanding unvested SAs ... shall become immediately
  vested"; s.10: awards pass only "by will or by the laws of descent or distribution".
  Performance awards vest at target (Exhibit 10.29). So unvested Microsoft awards would add to the
  US-situs estate. https://www.sec.gov/Archives/edgar/data/789019/000156459022035087/msft-ex1028_258.htm
  The user's own grant terms may differ (country addendum not read).
- IBKR, Fidelity, Alpaca/INDmoney deceased-account and TOD pages: not verified (404/403). A TOD
  does not remove the US tax or the transfer certificate (research note section 3).
- Whether US probate or ancillary letters are needed for a US broker account of a non-US
  decedent: not verified; question E5.

## Awards that vest at death
US estate value and Indian tax. Sources read 2026-11-15 unless marked. Not legal or tax advice.

| Reading | US-situs estate | US estate tax |
|---|---|---|
| Full value of awards in the gross estate (most likely) | $337,987 (awards $124,683 on 13 Nov) | ~$87,716 |
| Indian tax on the awards deductible pro rata | same | ~$73,618 |
| Awards counted net of Indian tax (~$80k) | lower | ~$72,454 |

- Why full value: gross estate = value at death of all property the decedent had an interest
  in (26 USC 2031(a), 2033). The award form says the awardee "will be deemed to have been issued
  the full number of Common Shares" even if shares are held back for tax, and the tax stays the
  awardee's liability (Exhibit 10.28 s.9(b), URL above). So withholding pays a debt; it does
  not shrink the asset. Shares go to the "legal representative" within 90 days (s.9(a)).
- Income tax as a deduction: only as a claim against the estate, and "Taxes on income received
  after the decedent's death are not deductible" (26 CFR 20.2053-6(f),
  https://www.ecfr.gov/current/title-26/section-20.2053-6). For an NRNC any allowed deduction is
  cut to US estate / worldwide estate (26 CFR 20.2106-2(a)(2), https://www.ecfr.gov/current/title-26/section-20.2106-2).
  ~$73,618 assumes the 36% tax ($44,886) were deductible and a worldwide estate of $365,887
  (+ AngelOne only; ratio 0.924). 26 USC 691(c) (https://www.law.cornell.edu/uscode/text/26/691)
  only gives a US income tax deduction; nothing for Indian tax found.
- Situs: the awards are "the Company's unfunded and unsecured promise", the awardee "a general
  unsecured creditor" of Microsoft Corporation (Exhibit 10.28 s.1(b)). A debt of a US person is
  US-situs (26 USC 2104(c), https://www.law.cornell.edu/uscode/text/26/2104); once shares issue,
  2104(a). US-situs either way; the employer being Microsoft India does not change the obligor.
- Indian tax: the perquisite is shares "allotted or transferred ... by the employer ... to the
  assessee" (1961 s.17(2)(vi), https://indiankanoon.org/doc/938899/); the legal representative
  pays what "the deceased would have been liable to pay" (1961 s.159,
  https://indiankanoon.org/doc/144582/). ITAT Mumbai, Executors of late D.S. Mistry (1988) 27
  ITD 525 (https://indiankanoon.org/doc/193945/): gratuity that became due only on death was not
  salary of the deceased or the heirs (citing CBDT letter F.35/1/65 on leave salary). By analogy a
  death vesting may not be a perquisite at all; Microsoft may still withhold shares (s.9(b)
  standard). Then a refund claim, and the heirs' cost basis (s.49(2AA) needs a taxed perquisite),
  are open: E15, E16.
- Not verified: AF (2025 Act) clauses for s.17(2)(vi), s.159, s.192; any ESOP-at-death ruling
  or CBDT circular (none found); the user's India addendum; US case law refusing a discount for
  embedded income tax (Estate of Kahn, 125 T.C. 227 (2005), from memory, not read).

## Ireland (Irish UCITS ETFs)
- Irish CAT applies to all property situate in Ireland; property outside Ireland only if the
  disponer or beneficiary is resident or ordinarily resident in Ireland (Revenue CAT Manual
  Part 1, updated Apr 2024).
  https://www.revenue.ie/en/tax-professionals/tdm/capital-acquisitions-tax/cat-administration-manual/cat-part01.pdf
- s.75 CATCA 2003: units in collective investment schemes, CCFs, ILPs or investment undertakings
  (TCA 1997 Part 27) are exempt where neither the disponer nor the successor is domiciled or
  ordinarily resident in Ireland at the date of the disposition and of the inheritance (Revenue
  CAT Manual Part 9, para 5, updated Feb 2026).
  https://www.revenue.ie/en/tax-professionals/tdm/capital-acquisitions-tax/cat-manual/part-09-exemptions/part-9-exemptions.pdf
- So: Irish UCITS ETF units -> exempt for this user and Indian-resident heirs. Not covered: ETCs
  (e.g. IGLN, debt securities, not fund units); a heir who lives in Ireland. Whether an Irish
  grant of probate is needed for street-name holdings at IBKR: not verified (E10).
