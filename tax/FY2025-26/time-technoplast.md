# Time Technoplast (TIMETECHNO, INE508G01029) - FY2025-26

## Summary

- The 26 Nov 2025 sale of 3 Time Technoplast shares gave a Rs 781.34 loss that the law ignores (bonus-stripping rule, s.94(8)): FY2025-26 tax nil, the filed return is fine.
- No revised return: the AY2026-27 return will not be revised again (user decision 2026-11-15).
- When you sell the 3 bonus shares still held, use cost Rs 781.34 (not Angel One's 0); long-term from about late Sep 2026.

Checked 2026-11-15 from Drive `Finance/Tax/FY2025-26/` (files of 2026-11-08 and 2026-11-15).

## Facts

| Date | Event | Qty | Rs | Source |
|---|---|---|---|---|
| 2025-07-25 | Buy | 3 | 460.75 (1,382.25) | AngelOne_TradesCharges_FY2025-26.xlsx |
| 2025-09-04 | Dividend 2.50/share | 3 | 7.50 | TaxPNL; AIS SFT-015 (Rs 8) |
| 2025-09-23 | 1:1 bonus ex/record date | +3 | 0 | yfinance split 2.0; allotment date in no file |
| 2025-11-26 | Sell, settled 27/11 | 3 | 203.17 (609.51) | TradesCharges; AIS SFT-17 |
| 2025-11-27 | DP charge | 3 | 23.60 | AngelOne_Ledger_FY2025-26.xlsx |
| now | Held, avg price 0 | 3 | - | TaxPnL FY2026-27 |

- Claim confirmed: the sale is in the trade book, P&L summary (-772.74) and AIS, but not in the TaxPnL.
- Angel One omits it on purpose (TaxPnL note 4: s.94(8)), yet shows the bonus shares at cost 0 instead of the deemed cost its note describes.
- The two FY2025-26 TaxPnL copies differ only in dividend date (03/09 vs 04/09) and ST/LT label of the holding (as-of date).

## Tax

- FIFO (1961 s.45(2A), Circular 768/1998; 2025 s.67(7)): the shares sold are the 3 bought 25 Jul 2025; held 4 months, short-term (s.111A).
- Loss: 609.51 - 1,382.25 - buy charges 2.68 - sell charges 5.92 = **-781.34** (STT 1.97 not deductible; -804.94 with the DP charge).
- **s.94(8) applies to shares**, not only MF units: Finance Act 2022 extended it to securities from AY 2023-24 (Budget 2022 Memorandum pp.53-54, Clause 25). 2025 Act: s.175(9)-(10), "securities" includes shares (s.175(11)(c)). Bought within 3 months before the record date (also if it was 15 Sep), sold within 9 months after, bonus shares still held: all met.
- So the loss is **ignored**; the 3 bonus shares get deemed cost Rs 781.34 (260.45 each), overriding nil cost (1961 s.55(2)(aa)(iiia); 2025 s.90(6)(d)).
- Bonus holding period runs from allotment (1961 s.2(42A) Expl.1; 2025 s.2(101)), about late Sep 2025 (unverified); long-term (s.112A / 2025 s.198) after about late Sep 2026.
- FY2025-26 taxable income from the sale: **Rs 0**; tax **nil**.

## ITR status

- Original and revised AY2026-27 JSON: no TIMETECHNO row; 111A (sale 16,666, -3,513) and 112A (12,525) match TaxPnL without it; `LossSec94of7Or94of8` = 0.
- AIS SFT-17-LES Rs 29,800 vs ITR 29,191: the Rs 609 gap is this sale. Missed income nil.

## Revised return

- 1961 s.139(5): until 31 Dec 2026 (3 months before end of AY) or assessment, if earlier. Finance Act 2021 wording; 1961 text not refetched.
- Finance Act 2026 (Act 4 of 2026) set 2025 Act s.263(5) to 12 months, w.e.f. 1-4-2026 (income-tax-rag act text, footnote 45). Deadline for the AY2026-27 return: 31 Mar 2027 per Finance Bill 2026, with a Rs 5,000 fee after 31 Dec 2026 (`tax/archive/fast-ds-2026.md` header; per Finance Bill 2026, enacted text not re-read).

## Recommendation

- No revised return (no tax; and the AY2026-27 return will not be revised again, user decision 2026-11-15).
- When the 3 bonus shares are sold, use cost Rs 781.34, not Angel One's 0.

## Open questions

- Exact record and allotment dates (check NSE corporate actions).
- Include the DP charge in the loss (deemed cost +23.60)?
- Risk of an AIS mismatch notice for a Rs 609 sale with no tax.
