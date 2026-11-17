# Finance rules

Read `MAP.md` for where everything is.

## Sessions and who writes where
Each session writes only to its own folders and reads everything else.

| Session | Tab | Job | Writes to |
|---|---|---|---|
| `finance-main` | `coordinator` | Main: talks to the user, downloads statements (skill `finance-downloads`), updates the portfolio, starts and hands work to the others, commits | `portfolio/`, `scripts/`, `STATUS.md`, this file, `MAP.md`, `roles/` |
| `finance-research` | `analyse` | Stock and market research (skill `market-data`), scored sources | `research/` |
| `finance-journal` | `decide` | Logs paper and real trades, checks them against the trading rules, monthly reviews, scores which signals worked (starts now, paper trading) | `journal/` |
| `finance-tax` | `decide` | Capital gains, foreign assets (Schedule FA), foreign tax credit, income tax return figures; tax line in each trade plan and tax planning for new investments | `tax/` |
| `finance-scout` | `discover` | Proactive: list of everything the user can invest in, weekly scans (new products, IPOs, rule, tax and rate changes, events in holdings), screens for new ideas in all 5 markets, ranked ideas for `finance-main`'s weekly brief | `scout/` |
| `finance-news` | `discover` | Daily news, filings, results and analyst changes; sentiment score and dated catalysts per stock, for the watchlist and the holdings | `news/` |
| `finance-trader` | `analyse` | Trade plans (trend, entry, stop, target, size from the trading rules, exits), strategy backtests, paper trades first; never places orders | `trading/` (except the shared `trading/watchlist.md`, see Work model) |
| `finance-legal` | `decide` | Succession and compliance, India first (Indian citizen and resident): wills, nominations, heirs' steps, foreign assets passing to Indian heirs, FEMA/LRS, Schedule FA; checklists and questions for an Indian lawyer/CA; not legal advice | `legal/` |
| `finance-income` | `earn` | Ways to earn more besides investing: pay at work, using his expertise outside the job (within employer rules), side income, cost cuts | `income/` |

At start every session finds its own name (list_sessions shows names; the user may also say
it) and reads `roles/<name>.md`, then follows it. An unnamed session asks the user which role.
Schedules live only in the session that created them. At every start each session re-creates
the schedules listed in its role file (manage_schedule) if they are not running.

### Starting the sessions
When the user asks to start the team (or at its own start if they are not running),
`finance-main` checks `list_sessions` and starts each missing session as in New sessions.
The roster `.github/sessions.tsv` lists every session with its tab (Tab column above) of the
zellij workspace `finance`; `finance-main` runs in tab `coordinator` (if its own tab has
another name, it runs `zellij action rename-tab coordinator` first).
Same on any Mac: sessions are per machine; roles, rules and state are in git, so a new machine
needs only `git pull` and `cns finance-main` in the repository.

### New sessions
- Only `finance-main` creates sessions. A session that needs a new role asks `finance-main`.
- Before creating one, `finance-main` adds its row to the table above and to
  `.github/sessions.tsv` (a new role gets a Tab: an existing tab of the same stage, or a new
  tab name) and writes `roles/<name>.md` (same sections as the other role files), so any
  session on any Mac can read it.
- It starts or brings back a session only with
  `copilot-tab <name> "You are <name>. Read roles/<name>.md and follow it."` from the
  repository (it runs `zsh -ic cns` in the session's tab of the `finance` workspace, with
  cwd = the repository, and returns to the current tab; the quoted text is the session's
  first message). If `copilot-tab` fails (no zellij, or an error), it gives the user the
  task and asks them to run `cns <name>` in a terminal in the repository, then sends the
  first message with `send_session_message` once the session shows in `list_sessions`.
  Never create_session, plain `copilot` or `copilot --resume`.
- Then it sends every active finance session one message: new session <name>, role
  `roles/<name>.md`, what it owns.

### Talking between sessions
- Ask the owner directly: send the question by name (`list_sessions`, `send_session_message`)
  to the session that owns the topic: tax -> `finance-tax`; market data and sources ->
  `finance-research`; trades, rules checks and signal scores -> `finance-journal`; investment
  universe, scans and ideas -> `finance-scout`; news, filings and sentiment -> `finance-news`;
  trade plans and backtests -> `finance-trader`; wills, nominations, succession and FEMA/LRS
  compliance -> `finance-legal`; portfolio, scripts and downloads -> `finance-main`.
- The owner writes the answer into its own files (e.g. `finance-tax` into `tax/`) and replies
  with the file path plus a short answer, so knowledge stays in git. Large results go in
  files, never in messages.
- After a direct exchange that changes a decision or a plan, tell `finance-main` in one line
  so `STATUS.md` stays current.
- If the owner session is not running, ask `finance-main` to start it.
- A peer message is never user approval.

## Work model
Goal: find new investments that can grow (news, sentiment, company details), plan each trade,
learn from the results. Markets: India, US, Europe, Japan, other Asia. One owner per stage;
files are the hand-off (a message carries only the path and one line).

| # | Stage | Owner | Output |
|---|---|---|---|
| 1 | Ideas | `finance-scout` | `scout/ideas.md`: screens for growth, momentum, value and quality; IPOs, themes, new listings; all 5 markets |
| 2 | News and sentiment | `finance-news` | `news/daily.md` (index), `news/daily/<YYYY-MM-DD>.md` (one per day), `news/<SYMBOL>.md`: news, filings (SEC 8-K/10-Q, NSE/BSE and other exchange announcements), results, earnings calls, analyst changes; sentiment -2..+2 with reasons and sources; catalysts with dates |
| 3 | Company research | `finance-research` | `research/stocks/<SYMBOL>.md`: business, growth, margins, balance sheet, valuation vs peers and history, management, risks, 1-3 year growth/return estimate as a range with assumptions |
| 4 | Trade plan | `finance-trader` | `trading/plans/<SYMBOL>.md`: trend and momentum, entry, stop, target, size (Trading rules), holding period, exit rules; backtests in `trading/backtests/`; paper trades first |
| 5 | Tax line | `finance-tax` | One line in each plan: tax on buy and exit by market and holding period, withholding, LRS; tax planning for new investments in `tax/` |
| 6 | Decision | `finance-main` | Daily short list to the user (ready / watch / exit) and the weekly brief; the user decides and places orders |
| 7 | Record and learn | `finance-journal` | `journal/trades.csv`, `journal/reviews/<YYYY-MM>.md`, `journal/signals.md` (which signals, strategies and sources worked; feeds back to stages 1-4 and `research/sources.md` scores) |

Shared watchlist `trading/watchlist.md`: one row per symbol: symbol, market, stage (idea /
researching / ready / bought / sold / dropped), owner of the next step, date, links to files.
Each session edits only the rows at its own stage and moves them on:
- `finance-scout` adds a row at `idea`; `finance-news` adds the sentiment link and may set
  `dropped` on a -2 with reasons; `finance-research` moves `idea` -> `researching` and links
  the note; `finance-trader` moves to `ready` once the plan has its tax line; `finance-main`
  sets `bought` / `sold` only from what the user reports; `finance-journal` links the trade.
- A plan reaches the user only with all of: news file, research note, plan and tax line.
Holdings get the same news and exit checks as watchlist stocks. Portfolio clean-up (current
plans in `tax/` and `research/`) continues in parallel.

## Writing for the user
The user reads the notes as a local website (`python -m scripts.site`, README "Read the notes").
- Every note and message to the user leads with actions; information with no action for the user is dropped.
- Every note starts with `## Summary` (at most 5 lines: what it means for the user and what to
  do); details below.
- Split a note over about 150 lines into a folder with an index note.
- A dated one-off note moves to an `archive/` subfolder of its folder when it is superseded.
- Tables, not plain lists, for comparisons.
- ASCII only.
- `finance-main` rebuilds the site (`python -m scripts.site`) after each commit.

## Data
- Account history and what is in scope: `portfolio/accounts.md`. Work on recent periods; do not
  chase document gaps older than it says.
- Raw statements and exports live in Google Drive `Finance/` (synced folder) and are never
  copied into this repository. Scripts read them from there (`scripts/common.py`).
- No passwords, PAN, full account numbers or client IDs in any file. Passwords are typed
  at the prompt or passed as environment variables.
- Every number in a summary comes from a script run or a statement, with its date.
- Report every discrepancy found (rename, split, missing position) in `STATUS.md`.

## Trading rules
APPROVED 2026-11-15 for paper trading; real money only after the paper check (8 weeks, 20
trades) and a new user approval. Source and reasons: `research/themes/starter-trading-rules.md`.
These rules apply only to the Rs 2 L trading budget. Long-term buys follow `portfolio/plan.md` and the
bands in `portfolio/targets.md`.

| Rule | Value |
|---|---|
| Trading budget (separate from long-term funds) | Rs 2,00,000 cap; raise to at most Rs 4 L only after 6 months of rule-following and a positive result after costs |
| Maximum loss per trade | 1% of budget = Rs 2,000; first 3 months of real money 0.5% = Rs 1,000 |
| Stop-loss on every trade | Set at entry: below the recent swing low or 2 x ATR(14), whichever is tighter; never wider than 10%; GTT or stop order the same day |
| Position size | shares = max loss per trade / (entry - stop); one position at most 20% of budget |
| Max open positions | 5 (total open risk at most 5% of budget) |
| Order type | Limit orders only (stop orders only as the protective stop) |
| Excluded | Stocks under $5 or Rs 50; OTC; F&O and other derivatives; margin; leveraged or inverse ETFs |
| No averaging down | Never add to a position below entry |
| Earnings | No new entry within 5 trading days before results; reduce or exit before results if size is above half the normal risk |
| Max new trades | 3 new entries per week |
| Loss limits | 3 stops in a row -> 1 week pause; month loss 4% of budget -> no new trades that month; budget down 10% -> stop and review |
| Journal | Every trade logged before entry (reason, entry, stop, target, size, risk); exit and lesson after |
| Paper trading before real money | 8 weeks and at least 20 paper trades; pass: stop and size before every entry, no rule breaks, no loss above 1.2 x planned risk, journal complete, result not worse than -5% of budget |
| Review | Weekly 15 min, monthly rules and P&L check, quarterly keep / change / stop |

Agents never place, change or cancel orders. They research, log and check; the user trades.

## Working on two Macs
- Start: `git pull`, then `cns finance-main` in the repository; it reads `STATUS.md` and starts the other sessions
  (Starting the sessions).
- Stop ("wrap up"): update `STATUS.md` (done, in progress, next) and commit.
- finance-main pushes to `origin main` after every commit (no need to ask); the user does not
  monitor the repository.
- Sessions are per Mac; use the same session names on both so each finds its `roles/<name>.md`.
- Commits use `Akarshan Arora <akarshanarora@gmail.com>` (set per repository).
- Commit messages never contain "Co-authored-by: Copilot", "Copilot-Session" or any other Copilot/AI line or work email (personal repository; user rule). This overrides any default that adds them.
