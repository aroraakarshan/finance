# Expertise-edge picks: checked

## Summary
- Survives, on WATCH only (Rs 0 now): Infineon (IFX, Xetra), score 3/5, Rs 1.5 L by swapping out the NU reservation after Feb 2027, and only after you ask Microsoft's insider-trading contact (finance-legal's answer, `legal/compliance/insider-trading.md`: user to ask).
- Dropped: Synopsys (2/5: your own signoff tool vendor, the highest insider-information risk, US-situs), MPWR (2/5), FormFactor (1/5), Vicor (1/5): all US-situs chip names, and research says "technology: do not add chips" while you hold 30.4% in chips.
- Agreed avoids: Navitas, AOSL, the Indian semi-theme stocks (Kaynes, CG Power).
- Hitachi Energy India (POWERINDIA): avoid now (Rs 30,885, P/E 114, 16 Nov); research WATCH at or below Rs 25,000, only if Q3 FY27 operating EBITDA margin is 15% or more and non-HVDC orders grow ([POWERINDIA.md](../../../research/stocks/POWERINDIA.md)); no insider-policy reason to avoid (finance-research).
- Main errors in the report: SOX fell 12.25% on 5 Nov (not about 9%), QCOM 9.5% (not 11.2%); Synopsys no longer owns PowerArtist (sold to Keysight); Infineon is the most QCOM-linked pick (weekly corr 0.44), not a diversifier; it uses Rs 89/USD (actual 94.20) and ignores that Rs 20.75 L of the Rs 21.05 L 5% limit is already used.
- Do nothing now. Ask finance-legal first (Microsoft trading policy, vendors, insider information); nothing here is a legal conclusion.

Checked 2026-11-15 by `finance-scout` (helper `scout-verify-edge`) against the unchecked report
`~/.local/share/superpowers/finance/opportunities/expertise-edge.md`. Prices: yfinance closes of 2026-11-13 ([Y]),
cached in `~/.local/share/finance-cache/market/scout-verify-edge/`. [SA] = stockanalysis.com, read 2026-11-15.
Portfolio: Rs 4,20,97,035 (`portfolio/summary.md`, 2026-11-15); USD/INR 94.1997 (`scout/buy-list.md`).
EUR/INR about 105.2 = 94.20 x 1.117 (IFNNY $55.71 / IFX EUR 49.875, ADR 1:1, [Y] 13 Nov).

## Claim check

| # | Claim in the report | Verdict | Correct value and source |
|---|---|---|---|
| 1 | SOX fell about 9% on 5 Nov 2026 | WRONG | -12.25% (10,268.65 -> 9,011.14); worst day since 16 Mar 2020 ([Y]; Yahoo Finance article 2026-11-06) |
| 2 | Worst chip sell-off since 2020 | CONFIRMED | Same sources; second-largest one-day fall on record |
| 3 | Cause: fear of data-center rules after the midterms | CONFIRMED in part | Forbes 2026-11-05: fear that a Democratic Congress slows the data-center build-out; QCOM fell on its own EPS guide |
| 4 | QCOM fell 11.2% that day | WRONG | -9.5% at the close (173.19 -> 156.75, [Y]); about -10.5% intraday (Forbes 2026-11-05) |
| 5 | Several picks 20-30% under their 50-day averages | CONFIRMED for 2 of 5 | VICR 159.05 vs 218.92 (-27%), FORM 87.53 vs 112.83 (-22%); IFX 49.88 vs 54.98 (-9%); SNPS 455.20 vs 445.16 (+2%) and MPWR 1,390.54 vs 1,284.98 (+8%) are above ([Y]) |
| 6 | Only Infineon and Synopsys diversify away from chip beta | WRONG | 2-yr weekly corr with QCOM: IFX 0.44 (highest of the five), SNPS 0.33, FORM 0.32, VICR 0.31, MPWR 0.30 (table below) |
| 7 | Rs 89 per USD | WRONG | 94.1997 (`scout/buy-list.md`); Rs 4.2 L = about USD 4,460 or EUR 3,990, not USD 4,700 / EUR 4,500 |
| 8 | Plan Rs 17.9 L, Rs 3 L reserve, inside Rs 21 L | WRONG for you | Arithmetic is right (4.2+4.2+3.5+3.0+3.0), but Rs 20.75 L of the Rs 21.05 L 5% limit is already used (`scout/buy-list.md`): Rs 0.30 L free |
| 9 | IFX EUR 49.88; EUR 59.50 at FY26 end | CONFIRMED | 49.875 on 13 Nov; 59.50 on 30 Sep 2026 ([Y], [SA]) |
| 10 | IFX Q4 FY26 revenue EUR 4.706B, segment margin 23.8% | CONFIRMED | Infineon release 2026-11-10 |
| 11 | IFX FY26 revenue EUR 16.353B, +12% | CONFIRMED | [SA] LTM 16.35B; [Y] totalRevenue 16.353B |
| 12 | IFX FY27 guide over 20% growth, margin +5 points; data-center power close to EUR 4B | CONFIRMED | Infineon release 2026-11-10 |
| 13 | IFX "about EUR 20B" FY27, data-center from EUR 2.2B, deals over EUR 10B, two price rises, FCF guide EUR 1.8B vs 2.26B | UNVERIFIED | Not in the release excerpts read |
| 14 | IFX forward P/E 17.5 | CONFIRMED | [SA] 17.45; [Y] shows 12.9 from a forward EPS of EUR 3.88 that does not fit LTM EPS 1.14 (likely a Yahoo EPS error, see `market-data` skill) |
| 15 | IFX 5-yr forward P/E range 10.5-23 | UNVERIFIED | |
| 16 | IFX is a respondent in Vicor's ITC case | CONFIRMED | USITC release 2026-10-09; inv. 337-TA-1526 (J&C IP 2026-10-12) |
| 17 | German dividend withholding 26.375%, treaty 10% | CONFIRMED | Same as `scout/buy-list.md` rank 5 (tax #21) |
| 18 | Synopsys closed Ansys on 17 Jul 2025 | CONFIRMED | Synopsys release 2025-07-17 |
| 19 | Synopsys owns RedHawk-SC, Totem, PowerArtist | WRONG in part | PowerArtist was sold to Keysight as a condition of the deal (approved 2025-10-10, closing about 2025-10-17, Synopsys release); RedHawk-SC and Totem came with Ansys |
| 20 | SNPS FQ3 2026 revenue $2.477B, +42% | CONFIRMED | $2.477B vs $1.740B = +42.4% (Synopsys release 2026-08-26) |
| 21 | SNPS FY26 guide midpoint $9.715B | CONFIRMED | Range $9.690-9.740B (Synopsys IR) |
| 22 | SNPS non-GAAP EPS $3.91; interest coverage 1.66; fwd P/E 31.7-45.3 FY21-25; EV/FCF 34 | UNVERIFIED | |
| 23 | SNPS forward P/E 25.9 | UNVERIFIED | [Y] 24.4 |
| 24 | SNPS +14% in 52 weeks; beta 1.18 | WRONG / CONFIRMED | +16.8% ([Y] closes; Yahoo 16.6%); beta 1.184 ([Y]) |
| 25 | SNPS results 8 Dec 2026 after the close | CONFIRMED | Synopsys release 2026-11-05 |
| 26 | Cadence forward P/E 34.3; 2026 growth guide 21% | UNVERIFIED | [Y] fwd P/E 32.8, latest quarter +22% |
| 27 | MPWR Q3 revenue $1.202B, +63% | CONFIRMED | $1,202.4M, +63.1% (MPS commentary 2026-10-29, SEC 8-K) |
| 28 | MPWR Enterprise Data $506.7M, +165%, 42% of revenue; Communications +135% | CONFIRMED | +164.6%, 42.1%, +134.7% (same) |
| 29 | MPWR non-GAAP EPS $8.19; 2026 ED floor 150%; SBC $106M | UNVERIFIED | |
| 30 | MPWR forward P/E 32.7; range 28-61 | UNVERIFIED | [Y] 29.8 |
| 31 | MPWR trailing P/E 76.6; beta 1.73 | CONFIRMED | [Y] 76.2, 1.725 |
| 32 | MPS is an ITC respondent | CONFIRMED | USITC 2026-10-09 |
| 33 | VICR Q3 revenue $197.1M, +78.5% y/y, +37.5% q/q, GM 68.3%, backlog $406M +166% | CONFIRMED | Vicor release 2026-10-20 (SEC 8-K) |
| 34 | VICR net income $63.3M; 5x capacity in 3 fabs | UNVERIFIED | |
| 35 | VICR cash $513M, no meaningful debt | CONFIRMED | $513.14M cash, $7.16M debt ([SA]) |
| 36 | First VPD license 16 Sep 2026 | CONFIRMED | Vicor release 2026-09-16 ("leading AI OEM"; not said to be the first) |
| 37 | ITC opened 9 Oct 2026; respondents Delta, Infineon, Luxshare, MPS, Flex, Celestica, Quanta, Foxconn, Ingrasys; limited exclusion order | CONFIRMED | USITC 2026-10-09: 20 respondent entities; Vicor also asks for cease-and-desist orders; complaint filed 9 Sep 2026 |
| 38 | ITC hearing mid-2027, decision 2028 | UNVERIFIED | Report's own estimate |
| 39 | VICR close $159, 50-day $219; fwd P/E 29.1; EV/FCF 134 | CONFIRMED | [Y] 159.05 / 218.92; [SA] 29.11, 134.45 ([Y] fwd P/E 26.2). Off its 30 Jun high of $379.78: -58% |
| 40 | VICR insiders own 44% | CONFIRMED | [SA] 44.10% (counts class B); [Y] 25.5% (class A only) |
| 41 | FORM Q3 revenue $280.5M, 4th record, about +40%; net income $73.8M | CONFIRMED | +38.4% (FormFactor release 2026-10-28) |
| 42 | FORM foundry/logic +10% q/q | UNVERIFIED | |
| 43 | FORM close $87.53, 50-day $113 | CONFIRMED | [Y] 87.53 / 112.83 |
| 44 | FORM forward P/E 21.6, PEG 0.30 | UNVERIFIED | [Y] 20.4 and PEG 1.39 |
| 45 | NVTS market cap $2.41B, P/S about 60, beta 4.1 | CONFIRMED | [Y] $2.412B, 59.7, 4.13 |
| 46 | NVTS Q4 guide $16M; shares +22% | UNVERIFIED | |
| 47 | Kaynes -47% in 52 weeks; Q2 FY27 profit -62% | CONFIRMED | -45.8% ([Y] closes); -61.6% to Rs 45.42 cr (ET Manufacturing, CNBC-TV18, 2026-11-15) |
| 48 | Forward P/E CG Power 67, Hitachi Energy India 75, Kaynes 47 | UNVERIFIED | [Y] 58.8, 62.8, 39.2 |
| 49 | AOSL -10.9% on 13 Nov; P/S 1.2; loss over 12 months | CONFIRMED | 30.53 -> 27.20; 1.22; trailing EPS -1.54 ([Y]) |
| 50 | B. Riley cut AOSL target to $22 | UNVERIFIED | |
| 51 | Your QCOM/MSFT holding is over the $60k estate threshold | CONFIRMED | US-situs $207,935-213,304 (`scout/ideas/us-estate-tax.md`) |
| 52 | Delta, Ibiden, Vertiv figures; IBKR Taiwan access | UNVERIFIED | Not checked (watchlist only) |

## Fit with your rules

| Pick | 2-yr weekly corr QCOM / MSFT | 1-yr corr QCOM | 5 Nov move | US-situs | Breaks |
|---|---|---|---|---|---|
| Infineon IFX.DE | 0.44 / 0.23 | 0.42 | -8.5% | No | Chips; corr above 0.4 |
| Synopsys SNPS | 0.33 / 0.38 | 0.29 | -4.9% | Yes | Tech; US-situs; your own tool vendor |
| MPWR | 0.30 / 0.27 | 0.21 | -10.3% | Yes | Chips; US-situs; beta 1.73 |
| Vicor VICR | 0.31 / 0.16 | 0.28 | -15.1% | Yes | Chips; US-situs; beta 2.46; legal binary |
| FormFactor FORM | 0.32 / 0.08 | 0.19 | -15.8% | Yes | Chips; US-situs; cyclical |
| For scale: SOX, SOXX | 0.61, 0.62 / 0.26, 0.23 | 0.55, 0.56 | -12.2%, -12.1% | - | - |
| UCITS chip funds SEMI.L, IUIT.L | 0.56, 0.58 / 0.21, 0.53 | 0.53, 0.57 | -9.9%, -5.0% | No | Hold NVDA, AVGO, QCOM: no UCITS fits |

Weekly Friday closes 2024-11-15 to 2026-11-13, 104 weeks, [Y].

- Sector rule: `research/sectors/README.md` says technology "do not add"; `research/events/2026-11-15/semis-selloff-nvda-arm.md` says WAIT, no chip buy (ARM corr with QCOM 0.50; AVGO 0.33, NVDA 0.27).
- Chip share: 30.4% (QCOM, AVGO, NVDA, Rs 1,28,05,537; `research/themes/employer-stock-concentration.md`). The scout method scores diversification 0 when two of corr under 0.4, not US-situs, not tech fail: all five fail at least two.
- The 5% limit: Rs 17.75 L ready + Rs 3.0 L reserved (KVB, NU) = Rs 20.75 L of Rs 21.05 L. Any pick needs a swap.
- Foreign money slots (10% of each QCOM/MSFT sale, from EXUS): sale 1 Rs 0.30 L left, sale 2 Rs 0.11 L, Aug 2027 Rs 0.91 L after ENR.
- US estate: each US-listed pick adds to a US-situs estate already 3.5x the $60k threshold. Infineon on Xetra does not.
- Trading rules: these would be long-term buys (not the Rs 2 L paper budget); the 5-day earnings rule does not apply, but timing after results is still sensible.

## Ranked picks

| Rank | Pick | Score (1-5) | Verdict | Size | Money and timing | Swap under the 5% |
|---|---|---|---|---|---|---|
| 1 | Infineon IFX (Xetra, IBKR, EUR) | 3 | WATCH, Rs 0 now | Rs 1.5 L (about EUR 1,430), not Rs 4.2 L: chips and corr 0.44 keep it under half the 1% cap, like ENR | Dollars at IBKR from the NU reservation; earliest after Infineon Q1 FY27 and NU Q4 2026 results (both Feb 2027; dates not verified), in 2 halves | Release the NU Rs 1.5 L only if NU's trigger has not fired by then; otherwise wait for the next MSFT-lot slot (to Sep 2028) |
| - | Synopsys SNPS | 2 | DROP for now | Rs 0 | - | Recheck only if finance-legal says no restriction and you accept US-situs; results 8 Dec 2026 |
| - | MPWR | 2 | DROP | Rs 0 | - | - |
| - | FormFactor FORM | 1 | DROP | Rs 0 | - | - |
| - | Vicor VICR | 1 | DROP | Rs 0 | - | - |

Why Infineon is 3/5: results confirmed by the company (FY27 over +20%, data-center power near EUR 4B), forward P/E 17.45 ([SA]), 9% under its 50-day and 13% under its 200-day average, not US-situs. Against: it is a chip stock with the highest QCOM link of the five, an ITC respondent, and German withholding needs a yearly reclaim.
Why the others drop: each is a US-situs chip or tech stock against the sector rule; Synopsys adds the highest insider-information risk (you use RedHawk-SC daily); Vicor's value turns on ITC 337-TA-1526, where hyperscaler licensing could involve your employer; FormFactor's link to your skill is weak (the report says so).

## Questions for finance-legal
1. Microsoft trading policy: does your role or level need pre-clearance or blackout windows for any trade, or only for designated insiders?
2. Does Microsoft keep a restricted list of suppliers, vendors or partners? Are Synopsys, Cadence, Infineon, MPS, Vicor or FormFactor on it?
3. Conflict of interest: must you disclose or avoid holding shares in a vendor whose tools you use or evaluate (Synopsys RedHawk-SC, Cadence Voltus)? Is there a size threshold?
4. Insider information: which of these count as material non-public information for the vendor: EDA roadmaps under NDA, license or pricing talks, which power-module vendor a Microsoft chip uses, Microsoft's position in ITC 337-TA-1526? Does any bar all trading in that stock, or only around events?
5. Do US insider-trading law (for SNPS, MPWR, VICR, FORM) and EU MAR (for IFX on Xetra) apply to you as an Indian resident trading at IBKR?
6. FEMA/LRS for each listing: NASDAQ common shares (SNPS, MPWR, VICR, FORM) and Xetra shares (IFX) as portfolio investment under the Overseas Investment Rules 2022; is the OTC ADR IFNNY allowed (the trading rules already exclude OTC)?

## Questions for finance-tax
1. Infineon: German withholding 26.375%, India credit 10%, reclaim 16.375% from the BZSt: same as ENR (tax row 26)?
2. Is an Infineon ADR (IFNNY) US-situs for estate tax? (`semis-selloff-nvda-arm.md`: unsettled for ADRs.)
3. Extra US estate tax per Rs 1 L of a US-listed pick at your current US-situs total.

## Discrepancies found
- `research/events/2026-11-15/semis-selloff-nvda-arm.md` says you hold 43.0% in chips; that is the old total (and close to QCOM+MSFT, 43.1%). The current chip share is 30.4% (`research/themes/employer-stock-concentration.md`, `scout/ideas/arm-trvi.md`). For finance-research.
- The report's valuation numbers differ from Yahoo for most stocks (forward P/E SNPS, MPWR, FORM, CDNS, Indian names); stockanalysis matched where checked (IFX, VICR). Not an error in itself: different analyst sets.
