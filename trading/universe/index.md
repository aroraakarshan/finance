# Scan universe

## Summary
- US: 684 of 918 names pass; India: 197 of 200 pass (data to 2026-11-13 close).
- US filter: close > $5 and 50-day average volume > 1,000,000 shares.
- India filter: close > Rs 50 and 50-day average traded value > Rs 20 crore (Nifty 200 names are already liquid, so this only drops thin ones).
- Failed or empty downloads after one retry: 0. Built 2026-11-15 in 9 min.

## Counts

| Market | Source | Names | Included |
|---|---|---|---|
| US | Nasdaq 100 | 101 | 96 |
| US | S&P 400 | 400 | 237 |
| US | S&P 500 | 503 | 433 |
| US | all (unique) | 918 | 684 |
| India | Nifty 200 | 200 | 197 |
| India | all (unique) | 200 | 197 |

| Market | Exclusion reason | Names |
|---|---|---|
| US | 50d avg volume under 1M | 233 |
| US | under 50 bars | 1 |
| India | price under Rs 50 | 3 |

## Failed downloads

None.

## Survivorship bias

These are today's index members. Stocks that were dropped, merged or went bust since 2010 are missing, so a backtest on this list over past years looks better than reality (it only holds the survivors). Use it for the daily scan; treat long backtests on it as an upper bound.

## Files and rebuild

- `us.csv`, `india.csv`: symbol, name, source index, sector, close, avg_volume (50 days), avg_value (50 days, local currency), history_start, included, reason.
- Prices: shared cache `/Users/akarshanarora/.local/share/superpowers/finance-trader-backtests/cache` (`<symbol>.csv`, `&` and `^` become `_`); `refresh` writes the latest bars to `/Users/akarshanarora/.local/share/superpowers/finance-trader-backtests/cache/live`.
- Rebuild: `.venv/bin/python -m trading.universe build` (lists from Wikipedia and NSE, downloads only names not yet cached, filters on the engine's LAST close). Daily: `.venv/bin/python -m trading.universe refresh`.
- Sources: Wikipedia (S&P 500, S&P 400 with GICS sector; Nasdaq 100 with ICB industry), NSE `ind_nifty200list.csv` (industry).
