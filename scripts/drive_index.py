"""Index of the documents in Google Drive Finance/, from file names only (no file is opened).

Classifies every file by top folder, broker or source, document type and period, and writes
portfolio/drive-index.md: per broker a table of document type -> periods covered, gaps inside the
covered range, file counts and the newest file date. Account numbers are masked to the last 4
digits. Folders that are not finance documents get one summary line each.

Run after every download: python -m scripts.drive_index
"""
import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

from scripts.common import finance_dir

OUT = Path(__file__).resolve().parent.parent / "portfolio" / "drive-index.md"

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
SNAPSHOT = {"holdings", "trades export", "FD summary"}
EVENT = {"trade confirmation", "ESPP/RSU confirmation", "other"}

# (pattern on the file stem, document type, kind); first match wins
RULES = [
    (r"^HDFC_CreditCard_", "credit card statement", "Credit card statement"),
    (r"^HDFC_Savings_.*InterestCert", "interest certificate", "Savings interest certificate"),
    (r"^HDFC_FD_InterestCert", "interest certificate", "FD interest certificate"),
    (r"^HDFC_Savings_", "savings statement", "Savings statement (PDF/XLS/CSV)"),
    (r"^HDFC_FD_Summary", "FD summary", "FD summary"),
    (r"^HDFC_TDS_Summary", "TDS", "TDS summary"),
    (r"^HDFC_TDS_Report", "TDS", "TDS report"),
    (r"^HDFC_16A_", "16A", "Form 16A"),
    (r"1042-?S", "1042-S", "1042-S"),
    (r"^AIS_", "AIS/TIS/26AS", "AIS"),
    (r"^TIS_", "AIS/TIS/26AS", "TIS"),
    (r"^Form26AS", "AIS/TIS/26AS", "26AS"),
    (r"^ForeignAssets", "AIS/TIS/26AS", "Foreign assets (portal)"),
    (r"^ITR(-V)?_.*Revised", "ITR", "ITR revised"),
    (r"^ITR_", "ITR", "ITR original"),
    (r"^Form67.*Revised", "ITR", "Form 67 revised"),
    (r"^Form67", "ITR", "Form 67"),
    (r"what_was_filed", "ITR", "Filed summary"),
    (r"Challan", "other", "Tax challan"),
    (r"^Form16|^Form12BA", "other", "Form 16 / 12BA"),
    (r"TaxComputation", "other", "Employer tax computation"),
    (r"Confirmation_ESPP", "ESPP/RSU confirmation", "ESPP purchase"),
    (r"Confirmation_RSRelease", "ESPP/RSU confirmation", "RS release"),
    (r"BankDepositProgram", "other", "Bank deposit program"),
    (r"(?i)TradeConfirmation", "trade confirmation", "TradeConfirmation"),
    (r"(?i)TaxPnL", "tax P&L", "TaxPnL"),
    (r"PnLSummary", "tax P&L", "PnLSummary"),
    (r"GainsLosses", "tax P&L", "GainsLosses"),
    (r"RealizedSummary", "tax P&L", "RealizedSummary"),
    (r"CapitalGains", "tax P&L", "MF CapitalGains"),
    (r"TaxOverview", "tax P&L", "TaxOverview"),
    (r"ConsolidatedTaxReport", "tax P&L", "ConsolidatedTaxReport"),
    (r"ClearTax", "tax P&L", "ClearTax US stocks"),
    (r"DP_TransactionHolding", "holdings", "DP transactions and holding"),
    (r"MF_Holdings", "holdings", "MF holdings"),
    (r"CombinedHolding", "holdings", "CombinedHolding"),
    (r"Holdings", "holdings", "Holdings"),
    (r"TradesCharges", "trades export", "TradesCharges"),
    (r"MF_Transactions", "trades export", "MF transactions"),
    (r"Trades", "trades export", "Trades"),
    (r"ESPP_Activity", "trades export", "ESPP activity"),
    (r"BenefitHistory", "trades export", "BenefitHistory"),
    (r"StockExport", "trades export", "StockExport (RSU vests)"),
    (r"ActivityStatement", "statement", "ActivityStatement"),
    (r"AccountStatement", "statement", "Account statement"),
    (r"US_Statement", "statement", "US statement"),
    (r"TransactionSummary", "statement", "TransactionSummary"),
    (r"YearEnd", "statement", "Year-end report"),
    (r"RecapofCash", "statement", "Cash management recap"),
    (r"Ledger", "statement", "Ledger"),
    (r"ELSS", "statement", "ELSS"),
    (r"Statement", "statement", "Statement"),
    (r"Payslip", "payslip", "Payslip"),
    (r"TaxDocuments", "other", "Tax documents"),
    (r"ADDRESSCHANGE|AnnualDisclosures|RequiredClientLetter", "other", "Letters and notices"),
    (r"^[A-Za-z]+_U?\d{4,}_\d{4}-\d{2}-\d{2}$", "statement", "Account statement"),
]


@dataclass
class Period:
    labels: set = field(default_factory=set)   # FY2025-26, CY2025, AY2026-27
    months: set = field(default_factory=set)   # (year, month) covered
    dates: set = field(default_factory=set)    # event or snapshot dates
    partial: dict = field(default_factory=dict)  # label -> "to <date>"
    ranges: list = field(default_factory=list)   # (from, to) of cumulative exports


def mask(text: str) -> str:
    """Mask PAN, IBKR accounts and long numbers; keep the last 4 digits."""
    text = re.sub(r"[A-Z]{5}\d{4}[A-Z]", "<PAN>", text)
    text = re.sub(r"\bU\d{3,}(\d{4})", r"U****\1", text)
    return re.sub(r"[A-Z]*\d{4,}(\d{4})(?=\D|$)", r"****\1", text)


def fy_months(y: int) -> set:
    return {(y, m) for m in range(4, 13)} | {(y + 1, m) for m in range(1, 4)}


def span(a: tuple, b: tuple) -> set:
    out, (y, m) = set(), a
    while (y, m) <= b:
        out.add((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def ymd(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def period(stem: str, fy_folder: str | None) -> Period:
    p = Period()
    s = re.sub(r"_dl\d{4}-\d{2}-\d{2}", "", stem)
    if m := re.search(r"(FY(\d{4})-\d{2}|CY(\d{4}))_to_(\d{4}-\d{2}-\d{2})", s):
        label, end = m[1], ymd(m[4])
        start = (int(m[2]), 4) if m[2] else (int(m[3]), 1)
        p.labels.add(label)
        p.partial[label] = f"to {end}"
        p.months |= span(start, (end.year, end.month))
        return p
    if m := re.search(r"FY(\d{4})-\d{2}_(\d{4})-(\d{2})$", s):
        p.months.add((int(m[2]), int(m[3])))
        return p
    if m := re.search(r"FY(\d{4})-(\d{2})", s):
        p.labels.add(m[0])
        p.months |= fy_months(int(m[1]))
        return p
    if m := re.search(r"AY(\d{4})-(\d{2})", s):
        p.labels.add(m[0])
        return p
    if m := re.search(r"(?:TY|CY)(\d{4})", s):
        p.labels.add(f"CY{m[1]}")
        p.months |= span((int(m[1]), 1), (int(m[1]), 12))
        return p
    if m := re.search(r"(\d{4})YearEnd|YearEnd\w*?_(\d{4})", s):
        y = int(m[1] or m[2])
        p.labels.add(f"CY{y}")
        p.months |= span((y, 1), (y, 12))
        return p
    names = "|".join(MONTHS)
    if m := re.search(rf"({names})({names})?(\d{{4}})Statement", s):
        a, b, y = MONTHS.index(m[1]) + 1, MONTHS.index(m[2] or m[1]) + 1, int(m[3])
        p.months |= span((y - 1 if a > b else y, a), (y, b))
        return p
    if m := re.search(r"(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})", s):
        a, b = ymd(m[1]), ymd(m[2])
        p.months |= span((a.year, a.month), (b.year, b.month))
        p.dates.add(b)
        p.ranges.append((a, b))
        return p
    if m := re.search(r"(\d{4})-(\d{2})_to_(\d{2})", s):
        p.months |= span((int(m[1]), int(m[2])), (int(m[1]), int(m[3])))
        return p
    if m := re.search(r"to_(\d{4}-\d{2}-\d{2})", s):
        p.dates.add(ymd(m[1]))
        return p
    if m := re.search(r"\d{4}-\d{2}-\d{2}", s):
        d = ymd(m[0])
        p.dates.add(d)
        p.months.add((d.year, d.month))
        return p
    if m := re.search(r"(\d{4})-(\d{2})(?!\d)", s):
        p.months.add((int(m[1]), int(m[2])))
        return p
    if m := re.search(r"_(\d{4})$", s):
        p.labels.add(f"CY{m[1]}")
        return p
    if fy_folder:
        p.labels.add(fy_folder)
        p.months |= fy_months(int(fy_folder[2:6]))
    return p


def classify(stem: str) -> tuple[str, str]:
    for pat, kind, label in RULES:
        if re.search(pat, stem):
            return kind, label
    return "other", "other"


def account(stem: str) -> str | None:
    m = re.match(r"[A-Za-z]+_(?:(?:CreditCard|Savings)_)?(U?)(\d{4,})_", stem)
    if not m or re.fullmatch(r"(19|20)\d{2}", m[2]):
        return None
    return f"{m[1]}****{m[2][-4:]}"


def ranges(items: list, step) -> list[tuple]:
    out = []
    for x in sorted(items):
        if out and step(out[-1][1]) == x:
            out[-1] = (out[-1][0], x)
        else:
            out.append((x, x))
    return out


def next_month(ym):
    y, m = ym
    return (y + 1, 1) if m == 12 else (y, m + 1)


def fmt_months(months: set, cap: int = 6) -> str:
    rs = ranges(list(months), next_month)
    parts = [f"{a[0]}-{a[1]:02d}" + ("" if a == b else f"..{b[0]}-{b[1]:02d}") for a, b in rs]
    if len(parts) > cap:
        return f"from {parts[0].split('..')[0]}, {len(parts) - cap} earlier ranges, " + ", ".join(parts[-cap:]) + f" ({len(months)} months)"
    return ", ".join(parts)


def fmt_labels(labels: set, partial: dict) -> tuple[str, str]:
    """Compressed year labels and the missing years between them."""
    shown, gaps = [], []
    for prefix in sorted({lab[:2] for lab in labels}):
        years = sorted(int(lab[2:6]) for lab in labels if lab.startswith(prefix))
        name = (lambda y: f"{prefix}{y}-{(y + 1) % 100:02d}") if prefix in ("FY", "AY") else (lambda y: f"{prefix}{y}")
        for a, b in ranges(years, lambda y: y + 1):
            shown.append(name(a) if a == b else f"{name(a)}..{name(b)}")
        gaps += [name(y) for y in range(years[0], years[-1] + 1) if y not in years]
    notes = [f"{k} {v}" for k, v in sorted(partial.items())]
    return ", ".join(shown) + (f" ({'; '.join(notes)})" if notes else ""), ", ".join(gaps)


@dataclass
class Doc:
    source: str
    fy: str | None
    where: str
    kind: str
    label: str
    account: str | None
    period: Period
    added: date


def walk(root: Path) -> tuple[list[Doc], dict]:
    docs, other = [], defaultdict(lambda: defaultdict(int))
    for dirpath, dirnames, files in os.walk(root):
        rel = Path(dirpath).relative_to(root).parts
        files = [f for f in files if not f.startswith(".")]
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        top = rel[0] if rel else ""
        if top in ("Salary", "Bills") or rel[:2] in (("Investments", "Research"), ("Investments", "Gold")) \
                or rel[:2] == ("Tax", "Employer document checklists") or rel in ((), ("Investments",)):
            key = "/".join(rel[:2]) if top != "Bills" else "Bills"
            for f in files:
                stem = Path(f).stem
                other[key]["files"] += 1
                if "Payslip" in stem:
                    other[key]["payslips"] += 1
                    m = period(stem, None).months
                    other[key].setdefault("payslip_months", set()).update(m)
                elif re.match(r"^[A-Z]{5}\d{17}_\d{4}$", stem):
                    other[key]["EPF passbooks"] += 1
                elif "StockExport" in stem:
                    other[key]["StockExport"] = stem.rsplit("_", 1)[-1]
            continue
        fy = next((p for p in rel if re.fullmatch(r"FY\d{4}-\d{2}", p)), None)
        if top == "Tax":
            source = rel[2] if len(rel) > 2 else None
        elif top == "Investments" and len(rel) > 2 and rel[1] == "Stocks":
            source = rel[2]
        elif top == "Guides":
            source = "Guides"
        elif top == "Banking" and len(rel) > 1:
            source = rel[1]
        else:
            source = "/".join(rel)
        for f in files:
            stem = Path(f).stem
            src = (source or ("Income Tax Site" if "Challan" in stem else "Tax (FY folder)")).replace("Angel One", "AngelOne")
            kind, label = ("guide", stem) if top == "Guides" else classify(stem)
            st = os.stat(os.path.join(dirpath, f))
            added = date.fromtimestamp(getattr(st, "st_birthtime", st.st_mtime))
            where = f"Tax/FY*/{rel[2]}" if top == "Tax" and len(rel) > 2 else "/".join(rel)
            docs.append(Doc(src, fy, where, kind, label, account(stem), period(stem, fy), added))
    return docs, other


def months_between(a, b) -> int:
    return (b[0] - a[0]) * 12 + b[1] - a[1]


def newest(p: Period, mon: set) -> str:
    """Newest date in the names: an explicit date, else a month, else a year label."""
    to = [d for d in p.dates] + [ymd(v[3:]) for v in p.partial.values()]
    if to:
        return str(max(to))
    if mon:
        y, m = max(mon)
        return f"{y}-{m:02d}"
    return max(p.labels, key=lambda lab: lab[2:]) if p.labels else "-"


def row(kind: str, label: str, docs: list[Doc]) -> str:
    p = Period()
    for d in docs:
        p.labels |= d.period.labels
        p.months |= d.period.months
        p.dates |= d.period.dates
        p.partial.update(d.period.partial)
        p.ranges += d.period.ranges
    gaps, mon = "", set()
    n = len(p.dates)
    if p.ranges and kind != "savings statement":
        cells = f"{min(a for a, _ in p.ranges)}..{max(b for _, b in p.ranges)} ({len(p.ranges)} cumulative exports)"
    elif kind in SNAPSHOT and p.dates and not p.labels:
        cells = f"as of {max(p.dates)}" + (f" ({n} dates, from {min(p.dates)})" if n > 1 else "")
    elif kind in EVENT and p.dates and not p.labels:
        cells = f"{n} dates, {min(p.dates)}..{max(p.dates)}" if n > 1 else f"1 date, {min(p.dates)}"
    else:
        lab, gaps = fmt_labels(p.labels, p.partial) if p.labels else ("", "")
        if "revised" in label or "summary" in label:
            gaps = ""
        dated = [d.period.months for d in docs if not d.period.labels and d.period.months]
        mon = set().union(*dated) if dated else set()
        step = 1
        if dated and all(len(m) == 1 for m in dated) and len(mon) > 1:
            ms = sorted(mon)
            step = min(months_between(a, b) for a, b in zip(ms, ms[1:]))
        cadence = {1: " monthly", 3: " quarterly", 12: " yearly"}.get(step, "") if len(mon) > 1 and dated and all(len(m) == 1 for m in dated) else ""
        cells = "; ".join(x for x in [lab, fmt_months(mon) + cadence if mon else ""] if x) or "no period in name"
        if p.months and (kind in ("statement", "payslip", "credit card statement", "savings statement") or not p.labels):
            covered = sorted(p.months)
            expected = {m for i, m in enumerate(sorted(span(covered[0], covered[-1])))
                        if i % step == 0} if not p.labels else span(covered[0], covered[-1])
            missing = expected - p.months
            gaps = fmt_months(missing) if missing else ""
    return f"| {kind} | {label} | {len(docs)} | {cells} | {gaps or '-'} | {newest(p, mon)} |"


def render(docs: list[Doc], other: dict) -> str:
    by_src = defaultdict(list)
    for d in docs:
        by_src[d.source].append(d)
    total = len(docs) + sum(v["files"] for v in other.values())
    out = [
        "# Drive index",
        "",
        f"Generated {date.today()} by `python -m scripts.drive_index` from file names in Google Drive",
        f"`Finance/` ({total} files; no file opened). Run it after every download. Periods come from the",
        "file names (\"Newest\" is the newest date in the names; \"Added\" is when the newest file was saved",
        "to Drive). Gaps are months or years missing inside the covered range, at the series' own cadence;",
        "brokers send quarterly statements in months without activity, so a monthly gap is not always a",
        "missing file. Account numbers show only the last 4 digits.",
        "",
        "## Brokers and sources",
        "| Broker / source | Files | Folders | Accounts | Added |",
        "|---|---|---|---|---|",
    ]
    for src in sorted(by_src, key=str.lower):
        ds = by_src[src]
        where = sorted({d.where for d in ds})
        accts = ", ".join(sorted({d.account for d in ds if d.account})) or "-"
        out.append(f"| {src} | {len(ds)} | {', '.join(where)} | {accts} | {max(d.added for d in ds)} |")
    for src in sorted(by_src, key=str.lower):
        ds = by_src[src]
        accts = sorted({d.account for d in ds if d.account})
        split = len(accts) > 1
        out += ["", f"## {src}"]
        per_fy = defaultdict(int)
        for d in ds:
            if d.fy:
                per_fy[d.fy] += 1
        if per_fy:
            out.append("Files per tax folder: " + ", ".join(f"{fy} {n}" for fy, n in sorted(per_fy.items())) + ".")
        out += ["", "| Type | Kind | Files | Periods | Gaps | Newest |", "|---|---|---|---|---|---|"]
        groups = defaultdict(list)
        for d in ds:
            groups[(d.kind, d.label + (f" {d.account}" if split and d.account else ""))].append(d)
        for (kind, label), g in sorted(groups.items()):
            out.append(row(kind, label, g))
    out += ["", "## Other folders (summary only)"]
    for key in sorted(other):
        v = other[key]
        parts = [f"{v['files']} file{'s' if v['files'] != 1 else ''}"]
        if v.get("payslips"):
            parts.append(f"{v['payslips']} payslips {fmt_months(v['payslip_months'])}")
        if v.get("EPF passbooks"):
            parts.append(f"{v['EPF passbooks']} EPF passbooks")
        if v.get("StockExport"):
            parts.append(f"StockExport {v['StockExport']} (RSU vests, read by fidelity.py)")
        out.append(f"- `{key}/` (top level)" if key in ("Investments", "") else f"- `{key}/`")
        out[-1] += ": " + ", ".join(parts)
    return mask("\n".join(out)) + "\n"


def main():
    root = finance_dir()
    docs, other = walk(root)
    OUT.write_text(render(docs, other))
    print(f"{len(docs)} documents indexed -> {OUT.relative_to(OUT.parent.parent)}")


if __name__ == "__main__":
    main()
