# finance

Personal portfolio tracking and trading notes. Rules: `AGENTS.md`. Where things are: `MAP.md`.
Current state: `STATUS.md`.

## Set up on a new Mac
1. Install Google Drive for desktop and sign in; `Finance/` appears under
   `~/Library/CloudStorage/GoogleDrive-*/My Drive/`. Allow the terminal to read it when macOS asks.
2. `git clone git@github.com:aroraakarshan/finance.git ~/Developers/finance`
3. `cd ~/Developers/finance && git config user.name "Akarshan Arora" && git config user.email akarshanarora@gmail.com`
4. `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
5. In zellij open the finance workspace, then start Copilot there:
   `zw finance ~/Developers/finance`, then `cns finance-main` (new; resumes if the session exists).
6. In the `finance-main` session say "start the team"; it starts the other sessions from `roles/`
   with `copilot-tab <name>`, each in its tab of the `finance` workspace (`coordinator`,
   `discover`, `analyse`, `decide`; roster `.github/sessions.tsv`). If that fails it gives you
   the task and asks you to run `cns <name>` yourself.

## Read the notes
1. `git pull && .venv/bin/pip install -q -r requirements.txt`
2. `.venv/bin/python -m scripts.site --serve` (builds the website into
   `~/.local/share/finance-site` and starts a local server if none is running)
3. Open http://127.0.0.1:8765. The "theme" link in the header switches between `reader` (large
   serif text) and `list` (dense, Hacker News-like); the browser remembers the choice.

## Do it yourself (no agent needed)
One command updates every figure and the day's market data (`news/market/data/<date>.md`):
`.venv/bin/python -m scripts.update`. It works offline too (last cached prices); `--no-market` skips
the market data. Google Drive `Finance/Guides/<broker>-download-guide.pdf` shows each download
step by step.

### One-time setup on a Mac
| Step | What |
|---|---|
| 1 | Install Google Drive for desktop and sign in. In Finder right-click `My Drive/Finance` -> "Available offline" (needed to update offline) |
| 2 | `git clone git@github.com:aroraakarshan/finance.git ~/Developers/finance && cd ~/Developers/finance` |
| 3 | `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` |
| 4 | Run `.venv/bin/python -m scripts.update` once from Terminal; allow Terminal to read Google Drive when macOS asks |

### Every month
1. Download each export by hand and save it in Drive under the exact name (the date is the download date, `YYYY-MM-DD`):

| Account | Where (guide in `Finance/Guides/`) | Drive folder (under `Finance/`) | File name |
|---|---|---|---|
| AngelOne | angelone.in, reports page: combined holdings (Excel, password = PAN in capitals) and mutual fund holdings (`angelone-download-guide.pdf`) | `Investments/Stocks/AngelOne` | `AngelOne_CombinedHolding_<date>.xlsx`, `AngelOne_MF_Holdings_<date>.xlsx` |
| INDmoney | INDmoney app or indmoney.com, US stocks: holdings report and trade history since inception (`indmoney-download-guide.pdf`) | `Investments/Stocks/INDmoney` | `INDmoney_US_Holdings_<date>.xls`, `INDmoney_US_Trades_SinceInception_to_<date>.xls` |
| INDmoney cash | INDmoney app dashboard, US wallet balance | - | edit `INDMONEY_CASH_USD` and `INDMONEY_CASH_DATE` in `scripts/value.py` (or pass `--indmoney-cash` to `scripts.value`) |
| IBKR | Portal, Performance & Reports: Activity Statement (CSV) for the current year to date; Trade Confirmation report (PDF) from 2025-04-01 to today (`ibkr-download-guide.pdf`) | `Tax/FY<yyyy-yy>/IBKR`; `Investments/Stocks/IBKR` | `IBKR_<account>_ActivityStatement_CY<yyyy>_to_<date>.csv`; `IBKR_<account>_TradeConfirmations_2025-04-01_to_<date>.pdf` |
| Fidelity (MSFT) | NetBenefits: new statements and trade confirmations (`fidelity-download-guide.pdf`); Microsoft stock award portal export after a vest | `Tax/FY<yyyy-yy>/Fidelity`; `Salary/Microsoft/Stock` | `Fidelity_<date>_Statements_<title>.pdf`, `Fidelity_<date>_Tradeconfirmations_TradeConfirmation.pdf`; `StockExport_<date>.xlsx` |
| ETrade | nothing (account empty since Dec 2025; `etrade-download-guide.pdf`) | - | - |
| HDFC | NetBanking: savings statement in "Delimited" format; Deposits: FD summary (PDF) | `Banking/HDFC/Savings`; `Banking/HDFC/FD` | `HDFC_Savings_<last4>_<from>_to_<to>.csv`; `HDFC_FD_Summary_<date>.pdf` |
| Physical gold | only after a purchase: the seller's invoice PDF | `Investments/Gold` | `<date>_<Seller>_Invoice.pdf` (Seller `Varnika`, `TanishqDubai` or `BhimaGold`; another seller needs a reader in `scripts/brokers/gold.py`) |

2. `cd ~/Developers/finance && .venv/bin/python -m scripts.update` (type the AngelOne password when asked, or Enter to skip).
3. Read the result: http://127.0.0.1:8765 (Portfolio page; if it does not open, run `.venv/bin/python -m scripts.site --serve`), or `Finance/Portfolio/portfolio.xlsx` in Google Drive (sheets Summary, Accounts, Holdings, FDs, Cash, Gold, History).

### Every day
`.venv/bin/python -m scripts.mark` (or the full `scripts.update`), then read `trading/alerts.md`: stop or
target hit, a move over 7%, news score -2, results within 5 trading days, allocation outside its band
(`portfolio/targets.md`), FD maturity within 30 days. Your own notes per holding (label, why you hold it,
when to sell, stop, target, review date) go in `trading/positions.csv`; the script never overwrites them.
Decisions: `portfolio/decisions.md`.

### Offline
| What | How |
|---|---|
| Prices, USD/INR, gold rate | Every fetch is saved in `~/.local/share/finance-cache/prices.json` (USD/INR: the FBIL reference rate in `fbil-usdinr.json`). `--offline`, or no network, uses those and prints their dates |
| Drive files | Read from the local Drive folder; they must be "Available offline" (step 1) |
| Website | `python -m scripts.site --serve` needs no network |

### Commands (`.venv/bin/python -m <command>`, from the repository folder)
| Command | Does |
|---|---|
| `scripts.update [--offline] [--no-site]` | Everything below in order; writes `portfolio/summary.md`, `portfolio/history/<date>.md`, the spreadsheet, the daily marks and alerts, and the website; prints total vs last snapshot, change per account, files used, warnings, alerts |
| `scripts.mark [--offline]` | Daily mark of every position: `trading/marks/<date>.csv` and `README.md`, `trading/alerts.md` (actions today), current allocation in `portfolio/targets.md`; exit code 1 when an action is needed |
| `scripts.value [--offline]` | Value of every account and the total in INR (AngelOne only with `ANGELONE_PASSWORD` set) |
| `scripts.pnl indmoney` (or `ibkr`, `etrade`) | Realised profit/loss per stock |
| `scripts.brokers.<name>` | One account's holdings (`angelone`, `indmoney`, `ibkr`, `etrade`, `fidelity`, `hdfc`, `gold`) |
| `scripts.drive_index` | List of the Drive documents -> `portfolio/drive-index.md` |
| `scripts.site [--serve]` | Builds the notes website; `--serve` starts http://127.0.0.1:8765 |

### Troubleshooting
| Problem | Fix |
|---|---|
| `NO MATCH <folder>/<pattern>` in the output | The file is missing or named differently: rename it to the pattern in the table above |
| `Operation not permitted` reading a Drive file | Drive has not downloaded it yet: open it once in Finder or mark `Finance` "Available offline" |
| `AngelOne skipped` | No password given: run in Terminal and type it, or `ANGELONE_PASSWORD=... .venv/bin/python -m scripts.update`; AngelOne keeps its last figure until then |
| `AngelOne: could not open` | Wrong password (PAN in capitals) |
| `cached prices used` | No network: prices are from the date shown; run again online |
| Website does not open | `.venv/bin/python -m scripts.site --serve`, then reload http://127.0.0.1:8765 |
