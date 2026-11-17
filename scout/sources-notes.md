# Source notes

## Summary
- Approved for news scans (2026-11-15): NSE announcement RSS feeds and Google / Bing News RSS; not TradingView.
- NSE feeds hold only about a day of items: poll at least daily; the NSE insider-trading feed is stale.
- Blocked from scripts: NSE and BSE APIs (403); Google News link decoding hits 429 after about 3 calls.
- Yahoo ratios need checks (P/E without FX, wrong EPS on some Japan and HK lines); screener.in and
  stockanalysis.com are for viewing only, no scripts. Open discrepancies for owners: numbered below.

## About these notes
Written by `finance-scout`. New, failed and changed sources, scan coverage and discrepancies found.
`research/sources.md` (finance-research) stays the scored list; lines here are for finance-research
to fold in.

## 2026-11-15 startup scan

### Sources that worked
| Source | Used for | Result |
|---|---|---|
| RBI press releases list, `rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx` (web_fetch) | Latest RBI releases | Works; listed 6-13 Nov 2026 |
| RBI drafts page, `rbi.org.in/Scripts/DraftNotificationsGuildelines.aspx` (note the RBI spelling) | Draft rules (LRS sub-limit check) | Works; newest draft 2026-11-05 |
| RBI home page, `rbi.org.in` | Policy rates, last T-bill cut-offs | Works, but the table labels are lost in text (values only; the repo row was missing). Use the MPC press release for rates |
| RBI MPC statement, `rbi.org.in/scripts/FS_PressRelease.aspx?prid=63742` | Repo 5.50% (2026-10-07) | Read through the web_search index (crawled 2026-11-11), not fetched directly |
| SEBI circulars list, `sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=1&ssid=7&smid=0` | New SEBI circulars | Works (titles and dates); score 5 for listings |
| SEC EDGAR submissions API and Archives (User-Agent with name and email) | Holdings 8-K/424B7/425 text; Anthropic S-1/A | Works; `browse-edgar?company=...&output=atom` finds CIKs by name (many SPVs share a name; check `tickers` in submissions) |
| Microsoft Source, `news.microsoft.com/source` | MSFT dividend | Works (via search index) |
| NSE circular PDFs, `nsearchives.nseindia.com/content/circulars/*.pdf`; NoticeBlue copy of NSE circulars | Trading holidays | Works through search index; `nseindia.com/api/*` returned 403 even with a home-page cookie |
| Google News RSS + batchexecute decode | Find dated news, get the article URL | Search works; decoding the article link hits HTTP 429 after a few calls. Space calls out (5 s+) |
| web_search tool | IPO pages, FD round-ups, primary pages | Works well for dated pages; check every snippet's date |
| Livemint, Economic Times, CNBC TV18, Business Standard IPO pages, Moneycontrol news | LRS report, FD rates, IPO terms | Readable; secondary |
| Kotak Neo IPO pages | IPO lot, dates | Readable, undated, secondary |
| Sirius Investors IPO calendar | US IPO calendar | Readable; secondary, unknown method; check against EDGAR |

### Sources that failed
- Google News article links: plain web_fetch returns the Google page, not the article; decode needed.
- NSE API (`www.nseindia.com/api/ipo-current-issue`, home page): 403 from script.
- The Hindu LRS explainer (2026-11-12): not read (decode rate-limited); headline only.

### Scan coverage (2026-11-15)
| Area | Done | Not done / gaps |
|---|---|---|
| India mainboard IPOs | Crystal Crop (18-20 Nov), Mahanadi Coalfields (from 19 Nov) | Full list for the week; exchange RHPs not opened; price band for MCL not found |
| India SME IPOs | SEBI 2026-10-14 proposal status (no final decision found) | Current SME issues not listed (no working source; Watrana Rentals seen as a headline only, type not checked) |
| US IPOs | Anthropic (ANT) S-1/A and FWPs on EDGAR; calendar for the week of 16 Nov | Price range and allocation access at IBKR for Indian residents |
| RBI / LRS | Repo 5.50%; no LRS draft on RBI pages; reported Rs 50 lakh sub-limit (secondary) | RBI text of any LRS change; LRS FAQ re-read; next MPC date |
| SEBI | Circulars to 2026-11-11 (titles) | Circular bodies; SEBI board meeting outcomes |
| Tax (Finance Act / CBDT) | Relied on `tax/investment-types.md` (2026-11-15) | No new CBDT/Finance Act scan; Rule 115 successor still unverified (STATUS) |
| IBKR product changes | Gap fill: press releases 1 Oct - 15 Nov (no pricing change; AI trading, ETH staking) | Fee-schedule change log (none published) |
| Rates | Repo (RBI), FD round-ups (secondary), T-bill/G-sec/SDL from research (RBI, 9-13 Nov) | Bank pages not opened; US T-bill yields not fetched; small-savings Jan-Mar 2027 rate not checked |
| Holdings events | From `research/themes/holdings-events-2026-11.md`; spot-checked NVDA, SHLS, IONQ, VRT on EDGAR, MSFT on Microsoft Source, NSE holiday on the NSE circular | CEG figures and ex-date, SCLX 10-Q timing, MSCI/FTSE changes, weekly moves: research-reported only; SHLS-Array close and vote dates not found |
| Gold/silver FoF pause | From research (no resume notice to 2026-11-15) | AMC notices not opened |

## Discrepancies for finance-main (and owners)
1. Stale denominator in research: mostly fixed. The first versions of `research/themes/silver-gold.md`
   and `research/themes/mutual-fund-overlap.md` sized the portfolio with about $15k of US stock; both
   were restated on the Rs 2,23,19,002 total on 2026-11-15 (02:40 IST): metals 3.7% of
   the total (8,29,676 / 2,23,19,002), 31.6% of AngelOne only, Rs 5 L cut withdrawn. One stale line
   remains: `mutual-fund-overlap.md` s1 Notes (PPFAS foreign stocks "overlaps your ~$15k US stocks";
   US accounts are $209,436). Owner: finance-research. `STATUS.md` still lists the issue as open.
2. Metals unrealised loss: research now uses -Rs 81,600 (13 Nov) and explains the earlier -Rs 64,000
   (8 Nov). Resolved; `STATUS.md` still lists it as open.
2a. `tax/angelone-metals-and-mf-exits.md` was briefly deleted in the working tree (about 02:45 IST)
   and is now rewritten but uncommitted (seen about 02:50 IST): it now covers research v2 and has new
   section numbers (whole-year picture s6, order s7, data s9). Research and `STATUS.md` cite the old
   section numbers (e.g. "s6" for the order). Owner: finance-tax / finance-main on commit.
3. QCOM Indian cost per share: $141.86 (method A, proposed, used by the repository since 2026-11-15)
   vs $143.91 (earlier snapshot, first in, first out) vs $133.55 (IBKR, US basis). The method is
   explained; validation still needs a CA and IBKR lot reports. Gain figures also differ by FX: Rs 39.6 L
   (method A, sale FX 95.15, `tax/investment-types.md` s5) vs Rs 34.8 L
   (`research/themes/employer-stock-concentration.md`, FX 94.03, FIFO lots).
4. US estate figures: $209,436 is the US-account total; US-situs is $207,935-209,436 depending on
   broker cash ($795 IBKR + $706 INDmoney); `tax/investment-types.md` s4 counts only QCOM + MSFT
   (about $192,500). Different scope, not an error.
5. Direct US T-bills: `research/themes/us-estate-tax.md` lists them as a conditional way to hold idle
   USD outside the US estate, while `research/themes/ibkr-global.md` s3.3 marks direct US debt LRS GREY
   and `tax/investment-types.md` flags possible always-short-term tax. The scout treats them as blocked
   until both are answered.
6. Crystal Crop IPO minimum: Rs 14,245 (Business Standard, floor price) vs Rs 14,960 (Kotak Neo, cap
   price); issue size Rs 455.72 crore vs Rs 455.49 crore.
7. NVDA results date: NVIDIA 2026-11-17 (US) vs yfinance 2026-11-18 (from [HE]; the scout did not
   re-check).
8. RBI home page policy-rate table loses its labels in text form and omits the repo row; values match
   the 2026-10-07 MPC release (SDF 5.25%, MSF/Bank Rate 5.75%).

## For finance-research (sources)
- Add: SEBI circulars list URL above (score 5); RBI drafts page (score 5); EDGAR `browse-edgar` atom
  name search (score 4, many name clashes).
- Lower: Google News RSS decode is rate-limited (429) after about 3 calls; keep RSS for search only.
- NSE API still 403 from script with a home-page cookie (same as `research/sources.md`).

## 2026-11-15 stock screens
- NEW, works: NSE archive `archives.nseindia.com/content/indices/ind_nifty500list.csv` (browser User-Agent), Nifty 500 list (501 rows incl. placeholder DUMMYHEG).
- NEW, works: `indexes.nikkei.co.jp/en/nkave/index/component?idx=nk225` with pandas.read_html: all 225 Nikkei members with codes (score 5).
- NEW, works: Wikipedia index lists (S&P 500, Euro Stoxx 50, FTSE 100, SMI, Hang Seng, STI, S&P/ASX 50) via read_html; may lag index changes; SMI page lists Roche as ROP (Yahoo ROP.SW; ROG.SW returns 404) (score 3).
- FAILED: Wikipedia Nasdaq-100 page: no constituent table found by read_html.
- screener.in `/company/<NSE symbol>/consolidated/`: consolidated P/E, ROE (last full year), ROCE. RULE (research/sources.md, terms checked 2026-11-15): viewing only - single, light web_fetch checks, one stock at a time; no curl/requests, no bulk scraping. The 2026-11-15 screen fetched 3 pages by script; that script is disabled.
- stockanalysis.com statistics pages (`/stocks/<t>/statistics/`, `/quote/<lon|epa|bme|tyo|hkg|...>/<code>/statistics/`): P/E, EV/EBITDA, ROE, margins, D/E as text (score 3); 404 for WuXi AppTec 2359 HK. Its P/E repeats Yahoo's no-FX error for European/UK USD reporters (Shell 8.60, Rio 11.32, TTE 9.24), so it is not a second source for those P/Es. RULE (research/sources.md, terms checked 2026-11-15): AI agents that follow robots.txt (web_fetch) are allowed; scripts are banned - no curl, requests or bulk loops. The 2026-11-15 screen fetched about 18 pages by script; that script is disabled and its cache deleted.
- tradingview.com: RULE (research/sources.md, terms checked 2026-11-15): terms forbid any automated access; never fetch it. Use company IR, LSE RNS, PR Newswire or Business Wire instead. Not used by the scout screens.
- Yahoo (yfinance 1.8.0) problems: P/E without FX on European/UK lines of USD reporters (true P/E Shell about 11.4 vs Yahoo 8.65, Rio about 15 vs 11.45, TTE about 10.5 vs 9.53; skill-session vs filings 2026-11-15, skill market-data commit 027ae1f); MKS.L EPS in pence; Kioxia 285A.T EPS wrong, cause unknown (its 3:1 split of 2026-09-29 IS in Yahoo prices); sharesOutstanding can count one class/listing only (WuXi H, Rio, Shell): use all classes; 1,562 info calls at about 50/min (two processes about 100/min) with no 429.
- Yahoo EPS (yfinance 1.8.0, 2026-11-15): for HK-listed mainland companies trailingEps can be in CNY while the price is HKD (2359: Yahoo P/E 18.9 vs company 17.8); for Japanese 8309 and 9766 Yahoo EPS is wrong (193.84 vs 142.76; 1,322 vs 979.42) - check filings (TDnet/HKEX, news/<SYM>.md).

## 2026-11-15 gap fill (scout-gaps, 09:00-10:00 IST)
Fills the "Not done" cells above for IBKR product changes, India SME IPOs, US T-bill yields,
small-savings rates and the SHLS-Array close date. Feed entries dated 2026-11-15, 2026-11-13,
2026-11-12, 2026-10-21, 2026-10-15 and 2026-09-30.
- NEW, works: TreasuryDirect auction API `treasurydirect.gov/TA_WS/securities/auctioned?format=json&type=Bill&days=21` (no key; fields highRate, investmentRate, bidToCoverRatio, results PDF name). Score 5.
- FAILED: fiscaldata `api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query` returned "Not Found" (2026-11-15); use TreasuryDirect above.
- Works: IBKR press releases `interactivebrokers.com/en/general/about/press-releases.php` and `mediaRelations/<m-d-yy>.php` (web_fetch). Score 5 for announcements; IBKR publishes no fee-schedule change log there, so pricing changes need a diff of the pricing pages.
- Works: EDGAR submissions for SHLS (CIK 1831651) and ARRY (CIK 1820721); IBKR 8-K EX-99.1 (CIK 1381197).
- FAILED: `www.nseindia.com` home page 403 from curl (browser User-Agent) on 2026-11-15, so no cookie and every `api/*` call 301; `api.bseindia.com/BseIndiaAPI/api/GetPIPO` 403 (Akamai "Access Denied").
- NEW, secondary: Chittorgarh IPO pages and SME calendar (`chittorgarh.com/ipo/<name>/<id>/`), dated, lot and minimum per category (score 3); Finaccle SME list `finaccle.in/ipo-tracker/sme-ipo` (compiled from Chittorgarh, publish time shown; score 3); ipomarket.in `/sme/upcoming` (score 2: shows 1-lot value, not the 2-lot individual minimum); ipoplatform.com (score 2, page date stale).
- Note: Chittorgarh's schedule report `/report/ipo-schedule-and-fund-planning-calendar/132/` shows "Total Records: 0" to web_fetch (filled by script); the search-index copy had the data.
- FAILED: India Post savings page (`indiapost.gov.in/Financial/Pages/Content/Post-Office-Saving-Schemes.aspx`) 404; `dea.gov.in/budgetdivision/notifications` 404. Small-savings OM read only as a copy (govtstaff.com PDF, through the search index; no local PDF text tool, pypdf not installable from the configured index).
- Secondary, works: ET small-savings article (2026-10-01) with the India Post rate table.

### Discrepancies (gap fill)
9. Watrana Rentals SME IPO minimum: ipomarket.in "Lot Value Rs 1,47,000" (1 lot) vs Chittorgarh / IPO Platform individual minimum 2 lots = Rs 2,94,000 at the cap.
10. Last small-savings rate change: ET (2026-10-01) says the December 2024 review; Mint (2025-12-31) says Q4 2023-24. Current rates agree in both.

## Approved sources (approved 2026-11-15)
Approved by the user via finance-main, 2026-11-15: NSE announcement RSS feeds and Google / Bing News
RSS feeds (details: `research/themes/tools/libraries-and-news.md`, News table and Sources). TradingView
is NOT adopted (its terms forbid automated access; `research/themes/tools/web-tools.md`).

| Feed | URL | Limits / notes | Test 2026-11-15 13:40 IST |
|---|---|---|---|
| NSE all announcements | `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml` | Browser User-Agent; ttl 5 min; latest items only (about one day), so poll at least daily | Works: HTTP 200, 82 items, newest 2026-11-15 13:33 IST |
| NSE financial results | `.../content/RSS/Financial_Results.xml` | as above | Works but thin: 3 items, newest 2026-11-03 10:29 (stale for results season; use the main feed) |
| NSE board meetings | `.../content/RSS/Board_Meetings.xml` | as above | Works: 1 item, newest 2026-11-15 00:00 |
| NSE corporate actions | `.../content/RSS/Corporate_action.xml` | as above | Works: 39 items, newest 2026-11-13 06:11 (last trading day) |
| NSE insider trading | `.../content/RSS/Insider_Trading.xml` | as above | STALE: 20 items, newest 2026-05-02 16:46 (old PIT feed; insider data moved to XBRL `api/corporates-pit-gg`, skill market-data). Do not rely on it |
| Google News RSS | `https://news.google.com/rss/search?q=<query>+when:7d&hl=en-IN&gl=IN&ceid=IN:en` | Search is fine; decoding article links (batchexecute) hits 429 after about 3 calls: space 5 s+ | Works: 100 items for "Qualcomm" (7 days), newest 2026-11-15 07:20 UTC |
| Bing News RSS | `https://www.bing.com/news/search?format=rss&q=<query>` | Direct article links (no decoding); backup when Google 429s | Works: 12 items for "Qualcomm", newest 2026-11-14 23:30 UTC |

NSE feed dates are day-first strings (`15-Nov-2026 13:33:11`) in some feeds and RFC 822 in others; parse
each with its own format (see skill market-data on day/month swaps).

### Weekly scan method (news and holdings-events steps)
1. First stop, India: fetch the NSE main announcements feed (and the corporate-actions and board-meetings
   feeds); match items against AngelOne holdings and watchlist India names (`trading/watchlist.md`);
   follow each match to the NSE filing PDF it links (primary = verified). Because the feeds hold only
   recent items, a weekly scan sees only the last day or so: for the rest of the week use the NSE
   filing pages / company IR or ask finance-news, which polls daily.
2. First stop, US and global: Google News RSS per holding and watchlist name (`<name> when:7d`), then
   Bing News RSS for the same query to get direct links when Google decoding 429s. News items are
   secondary; confirm each event in the primary filing (EDGAR 8-K/10-Q/424B, exchange, company release)
   before labelling it verified.
3. Then the existing primary sources (EDGAR submissions API, RBI, SEBI, TreasuryDirect) for anything
   the feeds point to or miss. Record each new or failed feed result here.

## 2026-11-15 - NSE bhavcopy for listed REITs (Bagmane)
- yfinance has no data for BAGMANE.NS (listed 2026-05-14). Price source used by finance-research
  (`research/themes/opp-real-assets/reits.md`): the NSE daily price file (bhavcopy) on nsearchives.nseindia.com;
  fallback yfinance BAGMANE.BO (BSE line). NAV, yield and occupancy: the Q2 investor presentation (2026-11-03).
- Worked 2026-11-15, one plain fetch with a browser user agent:
  `https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_DDMMYYYY.csv` (CSV, no zip). REITs are
  series RR. 13 Nov 2026: BAGMANE close Rs 106.18, MINDSPACE Rs 497.97 (matches yfinance).
- Small gap: reits.md shows Bagmane Rs 106.23 vs bhavcopy close Rs 106.18 (LAST_PRICE 106.20); likely a
  different price field or the BSE line, not verified.

## 2026-11-15 - Daiichi Sankyo (4568) P/E: Yahoo and stockanalysis use pre-correction profit
- Data error: Daiichi Sankyo corrected its FY2025 accounts in July 2026. Yahoo `trailingEps` (153.05) and its
  quarterly net income (Q4 FY3/26 JPY 42.4 bn vs corrected 62.3 bn), and the stockanalysis EPS, still use the
  pre-correction quarter, so they show P/E 18.5-18.7. True trailing P/E on corrected company profit: 17.4
  (TTM EPS about 164; `research/stocks/4568.md` section on valuation, finance-research 2026-11-15).
- Rule: for any company with restated accounts, recompute P/E from the company filing; do not quote Yahoo or
  stockanalysis EPS.
- Also from the same deep dives: scout weekly correlation with QCOM+MSFT (AZN -0.30) was not reproduced by
  research (-0.12 weekly, -0.02 monthly); different basis (scout: 68/32 basket, 53 weeks, local-currency
  closes); both low.
