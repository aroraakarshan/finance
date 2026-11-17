"""Daily scan universe: liquid US (S&P 500, Nasdaq 100, S&P 400) and India (Nifty 200) stocks.

.venv/bin/python -m trading.universe build     # lists + download into the shared cache + filter + write files
.venv/bin/python -m trading.universe refresh   # latest bars of the included names into the live cache
"""
import importlib.util, io, os, sys, time, unicodedata
from datetime import datetime
from pathlib import Path
import pandas as pd, requests

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "universe"
AGENT_LOG = Path.home() / ".local/share/superpowers/finance-trader-backtests/agents/universe.log"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
WIKI = "https://en.wikipedia.org/wiki/"
US_SRC = [("S&P 500", WIKI + "List_of_S%26P_500_companies", "Symbol", "Security", "GICS Sector"),
          ("Nasdaq 100", WIKI + "List_of_NASDAQ-100_companies", "Ticker", "Company", "ICB Industry[2]"),
          ("S&P 400", WIKI + "List_of_S%26P_400_companies", "Symbol", "Security", "GICS Sector")]
NSE = "https://archives.nseindia.com/content/indices/ind_nifty200list.csv"
US_MIN_PX, US_MIN_VOL = 5, 1_000_000
IN_MIN_PX, IN_MIN_VAL = 50, 20e7  # Rs 20 crore
BATCH = 40


def lg(step, what):
    AGENT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(AGENT_LOG, "a") as f:
        f.write(f"{datetime.now():%H:%M} {step}: {what}\n")
    print(f"{step}: {what}", flush=True)


def engine():
    if "engine" not in sys.modules:
        spec = importlib.util.spec_from_file_location("engine", ROOT / "backtests" / "engine.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        sys.modules["engine"] = m
    return sys.modules["engine"]


def get(url):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    return r.text


def us_list():
    rows = {}
    for src, url, sym, name, sec in US_SRC:
        t = next(t for t in pd.read_html(io.StringIO(get(url))) if sym in t.columns and name in t.columns)
        for _, r in t.iterrows():
            s = str(r[sym]).strip().replace(".", "-")
            e = rows.setdefault(s, dict(symbol=s, name=r[name], source=[], sector=""))
            e["source"].append(src)
            if src != "Nasdaq 100" or not e["sector"]:
                e["sector"] = r[sec]
    return pd.DataFrame([dict(r, source="+".join(r["source"])) for r in rows.values()])


def india_list():
    t = pd.read_csv(io.StringIO(get(NSE)))
    return pd.DataFrame(dict(symbol=t.Symbol.str.strip() + ".NS", name=t["Company Name"], source="Nifty 200", sector=t.Industry))


def fetch(tickers, step, live=False, end=None, batch=BATCH):
    """Download via engine.download (which backs off on 429, a bad crumb or an empty batch). Returns tickers still missing."""
    E = engine()
    has = lambda t: E.fname(t, live).exists()
    todo = [t for t in tickers if live or not has(t)]
    lg(step, f"{len(tickers)} tickers, {len(todo)} to download")
    E.download(todo, batch=batch, live=live, end=end or E.END)
    return [t for t in tickers if not has(t)]


def measure(t, us):
    E = engine()
    d = E.load(t)
    if d is None or d.empty:
        return dict(close=None, avg_volume=None, avg_value=None, history_start=None, included="no", reason="no data")
    tail = d.dropna(subset=["C"]).tail(50)
    r = dict(close=round(d.C.iloc[-1], 2), avg_volume=round(tail.V.mean()), avg_value=round((tail.C * tail.V).mean()),
             history_start=d.index[0].date(), included="no", reason="")
    if d.index[-1] != pd.Timestamp(E.LAST):
        r["reason"] = f"last bar {d.index[-1].date()}"
    elif len(d) < 50:
        r["reason"] = "under 50 bars"
    elif r["close"] <= (US_MIN_PX if us else IN_MIN_PX):
        r["reason"] = "price under $5" if us else "price under Rs 50"
    elif us and r["avg_volume"] <= US_MIN_VOL:
        r["reason"] = "50d avg volume under 1M"
    elif not us and r["avg_value"] <= IN_MIN_VAL:
        r["reason"] = "50d avg value under Rs 20 cr"
    else:
        r["included"] = "yes"
    return r


def write_index(tabs, failed, minutes):
    E = engine()
    us, ind = tabs["us"], tabs["india"]
    n = lambda t: int((t.included == "yes").sum())
    L = ["# Scan universe", "", "## Summary",
         f"- US: {n(us)} of {len(us)} names pass; India: {n(ind)} of {len(ind)} pass (data to {E.LAST} close).",
         f"- US filter: close > ${US_MIN_PX} and 50-day average volume > 1,000,000 shares.",
         f"- India filter: close > Rs {IN_MIN_PX} and 50-day average traded value > Rs 20 crore (Nifty 200 names are already liquid, so this only drops thin ones).",
         f"- Failed or empty downloads after one retry: {len(failed)}. Built {datetime.now():%Y-%m-%d} in {minutes:.0f} min.",
         "", "## Counts", "", "| Market | Source | Names | Included |", "|---|---|---|---|"]
    for k, t in (("US", us), ("India", ind)):
        for s in sorted({x for v in t.source for x in v.split("+")}):
            m = t[t.source.str.split("+").apply(lambda v: s in v)]
            L.append(f"| {k} | {s} | {len(m)} | {n(m)} |")
        L.append(f"| {k} | all (unique) | {len(t)} | {n(t)} |")
    L += ["", "| Market | Exclusion reason | Names |", "|---|---|---|"]
    for k, t in (("US", us), ("India", ind)):
        x = t[t.included == "no"]
        reasons = x.reason.str.replace(r"last bar \S+", "last bar before " + E.LAST, regex=True).value_counts()
        L += [f"| {k} | {r} | {c} |" for r, c in reasons.items()] or [f"| {k} | none | 0 |"]
    L += ["", "## Failed downloads", "", ", ".join(failed) if failed else "None.", "",
          "## Survivorship bias", "",
          "These are today's index members. Stocks that were dropped, merged or went bust since 2010 are missing, so a backtest "
          "on this list over past years looks better than reality (it only holds the survivors). Use it for the daily scan; treat "
          "long backtests on it as an upper bound.", "",
          "## Files and rebuild", "",
          "- `us.csv`, `india.csv`: symbol, name, source index, sector, close, avg_volume (50 days), avg_value (50 days, local currency), "
          "history_start, included, reason.",
          f"- Prices: shared cache `{E.CACHE}` (`<symbol>.csv`, `&` and `^` become `_`); `refresh` writes the latest bars to `{E.CACHE / 'live'}`.",
          "- Rebuild: `.venv/bin/python -m trading.universe build` (lists from Wikipedia and NSE, downloads only names not yet cached, "
          "filters on the engine's LAST close). Daily: `.venv/bin/python -m trading.universe refresh`.",
          "- Sources: Wikipedia (S&P 500, S&P 400 with GICS sector; Nasdaq 100 with ICB industry), NSE `ind_nifty200list.csv` (industry)."]
    (OUT / "index.md").write_text("\n".join(L) + "\n")


def to_ascii(s):
    s = str(s).replace("\u2013", "-").replace("\u2014", "-")
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def write_csv(t, k):
    t = t.assign(**{c: t[c].map(to_ascii) for c in ("name", "sector") if c in t})
    t.to_csv(OUT / f"{k}.csv", index=False)


def build():
    t0 = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    lists = {"us": us_list(), "india": india_list()}
    lg("build", f"lists: US {len(lists['us'])}, India {len(lists['india'])}")
    failed = []
    for k, t in lists.items():
        miss = fetch(list(t.symbol), f"download-{k}")
        if miss:
            lg(f"download-{k}", f"retrying {len(miss)}: {' '.join(miss)}")
            miss = fetch(miss, f"retry-{k}", batch=10)
        failed += miss
    for k, t in lists.items():
        m = pd.DataFrame([measure(s, k == "us") for s in t.symbol])
        lists[k] = pd.concat([t.reset_index(drop=True), m], axis=1)
        write_csv(lists[k], k)
    write_index(lists, failed, (time.time() - t0) / 60)
    lg("build", f"done in {(time.time() - t0) / 60:.1f} min; failed {failed}")


def included():
    return [s for k in ("us", "india") for s in pd.read_csv(OUT / f"{k}.csv").query("included == 'yes'").symbol]


def refresh():
    """Daily: add recent bars for the included names (engine.refresh_recent; full history only where Yahoo re-adjusted old prices)."""
    t0 = time.time()
    names = included()
    lg("refresh", f"{len(names)} included names")
    redo = engine().refresh_recent(names, batch=BATCH)
    lg("refresh", f"done in {(time.time() - t0) / 60:.1f} min; full history for {len(redo)}")


if __name__ == "__main__":
    {"build": build, "refresh": refresh}[sys.argv[1] if len(sys.argv) > 1 else "build"]()
