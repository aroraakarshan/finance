# US estate tax: The rule and what is US-situs

Written 2026-11-15 by `finance-research`. Research only, not tax or legal advice; no orders placed.
Part of [US estate tax](../us-estate-tax.md). Sources read 2026-11-15 unless another date is given; "not verified" = no source confirmed it.
Short names: "IRS page" = https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns ; "i706na" = Form 706-NA instructions, https://www.irs.gov/instructions/i706na (rev. 09/2025).

## Summary
The US taxes a non-US person's US company shares, US ETFs and US funds at death: 18-40% above a
$60,000 exemption (a $13,000 credit). The 2025 OBBBA did not change the $60,000. India has no estate
tax treaty with the US and no estate tax, so there is no credit. Irish UCITS ETF units, Treasuries
and US bank deposits are outside it; broker USD cash is unclear.

## Details

Who: an Indian resident who is not a US citizen, not US-domiciled and has no green card is a
"nonresident not a citizen" (NRNC) for US estate tax.

| Point | Rule | Source |
|---|---|---|
| Tax applies | US estate tax on the taxable estate of every NRNC decedent | 26 USC 2101(a), https://www.law.cornell.edu/uscode/text/26/2101 |
| Only US-situs part counts | Gross estate = the part "situated in the United States" at death | 26 USC 2103, https://www.law.cornell.edu/uscode/text/26/2103 |
| Credit | $13,000 credit; it equals the 2001(c) tax on the first $60,000, so in effect a $60,000 exemption | 26 USC 2102(b)(1), https://www.law.cornell.edu/uscode/text/26/2102 ; table in 2001(c) |
| Rates | 18% on the first $10k rising to 40% above $1,000,000 (full table in [exposure.md](exposure.md)) | 26 USC 2001(c), https://www.law.cornell.edu/uscode/text/26/2001 |
| Filing | Form 706-NA if US-situs assets at death exceed $60,000 | IRS, https://www.irs.gov/individuals/international-taxpayers/some-nonresidents-with-us-assets-must-file-estate-tax-returns (page updated 2026-06-27) |
| Debts | Only a pro-rata share (US estate / worldwide estate) of debts and expenses is deductible, and only if the worldwide estate is documented | 26 USC 2106(a)(1), https://www.law.cornell.edu/uscode/text/26/2106 ; Form 706-NA instructions Part IV, https://www.irs.gov/instructions/i706na (rev. 09/2025) |

**2025-26 law changes.** The One Big Beautiful Bill Act (Pub. L. 119-21, 2025-07-04) raised the
basic exclusion for US citizens/residents to $15,000,000 (26 USC 2010(c)(3),
https://www.law.cornell.edu/uscode/text/26/2010). Section 2102 lists no amendment after
Pub. L. 107-16 (2001), so the NRNC credit is still $13,000 (= $60,000). The IRS page above (updated
2026-06-27) still says $60,000. No 2026 change found; a 2026 law not yet in the Cornell text is
not verified.

**No India-US estate tax treaty.** The IRS list of estate/gift tax treaties (updated 2026-09-08)
has Australia, Austria, Canada, Denmark, Finland, France, Germany, Greece, Ireland, Italy, Japan,
Netherlands, South Africa, Switzerland, UK; India is not on it:
https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international

**India has no estate tax.** India had estate duty from 1953 to 1985 (Wikipedia, "Inheritance tax",
https://en.wikipedia.org/wiki/Inheritance_tax ; secondary source; Indian primary source not found).
So there is no Indian credit to offset the US tax: India's foreign tax credit (AF s.159/160) covers
income tax only (`tax/investment-types.md` section 4).

### What is US-situs (taxed) and what is not

| Asset | Situs | Source |
|---|---|---|
| Shares of a US-incorporated company (QCOM, MSFT, AVGO, VRT, IBKR) | US, wherever the broker or certificates are, even in a nominee's name | 26 USC 2104(a); IRS page above; i706na "Stock" |
| US-domiciled ETFs, mutual funds, money market funds | US (stock of a US company/RIC). The partial RIC exclusion in 2105(d) ended for deaths after 2011 | 26 USC 2105(d)(3), https://www.law.cornell.edu/uscode/text/26/2105 ; i706na "Stock in a RIC" |
| US real estate, tangible property in the US | US | IRS page above |
| US bank deposits not connected with a US business | Not US | 26 USC 2105(b)(1); i706na "Deposits" |
| US Treasury notes/bonds and US corporate bonds whose interest is portfolio interest (871(h)) | Not US | 26 USC 2105(b)(3); i706na "Debt obligations outside United States" |
| T-bills (183 days or less) | Not US, if interest not connected with a US business | 26 USC 2105(b)(4) and 871(g)(1)(B)(i), https://www.law.cornell.edu/uscode/text/26/871 |
| USD cash at a US broker (IBKR, Alpaca/INDmoney, Fidelity) | Unclear. 2105(b)(1) excludes only "deposits" as defined in 871(i)(3): deposits with persons carrying on the banking business, savings institutions, or insurers. A broker-dealer's cash balance is a debt of a US company (US-situs under 2104(c)) unless it is a bank deposit (e.g. swept to a bank) or portfolio-interest debt; neither IBKR's nor Alpaca's treatment was confirmed. A Fidelity core position held in a US money market fund would be US-situs (RIC stock); this account's core position not checked. Treated as US-situs here | 26 USC 871(i)(3), https://www.law.cornell.edu/uscode/text/26/871 ; 2104(c); broker side not verified |
| Shares of a non-US company, e.g. Ireland-domiciled UCITS ETF | Not US ("all other corporate stock is property located outside the United States") | 26 USC 2104(a); i706na "Stock" |
| ADRs of non-US companies | Commonly treated as non-US (the underlying issuer is foreign), but no IRS ruling found | not verified |
| Life insurance on the NRNC's life | Not US | 26 USC 2105(a); IRS page above |

Company domicile (SEC EDGAR, https://data.sec.gov/submissions/CIK<cik>.json): QCOM, VRT, IBKR
Delaware; MSFT Washington; AVGO files 10-K with a Palo Alto address but the state field is blank
(Delaware not verified). All five are treated as US companies here.
