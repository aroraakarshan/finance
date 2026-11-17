# How our sessions would use them, and recommendation

Checked 2026-11-15.

## Summary
- finance-trader: engine.py + quantstats reports; vectorbt sweeps not used for now.
- finance-news: NSE RSS for filings, Google/Bing News RSS for news, GDELT backup.
- finance-journal: quantstats reports on trade returns.
- Discrepancies are listed at the end.

Back to the index: [libraries-and-news.md](../libraries-and-news.md).

Safety: all news sources are read-only. API keys (Finnhub, Marketaux, Alpha Vantage, NewsAPI)
would go in env vars, never in the repo. No source here needs broker credentials.

## 3. How our sessions would use them

- `finance-trader` (stage 4): keep `engine.py` as the engine (it already handles `.NS`, costs,
  splits by period). Add **quantstats** to turn each strategy's daily returns into a tear
  sheet vs `^NSEI`/NIFTYBEES or SPY in `trading/backtests/`. Use **vectorbt** (open source)
  only when a plan needs a parameter sweep (stop width, ATR multiple, lookback) across many
  symbols; check one result against `engine.py` before trusting it.
- `finance-news` (stage 2): add the **NSE announcement RSS** feeds (main, results, board
  meetings, corporate actions, insider trading) as the primary India filings source next to
  SEC EDGAR; keep Google/Bing News RSS for news. GDELT as an optional third route for India
  press counts and tone when Google/Bing are thin. FinBERT optional, headlines only.
- `finance-journal` (stage 7): quantstats reports on paper/real trade returns.
- Not recommended: backtrader (dead), pandas-ta (repo gone), paid news APIs (US-centric,
  free tiers too small or dev-only).

## 4. Recommendation

Libraries: 1) **quantstats** (metrics/reports, Apache-2.0, 3.13 ok); 2) **vectorbt open
source** (EOD rule sweeps, free for personal use; PRO not needed).
News: 1) **NSE announcement RSS** (free, primary, live, no key); 2) keep **Google + Bing
News RSS**, with **GDELT** as a no-key backup once its rate limit allows.

Discrepancies found: pandas-ta GitHub repo is gone (404) while PyPI still serves it;
Alpha Vantage news sentiment is now marked Premium; Finnhub company news is North America
only despite the "Global" title; the engine `trading/backtests/engine.py` (formerly `bt.py`, which
collided with the `bt` package; renamed 2026-11-15) has no name clash now.

Update 2026-11-15 (finance-trader): engine renamed to `trading/backtests/engine.py`; quantstats accepted for later; vectorbt parameter sweeps not used for now, because backtests keep published parameters fixed (no optimisation) to avoid overfitting.
