# Employer stock: lot table and Indian tax

## Summary
All QCOM lots except 14 DRIP shares are long-term (12.5%, 14.95% all-in); all MSFT lots are short-term (35.88%)
until each turns long-term (first 2027-01-01). Most INR gain is the rupee falling. Sell QCOM first,
highest-Indian-cost lots first; hold each MSFT lot to its long-term date (saves about Rs 1.56 L, `tax/employer-stock.md`).
Lot choice vs FIFO and method A vs B cost: CA question.

Back to the index: [employer-stock-concentration.md](../employer-stock-concentration.md). Written 2026-11-15 by `finance-research`;
research only, not advice; no orders placed. "not verified" = could not confirm from a source.

## Tax rules used

Tax (from `tax/investment-types.md` by finance-tax, 2026-11-15, read 2026-11-15): foreign shares are long-term
after 24 months + 1 day at 12.5% (14.95% with this user's 15% surcharge + 4% cess); short-term at slab
30% (35.88%); no Rs 1.25 L exemption (section 0 item 7, rate table at top). Tax year 2026-27 falls under the
Income-tax Act 2025. The tax note's figures (sale FX 95.15, "method A" lots) differ slightly from the
gains on this page (see "Totals" below).

Indian rules (Finance (No.2) Bill 2024 memorandum, https://www.indiabudget.gov.in/budget2024-25/doc/memo.pdf,
checked 2026-11-15): listed securities long-term after 12 months, all other assets after 24 months.
US shares are not listed in India, so 24 months: LT 12.5% (14.95% all-in), ST slab 35.88%
(`tax/investment-types.md` section 0 item 7 and section 1). The Rs 1.25 L LTCG exemption is for Indian listed equity only, so it does not help here
(`tax/angelone-metals-and-mf-exits.md` 1).

Lot table. Cost = market value at vest/purchase (`etrade.transfers()`, `fidelity.holdings()`, run
2026-11-15). Value at 2026-11-13 close (QCOM $172.47, MSFT $523.88). INR gain is approx: cost at yfinance
`INR=X` close on/just before the acquisition date (not the SBI TT rate), value at 94.0338. LT from = first
day after 24 months ("24 months + 1 day", `tax/employer-stock.md`.2 item 2). Same-date lots
merged.

| Stock | Acquired | Type | Qty | Cost/sh $ | Cost $ | Value $ | Gain $ | USDINR then | Gain Rs L | LT from | Today |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QCOM | 2021-11-20 | RSU | 50.014 | 185.00 | 9,253 | 8,626 | -627 | 74.17 | 1.25 | 2023-11-21 | LT |
| QCOM | 2022-01-31 | ESPP | 21 | 175.76 | 3,691 | 3,622 | -69 | 75.04 | 0.64 | 2024-02-01 | LT |
| QCOM | 2022-02-20 | RSU | 31 | 167.64 | 5,197 | 5,347 | 150 | 75.06 | 1.13 | 2024-02-21 | LT |
| QCOM | 2022-05-20 | RSU | 50 | 131.60 | 6,580 | 8,624 | 2,044 | 77.42 | 3.01 | 2024-05-21 | LT |
| QCOM | 2022-07-31 | ESPP | 23 | 145.06 | 3,336 | 3,967 | 630 | 79.57 | 1.08 | 2024-08-01 | LT |
| QCOM | 2022-08-20 | RSU | 33 | 147.60 | 4,871 | 5,692 | 821 | 79.77 | 1.47 | 2024-08-21 | LT |
| QCOM | 2022-11-20 | RSU | 122 | 123.85 | 15,110 | 21,041 | 5,932 | 81.52 | 7.47 | 2024-11-21 | LT |
| QCOM | 2023-01-31 | ESPP | 27 | 133.21 | 3,597 | 4,657 | 1,060 | 81.58 | 1.44 | 2025-02-01 | LT |
| QCOM | 2023-05-20 | RSU | 67 | 105.86 | 7,093 | 11,555 | 4,463 | 82.73 | 5.00 | 2025-05-21 | LT |
| QCOM | 2023-07-31 | ESPP | 29 | 132.17 | 3,833 | 5,002 | 1,169 | 82.25 | 1.55 | 2025-08-01 | LT |
| QCOM | 2023-11-20 | RSU | 151 | 129.51 | 19,556 | 26,043 | 6,487 | 83.29 | 8.20 | 2025-11-21 | LT |
| QCOM | 2024-01-31 | ESPP | 29 | 148.51 | 4,307 | 5,002 | 695 | 83.11 | 1.12 | 2026-02-01 | LT |
| QCOM | 2024-02-20 | RSU | 36 | 151.96 | 5,471 | 6,209 | 738 | 83.02 | 1.30 | 2026-02-21 | LT |
| QCOM | 2024-05-20 | RSU | 75 | 197.76 | 14,832 | 12,935 | -1,897 | 83.30 | -0.19 | 2026-05-21 | LT |
| QCOM | 2024-09-26 | DRIP | 2.831 | 167.81 | 475 | 488 | 13 | 83.62 | 0.06 | 2026-09-27 | LT |
| QCOM | 2024-12-19 | DRIP | 2.974 | 160.34 | 477 | 513 | 36 | 85.17 | 0.08 | 2026-12-20 | ST |
| QCOM | 2025-03-27 | DRIP | 3.004 | 159.33 | 479 | 518 | 39 | 86.10 | 0.08 | 2027-03-28 | ST |
| QCOM | 2025-06-26 | DRIP | 3.235 | 155.57 | 503 | 558 | 55 | 86.01 | 0.09 | 2027-06-27 | ST |
| QCOM | 2025-09-25 | DRIP | 2.942 | 171.77 | 505 | 507 | 2 | 88.78 | 0.03 | 2027-09-26 | ST |
| QCOM | 2025-12-18 | DRIP | 2 | 175.09 | 350 | 345 | -5 | 90.41 | 0.01 | 2027-12-19 | ST |
| MSFT | 2024-12-31 | ESPP | 5.489 | 421.50 | 2,314 | 2,876 | 562 | 85.79 | 0.72 | 2027-01-01 | ST |
| MSFT | 2025-03-31 | ESPP | 6.146 | 375.39 | 2,307 | 3,220 | 913 | 85.54 | 1.05 | 2027-04-01 | ST |
| MSFT | 2025-06-30 | ESPP | 4.643 | 497.41 | 2,309 | 2,432 | 123 | 85.46 | 0.31 | 2027-07-01 | ST |
| MSFT | 2025-08-15 | RSU | 48.847 | 522.48 | 25,522 | 25,590 | 68 | 87.69 | 1.68 | 2027-08-16 | ST |
| MSFT | 2025-11-17 | RSU | 11.541 | 510.18 | 5,888 | 6,046 | 158 | 88.68 | 0.46 | 2027-11-18 | ST |
| MSFT | 2025-12-01 | RSU | 1.282 | 492.01 | 631 | 672 | 41 | 89.35 | 0.07 | 2027-12-02 | ST |
| MSFT | 2026-02-17 | RSU | 11.541 | 401.32 | 4,632 | 6,046 | 1,414 | 90.78 | 1.48 | 2028-02-18 | ST |
| MSFT | 2026-03-02 | RSU | 1.112 | 392.74 | 437 | 583 | 146 | 91.08 | 0.15 | 2028-03-03 | ST |
| MSFT | 2026-05-15 | RSU | 11.541 | 409.43 | 4,725 | 6,046 | 1,321 | 95.71 | 1.16 | 2028-05-16 | ST |
| MSFT | 2026-06-01 | RSU | 1.923 | 450.24 | 866 | 1,007 | 142 | 95.00 | 0.12 | 2028-06-02 | ST |
| MSFT | 2026-08-17 | RSU | 11.541 | 495.40 | 5,717 | 6,046 | 329 | 95.45 | 0.23 | 2028-08-18 | ST |
| MSFT | 2026-08-31 | RSU | 1.282 | 513.53 | 658 | 672 | 13 | 95.38 | 0.00 | 2028-09-01 | ST |

Totals: QCOM LT 746.845 sh, gain $21,609 / about Rs 34.5 L; QCOM ST 14.155 sh, about Rs 0.29 L.
MSFT all ST, gain $5,230 / about Rs 7.4 L. Most of the INR gain is the rupee falling (74-83 -> 94), so
USD "losses" (2021-11-20, 2022-01-31) are INR gains. Only the 2024-05-20 QCOM lot is an INR loss.
Discrepancy with the tax note (section 5): it gives QCOM gain Rs 39.6 L ("method A": net shares kept per
release, as in past ITRs) or Rs 36.0 L (method B = repository FIFO, the lots above), and MSFT Rs 8.1 L,
at sale FX 95.15 vs 94.03 here. Under method A the 2024-05-20 lot is 48 shares; the FIFO lots above show
75. Which method applies: CA (section 5). Tax note's tax if sold now (section 5.1): all QCOM about
Rs 5.8-5.9 L extra tax (method A, with/without AngelOne losses), all MSFT about Rs 2.2-2.5 L. Superseded 2026-11-15 by
`tax/employer-stock.md`: all QCOM about Rs 5.66 L in either year; first 432 sh highest cost first Rs 2.54 L (FIFO Rs 3.51 L).

- **Lot order (tax note section 5.2 item 1): QCOM first, highest-Indian-cost LT lots first.** This
  matches the order here (lowest INR gain per rupee first): QCOM 2024-05-20 (-2%), 2021-11-20 (15%),
  2022-01-31 (19%), 2022-02-20 / 2024-02-20 (22%), 2024-01-31 (24%); highest last: 2023-05-20 (46%),
  2022-11-20 (38%), 2022-05-20 (37%). Tax note: about $49,300 of these lots costs about Rs 1.43 L tax vs
  Rs 2.34 L for the same amount FIFO. This only defers tax. Specific-lot choice vs FIFO for Indian tax is
  not settled: **CA question**; use one rule every year and keep IBKR lot reports. Whether IBKR kept the
  ETrade dates per lot after ACATS: not verified (finance-main). IBKR's QCOM cost basis ($101,633,
  $133.55/sh) understates the Indian cost (FMV at vest/purchase) - tax note section 5, `STATUS.md`.
- **Hold MSFT lots to long-term (tax note section 5.2 item 2):** ST 35.88% vs LT 14.95% saves about
  Rs 1.70 L on today's MSFT gain; after the lost value of using FY26-27 losses against ST gains
  (Rs 62,410), holding beats selling now by about Rs 1.08 L (older figure; `tax/employer-stock.md` now gives **Rs 1.56 L**). New vests sold at once have about zero gain.
- **Indian tax years (tax note section 5.2 item 4).** Spreading over FYs only defers tax: 2026-27 and
  2027-28 are both in the 15% surcharge band and foreign shares have no yearly exemption. It helps only
  to keep total income below Rs 2 Cr in a year (headroom about Rs 86.6 L in 2026-27, `tax/employer-stock.md`; was Rs 93 L).
- **Advance tax (`tax/employer-stock.md`):** 432 QCOM sold by 15 Dec 2026 needs about Rs 1.59 L more by 15 Dec and
  Rs 1.14 L by 15 Mar 2027; sold after 15 Dec, all of it by 15 Mar.
- **Loss set-off in FY2026-27.** Already realised: INDmoney ST loss about -Rs 2,16,582 vs NXPI LT gain
  +Rs 2,76,457, net +Rs 59,875 LT (`tax/migration-indmoney-to-ibkr.md` 3.1). ST loss sets off any gain,
  LT loss only LT gain; no brought-forward losses. AngelOne metals: about -Rs 64,000 unrealised from
  summary percentages (`research/themes/silver-gold.md`) vs about -Rs 81,600 in the tax note (L2, section
  5.1, from AngelOne lot files); the tax note's figure is from lots, so prefer it. More
  INDmoney loss sales before the IBKR move are planned (-Rs 51,800 to -70,100). So little loss is left
  to absorb new QCOM gains this year.
