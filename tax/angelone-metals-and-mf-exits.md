# AngelOne: silver/gold sale, 7 equity MF exits and Kotak Arbitrage - tax plan for 2026-27

## Summary

- Done 18 Nov 2026 (actual fills, section 3B): all silver sold (ABSL and ICICI Silver ETFs, ICICI and Motilal FoFs; the ICICI ETF step "by 9 Dec" is done): loss -Rs 1,43,572 (slab ST -1,44,341, s.197 LT +769) saves about Rs 21,464 at 14.95% against QCOM sale 1 (+Rs 3,816 vs plan); GOLDIETF 1,770 bought (no tax). FoFs at NAV 17 Nov and estimated charges until the 18 Nov NAV and contract note.
- 7 equity MF exits (Kotak NN50 kept): Nippon MC150 and Invesco PSU redeemed 18 Nov (s.196 ST -3,484, NAV 17 Nov); ICICI LC, Invesco Mid Cap, SBI PSU, ABSL PSU, LIC Infra on Fri 11 - Mon 14 Dec (ST +2,064, LT +20,644 inside Rs 1.25 L): tax Rs 0.
- With QCOM sale 1 in 2026-27 (LTCG about Rs 15.2 L, specific identification, `employer-stock/staged-sale.md`), the silver and INDmoney losses ([migration-indmoney-to-ibkr.md](migration-indmoney-to-ibkr.md)) all offset this year's gains at 14.95%; the MF LTCG stays inside Rs 1.25 L if the ITR utility sets losses against s.197 gains (check Schedule SI). Section 6 counts AngelOne only (no QCOM); it applies if QCOM sale 1 slips past 31 Mar 2027.
- SIPs already changed (the SIP change of 16 Nov 2026 (portfolio/decisions.md)): no new lots in the 7 exit funds or the silver FoFs (last lots 2 Nov; Invesco PSU 9 Nov). Kotak Arbitrage: exiting now costs about Rs 373 (with QCOM sale 1); keeping costs nothing.

Written 2026-11-15 by `finance-tax`; revised 2026-11-15 with per-lot MF data and NAVs of 2026-11-13, and
for the user's decision of 2026-11-15 to KEEP Kotak Nifty Next 50 (7 MF exits, not 8).
Plan only: no orders placed; the user trades.
Tax year 2026-27 = 1 Apr 2026 - 31 Mar 2027 (Income-tax Act 2025; 1961 section in brackets).
Assesses `research/themes/silver-gold.md` (incl. "Option B" = Research v2) and
`research/themes/mutual-fund-overlap.md`.

Sources:
- MF lots: `tax/FY2026-27/angelone-mf-lots.csv` - built by `finance` (main session) on 2026-11-15 from the
  AngelOne MF transaction files FY2024-25 to FY2026-27; units reconciled to the 14 Nov 2026 holdings;
  switch-ins dated at the switch. Cost used = cost + stamp duty (the CSV `cost` excludes stamp duty).
- MF NAVs: AMFI `NAVAll.txt`, NAV date 2026-11-13 (fetched 2026-11-15).
- ETF lots: work file `numbers.md` G.1 (AngelOne tradebook to 2026-11-06); prices NSE close 2026-11-13
  (SILVER 177.03, SILVERIETF 175.91).
- Realised 2026-27 and US figures: `numbers.md` B and A.4. Rules: work file `rules.md` sections 3, 8, 10.
- Exit loads: `mutual-fund-overlap.md` table 1 (Groww, checked 2026-11-15).
- INR for US shares are approx (yfinance month-end USDINR, not SBI TT rates).
- The user files under the **new regime** (s.202; 1961 s.115BAC; AY2026-27 ITR per `empstock.md`): top slab 30%; surcharge 15% for income
  Rs 1-2 Cr (new-regime maximum 25%; on s.196/197/198 gains capped at 15%). `empstock.md` puts 2026-27
  income at about Rs 1.06 Cr before capital gains. Rates incl. 15% surcharge and 4% cess: ST at slab
  35.88% (30% x 1.15 x 1.04); s.196 (1961 s.111A)
  23.92%; LT 12.5% (s.197; 1961 s.112) 14.95%; s.198 (1961 s.112A) 14.95% above Rs 1.25 L.

## 1. Rules that decide the answer

| Product | Long term after | LT rate | ST rate | Rs 1.25 L exemption |
|---|---|---|---|---|
| Silver ETFs (ABSL, ICICI), listed | 12 months (s.2(101)(b)(i); 1961 s.2(42A)) | 12.5% | slab | No |
| Silver FoF (ICICI), Gold+Silver FoF (Motilal) | 24 months (s.2(101)(a)) | 12.5% | slab | No |
| Equity MFs incl. Kotak Arbitrage | 12 months | 12.5% above Rs 1.25 L (s.198) | 20% (s.196) | Yes, shared with shares |

- Metal funds are outside s.76 (1961 s.50AA) for sales from 1 Apr 2025. The Motilal SID shows equity-style
  rates; it is not equity-oriented (AF s.198(8)(i) needs 90% in equity funds; `ca-questions.md`).
- ST loss sets off against any capital gain; LT loss only against LT gain (s.108; 1961 s.70). Set-off comes
  before the Rs 1.25 L exemption, so loss set against exempt equity LTCG is wasted.
- Unused loss carries forward 8 tax years (s.111; 1961 s.74) **only if the return is filed by the due
  date, 31 Jul 2027** (s.121 with s.263(1); 1961 s.80 with s.139(1)).
- FIFO for units (s.67(7)(c); 1961 s.45(2A)). A switch is a transfer, so a switched-in lot's date and cost
  are the switch date and value - the CSV dating is correct.

## 2. Gains already realised in 2026-27 (`numbers.md` B, A.4)

| Item | Type | Approx INR |
|---|---|---|
| INDmoney sales to 2026-11-09 | ST loss, slab | -2,16,582 |
| NXPI sale 2026-07-09 (IBKR) | LT gain 12.5%, no exemption | +2,76,457 |
| INDmoney fractions at migration (2026-11-13 prices) | ST gain, slab | +6,448 |
| **Baseline** (nothing else sold) | LT 66,323 x 14.95% | **Rs 9,915** |

No slab or 20% ST gain is left to absorb new losses, so new losses save 14.95% (against NXPI), at most
about Rs 9,900 this year; the rest carries forward. That holds only without QCOM. With QCOM sale 1 in
2026-27 (the plan; LTCG about Rs 15.2 L, specific identification, `employer-stock/staged-sale.md` section 3) there is far more
LT gain than loss: the silver loss saves about Rs 21,464 (all silver, actual 18 Nov, section 3B; plan Rs 17,648) and the INDmoney loss sales of 16-25 Nov
(SCLX + IONQ about -Rs 35,209) about Rs 5,264, all at 14.95% this year; nothing carries forward
([migration-indmoney-to-ibkr.md](migration-indmoney-to-ibkr.md)).
MF LTCG (s.198, +20,644): the exemption applies to the s.198 gain left after set-off (s.198(2)); with
s.197 gains far above the losses it stays inside Rs 1.25 L, but the AY2026-27 ITR utility has one
12.5% column for s.112 and s.112A gains and decides which gain a loss meets (`gain-harvesting.md`
section 2). Check Schedule SI; at worst Rs 20,644 of loss falls on exempt gain (about Rs 3,086).

## 3. Silver and gold (prices 2026-11-13; superseded for the sale by section 3A)

| Holding | Lots | Gain/loss | Term on planned date | Turns long term |
|---|---|---|---|---|
| ABSL Silver ETF 2025-11-10 | 66 u | +1,708 | LT | already |
| ABSL 2025-12-01 | 469 u | +2,147 | LT from 2 Dec | 2026-12-02 |
| ABSL 2025-12-08/15/16/30 | 1,784 u | -17,071 | ST | 2026-12-09/16/17/31 |
| ICICI Silver ETF (3 lots 2025-12-09 to 2026-01-21) | 706 u | -47,538 | ST (done: sold 18 Nov) | first lot 2026-12-10 |
| ICICI Silver ETF FoF (13 lots 2025-11-11 to 2026-11-02) | 4,793.987 u | **-19,858** | ST | from 2027-11-12 |
| Motilal Gold+Silver FoF (13 lots 2025-11-12 to 2026-11-02) | 5,267.969 u | **-10,698** | ST | from 2027-11-13 |

FoF lots: first two lots of each are gains (ICICI +3,990, +1,087; Motilal +2,745, +820), all later lots
losses; all ST. Loads: ICICI FoF 1% within 15 days (2026-11-02 lot free from 18 Nov); Motilal nil.
All four in full: about -Rs 91,300.

- **Research v2 (Option B)**: sell ICICI ETF, ICICI FoF, Motilal FoF in full; keep ABSL whole; buy a gold
  ETF (a purchase, no tax). Loss **ST -Rs 78,094** at 2026-11-13 prices. Research's -Rs 68,402 used FoF
  NAVs of 2026-11-06/07; FoF NAVs fell since (ICICI -4,735, Motilal -4,957).
- Research v1 (trim ABSL ~Rs 2.2 L in 2-8 Dec): FIFO sells the cheap lots first, so ST -79,024 and LT +3,855.
- ABSL kept whole: its loss lots (-17,071) turn long term 9-31 Dec; any later loss on them is LT loss.
  Superseded 16 Nov: ABSL is sold in full (section 3A).

## 3A. Sell all silver (user decision 2026-11-16)

Prices: ETFs yfinance close Mon 2026-11-16 (SILVER 167.97, SILVERIETF 167.80); FoFs AMFI/mfapi NAV
2026-11-13 (the 16 Nov NAV was not yet published at 21:00 IST). The 18 Nov NAV/price will differ.
Cost includes buy charges.

| Product / lot | Units | Gain/loss | Term on sale date | LT from | 13 Nov (research check) |
|---|---|---|---|---|---|
| ABSL 2025-11-10 | 66 | +1,110 | LT | 2026-11-11 | +1,708 |
| ABSL 2025-12-01 | 469 | -2,102 | ST | 2026-12-02 | +2,147 |
| ABSL 2025-12-08 | 1,140 | -11,825 | ST | 2026-12-09 | -1,497 |
| ABSL 2025-12-15 | 260 | -5,680 | ST | 2026-12-16 | -3,324 |
| ABSL 2025-12-16 | 184 | -4,372 | ST | 2026-12-17 | -2,705 |
| ABSL 2025-12-30 | 200 | -11,357 | ST | 2026-12-31 | -9,545 |
| **ABSL Silver ETF, sold 18 Nov** | 2,319 (Rs 3,89,522) | **-34,226** (ST -35,337, LT +1,110) | | | -13,216 |
| ICICI Silver ETF 2025-12-09 / 12-26 / 2026-01-21 | 56 / 500 / 150 | -560 / -29,360 / -23,344 | ST (done: sold 18 Nov) | 2026-12-10 / 12-27 / 2027-01-22 | -47,538 |
| **ICICI Silver ETF** | 706 (Rs 1,18,467) | **-53,264** ST | | | |
| **ICICI Silver FoF** (13 lots; sold 18 Nov) | 4,793.987 (Rs 1,29,376) | **-19,858** ST | | from 2027-11-12 | same |
| **Motilal Gold+Silver FoF** (13 lots; sold 18 Nov) | 5,267.969 (Rs 1,38,484) | **-10,698** ST | | from 2027-11-13 | same |
| **All silver** | Rs 7,75,850 | **-1,18,047** (ST -1,19,157, LT +1,110) | | | -91,310 |

Research's ABSL lot figures (+1,708 / +2,147 / -17,071, net -13,216) are confirmed at 13 Nov prices; at
16 Nov the price is 5.1% lower, so the 2025-12-01 lot is now a loss and ABSL nets -34,226. If the ICICI
FoF NAV falls like SILVERIETF (-4.6%) its loss would be about -25,800 (rough estimate).

Set-off (s.108; 1961 s.70): ST loss may meet any capital gain, LT loss only LT gain. The Act fixes no order
among gains; the AY2026-27 ITR utility has one 12.5% column for s.112 and s.112A gains and decides which
one a loss meets (`gain-harvesting.md` section 2). Here the ST losses absorb the ABSL LT lot (+1,110), the
NXPI gain and the INDmoney fractions, and the rest meets the QCOM sale 1 LTCG at 14.95% (plan case,
`employer-stock/staged-sale.md` section 5). Tax saved (plan; actual in 3B): **all silver about Rs 17,648**; **ABSL alone
(incremental) about Rs 5,117**. Versus the earlier plan (silver -78,094, ABSL kept), Rs 5,973 more. Risk:
if the utility puts loss on the MF s.198 gain (+20,644) first, up to Rs 3,086 of saving is lost (check
Schedule SI).

Flags (none makes a full sale worse than keeping, for tax):
- ETF price vs iNAV: ETFs can trade at a premium or discount; use a limit order near the AMC's live iNAV,
  on a normal day, not in the first/last 15 minutes. Not checked for 18 Nov.
- Costs: brokerage, exchange and SEBI fees, GST, DP charge per scrip per sale day (about Rs 15-20, not
  verified); deductible as transfer cost (s.72(1)(a)). No STT on non-equity ETFs/FoFs (`rules.md` s.10
  reading of Finance (No.2) Act 2004 s.98; not verified on an AngelOne contract note).
- Exit loads: ETFs none; ICICI FoF load-free from 18 Nov (1% before); Motilal nil.
- LT dates: no ABSL lot gains by waiting. The 2025-12-01 lot (now a loss) would turn LT on 2 Dec; the
  loss lots turn LT 9-31 Dec. Selling 18 Nov keeps them ST. The LT gain lot (+1,110) is offset by losses.
- Gold plan: proceeds (about Rs 7.76 L at these prices) into the gold ETF: no tax on buying.
- Advance tax: the extra loss vs the earlier plan (-39,953) cuts QCOM tax by about Rs 5,973: about
  Rs 4,480 less by 15 Dec and Rs 1,490 less by 15 Mar (75%/25% as in staged-sale section 5). Updated in
  `employer-stock/staged-sale.md` and `FY2026-27/fd-and-advance-tax.md` (now, specific identification:
  about Rs 1,53,600 by 15 Dec and Rs 1,91,400 by 15 Mar). Superseded by section 3B (actual fills).

## 3B. Realised 18 Nov 2026 (actual fills)

Fills (Wed 18 Nov 2026, AngelOne, from `finance` main): SILVER (ABSL Silver ETF) 2,319 @ 162.83 and
SILVERIETF (ICICI Silver ETF) 706 @ 162.89, 12:37 - the ICICI ETF was sold today instead of by 9 Dec,
still short-term. Redemptions: ICICI Silver FoF, Motilal Gold+Silver FoF, Nippon MC150, Invesco PSU,
all units (the "4 MF withdrawals"; Kotak NN50 kept). Bought GOLDIETF 1,770 @ 111.56 (section 3B.4).
Shares sold the same day: [FY2026-27/angelone-stocks.md](FY2026-27/angelone-stocks.md) section 6.

Provisional on two points:
- No contract note for 18 Nov in Drive (`Tax/FY2026-27/Angel One/`, `Investments/Stocks/AngelOne/`,
  checked 18 Nov 12:50): ETF sale charges are estimates at the FY2025-26 trade-book rates (brokerage
  Rs 20 per order + 18% GST; NSE turnover 0.00297%; SEBI and IPFT 0.0001% each; DP Rs 23.60 per scrip).
  No STT on the silver ETFs (trade book: TATAGOLD ETF sell of 18 Nov 2025 shows STT 0).
- MF NAV: the 18 Nov NAV is not yet published (AMFI `NAVAll.txt` at 12:50 shows 17-Nov-2026), so the
  FoFs and MFs use the **AMFI NAV of 17 Nov 2026**: ICICI Silver FoF 25.6957, Motilal Gold+Silver FoF
  25.5601, Nippon MC150 26.2752, Invesco PSU 75.68. Each 1% change in the two FoF NAVs moves the loss
  by about Rs 2,578 (tax effect about Rs 385). Units: all units in `FY2026-27/angelone-mf-lots.csv`
  (FIFO, whole holding). Orders placed after 3 pm get the 19 Nov NAV.

### 3B.1 Silver ETFs, per lot (cost incl. buy charges, `numbers.md` G.1)

| Lot (bought) | Units | Cost Rs | Sale value Rs | Sale charges Rs | Gain/loss Rs | Term | Section |
|---|---|---|---|---|---|---|---|
| ABSL 2025-11-10 | 66 | 9,976 | 10,747 | 2 | +769 | LT (from 2026-11-11) | s.197 |
| ABSL 2025-12-01 | 469 | 80,880 | 76,367 | 12 | -4,525 | ST | slab |
| ABSL 2025-12-08 | 1,140 | 2,03,311 | 1,85,626 | 30 | -17,715 | ST | slab |
| ABSL 2025-12-15 | 260 | 49,352 | 42,336 | 7 | -7,023 | ST | slab |
| ABSL 2025-12-16 | 184 | 35,279 | 29,961 | 5 | -5,323 | ST | slab |
| ABSL 2025-12-30 | 200 | 44,951 | 32,566 | 5 | -12,391 | ST | slab |
| **ABSL Silver ETF** | 2,319 | 4,23,749 | 3,77,603 | 61 | **-46,207** (ST -46,977, LT +769) | | |
| ICICI ETF 2025-12-09 | 56 | 9,957 | 9,122 | 4 | -839 | ST | slab |
| ICICI ETF 2025-12-26 | 500 | 1,13,260 | 81,445 | 36 | -31,851 | ST | slab |
| ICICI ETF 2026-01-21 | 150 | 48,514 | 24,434 | 11 | -24,091 | ST | slab |
| **ICICI Silver ETF** | 706 | 1,71,731 | 1,15,000 | 52 | **-56,782** ST | | |

### 3B.2 Silver FoFs, per lot (NAV 17 Nov; cost incl. stamp duty; all ST, LT needs 24 months; no load)

| ICICI / Motilal lot | ICICI units | Cost | Value | Gain/loss | Motilal units | Cost | Value | Gain/loss |
|---|---|---|---|---|---|---|---|---|
| 2025-11-11 / 11-12 (switch-in) | 1,231.114 | 29,235 | 31,634 | +2,400 | 1,214.528 | 29,183 | 31,043 | +1,861 |
| 2025-11-26 | 410.821 | 10,000 | 10,556 | +556 | 411.587 | 10,000 | 10,520 | +520 |
| 2026-01-01 | 288.866 | 10,000 | 7,423 | -2,577 | 351.772 | 10,000 | 8,991 | -1,009 |
| 2026-02-02 | 279.308 | 10,000 | 7,177 | -2,823 | 329.278 | 10,000 | 8,416 | -1,584 |
| 2026-03-02 | 227.785 | 10,000 | 5,853 | -4,147 | 280.262 | 10,000 | 7,164 | -2,836 |
| 2026-04-02 | 288.763 | 10,000 | 7,420 | -2,580 | 327.600 | 10,000 | 8,373 | -1,627 |
| 2026-05-04 | 271.164 | 10,000 | 6,968 | -3,032 | 323.173 | 10,000 | 8,260 | -1,740 |
| 2026-06-02 | 248.119 | 10,000 | 6,376 | -3,624 | 303.075 | 10,000 | 7,747 | -2,253 |
| 2026-07-01 | 295.228 | 10,000 | 7,586 | -2,414 | 345.277 | 10,000 | 8,825 | -1,175 |
| 2026-08-03 | 302.480 | 10,000 | 7,772 | -2,228 | 344.276 | 10,000 | 8,800 | -1,200 |
| 2026-09-01 | 286.570 | 10,000 | 7,364 | -2,636 | 324.212 | 10,000 | 8,287 | -1,713 |
| 2026-10-01 | 299.114 | 10,000 | 7,686 | -2,314 | 336.511 | 10,000 | 8,601 | -1,399 |
| 2026-11-02 | 364.655 | 10,000 | 9,370 | -630 | 376.418 | 10,000 | 9,621 | -379 |
| **Total** | 4,793.987 | 1,49,235 | 1,23,185 | **-26,050** ST slab | 5,267.969 | 1,49,183 | 1,34,650 | **-14,533** ST slab |

### 3B.3 Equity MFs (NAV 17 Nov; equity-oriented: ST up to 12 months, s.196)

| Fund / lot | Units | Cost Rs | Value Rs | Exit load Rs | Gain/loss Rs | Term | Section |
|---|---|---|---|---|---|---|---|
| Nippon MC150 2026-09-23 | 8,560.056 | 2,27,500 | 2,24,917 | 0 | -2,583 | ST | s.196 |
| Invesco PSU 2025-12-10 | 26.349 | 2,000 | 1,994 | 18 | -24 | ST | s.196 |
| Invesco PSU 2026-01-07 | 24.940 | 2,000 | 1,887 | 17 | -130 | ST | s.196 |
| Invesco PSU 2026-02-09 | 24.614 | 2,000 | 1,863 | 17 | -154 | ST | s.196 |
| Invesco PSU 2026-03-09 | 25.564 | 2,000 | 1,935 | 17 | -83 | ST | s.196 |
| Invesco PSU 2026-04-07 | 26.545 | 2,000 | 2,009 | 18 | -9 | ST | s.196 |
| Invesco PSU 2026-05-07 | 24.206 | 2,000 | 1,832 | 16 | -185 | ST | s.196 |
| Invesco PSU 2026-06-08 | 25.996 | 2,000 | 1,967 | 18 | -50 | ST | s.196 |
| Invesco PSU 2026-07-07 | 25.620 | 2,000 | 1,939 | 17 | -79 | ST | s.196 |
| Invesco PSU 2026-08-07 | 25.105 | 2,000 | 1,900 | 17 | -117 | ST | s.196 |
| Invesco PSU 2026-09-07 | 25.789 | 2,000 | 1,952 | 18 | -66 | ST | s.196 |
| Invesco PSU 2026-10-07 | 26.935 | 2,000 | 2,038 | 18 | +20 | ST | s.196 |
| Invesco PSU 2026-11-09 | 26.332 | 2,000 | 1,993 | 18 | -25 | ST | s.196 |
| **Invesco PSU** | 307.995 | 24,000 | 23,309 | 210 | **-901** | ST | s.196 |
| **Both** | | 2,51,500 | 2,48,226 | 210 | **-3,484** | ST | s.196 |

Exit load: 1% on 90% of units (all lots under 1 year); it reduces the sale value. STT 0.001% on these
two redemptions (about Rs 2) is not deductible.

### 3B.4 Totals and change vs plan

| 18 Nov sales | Value Rs | Slab ST | s.196 ST | s.197 LT | s.198 LT | Net |
|---|---|---|---|---|---|---|
| Silver ETFs (3B.1) | 4,92,603 | -1,03,758 | | +769 | | -1,02,989 |
| Silver FoFs (3B.2) | 2,57,835 | -40,583 | | | | -40,583 |
| **All silver** | **7,50,438** | **-1,44,341** | | **+769** | | **-1,43,572** |
| Equity MFs (3B.3) | 2,48,226 | | -3,484 | | | -3,484 |
| Shares (`FY2026-27/angelone-stocks.md` 6) | 11,706 | | -646 | | -3,152 (+878 gains, -4,029 losses) | -3,797 |
| **All AngelOne 18 Nov** | **10,10,370** | **-1,44,341** | **-4,129** | **+769** | **-3,152** | **-1,50,853** |

| Item | Plan (3A / section 4, 16 Nov) | Actual 18 Nov | Change |
|---|---|---|---|
| ABSL Silver ETF | -34,226 | -46,207 | -11,981 |
| ICICI Silver ETF | -53,264 (by 9 Dec) | -56,782 (sold 18 Nov) | -3,518 |
| ICICI Silver FoF | -19,858 | -26,050 | -6,192 |
| Motilal FoF | -10,698 | -14,533 | -3,835 |
| All silver / tax saved at 14.95% | -1,18,047 / Rs 17,648 | -1,43,572 / Rs 21,464 | -25,525 / **+Rs 3,816** |
| Nippon MC150 + Invesco PSU | -3,027 | -3,484 | -457 / +Rs 68 |
| 6 loss shares (not in the advance-tax plan) | - | -4,675 | +Rs 699 |
| **Total extra saving vs plan (with QCOM sale 1)** | | | **about Rs 4,583** |

- Set-off (plan case, QCOM sale 1 in 2026-27): the ST and LT losses meet the NXPI and QCOM LT gains at
  14.95%; the ABSL LT lot (+769, s.197) is absorbed by them; the share gains AZAD/KPIL (+878, s.198)
  stay inside the Rs 1.25 L exemption (worst case Rs 131 if the ITR utility sets loss against them).
- GOLDIETF 1,770 @ 111.56 = Rs 1,97,461 (both planned parts, Rs 1,97,734, at once): a purchase, no tax;
  cost = price + buy charges (stamp 0.015% about Rs 30, brokerage and fees about Rs 31; estimate, no
  contract note); one lot, LT from 2027-11-19 (s.197 14.95%), ST at slab before.
- Whole-year position and advance tax: `employer-stock/staged-sale.md` section 5.

## 4. The 7 equity MF exits - per lot, on the planned dates (NAV 2026-11-13)

Kotak Nifty Next 50 Index is **kept** (user decision 2026-11-15; `finance-research` may add new money to
it, `tax/global-actions-2026-11.md` action 6). Its one lot (2026-09-23, +963 ST at NAV 2026-11-13) turns LT
on 2027-09-24; new buys are new FIFO lots.

Planned dates: Nippon MC150 and Invesco PSU from Wed 18 Nov; the other five on/after Fri 11 Dec.

| Fund (lots held) | Sale | Value | ST | LT | Exit load | Lot notes |
|---|---|---|---|---|---|---|
| ICICI Pru Large Cap (25) | 11 Dec | 91,473 | +1,369 | +2,461 | 143 | 14 lots to 2025-12-01 LT; 11 lots from 2026-01-01 ST; load on 2026-01-01..04-02 lots (old 1-year load) |
| Nippon Nifty Midcap 150 Index (1: 2026-09-23) | 18 Nov | 2,25,230 | -2,270 | 0 | nil | LT from 2027-09-24 |
| Invesco India Mid Cap (1: switch-in 2025-12-10) | 11 Dec | 37,352 | 0 | +4,244 | nil | LT and load-free from 11 Dec |
| SBI PSU (16) | 11 Dec | 41,336 | 0 | +3,336 | nil | all LT from 2 Dec |
| Invesco India PSU Equity (12) | 18 Nov | 23,454 | -757 | 0 | 211 | 1% on 90% of units, all lots < 1 year; new lot 2026-11-09 |
| ABSL PSU Equity (27) | 11 Dec | 65,159 | +695 | +4,464 | nil | 16 lots to 2025-12-01 LT; 11 ST |
| LIC MF Infrastructure (15) | 11 Dec | 48,139 | 0 | +6,139 | nil | all LT |
| **Total** | | **5,32,143** | **-963** | **+20,644** | **~354** | |

- Tax on the MFs alone: ST -963 (a loss); LT +20,644 is inside Rs 1.25 L -> **Rs 0**. Exemption left
  about Rs 1.04 L (less any other s.198 gains this year).
- Best dates unchanged: selling the 2 loss funds on 11 Dec instead would change ST by +11 and save Rs 18
  of load; selling the 5 gain funds on 18 Nov instead moves +3,884 from exempt LT to ST and adds Rs 428 of load.

## 5. Kotak Arbitrage Fund (equity-oriented)

One lot: 2026-09-23, 6,920.931 units, cost Rs 3,00,000 incl. stamp duty; NAV 43.7069 (2026-11-13) =
Rs 3,02,492, gain **+2,492, ST** (LT from 2027-09-24). Load 0.25% within 30 days ended 2026-10-23: nil now.

| Option | Tax effect |
|---|---|
| Exit now (18 Nov), with QCOM sale 1 in 2026-27 (the plan) | +Rs 373 tax (2,492 x 14.95%: the gain uses loss that would offset QCOM LTCG) |
| Exit now, Research v2 + MF exits, no QCOM sale this year | ST +2,492 is absorbed by the surplus loss; tax still 0 (it uses loss that would otherwise be wasted on exempt LTCG) |
| Exit now, Research v2 but no MF exits | tax 0; carried-forward ST loss falls by 2,492 (11,772 -> 9,280) |
| Exit now, nothing else sold | +Rs 373 tax (10,288 vs 9,915; the gain uses ST loss that would have offset 14.95% LTCG) |
| Exit on/after 24 Sep 2027 (2027-28) | LT: exempt within that year's Rs 1.25 L |
| Keep as parking | No tax until redeemed. Each new buy is a new lot: ST (23.92%) unless held 12 months; 0.25% load within 30 days of each buy |

## 6. Whole 2026-27 picture (approx INR; MF dates as planned; prices 2026-11-13)

AngelOne and NXPI only. With QCOM sale 1 in 2026-27 (the plan) no row applies: all losses offset
QCOM, nothing carries forward, and each rupee of loss saves 14.95% (section 2). The rows below
hold if QCOM sale 1 slips past 31 Mar 2027.

| Scenario | Net ST before set-off | LT 12.5% | Exempt equity LTCG left | Loss carried forward | Tax |
|---|---|---|---|---|---|
| A. Baseline (fractions only) | -2,10,134 | 66,323 | 0 | 0 | **9,915** |
| A + 7 MF exits only | -2,11,097 | 65,360 | 20,644 | 0 | 9,771 |
| **V2. A + Research v2** | -2,88,229 | 0 | 0 | **ST 11,772**, LT 0 | **0** |
| **V2 + 7 MF exits** | -2,89,192 | 0 | 7,908 (12,736 lost to set-off) | 0 | **0** |
| V2 + 7 MF + Kotak Arbitrage now | -2,86,700 | 0 | 10,401 | 0 | 0 |
| v1 (trim ABSL) + 7 MF | -2,90,122 | 0 | 10,833 (LT 3,855 also absorbed) | 0 | 0 |
| All four metals + 7 MF | -3,06,263 | 0 | 0 | ST 5,308 | 0 |
| All silver (16 Nov prices, section 3A) | -3,29,291 | 0 | 0 | ST 51,724 | 0 |
| All silver + 7 MF | -3,30,254 | 0 | 0 | ST 32,043 | 0 |
| **Actual 18 Nov sales (3B, incl. shares) + 5 Dec MF exits** | -3,56,541 | 0 (LT losses -3,152 set off first) | 0 | **ST about 61,800** | 0 |

Answers for Research v2:
1. Tax 2026-27 falls from Rs 9,915 to **Rs 0**, with or without the 7 MF exits.
2. Without the MF exits, **ST loss of about Rs 11,772 carries forward** (LT 0), usable against any capital
   gain for 8 years, only if the 2026-27 return is filed by 31 Jul 2027. With the 7 MF exits, the loss left
   (Rs 12,736 incl. the MF ST loss -963) is set off against MF LTCG that would have been exempt anyway, so
   nothing carries forward (cost about Rs 1,900 at 14.95%, up to Rs 4,570 at 35.88%, in a later year).
3. To keep a carry-forward and still exit: sell the 2 funds planned for 18 Nov now (net ST -3,027) and move
   the 5 gain funds (ICICI LC, Invesco Mid Cap, SBI PSU, ABSL PSU, LIC Infra) to on/after 1 Apr 2027, when
   their gains are mostly LT and exempt within that year's limit. Carry-forward then about **ST Rs 14,799**.
   Moving only the LT-only funds (Invesco MC, SBI PSU, LIC) keeps about Rs 5,811. Small sums; doing all
   exits this year for simplicity is reasonable.

## Gold plan (decided 2026-11-15): tax lines

Plan: gold to 5% of total (~Rs 14.2 L). Silver merge (sell ICICI Silver ETF, ICICI Silver FoF, Motilal
Gold+Silver FoF; ABSL Silver kept whole - changed 16 Nov: ABSL also sold, section 3A), proceeds into a gold ETF (e.g. GOLDIETF), then ~Rs 10.1 L more from
HDFC savings (~Rs 2.5 L Nov 2026 - early 2027) and the HDFC FD maturity on 10 May 2027.

- (a) Gold ETF buy and hold: listed in India, so LT after 12 months at 14.95% (AF s.197) and ST at slab
  35.88%; not equity-oriented and outside AF s.76 (1961 s.50AA); no Rs 1.25 L exemption; no STT (per
  `rules.md` s.10 reading of Finance (No.2) Act 2004 s.98; not checked on a contract note); stamp duty
  0.015% on each buy (Zerodha charges, 2026-11-15); no yearly tax while held. Each purchase is its own lot, sold
  FIFO; tranche buys over months give each tranche its own LT date (buy date + 12 months + 1 day).
- (b) FD maturity 10 May 2027: 2027-28 interest about Rs 34,100, tax about Rs 12,200 at 35.88%, TDS 10%
  (`tax/FY2026-27/fd-and-advance-tax.md`).
- (c) If the silver-merge date moves: the loss changes with prices/NAV on the sale day. ICICI Silver ETF
  lots turn LT on 2026-12-10 (56 u, -560), 2026-12-27 (500 u, -29,360) and 2027-01-22 (150 u, -23,344)
  (16 Nov close) - hence the "by 9 Dec" step; done: all sold 18 Nov, all ST (section 3B). An LT loss offsets only LT gains: still usable this year against
  the NXPI LTCG, but if carried forward it can only meet LT gains. FoF lots stay ST until Nov 2027
  (ICICI from 2027-11-12, Motilal from 2027-11-13). A sale after 31 Mar 2027 puts the loss in 2027-28: no
  use against the 2026-27 NXPI gain; it then follows the normal set-off and 8-year carry-forward rules
  (return by the due date). ICICI FoF exit load (1% within 15 days) applies only to sales before 18 Nov.

## 7. Order and timing (trade dates, all before 31 Mar 2027)

1. SIPs already changed (the SIP change of 16 Nov 2026 (portfolio/decisions.md), 2026-11-15): ABSL PSU, ICICI LC and Invesco PSU SIPs cancelled;
   new SIPs Rs 60,000 on the 1st of each month (UTI Nifty 50 21k, Parag Parikh 18k, HDFC Mid Cap 15k,
   Quant Small Cap 6k). Lot data (`tax/FY2026-27/angelone-mf-lots.csv`) ends at the last buys: 2026-11-02
   (ICICI LC, ABSL PSU, ICICI Silver FoF, Motilal FoF) and 2026-11-09 (Invesco PSU); the other exit funds
   earlier. The 2026-11-09 Invesco PSU lot (26.332 u, Rs 2,000) is ST and carries 1% load on 90% of units
   until 2027-11-09 (about Rs 18 if sold 18 Nov; included in the Rs 211). Kotak NN50 is kept.
   Each new monthly SIP lot in the 4 kept funds is its own lot: LT after 12 months, sold oldest first (FIFO).
2. Done Wed 18 Nov: sold all ABSL Silver ETF; redeemed ICICI Silver FoF, Motilal FoF, Nippon MC150 and
   Invesco PSU (section 3B).
3. Done Wed 18 Nov (was "by Wed 9 Dec"): sold all ICICI Silver ETF; bought GOLDIETF 1,770 (no tax).
4. Fri 11 - Mon 14 Dec: redeem ICICI LC, Invesco Mid Cap, SBI PSU, ABSL PSU, LIC Infra.
5. Advance tax (s.408; 1961 s.211): with QCOM sale 1, the losses lower the QCOM tax
   (`FY2026-27/fd-and-advance-tax.md` section 5). Without QCOM: with the metals sale, capital-gains
   tax is 0. Without it, about Rs 9,915 (75% by 15 Dec, 100% by 15 Mar); s.425(4) relief covers capital gains paid in the next instalment.

## 8. Differences from the first version of this file

| Item | Before (numbers.md G, NAV 2026-11-07) | Now (CSV, NAV 2026-11-13) | Why |
|---|---|---|---|
| Lot dates/units, 10 funds | - | identical except below | CSV matches numbers.md G.3 |
| Invesco PSU | 11 lots | 12 lots (+2026-11-09, 26.332 u, Rs 2,000) | SIP after 2026-11-07; still running |
| Invesco PSU old lots | not shown | 17 lots 2024-07-26..2025-12-01 fully gone | switched out 2025-12-10 into Invesco Mid Cap (a 2025-26 transfer; check it is in the AY2026-27 return) |
| CSV cost | incl. stamp duty | excl. stamp duty | stamp duty added back here; totals match |
| Kotak NN50 | -1,758 | +963 | NAV moved |
| Nippon MC150 | -6,368 | -2,270 | NAV moved |
| 8 MFs total | ST -7,559, LT +16,421, load ~314 | ST ~0, LT +20,644, load ~354 | NAVs, new lot |
| ICICI FoF / Motilal FoF | -15,123 / -5,741 | -19,858 / -10,698 | NAV fell |
| Tax baseline | Rs 8,622 (13%) | Rs 9,915 (14.95%) | 15% surcharge |
| Recommended dates | 18 Nov / 11 Dec | unchanged | new lots do not move any date |
| SIPs (fifth revision, the SIP change of 16 Nov 2026 (portfolio/decisions.md)) | step 1 said "stop SIPs" | SIPs already cancelled/changed; no new lots in exit funds or silver FoFs; last lots 2 Nov / 9 Nov confirmed in the CSV | finance-main change |

Third revision (user decision 2026-11-15: keep Kotak Nifty Next 50; new regime confirmed):

| Item | With 8 exits | With 7 exits | Why |
|---|---|---|---|
| MF exits value / ST / LT / load | 6,95,606 / ~0 / +20,644 / ~354 | 5,32,143 / -963 / +20,644 / ~354 | NN50 (+963 ST, 1,63,463) kept |
| A + MF exits only, tax | 9,915 | 9,771 | MF ST loss -963 now offsets NXPI LTCG |
| V2 + MF exits: exempt LTCG left / lost | 8,872 / 11,772 | 7,908 / 12,736 | |
| V2 + MF + Arbitrage: exempt left | 11,365 | 10,401 | |
| v1 + MF: exempt left | 11,797 | 10,833 | |
| All metals + MF: carry-forward | ST 4,344 | ST 5,308 | |
| Deferral option carry-forward | 13,836 / 4,847 | 14,799 / 5,811 | |
| V2 without MF exits; Arbitrage rows | unchanged | unchanged | no MF in them |
| Regime | not stated | new regime: 30% top slab, 15% surcharge (cap 25%) | no old-regime items were in the note; rates unchanged |

Sixth revision (user decision 2026-11-16: sell all silver incl. ABSL):

| Item | Before | Now | Why |
|---|---|---|---|
| ABSL Silver ETF | kept whole (-13,216 unrealised, 13 Nov) | sold 18 Nov: -34,226 (ST -35,337, LT +1,110) | user decision; price 177.03 -> 167.97 |
| ICICI Silver ETF | -47,538 (13 Nov) | -53,264 (16 Nov) | price 175.91 -> 167.80 |
| Silver total / tax saved | -78,094 / Rs 11,675 | -1,18,047 / Rs 17,648 (ABSL Rs 5,117) | |
| Advance tax (with QCOM) | 2,49,600 / 2,32,900 | 2,45,100 / 2,31,400; 1,53,600 / 1,91,400 from 17 Nov (specific identification, staged-sale 5) | Rs 5,973 less tax; then QCOM lot method |
| No-QCOM carry-forward | V2 + 7 MF: 0 | all silver + 7 MF: ST 32,043 | |

Seventh revision (actual fills 18 Nov 2026, section 3B; FoFs/MFs at NAV 17 Nov, charges estimated):

| Item | Before (16 Nov) | Now | Why |
|---|---|---|---|
| All silver | -1,18,047 (ST -1,19,157, LT +1,110) | -1,43,572 (ST -1,44,341, LT +769) | ETFs sold at 162.83 / 162.89; FoF NAVs fell |
| ICICI Silver ETF | by 9 Dec | sold 18 Nov, all ST | done early |
| Nippon MC150 + Invesco PSU | -3,027 | -3,484 | NAV 17 Nov |
| 6 loss shares + AZAD, KPIL | not in the plan | -3,797 (losses -4,675, gains +878) | sold 18 Nov (`FY2026-27/angelone-stocks.md` 6) |
| Tax saved with QCOM | silver Rs 17,648 | silver Rs 21,464; all 18 Nov sales Rs 4,583 more than plan | 14.95% |
| Advance tax (with QCOM) | 1,53,600 / 1,91,400 | 1,50,200 / 1,90,200 | staged-sale 5 |
| No-QCOM carry-forward | ST 32,043 | about ST 61,800 (with the 5 Dec MF exits) | more loss |

## 9. Data still needed

| Item | Have | Need |
|---|---|---|
| MF lots | `tax/FY2026-27/angelone-mf-lots.csv` (reconciled 2026-11-14) | CAMS/KFintech CAS only to confirm |
| ETF lots | AngelOne tradebook to 2026-11-06 | Contract note of 18 Nov (sale charges, GOLDIETF buy cost), CDSL statement, tradebook after 2026-11-06 |
| 18 Nov MF redemptions | NAV 17 Nov (AMFI), all units per the CSV | 18 Nov NAV (AMFI, published the evening of 18 Nov), redemption statements with units and NAV applied (19 Nov NAV if placed after 3 pm) |
| Exit loads | Groww pages | Each AMC's load on each lot's allotment date (ICICI LC change date 2026-04-06) |
| Prices | Actual ETF fills 18 Nov; NAV 17 Nov | Done for ETFs (section 3B); FoF/MF figures to update with the 18 Nov NAV |
| US INR values | yfinance rates | SBI TT buying rates; NXPI INR perquisite (Form 16 FY2018-19) |
| Fractions | 2026-11-13 estimate | Actual sale confirmations |

## 10. Questions

For the user:
1. Decided 16 Nov: sell all silver incl. ABSL (section 3A).
2. Do the 5 gain-fund exits this year (simple) or in April 2027 (keeps about Rs 14,799 of ST loss, 7 exits)?
3. Keep Kotak Arbitrage as parking, or exit now (free in V2 + MF exits)?
4. INDmoney loss lots: in the plan (16-25 Nov); they add carry-forward loss only (section 2).
5. Confirm income about Rs 1.06 Cr (15% surcharge band) under the new regime.

Former CA questions (answers in [ca-questions.md](ca-questions.md)):
1. Can ST loss be set off against taxable 12.5% LTCG first, leaving exempt s.198 LTCG untouched (Schedule CG order)?
2. Holding period of exchange sales: trade date or settlement date?
3. Confirm the Motilal and ICICI FoFs are not equity-oriented.
4. Exit load and ETF brokerage as transfer cost (s.72(1)(a); 1961 s.48(i)).
5. INR cost of NXPI (Form 16 perquisite vs month-end rate).
6. Was the 2025-12-10 Invesco PSU -> Invesco Mid Cap switch reported in the AY2026-27 return?
