# SELLAS Life Sciences (SLS) post-mortem - REGAL Phase 3 readout, 17 Nov 2026

Written by scout-ev-sls for finance-scout, 18 Nov 2026. Prices from yfinance (pulled 18 Nov 2026
about 01:40 IST). Company facts from SEC EDGAR filings and SELLAS press releases (links in Sources).
Source tags: [P] yfinance prices, [Sn] numbered sources at the end.

## Summary

- Was it visible? YES. A binary Phase 3 readout was public for almost two years, and its timing
  narrowed step by step:
  - since 23 Jan 2025: interim at 60 deaths passed, final analysis at 80 deaths "this year" [S3];
  - since 12 May 2026: 78 of 80 deaths counted; readout clearly months away [S6];
  - since 28 Oct 2026: 80th death reached, topline "this quarter" [S8];
  - since 12 Nov 2026: topline "this month" (press release) and "in November 2026" (10-Q) [S9, S10].
  An outside investor could have known "binary readout in about November 2026" on 28 Oct 2026
  (close 10.38) and the exact month on 12 Nov 2026 (close 8.03). Close before readout: 7.47 on
  16 Nov 2026 [P].
- Why we missed it: our screens drop loss-making companies (SLS lost $28.1 M in Jan-Sep 2026 [S10]),
  and we have no calendar of company-guided clinical readouts. The other filters did not block it:
  price was above $5 every day from 13 May 2026 [P]; market cap before the readout was about
  $1.52 B (7.47 x 203.86 M shares) [P, S10].
- What we would have needed: (1) a binary-event calendar fed by 8-K / press-release text
  ("final analysis", "Nth event", "topline", "IDMC"), not by profit screens; (2) an event-count
  tracker for trials whose readout date depends on deaths/events; (3) a separate "event bet"
  bucket with its own small size cap that is not subject to the profit filter.
- Could we have bought it under the rules? Only partly. The trading rules in AGENTS.md were approved on
  15 Nov 2026 for paper trading only (real money after 8 weeks and 20 paper trades) and cover only the
  Rs 2 L trading budget; no event-bet money existed before the user's decision of 18 Nov 2026
  (portfolio/targets.md, "Event bets"). (Corrected 18 Nov 2026: an earlier draft said the rules were
  all TBD, from an old copy of the finance rules.) Under the rules the user stated: price above $5 OK,
  0.5% cap (Rs 2.1 L = about $2,228 at 94.24 INR/USD on 16 Nov [P]) = about 298 shares at 7.47.
  Result at the 17 Nov close 19.15: about +$3,480 before tax, about +$2,230 after 35.88% slab tax
  (held under 24 months). A failed trial would likely have cost most of the $2,228.
- Now (after +156%): verdict AVOID (Rs 0), as in [research](../../research/stocks/SLS.md)
  (finance-research, 18 Nov 2026). The binary event is over; what is left is a slower regulatory
  path (BLA in 1H 2027, FDA decision most likely 2028), up to $322.5 M of new stock (a $150 M
  underwritten offering announced 17 Nov plus a $22.5 M option, and a separate unused $150 M ATM),
  a small open-label trial with p=0.035, and 28% of float sold short. At about $17 (after hours
  $17.13 on 17 Nov, after the offering; news/market/2026-11-18.md) the price assumes $1.6-2.5 B a
  year of US sales from a niche of about 1,000-1,500 US patients; research's risk-adjusted value
  is about $1.4 (low) / $4 (base, $3.7) / $11-16 (high) a share (SLS.md section 5, 18 Nov 2026).

## 1. Facts checked

| Item | Value | Source |
|---|---|---|
| Last close before readout | 7.47 on Mon 16 Nov 2026 (Fri 13 Nov: 7.86) | [P] |
| 17 Nov 2026 | open 24.11, high 24.89, low 16.70, close 19.15, volume 119.9 M (30-day average to 16 Nov: 7.0 M); after hours $17.13 on the offering news | [P] re-pulled by finance-research 18 Nov 2026 (research/stocks/SLS.md); after hours: news/market/2026-11-18.md |
| Move | 7.47 -> 19.15 = +156.4% | [P] |
| Readout | Primary endpoint OS met; HR 0.59 (41% lower risk of death); two-sided p=0.035; median OS 24.0 vs 14.7 months; 126 patients randomized 1:1 vs best available treatment; open-label; analysis at the pre-set 80 deaths; safety mostly grade 1/2 injection-site reactions | [S11] 8-K 17 Nov 2026 |
| FDA plan | Meet FDA "to discuss an accelerated filing strategy" and prepare a BLA "in the first half of 2027"; full data at a future medical meeting | [S11] |
| Designations | GPS has FDA Orphan Drug and Fast Track in AML; Rare Pediatric Disease (pediatric AML, Oct 2024) | [S10] 10-Q p.21 |
| China rights | 3D Medicines holds Greater China rights; SELLAS lost the arbitration on 24 Jul 2026 (paid about $1.0 M of costs); $191.5 M of milestones still possible | [S12] 8-K 27 Jul 2026 |

Discrepancies found:
- The brief said "14 Nov close". 14 Nov 2026 was a Saturday; the last close before the readout is
  16 Nov 2026 (7.47). Using 13 Nov (7.86) the move is +143.7%.
- yfinance gave 19.10 and 19.16 in pulls before the US close (02:30 IST on 18 Nov), so those were
  intraday prices. The final close, pulled at 02:34 IST on 18 Nov 2026, is 19.15; 19.15 is used. News sites quoted +165% intraday (wallstreetobserver, 17 Nov 2026).
- clinicaltrials.gov NCT04229979 still shows primary completion "2025-12 (estimated)", last
  updated 1 Oct 2025 [S1]. A screen that trusts registry dates would have looked in Dec 2025 and
  then dropped it. Registry start date is 8 Feb 2021 (first posted 18 Jan 2020).

Discrepancies fixed (18 Nov 2026, from [research](../../research/stocks/SLS.md) section 11):
- Offering: this note said "a $150 M ATM ready to sell shares". The 17 Nov sale is a separate
  $150 M underwritten offering (J.P. Morgan, TD Cowen; plus a 30-day option for $22.5 M), not priced
  at 18 Nov 12:00 IST; the $150 M ATM is still unused and usable after the 60-day lock-up (about
  mid-Jan 2027). Up to $322.5 M of new stock in all (preliminary 424B5, 17 Nov 2026).
- 17 Nov bar: open 24.00 -> 24.11, low 16.72 -> 16.70, volume 113.9 M -> 119.9 M (yfinance re-pull
  by finance-research, 18 Nov 2026). The close 19.15 and high 24.89 are unchanged.
- After hours on 17 Nov: $17.13 once the offering was announced (finance-news,
  news/market/2026-11-18.md); it was missing here.
- Highest close in the past year: the prospectus says $15.46; this note has 15.45 (29 Jun, yfinance).
  Left as is (small rounding gap between sources).

## 2. Timeline - was it visible beforehand?

| Date | Event | SLS close (day move) [P] | Source |
|---|---|---|---|
| 18 Jan 2020 | REGAL registered (NCT04229979); planned 125-140 patients, interim at 60 deaths | 3.66 (10 Jan) | [S1], [S10] |
| 8 Feb 2021 | Trial start (actual) per registry | - | [S1] |
| Mar 2024 | Enrollment completed (127 patients per registry) | about 1.0-1.5 | [S10], [S1] |
| 10 Dec 2024 | 60th death reached, interim analysis triggered | 1.04 (-4.6%); 0.90 next day (-13.5%) | [S2] |
| 23 Jan 2025 | IDMC interim (60 deaths): passed futility, no safety issue, "continue without modification"; did NOT stop early for efficacy. Company: under 50% of patients dead at 13.5 months median follow-up. Final at 80 deaths, "this year" | 0.99 (-13.2%, 28 M shares); 1.41 on 27 Jan (+39.6%) | [S3] |
| 7 Aug 2025 | IDMC "pre-specified analysis": continue without modification; final at 80 deaths "by year-end" | 1.60 (+0.6%) | [S4] (8-K 12 Aug 2025) |
| 13 Nov 2025 | Q3 PR: final "by year-end 2025"; "event driven ... may occur at a different time" | about 1.6-1.8 | [S5] |
| 29 Dec 2025 | One-time update: 72 deaths as of 26 Dec 2025; 80th not reached; CEO: "every passing month may increase the probability of a successful study" | 3.35 (+16.7%, 22.6 M shares) | [S13] |
| 5 Jan 2026 | First close at or above $5 | 5.00 (+14.9%) | [P] |
| 12 May 2026 | Q1 PR: 78 deaths as of 11 May 2026; company will announce the 80th | 5.22; 6.53 next day (+25.1%) | [S6] |
| 13 May 2026 | From here every close is above $5 | 6.53 | [P] |
| 26 Jun 2026 to 29 Jun 2026 | Run-up, no filing found | 12.39 -> 15.45 | [P] |
| 24-28 Jul 2026 | Lost 3D Medicines arbitration | 11.32 -> 10.09 | [S12] |
| 11 Aug 2026 | Q2 PR: still waiting for 80th death | about 11-13 | [S7] |
| 28 Oct 2026 | 80th death reached; topline "this quarter" | 10.38 (-14.7%, 23.8 M shares) | [S8] |
| 30 Oct 2026 | Short interest 57.1 M shares = 28.2% of float, 8.6 days to cover (prior month 55.1 M) | 9.68 | yfinance info, pulled 18 Nov 2026 |
| 12 Nov 2026 | Q3 PR: topline "this month"; 10-Q: topline "in November 2026" | 8.03 (-4.6%) | [S9], [S10] |
| 16 Nov 2026 | Last close before readout | 7.47 (-5.0%) | [P] |
| 17 Nov 2026 | Positive topline, pre-market | 19.15 (+156.4%) | [S11] |

Reading the timeline:
- The death count slowed sharply: 60 by Dec 2024, 72 by Dec 2025, 78 by May 2026, 80 by Oct 2026
  (8 deaths in 10 months) [S2, S13, S6, S8]. In a blinded OS trial, slow event accrual means
  pooled survival is longer than planned. It is a weak hint (the control arm can also do better),
  but the company and the market read it as positive: the stock went from 1.50 (1 Dec 2025) to
  15.45 (29 Jun 2026) [P] while the readout kept slipping.
- Prior IDMC "continue" decisions said only that the trial was not futile and safe. They did not
  say it would win; the Jan 2025 interim was also an efficacy look that did not stop the trial.
  The stock fell on both 60-death news days and on the 80th-death day, so "continue" news was not
  a reliable buy signal on the day.
- The pre-readout weeks were weak: 12.17 (27 Oct) -> 7.47 (16 Nov), -39% [P], with heavy shorting.
  Risk-off before a binary event is common; the lowest entry was right before the event.

## 3. Rule check (could we have bought it?)

| Check | SLS before the readout | Pass? | Source |
|---|---|---|---|
| Repo trading rules | Approved 15 Nov 2026 for paper trading only, Rs 2 L budget, max loss Rs 2,000 a trade, no entry within 5 trading days before results; no event-bet slot until 18 Nov 2026 | NO for real money | AGENTS.md, Trading rules; portfolio/targets.md, Event bets |
| No stocks under $5 | Under $5 until 7 May 2026; above $5 every day 13 May - 16 Nov 2026 (7.47 on 16 Nov) | YES from 13 May 2026 | [P] |
| Market cap | about $1.52 B on 16 Nov (7.47 x 203.86 M shares at 11 Nov 2026) | YES (not a micro cap) | [P], [S10] |
| Profitable | Net loss $28.1 M in Jan-Sep 2026; accumulated deficit $303.1 M | NO - this is the filter that dropped it | [S10] |
| Cash runway | $134.7 M cash at 30 Sep 2026; operating cash use $22.4 M in 9 months (about $30 M a year); company says enough for 12+ months; no going-concern doubt | YES | [S10] |
| Dilution history | Shares 28.3 M (15 Mar 2023) -> 70.4 M (12 Nov 2024) -> 142.4 M (11 Nov 2025) -> 203.9 M (11 Nov 2026), about 7.2x in 3.7 years; offerings with warrants 2023-2025; $85.1 M from 50.4 M warrant exercises at $1.69 average in Jan-Sep 2026; 8.1 M warrants left ($1.41-$2.00) | Heavy dilution, now funded | XBRL dei shares [S14], [S10] |
| ATM | $150 M ATM with TD Cowen since Mar 2026 (S-3ASR 20 Mar 2026); none sold as of 12 Nov 2026 | Overhang now, on top of the 17 Nov $150 M offering | [S10], [S6], [S17] |
| US-situs | Yes (US company, Nasdaq). Adds to US estate tax exposure that idea 2 is trying to shrink | Soft NO for size | scout/ideas.md |
| Tax | Foreign shares held under 24 months: slab 35.88%; over 24 months 14.95% | Event trades are always short-term | scout/universe.md |
| Size cap 0.5% (about Rs 2.1 L) | about $2,228 = 298 shares at 7.47 | YES | [P] FX 94.24 on 16 Nov |

What it would have paid: 298 shares x (19.15 - 7.47) = about $3,480; after 35.88% tax about
$2,230 (about Rs 2.08 L at 93.46 on 17 Nov) [P]. That is about +0.5% of the portfolio, for a
bet where a fail would likely have lost most of $2,228 (about -0.4%). Entry on 28 Oct (10.38) would
have made +85%; on 12 Nov (8.03) +139% [P].

Base rates for the setup:
- Oncology Phase 3 -> filing success was 47.5% (n=495), the lowest of all disease areas;
  oncology filing -> approval 92.0% (n=324); average regulatory stage 1.3 years. BIO / Informa /
  QLS, "Clinical Development Success Rates 2011-2020" (Feb 2021) [S15].
- So before the readout this was roughly a coin flip. Points against: cancer vaccines have a poor
  Phase 3 record, the trial was small (126 patients) and open-label, and the 60-death interim did
  not stop for efficacy. Points for: interim passed futility, slow death accrual, Orphan and Fast
  Track status, strong single-arm Phase 2 survival claims. A coin flip with a +150% / -70% payoff
  is a positive-expectation bet only at a small size; it fits a capped "event bet" bucket, not
  the core portfolio.

## 4. Lessons

Filters that dropped it:
- Profit filter: SLS has never been profitable; every clinical-stage biotech fails it.
- No event calendar: nothing in our feed reads 8-K / press-release text for trial milestones.
- Registry dates are stale: clinicaltrials.gov still said Dec 2025.
- (Not a cause this time) price under $5 would have blocked it until May 2026, and dilution and
  warrants would have flagged it as risky in 2024-2025.

Signals that would have put it on a watch list:
- "Final analysis at N events" plus a published event count close to N (72/80 in Dec 2025,
  78/80 in May 2026).
- "IDMC recommends continuing without modification" after a futility interim.
- "Nth event reached / database lock / topline this quarter" (28 Oct 2026).
- A 10-Q or press release giving a month ("November 2026", "this month").
- Short interest above 20% of float into a dated binary event.

Rules for the calendar (proposed for finance-scout):
1. Binary-event calendar outside the profit screens. Every week, scan 8-K and press-release text of
   Nasdaq/NYSE companies above $5 and $300 M market cap for "topline", "final analysis",
   "pivotal", "PDUFA", "IDMC", "database lock", "Nth event". Each hit becomes a calendar row
   (company, trial, endpoint, guided window, source date). Loss-making is allowed here.
2. Event-count tracker for event-driven trials. For trials whose readout depends on deaths or
   events: record the trigger (e.g. 80 deaths), every disclosed count with its date (60, 72, 78),
   and the accrual rate. Flag WATCH when the count is within 10% of the trigger or the company
   gives a quarter; flag IMMINENT when the company announces the trigger event or database lock
   (readout usually within 2-6 weeks: here 20 days). Do not trust clinicaltrials.gov dates;
   use the latest company statement.
3. Re-check guidance every quarter. On each 10-Q/10-K and earnings PR, update the guided window;
   a slip ("by year-end" -> "when the 80th event occurs") stays on the list, it does not drop off.
   Read the 10-Q text: it can be more precise than the PR (here "November 2026").
4. "Event bet" bucket with its own limits. Up to 0.5% per name (about Rs 2.1 L), at most 1-2%
   total in open event bets; size for a total loss; buy only after the company names a quarter or
   month; exit or re-decide within a day of the result. The user set this slot on 18 Nov 2026 with a
   3% total cap and approval of each bet (portfolio/targets.md, "Event bets"); the pre-bet checklist
   is in [calendar.md](calendar.md).
5. Pre-event checklist before any event bet: base rate for the phase and area (BIO 2011-2020),
   cash runway past the event, ATM/shelf in place (a raise after a spike is likely), short interest,
   size of the trial and whether it is blinded, and whether US-situs adds to the estate-tax issue.

## 5. What happens next (verdict: AVOID)

- Price now about 19.15, market cap about $3.9 B vs $134.7 M cash [P, S10]. The binary event is
  done; the next steps are slower and the stock has priced in a large part of approval.
- Regulatory path: FDA meeting first, BLA in 1H 2027 [S11]. Under PDUFA a new BLA gets a decision
  goal 10 months after the 60-day filing date (standard) or 6 months (priority), i.e. 12 or 8 months
  from submission [S16]. With a 1H 2027 submission the FDA decision is most likely between early
  2028 and mid 2028, unless the FDA asks for more data.
- Base rate filing -> eventual approval in oncology (after any resubmission, not first cycle): 92.0% (BIO 2011-2020) [S15], but that average covers
  filed applications; risks here are one small open-label trial, p=0.035 (close to 0.05), and full
  secondary data not yet shown. The FDA may want more, which would delay or block approval.
- Dilution: the raise came the same day. On 17 Nov SELLAS announced a $150 M underwritten offering
  (plus a 30-day option for $22.5 M), not priced at 18 Nov 12:00 IST; the separate $150 M ATM was
  unused on 12 Nov 2026 [S10] and is usable after the 60-day lock-up (about mid-Jan 2027) [S17].
  Up to $322.5 M of new stock in all; at about $17 the offering is about 9-10.5 M shares (+5%) and
  the full ATM about 8.8 M more (research/stocks/SLS.md, 18 Nov 2026). Watch EDGAR for the final 424B5.
- Other catalysts: SLS009 Phase 2 first-line AML preliminary topline Q4 2026; SLS009 r/r AML data
  at ASH 12-15 Dec 2026; full REGAL data at a future medical meeting [S9, S11].
- Volatility: 17 Nov range 16.72-24.89 [P]; short interest 28.2% of float (30 Oct) may keep it
  swinging both ways.
- Tax and size: any trade now is short-term (35.88%) and US-situs; no edge left from the event.

Verdict: AVOID (Rs 0), per [research](../../research/stocks/SLS.md) (18 Nov 2026). Not an event bet
now (the binary event is past) and not a long-term buy: at about $17 the price assumes $1.6-2.5 B a
year of US sales from about 1,000-1,500 US patients a year; research's risk-adjusted value is about
$1.4 (low) / $4 (base) / $11-16 (high) a share.
Look again only if:
- the price is $7 or less and the FDA accepts REGAL alone for filing; or
- the FDA sets a PDUFA date (likely about Q3 2027, on BLA acceptance), then as an event bet
  (0.5% cap, Rs 2.08 L at the 18 Nov total, portfolio/targets.md "Event bets").
Key risk: the FDA asks for a second trial (REGAL was one open-label trial, 126 patients, p=0.035).
On the [event calendar](calendar.md) as "BLA filing 1H 2027".

## Sources (all accessed 18 Nov 2026)

- [P] yfinance 1.8.0, ticker SLS and INR=X, daily history 2020-01-01 to 2026-11-17 and .info
  (market cap, short interest dated 30 Oct 2026), pulled 18 Nov 2026 01:40-02:10 IST; final 17 Nov close re-pulled 02:34 IST; 17 Nov open, low and volume from finance-research's later pull (research/stocks/SLS.md, 18 Nov 2026).
- [S1] clinicaltrials.gov NCT04229979, record last updated 1 Oct 2025:
  https://clinicaltrials.gov/study/NCT04229979
- [S2] SELLAS PR 10 Dec 2024, 60 events, interim triggered:
  https://ir.sellaslifesciences.com/news/News-Details/2024/SELLAS-Life-Sciences-Triggers-Interim-Analysis-in-Phase-3-REGAL-Trial-of-GPS-in-Acute-Myeloid-Leukemia/default.aspx
- [S3] 8-K 23 Jan 2025, EX-99.1, IDMC interim result:
  https://www.sec.gov/Archives/edgar/data/1390478/000110465925005648/tm254291d1_ex99-1.htm
- [S4] 8-K 12 Aug 2025, EX-99.1 (Q2 2025; IDMC 7 Aug 2025; final "by year-end"):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047825000017/sls-202508128xkexhibit991.htm
- [S5] 8-K 12 Nov 2025, EX-99.1 (Q3 2025):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047825000021/sls-202511128xkexhibit991.htm
- [S6] 8-K 12 May 2026, EX-99.1 (Q1 2026; 78 events; ATM):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047826000009/sls-202605128xkexhibit991.htm
- [S7] 8-K 11 Aug 2026, EX-99.1 (Q2 2026):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047826000013/sls-202608118xkexhibit991.htm
- [S8] SELLAS PR 28 Oct 2026, 80th event reached:
  https://ir.sellaslifesciences.com/news/News-Details/2026/SELLAS-Life-Sciences-Reaches-80th-Event-in-Phase-3-REGAL-Trial-of-Galinpepimut-S-GPS-in-Acute-Myeloid-Leukemia/default.aspx
- [S9] 8-K 12 Nov 2026, EX-99.1 (Q3 2026; topline "this month"):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047826000021/sls-202611128xkexhibit991.htm
- [S10] 10-Q for Q3 2026, filed 12 Nov 2026 (cash, losses, ATM, warrants, shares, "November 2026"):
  https://www.sec.gov/Archives/edgar/data/1390478/000139047826000020/sls-20260930.htm
- [S11] 8-K 17 Nov 2026, EX-99.1, REGAL topline:
  https://www.sec.gov/Archives/edgar/data/1390478/000110465926128825/tm2629947d1_ex99-1.htm
- [S12] 8-K 27 Jul 2026 (3D Medicines arbitration; cash $138.3 M at 30 Jun 2026):
  https://www.sec.gov/Archives/edgar/data/1390478/000110465926087110/tm2621415d1_8k.htm
- [S13] SELLAS PR 29 Dec 2025, 72 events as of 26 Dec 2025:
  https://ir.sellaslifesciences.com/news/News-Details/2025/SELLAS-Life-Sciences-Provides-Update-on-Pivotal-Phase-3-REGAL-Trial-of-Galinpepimut-S-GPS-in-Acute-Myeloid-Leukemia-AML/
- [S14] SEC XBRL dei:EntityCommonStockSharesOutstanding, CIK 1390478:
  https://data.sec.gov/api/xbrl/companyconcept/CIK0001390478/dei/EntityCommonStockSharesOutstanding.json
  Warrant-funded cash: 8-Ks 8 Jan 2026, 11 Mar 2026, 2 Jun 2026 (EDGAR filing index, CIK 1390478).
- [S15] BIO, Informa Pharma Intelligence, QLS Advisors, "Clinical Development Success Rates and
  Contributing Factors 2011-2020", Feb 2021:
  https://www.bio.org/clinical-development-success-rates-and-contributing-factors-2011-2020
- [S17] Preliminary 424B5, 17 Nov 2026 ($150 M underwritten offering, $22.5 M option, separate $150 M ATM, 60-day lock-up):
  https://www.sec.gov/Archives/edgar/data/1390478/000110465926129063/tm2629996d1_424b5.htm
- [S16] FDA PDUFA goals (PDUFA VII commitment letter, FY2023-2027): new BLA review goal 10 months
  (standard) / 6 months (priority) from the 60-day filing date:
  https://www.fda.gov/media/151712/download
- News check: wallstreetobserver.com, "SELLAS REGAL Trial Meets Survival Goal; SLS Stock Rises 165%",
  17 Nov 2026 (intraday figures only).
