# Backtest/analytics libraries and news/sentiment sources

Checked 2026-11-15. Research only: nothing installed, no accounts made.

## Summary
- Backtests: keep our own `trading/backtests/engine.py`; add **quantstats** for reports; **vectorbt** (free) only if a parameter sweep is ever needed.
- News: add the free **NSE announcement RSS** feeds for India filings (poll daily); keep Google + Bing News RSS; GDELT as a no-key backup.
- Skip backtrader, pandas-ta and the paid news APIs (US-centric or too small free tiers).
- Nothing to buy; no keys or broker access needed.

## Parts

| Part | What is in it |
|---|---|
| [libraries.md](libraries-and-news/libraries.md) | Stars, releases, Python support, licences and notes for 11 backtest/analytics libraries |
| [news.md](libraries-and-news/news.md) | 10 news and sentiment sources: cost, India coverage, limits, FinBERT details, sources |
| [usage.md](libraries-and-news/usage.md) | How each session would use them, recommendation, discrepancies, trader update |

## Ranked table

| Candidate | Cost | India? | Read-only possible | Maintainer | Fit |
|---|---|---|---|---|---|
| NSE announcement RSS | free | yes (NSE) | yes (no login) | NSE (official) | 5 |
| Google / Bing News RSS | free | yes | yes | Google / Microsoft | 5 |
| quantstats | free, Apache-2.0 | yes (any pandas data) | yes (local) | Ran Aroussi (single) | 5 |
| vectorbt (open source) | free; PRO $25/month | yes (any pandas data) | yes (local) | Oleg Polakow | 4 |
| bt | free, MIT | yes | yes (local) | pmorissette (GitHub) | 3 |
| backtesting.py | free, AGPL-3.0 | yes | yes (local) | kernc | 3 |
| pyfolio/empyrical-reloaded | free, Apache-2.0 | yes | yes (local) | Stefan Jansen | 3 |
| TA-Lib | free, BSD-2 | yes | yes (local) | TA-Lib org | 3 |
| GDELT DOC 2.0 | free, 1 req/5 s | yes | yes (no key) | GDELT Project | 3 |
| FinBERT | free, CC BY-NC-SA weights | English only | yes (local) | Prosus (no support) | 3 |
| zipline-reloaded | free, Apache-2.0 | needs custom bundle | yes (local) | Stefan Jansen | 2 |
| Riskfolio-Lib | free, BSD-3 | yes | yes (local) | dcajasn (GitHub) | 2 |
| Finnhub | free key; sentiment paid | no (company news NA only) | yes (key) | Finnhub | 2 |
| Marketaux | free 100/day; $29+ | not verified | yes (key) | Marketaux | 2 |
| Alpha Vantage news | premium $49.99+ | not verified | yes (key) | Alpha Vantage | 2 |
| BSE notices RSS | free | BSE notices only | yes | BSE (official) | 2 |
| backtrader | free, GPL-3.0 | yes | yes (local) | inactive since 2024 | 2 |
| NewsAPI.org | free dev-only; $449/month | not verified | yes (key) | NewsAPI | 1 |
| pandas-ta | free | yes | yes (local) | repo gone (404) | 1 |
