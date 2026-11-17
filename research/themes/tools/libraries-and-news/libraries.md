# Backtest and analytics libraries

Checked 2026-11-15 (all facts below dated 2026-11-15 unless noted). Research only: nothing
installed, no accounts made. Repo stats from the GitHub API (`api.github.com/repos/<repo>`),
versions and Python support from PyPI JSON (`pypi.org/pypi/<pkg>/json`).

## Summary
- Keep our own `trading/backtests/engine.py`; add **quantstats** for reports (maintained, 3.13 ok).
- **vectorbt** (free open source) only for parameter sweeps; PRO not needed.
- Avoid backtrader (no updates since 2024) and pandas-ta (GitHub repo gone).
- All libraries take any pandas table, so India `.NS` closes from yfinance work.

Back to the index: [libraries-and-news.md](../libraries-and-news.md).

Context: `trading/backtests/engine.py` (renamed from `bt.py` on 2026-11-15; 727 lines on 2026-11-15) is our own pandas engine on cached yfinance
closes (US + India `.NS`, costs per market). The repo `.venv` is Python 3.13 with yfinance
1.8.0. Any library must run on 3.13 and take a plain pandas price table. Stages: backtests =
stage 4 (`finance-trader`); news/sentiment = stage 2 (`finance-news`); results reviewed in
stage 7 (`finance-journal`). No library here touches a broker; all are read-only by nature.

## 1. Backtest and analytics libraries

| Library (repo) | Stars / open issues | Last push / last PyPI release | Python (PyPI) | Licence |
|---|---|---|---|---|
| vectorbt (polakowo/vectorbt) | 9852 / 127 | 2026-11-11 / 1.2.1, 2026-11-11 | 3.11-3.14 | Apache-2.0 + Commons Clause |
| backtrader (mementum/backtrader) | 23745 / 64 | 2024-08-19 / 1.9.78.123, 2023-04-19 | classifiers stop at 3.7 | GPL-3.0 |
| zipline-reloaded (stefan-jansen) | 2017 / 4 | 2026-11-02 / 3.2.1, 2026-10-25 | 3.11-3.14 | Apache-2.0 |
| backtesting.py (kernc) | 9241 / 108 | 2026-08-05 / 0.6.6, 2026-07-22 | >=3.9 (no classifiers) | AGPL-3.0 |
| bt (pmorissette/bt) | 3020 / 13 | 2026-11-13 / 1.4.1, 2026-10-10 | 3.9-3.13 | MIT |
| quantstats (ranaroussi) | 7871 / 33 | 2026-11-02 / 0.0.86, 2026-09-27 | 3.10-3.13 | Apache-2.0 |
| pyfolio-reloaded (stefan-jansen) | 624 / 0 | 2026-11-02 / 0.10.2, 2026-11-02 | 3.11-3.15 | Apache-2.0 |
| empyrical-reloaded (stefan-jansen) | 133 / 1 | 2026-11-08 / 0.7.2, 2026-11-02 | 3.11-3.15 | Apache-2.0 |
| Riskfolio-Lib (dcajasn) | 4610 / 12 | 2026-11-04 / 7.4.1, 2026-11-04 | 3.10-3.14 | BSD-3-Clause |
| TA-Lib (TA-Lib/ta-lib-python) | 12411 / 88 | 2026-11-11 / 0.8.3, 2026-10-28 | 3.9-3.14; cp313 macOS arm64 wheel | BSD-2-Clause |
| pandas-ta (twopirllc/pandas-ta) | repo returns 404 | - / 0.4.71b0 (beta), 2025-09-14 | >=3.12, classifier 3.12 only | not verified |

Sources: GitHub API and PyPI JSON for each row; vectorbt licence text
https://raw.githubusercontent.com/polakowo/vectorbt/master/LICENSE.md.

Notes per library (India data: every library here is data-agnostic; it takes whatever pandas
table we load, so `.NS` closes from yfinance work the same as US closes):
- **vectorbt (open source)**: vectorised signals -> portfolio (`Portfolio.from_signals`), fast
  parameter grids, built-in yfinance loader. Commons Clause forbids selling it as a service;
  personal use is fine. **vectorbt PRO** is a separate paid private repo: $25/month, $225/year,
  $500 lifetime (https://vectorbt.pro/become-a-member/); PRO now ships "agent skills" for
  Claude/coding agents (https://vectorbt.pro/). Learning curve: medium-high (numba, broadcasting).
  Fit 4: fastest way to sweep simple EOD rules (stops, ATR, rotation) over our universe.
- **backtrader**: event-driven, large old community. No push since 2024-08, no PyPI release
  since 2023-04, classifiers end at 3.7; 3.12/3.13 compatibility not verified. Fit 2: unmaintained.
- **zipline-reloaded**: Quantopian engine kept alive by Stefan Jansen. Needs a data "bundle"
  ingested first; default `quandl` bundle uses Quandl WIKI (docs:
  https://raw.githubusercontent.com/stefan-jansen/zipline-reloaded/main/docs/source/bundles.rst);
  WIKI stopped updating in 2018 (not verified today). For India we would write a `csvdir`
  bundle; exchange_calendars has BSE (`XBOM`) but no NSE code
  (https://raw.githubusercontent.com/gerrymanoim/exchange_calendars/master/README.md).
  Learning curve high. Fit 2: too heavy for EOD rules.
- **backtesting.py**: one-asset-at-a-time event backtester, simple API, nice HTML plots.
  AGPL (fine for private use; would bind us only if we published a service). No portfolio
  rotation across many symbols. Fit 3: good for single-stock rule checks, not rotation.
- **bt**: tree of "algos" for allocation/rotation strategies, MIT. Data via `ffn`, whose Yahoo
  default is now deprecated in favour of an explicit `provider='yahoo'`
  (https://raw.githubusercontent.com/pmorissette/ffn/master/ffn/data.py). Learning curve
  low-medium. Fit 3. Our engine was renamed from `bt.py` to `engine.py` on 2026-11-15 (finance-trader), so `import bt` is no longer shadowed
  when scripts run from that folder.
- **quantstats**: performance metrics and HTML tear sheets from a returns series (Sharpe,
  Sortino, drawdowns, monthly table, vs benchmark e.g. `^NSEI` or SPY). Single maintainer
  (Ran Aroussi), version still 0.0.x but releases through 2026-09 and push 2026-11. Learning
  curve very low. Fit 5: drop-in report for the returns `engine.py` already produces.
- **pyfolio-reloaded / empyrical-reloaded**: Jansen-maintained successors of Quantopian's
  tear sheets and metric functions. Maintained, 3.11+. Overlaps quantstats; pyfolio is
  notebook-oriented. Fit 3.
- **Riskfolio-Lib**: portfolio optimisation (mean-variance, CVaR, risk parity, HRP) on cvxpy.
  Not a backtester. Fit 2 for trader; possibly 3 for finance-research allocation work.
- **TA-Lib**: C indicator library; since 0.6.x PyPI ships binary wheels (cp313 macOS arm64
  present), so no separate C build. Fit 3: only if we need many indicators; ATR/SMA are
  already a few pandas lines in `engine.py`.
- **pandas-ta**: GitHub repo now 404; PyPI only has 0.4.x betas, Python 3.12 classifier only,
  pins `numba==0.61.2`. Community fork `xgboosted/pandas-ta-classic` exists (unofficial, not
  reviewed). Fit 1: avoid; supply-chain and maintenance risk.
