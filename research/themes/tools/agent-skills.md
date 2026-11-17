# Agent skills and MCP for finance work (checked 2026-11-15)

## Summary
No ready-made skill is worth installing as-is; our `market-data` already covers the free data.
Best value: copy the comps, DCF and earnings methods from Anthropic's official
`anthropics/financial-services` (Apache-2.0, fit 4) into our own skills, without its paid MCP servers.
`himself65/finance-skills` (MIT, fit 3) has useful trend/earnings write-ups to copy; OpenBB (fit 3) mostly duplicates `market-data`.
To do: the user decides which methods to add, then adds them through the `skills` session.

Question: are there ready-made agent skills (SKILL.md), agents or MCP servers we should add
to our Copilot CLI finance sessions? Research only; nothing installed or run.

Our skills today (`~/.copilot/skills`, linked from the user's dotfiles): `market-data`
(yfinance, SEC EDGAR, NSE, LRS rules), `finance-downloads` (the brief calls it `finance-docs`;
the installed name is `finance-downloads`), `pptx-generator`, `dev-workflow`.

How a new skill would reach our sessions: Copilot CLI reads SKILL.md from `~/.copilot/skills/`,
project `.github/skills/` or `.claude/skills/`, and from plugins; it can also install Claude
plugins (`.claude-plugin/plugin.json`) and marketplaces (`copilot plugin install`,
`copilot plugin marketplace add`) (source: Copilot CLI 1.0.112 built-in docs, checked
2026-11-15). Our rule: the user adds any new skill through the `skills` session into the dotfiles
layer; agents do not run `copilot plugin install` or copy files into `~/.copilot/skills`.
Best path for anything below: copy the useful method text into our own skill (licence
permitting), not install the third-party package.

## 1. anthropics/financial-services (Claude for Financial Services)
- Source: https://github.com/anthropics/financial-services and GitHub API (2026-11-15).
  Official Anthropic. 41.3k stars, 238 open issues, last commit 2026-11-12, Apache-2.0.
  (The old name `anthropics/financial-services-plugins` redirects here.)
- What: Claude Cowork / Claude Code plugins. Core plugin `financial-analysis` has skills
  comps-analysis, dcf-model, lbo-model, 3-statement-model, audit-xls, clean-data-xls,
  competitive-analysis, deck-refresh, pptx-author, xlsx-author and more. Vertical
  `equity-research` has earnings-analysis, earnings-preview, catalyst-calendar,
  idea-generation, initiating-coverage, model-update, morning-note, sector-overview,
  thesis-tracker. Also named agents (Market Researcher, Earnings Reviewer, Model Builder)
  and slash commands `/comps`, `/dcf`, `/earnings`.
- Quality: long, structured, written for sell-side analysts (earnings-analysis is 228 lines,
  "8-12 pages, JPMorgan/GS format, Times New Roman"). Good methods (formulas, not pasted
  numbers, in Excel; sensitivity tables; beat/miss structure). Too heavy for our one-page notes.
- Code / network: skills are markdown; dcf-model runs Python/openpyxl and a `recalc.py`.
  `.mcp.json` points to 12 paid remote MCP servers (FactSet, S&P Kensho, Morningstar, Daloopa,
  LSEG, PitchBook, Moody's, MT Newswires, Aiera, Chronograph, Egnyte, Box). comps-analysis
  says "use MCP exclusively, DO NOT use web search"; without those subscriptions it falls
  back to SEC EDGAR. Installing the whole plugin would register 12 remote servers: risk of
  data going to third parties and of tool-result prompt injection. Never install as-is.
- Cost: repo free; data connectors need paid subscriptions (not priced, "may require a
  subscription or API key").
- Markets: method is market-neutral; data connectors are US/global institutional. India via
  our own sources only.
- Overlap: `market-data` (data), `pptx-generator` (decks; pptx-author overlaps).
- Use: finance-research (stage 3: comps, DCF, earnings-analysis as checklists), finance-news
  (stage 2: earnings-preview, catalyst-calendar ideas), finance-scout (idea-generation).
- Fit 4: best-written method, official, Apache-2.0; take comps/DCF/earnings steps into
  `market-data` or a new research skill, drop the MCP block.

## 2. anthropics/skills (official Anthropic skills)
- Source: https://github.com/anthropics/skills, README (2026-11-15). 194.8k stars,
  1,543 open issues, pushed 2026-11-14. Repo has no top-level licence in the API; README says
  most skills and docx/pdf/pptx/xlsx are Apache-2.0; `skills/xlsx/LICENSE.txt` is Apache-2.0.
- What: 19 skills incl. `xlsx`, `pdf`, `docx`, `pptx`, `skill-creator`, `mcp-builder`. No
  finance-specific skill.
- Code: xlsx/pdf ship `scripts/` (Python: openpyxl, pypdf, LibreOffice recalculation). Local
  only, no network calls found in SKILL text (scripts not fully read: not verified).
- Overlap: `pptx-generator` covers pptx; `finance-downloads` and our `scripts/` read PDFs.
- Use: finance-main / finance-tax for reading statements (pdf) and building xlsx workbooks;
  finance-research for spreadsheets. Fit 3: solid, but we rarely need Excel output.

## 3. github/awesome-copilot
- Source: https://github.com/github/awesome-copilot (API, docs/README.skills.md,
  README.agents.md, README.instructions.md, 2026-11-15). Official GitHub, MIT, 41.2k stars,
  75 open issues, pushed 2026-11-14. Built-in marketplace in Copilot CLI.
- Finance content: none for investing. Found `convert-pdf-to-md`, `convert-excel-to-md`,
  `convert-word-to-md` (MarkItDown + pymupdf scripts; skill says install Python packages
  first), `d365-solution-blueprint` (Dynamics 365 ERP, not investing),
  `gtm-board-and-investor-communication` (startup board decks), `lightweight-charts-react-
  components` (TradingView chart library recipes), `new-relic-finops` agent (cloud cost).
  No finance instructions files.
- Use: convert-pdf-to-md could help finance-tax / finance-main read broker PDFs; `pptx-generator`
  already uses markitdown. Fit 2: little to add.

## 4. Community finance skill collections (GitHub search, 2026-11-15)
Search: `api.github.com/search/repositories?q=topic:agent-skills+finance` (231 results) and
`q=finance+skill+SKILL.md` (13 results). All unofficial: treat as untrusted code.

| Repo | Stars | Last push | Licence | What | Notes |
|---|---|---|---|---|---|
| himself65/finance-skills | 3,543 | 2026-11-04 (release v11.2.1, 2026-10-25) | MIT | ~25 skills: yfinance-data, company-valuation (DCF+SOTP), earnings-preview/recap, estimate-analysis, etf-premium, sepa-strategy (Minervini trend template, sizing), stock-liquidity, stock-correlation, social readers (X, Discord, Telegram), data providers (Fintel, Adanos sentiment, tradingview-mcp, Hyperliquid) | One person (user account). yfinance-data runs `pip install yfinance` itself if missing (would bypass our .venv rule). tradingview-mcp starts a third-party MCP via `uvx`. Social readers pull untrusted text: prompt-injection risk. India: yfinance `.NS` works, not stated in skills |
| RKiding/Awesome-finance-skills | 3,122 | 2026-03-29 | Apache-2.0 | 8 "alphaear" skills: news (Cailian, WSJ, Weibo, Polymarket), A-share/HK/US stock data, FinBERT sentiment, Kronos forecasting, signal tracker | China focus; not updated for 7 months; ML models download; fit low |
| alirezarezvani/claude-skills (finance/) | 29,830 (whole repo) | 2026-11-12 | MIT | finance/skills: financial-analyst, stock-analysis, passive-deal-screener, saas-metrics-coach, month-end-close | Mega-collection of 410+ skills; finance part content not read: not verified |
| komako-workshop/digital-oracle | 913 | 2026-07-26 | MIT | Macro questions (housing, gold, BTC) with probability estimates | Not read: not verified |
| lzwme/finance-quant-skills | 488 | 2026-11-10 | none | A-share (China) quant trading | No licence = not reusable; China only |
| eli-alvarado/us-watchlist-alerts | 4 | 2026-11-13 | MIT | US watchlist price alerts | Tiny, new; not read |

- Best of these: himself65 `sepa-strategy` (trend template, VCP, position sizing) for
  finance-trader (stage 4) and `earnings-preview`/`estimate-analysis` for finance-news
  (stage 2). Overlap: `market-data` already covers yfinance, so yfinance-data adds nothing.
- Fit: himself65 3 (useful methods to copy, MIT; do not install the plugins); others 1-2.

## 5. Trading / backtesting skills
- No official trading or backtesting skill found (anthropics, github: none, 2026-11-15).
- himself65 `sepa-strategy` (says "never execute trades based solely on this analysis") and
  `options-payoff` (options are excluded for us: no derivatives abroad under LRS).
- lzwme/finance-quant-skills: A-share only, no licence.
- Broad search `claude skills trading OR backtesting SKILL` returns general mega-repos, no
  focused backtest skill. Our backtests stay as scripts in `trading/backtests/` (finance-trader).
- No skill found places orders; any that does must not be used (agents never trade).

## 6. OpenBB (Open Data Platform) and openbb-mcp
- Source: https://github.com/OpenBB-finance/OpenBB (now redirects to `openbq-org/OpenBB`;
  reason for the rename not verified; PyPI and README still point to openbb.co and
  OpenBB-finance), PyPI JSON, https://docs.openbb.co/odp/python/extensions/interface/openbb-mcp
  (2026-11-15). 75.4k stars, 115 open issues, pushed 2026-11-14, Apache-2.0 ("Copyright
  2021-2026 OpenBB Inc."). Maintainer: OpenBB Inc.
- What: Python data platform (`openbb` 5.0.0, 2026-09-29) with provider extensions
  (`openbb-yfinance` 2.1.0 2026-11-01, `openbb-sec` 2.0.0, `openbb-fmp` 1.6.1 2026-05-26,
  cboe, imf, ...). `openbb-mcp-server` 2.0.1 (2026-09-28) serves every installed route as MCP
  tools; default HTTP on 127.0.0.1:8001, or stdio. `--allowed-categories` limits which tools
  exist; `--tool-discovery` hides tools behind discovery.
- Safety: data only, no broker or order tools found; local process; API keys in
  `~/.openbb_platform` credentials or env vars. Runs pip packages from many providers
  (supply-chain surface). Bind to localhost only.
- Cost: open source free; keys for paid providers (FMP, Polygon, Intrinio) priced by each
  provider; OpenBB Workspace (web app) pricing page redirects to the home page: not verified.
- Markets: same as the provider used. India via yfinance `.NS/.BO` (same as our `market-data`);
  other India providers not verified. US strong (SEC, CBOE, FMP); Europe/Japan via yfinance.
- `OpenBB-finance/agents-for-openbb`: 415 stars, MIT, last push 2026-07-01; agents for the
  OpenBB Workspace web app, not for Copilot CLI. Fit 1.
- Overlap: almost all with `market-data` (yfinance + SEC EDGAR). Adds one normalised API
  across providers, IMF/macro and CBOE data.
- Use: finance-research and finance-scout (stages 1, 3) if we later pay for a data provider.
- Fit 3: well maintained, read-only, but duplicates what already works for free.

## Discrepancies found
- Brief names our skill `finance-docs`; the installed skill is `finance-downloads`.
- `OpenBB-finance/OpenBB` redirects to `openbq-org/OpenBB` (odd org name); check it is the real
  OpenBB before any install.
- anthropics/skills shows no repo-level licence in the GitHub API; licences are per skill.

## Ranked
| Candidate | Cost | India? | Read-only possible | Maintainer | Fit |
|---|---|---|---|---|---|
| anthropics/financial-services (comps, DCF, earnings skills; copy method only) | free; MCP data paid | method only | yes (skip .mcp.json) | Anthropic (official) | 4 |
| himself65/finance-skills (sepa-strategy, earnings-preview, valuation) | free; some APIs paid | via yfinance .NS | yes; skip social/MCP parts | one individual (unofficial) | 3 |
| OpenBB ODP + openbb-mcp-server | free; provider keys paid | via yfinance only | yes (data only) | OpenBB Inc. | 3 |
| anthropics/skills (xlsx, pdf) | free | n/a | yes, local scripts | Anthropic (official) | 3 |
| github/awesome-copilot (convert-pdf-to-md etc.) | free | n/a | yes, local scripts | GitHub (official) | 2 |
| RKiding/Awesome-finance-skills | free | no (China/HK/US) | partly; many web sources | individual (unofficial) | 1 |
| alirezarezvani/claude-skills finance/ | free | not verified | not verified | individual (unofficial) | 2 |
| lzwme/finance-quant-skills | free, no licence | no (A-share) | not verified | individual | 1 |
| OpenBB-finance/agents-for-openbb | Workspace pricing not verified | no | n/a | OpenBB Inc. | 1 |
