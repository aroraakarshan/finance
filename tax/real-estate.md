# Real estate tax: section 86 on the QCOM/MSFT sales, house property, SM REITs (Nov 2026)

## Summary
- Decision unchanged: keep renting ([income/real-estate.md](../income/real-estate.md)). If you buy for life reasons, one house in India can cover all QCOM/MSFT sales under section 86 (old 54F) if bought Sep 2027 - Nov 2028 (or built within 3 years of each sale); a home loan is fine.
- Value: a Rs 1.0 Cr flat (Rs 1.08 Cr with stamp duty) saves about Rs 5.5 L of the Rs 6.4 L tax; the full Rs 6.4 L needs about Rs 1.48 Cr (house cost is shared out across the sales, not counted once per sale).
- If a purchase may come after 31 Aug 2027: put the unspent sale 1 money (up to Rs 70 L) in a Capital Gains Account by 31 Aug 2027 (31 Jul if the return has no business income), or sale 1 loses the exemption.
- Tell us what the Rs 4.99 L Punjab payment (18 Oct 2026) was: a plot, fee or shop changes nothing; one house is fine; a second house (or one finished within 3 years) blocks or reverses the exemption (section 5).
- SM REIT units are REIT units for tax: rent and SPV interest in the payout at 35.88% (10% TDS), sale after 12 months at 14.95%.

Written 2026-11-15 by `finance-tax` (agent `realestate`). Plan only; you decide. New regime, 15% surcharge:
LT 14.95%, slab 35.88%. "AF s." = Income-tax Act 2025 as amended by Finance Act 2026 (GitHub
abaasairam-ai/income-tax-rag `docs-text/income-tax-act-2025.txt`, read 2026-11-15). Rulings are under the
1961 Act s.54F, whose text s.86 repeats; no ruling under s.86 found (nv). "nv" = not verified.

## 1. Section 86 conditions (AF s.86, ex-54F)

| Condition | Text | Your case |
|---|---|---|
| Original asset | "any long-term capital asset, not being a residential house" (s.86(1)(a)) | QCOM/MSFT shares held over 24 months |
| New asset | "one residential house in India" purchased "within one year before, or two years after" the transfer, or "constructed" within three years (s.86(1)(b)) | Bengaluru flat |
| Exemption | gain x cost of new asset / net consideration; all of it if cost >= net consideration (s.86(1)(i)-(ii)) | per sale, table 2 |
| Net consideration | sale value less selling expenses (s.86(10)) | sale value at SBI TT rate less brokerage |
| Cap | new-asset cost above Rs 10 Cr ignored (s.86(8)) | no effect |
| Unspent money | deposit in the notified scheme by the s.263 due date, proof with the return (s.86(2)); used deposit + spent amount = cost (s.86(3)) | section 4 |
| Blocks | owns more than one house other than the new one on the transfer date; buys another within 1 year; builds another within 3 years (s.86(5)(a)), only houses whose income falls under "Income from house property" (s.86(5)(b)) | section 5 |
| Claw-backs | buys another house within 2 years / builds within 3 (s.86(6)); sells the new house within 3 years (s.86(7)) | gain taxed in that year |

Each sale part (P1-P4, sale 2, each MSFT lot) is a separate transfer: its own net consideration, its own
date window and its own "how many houses do you own" test on that date.

## 2. Rupee value (gains and lots from [qcom-lots.md](employer-stock/qcom-lots.md) 3.4 and [staged-sale.md](employer-stock/staged-sale.md) 3.6, prices of 13 Nov 2026)

| Sale | Date | Net consideration | Gain | Tax at 14.95% | Gain / net value |
|---|---|---|---|---|---|
| QCOM P1 (108 sh at 94.36) | 23-25 Nov 2026 | Rs 17.58 L | Rs 8.19 L | Rs 1.22 L | 46.6% |
| QCOM P2 / P3 / P4 (108 sh each at 93.80) | Dec 2026 | Rs 17.47 L each | 5.47 / 4.07 / 5.94 L | 0.82 / 0.61 / 0.89 L | 31% / 23% / 34% |
| QCOM sale 1 total | Nov-Dec 2026 | Rs 69.99 L | Rs 23.67 L | Rs 3.54 L | 33.8% |
| QCOM sale 2 (195 sh at 93.80) | Apr 2027 | Rs 31.55 L | Rs 11.55 L | Rs 1.73 L | 36.6% |
| MSFT, all 6 lot groups (116.888 sh at $523.88, 94.03) | Jan 2027 - Sep 2028 | Rs 57.58 L | Rs 7.45 L | Rs 1.11 L | 7-27% by lot |
| All | | Rs 1.59 Cr | Rs 42.67 L | Rs 6.38 L | |

Tax saved if the house cost is shared out best (highest gain/net-value sales first; own calc, work folder
`finance-tax-migration/realestate/calc.py`, 2026-11-15). Cost = price + 7.6% stamp duty and registration
(counting stamp duty in cost: common practice, nv; interiors not counted).

| Flat price | Cost of new asset | Tax saved (all sales) | Tax saved (QCOM only) | Tax still due |
|---|---|---|---|---|
| Rs 50 L | Rs 53.8 L | Rs 3.19 L | Rs 3.19 L | Rs 3.19 L |
| Rs 1.0 Cr | Rs 1.08 Cr | Rs 5.54 L | Rs 5.27 L | Rs 0.84 L |
| Rs 1.2 Cr | Rs 1.29 Cr | Rs 6.05 L | Rs 5.27 L | Rs 0.33 L |
| Rs 1.48 Cr or more | Rs 1.59 Cr | Rs 6.38 L | Rs 5.27 L | 0 |

Rule of thumb: each Rs 10 L of house cost saves Rs 0.70 L on P1, Rs 0.55 L on sale 2, Rs 0.10-0.27 L on MSFT.
The house is not cheaper because of this: the saving is already in the rent-vs-buy table of
[income/real-estate.md](../income/real-estate.md) (Rs 6.4 L assumed).

## 3. One house for several sales; loan; under-construction flat (rulings read 2026-11-15, Indian Kanoon)

| Question | Answer | Ruling (court, date) |
|---|---|---|
| Can one house cover several sales in different years? | Yes, if each sale meets its own window; the house cost was split between the years (Rs 2.10 Cr + Rs 1.68 Cr of a Rs 3.78 Cr bungalow), not counted twice. Do the same: share the cost across sales | DCIT v. Pankaj Chimanlal Patel (HUF), ITAT Ahmedabad, 12 Dec 2018 (ITA 3179/Ahd/2016); follows Anagha Ajit Panekar (2006) 9 SOT 685 (Mum), Krishnadevi Kejriwal (ITAT Mum, 25 Jun 2010), ACIT v. Mohinder Kumar Jain (2017) 84 taxmann.com 141 (Del) (these three quoted there, not read) |
| Shares of several companies sold in a year, one flat? | Yes; each company's shares are a separate asset; loss-making sales are not netted against the gain | Ashok Bansal v. DCIT, ITAT Delhi, 17 Apr 2026 (ITA 5568/Del/2025) |
| Same money needed? Home loan? | No: the house may be paid from a loan or other money; even a CGAS deposit from borrowed money was accepted | Smt. Sabita Devi Agarwal v. ITO, ITAT Kolkata, 19 Dec 2018 (ITA 1231/Kol/2016), quoting CIT v. Kapil Kumar Agarwal (P&H HC, (2016) 66 taxmann.com 191), ITO v. K.C. Gopalan (Ker HC, 1999), Muneer Khan v. ITO (ITAT Hyd, 2010) (quoted, not read) |
| Builder flat under construction? | Treated as construction: 3 years from each sale; registration and possession were inside the window | Avichal Kulshrestha v. ITO, ITAT Delhi, 18 Jun 2025 (ITA 1580/Del/2024; home loan taken); CBDT Circulars 471 (1986) and 672 (1993) (quoted, not read) |
| Possession or completion after 3 years? | Allowed where the full amount was paid and the house was substantially built in time; not settled. A builder delay past 3 years from the first covered sale (Nov 2029 for P1) is a real risk: buy ready or near-ready | ITAT Bangalore ITA 634/Bang/2010 (Sambandam Udaykumar), following CIT v. Sardarmal Kothari (2008) 302 ITR 286 (Mad HC); CIT v. Sambandam Udaykumar (2012) 345 ITR 389 (Kar HC) as quoted in ITO v. Sangeeta Nareshkumar Mehta, ITAT Mumbai, 13 Nov 2025 |
| Sale deed not yet registered? | Payment under an agreement in time was enough | Sangeeta Nareshkumar Mehta (above) |

Windows for one purchase covering all sales: P1 (23 Nov 2026) needs purchase by about 23 Nov 2028; the
last MSFT lot (Sep 2028) needs purchase on or after about Sep 2027. So register a ready flat between Sep 2027
and Nov 2028; a house bought before Nov 2026 covers none of these sales (only 1 year back is allowed).

## 4. Capital Gains Account deposit (AF s.86(2), s.263(1)(c))

Money not spent on the house before the return is filed must be deposited by the return due date. The
deposit is of net consideration (sale value), not only the gain. The scheme is the Capital Gains Accounts
Scheme 1988, kept alive by AF s.536(2)(j) (notifications and schemes under the 1961 Act continue); not
renamed in the Rules 2026 text (searched, 2026-11-15).

| Sales | Tax year | Due date (AF s.263(1)(c) Table, as substituted by Finance Act 2026) |
|---|---|---|
| QCOM sale 1, MSFT Jan 2027 lot | 2026-27 | 31 Aug 2027 if the return reports Topmate as profession income (Sl.3: business/profession, no audit; [side-income.md](side-income.md)); 31 Jul 2027 if no business income (Sl.4) |
| QCOM sale 2, MSFT Apr 2027 - Mar 2028 lots | 2027-28 | 31 Aug 2028 / 31 Jul 2028, same test |
| MSFT May-Sep 2028 lots | 2028-29 | 31 Aug 2029 / 31 Jul 2029 |

- Unused deposit after 3 years: the extra exemption (X - Y in s.86(4)) is taxed in the year the 3 years end.
- Bansal (section 3) accepted money spent before a belated return; s.86(2)(b) fixes the deposit date, so do not rely on it.
- Cost of a deposit: Rs 70 L sits in a bank CGAS account at savings/FD rates (taxed 35.88%) for up to 3 years, and must be in INR in India.

## 5. The Rs 4,99,123.60 Punjab Government payment (18 Oct 2026, HDFC CSV; purpose unknown)

s.86(5) counts only a "residential house" whose income is under "Income from house property".

| If the payment was | Effect on section 86 |
|---|---|
| Plot, agricultural land, shop or office | None: land and commercial property are not a residential house (s.86(5) text). Building a house on that plot within 3 years of a sale blocks or reverses the claim (s.86(5)(a)(iii), (6)) |
| Stamp duty/fee for a house you now own (your only one) | None: you may own one other house on each sale date (s.86(5)(a)(i)) |
| A second house, or you already own a house elsewhere | Blocked for every sale made while you own two |
| Allotment of a house still being built (e.g. a development authority) | Not "owned" until handed over (nv); if completed within 3 years of a sale it is a second house built -> exemption reversed (s.86(5)(a)(iii), (6)) |
| Share in a family house (inherited or joint) | Usually counted as owning a house (nv, rulings split); one 1/3 share in a single house was counted as one house in Ashok Bansal (section 3) |
| Purchase of a house in Punjab used as the new asset | Possible only for sales up to 17 Oct 2027 (sale 1, sale 2, MSFT lots to Aug 2027), on that house's full cost (unknown); a Bengaluru flat bought within 2 years of those sales would then reverse it (s.86(6)) |

## 6. New regime: house property (AF s.202, quoted)

| Case | Text | Effect |
|---|---|---|
| Own home, loan interest | total income computed "without any exemption or deduction under ... (v) section 22(1)(b), in respect of properties referred to in section 21(6)" (s.202(2)(a)(v)); s.21(6): annual value nil "if the owner occupies it for his own residence" | No interest deduction; the Rs 2 L limit of s.22(2) is old-regime only. No principal deduction |
| Let-out house, loss | "without set off of ... (ii) any loss under the head 'Income from house property' with any other head of income" (s.202(2)(b)(ii)); such loss "shall be deemed to have been given full effect to and no further deduction ... shall be allowed for any subsequent year" (s.202(3)) | Rent less 30% (s.22(1)(a)) less interest (s.22(1)(b)), taxed at 35.88%; a loss is lost |

## 7. SM REIT units (row 6 of [property-and-alternatives-2026-11.md](property-and-alternatives-2026-11.md))

| Point | Answer | Source (read 2026-11-15) |
|---|---|---|
| Business trust? | Yes: an SM REIT "means a REIT that pools money from investors under one or more schemes" (Reg 26H(c)), registered under the SEBI (REIT) Regulations 2014 (Reg 26I, Chapter VIB, inserted w.e.f. 8 Mar 2024); AF s.2(21)(b) covers REITs registered under those Regulations | SEBI REIT Regs 2014 as amended 15 Oct 2026 (sebi.gov.in PDF) |
| Payout | Same nature as received by the trust (AF s.223(1)). Rent from assets the trust owns and SPV interest: taxable at 35.88%; SPV dividend: exempt unless the SPV chose the 22% company rate (s.200), then taxable (Schedule V Sl.5) | AF s.223, Schedule V Sl.3-5 |
| Debt repayment part | Reduces unit cost (s.72(4)); taxed as "specified sum" only once total such receipts exceed the issue price (s.92(2)(k)) | AF s.72(4), 92(2)(k) |
| TDS | 10% on the taxable parts, no threshold (s.393 Table Sl.4(ii)) | AF s.393 |
| Sale on exchange (STT paid) | Long term after 12 months: 12.5% above Rs 1.25 L a year (s.198) -> 14.95%; short term 20% (s.196) -> 23.92% | AF s.196, 198; 12 months for listed securities (s.2(101)(b)(i)) |
| Sale off exchange (no STT) | s.196/198 do not apply; LT at 12.5% without the Rs 1.25 L allowance (nv) | AF s.197 not re-read |
| Payout split | At least 95% of SPV net distributable cash flow is paid out (Reg 26ZK); the rent/interest/dividend/debt split is in each payout notice | Check before buying (income/real-estate.md idea 1) |

## 8. Discrepancies and open points

| # | Item | Action |
|---|---|---|
| 1 | income/real-estate.md section 1: "the house must cost at least each sale's net value". Safe reading: at least the sum (Rs 1.59 Cr net, about Rs 1.48 Cr flat price) for all Rs 6.4 L; a Rs 1.0 Cr flat saves about Rs 5.5 L | `finance-income`: update the note |
| 2 | Task brief assumed the ITR-3 due date is 31 Jul; Finance Act 2026 moved non-audit business/profession returns to 31 Aug (AF s.263(1)(c) Sl.3; memo "from 31st July to 31st August") | used here |
| 3 | property-and-alternatives-2026-11.md N3: SM REITs "in Chapter VIA ... (unv)": they are in Chapter VIB and are REITs under the 2014 Regs (verified) | `finance-tax`: fix N3 and mark verified |
| 4 | income/real-estate.md lists claw-back for "buy another within 1 year (s.86(5))" only; s.86(6) also reverses it for a purchase within 2 years or construction within 3 | `finance-income` |
| 5 | Using the same house cost twice (full cost against each sale) has no ruling read; not used | do not claim |
| 6 | Punjab payment purpose; any family house share in your name | user |

Sources: Act text as above (s.2(21), 21(6), 22, 72(4), 86, 92(2)(k), 196, 198, 200, 202, 223, 263, 393, 536,
Schedule V); Finance Bill 2026 memorandum (indiabudget.gov.in/doc/memo.pdf, due dates and s.22 changes);
SEBI REIT Regulations 2014 as amended 15 Oct 2026; Indian Kanoon docs 31212624, 186851834, 99117679,
18278577, 197906193, 125962721 (read 2026-11-15).
