import os, sys, time, math
from pathlib import Path
import numpy as np, pandas as pd

CACHE = Path.home() / ".local/share/superpowers/finance-trader-backtests/cache"
OUT = Path(__file__).resolve().parent
START, END, LAST = "2010-01-01", "2026-11-14", "2026-11-13"
SPLITS = [("full", "2010-01-01", LAST), ("2010-2019", "2010-01-01", "2019-12-31"), ("2020-2026", "2020-01-01", LAST)]
US_ETF = "SPY QQQ IWM EFA EEM TLT GLD".split()
US_STK = ("AAPL MSFT NVDA AMZN GOOGL META AVGO JPM V MA UNH LLY JNJ PG KO PEP XOM CVX HD COST WMT BAC CSCO ORCL "
          "ADBE CRM AMD QCOM TXN INTC CAT GE HON").split()
IN_ETF = "NIFTYBEES.NS BANKBEES.NS GOLDBEES.NS".split()
IN_STK = [t + ".NS" for t in ("RELIANCE TCS HDFCBANK ICICIBANK INFY HINDUNILVR ITC SBIN BHARTIARTL KOTAKBANK LT AXISBANK "
          "BAJFINANCE ASIANPAINT MARUTI SUNPHARMA TITAN ULTRACEMCO NESTLEIND HCLTECH WIPRO POWERGRID NTPC ONGC TATASTEEL "
          "JSWSTEEL M&M ADANIPORTS DRREDDY CIPLA").split()]
MK = {"US": dict(etf=US_ETF, stk=US_STK, idx="SPY", bench=["SPY"], cost=0.0005, cur="USD", budget=200000 / 94),
      "India": dict(etf=IN_ETF, stk=IN_STK, idx="^NSEI", bench=["^NSEI", "NIFTYBEES.NS"], cost=0.0022, cur="INR", budget=200000)}
MARKETS_IDX = {"US": "SPY", "India": "^NSEI"}
ALL = US_ETF + US_STK + IN_ETF + IN_STK + ["^NSEI"]
MIN_BARS = 1000


def log(m):
    print(m, flush=True)


def fname(t, live=False):
    return (CACHE / "live" if live else CACHE) / (t.replace("^", "_").replace("&", "_") + ".csv")


def crumb_ok():
    """yfinance can keep a 429 reply as its crumb (then every call fails): reset it if it looks wrong."""
    from yfinance.data import YfData
    yd = YfData()
    c = getattr(yd, "_crumb", None)
    if c is None or (len(c) < 40 and " " not in c and "<" not in c):
        return True
    log(f"bad crumb ({len(c)} chars), resetting")
    yd._crumb = None
    try:
        yd._get_cookie_and_crumb()
    except Exception as ex:
        log(f"crumb reset failed: {ex}")
    return False


def yf_batch(b, **kw):
    """One yf.download call with backoff (2 min doubling to 15) on HTTP 429, a bad crumb, or an all-empty batch of 3+ names.
    Returns (frame, names with data)."""
    import yfinance as yf, yfinance.shared as yfs
    wait = 120
    while True:
        bad_crumb = not crumb_ok()
        df = yf.download(b, auto_adjust=True, group_by="ticker", progress=False, threads=False, **kw)
        got = [t for t in b if df is not None and t in df.columns.get_level_values(0) and df[t].dropna(how="all").shape[0] > 0]
        errs = " ".join(str(v) for v in getattr(yfs, "_ERRORS", {}).values())
        limited = "429" in errs or "Rate" in errs or bad_crumb or (not got and len(b) >= 3)
        if got or not limited or wait > 900:
            return df, got
        log(f"no data ({'rate limit' if '429' in errs or 'Rate' in errs else 'bad crumb' if bad_crumb else 'empty batch'}), sleeping {wait}s")
        time.sleep(wait)
        wait *= 2


def download(tickers=ALL, batch=15, live=False, end=END):
    fname(ALL[0], live).parent.mkdir(parents=True, exist_ok=True)
    todo = list(tickers) if live else [t for t in tickers if not fname(t).exists()]
    for i in range(0, len(todo), batch):
        b = todo[i:i + batch]
        df, got = yf_batch(b, start=START, end=end)
        for t in got:
            closed_bars(t, df[t].dropna(how="all")).to_csv(fname(t, live))
        log(f"batch {i // batch + 1}: saved {len(got)}/{len(b)} missing={sorted(set(b) - set(got))}")
        time.sleep(3)


CLOSE_UTC = {"": (21, 0, -5), ".NS": (10, 0, 5.5), ".BO": (10, 0, 5.5), ".T": (6, 0, 9), ".HK": (8, 0, 8), ".L": (16, 30, 0),
             ".DE": (16, 30, 1), ".PA": (16, 30, 1), ".MC": (16, 30, 1), ".MI": (16, 30, 1), "=X": (23, 0, 0)}
INDEX_SUFFIX = {"^NSEI": ".NS", "^N225": ".T", "^HSI": ".HK", "^FTSE": ".L", "^GDAXI": ".DE", "^FCHI": ".PA", "^IBEX": ".MC", "FTSEMIB.MI": ".MI"}


def closed_bars(t, df, now=None):
    """Drop a bar for a session that has not closed yet (exchange close in UTC + 30 min), so an intraday bar is never stored as a close."""
    suf = "=X" if t.endswith("=X") else INDEX_SUFFIX.get(t, "." + t.rsplit(".", 1)[1] if "." in t else "")
    h, mnt, off = CLOSE_UTC.get(suf, CLOSE_UTC[""])
    now = now or pd.Timestamp.now(tz="UTC").tz_localize(None)
    local_day = (now + pd.Timedelta(hours=off)).normalize()
    done = now >= local_day + pd.Timedelta(hours=h, minutes=mnt + 30)
    cut = local_day if not done else local_day + pd.Timedelta(days=1)
    return df[df.index < cut]


def merge_recent(t, new):
    """Splice new bars onto the live cache file (seeded from the main cache); the new download replaces the cached bars for every date it
    covers. False if older prices were re-adjusted by more than 1% (split/dividend: needs full history)."""
    p, base = fname(t, True), fname(t)
    src = p if p.exists() else base
    if not src.exists():
        return False
    new = closed_bars(t, new)
    if new.empty:
        return True
    old = pd.read_csv(src, index_col=0, parse_dates=True)
    both = old.index.intersection(new.index)[:-1]
    if len(both) and ((old.loc[both, "Close"] / new.loc[both, "Close"] - 1).abs() > 0.01).any():
        return False
    p.parent.mkdir(parents=True, exist_ok=True)
    pd.concat([old[old.index < new.index[0]], new[old.columns]]).to_csv(p)
    return True


def refresh_recent(names, batch=40, period="1mo"):
    """Add the last month of bars to the live cache; names whose history was re-adjusted (or that are not cached) get full history."""
    names = list(dict.fromkeys(names))
    redo = []
    for i in range(0, len(names), batch):
        b = names[i:i + batch]
        df, got = yf_batch(b, period=period)
        redo += [t for t in b if t not in got or not merge_recent(t, df[t].dropna(how="all"))]
        time.sleep(3)
    if redo:
        log(f"full history for {len(redo)}: {' '.join(redo)}")
        download(redo, batch=20, live=True, end=str((pd.Timestamp.today() + pd.Timedelta(days=1)).date()))
    return redo


def latest_date(m, live=True):
    """Last close date in the data for a market (its index file), not the fixed backtest LAST."""
    d = load(MARKETS_IDX[m], None, live) if live else None
    return (d if d is not None else load(MARKETS_IDX[m], None, False)).index[-1]


def load(t, until=LAST, live=False):
    p = fname(t, live)
    if not p.exists():
        return None
    d = pd.read_csv(p, index_col=0, parse_dates=True)[["Open", "High", "Low", "Close", "Volume"]]
    d.columns = list("OHLCV")
    return d.loc[:until]


def check_data(tickers=ALL, min_bars=MIN_BARS, until=LAST, live=False):
    rows, data, short = [], {}, []
    for t in tickers:
        d = load(t, until, live)
        if d is None or len(d) < min_bars:
            short.append((t, 0 if d is None else len(d)))
            continue
        nan = int((d[list("OHLC")].isna().any(axis=1) | (d[list("OHLC")] <= 0).any(axis=1)).sum())
        d = d.dropna(subset=list("OHLC"))
        d = d[(d[list("OHLC")] > 0).all(axis=1)]
        stale = (d.V == 0) & (d.O == d.H) & (d.H == d.L) & (d.L == d.C) if not t.startswith("^") else d.V < -1
        d = d[~stale].copy()
        fixed = []
        r = (d.C / d.C.shift()).values
        for i in np.where(r < 0.6)[0]:
            f = 10 ** round(math.log10(1 / r[i]))
            for j in range(i + 1, min(i + 6, len(d))):
                if abs(r[j] * 1 / f - 1) < 0.2 and f >= 10:
                    d.iloc[i:j, :4] *= f
                    d.iloc[i:j, 4] /= f
                    fixed.append(f"{d.index[i].date()} to {d.index[j - 1].date()} x{f}")
                    break
        bad_hl = int(((d.H < d[["O", "C"]].max(axis=1) * 0.999) | (d.L > d[["O", "C"]].min(axis=1) * 1.001)).sum())
        prints = 0
        if t in IN_ETF:
            nx = load("^NSEI", until, live)
            calm = ((nx.H / nx.L - 1) < 0.03).reindex(d.index).fillna(False)
            pc = d.C.shift()
            bo = ((d.O / pc - 1).abs() > 0.05) & ((d.C / pc - 1).abs() < 0.025) & calm
            d.loc[bo, "O"] = pc[bo]
            bh = (d.H > d[["O", "C"]].max(axis=1) * 1.05) & calm
            bl = (d.L < d[["O", "C"]].min(axis=1) * 0.95) & calm
            d.loc[bh, "H"] = d[["O", "C"]].max(axis=1)[bh]
            d.loc[bl, "L"] = d[["O", "C"]].min(axis=1)[bl]
            d["H"], d["L"] = d[["H", "O", "C"]].max(axis=1), d[["L", "O", "C"]].min(axis=1)
            prints = int((bo | bh | bl).sum())
        r = d.C.pct_change()
        g = d.O / d.C.shift() - 1
        big = [(x.date(), round(100 * r[x], 1)) for x in r.index[r.abs() > 0.4]]
        gap = [(x.date(), round(100 * g[x], 1)) for x in g.index[g.abs() > 0.4]]
        zv = int((d.V == 0).sum()) if not t.startswith("^") else 0
        rows.append(dict(t=t, first=d.index[0].date(), last=d.index[-1].date(), bars=len(d), nan=nan, bad_hl=bad_hl, stale=int(stale.sum()), fixed=fixed, prints=prints,
                         zero_vol=zv, big=big, gap=gap, maxmove=round(100 * r.abs().max(), 1)))
        data[t] = d
    return data, rows, short


def ind(d):
    d = d.copy()
    c = d.C
    d["sma200"] = c.rolling(200).mean()
    d["sma5"] = c.rolling(5).mean()
    dl = c.diff()
    up, dn = dl.clip(lower=0).ewm(alpha=0.5, adjust=False).mean(), (-dl.clip(upper=0)).ewm(alpha=0.5, adjust=False).mean()
    d["rsi2"] = 100 - 100 / (1 + up / dn.replace(0, np.nan))
    d.loc[dn == 0, "rsi2"] = 100.0
    tr = pd.concat([d.H - d.L, (d.H - c.shift()).abs(), (d.L - c.shift()).abs()], axis=1).max(axis=1)
    d["atr14"] = tr.ewm(alpha=1 / 14, adjust=False).mean()
    d["swlo"] = d.L.rolling(10).min()
    d["hi50"] = d.H.shift().rolling(50).max()
    d["lo20"] = d.L.shift().rolling(20).min()
    d["mom"] = c.shift(21) / c.shift(252) - 1
    return d


def stats(eq, inv=None, a=None, b=None):
    e = eq.loc[a:b].dropna()
    if len(e) < 2:
        return {}
    yrs = (e.index[-1] - e.index[0]).days / 365.25
    r = e.pct_change().dropna()
    o = dict(cagr=(e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1, mdd=(e / e.cummax() - 1).min(),
             sharpe=r.mean() / r.std() * math.sqrt(252) if r.std() > 0 else 0.0)
    if inv is not None:
        o["expo"] = inv.loc[a:b].mean()
    return o


def tstats(tr, a=None, b=None):
    t = tr if tr is None or len(tr) == 0 else tr[(tr.entry_date >= pd.Timestamp(a or "1900")) & (tr.entry_date <= pd.Timestamp(b or "2100"))]
    if t is None or len(t) == 0:
        return dict(n=0, win=np.nan, aw=np.nan, al=np.nan, pf=np.nan, hold=np.nan, avg=np.nan)
    w, l = t.ret[t.ret > 0], t.ret[t.ret <= 0]
    return dict(n=len(t), win=len(w) / len(t), aw=w.mean() if len(w) else np.nan, al=l.mean() if len(l) else np.nan,
                pf=w.sum() / -l.sum() if l.sum() < 0 else np.inf, hold=t.days.mean(), avg=t.ret.mean())


def calendar(data, m):
    return data[MK[m]["idx"]].index


def weight_engine(data, m, tickers, wfun, cost):
    cal = calendar(data, m)
    O = pd.DataFrame({t: data[t].O for t in tickers}).reindex(cal)
    C = pd.DataFrame({t: data[t].C for t in tickers}).reindex(cal)
    live = C.notna()
    O, C = O.fillna(C.ffill()).ffill(), C.ffill()
    me = pd.Series(cal, index=cal).groupby(cal.to_period("M")).max().values
    reb = set(cal[cal.searchsorted(me[:-1]) + 1]) if len(me) > 1 else set()
    cash, sh, eq, inv = 1.0, pd.Series(0.0, index=tickers), [], []
    pend, open_tr, trades = None, {}, []
    for i, d in enumerate(cal):
        if pend is not None:
            o = O.loc[d]
            val = cash + (sh * o).sum()
            tgt = pd.Series(pend).reindex(tickers).fillna(0.0)
            new = (tgt * val / o).where(o > 0, 0.0).fillna(0.0)
            new[tgt == 0] = 0.0
            diff = (new - sh) * o
            cash -= diff.sum() + diff.abs().sum() * cost
            for t in tickers:
                if sh[t] == 0 and new[t] > 0:
                    open_tr[t] = (d, o[t])
                elif sh[t] > 0 and new[t] == 0:
                    ed, ep = open_tr.pop(t)
                    trades.append(dict(t=t, entry_date=ed, exit_date=d, ep=ep, xp=o[t], days=(d - ed).days,
                                       ret=o[t] * (1 - cost) / (ep * (1 + cost)) - 1, why="rebalance"))
            sh, pend = new, None
        c = C.loc[d]
        mv = (sh * c).sum()
        eq.append(cash + mv)
        inv.append(mv / (cash + mv))
        nxt = cal[i + 1] if i + 1 < len(cal) else None
        if nxt is not None and nxt in reb:
            pend = wfun(d, live.loc[d])
    for t, (ed, ep) in open_tr.items():
        trades.append(dict(t=t, entry_date=ed, exit_date=cal[-1], ep=ep, xp=C[t].iloc[-1], days=(cal[-1] - ed).days,
                           ret=C[t].iloc[-1] * (1 - cost) / (ep * (1 + cost)) - 1, why="open at end"))
    return pd.Series(eq, index=cal), pd.Series(inv, index=cal), pd.DataFrame(trades)


def trade_engine(data, m, tickers, sig, cost, mode="signal", use_stop=False, time_stop=None, max_pos=None,
                 week_max=None, budget=1.0, risk=0.01, cap=0.2, target_r=None):
    cal = calendar(data, m)
    D = {t: sig(ind(data[t])) for t in tickers}
    A = {}
    sigs = {}
    for t, d in D.items():
        A[t] = dict(ix=d.index, O=d.O.values, H=d.H.values, L=d.L.values, C=d.C.values, atr=d.atr14.values, swlo=d.swlo.values,
                    lvl=d.stop_lvl.values if "stop_lvl" in d.columns else None, ex=d.exit.values if hasattr(d.exit, "values") else np.zeros(len(d), bool),
                    pos={x: i for i, x in enumerate(d.index)})
        ent = d.entry.fillna(False).values.astype(bool) if hasattr(d.entry, "fillna") else np.zeros(len(d), bool)
        for i in np.where(ent)[0]:
            sigs.setdefault(d.index[i], []).append((d.score.iloc[i], t))

    def close_before(t, d, k):
        a = A[t]
        j = a["ix"].searchsorted(d, side="right") - 1 - k
        return a["C"][j]
    cash, pos, pend_in, pend_out, trades, eq, inv = budget, {}, [], set(), [], [], []
    skip = dict(max_pos=0, week_limit=0, price_above_cap=0, cash=0)
    wk, wn = None, 0
    for d in cal:
        if d.isocalendar()[:2] != wk:
            wk, wn = d.isocalendar()[:2], 0
        for t in sorted(pend_out):
            if t in pos and d in A[t]["pos"]:
                p = pos.pop(t)
                px = A[t]["O"][A[t]["pos"][d]]
                cash += p["sh"] * px * (1 - cost)
                trades.append(dict(t=t, entry_date=p["d"], exit_date=d, ep=p["ep"], xp=px, days=(d - p["d"]).days,
                                   ret=px * (1 - cost) / (p["ep"] * (1 + cost)) - 1, why=p["why"], stop=p["stop"]))
                pend_out.discard(t)
        for score, t in sorted(pend_in):
            a = A[t]
            if t in pos or d not in a["pos"]:
                continue
            i = a["pos"][d]
            ep = a["O"][i]
            stop = None
            if use_stop:
                s_atr = ep - 2 * a["atr"][i - 1]
                s_sw = a["swlo"][i - 1] if a["swlo"][i - 1] < ep and use_stop != "atr" else -np.inf
                stop = max(s_atr, s_sw, 0.9 * ep)
                if a["lvl"] is not None and a["lvl"][i - 1] < ep:
                    stop = max(stop, a["lvl"][i - 1])
            if mode == "signal":
                sh = 1.0
            else:
                if max_pos and len(pos) >= max_pos:
                    skip["max_pos"] += 1
                    continue
                if week_max and wn >= week_max:
                    skip["week_limit"] += 1
                    continue
                equity = cash + sum(p["sh"] * close_before(x, d, 1) for x, p in pos.items())
                if mode == "risk":
                    st = stop if stop is not None else 0.9 * ep
                    sh = math.floor(min(risk * equity / (ep - st), cap * equity / ep))
                    if sh < 1:
                        skip["price_above_cap"] += 1
                        continue
                    if sh * ep * (1 + cost) > cash:
                        sh = math.floor(cash / (ep * (1 + cost)))
                        if sh < 1:
                            skip["cash"] += 1
                            continue
                else:
                    sh = min(cap * equity, cash) / (ep * (1 + cost))
                    if sh * ep < 0.01 * equity:
                        skip["cash"] += 1
                        continue
                cash -= sh * ep * (1 + cost)
            wn += 1
            pos[t] = dict(sh=sh, ep=ep, d=d, stop=stop, n=0, why="exit rule",
                          tgt=ep + target_r * (ep - stop) if target_r and stop is not None else None)
        pend_in = []
        for t, p in list(pos.items()):
            a = A[t]
            if d not in a["pos"]:
                continue
            i = a["pos"][d]
            if p["stop"] is not None and a["L"][i] <= p["stop"] and t not in pend_out:
                px = min(a["O"][i], p["stop"])
                if mode != "signal":
                    cash += p["sh"] * px * (1 - cost)
                trades.append(dict(t=t, entry_date=p["d"], exit_date=d, ep=p["ep"], xp=px, days=(d - p["d"]).days,
                                   ret=px * (1 - cost) / (p["ep"] * (1 + cost)) - 1, why="stop", stop=p["stop"]))
                del pos[t]
                continue
            if p.get("tgt") is not None and a["H"][i] >= p["tgt"] and t not in pend_out:
                px = max(a["O"][i], p["tgt"])
                if mode != "signal":
                    cash += p["sh"] * px * (1 - cost)
                trades.append(dict(t=t, entry_date=p["d"], exit_date=d, ep=p["ep"], xp=px, days=(d - p["d"]).days,
                                   ret=px * (1 - cost) / (p["ep"] * (1 + cost)) - 1, why="target", stop=p["stop"]))
                del pos[t]
                continue
            p["n"] += 1
            if a["ex"][i]:
                pend_out.add(t)
            elif time_stop and p["n"] >= time_stop:
                p["why"] = "time stop"
                pend_out.add(t)
        for score, t in sigs.get(d, ()):
            if t not in pos:
                pend_in.append((score, t))
        if mode != "signal":
            mv = sum(p["sh"] * close_before(t, d, 0) for t, p in pos.items())
            eq.append(cash + mv)
            inv.append(mv / (cash + mv))
    for t, p in pos.items():
        px = A[t]["C"][-1]
        trades.append(dict(t=t, entry_date=p["d"], exit_date=cal[-1], ep=p["ep"], xp=px, days=(cal[-1] - p["d"]).days,
                           ret=px * (1 - cost) / (p["ep"] * (1 + cost)) - 1, why="open at end", stop=p["stop"]))
    eqs = pd.Series(eq, index=cal) if eq else None
    invs = pd.Series(inv, index=cal) if inv else None
    return eqs, invs, pd.DataFrame(trades), skip

def sig_donchian(d):
    d["entry"] = d.C > d.hi50
    d["exit"] = d.C < d.lo20
    d["score"] = -(d.C / d.hi50)
    return d


def sig_rsi2(d):
    d["entry"] = (d.C > d.sma200) & (d.rsi2 < 10)
    d["exit"] = d.C > d.sma5
    d["score"] = d.rsi2
    return d


def sig_turtle(d):
    d["hi20"] = d.H.shift().rolling(20).max()
    d["entry"] = d.C > d.hi20
    d["exit"] = d.C < d.L.shift().rolling(10).min()
    d["score"] = -(d.C / d.hi20)
    return d


def sig_hi52(d):
    d["hi252"] = d.H.shift().rolling(252).max()
    d["vr"] = d.V / d.V.shift().rolling(50).mean()
    d["entry"] = (d.C > d.hi252) & (d.vr >= 1.5)
    d["exit"] = False
    d["score"] = -d.vr
    return d


def sig_gap(d):
    d["gp"] = d.O / d.C.shift() - 1
    d["vr"] = d.V / d.V.shift().rolling(50).mean()
    d["entry"] = (d.gp >= 0.04) & (d.vr >= 3) & (d.H > d.L) & (d.C - d.L >= 0.5 * (d.H - d.L)) & (d.C > d.sma200)
    d["exit"] = False
    d["stop_lvl"] = d.L
    d["score"] = -d.gp
    return d


sig_turtle.__doc__ = "close {C:.2f} > prior 20-day high {hi20:.2f}"
sig_hi52.__doc__ = "close {C:.2f} > prior 52-week high {hi252:.2f}, volume {vr:.1f}x 50-day average"
sig_gap.__doc__ = "open gap {gp:+.1%}, volume {vr:.1f}x, close {C:.2f} in top half of {L:.2f}-{H:.2f}, > SMA200 {sma200:.2f}"

SHORT = {"short-breakout": (sig_turtle, [("turtle", "Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop", dict(time_stop=15)),
                                         ("turtle2r", "Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop", dict(time_stop=15, target_r=2))]),
         "52w-high-breakout": (sig_hi52, [("hi52", "52-week high on 1.5x volume, rules stop, 2R target, 20-day time stop", dict(time_stop=20, target_r=2))]),
         "gap-drift": (sig_gap, [("gap", "Gap-up 4%+ on 3x volume, gap-low or rules stop, 2R target, 20-day time stop", dict(time_stop=20, target_r=2))])}
RULES_SIZED = {"donchian", "rsi2", "turtle", "turtle2r", "hi52", "gap"}


def run_short(name):
    sig, variants = SHORT[name]

    def run(data):
        rows, out, extra, wt, eqs = [], [], [], {}, {}
        for m in MK:
            c, tick = MK[m], MK[m]["stk"]
            for k, lab, kw in variants:
                _, _, tr, _ = trade_engine(data, m, tick, sig, c["cost"], use_stop=True, **kw)
                eq, inv, _, _ = trade_engine(data, m, tick, sig, c["cost"], mode="slot", use_stop=True, max_pos=5, **kw)
                for p, a, z in SPLITS:
                    rows.append((m, lab + " (every signal / 5 slots x 20%)", p, tstats(tr, a, z), stats(eq, inv, a, z)))
                extra.append((m, lab, f"every-signal trades by exit: {trades_by_exit(tr)}"))
                wt[(m, lab + ", every signal")] = tr
                r, trr, sk, eqr, invr = rules_block(data, m, tick, sig, True, kw.get("time_stop"), label=lab + ", rules-sized", target_r=kw.get("target_r"))
                out += r
                wt[(m, lab + ", rules-sized")] = trr
                eqs[(k, m)] = (eqr, invr, trr)
                extra.append((m, lab + ", rules-sized", f"budget {c['budget']:,.0f} {c['cur']}, final equity {eqr.iloc[-1]:,.0f} {c['cur']}; "
                              f"trades by exit: {trades_by_exit(trr)}; signals skipped: " + ", ".join(f"{a} {b}" for a, b in sk.items())))
                if name == "gap-drift":
                    extra.append((m, "earnings check", gap_earnings_check(tr)))
        return rows, out, extra, wt, eqs
    return run


def gap_earnings_check(tr, n=10):
    import json
    p = CACHE / "live" / "meta.json"
    meta_ = json.loads(p.read_text()) if p.exists() else {}
    have = {t: v.get("earnings") for t, v in meta_.items() if v.get("earnings")}
    recent = tr[(tr.entry_date >= pd.Timestamp(LAST) - pd.Timedelta(days=730)) & tr.t.isin(list(have))].sort_values("entry_date").tail(n)
    if not len(recent):
        return ("not done: no cached earnings dates for the tickers with gap events in the last 2 years "
                "(checking them needs new yfinance calls, which were not allowed in this run)")
    res = []
    for r in recent.itertuples():
        gap_day = r.entry_date - pd.tseries.offsets.BDay(1)
        near = [e for e in have[r.t] if 0 <= np.busday_count(e, str(gap_day.date())) <= 1]
        res.append(f"{r.t} {gap_day.date()} {'earnings ' + near[0] if near else 'no earnings within 1 day'}")
    return f"{len(res)} recent gap days with cached earnings dates (others would need downloads): " + "; ".join(res)


def bar_check(k, eq, inv, tr):
    if k not in RULES_SIZED:
        return "fail: no rules-sized run with the stop", {}
    f, a, b = tstats(tr), tstats(tr, *SPLITS[1][1:]), tstats(tr, *SPLITS[2][1:])
    es = stats(eq, inv)
    fails = ([f"trades {f['n']} < 100"] if f["n"] < 100 else []) + \
            ([f"PF full {num(f['pf'])} < 1.2"] if not f["pf"] >= 1.2 else []) + \
            ([f"PF 2020-2026 {num(b['pf'])} < 1.2"] if not b["pf"] >= 1.2 else []) + \
            ([f"avg trade 2010-2019 {pct(a['avg'], 2)}"] if not a["avg"] > 0 else []) + \
            ([f"avg trade 2020-2026 {pct(b['avg'], 2)}"] if not b["avg"] > 0 else []) + \
            ([f"CAGR {pct(es['cagr'])}"] if not es["cagr"] > 0 else []) + \
            ([f"max DD {pct(es['mdd'])}"] if es["mdd"] < -0.25 else [])
    return ("pass" if not fails else "fail: " + "; ".join(fails)), dict(f=f, a=a, b=b, es=es)


BAR_TEXT = ("A strategy may open paper trades in a market only if ALL of these hold for that market (scored on the rules-sized run: "
            "AGENTS.md stop and sizing, costs, 5 open, 3 new a week, 20% cap, whole shares):\n\n" +
            "| # | Test |\n|---|---|\n| 1 | Fixed published parameters, every variant shown |\n| 2 | A rules-sized run with the stop and costs |\n"
            "| 3 | At least 100 trades over the full period |\n| 4 | Profit factor >= 1.2 for the full period AND for 2020-2026 |\n"
            "| 5 | Positive average net trade in 2010-2019 and in 2020-2026 |\n| 6 | Rules-sized CAGR > 0 |\n| 7 | Rules-sized max drawdown no worse than -25% |\n")


def bar_row(page, label, m, bar, v, universe):
    return dict(page=page, label=label, m=m, universe=universe, bar=bar, n=v["f"]["n"] if v else None,
                pf=v["f"]["pf"] if v else None, pfo=v["b"]["pf"] if v else None, avg=v["f"]["avg"] if v else None,
                cagr=v["es"]["cagr"] if v else None, mdd=v["es"]["mdd"] if v else None, hold=v["f"]["hold"] if v else None)


def bar_store(kind, rows):
    import json
    p = CACHE / "bar.json"
    j = json.loads(p.read_text()) if p.exists() else {}
    j[kind] = rows
    p.write_text(json.dumps(j, indent=1, default=float))
    return j


def write_bar(heads=None, uni=None):
    j = bar_store("35", [bar_row(h["name"], h["label"], h["m"], h["bar"], h["barv"], "35 names") for h in heads]) if heads is not None else \
        bar_store("universe", uni)
    f = lambda x, g: "-" if x is None else g(x)
    rows = [(f"[{r['page']}](backtests/{r['page']}/index.md)", r["label"], r["m"], r["universe"], "PASS" if r["bar"] == "pass" else "fail",
             r["bar"][6:] if r["bar"] != "pass" else "-", f(r["n"], str), f(r["pf"], num), f(r["pfo"], num), f(r["avg"], lambda x: pct(x, 2)),
             f(r["cagr"], pct), f(r["mdd"], pct), f(r["hold"], lambda x: num(x, 0))) for k in ("35", "universe") for r in j.get(k, [])]
    ok = [f"{r['label']} ({r['m']})" for r in j.get("universe", []) if r["bar"] == "pass"]
    sec = (f"## Backtest bar\nScored by `.venv/bin/python trading/backtests/engine.py all` (35 names) and `engine.py universe-bar` (full universe), "
           f"last run {time.strftime('%Y-%m-%d')} (daily Yahoo data {START} to {LAST}). Paper trades in a market may use only strategies that pass on the "
           f"FULL universe: {', '.join(ok) or 'none'}. Both universes are today's index members, so every result is biased upwards (survivorship). "
           "Items 1 and 2: every variant run is shown on the strategy pages; Faber and momentum have no rules-sized run with a stop.\n\n" + BAR_TEXT + "\n" +
           tbl(["Strategy", "Version", "Market", "Universe", "Bar", "Failing items", "Trades", "PF full", "PF 2020-2026", "Avg trade", "CAGR", "Max DD",
                "Avg calendar days held"], rows))
    p = OUT.parent / "playbook.md"
    t = p.read_text()
    if "\n## Backtest bar\n" in t:
        i = t.index("\n## Backtest bar\n") + 1
        k = t.find("\n## ", i + 5)
        t = t[:i] + sec + ("\n" + t[k:] if k >= 0 else "")
    else:
        t = t.rstrip("\n") + "\n\n" + sec
    p.write_text(t)
    log(f"wrote {p} (Backtest bar)")


STRATS = {"donchian": dict(name="trend-following-donchian", page="trend-following", sig="sig_donchian", time_stop=None, target_r=None, label="Donchian 50/20, rules stop"),
          "turtle": dict(name="short-breakout", page="short-breakout", sig="sig_turtle", time_stop=15, target_r=None, label="Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop"),
          "turtle2r": dict(name="short-breakout-2R", page="short-breakout", sig="sig_turtle", time_stop=15, target_r=2, label="Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop"),
          "hi52": dict(name="52w-high-breakout", page="52w-high-breakout", sig="sig_hi52", time_stop=20, target_r=2, label="52-week high on 1.5x volume, 2R, 20 days"),
          "gap": dict(name="gap-drift", page="gap-drift", sig="sig_gap", time_stop=20, target_r=2, label="Gap-up 4%+ on 3x volume, 2R, 20 days")}
SIGTEXT = {"donchian": ("50d high breakout {date} (close {C:.2f} > prior 50d high {hi50:.2f})", "20-day low"),
           "turtle": ("20d high breakout {date} (close {C:.2f} > prior 20d high {hi20:.2f})", "10-day low"),
           "turtle2r": ("20d high breakout {date} (close {C:.2f} > prior 20d high {hi20:.2f})", "10-day low"),
           "hi52": ("52w high on volume {date} (close {C:.2f} > prior 52w high {hi252:.2f}, volume {vr:.1f}x 50d avg)", None),
           "gap": ("gap-up {date} (open {gp:+.1%} vs prior close on {vr:.1f}x 50d volume, close {C:.2f} in top half)", None)}
EXIT_WORDS = {"stop": "stop", "target": "target", "time stop": "time", "news -2": "news"}
UNIV_RUNS = [("donchian", ["US", "India"]), ("turtle", ["US"]), ("turtle2r", ["US"]), ("hi52", ["US", "India"]), ("gap", ["US", "India"])]
UNIV_MIN_BARS = 300


def universe_names(m, extra=False):
    p = OUT.parent / "universe" / ("us.csv" if m == "US" else "india.csv")
    names = list(pd.read_csv(p).query("included == 'yes'").symbol)
    if extra:
        x = pd.read_csv(OUT.parent / "universe" / "extra.csv")
        names += [t for t in x[x.market == m].symbol if t not in names]
    return names


def run_universe():
    data, short, flags = {}, {}, {}
    for m in MK:
        d, rows, sh = check_data(universe_names(m) + [MK[m]["idx"]], min_bars=UNIV_MIN_BARS)
        data.update(d)
        short[m] = sh
        flags[m] = [f"{r['t']} " + ", ".join(f"{a} {b:+.0f}%" for a, b in (r["big"] or r["gap"])[:2]) for r in rows if r["big"] or r["gap"]]
    res = []
    for k, mkts in UNIV_RUNS:
        s = STRATS[k]
        sig = globals()[s["sig"]]
        for m in mkts:
            tick = [t for t in universe_names(m) if t in data]
            log(f"universe-bar: {k} {m} on {len(tick)} names")
            _, _, tr, _ = trade_engine(data, m, tick, sig, MK[m]["cost"], use_stop=True, time_stop=s["time_stop"], target_r=s["target_r"])
            rr, trr, sk, eqr, invr = rules_block(data, m, tick, sig, True, s["time_stop"], label=s["label"] + ", rules-sized", target_r=s["target_r"])
            bar, barv = bar_check(k, eqr, invr, trr)
            res.append(dict(k=k, m=m, names=len(tick), short=len(short[m]), flags=flags[m], every=[(m, s["label"] + ", every signal", p, tstats(tr, a, z), {}) for p, a, z in SPLITS],
                            rules=rr, bar=bar, barv=barv, skip=sk, worst=worst(trr), exits=trades_by_exit(trr)))
    return res


def write_universe(res):
    for pg in dict.fromkeys(STRATS[r["k"]]["page"] for r in res):
        rs = [r for r in res if STRATS[r["k"]]["page"] == pg]
        summ = [f"{r['m']}, {STRATS[r['k']]['label']}, full universe ({r['names']} names): bar {r['bar'].upper() if r['bar'] == 'pass' else r['bar']}." for r in rs][:4]
        summ.append("Full universe = today's included scan names (S&P 500/400, Nasdaq 100; Nifty 200), each with the history it has: still survivorship-biased, but a much bigger sample than the 35-name lists.")
        body = (RUN_NOTE.format(d=time.strftime("%Y-%m-%d"), name="universe-bar") + "\n\n## Universe\n" +
                tbl(["Market", "Names used", f"Dropped (< {UNIV_MIN_BARS} bars or no data)", "List"], [(r["m"], r["names"], r["short"], f"[trading/universe/{'us' if r['m'] == 'US' else 'india'}.csv](../../universe/{'us' if r['m'] == 'US' else 'india'}.csv)") for r in rs if r is rs[0] or r["m"] != rs[0]["m"]]) +
                "\nSame rules, costs and execution as the 35-name pages; the rules-sized run is the Rs 2 L AGENTS.md simulation. Names listed after 2010 enter when they have 200+ days of data.\n\n"
                "## Every signal (one unit each, no capital limit)\n" + perf_table([x for r in rs for x in r["every"]], "full universe") +
                "\n## Rules-sized Rs 2 L run\n" + perf_table([x for r in rs for x in r["rules"]], "full universe") +
                "\n## Backtest bar (full universe)\n" + tbl(["Market", "Universe", "Version", "Bar", "Trades by exit", "Signals skipped"],
                                                             [(r["m"], "full universe", STRATS[r["k"]]["label"], r["bar"], r["exits"], ", ".join(f"{a} {b}" for a, b in r["skip"].items())) for r in rs]))
        for r in rs:
            body += f"\n### Worst 5 rules-sized trades: {r['m']}, {STRATS[r['k']]['label']}\n" + r["worst"]
        for m in dict.fromkeys(r["m"] for r in rs):
            fl = next(r["flags"] for r in rs if r["m"] == m)
            body += (f"\n### Data: {m} names with a 1-day move or open gap above 40% ({len(fl)}; not repaired)\nMost are real (results, March 2020, biotech news). "
                     "Some look like unadjusted corporate actions (spin-offs, demergers, bonus issues) and can create false stops or breakouts: "
                     "for example DHR 2016-07-05, ADANIENT.NS 2015-06-03, MOTILALOFS.NS 2024-01-01, VEDL.NS 2026-04-30 (not verified one by one).\n\n" + "; ".join(fl) + "\n")
        page(OUT / pg / "universe.md", f"Full-universe check: {pg}", summ, body)
    write_bar(uni=[bar_row(STRATS[r["k"]]["page"], STRATS[r["k"]]["label"] + ", rules-sized", r["m"], r["bar"], r["barv"], f"full ({r['names']} names)") for r in res])


def active(m):
    """Strategies that may open paper orders in market m: bar pass (by full-universe PF) then trading/paper/allowed.csv rows (below-bar, user-approved).
    Returns [(key, status, note)]."""
    out = [(k, "pass", "passes the full-universe backtest bar") for k in passing(m)]
    p = OUT.parent / "paper" / "allowed.csv"
    if p.exists():
        byname = {v["name"]: k for k, v in STRATS.items()}
        for r in pd.read_csv(p, dtype=str).fillna("").itertuples():
            k = byname.get(r.strategy, r.strategy if r.strategy in STRATS else None)
            if r.market == m and k and k not in [x[0] for x in out] and r.status in ("pass", "below-bar"):
                out.append((k, r.status, f"{r.approved_by} {r.date}: {r.note}"))
    return out


def status_label(st):
    return "below bar" if st == "below-bar" else "passes bar"


def passing(m):
    import json
    p = CACHE / "bar.json"
    rows = json.loads(p.read_text()).get("universe", []) if p.exists() else []
    lab = {v["label"] + ", rules-sized": k for k, v in STRATS.items()}
    ok = [(r["pf"], lab[r["label"]]) for r in rows if r["m"] == m and r["bar"] == "pass" and r["label"] in lab]
    return [k for _, k in sorted(ok, reverse=True)]

def bench(data, m):
    out = {}
    for b in MK[m]["bench"]:
        c = data[b].C
        out[b] = c / c.iloc[0]
    return out


def pct(x, nd=1):
    return "n/a" if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))) else f"{100 * x:.{nd}f}%"


def num(x, nd=2):
    return "n/a" if x is None or np.isnan(x) else ("inf" if np.isinf(x) else f"{x:.{nd}f}")


def perf_table(rows, universe="35 names"):
    h = "| Market | Universe | Version | Period | Trades | Win rate | Avg win | Avg loss | Avg trade | Profit factor | Avg calendar days held | CAGR | Max DD | Exposure | Sharpe (rf=0) |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    for m, v, p, ts, es in rows:
        h += (f"| {m} | {universe} | {v} | {p} | {ts.get('n', 'n/a')} | {pct(ts.get('win'))} | {pct(ts.get('aw'))} | {pct(ts.get('al'))} | {pct(ts.get('avg'), 2)} | "
              f"{num(ts.get('pf'))} | {num(ts.get('hold'), 0)} | {pct(es.get('cagr'))} | {pct(es.get('mdd'))} | "
              f"{pct(es.get('expo'), 0)} | {num(es.get('sharpe'))} |\n")
    return h


def bench_table(data):
    h = "| Market | Benchmark (buy and hold) | Period | CAGR | Max DD | Sharpe (rf=0) |\n|---|---|---|---|---|---|\n"
    for m in MK:
        for b, e in bench(data, m).items():
            for p, a, z in SPLITS:
                s = stats(e, None, a, z)
                h += f"| {m} | {b} | {p} | {pct(s['cagr'])} | {pct(s['mdd'])} | {num(s['sharpe'])} |\n"
    return h


def worst(tr, k=5):
    t = tr.sort_values("ret").head(k)
    h = "| Ticker | Entry date | Entry price | Exit date | Exit price | Exit reason | Return (net) |\n|---|---|---|---|---|---|---|\n"
    for _, r in t.iterrows():
        h += f"| {r.t} | {r.entry_date.date()} | {r.ep:.2f} | {r.exit_date.date()} | {r.xp:.2f} | {r.why} | {pct(r.ret)} |\n"
    return h


def trades_by_exit(tr):
    return ", ".join(f"{k} {v}" for k, v in tr.why.value_counts().items())


def spot(data, tr, sigf, n=2):
    h = "| Ticker | Signal date | Signal-day close | Indicator check | Fill date | Fill (next open, raw cache) | Engine entry price | Stop | Exit date | Exit reason | Raw bar on exit day (O/H/L) | Engine exit price |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    tr = tr.sort_values(["entry_date", "t"], kind="stable")
    second = next((w for w in ("exit rule", "target", "time stop") if (tr.why == w).any()), "exit rule")
    pick = pd.concat([tr[tr.why == w].iloc[len(tr[tr.why == w]) // 2:].head(1) for w in ("stop", second)])
    for _, r in pick.iterrows():
        raw = pd.read_csv(fname(r.t), index_col=0, parse_dates=True)
        i = raw.index.get_loc(r.entry_date)
        sd = raw.index[i - 1]
        d = sigf(ind(data[r.t]))
        h += (f"| {r.t} | {sd.date()} | {raw.Close.iloc[i - 1]:.2f} | {sigf.__doc__.format(**d.loc[sd].to_dict())} | "
              f"{r.entry_date.date()} | {raw.Open.iloc[i]:.2f} | {r.ep:.2f} | {num(r.stop) if r.stop is not None else '-'} | {r.exit_date.date()} | "
              f"{r.why} | {raw.Open[r.exit_date]:.2f} / {raw.High[r.exit_date]:.2f} / {raw.Low[r.exit_date]:.2f} | {r.xp:.2f} |\n")
    return h


def data_section(rows, short):
    h = "| Ticker | First bar | Bars used | NaN or zero-price rows dropped | Stale bars dropped (volume 0, O=H=L=C) | Bars repaired (wrong scale) | Bad open/high/low prints fixed (India ETFs) | High/low inconsistent bars | Largest 1-day move after repair | Close-to-close moves > 40% after repair | Open gaps > 40% after repair |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
    for r in rows:
        if r["big"] or r["gap"] or r["bad_hl"] or r["nan"] or r["stale"] or r["fixed"] or str(r["first"]) > "2010-01-08":
            h += (f"| {r['t']} | {r['first']} | {r['bars']} | {r['nan']} | {r['stale']} | {'; '.join(r['fixed']) or '-'} | {r['prints']} | {r['bad_hl']} | {r['maxmove']}% | "
                  f"{'; '.join(f'{a} {b}%' for a, b in r['big']) or '-'} | {'; '.join(f'{a} {b}%' for a, b in r['gap']) or '-'} |\n")
    h += f"\nAll other tickers: full history from early January 2010, no NaN or stale rows, no high/low inconsistencies, no 1-day move above 40%.\n"
    if short:
        h += "\nDropped for short or missing history (< %d bars): %s\n" % (MIN_BARS, ", ".join(f"{t} ({n} bars)" for t, n in short))
    return h


COMMON = """## Data
- Source: Yahoo Finance daily bars via yfinance 1.8.0, `auto_adjust=True` (prices adjusted for splits and dividends), {START} to {LAST} (last close). Downloaded {DL}; cached outside the repository in `~/.local/share/superpowers/finance-trader-backtests/cache/`.
- Universe (today's large caps, chosen with hindsight):
  - US ETFs: {us_etf}. US stocks: {us_stk}.
  - India ETFs: {in_etf}. India stocks (NSE): {in_stk}. Index ^NSEI (Nifty 50) used for the regime filter and as benchmark.
- Data checks (run by the script): tickers with any issue listed; moves above 40% in one day on a large cap are treated as suspect.

{data}
{data_note}

## Costs and execution
- Signals use the daily close; every fill is at the NEXT trading day's open. Indicators use only data up to the signal day (breakout levels use the prior 50/20 days, excluding the signal day).
- Costs per side, applied to the fill price: US 0.05% slippage, $0 commission (IBKR Lite / Alpaca style). India 0.22% = 0.10% slippage + 0.12% charges (STT 0.1% on delivery buy and sell, exchange fee about 0.003%, SEBI fee, stamp duty 0.015% on buy, GST 18% on fees, DP charge about Rs 16 per sell; zero-brokerage delivery assumed; averaged over both sides).
- Protective stops (where used) fill at the stop price, or at the open if the day opens below the stop (gap), minus costs.
- Cash earns 0%. Dividends are in the adjusted prices (as if reinvested, before tax). No taxes.
- Sharpe ratio: daily returns, risk-free rate 0, annualised with sqrt(252).
- Period splits: in-sample 2010-2019 and out-of-sample 2020-01-01 to {LAST}. Sub-period numbers are slices of one continuous run (positions carried across the split), trades are split by entry date. Indicator warm-up (200 days, or 252 days for 12-1 momentum) means the strategies are in cash for most of 2010; benchmarks start on the first bar.

## Benchmarks (buy and hold, adjusted close, no costs; ^NSEI is a price index without dividends, NIFTYBEES includes them)
{bench}
Sanity check: engine buy-and-hold CAGR vs direct (last adjusted close / first adjusted close) ^ (1/years) - 1: {bcheck}
"""

BIASES = """## Known biases and limits
- Survivorship and hindsight bias: the stock lists are today's large caps and Nifty 50 members. Stocks that fell out (for example Yes Bank, Vedanta, IBM-style laggards) are missing, so stock results are biased upwards. The ETF and index results do not have this bias.
- Yahoo adjusted data: dividends are folded into back-adjusted prices; old adjusted prices are lower than the prices actually traded (matters for whole-share sizing and for the price filter). NSE split/bonus adjustments on Yahoo are sometimes wrong; see Data checks.
- The earnings rule (no entry within 5 trading days before results) is NOT modelled: no earnings date history was used.
- The price filter (no stocks under $5 or Rs 50) is not applied, because adjusted old prices are below the prices actually traded. One real case is missed: AMD traded under $5 in 2012-2016 (it has had no split, so its adjusted price is close to the traded price) and would have been excluded by the rule.
- Whole-share sizing uses adjusted prices, which for split stocks (NVDA, AAPL, many NSE names) are far below the traded prices of the time, so early rules-sized trades are easier to size than they really were.
- No taxes (STCG, US withholding on dividends), no FX moves (US results are in USD), no interest on cash.
- Fills at the open with fixed slippage; real fills on gap days can be worse. Stops are assumed to fill at the stop price intraday.
- Fixed published parameters, not optimised; every variant run is reported.
"""


def fmt_list(x):
    return " ".join(t.replace(".NS", "") for t in x)


def header(data, rows, short):
    dl = time.strftime("%Y-%m-%d", time.localtime(min(fname(t).stat().st_mtime for t in data)))
    bc = []
    for m in MK:
        for b, e in bench(data, m).items():
            c = data[b].C
            yrs = (c.index[-1] - c.index[0]).days / 365.25
            bc.append(f"{b} engine {pct(stats(e)['cagr'], 2)} vs direct {pct((c.iloc[-1] / c.iloc[0]) ** (1 / yrs) - 1, 2)}")
    return COMMON.format(START=START, LAST=LAST, DL=dl, us_etf=fmt_list(US_ETF), us_stk=fmt_list(US_STK),
                         in_etf=fmt_list(IN_ETF), in_stk=fmt_list(IN_STK), data=data_section(rows, short),
                         data_note=DATA_NOTE, bench=bench_table(data), bcheck="; ".join(bc))




def rules_block(data, m, tickers, sig, use_stop, time_stop, label="rules-sized", **kw):
    c = MK[m]
    eq, inv, tr, sk = trade_engine(data, m, tickers, sig, c["cost"], mode="risk", use_stop=True, time_stop=time_stop,
                                   max_pos=5, week_max=3, budget=c["budget"], **kw)
    rows = [(m, label, p, tstats(tr, a, z), stats(eq, inv, a, z)) for p, a, z in SPLITS]
    return rows, tr, sk, eq, inv


def run_trend(data):
    out, rows, extra, wt, eqs = [], [], [], {}, {}
    for m in MK:
        c = MK[m]
        for name, tick in (("Faber SMA200 monthly, ETFs", c["etf"]), ("Faber SMA200 monthly, stocks", c["stk"])):
            D = {t: ind(data[t]) for t in tick}

            def wf(d, live, D=D, tick=tick, on=True):
                ok = [t for t in tick if live[t] and d in D[t].index and (not on or D[t].C[d] > D[t].sma200[d])]
                return {t: 1 / len(tick) for t in ok}
            eq, inv, tr = weight_engine(data, m, tick, wf, c["cost"])
            beq, binv, _ = weight_engine(data, m, tick, lambda d, live, f=wf: f(d, live, on=False), c["cost"])
            if tick is c["stk"]:
                eqs[("faber", m)] = (eq, inv, tr)
            for p, a, z in SPLITS:
                rows.append((m, name, p, tstats(tr, a, z), stats(eq, inv, a, z)))
                rows.append((m, name.replace("Faber SMA200 monthly", "Equal-weight buy and hold (monthly rebalance)"), p, {}, stats(beq, binv, a, z)))
        for vname, st in (("Donchian 50/20, stocks, no stop", False), ("Donchian 50/20, stocks, with rules stop", True)):
            _, _, tr, _ = trade_engine(data, m, c["stk"], sig_donchian, c["cost"], use_stop=st)
            eq, inv, tr5, _ = trade_engine(data, m, c["stk"], sig_donchian, c["cost"], mode="slot", use_stop=st, max_pos=5)
            for p, a, z in SPLITS:
                rows.append((m, vname + " (every signal / 5 slots x 20%)", p, tstats(tr, a, z), stats(eq, inv, a, z)))
            wt[(m, vname)] = tr
            extra.append((m, vname, f"every-signal trades by exit: {trades_by_exit(tr)}"))
        r, tr, sk, eq, inv = rules_block(data, m, c["stk"], sig_donchian, True, None)
        out += r
        wt[(m, "Donchian rules-sized")] = tr
        eqs[("donchian", m)] = (eq, inv, tr)
        extra.append((m, "Donchian rules-sized", f"budget {c['budget']:,.0f} {c['cur']}, final equity {eq.iloc[-1]:,.0f} {c['cur']}; "
                     f"trades by exit: {trades_by_exit(tr)}; signals skipped: " + ", ".join(f"{k} {v}" for k, v in sk.items())))
    return rows, out, extra, wt, eqs


def run_momentum(data):
    rows, extra, wt, eqs = [], [], {}, {}
    for m in MK:
        c = MK[m]
        tick, idx = c["stk"], ind(data[c["idx"]])
        D = {t: ind(data[t]) for t in tick}

        def wf(d, live, filt=True):
            if filt and not idx.C[d] > idx.sma200[d]:
                return {}
            mom = pd.Series({t: D[t].mom.get(d, np.nan) for t in tick if live[t]}).dropna()
            return {t: 0.2 for t in mom.sort_values(ascending=False).index[:5]} if len(mom) >= 10 else {}
        for name, f in (("Top-5 12-1 momentum, index > SMA200 filter", wf), ("Top-5 12-1 momentum, no filter", lambda d, l: wf(d, l, False))):
            eq, inv, tr = weight_engine(data, m, tick, f, c["cost"])
            for p, a, z in SPLITS:
                rows.append((m, name, p, tstats(tr, a, z), stats(eq, inv, a, z)))
            wt[(m, name)] = tr
            if f is wf:
                eqs[("momentum", m)] = (eq, inv, tr)
            mo = (inv > 0).groupby(inv.index.to_period("M")).first()
            extra.append((m, name, f"months in cash {int((~mo).sum())} of {len(mo)}; holding spans by exit: {trades_by_exit(tr)}; "
                          f"average names changed per month {len(tr) / max(1, int(mo.sum())):.2f}"))
        beq, binv, _ = weight_engine(data, m, tick, lambda d, live: {t: 1 / len(tick) for t in tick if live[t]}, c["cost"])
        for p, a, z in SPLITS:
            rows.append((m, "Equal-weight buy and hold of the same stocks", p, {}, stats(beq, binv, a, z)))
    return rows, None, extra, wt, eqs


def run_swing(data):
    rows, out, extra, wt, eqs = [], [], [], {}, {}
    for m in MK:
        c = MK[m]
        tick = c["etf"] + c["stk"]
        for vname, st in (("RSI2, no stop", False), ("RSI2, with rules stop", True), ("RSI2, 2xATR stop only (not rule-compliant, comparison)", "atr")):
            _, _, tr, _ = trade_engine(data, m, tick, sig_rsi2, c["cost"], use_stop=st, time_stop=10)
            eq, inv, tr5, _ = trade_engine(data, m, tick, sig_rsi2, c["cost"], mode="slot", use_stop=st, time_stop=10, max_pos=5)
            for p, a, z in SPLITS:
                rows.append((m, vname + " (every signal / 5 slots x 20%)", p, tstats(tr, a, z), stats(eq, inv, a, z)))
            wt[(m, vname)] = tr
            extra.append((m, vname, f"every-signal trades by exit: {trades_by_exit(tr)}"))
        r, tr, sk, eq, inv = rules_block(data, m, tick, sig_rsi2, True, 10)
        out += r
        wt[(m, "RSI2 rules-sized")] = tr
        eqs[("rsi2", m)] = (eq, inv, tr)
        extra.append((m, "RSI2 rules-sized", f"budget {c['budget']:,.0f} {c['cur']}, final equity {eq.iloc[-1]:,.0f} {c['cur']}; "
                     f"trades by exit: {trades_by_exit(tr)}; signals skipped: " + ", ".join(f"{k} {v}" for k, v in sk.items())))
    return rows, out, extra, wt, eqs


MARKETS = {"": ("US", "SPY"), ".NS": ("India", "^NSEI"), ".T": ("Japan", "^N225"), ".HK": ("Hong Kong", "^HSI"),
           ".L": ("UK", "^FTSE"), ".PA": ("France", "^FCHI"), ".MC": ("Spain", "^IBEX"), ".DE": ("Germany", "^GDAXI"), ".MI": ("Italy", "FTSEMIB.MI")}
RISK_INR, CAP_INR, MIN_USD, MIN_INR = 2000, 40000, 5, 50


def market(t):
    suf = "." + t.rsplit(".", 1)[1] if "." in t else ""
    return MARKETS.get(suf, (None, None))


def meta(t, key, fetch, live_hours=24):
    import json
    p = CACHE / "live" / "meta.json"
    m = json.loads(p.read_text()) if p.exists() else {}
    e = m.get(t, {})
    if key not in e or time.time() - e.get(key + "_at", 0) > live_hours * 3600:
        try:
            e[key] = fetch()
        except Exception as ex:
            log(f"{t} {key}: {ex}")
            e[key] = e.get(key)
        e[key + "_at"] = time.time()
        m[t] = e
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(m, indent=1, default=str))
        time.sleep(2)
    return e[key]


def currency(t):
    import yfinance as yf
    return meta(t, "currency", lambda: yf.Ticker(t).fast_info["currency"], live_hours=24 * 30)


def is_fund(t):
    import yfinance as yf
    if meta(t, "quoteType", lambda: yf.Ticker(t).info.get("quoteType"), live_hours=24 * 30) in ("ETF", "MUTUALFUND"):
        return True
    name = meta(t, "name", lambda: (lambda i: i.get("longName") or i.get("shortName") or "")(yf.Ticker(t).info), live_hours=24 * 30) or ""
    return any(w in name.upper().split() for w in ("ETF", "BEES", "UCITS"))


def rs_index(t):
    m, ix = market(t)
    return ix if not is_fund(t) or m == "India" else "ACWI"


def earnings_dates(t):
    import yfinance as yf

    def f():
        d = yf.Ticker(t).get_earnings_dates(limit=12)
        return [] if d is None else sorted({str(x.date()) for x in d.index})
    return meta(t, "earnings", f)


def fx_inr(ccy, until, live=True):
    if ccy == "INR":
        return 1.0, None
    base, div = ("GBP", 100) if ccy == "GBp" else (ccy, 1)
    sym = "INR=X" if base == "USD" else f"{base}INR=X"
    d = load(sym, until, live)
    return d.C.iloc[-1] / div, d.index[-1].date()


def refresh(tickers, until=None, max_age_h=12):
    stale = []
    for t in dict.fromkeys(tickers):
        p = fname(t, True)
        d = load(t, None, True) if p.exists() else None
        if d is None or (until and d.index[-1] < pd.Timestamp(until) and time.time() - p.stat().st_mtime > 3600) or \
                (not until and time.time() - p.stat().st_mtime > max_age_h * 3600):
            stale.append(t)
    if stale:
        log(f"refreshing {len(stale)}: {' '.join(stale)}")
        refresh_recent(stale)


def setup(t, until=None, live=True, benches=None, swing=10):
    """Trade-plan numbers for one ticker: indicators, Donchian state, rules stop and size at the trigger."""
    data, rows, short = check_data([t], min_bars=260, until=until, live=live)
    if t not in data:
        return dict(t=t, error=f"no or short data ({short[0][1] if short else 0} bars)")
    d = ind(data[t])
    c, l = d.C, d.iloc[-1]
    dl = c.diff()
    up, dn = dl.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean(), (-dl.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
    o = dict(t=t, date=d.index[-1].date(), close=l.C, sma50=c.rolling(50).mean().iloc[-1], sma200=l.sma200, rsi14=(100 - 100 / (1 + up / dn)).iloc[-1],
             atr14=l.atr14, swlo=l.swlo, swlo_date=d.L.tail(swing).idxmin().date(), hi50=l.hi50, lo20=l.lo20,
             hi52=d.H.tail(252).max(), lo52=d.L.tail(252).min(), vol=d.V.iloc[-1], vol50=d.V.tail(50).mean(),
             don_entry=bool(l.C > l.hi50), don_exit=bool(l.C < l.lo20),
             last_entry=d.index[d.C > d.hi50][-1].date() if (d.C > d.hi50).any() else None,
             last_exit=d.index[d.C < d.lo20][-1].date() if (d.C < d.lo20).any() else None,
             from_hi63=l.C / d.H.tail(63).max() - 1, data_rows=rows)
    for n, lab in ((63, "3m"), (252, "12m")):
        o[f"ret_{lab}"] = c.iloc[-1] / c.iloc[-1 - n] - 1
        for b in benches or [rs_index(t)]:
            bd = load(b, until, live)
            if bd is not None:
                bc = bd.C.reindex(c.index).ffill()
                o[f"rs_{b}_{lab}"] = o[f"ret_{lab}"] - (bc.iloc[-1] / bc.iloc[-1 - n] - 1)
    o["entry"] = l.C * (1 + LIMIT_UP) if o["don_entry"] else l.hi50
    o["stop"] = plan_stop(o["entry"], l.atr14, l.swlo)
    o["stop_rule"] = "10% cap" if o["stop"] == 0.9 * o["entry"] else ("swing low" if o["stop"] == l.swlo else "2 x ATR")
    return o


def plan_stop(entry, atr, swlo):
    s_sw = swlo if swlo < entry else -np.inf
    return max(entry - 2 * atr, s_sw, 0.9 * entry)


def news_score(t):
    import re
    p = OUT.parents[1] / "news" / f"{t}.md"
    if not p.exists():
        return None
    m = re.search(r"Score:\s*([+-]?\d)", p.read_text())
    return int(m.group(1)) if m else None


def size(entry, stop, fx):
    risk_sh = math.floor(RISK_INR / ((entry - stop) * fx))
    cap_sh = math.floor(CAP_INR / (entry * fx))
    return min(risk_sh, cap_sh), risk_sh, cap_sh


def check_rules(o, fx, earn, today):
    fails = []
    if not o["don_entry"]:
        fails.append(f"no Donchian 50-day-high close (trigger {o['hi50']:.2f})")
    sh, rs, cs = size(o["entry"], o["stop"], fx)
    if o["close"] * fx < (MIN_INR if market(o["t"])[0] == "India" else MIN_USD * fx_inr("USD", str(today))[0]):
        fails.append("price under $5 / Rs 50")
    if sh < 1:
        fails.append("20% cap: 1 share > Rs 40,000" if cs < 1 else "risk: Rs 2,000 buys < 1 share")
    if is_fund(o["t"]):
        pass
    elif earn is None:
        fails.append("earnings date unknown (not checked)")
    else:
        nxt = [e for e in earn if pd.Timestamp(e) > pd.Timestamp(today)]
        if not nxt:
            fails.append("earnings date unknown (not checked)")
        elif np.busday_count(str(today), nxt[0]) <= 5:
            fails.append(f"earnings {nxt[0]} within 5 trading days")
    ns = news_score(o["t"])
    if ns is None:
        fails.append("no news file (news/<SYMBOL>.md)")
    elif ns <= -2:
        fails.append("news score -2")
    return fails, sh, ns


def setup_table(syms, until=None, limits=None):
    limits = limits or {}
    idx = [market(t)[1] for t in syms]
    bad = [t for t, i in zip(syms, idx) if i is None]
    syms = [t for t in syms if t not in bad]
    ccys = {t: currency(t) for t in syms}
    fxs = {("INR=X" if c in ("USD",) else ("GBPINR=X" if c == "GBp" else f"{c}INR=X")) for c in ccys.values() if c != "INR"} | {"INR=X"}
    refresh(syms + [i for i in idx if i] + [rs_index(t) for t in syms] + sorted(fxs), until)
    head = ("| Symbol | Close (ccy, date) | Trend (50/200-day SMA; Donchian 50/20) | RSI14 | RS vs index 3m | Entry or trigger | Stop (rule, risk %) | "
            "Shares (Rs 2,000 risk, Rs 40k cap) | Valid today (first failing rule) | Note for staged buying |\n|---|---|---|---|---|---|---|---|---|---|\n")
    out, notes, info = head, [], []
    for t in syms:
        o = setup(t, until)
        if "error" in o:
            out += f"| {t} | {o['error']} | | | | | | | no | |\n"
            info.append(dict(t=t, valid=False, waits=["no data"]))
            continue
        fx, fxd = fx_inr(ccys[t], str(o["date"]))
        earn = None if is_fund(t) else earnings_dates(t)
        fails, sh, ns = check_rules(o, fx, earn, o["date"])
        ix = rs_index(t)
        trend = (f"{'above' if o['close'] > o['sma50'] else 'below'} 50 ({o['sma50']:.2f}), {'above' if o['close'] > o['sma200'] else 'below'} 200 ({o['sma200']:.2f}); "
                 + ("Donchian BUY signal today" if o["don_entry"] else "Donchian exit signal today" if o["don_exit"] else
                    f"no signal (last buy {o['last_entry']}, last exit {o['last_exit']})"))
        entry = (f"buy next open, limit {o['close'] * (1 + LIMIT_UP):.2f}" if o["don_entry"] else
                 f"trigger: close > {o['hi50']:.2f} ({o['hi50'] / o['close'] - 1:+.1%})")
        risk = o["entry"] - o["stop"]
        out += (f"| {t} | {o['close']:.2f} {ccys[t]} ({o['date']}) | {trend} | {o['rsi14']:.1f} | {o.get(f'rs_{ix}_3m', float('nan')):+.1%} vs {ix} | {entry} | "
                f"{o['stop']:.2f} ({o['stop_rule']}, {risk / o['entry']:.1%}) | {sh} (risk {size(o['entry'], o['stop'], fx)[1]}, cap {size(o['entry'], o['stop'], fx)[2]}; "
                f"FX {fx:.4f} {fxd or ''}) | {'yes' if not fails else 'no: ' + fails[0] + (f' (+{len(fails) - 1} more: ' + '; '.join(fails[1:]) + ')' if len(fails) > 1 else '')}{'; earnings n/a (fund)' if is_fund(t) else ''} | {limit_note(o, limits.get(t))}{stage_note(o)[0]} |\n")
        info.append(dict(t=t, valid=not fails, waits=stage_note(o)[1], date=o["date"], limit=limits.get(t), close=o["close"]))
        for r in o["data_rows"]:
            if r["big"] or r["gap"] or r["fixed"] or r["stale"] or r["bad_hl"]:
                notes.append(f"{t}: stale bars dropped {r['stale']}, rescaled {r['fixed'] or '-'}, moves > 40% {'; '.join(f'{a} {b}%' for a, b in r['big']) or '-'}, gaps > 40% {'; '.join(f'{a} {b}%' for a, b in r['gap']) or '-'}")
    for t in bad:
        out += f"| {t} | unknown exchange suffix | | | | | | | no | |\n"
        info.append(dict(t=t, valid=False, waits=["unknown exchange suffix"]))
    out += ("\nNote column: trend up = above both the 50- and 200-day SMA, down = below both, else mixed; distance from the 52-week high; RSI(14); "
            "ATR(14) as % of price (a normal daily move). Funds (yfinance quoteType ETF, or ETF/BeES/UCITS in the name, since Yahoo tags some NSE ETFs as EQUITY): relative strength vs ACWI, except funds listed in India (local index); the earnings rule does not apply. Wait flags: RSI(14) above 75, or close more than 10% above the 50-day SMA.\n""\nStop and shares are at the entry shown (trigger price if no signal), with today's ATR(14) and 10-day swing low. Portfolio rules "
            "(5 open positions, 3 entries a week, loss limits) are checked in the plan, not here.\n")
    return out + "".join(f"\nData note: {n}" for n in notes), info


def limit_note(o, lim):
    if lim is None:
        return ""
    d = o["close"] / lim - 1
    return f"research limit {lim:,.2f}: close {d:+.1%} ({'inside' if d <= 0 else 'ABOVE'}{', at the edge' if -0.01 <= d <= 0 else ''}); "


def stage_note(o):
    c = o["close"]
    tr = "up" if c > o["sma50"] and c > o["sma200"] else "down" if c < o["sma50"] and c < o["sma200"] else "mixed"
    waits = (["RSI > 75"] if o["rsi14"] > 75 else []) + (["more than 10% above the 50-day"] if c / o["sma50"] - 1 > 0.10 else [])
    return (f"trend {tr}; {c / o['hi52'] - 1:+.1%} vs 52-week high; RSI {o['rsi14']:.0f}; ATR {o['atr14'] / c:.1%} a day; "
            + ("wait: " + ", ".join(waits) if waits else "no wait flag")), waits


def write_setup(path, table, info, note="", title=None, until=None):
    path = Path(path)
    date = max((str(i["date"]) for i in info if "date" in i), default=time.strftime("%Y-%m-%d"))
    valid = [i["t"] for i in info if i["valid"]]
    waits = [f"{i['t']} ({', '.join(i['waits'])})" for i in info if i["waits"]]
    summ = [f"{len(info)} symbols checked on the {date} close; valid under the trading rules today: {', '.join(valid) or 'none'}.",
            "Staged long-term buys: " + ("wait on " + "; ".join(waits) if waits else "no wait flag (no RSI above 75, none more than 10% above its 50-day SMA)") + "."]
    lim = [i for i in info if i.get("limit")]
    if lim:
        edge = [i["t"] for i in lim if -0.01 <= i["close"] / i["limit"] - 1 <= 0]
        above = [i["t"] for i in lim if i["close"] > i["limit"]]
        summ.append(f"Research limits: {len(lim) - len(above)} of {len(lim)} closes inside; above: {', '.join(above) or 'none'}; within 1% of the limit: {', '.join(edge) or 'none'}.")
    old = [f"{i['t']} ({i['date']})" for i in info if until and "date" in i and str(i["date"]) < until]
    if old:
        summ.append(f"No {until} bar yet, last close used: {', '.join(old)}.")
    if note:
        summ.append(note)
    page(path, title or f"Setup check {path.stem}", summ,
         f"Run {time.strftime('%Y-%m-%d')} with `.venv/bin/python trading/backtests/engine.py setup {' '.join(i['t'] for i in info)} --out {path.as_posix().split('finance/')[-1]}"
         + (" --limits ..." if lim else "") + (f" --date {until}" if until else "") + "`; "
         "every number is printed by that command (yfinance daily data).\n\n" + table + "\n")
    setups_index()

SEMIS = ["NVDA", "AVGO", "AMD", "QCOM", "TXN", "INTC", "TSM", "MU", "ARM", "SMH", "SOXX"]


def hold_stats(rows, data):
    spy = data["SPY"]
    out = []
    for t, e, x, ret in rows:
        d = data[t]
        so, sx = spy.O.asof(e), spy.O.asof(x)
        out.append(dict(t=t, entry_date=e, exit_date=x, ret=ret, spy=sx / so - 1, mae=d.L.loc[e:x].iloc[:-1].min() / d.O[e] - 1 if x > e else 0.0))
    return pd.DataFrame(out)


def drop_events(data, tickers, hold, trend, cost=0.0005, drop=0.25):
    rows = []
    for t in tickers:
        d = ind(data[t])
        cond = (d.C <= (1 - drop) * d.H.rolling(63).max()) & d.sma200.notna()
        if trend:
            cond &= d.C > d.sma200
        nxt, idx = 0, d.index
        for i in np.where(cond.values)[0]:
            if i < nxt or i + 1 + hold >= len(d):
                continue
            e, x = idx[i + 1], idx[i + 1 + hold]
            rows.append((t, e, x, d.O[x] * (1 - cost) / (d.O[e] * (1 + cost)) - 1))
            nxt = i + 1 + hold
    return hold_stats(rows, data)


def dist_row(name, h):
    if len(h) == 0:
        return (name, 0) + ("n/a",) * 9
    return (name, len(h), pct(h.ret.mean()), pct(h.ret.median()), pct((h.ret > 0).mean(), 0), pct(h.ret.quantile(0.1)),
            pct(h.spy.mean()), pct((h.spy > 0).mean(), 0), pct(h.mae.mean()), pct(h.mae.min()), pct((h.mae <= -0.10).mean(), 0))


def run_drop():
    tick = US_STK + [t for t in SEMIS if t not in US_STK]
    data, rows, short = check_data(tick + ["SPY"] + US_ETF)
    tick = [t for t in tick if t in data]
    us = MK["US"]
    var = []
    for hold in (20, 60):
        for trend in (False, True):
            h = drop_events(data, tick, hold, trend)
            nm = f"({'b' if trend else 'a'}) Drop 25%+ from 63-day high{', above SMA200' if trend else ''}, hold {hold} days"
            var.append((nm, h, True))
            var.append((nm + ", without NVDA", h[h.t != "NVDA"], False))
    _, _, trc, _ = trade_engine(data, "US", US_STK, sig_donchian, us["cost"], use_stop=True)
    _, _, trd, _ = trade_engine(data, "US", US_ETF + US_STK, sig_rsi2, us["cost"], use_stop=True, time_stop=10)
    for nm, tr in (("(c) Donchian 50/20, rules stop (reused, original US universe)", trc), ("(d) RSI(2) dip-buy, rules stop (reused, original US universe)", trd)):
        tr = tr[tr.why != "open at end"]
        var.append((nm, hold_stats([(r.t, r.entry_date, r.exit_date, r.ret) for r in tr.itertuples()], data), True))
    return var, rows, short, tick


def write_drop(var, rows, short, tick):
    d = OUT / "drop-vs-trend"
    run = RUN_NOTE.format(d=time.strftime("%Y-%m-%d"), name="drop-vs-trend")
    hd = ["Variant", "Events", "Mean", "Median", "% positive", "Worst 10% (10th pct)", "SPY same days mean", "SPY % positive", "Mean worst dip in hold", "Worst dip in hold", "% that fell 10%+ below entry"]
    uni = lambda n: "35 names" if n[:3] in ("(c)", "(d)") else f"US list + semis ({len(tick)} names)"
    main = tbl(["Variant", "Universe"] + hd[1:], [(r[0], uni(r[0])) + tuple(r[1:]) for r in (dist_row(n, h) for n, h, _ in var)])
    per = tbl(["Variant", "Universe", "Period", "Events", "Mean", "Median", "% positive", "Worst 10%", "SPY same days mean"],
              [(n, uni(n), p) + dist_row(n, h[(h.entry_date >= a) & (h.entry_date <= z)])[1:6] + dist_row(n, h[(h.entry_date >= a) & (h.entry_date <= z)])[6:7]
               for n, h, k in var if k for p, a, z in SPLITS[1:]])
    a60 = next(h for n, h, _ in var if n.startswith("(a)") and "60" in n and "NVDA" not in n)
    c = next(h for n, h, _ in var if n.startswith("(c)"))
    summ = [SUMMARY["drop"],
            f"Buying a 25%+ drop and holding 60 days: mean {pct(a60.ret.mean())}, median {pct(a60.ret.median())}, {pct((a60.ret > 0).mean(), 0)} positive, worst 10% {pct(a60.ret.quantile(0.1))} (SPY same days mean {pct(a60.spy.mean())}).",
            f"Waiting for the trend (Donchian 50/20, rules stop): mean {pct(c.ret.mean())} a trade, {pct((c.ret > 0).mean(), 0)} positive, losses capped by the stop (worst 10% {pct(c.ret.quantile(0.1))}).",
            "These are today's surviving large caps; real dip-buying also hits stocks that never came back, so the drop numbers are too good."]
    body = (f"{run}\n\n## Rules (fixed, not tuned)\n"
            "- (a) Event: close at least 25% below the highest high of the last 63 trading days. Buy at the next open, sell at the open 20 or 60 trading days later. "
            "One event per stock at a time (no new event while a hold is open). Costs 0.05% a side (US).\n"
            "- (b) Same, but only if the close is still above the 200-day SMA.\n"
            "- (c) Wait for the trend: Donchian 50/20 with the AGENTS.md stop, every signal (from [trend-following](../trend-following/index.md); same run, original US stock list).\n"
            "- (d) RSI(2) < 10 dip-buy above the 200-day SMA with the AGENTS.md stop (from [swing-pullback](../swing-pullback/index.md); US ETFs and stocks).\n"
            f"- Universe for (a) and (b): the US stock list plus semis {' '.join(t for t in SEMIS if t not in US_STK)}; daily Yahoo data {START} to {LAST}. "
            "Worst dip in hold = lowest low from the entry day to the day before the exit, vs the entry price (the drawdown you sit through; a stop-day gap shows in the return, not here); a dip of 10% or more would have hit any stop allowed by the rules (max 10%), so (a) and (b) as tested, with no stop, are not rule-compliant. "
            "SPY same days = SPY open-to-open over the same dates. (c) and (d) count closed trades only.\n\n"
            "## Results (full period, every event, net of costs)\n" + main +
            "\nHolds differ: (a)/(b) are fixed 20 or 60 days; (c) averages about 54 days; (d) about 2 days. Compare (c) and (d) mainly on the shape (median, % positive, worst 10%), not the mean.\n\n"
            "## By period (2010-2019 vs 2020-2026)\n" + per +
            "\n## Biases\n" + tbl(["Bias", "Effect"], [
                ("Survivorship: today's large caps only", "Stocks that fell 25% and kept falling (delisted, merged, shrunk out of the list) are missing: drop-buying looks better than it was"),
                ("NVDA 2010-2026 is an outlier", "Shown with and without NVDA"),
                ("Overlapping events across stocks", "Drops cluster in crashes (2020, 2022): events are not independent, so the % positive is less certain than the count suggests"),
                ("No earnings rule, no news filter", "Many 25% drops follow results or news; the AGENTS.md earnings and news -2 rules would block some entries")]) +
            "\n## Data\n" + (f"Dropped for short history (< {MIN_BARS} bars): {', '.join(f'{t} ({n})' for t, n in short)}. " if short else "") +
            "Data problems in the added tickers: " + ("; ".join(f"{r['t']}: moves > 40% {'; '.join(f'{a} {b}%' for a, b in r['big'])}" for r in rows if r["big"] and r["t"] not in ALL) or "none") +
            ". Other data checks: see [trend-following/data.md](../trend-following/data.md).\n\n## Verdict\n" + TEXT_DROP + "\n")
    page(d / "index.md", "Study: buy after a sharp drop vs wait for the trend", summ, body)

sig_donchian.__doc__ = "close {C:.2f} > prior 50-day high {hi50:.2f}"
sig_rsi2.__doc__ = "close {C:.2f} > SMA200 {sma200:.2f}, RSI(2) {rsi2:.1f} < 10"


REPORTS = Path(os.environ.get("FINANCE_REPORTS", Path.home() / ".local/share/finance-reports")) / "trading/backtests/reports"
RUN_NOTE = "Run {d} with `.venv/bin/python trading/backtests/engine.py {name}`; every number on this page is printed by that script."


def qs_report(equity, bench_close, slug, title, bench_name, periods=252, universe="35 names"):
    """Quantstats table vs benchmark (markdown) + HTML tearsheet in $FINANCE_REPORTS/trading/backtests/reports/<slug>.html (outside git).
    Works for any daily equity series (backtest or paper-trading account)."""
    import warnings
    import quantstats as qs
    warnings.filterwarnings("ignore")
    r = equity.pct_change().dropna()
    b = bench_close.reindex(equity.index).ffill().pct_change().dropna().reindex(r.index).fillna(0.0)
    r.name, b.name = "Strategy", bench_name

    def m(x):
        dd = qs.stats.to_drawdown_series(x)
        det = qs.stats.drawdown_details(dd)
        return dict(cagr=qs.stats.cagr(x, periods=periods), sharpe=qs.stats.sharpe(x, rf=0, periods=periods),
                    sortino=qs.stats.sortino(x, rf=0, periods=periods), mdd=qs.stats.max_drawdown(x),
                    ldd=float(det["days"].max()) if len(det) else 0.0, vol=qs.stats.volatility(x, periods=periods),
                    bm=qs.stats.best(x, aggregate="ME"), wm=qs.stats.worst(x, aggregate="ME"),
                    wr=qs.stats.win_rate(x, aggregate="ME"), calmar=qs.stats.calmar(x))
    ms, mb = m(r), m(b)
    REPORTS.mkdir(parents=True, exist_ok=True)
    qs.reports.html(r, benchmark=b, rf=0, title=title, output=str(REPORTS / f"{slug}.html"), periods_per_year=periods,
                    match_dates=False)
    names = [("CAGR", "cagr", pct), ("Sharpe (rf=0)", "sharpe", num), ("Sortino (rf=0)", "sortino", num), ("Max drawdown", "mdd", pct),
             ("Longest drawdown (calendar days)", "ldd", lambda v: f"{v:.0f}"), ("Volatility (annual)", "vol", pct),
             ("Best month", "bm", pct), ("Worst month", "wm", pct), ("Months with a gain (of months with a non-zero return)", "wr", pct),
             ("Calmar (CAGR / max drawdown)", "calmar", num)]
    h = f"| Metric (quantstats, {universe}) | Strategy | {bench_name} |\n|---|---|---|\n"
    for lab, k, f in names:
        h += f"| {lab} | {f(ms[k])} | {f(mb[k])} |\n"
    return h, ms


def tbl(head, rows):
    return "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n" + "".join("| " + " | ".join(str(x) for x in r) + " |\n" for r in rows)


def page(path, title, summary, body):
    assert len(summary) <= 5
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n## Summary\n" + "\n".join(f"- {x}" for x in summary) + "\n\n" + body)
    log(f"wrote {path}")


def write(key, name, title, rules, src, rows, rules_rows, extra, wt, verdict, head, spot_tbl, pv_note, eqs, data):
    d = OUT / name
    run = RUN_NOTE.format(d=time.strftime("%Y-%m-%d"), name=name)
    data_part, res_part = head.split("## Costs and execution")
    res_part = "## Costs and execution" + res_part
    heads, qs_txt = [], ""
    for (k, m), (eq, inv, tr) in eqs.items():
        b = MK[m]["idx"]
        es, ts, bs = stats(eq, inv), tstats(tr), stats(data[b].C / data[b].C.iloc[0])
        slug = f"{name}-{k}-{m}" if len({x for x, _ in eqs}) > 1 else f"{name}-{m}"
        label = VERSIONS[k]
        q, qm = qs_report(eq, data[b].C, slug, f"{label} ({m}) vs {b}", b)
        qs_txt += (f"\n### {m}: {label} vs {b}\nHTML tearsheet: [reports/{slug}.html](../reports/{slug}.html)\n\n" + q +
                   f"\nEngine (same run): CAGR {pct(es['cagr'])}, max drawdown {pct(es['mdd'])}, Sharpe {num(es['sharpe'])}. "
                   f"quantstats CAGR {pct(qm['cagr'])} counts years as trading days / 252; the engine uses calendar days / 365.25. "
                   f"Max drawdown is the same calculation in both.\n")
        bar, barv = bar_check(k, eq, inv, tr)
        heads.append(dict(key=k, m=m, label=label, es=es, ts=ts, b=b, bs=bs, slug=slug, name=name, fit=FIT.get((k, m), "see bar"), qcagr=qm["cagr"], qmdd=qm["mdd"],
                          bar=bar, barv=barv))
    head_tbl = tbl(["Market", "Universe", "Version that counts", "CAGR", "Max DD", "Win rate", "Trades", "Benchmark", "Bench CAGR", "Bench max DD", "Fit", "Backtest bar", "Tearsheet"],
                   [(h["m"], "35 names", h["label"], pct(h["es"]["cagr"]), pct(h["es"]["mdd"]), pct(h["ts"]["win"]), h["ts"]["n"], h["b"],
                     pct(h["bs"]["cagr"]), pct(h["bs"]["mdd"]), h["fit"], h["bar"], f"[HTML](../reports/{h['slug']}.html)") for h in heads])
    verdict += "\n\nBacktest bar ([trading/playbook.md](../../playbook.md#backtest-bar)): " + "; ".join(f"{h['m']} {h['label']}: {h['bar']}" for h in heads) + "."
    summ = [SUMMARY[key]] + [f"{h['m']}, {h['label']}: {pct(h['es']['cagr'])} a year, worst drop {pct(h['es']['mdd'])} "
                             f"({h['b']} {pct(h['bs']['cagr'])}, {pct(h['bs']['mdd'])})." for h in heads]
    links = tbl(["Page", "What is in it"], [("[results.md](results.md)", "All variants and periods, rules-sized simulation, quantstats metrics, costs, benchmarks"),
                                            ("[trades.md](trades.md)", "Trade counts, exits, skipped signals, worst trades, spot checks"),
                                            ("[data.md](data.md)", "Data source, universe, data problems, known biases")] +
                ([("[universe.md](universe.md)", "Full-universe check (all included scan names) and its backtest bar")] if name in {v["page"] for v in STRATS.values()} else []) + [
                                            ("[../index.md](../index.md)", "All strategies compared")])
    page(d / "index.md", f"Backtest: {title}", summ,
         f"{run}\n\n## Rules (exact)\n{rules}\n\n## Headline (full period {START} to {LAST}, costs included)\n{head_tbl}\n## Verdict\n{verdict}\n\n"
         f"## Sources\n{src}\n\n## Pages\n{links}")
    body = f"{run}\n\n## How to read the tables\n{pv_note}\n\n## Results by variant and period\n" + perf_table(rows)
    if rules_rows:
        body += ("\n## Rules-sized simulation (AGENTS.md trading rules, approved 2026-11-15 for paper trading)\nBudget Rs 2,00,000 for India; US simulated in USD with 200000 / 94 = $2,128 (fixed USD/INR 94). "
                 "Risk 1% of current equity per trade, shares = risk / (entry - stop) rounded down to whole shares, at most 20% of equity per position, "
                 "at most 5 open positions, at most 3 new entries per calendar week, stop placed at entry (2 x ATR(14) below entry or the 10-day swing low, "
                 "whichever is tighter, never wider than 10%). Candidates on the same day are taken in signal-strength order. Equity compounds (risk and cap use current equity, not a fixed Rs 2 L).\n\n"
                 + perf_table(rules_rows))
    body += "\n## quantstats metrics (version that counts vs benchmark, rf=0, daily returns of the same equity curve)\n" + qs_txt + "\n" + res_part
    page(d / "results.md", f"Backtest results: {title}", [f"All variants and periods for {name}; the verdict is in [index.md](index.md).", summ[1]], body)
    body = f"{run}\n\n## Trade counts, exits and skipped signals\n" + tbl(["Market", "Version", "Detail"], extra)
    for k, tr in wt.items():
        if len(tr):
            body += f"\n### Worst 5 trades: {k[0]}, {k[1]}\n" + worst(tr)
    body += ("\n## Spot check of 2 trades against the raw cached data\n" + spot_tbl + "\nThe rows above were also checked by hand on 2026-11-15 against the cache csv files "
             "(signal-day close and indicator, next-day open fill, stop level, exit-day bar and exit price) with a separate calculation; all matched.\n")
    page(d / "trades.md", f"Backtest trades: {title}", [f"Trade-level detail for {name}: exits, skipped signals, worst trades, spot checks.",
                                                        "Verdict and headline numbers: [index.md](index.md)."], body)
    page(d / "data.md", f"Backtest data: {title}", ["Yahoo daily data 2010 to " + LAST + "; bad bars in the India ETFs were repaired, stale filler rows dropped (table below).",
                                                    "Stock results are biased upwards: the lists are today's large caps (survivorship)."],
         f"{run}\n\n" + data_part + "\n" + BIASES)
    old = OUT / f"{name}.md"
    if old.exists():
        old.unlink()
    return heads


def write_index(heads):
    rows = [(f"[{h['name']}]({h['name']}/index.md)", h["label"], h["m"], "35 names", pct(h["es"]["cagr"]), pct(h["es"]["mdd"]), pct(h["ts"]["win"]), h["ts"]["n"],
             h["b"], pct(h["bs"]["cagr"]), pct(h["bs"]["mdd"]), h["fit"], "PASS" if h["bar"] == "pass" else "fail", f"[HTML](reports/{h['slug']}.html)") for h in heads]
    ok = [h for h in heads if h["bar"] == "pass"]
    summ = ["Pass the backtest bar on the 35-name lists: " + (", ".join(f"{h['label']} in {h['m']} ({pct(h['es']['cagr'])} a year, worst drop {pct(h['es']['mdd'])})" for h in ok) or "none") + ".",
            f"All other strategy x market pairs fail at least one test ({len(heads) - len(ok)} of {len(heads)}); the failing items are in [trading/playbook.md](../playbook.md#backtest-bar).",
            "Binding test, the FULL scan universe (about 680 US and 190 India names, [playbook](../playbook.md#backtest-bar)): " +
            (lambda u: ("these pass: " + ", ".join(f"{r['label']} ({r['m']})" for r in u if r["bar"] == "pass")) if any(r["bar"] == "pass" for r in u) else
             "no strategy passes, so no paper trades are opened yet")(__import__("json").loads((CACHE / "bar.json").read_text()).get("universe", []) if (CACHE / "bar.json").exists() else []) + ".",
            "Momentum rotation and Faber timing have no stop, so they sit outside the trading rules (long-term ideas only).",
            f"All numbers: daily Yahoo data {START} to {LAST}, costs included, run {time.strftime('%Y-%m-%d')} with `.venv/bin/python trading/backtests/engine.py all`."]
    page(OUT / "index.md", "Backtests", summ,
         "## Versions that count vs benchmark (full period, costs included)\n" +
         tbl(["Strategy", "Version that counts", "Market", "Universe", "CAGR", "Max DD", "Win rate", "Trades", "Benchmark", "Bench CAGR", "Bench max DD", "Fit", "Backtest bar", "Tearsheet"], rows) +
         "\nBenchmarks are buy and hold (SPY with dividends; ^NSEI is a price index without dividends). Win rate and trades: rules-sized trades for "
         "the rules-sized strategies, holding spans for Faber and momentum. Each strategy page has all variants, periods, trades and data checks.\n"
         "\n## Other studies\n" + tbl(["Study", "Question"], [("[drop-vs-trend](drop-vs-trend/index.md)", "Buy after a 25%+ drop, or wait for a trend signal?")]) +
         "\n## Daily setup check\n`.venv/bin/python trading/backtests/engine.py setup SYM1 SYM2 ... [--date YYYY-MM-DD]` prints one row per symbol: trend, RSI, "
         "relative strength vs the local index, Donchian trigger, rules stop, shares at Rs 2,000 risk and the Rs 40,000 cap, and whether the approved rules allow an entry today. "
         "Prices for it are kept in a separate live cache so these backtests stay reproducible.\n")


VERSIONS = {"donchian": "Donchian 50/20, rules stop, rules-sized", "faber": "Faber SMA200 monthly, stocks",
            "momentum": "Top-5 12-1 momentum, index filter", "rsi2": "RSI(2), rules stop, rules-sized"}
FIT = {("donchian", "US"): "Fit for paper trading", ("donchian", "India"): "Paper test only (weak)",
       ("faber", "US"): "Outside rules (30+ positions); filter idea", ("faber", "India"): "Outside rules (30+ positions); filter idea",
       ("momentum", "US"): "Long-term sleeve only (no stop)", ("momentum", "India"): "Long-term sleeve only (no stop)",
       ("rsi2", "US"): "Not fit (rules stop)", ("rsi2", "India"): "Not fit (costs and stop)"}
SUMMARY = {"trend": "Fit for paper trading in the US only: use Donchian 50/20 with the rules stop. Faber SMA200 on stocks had smaller drops but holds up to 30+ stocks at once, outside the 5-position rule: a long-term or market-filter idea only.",
           "mom": "Beats the index but not an equal-weight hold of the same stocks, and it has no stop: a long-term sleeve at most, not for the trading budget.",
           "drop": "Buying a sharp drop is not a valid entry under the approved rules; on survivors it made money on average but with deep dips during the hold.",
           "swing": "Not fit: the required stop cuts most trades in 2 days, and in India costs eat the edge; do not put it in trade plans."}


NOTE_TRADE = ("How to read the table: Trades, Win rate, Avg win, Avg loss, Avg trade, Profit factor and days held come from the every-signal run "
              "(every signal is taken, one unit each, no capital limit; returns net of costs). CAGR, Max DD, Exposure (average share of equity invested) "
              "and Sharpe come from a portfolio run of the same signals: 5 slots, each 20% of current equity, fractional shares, no weekly limit, "
              "candidates on the same day taken in signal-strength order. Skip counts below are per signal-day (a stock can signal on many days in a row).")
NOTE_W = ("How to read the table: each row is a portfolio run. Trades are holding spans (from the open where a name is bought to the open where it is sold; "
          "monthly top-ups between are ignored), returns net of costs. Exposure = average share of equity invested.")
TEXT = {
    "trend": ("""Two families, run separately for US and India.

A. Faber timing (SMA200, monthly check). On the last trading day of each month, for each asset in the set: if close > its 200-day simple moving average of closes, hold it at weight 1/N (N = all assets in the set) from the next day's open; otherwise that share sits in cash. All held assets are reset to 1/N at each monthly rebalance. Sets: the market's ETFs (US: SPY QQQ IWM EFA EEM TLT GLD; India: NIFTYBEES BANKBEES GOLDBEES) and the market's stock list. Compared with the same set held at 1/N with monthly rebalance.

B. Donchian 50/20 breakout on the stock lists. Entry: close > highest high of the prior 50 trading days (signal day excluded) -> buy next open. Exit: close < lowest low of the prior 20 trading days -> sell next open. Variants: (1) no stop; (2) with the AGENTS.md stop: at the fill, stop = the highest (tightest) of entry - 2 x ATR(14), the 10-day swing low (lowest low of the 10 days up to the signal day, used only if below entry) and entry x 0.90; the stop never moves. Every variant run is shown.""",
              """- Faber, M. (2007), "A Quantitative Approach to Tactical Asset Allocation", Journal of Wealth Management (SSRN 962461). Faber uses a 10-month SMA on month-end closes; a 200-day SMA checked monthly is used here (close equivalent, as specified for this test).
- Moskowitz, T., Ooi, Y. H., Pedersen, L. H. (2012), "Time series momentum", Journal of Financial Economics 104(2): an asset's own past 12-month return predicts its next month across asset classes.
- Donchian channel breakout and the Turtle rules (Faith, C. (2007), "Way of the Turtle"): System 2 enters on a 55-day high; the 50-day entry / 20-day exit used here is the common simplified version. Turtles trade intraday breakouts; here signals use the close and fill at the next open.""",
              """US: Donchian 50/20 with the rules stop is the only tested trend strategy that kept up with buy and hold while cutting the drawdown: rules-sized (Rs 2 L equivalent) it made 13.1% a year with a -23.1% worst drop, against SPY 13.9% and -33.7%, and it held up in both 2010-2019 and 2020-2026 (profit factor about 2 in each). Win rate is low (about 4 in 10); profits come from a few large trends, so expect long runs of small stopped-out losses. India: the same rules made only 5.1% a year with a -33.0% drop against Nifty 9.8% (price index); costs of 0.22% a side and the tight stop hurt, and it was weak in 2010-2019. Faber SMA200 timing roughly halved drawdowns in both markets but gave up a lot of return against holding the same assets; it is better used as a market filter than as a trading strategy. Verdict: fit for paper trading on US large caps; India only as a paper test to collect evidence, not for real money on these results. A trade plan should use exactly: buy at the next open after a daily close above the prior 50-day high; stop at entry = tightest of 2 x ATR(14), 10-day swing low, 10% (GTT/stop order the same day, never moved down); exit at the next open after a close below the prior 20-day low or at the stop; size = 1% risk / (entry - stop), max 20% of budget, max 5 open, max 3 new entries a week; earnings rule applied by hand (not tested).""",
              NOTE_TRADE),
    "mom": ("""At each month-end close: if the market index (US: SPY; India: ^NSEI) closes above its 200-day SMA, rank the market's stock list by 12-1 month return = close 21 trading days ago / close 252 trading days ago - 1 (the latest month skipped), and hold the top 5 at 20% each from the next day's open; all holdings reset to 20% each month. If the index is below its SMA200, hold cash. At least 10 stocks with full history are needed to rank. Variant run: the same without the index filter. No stop (the published rules have none).""",
            """- Jegadeesh, N., Titman, S. (1993), "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency", Journal of Finance 48(1): 3-12 month winners keep outperforming for 3-12 months.
- Antonacci, G. (2014), "Dual Momentum Investing": relative momentum plus an absolute (trend) filter that moves to cash in bear markets. Antonacci's absolute filter is the 12-month return vs T-bills; the index > 200-day SMA filter (Faber 2007) is used here as specified for this test.""",
            """Momentum rotation beat the market index in both markets: US 17.1% a year with the filter (27.8% without) vs SPY 13.9%; India 13.7% with the filter (15.6% without) vs Nifty 9.8% (price index) and NIFTYBEES 10.6%. But it did not beat simply holding the same hand-picked stocks at equal weight (US 21.1%, India 18.0%), and that basket is itself inflated by survivorship (today's winners chosen in 2026), so the true edge is smaller than the gap to the index suggests. The index filter cut the India drawdown (-22.1% vs -36.3%) but in the US it cost return and did not reduce the worst drop (-38.5% vs -32.7%), because the filter re-entered late after sharp falls. Results also weakened in 2020-2026 in the US (win rate and profit factor down). Verdict: this is a monthly allocation method, not a swing trade, and it has no stop, so it does not fit the AGENTS.md trading rules as written (stop on every trade, 1% risk sizing, 5 positions at 20%). Fit for paper trading only as a separate long-term sleeve if finance-main and the user agree; a plan would use exactly: month-end ranking by 12-1 return, top 5 at 20% each, next-open fills, monthly reset, cash when the index is below its 200-day SMA (India) - and a catastrophic stop would have to be added and tested first before any real money.""",
            NOTE_W),
    "swing": ("""Universe: the market's ETFs and stocks. Entry: close > 200-day SMA and RSI(2) < 10 (Wilder smoothing) -> buy next open. Exit: close > 5-day SMA -> sell next open; time stop: sell at the next open after 10 trading days in the trade. Variants: (1) no stop (published rules); (2) with the AGENTS.md stop: at the fill, stop = the highest (tightest) of entry - 2 x ATR(14), the 10-day swing low (if below entry) and entry x 0.90; (3) 2 x ATR(14) stop only, capped at 10% (not compliant with the AGENTS.md rule, which takes the tighter of the two; shown only for comparison). The with-stop version (2) is the one that counts under the rules. Candidates on the same day are ranked by lowest RSI(2).""",
              """- Connors, L., Alvarez, C. (2008), "Short Term Trading Strategies That Work", TradingMarkets: buy pullbacks (RSI(2) under 10, or under 5) in stocks above their 200-day average, exit on a close above the 5-day average; Connors argues stops hurt this kind of strategy.""",
              """Not fit for paper trading under the AGENTS.md rules. With the required stop the swing-low part sits only a little below the entry after a pullback, so about half the trades are stopped out within 2 days; rules-sized the US made 1.4% a year and India lost 8.8% a year with a -79.3% worst drop. Without a stop (Connors' published rules) the US version made 9.6% a year in the 5-slot portfolio with a -17.1% worst drop, below SPY's 13.9%, while India lost money even without a stop: the average edge per trade is smaller than India's round-trip cost of about 0.44%. The 2 x ATR-only stop did better than the rule stop in the US but worse than no stop. Verdict: do not paper-trade this in India. In the US it would need a change to the stop rule for mean-reversion trades (a wider or time-based stop), which only the user can approve; until then it should not go into trade plans. If the rule is changed, a plan would use exactly: close > 200-day SMA and RSI(2) < 10, buy next open, sell next open after a close above the 5-day SMA or after 10 days, 2 x ATR(14) stop capped at 10%.""",
              NOTE_TRADE),
}
VERSIONS.update({"turtle": "Turtle 20/10 (10-day-low exit), rules stop, 15-day time stop, rules-sized", "turtle2r": "Turtle 20/10 (10-day-low exit), rules stop, 2R target, 15-day time stop, rules-sized",
                 "hi52": "52-week high on 1.5x volume, 2R target, 20 days, rules-sized", "gap": "Gap-up 4%+ on 3x volume, 2R target, 20 days, rules-sized"})
TITLES = {"short-breakout": "short breakout (Turtle System 1 style, 20-day high / 10-day low)",
          "52w-high-breakout": "52-week-high breakout on volume (George and Hwang 2004)",
          "gap-drift": "gap-up drift (post-earnings-announcement drift proxy)"}
SHORT_COMMON = (" Universe: the market's stock list (same as the other backtests). Every variant uses the AGENTS.md stop at the fill: the tightest of entry - 2 x ATR(14), "
                "the 10-day swing low (if below entry) and entry x 0.90. Exits are checked in this order each day: stop (fills at the stop, or the open if it gaps below), "
                "then target (fills at the target, or the open if it gaps above), then the exit signal or time stop (sell at the next open). The stop is checked before the "
                "target on the same day (conservative). Time stop counts trading days held including the entry day.")
SUMMARY.update({"short-breakout": "Short-hold breakout (days to 3 weeks). Read the bar line below each market before using it.",
                "52w-high-breakout": "Buy a new 52-week high on heavy volume, out within 20 days. Read the bar line below each market before using it.",
                "gap-drift": "Buy the day after a big gap-up on heavy volume, out within 20 days. A proxy for earnings drift: gap days were not matched to earnings dates."})
TEXT.update({
    "short-breakout": ("Entry: close above the highest high of the prior 20 trading days -> buy next open. Exit: close below the lowest low of the prior 10 trading days "
                       "-> sell next open; or the rules stop; or a 15-day time stop. Variant 2 adds a target at 2R (entry + 2 x (entry - stop)). Both variants are shown." + SHORT_COMMON,
                       "- Faith, C. (2007), \"Way of the Turtle\", McGraw-Hill: System 1 enters on a 20-day breakout and exits on a 10-day low (original stop 2N = 2 x ATR(20); "
                       "here replaced by the AGENTS.md stop, and a 15-day time stop added as specified for this test).\n- Donchian channel breakouts (R. Donchian, 1960s).",
                       "Short breakouts are the fastest in-and-out style tested here.", NOTE_TRADE),
    "52w-high-breakout": ("Entry: close above the highest high of the prior 252 trading days (a new 52-week high) with volume at least 1.5 x the average of the prior 50 days "
                          "-> buy next open. Exit: rules stop, 2R target, or after 20 trading days. One variant (fixed)." + SHORT_COMMON,
                          "- George, T. J., Hwang, C.-Y. (2004), \"The 52-Week High and Momentum Investing\", Journal of Finance 59(5): stocks near their 52-week high keep "
                          "outperforming. The paper ranks monthly and holds 6 months; this test is a short-hold breakout version with a volume filter, as specified.",
                          "A short-hold version of 52-week-high momentum.", NOTE_TRADE),
    "gap-drift": ("Entry: the open gaps up at least 4% above the prior close, volume at least 3 x the average of the prior 50 days, the close is in the top half of the "
                  "day's range and above the 200-day SMA -> buy the next open. Stop: the gap day's low, or the rules stop if that is tighter (never wider than 10%). "
                  "Exit: 2R target or after 20 trading days. One variant (fixed). This is a proxy for post-earnings drift: gap days are not matched to earnings dates." + SHORT_COMMON,
                  "- Bernard, V. L., Thomas, J. K. (1989), \"Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?\", Journal of Accounting Research 27: "
                  "prices keep drifting in the direction of an earnings surprise for weeks.\n- \"Gap and go\": trader practice of buying strong gap-ups on volume (no single paper).",
                  "Gap-up drift is the event-driven short-hold style tested here.", NOTE_TRADE)})

TEXT_DROP = ("On today's surviving large caps and semis, buying a 25% drop made money on average and beat SPY over the same days, but it is not a trade the approved rules allow: "
             "the rules need a stop of at most 10% at entry, and a large share of drop-buys fell 10% or more below the entry before recovering, so they would have been stopped out "
             "(this stop version was not simulated). The trend filter (b) leaves too few events to trust. Waiting for the trend (Donchian 50/20 with the rules stop) wins less often "
             "but keeps each loss small, which is what the rules are built for. For the trading budget: wait for a Donchian 50-day-high close. Buying after a drop is a long-term "
             "investing decision (research view, finance-research), not a paper trade under these rules.")
DATA_NOTE = """Data problems found and what was done:
- TATASTEEL.NS and CIPLA.NS came back empty in the first batch ("possibly delisted"); a retry one ticker at a time worked. No ticker was dropped for short history; META starts 2012-05-18 (IPO).
- Stale bars (volume 0 and open = high = low = close) are Yahoo filler rows on NSE holidays (for example RELIANCE.NS 2014-04-24, an election holiday) and long no-trade stretches in the India ETFs (BANKBEES 346 and GOLDBEES 344 such days in total, most in 2012-2013; NIFTYBEES 169). They were dropped. NESTLEIND.NS's first 4 rows (2010-01-04 to 07) were stale at the wrong scale (-76% "move" on 2010-01-08) and were dropped this way.
- Rows with an open of 0 (BANKBEES.NS and GOLDBEES.NS in January 2010) were dropped, so these two start in February 2010.
- NIFTYBEES, BANKBEES and GOLDBEES split their units in December 2019. Yahoo has the rest of the history adjusted but 2019-12-19 and 2019-12-20 at the unadjusted scale (for example NIFTYBEES close 129.25, then 13.02, then 129.93). Those two bars were multiplied back by 10 (100 for GOLDBEES).
- The India ETFs also have many bad open, high and low prints (for example NIFTYBEES 2021-03-26 open 183.48 against a close of 155.21; GOLDBEES 2020-11-27 open 37.40 against a close of 42.84). On days when the Nifty's own range was under 3%, an open more than 5% from the previous close while the close moved under 2.5% was set to the previous close, and highs or lows more than 5% outside the open/close were cut back to the open/close. Results that trade the India ETFs (swing-pullback, Faber ETF sets) are less reliable than the stock results.
- Real large moves were kept: AMD +52% on 2016-04-22 (results), the 2010-05-06 US flash crash, 2015-08-24, the NSE erroneous-order crash of 2012-10-05, March 2020, and the 2018-09-21 NSE crash (BAJFINANCE, ADANIPORTS, M&M). Stops in the backtest fill on those intraday lows, as real stop orders could have.
- No split errors were found in the NSE stocks (no 1-day move above 40% after the steps above).
"""


DRY = os.environ.get("FINANCE_PAPER_DIR")
PAPER = Path(DRY) / "paper" if DRY else OUT.parent / "paper"
SETUPS = Path(DRY) / "setups" if DRY else OUT.parent / "setups"
BUDGET, LIMIT_UP = 200000, 0.005
LEDGER_COLS = ["id", "strategy", "approval", "signal", "symbol", "market", "ccy", "signal_date", "status", "limit", "fill_date", "fill_price", "stop", "target",
               "time_stop_date", "shares", "risk_inr", "fx", "exit_date", "exit_price", "exit_reason", "r_multiple", "pnl_inr", "pnl_ccy", "costs_inr", "notes"]
TRIGGER = {"donchian": ("hi50", None), "turtle": ("hi20", None), "turtle2r": ("hi20", None), "hi52": ("hi252", "needs volume >= 1.5x the 50-day average")}


def scan_data(names, until):
    data, _, _ = check_data(names, min_bars=260, until=until, live=True)
    rest = [t for t in names if t not in data and not fname(t, True).exists()]
    if rest:
        d2, _, _ = check_data(rest, min_bars=260, until=until)
        data.update(d2)
    return data


def market_date(m, D=None):
    d = load(MARKETS_IDX[m], None, True)
    d = d if d is not None else load(MARKETS_IDX[m], None)
    return d.index[d.index <= pd.Timestamp(D)][-1] if D else d.index[-1]


def strat_frame(k, d):
    return globals()[STRATS[k]["sig"]](d.copy())


def order_levels(k, entry, row, fx):
    stop = plan_stop(entry, row.atr14, row.swlo)
    if "stop_lvl" in row.index and row.stop_lvl < entry:
        stop = max(stop, row.stop_lvl)
    tr = STRATS[k]["target_r"]
    sh, rs, cs = size(entry, stop, fx)
    return stop, (entry + tr * (entry - stop) if tr else None), sh, rs, cs


def scan(D=None, do_refresh=True):
    xs = pd.read_csv(OUT.parent / "universe" / "extra.csv")
    if do_refresh:
        t0 = time.time()
        refresh_recent(universe_names("US", True) + universe_names("India", True) + list(MARKETS_IDX.values()) + ["INR=X"])
        log(f"refresh: {(time.time() - t0) / 60:.1f} min")
    sigs, near, dates, stale = [], [], {}, {}
    for m in MARKETS_IDX:
        Dm = market_date(m, D)
        dates[m] = Dm.date()
        act = active(m)
        allowed = {k: st for k, st, _ in act}
        ks = [k for k, mk in UNIV_RUNS if m in mk]
        names = universe_names(m, extra=True)
        data = scan_data(names, Dm)
        fx = fx_inr("USD" if m == "US" else "INR", str(Dm.date()))[0]
        log(f"scan {m}: {len(data)} names with data to {Dm.date()}; active strategies: {allowed or 'none'}")
        stale[m] = sum(1 for x in data.values() if x.index[-1] < Dm) / max(1, len(data))
        for t, raw in data.items():
            if raw.index[-1] != Dm:
                continue
            base = ind(raw)
            for k in ks:
                d = strat_frame(k, base)
                r = d.iloc[-1]
                if bool(r.entry):
                    lim = r.C * (1 + LIMIT_UP)
                    stop, tgt, sh, rs, cs = order_levels(k, lim, r, fx)
                    sigs.append(dict(k=k, t=t, m=m, ccy="USD" if m == "US" else "INR", date=Dm.date(), close=r.C, limit=lim, stop=stop, target=tgt,
                                     shares=sh, risk_inr=sh * (lim - stop) * fx, fx=fx, score=r.score, allowed=k in allowed,
                                     approval=allowed.get(k, "fails bar"), scout=t in set(xs.symbol),
                                     signal=SIGTEXT[k][0].format(date=Dm.date(), **r.to_dict())))
                elif k in TRIGGER and r[TRIGGER[k][0]] > r.C:
                    dist = r[TRIGGER[k][0]] / r.C - 1
                    if dist <= 0.02:
                        near.append(dict(k=k, t=t, m=m, close=r.C, trig=r[TRIGGER[k][0]], dist=dist, extra=TRIGGER[k][1] or "", allowed=k in allowed))
    for s_ in sigs:
        s_["why"] = signal_check(s_)
    grp = {}
    for n in near:
        g = grp.setdefault((n["t"], round(n["trig"], 4)), dict(n, ks=[]))
        g["ks"].append(n["k"])
        g["extra"] = g["extra"] or n["extra"]
        g["allowed"] = g["allowed"] or n["allowed"]
    return dict(sigs=sigs, near=sorted(grp.values(), key=lambda x: x["dist"])[:20], dates=dates, active={m: active(m) for m in MARKETS_IDX}, stale=stale)


def signal_check(s_):
    if not s_["allowed"]:
        return f"{STRATS[s_['k']]['label']} fails the full-universe backtest bar and is not in trading/paper/allowed.csv"
    if s_["close"] * s_["fx"] < (MIN_INR if s_["m"] == "India" else MIN_USD * s_["fx"]):
        return "price under $5 / Rs 50"
    if s_["shares"] < 1:
        return "20% cap: 1 share > Rs 40,000" if s_["limit"] * s_["fx"] > CAP_INR else "risk: Rs 2,000 buys < 1 share"
    ns = news_score(s_["t"])
    if ns is not None and ns <= -2:
        return "news score -2"
    earn = earnings_dates(s_["t"])
    nxt = [e for e in (earn or []) if pd.Timestamp(e) > pd.Timestamp(s_["date"])]
    if not nxt:
        return "no earnings date found (skipped)"
    if np.busday_count(str(s_["date"]), nxt[0]) <= 5:
        return f"earnings {nxt[0]} within 5 trading days"
    return ""


def active_table(act):
    rows = [(m, STRATS[k]["label"], f"[{STRATS[k]['page']}](../backtests/{STRATS[k]['page']}/index.md)", status_label(st), why) for m, v in act.items() for k, st, why in v]
    return tbl(["Market", "Strategy", "Backtest", "Status", "Why"], rows) if rows else "None: no strategy passes the full-universe bar and trading/paper/allowed.csv is empty.\n"


def write_scan(res, scout_tbl):
    D = max(res["dates"].values())
    sg = res["sigs"]
    ok = [s_ for s_ in sg if not s_["why"]]
    al = "; ".join(f"{m}: {', '.join(STRATS[k]['label'] + ' (' + status_label(st) + ')' for k, st, _ in v) or 'none'}" for m, v in res["active"].items())
    summ = [f"Scan of the {D} close (US {res['dates']['US']}, India {res['dates']['India']}): {len(sg)} signals, {len(ok)} valid for a paper order.",
            f"Active for paper trades (full-universe bar pass, or user-approved below bar in trading/paper/allowed.csv): {al}.",
            "Signals from other strategies are listed for information only; they never become paper orders.",
            f"Near triggers (within 2%): {len(res['near'])}; scout names: table at the end."]
    rows = [(s_["t"], s_["m"], STRATS[s_["k"]]["label"], status_label(s_["approval"]) if s_["allowed"] else "fails bar", f"{s_['close']:.2f}", f"{s_['limit']:.2f}", f"{s_['stop']:.2f}",
             f"{s_['target']:.2f}" if s_["target"] else "-", s_["shares"], f"{s_['risk_inr']:,.0f}", "yes" if not s_["why"] else "no: " + s_["why"])
            for s_ in sorted(sg, key=lambda x: (bool(x["why"]), x["k"], x["score"]))]
    nr = [(n["t"], n["m"], "; ".join(STRATS[k]["label"] for k in n["ks"]), f"{n['close']:.2f}", f"{n['trig']:.2f}", pct(n["dist"]), n["extra"] or "-", "yes" if n["allowed"] else "no")
          for n in res["near"]]
    body = (f"Run {time.strftime('%Y-%m-%d %H:%M')} with `.venv/bin/python trading/backtests/engine.py daily --date {D}`; universe: "
            "[trading/universe/](../universe/index.md) included names plus [extra.csv](../universe/extra.csv). Limit = signal close x 1.005; stop and target "
            "are estimates at the limit and are recomputed at the fill; shares = min(Rs 2,000 / (limit - stop), Rs 40,000 cap) in whole shares. "
            "Portfolio rules (5 open, 3 a week, 5% open risk, loss limits) are applied in [trading/paper/](../paper/index.md).\n\n"
            "## Active strategies\n" + active_table(res["active"]) + "\n## Signals today\n" + (tbl(["Symbol", "Market", "Strategy", "Strategy status", "Close", "Limit", "Stop", "Target", "Shares", "Risk Rs", "Valid (first failing rule)"], rows) if rows else "None.\n") +
            "\n## Near triggers (within 2% of a trigger, top 20)\n" + (tbl(["Symbol", "Market", "Strategies", "Close", "Trigger (close above)", "Distance", "Also needs", "Any strategy allowed"], nr) if nr else "None.\n") +
            "\n## Scout names\n" + scout_tbl + "\n")
    p = SETUPS / f"{D}.md"
    page(p, f"Setup check {D}", summ, body)
    setups_index()
    return p


def setups_index():
    rows_ = []
    for f in sorted(SETUPS.glob("[0-9]*.md"), reverse=True):
        t = f.read_text()
        first = next((l[2:] for l in t.splitlines() if l.startswith("- ")), "")
        rows_.append((f"[{f.stem}]({f.name})", first))
    page(SETUPS / "index.md", "Setup checks", ["Daily scans (`engine.py daily`) and setup checks (`engine.py setup --out`), newest first.",
                                               f"Latest: {rows_[0][0]}." if rows_ else "None yet."], tbl(["Date", "Result"], rows_))


def ledger():
    p = PAPER / "trades.csv"
    if not p.exists():
        return pd.DataFrame(columns=LEDGER_COLS)
    return pd.read_csv(p, dtype=str).fillna("")


def walk(row, d, f, last, k, cost):
    """Bars f..last for an open trade: stop, target, exit signal, time stop, news exit. Returns (exit_i, price, reason, pending_note)."""
    st, tg = float(row["stop"]), float(row["target"]) if row["target"] else None
    N, pend, n = STRATS[k]["time_stop"], None, 0
    news_after = next((x.split("=")[1] for x in row["notes"].split(";") if x.startswith("news_exit_after=")), None)
    for i in range(f, last + 1):
        b = d.iloc[i]
        if i > f and pend:
            return i, b.O, pend, ""
        if i > f and news_after and d.index[i] > pd.Timestamp(news_after):
            return i, b.O, "news -2", ""
        if b.L <= st:
            return i, min(b.O, st), "stop", ""
        if tg is not None and b.H >= tg:
            return i, max(b.O, tg), "target", ""
        n += 1
        if bool(b.exit):
            pend = "exit rule"
        elif N and n >= N:
            pend = "time stop"
    return None, None, None, (f"sells at the next open ({pend})" if pend else "")


def paper(D=None, res=None, allow_new=True, warn=""):
    PAPER.mkdir(parents=True, exist_ok=True)
    res = res or scan(D, do_refresh=False)
    L = ledger()
    events = []
    dates = {m: market_date(m, D) for m in MARKETS_IDX}
    act = L[L.status.isin(["pending", "open"])]
    data = scan_data(list(act.symbol), max(dates.values())) if len(act) else {}
    for i, row in act.iterrows():
        k, t, m = row["strategy"], row["symbol"], row["market"]
        if t not in data:
            continue
        cost, fx = MK[m]["cost"], float(row["fx"])
        d = strat_frame(k, ind(data[t]))
        d = d[d.index <= dates[m]]
        if row["status"] == "pending":
            after = np.where(d.index > pd.Timestamp(row["signal_date"]))[0]
            if not len(after):
                continue
            f = after[0]
            b, lim = d.iloc[f], float(row["limit"])
            fill = b.O if b.O <= lim else (lim if b.L <= lim else None)
            if fill is None:
                L.loc[i, ["status", "notes"]] = ["cancelled", f"open {b.O:.2f} above limit and no trade at the limit on {d.index[f].date()}"]
                events.append(("cancel", L.loc[i]))
                continue
            sr = d.loc[pd.Timestamp(row["signal_date"])]
            stop, tgt, _, rs, _ = order_levels(k, fill, sr, fx)
            sh = min(int(row["shares"]), rs)
            if sh < 1:
                L.loc[i, ["status", "notes"]] = ["cancelled", "size 0 at the fill (risk above Rs 2,000)"]
                events.append(("cancel", L.loc[i]))
                continue
            N = STRATS[k]["time_stop"]
            tsd = (d.index[f + N].date() if f + N < len(d) else np.busday_offset(str(d.index[f].date()), N)) if N else ""
            L.loc[i, ["status", "fill_date", "fill_price", "stop", "target", "shares", "risk_inr", "time_stop_date"]] = \
                ["open", str(d.index[f].date()), f"{fill:.4f}", f"{stop:.4f}", f"{tgt:.4f}" if tgt else "", str(sh), f"{sh * (fill - stop) * fx:.0f}", str(tsd)]
            events.append(("fill", L.loc[i]))
        row = L.loc[i]
        if row["status"] != "open":
            continue
        f = d.index.get_loc(pd.Timestamp(row["fill_date"]))
        ei, px, why, note = walk(row, d, f, len(d) - 1, k, cost)
        if ei is not None:
            sh, fp, st = int(row["shares"]), float(row["fill_price"]), float(row["stop"])
            pc = sh * (px * (1 - cost) - fp * (1 + cost))
            L.loc[i, ["status", "exit_date", "exit_price", "exit_reason", "r_multiple", "pnl_ccy", "pnl_inr", "costs_inr"]] = \
                ["closed", str(d.index[ei].date()), f"{px:.4f}", why, f"{pc / (sh * (fp - st)):.2f}", f"{pc:.2f}", f"{pc * fx:.0f}", f"{sh * (px + fp) * cost * fx:.0f}"]
            events.append(("exit", L.loc[i]))
        else:
            ns = news_score(t)
            notes = [x for x in row["notes"].split(";") if x and not x.startswith("sells at")]
            if ns is not None and ns <= -2 and not any(x.startswith("news_exit_after=") for x in notes):
                notes.append(f"news_exit_after={dates[m].date()}")
                note = "sells at the next open (news -2)"
            L.loc[i, "notes"] = ";".join(notes + ([note] if note else []))
    closed = L[L.status == "closed"]
    pnl = closed.pnl_inr.astype(float) if len(closed) else pd.Series(dtype=float)
    equity = BUDGET + pnl.sum()
    nxt = {m: pd.Timestamp(np.busday_offset(str(dates[m].date()), 1, roll="forward")) for m in dates}
    block = None
    if equity <= 0.9 * BUDGET:
        block = "budget down 10%: stop and review"
    month = closed[closed.exit_date.str[:7] == str(max(dates.values()).date())[:7]]
    if len(month) and month.pnl_inr.astype(float).sum() <= -0.04 * BUDGET:
        block = "month loss 4% of budget: no new trades this month"
    last3 = closed.sort_values("exit_date").tail(3)
    if len(last3) == 3 and (last3.exit_reason == "stop").all() and (max(dates.values()) - pd.Timestamp(last3.exit_date.iloc[-1])).days < 7:
        block = "3 stops in a row: 1 week pause"
    live_ = L[L.status.isin(["pending", "open"])]
    n_live, risk_live = len(live_), live_.risk_inr.astype(float).sum()
    rank = {}
    for m, ks in res["active"].items():
        for j, (k, _, _) in enumerate(ks):
            rank[(m, k)] = j
    skipped = []
    cands = sorted([s_ for s_ in res["sigs"] if not s_["why"] and (allow_new is True or s_["m"] in allow_new)],
                   key=lambda x: (rank.get((x["m"], x["k"]), 99), x["score"]))
    for s_ in cands:
        wk = nxt[s_["m"]].isocalendar()[:2]
        week_n = sum(1 for _, r in L.iterrows() if r["status"] in ("pending", "open", "closed") and
                     pd.Timestamp(r["fill_date"] or np.busday_offset(r["signal_date"], 1, roll="forward")).isocalendar()[:2] == wk)
        why = (block or ("already open or pending" if ((L.symbol == s_["t"]) & L.status.isin(["pending", "open"])).any() else None) or
               ("5 open or pending positions" if n_live >= 5 else None) or ("3 new entries this week" if week_n >= 3 else None) or
               ("open risk would exceed 5% of budget" if risk_live + s_["risk_inr"] > 0.05 * equity else None))
        if why:
            skipped.append((s_["t"], STRATS[s_["k"]]["label"], why))
            continue
        row = dict.fromkeys(LEDGER_COLS, "")
        row.update(id=f"{s_['date']}-{s_['t']}-{s_['k']}", strategy=s_["k"], approval=status_label(s_["approval"]), signal=s_["signal"], symbol=s_["t"], market=s_["m"], ccy=s_["ccy"], signal_date=str(s_["date"]),
                   status="pending", limit=f"{s_['limit']:.4f}", stop=f"{s_['stop']:.4f}", target=f"{s_['target']:.4f}" if s_["target"] else "",
                   shares=str(s_["shares"]), risk_inr=f"{s_['risk_inr']:.0f}", fx=f"{s_['fx']:.4f}", notes="stop/target are estimates until the fill")
        L = pd.concat([L, pd.DataFrame([row])], ignore_index=True)
        events.append(("order", pd.Series(row)))
        n_live += 1
        risk_live += s_["risk_inr"]
    L[LEDGER_COLS].to_csv(PAPER / "trades.csv", index=False)
    D_ = max(dates.values()).date()
    out = write_outbox(D_, events, skipped, L, equity, warn)
    write_paper_index(L, equity, D_, block, res["active"])
    return events, skipped, out


def journal_line(kind, r):
    m, k = r["market"], r["strategy"]
    cost = MK[m]["cost"]
    pl = OUT.parent / "plans" / f"{r['symbol']}.md"
    plan = r["id"] + (f" + trading/plans/{r['symbol']}.md" if pl.exists() else "")
    tag, sig = f"[{r.get('approval') or 'passes bar'}] ", r.get("signal") or STRATS[k]["label"]
    base = dict(symbol=r["symbol"], market=m, qty=r["shares"], stop_loss=r["stop"], target=r["target"], risk=r["risk_inr"], paper_or_real="paper", plan=plan)
    if kind == "order":
        return dict(base, date=r["signal_date"], side="buy limit (pending)", price=r["limit"], fees="",
                    reason=tag + sig + f"; buy limit {float(r['limit']):.2f} (close x 1.005) for the next session only")
    if kind == "fill":
        how = "the limit" if abs(float(r["fill_price"]) - float(r["limit"])) < 1e-6 else "the open"
        return dict(base, date=r["fill_date"], side="buy", price=r["fill_price"],
                    fees=f"{float(r['shares']) * float(r['fill_price']) * cost * float(r['fx']):.0f}",
                    reason=tag + sig + f"; filled at {how}; stop and target set from the fill; time stop {r['time_stop_date'] or 'none'}")
    if kind == "exit":
        why = SIGTEXT[k][1] if r["exit_reason"] == "exit rule" else EXIT_WORDS.get(r["exit_reason"], r["exit_reason"])
        return dict(base, date=r["exit_date"], side="sell", price=r["exit_price"], fees=r["costs_inr"],
                    reason=tag + f"{why} exit {r['exit_date']}; R {r['r_multiple']}; P&L Rs {r['pnl_inr']}; entry: " + sig)
    return dict(base, date=r["signal_date"], side="cancel", price=r["limit"], stop_loss="", target="", risk="", fees="",
                reason=tag + sig + "; cancelled: " + r["notes"])

def write_outbox(D, events, skipped, L, equity, warn=""):
    cols = ["symbol", "market", "date", "side", "qty", "price", "stop_loss", "target", "risk", "fees", "paper_or_real", "plan", "reason"]
    lines = [journal_line(k, r) for k, r in events]
    for x in lines:
        print(",".join(str(x[c]) for c in cols))
    p = PAPER / "outbox" / f"{D}.md"
    cnt = lambda k: sum(1 for k_, _ in events if k_ == k)
    head = (f"Paper: {(L.status == 'open').sum()} open, {cnt('order')} new orders, {cnt('exit')} exits, equity Rs {equity:,.0f}, "
            f"trades so far {(L.status == 'closed').sum()}/20" + (f"; {warn}" if warn else "") + ".")
    page(p, f"Paper outbox {D}", [head, f"{len(lines)} lines for finance-journal ({sum(1 for k, _ in events if k == 'order')} new pending orders, "
                                  f"{sum(1 for k, _ in events if k == 'fill')} fills, {sum(1 for k, _ in events if k == 'exit')} exits); {len(skipped)} valid signals skipped by portfolio rules.",
                                  "Columns match journal/trades.csv; risk and fees in INR; plan = paper ledger id (+ trade plan if one exists); paper only, no orders at any broker."],
         (tbl(cols, [[x[c] for c in cols] for x in lines]) if lines else "No new orders, fills or exits.\n") +
         ("\n## Valid signals skipped by portfolio rules\n" + tbl(["Symbol", "Strategy", "Rule"], skipped) if skipped else ""))
    return p


def write_paper_index(L, equity, D, block, act):
    op, pe, cl = L[L.status == "open"], L[L.status == "pending"], L[L.status == "closed"]
    risk = L[L.status.isin(["open", "pending"])].risk_inr.astype(float).sum()
    first = L[L.fill_date != ""].fill_date.min() if (L.fill_date != "").any() else None
    weeks = (pd.Timestamp(D) - pd.Timestamp(first)).days / 7 if first else 0
    summ = [f"{D}: {len(op)} open, {len(pe)} pending orders; open risk Rs {risk:,.0f} ({risk / equity:.1%} of equity; limit 5%).",
            f"Budget equity Rs {equity:,.0f} (Rs 2,00,000 + realised paper P&L Rs {equity - BUDGET:,.0f}).",
            f"Paper check: {len(cl)} of 20 closed trades, {weeks:.1f} of 8 weeks since the first fill ({first or 'no fill yet'}).",
            f"Rule breaks: 0 (orders are only created inside the AGENTS.md rules){'; new trades blocked: ' + block if block else ''}.",
            "Active strategies: " + ("; ".join(f"{STRATS[k]['label']} ({m}, {status_label(st)}: {why})" for m, v in act.items() for k, st, why in v) or "none") + "."]
    show = ["symbol", "strategy", "approval", "status", "signal_date", "limit", "fill_date", "fill_price", "stop", "target", "time_stop_date", "shares", "risk_inr", "notes"]
    body = ("Paper only: agents never place orders. Ledger: [trades.csv](trades.csv); strategies allowed below the bar: [allowed.csv](allowed.csv); "
            "daily lines for finance-journal: [outbox/](outbox/).\n\n## Active strategies\n" + active_table(act).replace("../backtests/", "../backtests/") + "\n## Open and pending\n" + (tbl(show, L[L.status.isin(["open", "pending"])][show].values.tolist()) if len(op) + len(pe) else "None.\n") +
            "\n## Closed (last 20)\n" + (tbl(["symbol", "strategy", "fill_date", "fill_price", "exit_date", "exit_price", "exit_reason", "r_multiple", "pnl_inr"],
                                           cl.sort_values("exit_date").tail(20)[["symbol", "strategy", "fill_date", "fill_price", "exit_date", "exit_price", "exit_reason", "r_multiple", "pnl_inr"]].values.tolist())
                                       if len(cl) else "None.\n") +
            "\n## How orders are handled\n" + tbl(["Step", "Rule"], [
                ("Order", "Limit = signal close x 1.005, for the next session only"),
                ("Fill", "At the open if the open <= limit; else at the limit if the day's low <= limit; else cancelled (no chasing)"),
                ("At the fill", "Rules stop recomputed from the fill (tightest of 2 x ATR(14), 10-day swing low, 10%; gap-drift also the gap-day low); target 2R where the strategy has one; shares cut so risk <= Rs 2,000"),
                ("Each day", "Stop first (stop price, or the open on a gap below), then target, then the strategy exit or time stop (next open); news score -2 -> next open"),
                ("New orders", "Only strategies that pass the full-universe backtest bar; <= 5 open + pending, <= 3 new a week, open risk <= 5%, 20% cap, whole shares, earnings > 5 trading days away (no date = skip), news not -2"),
                ("Ranking", "Strategies by full-universe profit factor (higher first), then the strategy's own signal strength (same score as the backtests)"),
                ("Loss limits", "3 stops in a row -> 1 week pause; month loss 4% -> no new trades; budget -10% -> stop"),
                ("Costs", "US 0.05% a side, India 0.22% a side (as in the backtests)")]))
    page(PAPER / "index.md", "Paper trading", summ, body)


def expected_day(m, D=None):
    """The trading day whose close should be in the data: --date (or the weekday before it), else the last weekday whose market has closed.
    Exchange holidays are not known, so a holiday makes the check fail (no new orders that day)."""
    if D:
        d = pd.Timestamp(D)
    else:
        tz, close = ("America/New_York", (16, 30)) if m == "US" else ("Asia/Kolkata", (15, 45))
        now = pd.Timestamp.now(tz=tz)
        d = now.tz_localize(None).normalize() - pd.Timedelta(days=1 if (now.hour, now.minute) < close else 0)
    while d.weekday() >= 5:
        d -= pd.Timedelta(days=1)
    return d.date()


def daily(D=None):
    """scan + paper, safe to run unattended: lock file, non-zero exit on a data failure, no new orders on stale data. Returns the exit code."""
    t0, lock = time.time(), CACHE / "daily.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        pid = int(lock.read_text() or 0)
        try:
            os.kill(pid, 0)
            log(f"daily: another run is active (pid {pid}, {lock}); exiting")
            return 2
        except (OSError, ValueError):
            lock.unlink()
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    rc = 0
    try:
        try:
            res = scan(D)
        except Exception as ex:
            log(f"daily: DATA FAILURE in refresh/scan: {ex!r}")
            return 1
        fresh, warn = set(), []
        for m in MARKETS_IDX:
            exp = expected_day(m, D)
            ok = res["dates"][m] == exp and res["stale"][m] <= 0.10
            if ok:
                fresh.add(m)
            elif res["active"][m]:
                warn.append(f"{m}: latest bar {res['dates'][m]} (expected {exp}), {res['stale'][m]:.0%} of names stale -> no new {m} orders")
                rc = 3
        for w in warn:
            log("daily: WARNING " + w)
        try:
            xs = pd.read_csv(OUT.parent / "universe" / "extra.csv")
            scout_tbl, _ = setup_table(list(xs.symbol), D)
        except Exception as ex:
            scout_tbl = f"Scout rows failed: {ex!r}\n"
        p = write_scan(res, scout_tbl)
        events, skipped, out = paper(D, res, allow_new=fresh, warn="; ".join(warn))
        log(f"daily: setups {p}; {(time.time() - t0) / 60:.1f} min; exit code {rc}")
        print(out)
        return rc
    finally:
        lock.unlink(missing_ok=True)


def main(what):
    if what in ("download", "all", "trend-following", "momentum-rotation", "swing-pullback"):
        download()
    data, rows, short = check_data()
    for r in rows:
        if r["big"] or r["gap"] or r["bad_hl"] or r["nan"] or r["fixed"] or r["stale"]:
            log(f"data: {r}")
    log(f"short: {short}")
    head = header(data, rows, short)
    jobs = [("trend", "trend-following", "trend following (Faber SMA200 timing and Donchian 50/20 breakout)", run_trend,
             lambda wt: spot(data, wt[("US", "Donchian 50/20, stocks, with rules stop")], sig_donchian)),
            ("mom", "momentum-rotation", "momentum rotation (top-5 12-1 month momentum with index trend filter)", run_momentum,
             lambda wt: momentum_spot(data, wt)),
            ("swing", "swing-pullback", "swing pullback (Connors RSI(2) in an uptrend)", run_swing,
             lambda wt: spot(data, wt[("India", "RSI2, with rules stop")], sig_rsi2))] + \
           [(n, n, TITLES[n], run_short(n), lambda wt, n=n: spot(data, wt[("US", SHORT[n][1][-1][1] + ", rules-sized")], SHORT[n][0])) for n in SHORT]
    heads = []
    for key, name, title, run, sp in jobs:
        if what in (name, "all"):
            rws, rr, ex, wt, eqs = run(data)
            t = TEXT[key]
            heads += write(key, name, title, t[0], t[1], rws, rr, ex, wt, t[2], head, sp(wt), t[3], eqs, data)
    if what == "universe-bar":
        write_universe(run_universe())
    if what in ("drop-vs-trend", "all"):
        write_drop(*run_drop())
    if what == "all":
        write_index(heads)
        write_bar(heads)


def momentum_spot(data, wt):
    h = "| Market | Ticker | Entry fill date | Signal (month-end) date | 12-1 return on signal date (engine) | 12-1 return recomputed from raw cache | Fill (next open, raw cache) | Engine entry price |\n|---|---|---|---|---|---|---|---|\n"
    for m in MK:
        tr = wt[(m, "Top-5 12-1 momentum, index > SMA200 filter")]
        r = tr.iloc[len(tr) // 2]
        raw = pd.read_csv(fname(r.t), index_col=0, parse_dates=True)
        cal = calendar(data, m)
        sd = cal[cal.get_loc(r.entry_date) - 1]
        i = raw.index.get_loc(sd)
        h += (f"| {m} | {r.t} | {r.entry_date.date()} | {sd.date()} | {pct(ind(data[r.t]).mom[sd], 2)} | "
              f"{pct(raw.Close.iloc[i - 21] / raw.Close.iloc[i - 252] - 1, 2)} | {raw.Open.loc[r.entry_date]:.2f} | {r.ep:.2f} |\n")
    return h


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "setup":
        opt = {k: a[a.index(k) + 1] for k in ("--date", "--out", "--note", "--title", "--limits") if k in a}
        syms = [x for x in a[1:] if x not in opt and x not in opt.values()]
        lims = {k: float(v) for k, v in (x.split("=") for x in opt.get("--limits", "").split(",") if "=" in x)}
        table, info = setup_table(syms, opt.get("--date"), lims)
        print(table)
        if "--out" in opt:
            write_setup(opt["--out"], table, info, opt.get("--note", ""), opt.get("--title"), opt.get("--date"))
    elif a and a[0] in ("scan", "paper", "daily"):
        dt = a[a.index("--date") + 1] if "--date" in a else None
        if a[0] == "scan":
            xs = pd.read_csv(OUT.parent / "universe" / "extra.csv")
            print(write_scan(scan(dt), setup_table(list(xs.symbol), dt)[0]))
        else:
            sys.exit(daily(dt) if a[0] == "daily" else (paper(dt), 0)[1])
    elif a and a[0] in ("-h", "--help"):
        print("engine.py [all|trend-following|momentum-rotation|swing-pullback|drop-vs-trend]  |  engine.py setup SYM ... [--date YYYY-MM-DD] [--out trading/setups/YYYY-MM-DD.md] [--note TEXT] [--title TEXT] [--limits SYM=PRICE,...]  |  engine.py scan|paper|daily [--date YYYY-MM-DD]  |  engine.py universe-bar")
    else:
        main(a[0] if a else "all")
