# Map

## Purpose
Personal portfolio tracking: reads broker exports from Google Drive, computes holdings and
profit/loss, and keeps research, a trade journal and tax notes.

## Layout
| Path | Holds | Written by |
|---|---|---|
| `AGENTS.md` | Rules: sessions, work model, data handling, trading rules, two-Mac routine | `finance` |
| `STATUS.md` | Handoff: done, in progress, next, open discrepancies | `finance` |
| `roles/<session>.md` | Each session's role, what it owns, what it reads at start | `finance-main` |
| `.github/sessions.tsv` | Session roster for `copilot-tab`: workspace `finance`, one row per session (tab, what it owns) | `finance-main` |
| `scripts/common.py` | `finance_dir` (Drive folder, `FINANCE_DATA` overrides), `latest` (newest export), `read_table` (find header row under banners), `decrypt` (protected xlsx), `tax_files(broker, pattern)` (`Tax/FY*/<broker>/`), `pdf_text` (cached PDF text), `num`, `every` (all files of a pattern), `LOOKUPS` (every pattern looked up and the file it found, for `update.py`), `cached_prices`/`cache_prices` (`~/.local/share/finance-cache/prices.json`: symbol -> price, date, prev, prev_date), `rs` (Rs with Indian digit grouping) | `finance` |
| `scripts/brokers/angelone.py` | `equity(password)`, `mutual_funds()`, `file_date(EQUITY_FILE or MF_FILE)`, `open_holdings()` (stocks and ETFs from the newest TaxPnL 'Open Holdings' table, no password) | `finance` |
| `scripts/brokers/indmoney.py` | `holdings()`, `trades()`, `RENAMES` (SAVA -> FLNA), `SPLITS` (CERO, HSDT, SCLX reverse splits; CRWD, KLAC) | `finance` |
| `scripts/brokers/ibkr.py` | `holdings()` (open positions of the newest Activity Statement, IBKR cost basis and market value), `cash()`, `transfers()`, `broker_realised()` (IBKR's own P/L), `trades()` (Trade Confirmation PDF plus transfers in as BUY `TRANSFER_IN` at the ETrade lot cost) | `finance` |
| `scripts/brokers/etrade.py` | `acquisitions()` (RSU/ESPP lots), `sales()`, `statements()`, `holdings()`, `transfers()` (lots moved to IBKR with cost), `trades()`, `checks()` | `finance` |
| `scripts/brokers/fidelity.py` | `vests()`, `purchases()`, `statements()`, `holdings()`, `trades()` (buys only so far), `checks()` | `finance` |
| `scripts/brokers/hdfc.py` | `fds()` (newest FD summary: FD last 4, principal, rate, start, maturity, maturity amount; compounding found from the maturity amount, interest accrued to today, value), `savings_balance()` (closing balance and date of the newest savings CSV) | `finance` |
| `scripts/pnl.py` | `realised(trades)`: average-cost P&L, split detection, open positions | `finance` |
| `scripts/brokers/gold.py` | Physical gold: `items()` (one row per invoice line: date, seller, item, purity, net grams, gold value, making, stones/other, discount, GST/VAT, paid in INR; AED at `AED_INR`), `invoices()`, `rates(offline)` (IBJA PM rate per gram 24K/22K/18K, fallback international gold x premium, then cache), `valued()` | `finance` |
| `scripts/value.py` | `snapshot(offline, indmoney_cash, angelone_password, carry)`: every account (AngelOne with password, US holdings at the last yfinance close, cash, HDFC savings, FDs with accrued interest, physical gold, `portfolio/manual-assets.csv` rows), USD/INR (`usdinr(day)`: FBIL reference rate of the valuation date or the business day before, from the RBI reference rate archive, else fbil.org.in (public data lags about a week), cached in `~/.local/share/finance-cache/fbil-usdinr.json`; else yfinance `INR=X` with a printed warning), totals in INR; `closes()` falls back to the price cache and caches the close before; `amfi()` (AMFI NAV file), `navs(codes)` (MF NAVs as `AMFI:<code>`, cached like `closes`) | `finance` |
| `scripts/update.py` | One-command update: broker readers, `pnl` (INDmoney, IBKR, ETrade), `value.snapshot`, `drive_index`, `portfolio/summary.md` + `portfolio/history/<date>.md`, `<Drive>/Finance/Portfolio/portfolio.xlsx` (Summary, Accounts, Holdings, FDs, Cash, Gold, History), `mark.run`, `scripts.market` (subprocess, TZ=UTC, `--offline` when offline -> `news/market/data/<date>.md`, git-ignored, not on the site; failure is a warning; `--no-market` skips), site; prints total vs last snapshot, files used, patterns with no match, warnings. AngelOne without password: figure carried from the last snapshot | `finance` |
| `scripts/mark.py` | Daily mark to market: `run(snapshot, offline)` syncs `trading/positions.csv` with the readers (hand columns kept), prices every position (yfinance US and `<SYMBOL>.NS`, AMFI NAVs, snapshot values for cash, FDs, gold), writes `trading/marks/<date>.csv`, `trading/marks/README.md`, `trading/alerts.md` and the generated section of `portfolio/targets.md`; exit code 1 when an alert needs action | `finance-main` |
| `scripts/drive_index.py` | Drive inventory from file names (type, broker, period, gaps; account numbers masked) -> `portfolio/drive-index.md` | `finance` |
| `scripts/market.py` | Daily market data as markdown (indices, volatility, breadth, flows, sentiment, rates/FX/commodities, sector heat, notable moves) with source and date per number; cache `~/.local/share/finance-cache/market/`; `TZ=UTC python -m scripts.market [--date] [--out] [--offline]`; run by `scripts.update` | `finance-news` |
| `scripts/site.py` | Notes website: every note in the repository root and the content folders -> static HTML in `~/.local/share/finance-site` (not in git), plus the reports in `~/.local/share/finance-reports`. Menu: Home (`portfolio/plan.md`: next steps, Sell / Buy / Keep cards, the plan in one picture; terms from `portfolio/glossary.md` explained on hover), Market (newest `news/market/<date>.md`, `scout/buy-list.md`, one line per `research/sectors/<sector>/`), Decisions (from `STATUS.md` Next and Needed from user, with the options and recommendation of the linked note), Portfolio (`portfolio/summary.md`), Library (all notes by folder, filter box; team files last). `--serve` starts http://127.0.0.1:8765 | `finance-main` |
| `site/page.html`, `site/style.css` | Page template (menu, theme switch, table sorting) and the two themes: `reader` (default) and `list` | `finance-main` |
| `portfolio/manual-assets.csv` | Hand-entered assets with no export (symbol, name, account, asset, value INR, as_of, source): EPF (passbook figure), Punjab Gramin Bank FDs and savings (user estimate until documents come). `value.manual()` adds each to the totals; `scripts.mark` adds each as a position | `finance-main` |
| `portfolio/summary.md` | Current snapshot across accounts (generated by `scripts.update`; do not edit) | `scripts.update` |
| `portfolio/targets.md` | Target allocation: hand table (class, counts = positions.csv `asset` values, target, band, fix in progress, source) and a section generated by `scripts.mark` (current per class and asset) | `finance-main` + `scripts.mark` |
| `portfolio/decisions.md` | Decision log: date, decision, why, source note, review date; STATUS.md links here | `finance-main` |
| `portfolio/details.md` | Hand-written notes of the 2026-11-15 snapshot (cost methods, INDmoney history, IBKR transfers, NXPI, AngelOne lists) | `finance-main` |
| `portfolio/history/<date>.md` | One snapshot per update (generated; a rerun the same day replaces it) | `scripts.update` |
| `portfolio/drive-index.md` | Generated inventory of the Drive `Finance/` documents (`scripts.drive_index`) | `finance` |
| `portfolio/accounts.md` | Account history (opened, moved, how shares came in) and what is in scope | `finance-main` |
| `portfolio/how-to/<topic>.md` | Step-by-step guides for the user (e.g. `fidelity-to-ibkr.md`: move vested MSFT shares by form, ESPP sale dollars by wire, payout instruction to IBKR) | `finance-main` |
| `portfolio/migration-indmoney-to-ibkr.md` | INDmoney -> IBKR transfer status (from Gmail) | `finance-main` |
| `research/watchlist.md`, `stocks/<SYMBOL>.md`, `themes/<topic>.md` | Research notes (`stocks/` = deep dives for `trading/watchlist.md`; `research/watchlist.md` is the older list) | `finance-research` |
| `research/sources.md` | Scored sources | `finance-research` |
| `research/briefs/<task>.txt` | Briefs for `finance-research`'s standing tasks (daily events, sector, sector ranking, stock deep dive): what each run does and writes | `finance-research` |
| `journal/trades.csv`, `reviews/<YYYY-MM>.md` | Trade log (paper and real) and monthly reviews | `finance-journal` |
| `journal/signals.md` | Which signals, strategies and sources worked (hit rate, average result) | `finance-journal` |
| `news/daily.md`, `news/daily/<YYYY-MM-DD>.md`, `news/<SYMBOL>.md` | Daily news index (summary, one row per day) and one file per day; per stock: dated news and filings, sentiment -2..+2 with sources, catalysts | `finance-news` |
| `trading/watchlist.md` | Shared watchlist: symbol, market, stage, next owner, date, links; each session moves only its own stage | all (own stage only) |
| `trading/positions.csv` | One row per holding in every account plus paper trades: symbol, name, market, account, label (core / satellite / trade / cash / gold), asset, ticker, qty, currency, cost_native, cost_inr, thesis, sell_if, stop, target, review, status (open / paper / closed), source. `scripts.mark` refreshes qty, cost, status and source; label, asset, thesis, sell_if, stop, target and review are hand-written | `finance-main` (hand columns) + `scripts.mark` |
| `trading/marks/<date>.csv`, `trading/marks/README.md`, `trading/alerts.md` | Daily marks (price, value, P&L, day change, distance to stop/target per position), their summary (day P&L, movers, near stop/target, by label) and the alerts (actions today, information, data notes) | `scripts.mark` |
| `trading/plans/<SYMBOL>.md`, `trading/backtests/` | Trade plans (entry, stop, target, size, exits, tax line); backtests: `index.md` (comparison), one folder per strategy (`<strategy>/index.md`, `results.md`, `trades.md`, `data.md`), `engine.py`; tearsheets in `~/.local/share/finance-reports/trading/backtests/reports/` (not in git; `FINANCE_REPORTS` overrides) | `finance-trader` |
| `tax/FY<yyyy-yy>/` | Tax notes and computed figures | `finance-tax` |
| `tax/migration-indmoney-to-ibkr.md` | Tax plan for the INDmoney -> IBKR transfer | `finance-tax` |
| `research/global/` | What an Indian resident can invest in worldwide: `README.md` (map), one note per country or asset class; `property/` (real estate notes, empty on 2026-11-15) | `finance-research` |
| `legal/` | `estate/` (`README.md` index: one row per account, nominee or beneficiary, gaps; topic notes: `india-rules.md`, `insurance.md`, `foreign-assets.md`, `sources.md`, `family-info-template.md`), `compliance/` (`README.md` index: status, top actions; topic notes: `fema-lrs.md` LRS use per FY and permitted holdings, `schedule-fa.md`, `property-abroad.md`, `poa-and-us-forms.md`, `sources.md`), `questions.md` (for an Indian lawyer/CA) | `finance-legal` |
| `scout/universe.md` | Every instrument the user can invest in: account, minimum, cost, LRS, status | `finance-scout` |
| `scout/feed.md`, `ideas.md`, `sources-notes.md` | Dated scan findings (newest first), ranked ideas, source notes | `finance-scout` |

All `trades()` functions return the same columns: `symbol, when, side, qty, price, amount, fee, order_type`.
`side` is `BUY`, `SELL` or `TRANSFER_OUT` (shares moved to another broker: `pnl.py` removes them at cost,
no P/L). A transfer in is a `BUY` with `order_type` `TRANSFER_IN` at the cost the shares left with.

## Data (Google Drive `Finance/`)
Inventory: `portfolio/drive-index.md` (per broker: document types, periods covered, gaps, newest
date). Refresh it with `python -m scripts.drive_index` after every download; read it instead of
listing Drive.

| Folder | Content |
|---|---|
| `Tax/FY<yyyy-yy>/<broker>` | Most documents: statements, confirmations, tax P&L, 1042-S, per Indian FY. Brokers: `ETrade` (FY2018-19 on, accounts ****7855 QCOM and ****8803 NXPI: account statements, RS release, ESPP and trade confirmations, 1042-S), `Fidelity` (statements, trade confirmations, transaction summary, 1042-S, year-end report), `IBKR` (`IBKR_[<account>_]ActivityStatement_<period>.csv/.pdf`, RealizedSummary), `INDmoney` (monthly `INDmoney_US_Statement_<yyyy-mm>.pdf`, tax reports, 1042-S), `Angel One` (TaxPnL, PnLSummary, Ledger, TradesCharges, MF transactions and capital gains, ELSS), `ClearTax` |
| `Tax/FY<yyyy-yy>/Income Tax Site`, `ITR`, `<employer>` | AIS, TIS, Form 26AS, challans; ITR forms, receipts, intimations, Form 67; Form 16 and tax computations |
| `Investments/Stocks/AngelOne` | `AngelOne_CombinedHolding_<date>.xlsx` (password: PAN in capitals), `AngelOne_MF_Holdings_<date>.xlsx` |
| `Investments/Stocks/INDmoney` | `INDmoney_US_Holdings_<date>.xls`, `INDmoney_US_Trades_SinceInception_to_<date>.xls` |
| `Investments/Stocks/IBKR` | `IBKR_<account>_TradeConfirmations_<from>_to_<to>.pdf` (cumulative) |
| `Investments/Stocks/ETrade` | `ETrade_<last4>_BenefitHistory_Expanded_<date>.xlsx`, `ETrade_<last4>_GainsLosses_TY<year>.xlsx`; the reader uses the PDFs in `Tax/FY*/ETrade` |
| `Investments/Stocks/Fidelity` | `Fidelity_ESPP_Activity_<year>.csv`; the reader uses `Tax/FY*/Fidelity` and `Salary/Microsoft/Stock/StockExport_<date>.xlsx` (RSU vests) |
| `Investments/Research/<date>` | Earlier research runs (counted only in the index) |
| `Salary/<employer>` | Payslips, EPF passbooks, `Microsoft/Stock/StockExport_<date>.xlsx` (counted only in the index) |
| `Banking/HDFC` | `Savings/HDFC_Savings_<last4>_<from>_to_<to>.csv/.pdf/.xls` and interest certificates; `FD/HDFC_FD_Summary_<date>.pdf`, FD interest certificates, TDS summary/report, Form 16A; card statements. Read by `hdfc.py` (savings CSV, FD summary) |
| `Investments/Gold` | `<date>_<Seller>_Invoice.pdf` (Varnika, TanishqDubai in AED, BhimaGold), read by `gold.py` |
| `Portfolio/portfolio.xlsx` | Spreadsheet written by `scripts.update` (overwritten each run; Drive keeps versions) |
| `Bills/` | Few or no files; counted only in the index |
| `Guides/` | How to download each export (made by skill `finance-downloads`) |

## Run
```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # once per Mac
.venv/bin/python -m scripts.brokers.angelone      # asks for the file password
.venv/bin/python -m scripts.brokers.indmoney
.venv/bin/python -m scripts.brokers.etrade        # QCOM/NXPI stock plans (empty since the Dec 2025 move to IBKR)
.venv/bin/python -m scripts.brokers.fidelity      # MSFT RSU and ESPP
.venv/bin/python -m scripts.brokers.ibkr
.venv/bin/python -m scripts.pnl indmoney          # or ibkr, etrade
.venv/bin/python -m scripts.brokers.hdfc          # HDFC FDs and savings balance
.venv/bin/python -m scripts.brokers.gold         # physical gold invoices and value at the IBJA rate
.venv/bin/python -m scripts.value                 # every account and total in INR (--offline: cached prices)
.venv/bin/python -m scripts.update                # all of it: totals, summary, history, Drive spreadsheet, marks and alerts, market data, site (--no-market, --no-site)
.venv/bin/python -m scripts.mark                  # daily marks and alerts only (--offline: cached prices); exit 1 = action needed
.venv/bin/python -m scripts.drive_index           # Drive inventory -> portfolio/drive-index.md; run after every download
.venv/bin/python -m scripts.site --serve          # notes website -> ~/.local/share/finance-site, http://127.0.0.1:8765
```
Each runs in a few seconds. Run from the repository root.

## Traps
- INDmoney holdings `Total Value ($)` is cost (quantity x average price), not market value (`indmoney.py`).
- Trade files do not show splits or ticker changes: `indmoney.SPLITS` restates orders before each split
  (KLAC 10:1, CRWD 4:1, reverse splits CERO, HSDT, SCLX); `indmoney.RENAMES` maps SAVA -> FLNA. `pnl.py`
  still treats an unexplained oversized sell as a split and reports it.
- IBKR shares moved in from ETrade (NXPI 13 on 2025-12-08, QCOM 759 + 2 on 2025-12-16/19) have no
  buy in the trade file; `ibkr.trades()` adds them at the ETrade lot cost (`etrade.transfers()`).
  Two cost methods: IBKR's own basis is the US basis sent by ETrade, ESPP at the price paid (NXPI
  $77.615, QCOM $133.55); the repository and Indian tax use market value at release or purchase,
  with each sell-to-cover matched to its own release (net shares per vest) and fractional sales
  taken from DRIP lots (NXPI $91.32, QCOM $141.86). So IBKR's realised P/L and `pnl ibkr` differ.
- `pnl etrade` lists QCOM and NXPI as "open in trades but not in holdings": `etrade.trades()`
  leaves out the transfers to IBKR (see `etrade.transfers()`); expected.
- ETrade statements start Oct 2019 (QCOM) and Nov 2019 (NXPI); older gaps are not chased
  (`portfolio/accounts.md`). The new platform rounds shares to 3 decimals (NXPI 0.0008 share).
- Fidelity has no statements for Jan-Jun 2025; the Aug 2026 statement shows cost "unknown".
- INDmoney SMNR came from a Scilex stock dividend (2026-06-15), not a trade; not in `pnl.py`.
- AngelOne `Time Technoplast` shows average price 0 for the 3 bonus shares; for Indian tax their cost is about Rs 260.45 each (s.94(8) bonus-stripping adds the disallowed Rs 781 loss), see `tax/FY2025-26/time-technoplast.md`.
- HDFC savings CSV narrations can hold unquoted commas (RTGS); `hdfc.py` splits rows by hand. The FD
  summary has no current value or compounding; `hdfc.py` takes quarterly compounding when it reproduces
  the maturity amount and adds the interest accrued to today (before TDS).
- Drive files never opened on this Mac can fail with "Operation not permitted" until read once
  (`head -c 4 <file>`) or made available offline.
- Gold invoices: stones are inside the price (Varnika, Tanishq rings), so the value counts the net gold
  weight only; the Dubai invoice is in AED (`gold.AED_INR`, invoice-date rate) and in another person's name.
- macOS asks the terminal for permission to read the Google Drive folder the first time.
- `scripts.mark` takes AngelOne stock and ETF quantities from the newest TaxPnL (no password), mutual fund units from the MF export, and prices both itself (`.NS` closes, AMFI NAVs); `scripts.update` still carries the AngelOne total from the last snapshot without the password, so the marked total and the summary total differ by that.
- AMFI gives only the latest NAV: a fund's day change appears from the second day it is cached.
