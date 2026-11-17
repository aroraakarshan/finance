# Backtest data: gap-up drift (post-earnings-announcement drift proxy)

## Summary
- Yahoo daily data 2010 to 2026-11-13; bad bars in the India ETFs were repaired, stale filler rows dropped (table below).
- Stock results are biased upwards: the lists are today's large caps (survivorship).

Run 2026-11-16 with `.venv/bin/python trading/backtests/engine.py gap-drift`; every number on this page is printed by that script.

## Data
- Source: Yahoo Finance daily bars via yfinance 1.8.0, `auto_adjust=True` (prices adjusted for splits and dividends), 2010-01-01 to 2026-11-13 (last close). Downloaded 2026-11-15; cached outside the repository in `~/.local/share/superpowers/finance-trader-backtests/cache/`.
- Universe (today's large caps, chosen with hindsight):
  - US ETFs: SPY QQQ IWM EFA EEM TLT GLD. US stocks: AAPL MSFT NVDA AMZN GOOGL META AVGO JPM V MA UNH LLY JNJ PG KO PEP XOM CVX HD COST WMT BAC CSCO ORCL ADBE CRM AMD QCOM TXN INTC CAT GE HON.
  - India ETFs: NIFTYBEES BANKBEES GOLDBEES. India stocks (NSE): RELIANCE TCS HDFCBANK ICICIBANK INFY HINDUNILVR ITC SBIN BHARTIARTL KOTAKBANK LT AXISBANK BAJFINANCE ASIANPAINT MARUTI SUNPHARMA TITAN ULTRACEMCO NESTLEIND HCLTECH WIPRO POWERGRID NTPC ONGC TATASTEEL JSWSTEEL M&M ADANIPORTS DRREDDY CIPLA. Index ^NSEI (Nifty 50) used for the regime filter and as benchmark.
- Data checks (run by the script): tickers with any issue listed; moves above 40% in one day on a large cap are treated as suspect.

| Ticker | First bar | Bars used | NaN or zero-price rows dropped | Stale bars dropped (volume 0, O=H=L=C) | Bars repaired (wrong scale) | Bad open/high/low prints fixed (India ETFs) | High/low inconsistent bars | Largest 1-day move after repair | Close-to-close moves > 40% after repair | Open gaps > 40% after repair |
|---|---|---|---|---|---|---|---|---|---|---|
| META | 2012-05-18 | 3644 | 0 | 0 | - | 0 | 0 | 29.6% | - | - |
| AMD | 2010-01-04 | 4242 | 0 | 1 | - | 0 | 0 | 52.3% | 2016-04-22 52.3% | - |
| NIFTYBEES.NS | 2010-01-04 | 3992 | 0 | 169 | 2019-12-19 to 2019-12-20 x10 | 173 | 0 | 17.4% | - | - |
| BANKBEES.NS | 2010-02-05 | 3804 | 11 | 346 | 2019-12-19 to 2019-12-20 x10 | 59 | 0 | 14.4% | - | - |
| GOLDBEES.NS | 2010-02-05 | 3805 | 11 | 344 | 2019-12-19 to 2019-12-20 x100 | 90 | 0 | 10.5% | - | - |
| RELIANCE.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 14.7% | - | - |
| TCS.NS | 2010-01-04 | 4161 | 0 | 2 | - | 0 | 0 | 12.2% | - | - |
| HDFCBANK.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 12.6% | - | - |
| ICICIBANK.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 17.8% | - | - |
| INFY.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 21.3% | - | - |
| HINDUNILVR.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 17.4% | - | - |
| ITC.NS | 2010-01-04 | 4160 | 0 | 3 | - | 0 | 0 | 12.8% | - | - |
| SBIN.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 27.7% | - | - |
| BHARTIARTL.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 12.0% | - | - |
| KOTAKBANK.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 13.0% | - | - |
| LT.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 16.3% | - | - |
| AXISBANK.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 27.9% | - | - |
| BAJFINANCE.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 23.2% | - | - |
| ASIANPAINT.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 14.0% | - | - |
| MARUTI.NS | 2010-01-04 | 4158 | 0 | 5 | - | 0 | 0 | 16.9% | - | - |
| SUNPHARMA.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 15.1% | - | - |
| TITAN.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 18.8% | - | - |
| ULTRACEMCO.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 14.5% | - | - |
| NESTLEIND.NS | 2010-01-08 | 4155 | 0 | 8 | - | 0 | 0 | 12.8% | - | - |
| HCLTECH.NS | 2010-01-04 | 4160 | 0 | 4 | - | 0 | 0 | 12.7% | - | - |
| WIPRO.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 16.8% | - | - |
| POWERGRID.NS | 2010-01-04 | 4160 | 0 | 3 | - | 0 | 0 | 12.4% | - | - |
| NTPC.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 15.5% | - | - |
| ONGC.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 18.5% | - | - |
| TATASTEEL.NS | 2010-01-04 | 4161 | 0 | 2 | - | 0 | 0 | 13.7% | - | - |
| JSWSTEEL.NS | 2010-01-04 | 4152 | 0 | 11 | - | 0 | 0 | 17.8% | - | - |
| M&M.NS | 2010-01-04 | 4158 | 0 | 5 | - | 0 | 0 | 16.9% | - | - |
| ADANIPORTS.NS | 2010-01-04 | 4157 | 0 | 6 | - | 0 | 0 | 21.1% | - | - |
| DRREDDY.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 14.6% | - | - |
| CIPLA.NS | 2010-01-04 | 4159 | 0 | 4 | - | 0 | 0 | 13.0% | - | - |

All other tickers: full history from early January 2010, no NaN or stale rows, no high/low inconsistencies, no 1-day move above 40%.

Data problems found and what was done:
- TATASTEEL.NS and CIPLA.NS came back empty in the first batch ("possibly delisted"); a retry one ticker at a time worked. No ticker was dropped for short history; META starts 2012-05-18 (IPO).
- Stale bars (volume 0 and open = high = low = close) are Yahoo filler rows on NSE holidays (for example RELIANCE.NS 2014-04-24, an election holiday) and long no-trade stretches in the India ETFs (BANKBEES 346 and GOLDBEES 344 such days in total, most in 2012-2013; NIFTYBEES 169). They were dropped. NESTLEIND.NS's first 4 rows (2010-01-04 to 07) were stale at the wrong scale (-76% "move" on 2010-01-08) and were dropped this way.
- Rows with an open of 0 (BANKBEES.NS and GOLDBEES.NS in January 2010) were dropped, so these two start in February 2010.
- NIFTYBEES, BANKBEES and GOLDBEES split their units in December 2019. Yahoo has the rest of the history adjusted but 2019-12-19 and 2019-12-20 at the unadjusted scale (for example NIFTYBEES close 129.25, then 13.02, then 129.93). Those two bars were multiplied back by 10 (100 for GOLDBEES).
- The India ETFs also have many bad open, high and low prints (for example NIFTYBEES 2021-03-26 open 183.48 against a close of 155.21; GOLDBEES 2020-11-27 open 37.40 against a close of 42.84). On days when the Nifty's own range was under 3%, an open more than 5% from the previous close while the close moved under 2.5% was set to the previous close, and highs or lows more than 5% outside the open/close were cut back to the open/close. Results that trade the India ETFs (swing-pullback, Faber ETF sets) are less reliable than the stock results.
- Real large moves were kept: AMD +52% on 2016-04-22 (results), the 2010-05-06 US flash crash, 2015-08-24, the NSE erroneous-order crash of 2012-10-05, March 2020, and the 2018-09-21 NSE crash (BAJFINANCE, ADANIPORTS, M&M). Stops in the backtest fill on those intraday lows, as real stop orders could have.
- No split errors were found in the NSE stocks (no 1-day move above 40% after the steps above).



## Known biases and limits
- Survivorship and hindsight bias: the stock lists are today's large caps and Nifty 50 members. Stocks that fell out (for example Yes Bank, Vedanta, IBM-style laggards) are missing, so stock results are biased upwards. The ETF and index results do not have this bias.
- Yahoo adjusted data: dividends are folded into back-adjusted prices; old adjusted prices are lower than the prices actually traded (matters for whole-share sizing and for the price filter). NSE split/bonus adjustments on Yahoo are sometimes wrong; see Data checks.
- The earnings rule (no entry within 5 trading days before results) is NOT modelled: no earnings date history was used.
- The price filter (no stocks under $5 or Rs 50) is not applied, because adjusted old prices are below the prices actually traded. One real case is missed: AMD traded under $5 in 2012-2016 (it has had no split, so its adjusted price is close to the traded price) and would have been excluded by the rule.
- Whole-share sizing uses adjusted prices, which for split stocks (NVDA, AAPL, many NSE names) are far below the traded prices of the time, so early rules-sized trades are easier to size than they really were.
- No taxes (STCG, US withholding on dividends), no FX moves (US results are in USD), no interest on cash.
- Fills at the open with fixed slippage; real fills on gap days can be worse. Stops are assumed to fill at the stop price intraday.
- Fixed published parameters, not optimised; every variant run is reported.
