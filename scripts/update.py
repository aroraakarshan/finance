"""One-command portfolio update: every broker reader, P&L, totals, Drive index, spreadsheet, site.

Order: broker readers (AngelOne, INDmoney, ETrade, IBKR, Fidelity, HDFC, gold), realised P&L
(INDmoney, IBKR, ETrade), totals (scripts.value), Drive index, portfolio/history/<date>.md and
portfolio/summary.md, <Drive>/Finance/Portfolio/portfolio.xlsx, daily marks and alerts
(scripts.mark: trading/positions.csv, trading/marks/, trading/alerts.md, portfolio/targets.md), the
market data for finance-news (scripts.market -> news/market/data/<date>.md, git-ignored; optional: a
failure is only a warning; skip with --no-market), the notes website (unless --no-site). Ends with a short summary: total now vs the last snapshot, change per account, the
files used per broker, file patterns that matched nothing, warnings.

AngelOne's combined holdings file needs its password (PAN in capitals): ANGELONE_PASSWORD, else a
prompt when run in a terminal; without it AngelOne keeps the figure of the last snapshot.
--offline: no network; prices, USD/INR and the gold rate come from the cache
(~/.local/share/finance-cache/prices.json; USD/INR: the FBIL reference rate in fbil-usdinr.json, see
scripts.value); without --offline the cache is used for anything the
network did not give. Everything else reads the local Google Drive files.

Run: python -m scripts.update [--offline] [--no-site] [--no-market]
"""
import argparse
import contextlib
import getpass
import io
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import pandas as pd

from scripts import drive_index, mark, pnl, value
from scripts.brokers import angelone, etrade, fidelity, gold, hdfc, ibkr, indmoney
from scripts.common import LOOKUPS, finance_dir, rs

REPO = Path(__file__).resolve().parent.parent
HISTORY = REPO / "portfolio" / "history"
SUMMARY = REPO / "portfolio" / "summary.md"
MARKET = REPO / "news" / "market" / "data"
GROUPS = [("angelone", "AngelOne"), ("indmoney", "INDmoney"), ("ibkr", "IBKR"), ("fidelity", "Fidelity"),
          ("etrade", "ETrade"), ("hdfc", "India bank"), ("india bank", "India bank"), ("gold", "Physical gold")]
INR_FMT = r"[>=10000000]##\,##\,##\,##0;[>=100000]##\,##\,##0;##,##0"


def group(name: str) -> str:
    n = name.lower()
    return next((g for key, g in GROUPS if key in n), name)


def crore(x: float) -> str:
    return f"Rs {x / 1e7:.2f} Cr" if abs(x) >= 1e7 else f"Rs {x / 1e5:.2f} L"


def plain(cell: str) -> str:
    return re.sub(r"[*`]", "", cell).strip()


def amount(cell: str) -> float:
    m = re.search(r"-?[0-9][0-9,]*(?:\.[0-9]+)?", plain(cell))
    return float(m.group(0).replace(",", "")) if m else float("nan")


def read_snapshot(path: Path) -> dict:
    """Date, total and account rows (name, inr, as_of) of a snapshot's 'Total investments' table."""
    text = path.read_text()
    m = re.search(r"^## Total investments.*?\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    rows, total = [], None
    for line in (m[1] if m else "").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or len(cells) < 3 or set(cells[0]) <= set("-: ") or plain(cells[0]) == "Account":
            continue
        if plain(cells[0]).lower() == "total":
            total = amount(cells[2])
        else:
            rows.append((plain(cells[0]), amount(cells[2]), plain(cells[3]) if len(cells) > 3 else ""))
    if total is None:
        total = sum(r[1] for r in rows if pd.notna(r[1]))
    return {"date": path.stem, "total": total, "rows": rows}


def by_group(rows) -> dict[str, float]:
    out: dict[str, float] = {}
    for name, inr, *_ in rows:
        if pd.notna(inr):
            out[group(name)] = out.get(group(name), 0.0) + inr
    return out


class Run:
    """Runs steps, keeps the files each step looked up and every warning."""

    def __init__(self):
        self.files: dict[str, list] = {}
        self.warnings: list[str] = []
        self.checks: list[str] = []

    def step(self, name: str, fn, quiet: bool = True):
        start = len(LOOKUPS)
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out) if quiet else contextlib.nullcontext():
                return fn()
        except (Exception, SystemExit) as e:
            self.warnings.append(f"{name}: {type(e).__name__}: {e}")
            return None
        finally:
            self.files.setdefault(name, []).extend(LOOKUPS[start:])


def file_lines(files: dict[str, list]) -> list[tuple[str, str, str]]:
    """[(step, file or 'NO MATCH <pattern>', saved date)] from the LOOKUPS of each step; a pattern is shown
    under the first step that used it; names masked."""
    out, seen = [], set()
    for step, found in files.items():
        by_pattern: dict[tuple, set] = {}
        for folder, pattern, path in found:
            by_pattern.setdefault((folder, pattern), set()).update([path] if path else [])
        for key, paths in by_pattern.items():
            if key in seen:
                continue
            seen.add(key)
            if not paths:
                where = f"{key[0]}/{key[1]}".replace(str(finance_dir()) + "/", "")
                out.append((step, drive_index.mask(f"NO MATCH {where}"), ""))
                continue
            newest = max(paths, key=lambda f: (f.stat().st_mtime, f.name))
            day = f"{datetime.fromtimestamp(newest.stat().st_mtime):%Y-%m-%d}"
            name = drive_index.mask(newest.name)
            out.append((step, name if len(paths) == 1 else f"{len(paths)} files {key[1]}, newest saved {name}", day))
    return out


def angelone_password(run: Run) -> str | None:
    pw = os.environ.get("ANGELONE_PASSWORD")
    if not pw and sys.stdin is not None and sys.stdin.isatty():
        try:
            pw = getpass.getpass("AngelOne file password (PAN in capitals; Enter to skip): ").strip()
        except (EOFError, KeyboardInterrupt):
            pw = None
    if not pw:
        run.warnings.append("AngelOne skipped: no password (ANGELONE_PASSWORD not set, no terminal or Enter); "
                            "its figure is carried from the last snapshot")
    return pw or None


def read_brokers(run: Run, pw: str | None) -> str | None:
    if pw and run.step("AngelOne", lambda: (angelone.equity(pw), angelone.mutual_funds())) is None:
        run.warnings.append("AngelOne: could not open the combined holdings file (wrong password?); "
                            "its figure is carried from the last snapshot")
        pw = None
    run.step("INDmoney", lambda: (indmoney.holdings(), indmoney.trades()))
    got = run.step("ETrade", lambda: (etrade.holdings(), etrade.checks()))
    run.checks += [f"ETrade: {n}" for n in (got[1] if got else [])]
    run.step("IBKR", lambda: (ibkr.holdings(), ibkr.cash(), ibkr.trades()))
    got = run.step("Fidelity", lambda: (fidelity.holdings(), fidelity.checks()))
    run.checks += [f"Fidelity: {n}" for n in (got[1] if got else [])]
    run.step("HDFC", lambda: (hdfc.fds(), hdfc.savings_balance()))
    run.step("Gold", gold.items)
    return pw


def realised(run: Run) -> list[str]:
    out = []
    for name in ["indmoney", "ibkr", "etrade"]:
        def one(name=name):
            sales, _, notes = pnl.realised(pnl.BROKERS[name].trades())
            r = sales.pnl.dropna().sum()
            return f"{name}: realised {'-' if r < 0 else ''}${abs(r):,.0f} over {len(sales)} sales ({len(set(notes))} notes; " \
                   f"`python -m scripts.pnl {name}`)"
        line = run.step(f"pnl {name}", one)
        if line:
            out.append(line)
    return out


# ---------- markdown ----------

def table(header: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def native(r) -> str:
    return f"${r.value:,.0f}" if r.currency == "USD" else rs(r.value)


def concentrations(s: dict, total: float) -> list[tuple[str, float]]:
    """Largest single holdings in INR: positions (summed over accounts), FDs, cash, physical gold, manual assets."""
    h = s["holdings"].groupby("symbol").inr.sum()
    acc = s["accounts"]
    pick = acc.name.str.contains("FDs|savings|cash|gold|stocks and ETFs|mutual funds", case=False) | \
        acc.source.str.startswith("manual:")
    for r in acc[pick].itertuples():
        if not (s["holdings"].account.str.startswith("AngelOne").any() and r.name.startswith("AngelOne")):
            h[r.name] = r.inr
    return [(k, v) for k, v in h.sort_values(ascending=False).head(10).items()]


def markdown(s: dict, today: date, last: dict | None, run: Run, pnl_lines: list[str], carried: bool) -> str:
    acc = s["accounts"]
    body, total = acc[acc.name != "Total"], float(acc.inr.iloc[-1])
    fd, it = s["fds"], s["gold"]
    rates, gday, gsource = s["gold_rate"]
    us_days = sorted({f"{d:%Y-%m-%d}" for d in s["holdings"][s["holdings"].market == "US"].price_date.dropna()})
    top = concentrations(s, total)
    lines = ["# Portfolio summary", "", "## Summary"]
    change = ""
    if last:
        d = total - last["total"]
        change = f", {'+' if round(d) > 0 else ''}{rs(d)} ({d / last['total']:+.1%}) since the {last['date']} snapshot"
    lines.append(f"Total {crore(total)} ({rs(total)}) on {today:%Y-%m-%d}{change}.")
    lines.append(f"Largest holding {top[0][0]} at {top[0][1] / total:.0%} of the total; HDFC FDs and savings "
                 f"{(fd.value.sum() + s['savings'][0]) / total:.0%}; physical gold {it.value_now.sum() / total:.1%}"
                 + "".join(f"; {r.name} {r.value / total:.0%}" for r in s["manual"].itertuples()) + ".")
    lines.append("AngelOne: last snapshot figure (no file password this run)." if carried
                 else "AngelOne: values of its export files.")
    lines.append(f"{len(run.warnings)} warnings (section Warnings).")
    lines += ["", f"Updated {today:%Y-%m-%d} by `python -m scripts.update` (generated; hand-written notes are in "
              f"[details.md](details.md)). US prices: yfinance closes of {', '.join(us_days)}. "
              f"USD/INR {s['fx']:.4f}: {s['fx_source']}. Gold: {gsource}. "
              "Spreadsheet: Google Drive `Finance/Portfolio/portfolio.xlsx`.", ""]
    lines += ["## Total investments in INR", table(
        ["Account", "Value", "In INR", "As of", "Source"],
        [[r.name, native(r), rs(r.inr), r.as_of, r.source] for r in body.itertuples()]
        + [["**Total**", "", f"**{rs(total)}**", "", f"US at USD/INR {s['fx']:.4f}"]]), ""]
    if last:
        then, now = by_group(last["rows"]), by_group([(r.name, r.inr) for r in body.itertuples()])
        rows = [[g, rs(then.get(g, float("nan"))), rs(now.get(g, float("nan"))),
                 rs(now.get(g, 0) - then.get(g, 0))] for g in dict.fromkeys([*now, *then])]
        lines += [f"## Change since the {last['date']} snapshot", table(
            ["Account", "Then", "Now", "Change"], rows + [["**Total**", rs(last["total"]), rs(total), rs(total - last["total"])]]),
            ""]
    lines += ["## Largest holdings", table(["Holding", "In INR", "Share of total"],
                                           [[k, rs(v), f"{v / total:.1%}"] for k, v in top]), ""]
    us = s["holdings"][s["holdings"].market == "US"].sort_values("inr", ascending=False)
    lines += ["## US holdings", table(["Symbol", "Account", "Shares", "Cost", "Value", "In INR"],
                                      [[r.symbol, r.account, f"{r.qty:,.4f}".rstrip("0").rstrip("."), f"${r.cost:,.0f}",
                                        f"${r.value:,.0f}", rs(r.inr)] for r in us.itertuples()]), ""]
    india = s["holdings"][s["holdings"].market == "India"].sort_values("inr", ascending=False)
    if len(india):
        lines += ["## AngelOne holdings", table(["Name", "Account", "Quantity", "Invested", "Value"],
                                                [[r.symbol, r.account, f"{r.qty:,.3f}", rs(r.cost), rs(r.value)]
                                                 for r in india.itertuples()]), ""]
    lines += [f"## HDFC fixed deposits (FD summary {fd.as_of.iloc[0]:%Y-%m-%d})",
              "Accrued interest to today; compounding taken from the maturity amount (`scripts.brokers.hdfc`). "
              "Before TDS.", "",
              table(["FD", "Principal", "Rate", "Start", "Maturity", "Compounding", "Accrued", "Value today"],
                    [[f"****{r.fd}", rs(r.principal), f"{r.rate}%", f"{r.start:%Y-%m-%d}", f"{r.maturity:%Y-%m-%d}",
                      r.compounding, rs(r.accrued), rs(r.value)] for r in fd.itertuples()]
                    + [["**Total**", rs(fd.principal.sum()), "", "", "", "", rs(fd.accrued.sum()), rs(fd.value.sum())]]), ""]
    by = it.groupby("purity").agg(grams=("grams", "sum"), paid=("paid", "sum"), value_now=("value_now", "sum"))
    lines += ["## Physical gold",
              f"Rate per gram: 24K {rs(rates[24])}, 22K {rs(rates[22])}, 18K {rs(rates[18])} ({gsource}). Value = net gold "
              "weight x rate; stones, making and GST are not counted in the value. AED at the invoice-date rate "
              "(`scripts.brokers.gold`).", "",
              table(["Date", "Seller", "Item", "Purity", "Grams", "Gold on invoice", "Making", "Stones, other",
                     "Discount", "GST/VAT", "Paid", "Value now"],
                    [[f"{r.date:%Y-%m-%d}", r.seller, r.description, r.purity, f"{r.grams:.3f}", rs(r.gold_value),
                      rs(r.making), rs(r.other), rs(r.discount), rs(r.tax), rs(r.paid), rs(r.value_now)]
                     for r in it.itertuples()]), "",
              table(["Purity", "Grams", "Paid", "Value now"],
                    [[k, f"{r.grams:.3f}", rs(r.paid), rs(r.value_now)] for k, r in by.iterrows()]
                    + [["**Total**", f"{it.grams.sum():.3f}", rs(it.paid.sum()), rs(it.value_now.sum())]]), ""]
    if pnl_lines:
        lines += ["## Realised P&L (average cost)", *[f"- {p}" for p in pnl_lines], ""]
    lines += ["## Files used", table(["Step", "File", "Saved"], [list(r) for r in file_lines(run.files)]), ""]
    lines += ["## Warnings", *([f"- {w}" for w in run.warnings + run.checks] or ["None."]), ""]
    return drive_index.mask("\n".join(lines))


# ---------- spreadsheet ----------

def workbook(s: dict, today: date, history: list[dict], path: Path) -> None:
    from openpyxl import Workbook
    from openpyxl.styles import Font
    from openpyxl.utils import get_column_letter

    acc = s["accounts"]
    body, total = acc[acc.name != "Total"], float(acc.inr.iloc[-1])
    wb = Workbook()
    wb.remove(wb.active)

    def cell(v):
        if isinstance(v, pd.Timestamp):
            return None if pd.isna(v) else v.to_pydatetime().date()
        if isinstance(v, float) and pd.isna(v):
            return None
        return v.item() if hasattr(v, "item") else v

    def sheet(title, header, rows, fmt=None, start=1):
        ws = wb[title] if title in wb.sheetnames else wb.create_sheet(title)
        for c, h in enumerate(header, 1):
            ws.cell(start, c, h).font = Font(bold=True)
        for r, row in enumerate(rows, start + 1):
            for c, v in enumerate(row, 1):
                x = ws.cell(r, c, cell(v))
                f = (fmt or {}).get(header[c - 1])
                if f:
                    x.number_format = f
                elif isinstance(x.value, date):
                    x.number_format = "yyyy-mm-dd"
        if start == 1:
            ws.freeze_panes = "B2"
        for c in range(1, ws.max_column + 1):
            width = max(len(str(ws.cell(r, c).value or "")) for r in range(1, ws.max_row + 1))
            ws.column_dimensions[get_column_letter(c)].width = min(max(width + 2, 10), 60)
        return ws

    money = {"In INR": INR_FMT, "INR": INR_FMT, "Principal": INR_FMT, "Accrued": INR_FMT, "Value today": INR_FMT,
             "Maturity amount": INR_FMT, "Total INR": INR_FMT, "Gold on invoice": INR_FMT, "Making": INR_FMT,
             "Stones, other": INR_FMT, "Discount": INR_FMT, "GST/VAT": INR_FMT, "Paid INR": INR_FMT,
             "Value now": INR_FMT, "% of total": "0.0%", "Value": "#,##0.00", "Cost": "#,##0.00",
             "Qty": "#,##0.0000", "Grams": "0.000", "Rate %": "0.00", "Rate now (per g)": "#,##0.00",
             "Paid (invoice currency)": "#,##0.00", "USD/INR": "0.0000"}
    top = concentrations(s, total)
    ws = sheet("Summary", ["Date", "Total INR", "USD/INR"], [[today, total, s["fx"]]], money)
    sheet("Summary", ["Account", "In INR", "% of total"],
          [[r.name, r.inr, r.inr / total] for r in body.itertuples()], money, start=4)
    sheet("Summary", ["Top concentrations", "In INR", "% of total"], [[k, v, v / total] for k, v in top], money,
          start=6 + len(body))
    ws.freeze_panes = "A2"
    sheet("Accounts", ["Account", "Currency", "Value", "Cost", "In INR", "% of total", "As of", "Source"],
          [[r.name, r.currency, r.value, r.cost, r.inr, r.inr / total, r.as_of, r.source] for r in body.itertuples()]
          + [["Total", "INR", None, None, total, 1.0, f"{today:%Y-%m-%d}", ""]], money)
    h = s["holdings"].sort_values("inr", ascending=False)
    sheet("Holdings", ["Symbol or name", "Account", "Market", "Qty", "Cost", "Value", "Currency", "In INR", "Price date"],
          [[r.symbol, r.account, r.market, r.qty, r.cost, r.value, r.currency, r.inr, r.price_date]
           for r in h.itertuples()], money)
    fd = s["fds"]
    sheet("FDs", ["FD (last 4)", "Principal", "Rate %", "Start", "Maturity", "Compounding", "Accrued", "Value today",
                  "Maturity amount"],
          [[r.fd, r.principal, r.rate, r.start, r.maturity, r.compounding, r.accrued, r.value, r.maturity_amount]
           for r in fd.itertuples()], money)
    cash = body[body.name.str.contains("cash|savings", case=False)]
    sheet("Cash", ["Account", "Currency", "Value", "In INR", "As of"],
          [[r.name, r.currency, r.value, r.inr, r.as_of] for r in cash.itertuples()], money)
    it = s["gold"]
    sheet("Gold", ["Date", "Seller", "Invoice", "Item", "Description", "Purity", "Grams", "Gold on invoice", "Making",
                   "Stones, other", "Discount", "GST/VAT", "Paid INR", "Currency", "Paid (invoice currency)", "FX",
                   "Rate now (per g)", "Value now"],
          [[r.date, r.seller, r.invoice, r.item, r.description, r.purity, r.grams, r.gold_value, r.making, r.other,
            r.discount, r.tax, r.paid, r.currency, r.paid_native, r.fx, r.rate_now, r.value_now] for r in it.itertuples()],
          money)
    groups = list(dict.fromkeys(g for hs in history for g in by_group(hs["rows"])))
    sheet("History", ["Date", "Total INR", *groups],
          [[pd.Timestamp(hs["date"]), hs["total"], *[by_group(hs["rows"]).get(g) for g in groups]] for hs in history],
          {**money, **{g: INR_FMT for g in groups}})
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def market_data(today: date, offline: bool) -> Path:
    """scripts.market in its own process: it needs TZ=UTC set before yfinance is imported."""
    out = MARKET / f"{today:%Y-%m-%d}.md"
    cmd = [sys.executable, "-m", "scripts.market", "--date", f"{today:%Y-%m-%d}", "--out", str(out)]
    r = subprocess.run(cmd + (["--offline"] if offline else []), cwd=REPO, env={**os.environ, "TZ": "UTC"},
                       capture_output=True, text=True, timeout=1800)
    if r.returncode:
        raise RuntimeError((r.stderr or r.stdout).strip().splitlines()[-1] if (r.stderr or r.stdout).strip() else f"exit {r.returncode}")
    return out


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--offline", action="store_true", help="no network: cached prices, USD/INR and gold rate")
    ap.add_argument("--no-site", action="store_true", help="do not rebuild the notes website")
    ap.add_argument("--no-market", action="store_true", help="do not write the market data (scripts.market)")
    args = ap.parse_args()
    today = date.today()
    snaps = [x for x in map(read_snapshot, sorted(HISTORY.glob("20??-??-??.md"))) if x["rows"]]
    earlier = [x for x in snaps if x["date"] < f"{today:%Y-%m-%d}"]
    last = earlier[-1] if earlier else snaps[-1] if snaps else None
    run = Run()
    pw = read_brokers(run, angelone_password(run))
    pnl_lines = realised(run)
    carry = [r for r in (last["rows"] if last else []) if group(r[0]) == "AngelOne"]
    carry = [(n, v, a if "from snapshot" in a else f"{a}; from snapshot {last['date']}") for n, v, a in carry]
    s = run.step("value", lambda: value.snapshot(args.offline, angelone_password=pw, carry=carry))
    if s is None:
        print("\n".join(run.warnings))
        raise SystemExit("totals failed; nothing written")
    run.warnings += s["notes"]
    run.step("drive_index", drive_index.main)
    text = markdown(s, today, last, run, pnl_lines, carried=not pw)
    out = HISTORY / f"{today:%Y-%m-%d}.md"
    out.write_text(re.sub(r"\]\((?![a-z]+:|/|#)", "](../", text))
    SUMMARY.write_text(text)
    history = [x for x in map(read_snapshot, sorted(HISTORY.glob("20??-??-??.md"))) if x["rows"]]
    xlsx = finance_dir() / "Portfolio" / "portfolio.xlsx"
    run.step("spreadsheet", lambda: workbook(s, today, history, xlsx))
    marked = run.step("mark", lambda: mark.run(s, args.offline))
    market = None if args.no_market else run.step("market", lambda: market_data(today, args.offline))
    if not args.no_site:
        from scripts import site
        run.step("site", lambda: (site.Site().build(), site.serve()), quiet=False)

    acc = s["accounts"]
    total = float(acc.inr.iloc[-1])
    print(f"\nTotal {rs(total)} ({crore(total)}) on {today:%Y-%m-%d}", end="")
    if last:
        d = total - last["total"]
        print(f"; last snapshot {last['date']} {rs(last['total'])}; change {rs(d)} ({d / last['total']:+.1%})")
        then, now = by_group(last["rows"]), by_group([(r.name, r.inr) for r in acc[acc.name != "Total"].itertuples()])
        for g in dict.fromkeys([*now, *then]):
            print(f"  {g:<14} {rs(then.get(g, float('nan'))):>16} -> {rs(now.get(g, float('nan'))):>16}  "
                  f"change {rs(now.get(g, 0) - then.get(g, 0))}")
    else:
        print()
    days = sorted({f"{d:%Y-%m-%d}" for d in s["holdings"].price_date.dropna()})
    print(f"Prices of {', '.join(days)}; USD/INR {s['fx']:.4f} ({s['fx_source']}); gold: {s['gold_rate'][2]}")
    print("Files used:")
    for name, f, d in file_lines(run.files):
        print(f"  {name:<12} {f}{f' ({d})' if d else ''}")
    for p in pnl_lines:
        print("P&L", p)
    for w in run.warnings:
        print("WARNING", w)
    for c in run.checks:
        print("CHECK", c)
    if marked:
        acts = [a for a in marked["alerts"] if a["level"] == "action"]
        print(f"Marks: {len(marked['positions'])} positions, marked {rs(marked['total'])}; "
              f"{len(acts)} alert(s) need action (trading/alerts.md)")
        for a in acts:
            print("ALERT", a["text"])
        for n in marked["notes"]:
            print("MARK", n)
    print(f"Wrote {out.relative_to(REPO)}, {SUMMARY.relative_to(REPO)}"
          f"{', ' + str(xlsx) if 'spreadsheet' in run.files and xlsx.exists() else ''}"
          f"{', ' + str(market.relative_to(REPO)) if market else ''}")


if __name__ == "__main__":
    main()
