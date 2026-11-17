"""Market value of every account at the last prices, in USD and INR, with totals.

Holdings come from the broker readers (INDmoney export, IBKR newest Activity Statement plus its
cash, Fidelity lots; ETrade is empty). INDmoney cash is the dashboard wallet balance
(INDMONEY_CASH_USD below): statements and exports do not show the wallet. Prices: yfinance daily
close of the last trading day before today per symbol; USD/INR: FBIL reference rate (1 pm fix) of the
valuation date (newest US close date) or the business day before, from the RBI reference rate
archive (same day) or fbil.org.in (public data lags about a week), cached in
~/.local/share/finance-cache/fbil-usdinr.json; without one, yfinance 'INR=X' with a warning (its
dates are shifted: the bar dated D is about the onshore close of D-1). Every fetched
price is cached in ~/.local/share/finance-cache/prices.json; with --offline, or for a symbol the
network did not give, the cached price is used and its date reported. India bank (INR): HDFC
savings closing balance (newest statement CSV) plus FDs at principal + interest accrued to today
(scripts.brokers.hdfc). Physical gold: net gold weight x IBJA rate (scripts.brokers.gold). Assets
with no export (EPF, Punjab Gramin Bank): hand-entered rows of portfolio/manual-assets.csv.
AngelOne (INR, values of the export date) only with its file password (ANGELONE_PASSWORD), else
left out here (scripts.update carries the last snapshot figure).

Run: python -m scripts.value [--offline] [--indmoney-cash USD]
"""
import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path

import pandas as pd

from scripts.brokers import angelone, etrade, fidelity, gold, hdfc, ibkr, indmoney
from scripts.common import PRICE_CACHE, cache_prices, cached_prices

# INDmoney US wallet balance from the INDmoney app dashboard on this date. Not in any export or
# statement (INDmoney moves into the account only what each buy needs). Update with a new reading,
# or pass --indmoney-cash.
INDMONEY_CASH_USD = 4574.05
INDMONEY_CASH_DATE = "2026-11-15"
FX = "INR=X"
MANUAL = Path(__file__).resolve().parent.parent / "portfolio" / "manual-assets.csv"


def manual() -> pd.DataFrame:
    """Hand-entered assets with no export: symbol, name, account, asset, value (INR), as_of, source."""
    return pd.read_csv(MANUAL, dtype={"value": float}) if MANUAL.exists() else \
        pd.DataFrame(columns=["symbol", "name", "account", "asset", "value", "as_of", "source"])


def positions() -> pd.DataFrame:
    parts = []
    for name, mod in [("INDmoney", indmoney), ("IBKR", ibkr), ("ETrade", etrade), ("Fidelity", fidelity)]:
        h = mod.holdings()
        if len(h):
            g = h.groupby("Stock Symbol", as_index=False).agg(qty=("Quantity", "sum"), cost=("Cost ($)", "sum"))
            parts.append(g.assign(account=name).rename(columns={"Stock Symbol": "symbol"}))
    p = pd.concat(parts, ignore_index=True)
    return p[p.qty > 1e-6].reset_index(drop=True)


def closes(symbols: list[str], offline: bool = False) -> tuple[dict[str, tuple[float, pd.Timestamp]], list[str]]:
    """({symbol: (close, date)} for symbols and INR=X, notes). Last yfinance close before today, else the cache."""
    got, notes = {}, []
    if not offline:
        try:
            import yfinance as yf

            logging.getLogger("yfinance").setLevel(logging.CRITICAL)
            d = yf.download(symbols + [FX], period="10d", auto_adjust=False, progress=False)["Close"]
            d = d[d.index < pd.Timestamp.today().normalize()]
            fresh = {}
            for s in d.columns:
                c = d[s].dropna()
                if len(c):
                    got[s] = (float(c.iloc[-1]), c.index[-1])
                    fresh[s] = got[s] + ((float(c.iloc[-2]), c.index[-2]) if len(c) > 1 else ())
        except Exception as e:
            notes.append(f"yfinance failed: {e}")
        if got:
            cache_prices(fresh)
    cache, used = cached_prices(), []
    for s in symbols + [FX]:
        if s in got:
            continue
        if s in cache:
            got[s] = (cache[s]["price"], pd.Timestamp(cache[s]["date"]))
            used.append(f"{s} {cache[s]['date']}")
        else:
            notes.append(f"{s}: no price (not fetched and not cached)")
    if used:
        why = "offline" if offline else "not fetched (network?)"
        notes.append(f"{why}: cached prices used: {', '.join(used)}")
    if FX not in got:
        raise SystemExit("no USD/INR rate: not fetched and not cached")
    return got, notes


RBI_REFRATE_URL = "https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx"
FBIL_URL = "https://www.fbil.org.in/wasdm/refrates/fetchfiltered"
FBIL_CACHE = PRICE_CACHE.parent / "fbil-usdinr.json"


def fbil_fetch(start: pd.Timestamp, end: pd.Timestamp) -> tuple[dict[str, float], str]:
    """({YYYY-MM-DD: FBIL USD/INR reference rate}, site) between start and end: the RBI reference rate archive,
    else fbil.org.in. Raises when both fail."""
    import requests

    h, errors = {"User-Agent": "Mozilla/5.0"}, []
    try:
        s = requests.Session()
        page = s.get(RBI_REFRATE_URL, headers=h, timeout=30).text
        form = dict(re.findall(r'name="(__[A-Z]+)"[^>]*value="([^"]*)"', page))
        form.update(chkUSD="on", txtFromDate=f"{start:%d/%m/%Y}", txtToDate=f"{end:%d/%m/%Y}", btnSubmit=" GO ")
        r = s.post(RBI_REFRATE_URL, data=form, headers=h, timeout=30)
        r.raise_for_status()
        got = {f"{pd.to_datetime(d, format='%d/%m/%Y'):%Y-%m-%d}": float(v) for d, v in
               re.findall(r">\s*(\d\d/\d\d/\d{4})\s*<.*?>\s*(\d+\.\d+)\s*<", r.text, re.S)}
        if got:
            return got, "rbi.org.in"
        errors.append("RBI archive: no USD rows")
    except Exception as e:
        errors.append(f"RBI archive: {e}")
    try:
        r = requests.get(FBIL_URL, params={"fromDate": f"{start:%Y-%m-%d}", "toDate": f"{end:%Y-%m-%d}",
                                           "authenticated": "false"}, headers=h, timeout=30)
        r.raise_for_status()
        got = {x["processRunDate"][:10]: float(x["rate"]) for x in r.json() if x["subProdName"] == "INR / 1 USD"}
        if got:
            return got, "fbil.org.in"
        errors.append("fbil.org.in: no USD rows")
    except Exception as e:
        errors.append(f"fbil.org.in: {e}")
    raise RuntimeError("; ".join(errors))


def usdinr(day: pd.Timestamp, offline: bool = False) -> tuple[float, pd.Timestamp, str, list[str]] | None:
    """(rate, date, source, notes): FBIL USD/INR reference rate of day or the newest business day before it (at
    most 7 days), fetched (unless offline) and cached in FBIL_CACHE; None when there is none."""
    cache = json.loads(FBIL_CACHE.read_text()) if FBIL_CACHE.exists() else {}
    notes, site = [], cache.get("_site", {})
    key = f"{day:%Y-%m-%d}"
    if not offline and key not in cache:
        try:
            got, where = fbil_fetch(day - pd.Timedelta(days=10), day)
            cache.update(got)
            site.update(dict.fromkeys(got, where))
            cache["_site"] = site
            FBIL_CACHE.parent.mkdir(parents=True, exist_ok=True)
            FBIL_CACHE.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
        except Exception as e:
            notes.append(f"FBIL USD/INR fetch failed: {e}")
    days = [d for d in cache if d != "_site" and day - pd.Timedelta(days=7) <= pd.Timestamp(d) <= day]
    if not days:
        return None
    d = max(days)
    return cache[d], pd.Timestamp(d), f"FBIL reference rate of {d}, via {site.get(d, 'cache')}", notes


AMFI_URL = "https://portal.amfiindia.com/spages/NAVAll.txt"


def amfi() -> pd.DataFrame:
    """Every Indian mutual fund scheme of today's AMFI NAV file: code, isin, name, plan, option, nav, date."""
    import requests

    r = requests.get(AMFI_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
    r.raise_for_status()
    text = r.text
    rows = [line.split(";") for line in text.splitlines() if line.count(";") == 7 and line[:1].isdigit()]
    d = pd.DataFrame(rows, columns=["code", "isin", "isin2", "name", "plan", "option", "nav", "date"])
    d["nav"] = pd.to_numeric(d.nav, errors="coerce")
    d["date"] = pd.to_datetime(d.date, format="%d-%b-%Y", errors="coerce")
    return d.dropna(subset=["nav", "date"]).drop(columns="isin2")


def navs(codes: list[str], offline: bool = False, table: pd.DataFrame | None = None
         ) -> tuple[dict[str, tuple[float, pd.Timestamp]], list[str]]:
    """({'AMFI:<code>': (nav, date)}, notes) for AMFI scheme codes; cached like closes()."""
    keys, got, notes = [f"AMFI:{c}" for c in codes], {}, []
    if codes and not offline:
        try:
            t = amfi() if table is None else table
            t = t[t.code.isin(codes)]
            got = {f"AMFI:{r.code}": (r.nav, r.date) for r in t.itertuples()}
            if got:
                cache_prices(got)
        except Exception as e:
            notes.append(f"AMFI NAV fetch failed: {e}")
    cache, used = cached_prices(), []
    for k in keys:
        if k in got:
            continue
        if k in cache:
            got[k] = (cache[k]["price"], pd.Timestamp(cache[k]["date"]))
            used.append(f"{k} {cache[k]['date']}")
        else:
            notes.append(f"{k}: no NAV (not fetched and not cached)")
    if used:
        notes.append(f"{'offline' if offline else 'not fetched (network?)'}: cached NAVs used: {', '.join(used)}")
    return got, notes


def snapshot(offline: bool = False, indmoney_cash: float = INDMONEY_CASH_USD, angelone_password: str | None = None,
             carry: list[tuple[str, float, str]] = ()) -> dict:
    """Every account valued. Returns dict with accounts (name, currency, value, cost, inr, as_of, source; last
    row Total), holdings (account, market, symbol, qty, cost, value, currency, inr, price_date), fx, fx_day,
    fds, savings (balance, day, last4), gold (items valued), gold_rate (rates, day, source), manual (manual()), notes.
    carry: (name, inr, as_of) rows used for AngelOne when there is no password."""
    notes = []
    p = positions()
    px, n = closes(sorted(set(p.symbol)), offline)
    notes += n
    fx, fx_day = px[FX]
    fx_source = f"yfinance INR=X close of {fx_day:%Y-%m-%d}"
    ref = usdinr(p.symbol.map(lambda s: px.get(s, (None, pd.NaT))[1]).max(), offline)
    if ref:
        fx, fx_day, fx_source, n = ref
        notes += n
    else:
        warn = (f"WARNING no FBIL USD/INR reference rate (fetch failed or not cached); using {fx_source} "
                "(Yahoo dates are shifted about a day)")
        print(warn, file=sys.stderr)
        notes.append(warn)
    p["close"] = p.symbol.map(lambda s: px.get(s, (float("nan"), None))[0])
    p["price_date"] = p.symbol.map(lambda s: px.get(s, (None, pd.NaT))[1])
    p["value"] = p.qty * p.close
    hold = [pd.DataFrame({"account": p.account, "market": "US", "symbol": p.symbol, "qty": p.qty, "cost": p.cost,
                          "value": p.value, "currency": "USD", "inr": p.value * fx, "price_date": p.price_date})]
    rows = []

    def add(name, currency, value, cost, as_of, source):
        rows.append({"name": name, "currency": currency, "value": value, "cost": cost,
                     "inr": value * fx if currency == "USD" else value, "as_of": as_of, "source": source})

    if angelone_password:
        eq, mf = angelone.equity(angelone_password), angelone.mutual_funds()
        eq_day, mf_day = angelone.file_date(angelone.EQUITY_FILE), angelone.file_date(angelone.MF_FILE)
        add("AngelOne stocks and ETFs", "INR", eq["Market Value"].sum(), eq["Invested Value"].sum(),
            f"{eq_day:%Y-%m-%d}", "AngelOne combined holdings export (its LTP)")
        add("AngelOne mutual funds", "INR", mf["Market Value"].sum(), mf["Invested Value"].sum(),
            f"{mf_day:%Y-%m-%d}", "AngelOne MF holdings export (its NAV)")
        hold.append(pd.DataFrame({"account": "AngelOne", "market": "India", "symbol": eq["Company Name"],
                                  "qty": eq["Total Quantity"], "cost": eq["Invested Value"], "value": eq["Market Value"],
                                  "currency": "INR", "inr": eq["Market Value"], "price_date": eq_day}))
        hold.append(pd.DataFrame({"account": "AngelOne MF", "market": "India", "symbol": mf["Fund Name"],
                                  "qty": mf["Units"], "cost": mf["Invested Value"], "value": mf["Market Value"],
                                  "currency": "INR", "inr": mf["Market Value"], "price_date": mf_day}))
    else:
        for name, inr, as_of in carry:
            add(name, "INR", inr, float("nan"), as_of, "last snapshot (AngelOne skipped: no file password)")
        if not carry:
            notes.append("AngelOne left out: no file password (set ANGELONE_PASSWORD)")
    labels = {"INDmoney": "INDmoney US positions", "IBKR": "IBKR US positions", "Fidelity": "Fidelity (MSFT)"}
    for acct in ["INDmoney", "IBKR", "Fidelity", "ETrade"]:
        a = p[p.account == acct]
        day = a.price_date.max() if len(a) else pd.NaT
        if acct == "INDmoney":
            add(labels[acct], "USD", a.value.sum(), a.cost.sum(), f"{day:%Y-%m-%d}", "holdings export x yfinance close")
            add("INDmoney cash", "USD", indmoney_cash, indmoney_cash, INDMONEY_CASH_DATE, "INDmoney dashboard wallet")
        elif acct == "IBKR":
            st = ibkr.statements().iloc[-1]
            add(labels[acct], "USD", a.value.sum(), a.cost.sum(), f"{day:%Y-%m-%d}",
                f"Activity Statement to {st.end:%Y-%m-%d} x yfinance close")
            c = ibkr.cash()
            add("IBKR cash", "USD", c, c, f"{st.end:%Y-%m-%d}", "Activity Statement Cash Report")
        elif acct == "Fidelity":
            add(labels[acct], "USD", a.value.sum(), a.cost.sum(), f"{day:%Y-%m-%d}", "vests and ESPP x yfinance close")
        else:
            add("ETrade", "USD", a.value.sum(), a.cost.sum(), "-", "no shares left (moved to IBKR Dec 2025)")
    bal, sday, last4 = hdfc.savings_balance()
    add(f"HDFC savings ****{last4}", "INR", bal, bal, f"{sday:%Y-%m-%d}", "statement CSV closing balance")
    fd = hdfc.fds()
    add(f"HDFC FDs ({len(fd)}, principal + accrued)", "INR", fd.value.sum(), fd.principal.sum(),
        f"{pd.Timestamp.today():%Y-%m-%d}", f"FD summary {fd.as_of.iloc[0]:%Y-%m-%d}; interest accrued to today")
    it, gnotes = gold.items()
    notes += gnotes
    rates, gday, gsource = gold.rates(offline)
    it = gold.valued(it, rates)
    add(f"Physical gold ({it.grams.sum():.1f} g)", "INR", it.value_now.sum(), it.paid.sum(), f"{gday:%Y-%m-%d}",
        "invoices; net gold weight x IBJA rate")
    man = manual()
    for r in man.itertuples():
        add(r.name, "INR", r.value, r.value, r.as_of, f"manual: {r.source}")
    acc = pd.DataFrame(rows)
    total = pd.DataFrame([{"name": "Total", "currency": "INR", "value": acc.inr.sum(), "cost": float("nan"),
                           "inr": acc.inr.sum(), "as_of": "", "source": ""}])
    for r in p[p.close.isna()].itertuples():
        notes.append(f"{r.account} {r.symbol}: no price")
    return {"accounts": pd.concat([acc, total], ignore_index=True), "holdings": pd.concat(hold, ignore_index=True),
            "fx": fx, "fx_day": fx_day, "fx_source": fx_source, "fds": fd, "savings": (bal, sday, last4), "gold": it,
            "gold_rate": (rates, gday, gsource), "manual": man, "notes": notes}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--indmoney-cash", type=float, default=INDMONEY_CASH_USD,
                    help=f"INDmoney wallet cash in USD (default {INDMONEY_CASH_USD:,.2f}, dashboard {INDMONEY_CASH_DATE})")
    ap.add_argument("--offline", action="store_true", help="use cached prices (no network)")
    args = ap.parse_args()
    pd.set_option("display.width", 200)
    s = snapshot(args.offline, args.indmoney_cash, os.environ.get("ANGELONE_PASSWORD"))
    print(f"USD/INR {s['fx']:.4f} ({s['fx_source']}); gold: {s['gold_rate'][2]}\n")
    h = s["holdings"]
    print(h[h.market == "US"].drop(columns=["market", "currency"]).to_string(
        index=False, float_format="{:,.4f}".format, formatters={"price_date": "{:%Y-%m-%d}".format}))
    print("\n" + s["accounts"].to_string(index=False, float_format="{:,.2f}".format))
    fd = s["fds"]
    print(f"\nHDFC FDs: principal Rs {fd.principal.sum():,.2f} + accrued Rs {fd.accrued.sum():,.2f} "
          f"(FD summary {fd.as_of.iloc[0]:%Y-%m-%d})")
    for n in s["notes"]:
        print("NOTE", n)
    if args.indmoney_cash == INDMONEY_CASH_USD:
        print(f"NOTE INDmoney cash ${INDMONEY_CASH_USD:,.2f} is the dashboard wallet balance of {INDMONEY_CASH_DATE}")


if __name__ == "__main__":
    main()
