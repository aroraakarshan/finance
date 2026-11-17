"""Daily market data as markdown: indices, volatility and breadth, flows, sentiment, rates/FX/commodities,
sector heat by region and notable moves, with the source and as-of date of every number.

Sources: yfinance daily closes (currency =X closes moved to their own day, see FX_NOTE); NSE India API (allIndices, live-analysis-advance, fiidiiTradeReact,
historicalOR/indicesHistory) with a browser User-Agent and home-page cookies, for India indices Yahoo
has no history for; Sina Finance daily klines for China CSI indices (Yahoo gives one row only); CNN
Fear & Greed JSON; constituent lists: Wikipedia (S&P 500, Euro Stoxx 50, Hang Seng), NSE archives
(Nifty 500), indexes.nikkei.co.jp (Nikkei 225). Moves use each series' own trading days up to --date
(a bar dated D is used only once its exchange has closed on D plus CLOSE_BUFFER, see EXCHANGES; futures, FX and
crypto only up to yesterday (UTC), so no partial bar): 1d = last close vs the one before, 1w = vs 5 trading days
earlier, 1m = vs 21 trading days earlier; 52-week high = highest daily close of the last 365 days.
NSE snapshots (breadth, FII/DII), allIndices and CNN are the latest the site gives and carry their
own timestamp. Every download is cached in ~/.local/share/finance-cache/market/; with --offline, or
when a fetch fails, the cache is used. Run with TZ=UTC (yfinance dates).

Run: TZ=UTC python -m scripts.market [--date YYYY-MM-DD] [--out FILE] [--offline]
"""
import argparse
import io
import json
import logging
import re
import time
from datetime import date, datetime
from functools import cache
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import requests

from scripts.common import PRICE_CACHE

CACHE = PRICE_CACHE.parent / "market"
OUT_DIR = Path.home() / ".local" / "share" / "superpowers" / "finance-news-first-run" / "market"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/130.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}

# (label, [(source, code), ...] tried in order, note). Sources: yf = yfinance, nse = NSE index history,
# sina = Sina Finance kline. A note starting "proxy" marks an instrument that stands in for the label.
INDICES = {
    "India": [("Nifty 50", [("yf", "^NSEI")], ""), ("Sensex", [("yf", "^BSESN")], ""),
              ("Nifty Bank", [("yf", "^NSEBANK")], ""), ("Nifty Midcap 50", [("yf", "^NSEMDCP50")], ""),
              ("Nifty Midcap 100", [("nse", "NIFTY MIDCAP 100")], ""),
              ("Nifty Smallcap 100", [("nse", "NIFTY SMALLCAP 100")], "")],
    "US": [("S&P 500", [("yf", "^GSPC")], ""), ("Nasdaq Composite", [("yf", "^IXIC")], ""),
           ("Dow Jones", [("yf", "^DJI")], ""), ("Russell 2000", [("yf", "^RUT")], "")],
    "Europe": [("Euro Stoxx 50", [("yf", "^STOXX50E")], ""), ("Stoxx Europe 600", [("yf", "^STOXX")], ""),
               ("DAX", [("yf", "^GDAXI")], ""), ("FTSE 100", [("yf", "^FTSE")], ""), ("CAC 40", [("yf", "^FCHI")], "")],
    "Japan": [("Nikkei 225", [("yf", "^N225")], ""), ("TOPIX", [("yf", "1306.T")], "proxy: NEXT FUNDS TOPIX ETF 1306.T")],
    "China/HK": [("Hang Seng", [("yf", "^HSI")], ""), ("HS China Enterprises", [("yf", "^HSCE")], ""),
                 ("CSI 300", [("sina", "sh000300")], ""), ("Shanghai Composite", [("yf", "000001.SS")], "")],
    "Other Asia": [("KOSPI", [("yf", "^KS11")], ""), ("Taiwan Weighted", [("yf", "^TWII")], ""),
                   ("Straits Times", [("yf", "^STI")], ""), ("ASX 200", [("yf", "^AXJO")], "")],
}
VOLATILITY = [("CBOE VIX", [("yf", "^VIX")], ""), ("India VIX", [("yf", "^INDIAVIX")], "")]
NO_SOURCE = ["VSTOXX (^V2TX not on Yahoo)", "Nikkei Stock Average Volatility Index (no free daily source found)",
             "India 10y G-sec yield (no free yield series; Nifty 10 yr benchmark G-sec price index shown instead)",
             "Japan 10y JGB yield (no free daily source found)"]
# kind "yield": quoted in percent, moves in basis points
RATES = [("US 10y yield", [("yf", "^TNX")], "yield"), ("US 5y yield", [("yf", "^FVX")], "yield"),
         ("US 2y yield", [("yf", "2YY=F")], "yield: CBOT 2-year yield futures; shown n/a while Yahoo's series is frozen"),
         ("US 13-week T-bill", [("yf", "^IRX")], "yield"),
         ("Nifty 10 yr benchmark G-sec", [("nse", "NIFTY 10 YR BENCHMARK G-SEC")], "proxy: price index, up = yields down"),
         ("USD/INR", [("yf", "INR=X")], ""), ("Dollar index DXY", [("yf", "DX-Y.NYB")], ""),
         ("EUR/USD", [("yf", "EURUSD=X")], ""), ("USD/JPY", [("yf", "JPY=X")], ""),
         ("USD/CNY", [("yf", "CNY=X")], "proxy: onshore CNY (CNH=X has no history on Yahoo)"),
         ("Brent", [("yf", "BZ=F")], "front-month future"), ("WTI", [("yf", "CL=F")], "front-month future"),
         ("Gold", [("yf", "GC=F")], "front-month future"), ("Silver", [("yf", "SI=F")], "front-month future"),
         ("Copper", [("yf", "HG=F")], "front-month future"), ("Bitcoin", [("yf", "BTC-USD")], "")]
REGIONS = ["US", "Europe", "India", "Japan", "China/HK"]
# sector -> region -> (instrument name, [(source, code)], proxy?)
SECTORS = {
    "Tech": {"US": ("XLK", [("yf", "XLK")], 0), "Europe": ("Stoxx 600 Technology EXV3", [("yf", "EXV3.DE")], 0),
             "India": ("Nifty IT", [("yf", "^CNXIT")], 0), "Japan": ("TOPIX-17 Electric & Precision 1625", [("yf", "1625.T")], 0),
             "China/HK": ("CSI 800 IT / CQQQ", [("sina", "sh000935"), ("yf", "CQQQ")], 0)},
    "Health care": {"US": ("XLV", [("yf", "XLV")], 0), "Europe": ("Stoxx 600 Health Care EXV4", [("yf", "EXV4.DE")], 0),
                    "India": ("Nifty Healthcare / Pharma", [("nse", "NIFTY HEALTHCARE INDEX"), ("yf", "^CNXPHARMA")], 0),
                    "Japan": ("TOPIX-17 Pharmaceutical 1621", [("yf", "1621.T")], 0),
                    "China/HK": ("CSI 800 Health Care / KURE", [("sina", "sh000933"), ("yf", "KURE")], 0)},
    "Financials": {"US": ("XLF", [("yf", "XLF")], 0), "Europe": ("Stoxx 600 Banks EXV1", [("yf", "EXV1.DE")], 1),
                   "India": ("Nifty Financial Services / Bank", [("nse", "NIFTY FINANCIAL SERVICES"), ("yf", "^NSEBANK")], 0),
                   "Japan": ("TOPIX-17 Banks 1631", [("yf", "1631.T")], 1),
                   "China/HK": ("CSI 800 Financials / HS Finance", [("sina", "sh000934"), ("yf", "^HSNF")], 0)},
    "Energy": {"US": ("XLE", [("yf", "XLE")], 0), "Europe": ("Stoxx 600 Oil & Gas EXH1", [("yf", "EXH1.DE")], 0),
               "India": ("Nifty Oil & Gas / Energy", [("nse", "NIFTY OIL & GAS"), ("yf", "^CNXENERGY")], 0),
               "Japan": ("TOPIX-17 Energy Resources 1618", [("yf", "1618.T")], 0),
               "China/HK": ("CSI 800 Energy", [("sina", "sh000928")], 0)},
    "Industrials": {"US": ("XLI", [("yf", "XLI")], 0), "Europe": ("Stoxx 600 Industrial Goods EXH4", [("yf", "EXH4.DE")], 0),
                    "India": ("Nifty Infrastructure", [("yf", "^CNXINFRA")], 1),
                    "Japan": ("TOPIX-17 Machinery 1624", [("yf", "1624.T")], 1),
                    "China/HK": ("HS Commerce & Industry", [("yf", "^HSNC")], 1)},
    "Consumer discretionary": {"US": ("XLY", [("yf", "XLY")], 0), "Europe": ("Stoxx 600 Autos EXV5", [("yf", "EXV5.DE")], 1),
                               "India": ("Nifty Auto", [("yf", "^CNXAUTO")], 1),
                               "Japan": ("TOPIX-17 Autos & Transport Equipment 1622", [("yf", "1622.T")], 1),
                               "China/HK": ("CHIQ (China consumer ETF)", [("yf", "CHIQ")], 1)},
    "Consumer staples": {"US": ("XLP", [("yf", "XLP")], 0), "Europe": ("Stoxx 600 Food & Beverage EXH3", [("yf", "EXH3.DE")], 1),
                         "India": ("Nifty FMCG", [("yf", "^CNXFMCG")], 0), "Japan": ("TOPIX-17 Foods 1617", [("yf", "1617.T")], 1),
                         "China/HK": ("CSI 800 Consumer Staples", [("sina", "sh000932")], 0)},
    "Materials/metals": {"US": ("XLB", [("yf", "XLB")], 0), "Europe": ("Stoxx 600 Basic Resources EXV6", [("yf", "EXV6.DE")], 1),
                         "India": ("Nifty Metal", [("yf", "^CNXMETAL")], 1),
                         "Japan": ("TOPIX-17 Steel & Nonferrous 1623", [("yf", "1623.T")], 1), "China/HK": ("n/a", [], 0)},
    "Utilities": {"US": ("XLU", [("yf", "XLU")], 0), "Europe": ("Stoxx 600 Utilities EXH9", [("yf", "EXH9.DE")], 0),
                  "India": ("Nifty Energy (oil, gas and power)", [("yf", "^CNXENERGY")], 1),
                  "Japan": ("TOPIX-17 Electric Power & Gas 1627", [("yf", "1627.T")], 0),
                  "China/HK": ("HS Utilities", [("yf", "^HSNU")], 0)},
    "Real estate": {"US": ("XLRE", [("yf", "XLRE")], 0), "Europe": ("Stoxx 600 Real Estate EXI5", [("yf", "EXI5.DE")], 0),
                    "India": ("Nifty Realty", [("yf", "^CNXREALTY")], 0), "Japan": ("TOPIX-17 Real Estate 1633", [("yf", "1633.T")], 0),
                    "China/HK": ("HS Properties", [("yf", "^HSNP")], 0)},
    "Communication": {"US": ("XLC", [("yf", "XLC")], 0), "Europe": ("Stoxx 600 Telecom EXV2", [("yf", "EXV2.DE")], 1),
                      "India": ("Nifty Media", [("nse", "NIFTY MEDIA")], 1),
                      "Japan": ("TOPIX-17 IT & Services, Others 1626", [("yf", "1626.T")], 1),
                      "China/HK": ("KWEB (China internet ETF)", [("yf", "KWEB")], 1)},
}
BREADTH_YF = ["RSP", "SPY"]
LISTS = {"US": "S&P 500", "India": "Nifty 500", "Europe": "Euro Stoxx 50", "Japan": "Nikkei 225", "HK": "Hang Seng"}
WIKI = "https://en.wikipedia.org/wiki/"
SECTOR_MOVE_1W, SECTOR_MOVE_1D, STOCK_MOVE_1D, VOL_RATIO, UNUSUAL_CAP = 4.0, 2.5, 7.0, 3.0, 30

# exchange -> (regular close, time zone); a bar dated D counts once now >= close on D + CLOSE_BUFFER (final prints)
EXCHANGES = {"NSE": ("15:30", "Asia/Kolkata"), "TSE": ("15:30", "Asia/Tokyo"), "HKEX": ("16:10", "Asia/Hong_Kong"),
             "SSE": ("15:00", "Asia/Shanghai"), "KRX": ("15:30", "Asia/Seoul"), "TWSE": ("13:30", "Asia/Taipei"),
             "ASX": ("16:10", "Australia/Sydney"), "SGX": ("17:00", "Asia/Singapore"), "LSE": ("16:35", "Europe/London"),
             "Xetra": ("17:35", "Europe/Berlin"), "Euronext": ("17:35", "Europe/Paris"), "BME": ("17:35", "Europe/Madrid"),
             "Milan": ("17:35", "Europe/Rome"), "Helsinki": ("18:30", "Europe/Helsinki"),
             "SIX": ("17:40", "Europe/Zurich"), "Stockholm": ("17:30", "Europe/Stockholm"),
             "Copenhagen": ("17:00", "Europe/Copenhagen"), "Oslo": ("16:25", "Europe/Oslo"),
             "Vienna": ("17:35", "Europe/Vienna"),
             "US": ("16:00", "America/New_York"), "Cboe": ("16:15", "America/New_York")}
CLOSE_BUFFER = pd.Timedelta(minutes=20)
SUFFIX_EXCHANGE = {"NS": "NSE", "BO": "NSE", "T": "TSE", "HK": "HKEX", "SS": "SSE", "SZ": "SSE", "KS": "KRX", "KQ": "KRX",
                   "TW": "TWSE", "TWO": "TWSE", "AX": "ASX", "SI": "SGX", "L": "LSE", "DE": "Xetra", "PA": "Euronext",
                   "AS": "Euronext", "BR": "Euronext", "LS": "Euronext", "IR": "Euronext", "MI": "Milan", "MC": "BME",
                   "HE": "Helsinki", "SW": "SIX", "ST": "Stockholm", "CO": "Copenhagen", "OL": "Oslo", "VI": "Vienna"}
INDEX_EXCHANGE = {"^NSEI": "NSE", "^BSESN": "NSE", "^NSEBANK": "NSE", "^NSEMDCP50": "NSE", "^INDIAVIX": "NSE",
                  "^GSPC": "US", "^IXIC": "US", "^DJI": "US", "^RUT": "US", "^TNX": "US", "^FVX": "US", "^IRX": "US",
                  "^VIX": "Cboe", "^STOXX50E": "Xetra", "^STOXX": "Xetra", "^GDAXI": "Xetra", "^FTSE": "LSE",
                  "^FCHI": "Euronext", "^N225": "TSE", "^HSI": "HKEX", "^HSCE": "HKEX", "^KS11": "KRX", "^TWII": "TWSE",
                  "^STI": "SGX", "^AXJO": "ASX"}


def exchange(src: str, code: str) -> str | None:
    """Exchange whose close ends the daily bar of `code`; None for futures, FX, crypto and anything unknown."""
    if src == "nse":
        return "NSE"
    if src == "sina":
        return "SSE"
    if code in INDEX_EXCHANGE:
        return INDEX_EXCHANGE[code]
    if code.startswith("^CNX"):
        return "NSE"
    if code.startswith("^HSN"):
        return "HKEX"
    if code.startswith("^") or "=" in code or code.endswith("-USD"):
        return None
    if "." in code:
        return SUFFIX_EXCHANGE.get(code.rsplit(".", 1)[1])
    return "US"


@cache
def last_complete(exch: str | None) -> pd.Timestamp:
    """Latest bar date whose session is over: today in the exchange's zone once close + buffer has passed, else the
    day before; for exch None (futures, FX, crypto) yesterday, as fix_fx leaves today's FX bar empty."""
    if exch is None:
        return pd.Timestamp.today().normalize() - pd.Timedelta(days=1)
    hm, tz = EXCHANGES[exch]
    now = datetime.now(ZoneInfo(tz))
    h, m = map(int, hm.split(":"))
    d = pd.Timestamp(now.date())
    return d if now >= now.replace(hour=h, minute=m, second=0, microsecond=0) + CLOSE_BUFFER else d - pd.Timedelta(days=1)


def complete(df: pd.DataFrame, src: str) -> pd.DataFrame:
    """Wide date x code table with each code's unfinished bars (see last_complete) set to NaN."""
    return df.apply(lambda s: s.where(s.index <= last_complete(exchange(src, str(s.name)))))


def get(url: str, session: requests.Session | None = None, tries: int = 3, **kw) -> requests.Response:
    for i in range(tries):
        try:
            r = (session or requests).get(url, headers=None if session else UA, timeout=30, **kw)
            r.raise_for_status()
            return r
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def merge_cache(name: str, new: pd.DataFrame | None, src: str) -> pd.DataFrame:
    """Wide date x code table cached as CACHE/<name>.csv; new values win, missing codes keep their cached history.
    Unfinished bars (see complete) are neither cached nor returned."""
    f = CACHE / f"{name}.csv"
    old = pd.read_csv(f, index_col=0, parse_dates=True) if f.exists() else pd.DataFrame()
    if new is None or new.empty:
        return complete(old, src)
    out = complete(new, src).combine_first(old) if len(old) else complete(new, src)
    CACHE.mkdir(parents=True, exist_ok=True)
    out.sort_index().to_csv(f)
    return complete(out, src)


def snapshot(name: str, fetch, offline: bool):
    """(data, how): fetch() result cached as CACHE/<name>.json; on --offline or failure the cached copy."""
    f = CACHE / f"{name}.json"
    if not offline:
        try:
            data = fetch()
            CACHE.mkdir(parents=True, exist_ok=True)
            f.write_text(json.dumps(data))
            return data, "live"
        except Exception as e:
            err = f"failed ({type(e).__name__})"
    else:
        err = "offline"
    if f.exists():
        return json.loads(f.read_text()), f"{err}; cached copy of {datetime.fromtimestamp(f.stat().st_mtime):%Y-%m-%d %H:%M}"
    return None, f"{err}; no cache"


def yf_download(codes: list[str], start: date, end: date, batch: int = 250) -> tuple[pd.DataFrame, pd.DataFrame]:
    """(close, volume) wide tables from yf.download in batches; missing codes are simply absent."""
    import yfinance as yf

    logging.getLogger("yfinance").setLevel(logging.CRITICAL)
    closes, vols = [], []
    for i in range(0, len(codes), batch):
        part = codes[i:i + batch]
        try:
            d = yf.download(part, start=f"{start}", end=f"{end}", auto_adjust=False, progress=False, threads=True)
        except Exception:
            continue
        if d is None or d.empty:
            continue
        c, v = d["Close"], d["Volume"]
        if isinstance(c, pd.Series):
            c, v = c.to_frame(part[0]), v.to_frame(part[0])
        closes.append(c)
        vols.append(v)
        time.sleep(1)
    if not closes:
        return pd.DataFrame(), pd.DataFrame()
    c, v = pd.concat(closes, axis=1), pd.concat(vols, axis=1)
    for t in (c, v):
        t.index = pd.to_datetime(t.index).tz_localize(None).normalize()
    return c.dropna(axis=1, how="all"), v.loc[:, c.dropna(axis=1, how="all").columns]


FX_NOTE = ("FX (=X) closes: Yahoo's finished FX daily bar dated D holds the close of the trading day before, so for "
           "INR, JPY and EUR day D uses the next daily bar, or the last 1h bar of D (UTC) when that bar is not finished "
           "yet (checked against ECB and FRED noon reference rates); CNY daily bars match neither the start nor the end "
           "of the day, so USD/CNY always uses the last 1h bar of D (UTC)")
FX_HOURLY = {"CNY=X"}


def fix_fx(close: pd.DataFrame) -> pd.DataFrame:
    """Yahoo currency (=X) daily closes moved to the day they belong to; see FX_NOTE."""
    import yfinance as yf

    today = pd.Timestamp.today().normalize()
    close = close.copy()
    for c in [c for c in close if c.endswith("=X")]:
        s = close[c].dropna()
        nxt = pd.Series(s.index, index=s.index).shift(-1)
        fixed = s.shift(-1).where((nxt < today) & (c not in FX_HOURLY))
        need = [d for d in fixed.index[fixed.isna()] if d < today]
        if need:
            try:
                h = yf.download(c, start=f"{min(need).date()}", end=f"{(max(need) + pd.Timedelta(days=1)).date()}",
                                interval="1h", auto_adjust=False, progress=False)["Close"].squeeze("columns").dropna()
                h.index = h.index.tz_convert("UTC").tz_localize(None)
                last = h.groupby(h.index.normalize()).last()
                fixed.loc[need] = last.reindex(need).values
            except Exception:
                pass
        close[c] = fixed.reindex(close.index)
    return close


@cache
def nse_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(UA)
    try:
        s.get("https://www.nseindia.com", timeout=20)  # sets the cookies the API needs, even on 403
    except Exception:
        pass
    return s


def nse_api(path: str):
    time.sleep(1)
    return get("https://www.nseindia.com/api/" + path, nse_session()).json()


def nse_history(index: str, day: date, since: pd.Timestamp | None = None) -> pd.Series:
    """Daily closes of an NSE index from `since` (default 365 days back) to `day`. The API returns at most
    about 70 rows per call, so it is asked in 80-day pieces."""
    end = pd.Timestamp(day)
    start = max(since, end - pd.Timedelta(days=364)) if since is not None else end - pd.Timedelta(days=364)
    out = {}
    while start <= end:
        stop = min(start + pd.Timedelta(days=79), end)
        j = nse_api(f"historicalOR/indicesHistory?indexType={requests.utils.quote(index)}"
                    f"&from={start:%d-%m-%Y}&to={stop:%d-%m-%Y}")
        out.update({pd.to_datetime(r["EOD_TIMESTAMP"], format="%d-%b-%Y"): float(r["EOD_CLOSE_INDEX_VAL"])
                    for r in j["data"]})
        start = stop + pd.Timedelta(days=1)
    return pd.Series(out, name=index, dtype=float).sort_index()


def sina_history(symbol: str) -> pd.Series:
    """Last ~300 daily closes of a China index from Sina Finance (sh000300 = CSI 300)."""
    j = get("https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData"
            f"?symbol={symbol}&scale=240&ma=no&datalen=300").json()
    return pd.Series({pd.Timestamp(r["day"]): float(r["close"]) for r in j}, name=symbol)


def fetch_series(day: date, offline: bool) -> tuple[dict[str, pd.Series], list[str]]:
    """{"src:code": closes} for every instrument in the tables; notes list fetch failures."""
    specs = [c for sec in INDICES.values() for _, cands, _ in sec for c in cands]
    specs += [c for _, cands, _ in VOLATILITY + RATES for c in cands]
    specs += [c for row in SECTORS.values() for _, cands, _ in row.values() for c in cands]
    specs += [("yf", t) for t in BREADTH_YF]
    specs = list(dict.fromkeys(specs))
    notes, out = [], {}
    end = (pd.Timestamp(day) + pd.Timedelta(days=1)).date()
    yf_codes = [c for s, c in specs if s == "yf"]
    new = None if offline else fix_fx(yf_download(yf_codes, end - pd.Timedelta(days=400), end)[0])
    yfc = merge_cache("yf-index", new, "yf")
    notes.append(FX_NOTE)
    for c in yf_codes:
        if c in yfc:
            out[f"yf:{c}"] = yfc[c]
    nse_old = merge_cache("nse-index", None, "nse")

    def nse_fetch(c):
        # only the days after the cached history (with a week of overlap), once the cache covers a year
        s = nse_old[c].dropna() if c in nse_old else pd.Series(dtype=float)
        full = len(s) and s.index[0] <= pd.Timestamp(day) - pd.Timedelta(days=360)
        return nse_history(c, day, s.index[-1] - pd.Timedelta(days=7) if full else None)

    for src, name, fn in [("nse", "nse-index", nse_fetch), ("sina", "sina-index", sina_history)]:
        got = {}
        for s, c in specs:
            if s != src or offline:
                continue
            try:
                got[c] = fn(c)
            except Exception as e:
                notes.append(f"{src} {c}: fetch failed ({type(e).__name__}), cache used if present")
        cached = merge_cache(name, pd.DataFrame(got) if got else None, src)
        for s, c in specs:
            if s == src and c in cached:
                out[f"{src}:{c}"] = cached[c]
    return out, notes


def stats(s: pd.Series | None, day: date) -> dict | None:
    """Closes and moves at the last trading day <= day (finished bars only, see merge_cache); None if no data or
    stale (>7 days)."""
    if s is None:
        return None
    s = s.dropna()
    s = s[s.index <= pd.Timestamp(day)]
    if len(s) < 2 or (pd.Timestamp(day) - s.index[-1]).days > 7 or s.iloc[-6:].nunique() == 1:
        return None  # no data, stale, or frozen (same close 6 days running)
    last, d = s.iloc[-1], s.index[-1]

    def back(n):
        return (s.iloc[-1 - n], s.index[-1 - n]) if len(s) > n else (float("nan"), None)

    yr = s[s.index > d - pd.Timedelta(days=365)]
    r = {"close": last, "date": d, "hi": yr.max(), "hi_date": yr.idxmax(), "hist_days": (d - s.index[0]).days}
    for k, n in [("d", 1), ("w", 5), ("m", 21)]:
        r[f"{k}_base"], r[f"{k}_date"] = back(n)
        r[k] = (last / r[f"{k}_base"] - 1) * 100
    return r


def pick(series: dict, cands: list, day: date) -> tuple[dict | None, str]:
    """First candidate with current data: (stats, "src code")."""
    for src, code in cands:
        st = stats(series.get(f"{src}:{code}"), day)
        if st:
            return st, f"{src} {code}"
    return None, " / ".join(f"{s} {c}" for s, c in cands) or "-"


def f2(x, nd=2) -> str:
    return "n/a" if x is None or pd.isna(x) else f"{x:,.{nd}f}"


def pc(x) -> str:
    return "n/a" if x is None or pd.isna(x) else f"{x:+.2f}"


def ds(d) -> str:
    return "n/a" if d is None or pd.isna(d) else f"{pd.Timestamp(d):%Y-%m-%d}"


def move_cells(st: dict, kind: str = "", nd: int = 2) -> list[str]:
    """'move (base close, base date)' cells for 1d, 1w, 1m; yields in basis points."""
    cells = []
    for k in "dwm":
        if kind.startswith("yield"):
            mv = "n/a" if pd.isna(st[f"{k}_base"]) else f"{(st['close'] - st[f'{k}_base']) * 100:+.0f} bp"
        else:
            mv = pc(st[k])
        cells.append(f"{mv} ({f2(st[f'{k}_base'], nd)}, {ds(st[f'{k}_date'])})")
    return cells


def table(header: list[str], rows: list[list]) -> list[str]:
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + \
           ["| " + " | ".join(str(c) for c in r) + " |" for r in rows] + [""]


def section_indices(series, day, failed) -> list[str]:
    out = ["## 1. Indices", "",
           "Moves in % with the base close and its date in brackets. 52w high: highest daily close of the last 365 days.", ""]
    hdr = ["Index", "Close", "As of", "1d %", "1w %", "1m %", "From 52w high %", "Source"]
    for region, rows in INDICES.items():
        out += [f"### {region}", ""]
        body = []
        for label, cands, note in rows:
            st, src = pick(series, cands, day)
            if not st:
                failed.append(f"{label} ({src})")
                body.append([label] + ["n/a"] * 6 + [src])
                continue
            hi = f"{pc((st['close'] / st['hi'] - 1) * 100)} ({f2(st['hi'])}, {ds(st['hi_date'])})"
            if st["hist_days"] < 360:
                hi += f" [history {st['hist_days']} days]"
            body.append([label + (f" ({note})" if note else ""), f2(st["close"]), ds(st["date"])] + move_cells(st) + [hi, src])
        out += table(hdr, body)
    return out


def section_vol_breadth(series, day, failed, offline) -> list[str]:
    out = ["## 2. Volatility and breadth", ""]
    body = []
    for label, cands, _ in VOLATILITY:
        st, src = pick(series, cands, day)
        if not st:
            failed.append(f"{label} ({src})")
            continue
        body.append([label, f2(st["close"]), ds(st["date"])] + move_cells(st) + [src])
    out += table(["Gauge", "Level", "As of", "1d %", "1w %", "1m %", "Source"], body)
    out += ["Not available: " + "; ".join(NO_SOURCE[:2]) + ".", ""]

    adv, how = snapshot("nse-advance", lambda: nse_api("live-analysis-advance"), offline)
    out += ["### India breadth", ""]
    rows = []
    if adv:
        c = adv["advance"]["count"]
        rows.append(["All NSE stocks traded", c["Advances"], c["Declines"], c["Unchange"],
                     f2(c["Advances"] / max(c["Declines"], 1)), adv["timestamp"], f"NSE api/live-analysis-advance ({how})"])
    ai, how2 = snapshot("nse-allindices", lambda: nse_api("allIndices"), offline)
    if ai:
        for r in ai["data"]:
            if r["index"] in ("NIFTY 50", "NIFTY 500", "NIFTY MIDCAP 100", "NIFTY SMALLCAP 100"):
                a, d = int(r.get("advances") or 0), int(r.get("declines") or 0)
                rows.append([r["index"], a, d, r.get("unchanged", "n/a"), f2(a / max(d, 1)), ai.get("timestamp", "n/a"),
                             f"NSE api/allIndices ({how2})"])
    out += table(["Universe", "Advances", "Declines", "Unchanged", "A/D ratio", "As of", "Source"], rows) if rows \
        else ["NSE breadth not available: " + how, ""]

    out += ["### US breadth (proxy)", "",
            "Proxy: count of the 11 SPDR sector ETFs up, and equal-weight S&P 500 (RSP) vs cap-weight (SPY).", ""]
    secs = [stats(series.get(f"yf:{SECTORS[s]['US'][1][0][1]}"), day) for s in SECTORS]
    secs = [s for s in secs if s]
    rsp, spy = stats(series.get("yf:RSP"), day), stats(series.get("yf:SPY"), day)
    rows = []
    for k, name in [("d", "1d"), ("w", "1w"), ("m", "1m")]:
        up = sum(s[k] > 0 for s in secs)
        rel = pc(rsp[k] - spy[k]) if rsp and spy else "n/a"
        rows.append([name, f"{up} of {len(secs)}", pc(rsp[k]) if rsp else "n/a", pc(spy[k]) if spy else "n/a", rel])
    as_of = ds(spy["date"]) if spy else "n/a"
    out += table(["Period", "Sector ETFs up", "RSP %", "SPY %", "RSP - SPY (pp)"], rows)
    out += [f"As of {as_of}; source yfinance (XLK..XLC, RSP, SPY).", ""]
    return out


def section_flows(offline) -> list[str]:
    out = ["## 3. Flows (India cash market, Rs crore)", ""]

    def fetch():
        return nse_api("fiidiiTradeReact")

    data, how = snapshot("nse-fiidii", fetch, offline)
    hist_f = CACHE / "fiidii-history.json"
    hist = json.loads(hist_f.read_text()) if hist_f.exists() else {}
    if data:
        for r in data:
            hist.setdefault(r["date"], {})[r["category"]] = r
        CACHE.mkdir(parents=True, exist_ok=True)
        hist_f.write_text(json.dumps(hist, indent=1, sort_keys=True))
    if not hist:
        return out + [f"Not available: NSE api/fiidiiTradeReact {how}.", ""]
    days = sorted(hist, key=lambda d: pd.to_datetime(d, format="%d-%b-%Y"))
    rows = []
    for d in days[-10:]:
        for cat in ("FII/FPI", "DII"):
            r = hist[d].get(cat)
            if r:
                rows.append([d, cat, f2(float(r["buyValue"])), f2(float(r["sellValue"])), f2(float(r["netValue"]))])
    out += table(["Date", "Category", "Buy", "Sell", "Net"], rows)
    last5 = days[-5:]
    for cat in ("FII/FPI", "DII"):
        vals = [float(hist[d][cat]["netValue"]) for d in last5 if cat in hist[d]]
        out.append(f"- {cat} net over the {len(vals)} day(s) on record ({last5[0]} to {last5[-1]}): Rs {f2(sum(vals))} cr")
    out += ["", f"Source: NSE api/fiidiiTradeReact ({how}); it gives the latest day only, so the week builds up from "
                "daily runs (kept in finance-cache/market/fiidii-history.json).", ""]
    return out


def section_sentiment(offline) -> list[str]:
    out = ["## 4. Sentiment", ""]
    h = dict(UA, Referer="https://edition.cnn.com/", Origin="https://edition.cnn.com")
    data, how = snapshot("cnn-fear-greed", lambda: requests.get(
        "https://production.dataviz.cnn.io/index/fearandgreed/graphdata", headers=h, timeout=30).json(), offline)
    if not data:
        return out + [f"CNN Fear & Greed not available: {how}.", ""]
    fg = data["fear_and_greed"]
    rows = [["Now", f2(fg["score"], 1), fg["rating"], fg["timestamp"][:10]],
            ["Previous close", f2(fg["previous_close"], 1), "", ""],
            ["1 week ago", f2(fg["previous_1_week"], 1), "", ""],
            ["1 month ago", f2(fg["previous_1_month"], 1), "", ""],
            ["1 year ago", f2(fg["previous_1_year"], 1), "", ""]]
    for k, name in [("put_call_options", "Put/call ratio component"), ("market_momentum_sp500", "S&P 500 momentum component"),
                    ("stock_price_breadth", "Price breadth component")]:
        if k in data:
            rows.append([name, f2(data[k].get("score"), 1), data[k].get("rating", ""),
                         pd.Timestamp(data[k].get("timestamp", 0), unit="ms").strftime("%Y-%m-%d") if data[k].get("timestamp") else ""])
    out += table(["CNN Fear & Greed (US, 0-100)", "Score", "Label", "As of"], rows)
    out += [f"Source: production.dataviz.cnn.io/index/fearandgreed/graphdata ({how}). India: no free official gauge; "
            "none used.", ""]
    return out


def section_rates(series, day, failed) -> list[str]:
    out = ["## 5. Rates, FX, commodities", "", "Yields in percent, their moves in basis points; others in %.", ""]
    body = []
    for label, cands, note in RATES:
        st, src = pick(series, cands, day)
        if not st:
            failed.append(f"{label} ({src})")
            body.append([label, "n/a", "n/a", "n/a", "n/a", "n/a", src])
            continue
        lab = label + (f" ({note.removeprefix('yield').lstrip(': ')})" if note.removeprefix("yield") else "")
        nd = 4 if st["close"] < 10 and not note.startswith("yield") else 2
        body.append([lab, f2(st["close"], nd), ds(st["date"])] + move_cells(st, note, nd) + [src])
    out += table(["Instrument", "Level", "As of", "1d", "1w", "1m", "Source"], body)
    out += ["Not available: " + "; ".join(NO_SOURCE[2:]) + ".", ""]
    return out


def sector_cells(series, day) -> dict:
    """{(sector, region): (stats, src, instrument, proxy)}"""
    return {(sec, reg): (*pick(series, cands, day), name, proxy)
            for sec, row in SECTORS.items() for reg, (name, cands, proxy) in row.items()}


def asof(cells, reg) -> str:
    """Last close date(s) of a region's sector cells: one date, or 'first to last' when they differ."""
    d = sorted({ds(st["date"]) for (_, r), (st, *_) in cells.items() if r == reg and st})
    return "n/a" if not d else d[0] if len(d) == 1 else f"{d[0]} to {d[-1]}"


def section_sectors(cells, failed) -> list[str]:
    out = ["## 6. Sector heat", "", "Price change in %; * = proxy (nearest available sector index or ETF). "
           "Instruments and as-of dates in the last table.", ""]
    for k, name in [("w", "1-week"), ("m", "1-month"), ("d", "1-day")]:
        rows = []
        for sec in SECTORS:
            r = [sec]
            for reg in REGIONS:
                st, _, _, proxy = cells[(sec, reg)]
                r.append("n/a" if not st else pc(st[k]) + ("*" if proxy else ""))
            rows.append(r)
        rows.append(["As of"] + [asof(cells, reg) for reg in REGIONS])
        out += [f"### {name} %", ""] + table(["Sector"] + REGIONS, rows)
    ranked = sorted([(st["w"], sec, reg, name, st["date"]) for (sec, reg), (st, _, name, _) in cells.items() if st], reverse=True)
    out += ["### Strongest and weakest cells (1-week)", ""]
    out += table(["", "Sector", "Region", "Instrument", "1w %", "As of"],
                 [["Top", s, r, n, pc(v), ds(d)] for v, s, r, n, d in ranked[:3]] +
                 [["Bottom", s, r, n, pc(v), ds(d)] for v, s, r, n, d in ranked[-3:]])
    rows = []
    for sec in SECTORS:
        r = [sec]
        for reg in REGIONS:
            st, src, name, _ = cells[(sec, reg)]
            if not st and name != "n/a":
                failed.append(f"sector {sec}/{reg} ({src})")
            r.append(f"{name}: {src}, {ds(st['date'])}" if st else f"n/a ({src})")
        rows.append(r)
    out += ["### Instruments used (source, last close date)", ""] + table(["Sector"] + REGIONS, rows)
    return out


def read_wiki_table(page: str, need: set[str]) -> pd.DataFrame:
    for t in pd.read_html(io.StringIO(get(WIKI + page).text)):
        if need <= set(map(str, t.columns)):
            return t
    raise ValueError(f"no table with {need} on {page}")


def nikkei_list() -> pd.DataFrame:
    html = get("https://indexes.nikkei.co.jp/en/nkave/index/component?idx=nk225").text
    rows = []
    for sec, body in re.findall(r'idx-section-subheading">(.*?)</h3>(.*?)</table>', html, re.S):
        for code, name in re.findall(r"<td>\s*(\w+)\s*</td>\s*<td>\s*(.*?)\s*</td>", body, re.S):
            rows.append((f"{code}.T", name, sec.strip()))
    return pd.DataFrame(rows, columns=["symbol", "name", "sector"])


def fetch_list(market: str) -> pd.DataFrame:
    if market == "US":
        t = read_wiki_table("List_of_S%26P_500_companies", {"Symbol", "Security", "GICS Sector"})
        return pd.DataFrame({"symbol": t.Symbol.str.replace(".", "-"), "name": t.Security, "sector": t["GICS Sector"]})
    if market == "India":
        t = pd.read_csv(io.StringIO(get("https://archives.nseindia.com/content/indices/ind_nifty500list.csv").text))
        return pd.DataFrame({"symbol": t.Symbol + ".NS", "name": t["Company Name"], "sector": t.Industry})
    if market == "Europe":
        t = read_wiki_table("EURO_STOXX_50", {"Ticker", "Name", "Sector"})
        return pd.DataFrame({"symbol": t.Ticker.str.strip().str.replace(" ", "-"), "name": t.Name, "sector": t.Sector})
    if market == "Japan":
        return nikkei_list()
    t = read_wiki_table("Hang_Seng_Index", {"Ticker", "Name", "Sub-index"})
    code = t.Ticker.str.extract(r"(\d+)")[0].astype(int)
    return pd.DataFrame({"symbol": code.map("{:04d}.HK".format), "name": t.Name, "sector": t["Sub-index"]})


def constituents(market: str, offline: bool) -> tuple[pd.DataFrame | None, str]:
    """Index member list, refreshed weekly; cached as CACHE/list-<market>.csv."""
    f = CACHE / f"list-{market}.csv"
    fresh = f.exists() and time.time() - f.stat().st_mtime < 7 * 86400
    if not offline and not fresh:
        try:
            t = fetch_list(market).dropna(subset=["symbol"]).drop_duplicates("symbol")
            if len(t) < 30:
                raise ValueError(f"only {len(t)} rows")
            CACHE.mkdir(parents=True, exist_ok=True)
            t.to_csv(f, index=False)
            return t, f"fetched {date.today()}"
        except Exception as e:
            how = f"fetch failed ({type(e).__name__}: {e})"
            if not f.exists():
                return None, how
            return pd.read_csv(f), f"{how}; cached list"
    if f.exists():
        return pd.read_csv(f), f"cached list of {datetime.fromtimestamp(f.stat().st_mtime):%Y-%m-%d}"
    return None, "offline; no cached list"


def stock_moves(market: str, lst: pd.DataFrame, day: date, offline: bool) -> tuple[pd.DataFrame, str]:
    """One row per member: close, 1d %, 1w %, volume / 20-day average volume, at the market's last trading day."""
    end = (pd.Timestamp(day) + pd.Timedelta(days=1)).date()
    c = v = None
    if not offline:
        c, v = yf_download(list(lst.symbol), end - pd.Timedelta(days=75), end)
    c, v = merge_cache(f"yf-{market}-close", c, "yf"), merge_cache(f"yf-{market}-volume", v, "yf")
    c = c[c.index <= pd.Timestamp(day)]
    v = v.reindex(index=c.index, columns=c.columns)
    if c.empty:
        return pd.DataFrame(), "no prices"
    last_day = c.dropna(how="all").index[-1]
    rows = []
    for s in c.columns:
        cs = c[s].dropna()
        if len(cs) < 6 or cs.index[-1] != last_day:
            continue
        vs = v[s].reindex(cs.index)
        avg = vs.iloc[-21:-1].mean()
        rows.append({"symbol": s, "close": cs.iloc[-1], "d": (cs.iloc[-1] / cs.iloc[-2] - 1) * 100,
                     "w": (cs.iloc[-1] / cs.iloc[-6] - 1) * 100,
                     "vr": vs.iloc[-1] / avg if avg and avg > 0 else float("nan")})
    m = pd.DataFrame(rows)
    if m.empty:
        return m, "no prices"
    m = m.merge(lst, on="symbol", how="left")
    return m, f"{len(m)} of {len(lst)} members priced, last trading day {last_day:%Y-%m-%d}"


def section_notable(cells, day, offline, failed) -> list[str]:
    out = ["## 7. Notable moves", "", f"Stocks: yfinance daily closes and volumes in local currency; Vol x = day volume / "
           f"average of the 20 trading days before. Unusual: |1d| >= {STOCK_MOVE_1D:g}% or Vol x >= {VOL_RATIO:g} "
           f"(at most {UNUSUAL_CAP} per market, largest move first).", ""]
    out += [f"### Sector rallies and selloffs (|1w| >= {SECTOR_MOVE_1W:g}% or |1d| >= {SECTOR_MOVE_1D:g}%)", ""]
    rows = [[sec, reg, name, pc(st["d"]), pc(st["w"]), ds(st["date"])] for (sec, reg), (st, _, name, _) in cells.items()
            if st and (abs(st["w"]) >= SECTOR_MOVE_1W or abs(st["d"]) >= SECTOR_MOVE_1D)]
    rows.sort(key=lambda r: -abs(float(r[4])))
    out += table(["Sector", "Region", "Instrument", "1d %", "1w %", "As of"], rows) if rows else ["None.", ""]
    hdr = ["Symbol", "Name", "Sector", "Close", "1d %", "1w %", "Vol x"]

    def rowsof(df):
        return [[r.symbol, r.name, r.sector, f2(r.close), pc(r.d), pc(r.w), f2(r.vr, 1)] for r in df.itertuples()]

    for market, index in LISTS.items():
        lst, how = constituents(market, offline)
        out += [f"### {market}: {index}", ""]
        if lst is None:
            failed.append(f"{index} member list ({how})")
            out += [f"Not available: member list {how}.", ""]
            continue
        m, mhow = stock_moves(market, lst, day, offline)
        out += [f"List: {how}; prices: {mhow}.", ""]
        if m.empty:
            failed.append(f"{index} prices ({mhow})")
            continue
        missing = sorted(set(lst.symbol) - set(m.symbol))
        if missing:
            out += [f"Not priced on the last day ({len(missing)}): {', '.join(missing[:40])}{' ...' if len(missing) > 40 else ''}", ""]
        for k, name in [("d", "1-day"), ("w", "1-week")]:
            out += [f"Top 10 gainers, {name}", ""] + table(hdr, rowsof(m.nlargest(10, k)))
            out += [f"Top 10 losers, {name}", ""] + table(hdr, rowsof(m.nsmallest(10, k)))
        u = m[(m.d.abs() >= STOCK_MOVE_1D) | (m.vr >= VOL_RATIO)]
        u = u.reindex(u.d.abs().sort_values(ascending=False).index).head(UNUSUAL_CAP)
        out += [f"Unusual moves ({len(u)})", ""] + (table(hdr, rowsof(u)) if len(u) else ["None.", ""])
    return out


def cross_check(series, day, offline) -> list[str]:
    """Yahoo closes vs NSE allIndices 'last' for the same day (NSE gives only its latest session)."""
    ai, how = snapshot("nse-allindices", lambda: nse_api("allIndices"), offline)
    if not ai:
        return []
    pairs = [("NIFTY 50", "yf:^NSEI"), ("NIFTY BANK", "yf:^NSEBANK"), ("NIFTY IT", "yf:^CNXIT"), ("INDIA VIX", "yf:^INDIAVIX")]
    nse = {r["index"]: r for r in ai["data"]}
    rows = []
    for idx, key in pairs:
        st = stats(series.get(key), day)
        if st and idx in nse:
            rows.append([idx, f2(st["close"]), ds(st["date"]), f2(nse[idx]["last"]), ai.get("timestamp", "n/a"),
                         pc((st["close"] / nse[idx]["last"] - 1) * 100)])
    return ["## Cross-check (Yahoo vs NSE)", ""] + table(
        ["Index", "Yahoo close", "Yahoo date", "NSE last", "NSE timestamp", "Diff %"], rows) + \
        [f"NSE api/allIndices ({how}); differences matter only when the dates are the same session.", ""]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--date", type=date.fromisoformat, default=date.today(), help="use closes up to this day (default today)")
    ap.add_argument("--out", type=Path, help="output file (default <work folder>/market/data-<date>.md)")
    ap.add_argument("--offline", action="store_true", help="use cached data only (no network)")
    args = ap.parse_args()
    day, out_f = args.date, args.out or OUT_DIR / f"data-{args.date}.md"
    t0 = time.time()
    series, notes = fetch_series(day, args.offline)
    failed: list[str] = []
    cells = sector_cells(series, day)
    lines = [f"# Market data {day}", "",
             f"Generated {datetime.now():%Y-%m-%d %H:%M} by scripts/market.py{' (offline)' if args.offline else ''}. "
             "Closes up to the date above; each row shows its own last trading day. A bar counts only once its exchange "
             f"has closed that day (+{CLOSE_BUFFER.seconds // 60} min), so Asia can be a day ahead of Europe and the US; "
             "futures, FX and crypto use the last full UTC day.", ""]
    lines += section_indices(series, day, failed)
    lines += section_vol_breadth(series, day, failed, args.offline)
    lines += section_flows(args.offline)
    lines += section_sentiment(args.offline)
    lines += section_rates(series, day, failed)
    lines += section_sectors(cells, failed)
    lines += section_notable(cells, day, args.offline, failed)
    lines += cross_check(series, day, args.offline)
    lines += ["## Failures and notes", ""] + [f"- {x}" for x in failed + notes] + ([] if failed or notes else ["- none"]) + [""]
    out_f.parent.mkdir(parents=True, exist_ok=True)
    out_f.write_text("\n".join(lines))
    print(f"wrote {out_f} in {time.time() - t0:.0f} s")
    for x in failed + notes:
        print("NOTE", x)


if __name__ == "__main__":
    main()
