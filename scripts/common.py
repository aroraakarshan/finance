import glob
import io
import json
import logging
import os
from functools import cache
from pathlib import Path

import pandas as pd


def finance_dir() -> Path:
    """Google Drive Finance folder; FINANCE_DATA overrides the default location."""
    if os.environ.get("FINANCE_DATA"):
        return Path(os.environ["FINANCE_DATA"]).expanduser()
    hits = glob.glob(os.path.expanduser("~/Library/CloudStorage/GoogleDrive-*/My Drive/Finance"))
    if not hits:
        raise SystemExit("Google Drive Finance folder not found; set FINANCE_DATA")
    return Path(hits[0])


def stocks_dir(broker: str) -> Path:
    return finance_dir() / "Investments" / "Stocks" / broker


# Every file pattern looked up by latest() and tax_files() in this process: (folder or glob, pattern, file or None).
# scripts.update reads it to report the files used per broker and the patterns that matched nothing.
LOOKUPS: list[tuple[str, str, Path | None]] = []

PRICE_CACHE = Path.home() / ".local" / "share" / "finance-cache" / "prices.json"


def latest(folder: Path, pattern: str) -> Path:
    """Newest file by name; exports carry the date in the name."""
    files = sorted(folder.glob(pattern))
    LOOKUPS.append((str(folder), pattern, files[-1] if files else None))
    if not files:
        raise SystemExit(f"no {pattern} in {folder}")
    return files[-1]


def every(folder: Path, pattern: str) -> list[Path]:
    """All files matching pattern in folder, sorted by name."""
    files = sorted(folder.glob(pattern))
    LOOKUPS.extend((str(folder), pattern, f) for f in files or [None])
    return files


def read_table(source, label: str, sheet=0) -> pd.DataFrame:
    """Read a sheet whose header row is the first row containing `label` (broker exports have banners above it)."""
    raw = pd.read_excel(source, sheet_name=sheet, header=None)
    rows = raw.index[raw.apply(lambda r: r.astype(str).str.strip().eq(label).any(), axis=1)]
    if len(rows) == 0:
        raise SystemExit(f"header '{label}' not found")
    start = rows[0]
    df = raw.iloc[start + 1:].copy()
    df.columns = [str(c).strip() for c in raw.iloc[start]]
    df = df.dropna(how="all")
    return df.loc[:, [c for c in df.columns if c != "nan"]]


def decrypt(path: Path, password: str) -> io.BytesIO:
    import msoffcrypto

    f = msoffcrypto.OfficeFile(open(path, "rb"))
    f.load_key(password=password)
    buf = io.BytesIO()
    f.decrypt(buf)
    buf.seek(0)
    return buf


def tax_files(broker: str, pattern: str) -> list[Path]:
    """Files in Tax/FY*/<broker>/ matching `pattern`, sorted by path."""
    files = sorted(finance_dir().glob(f"Tax/FY*/{broker}/{pattern}"))
    LOOKUPS.extend((f"Tax/FY*/{broker}", pattern, f) for f in files or [None])
    return files


def cached_prices() -> dict:
    """{symbol: {"price": float, "date": "YYYY-MM-DD"[, "prev": float, "prev_date": "YYYY-MM-DD"]}} from
    PRICE_CACHE (empty if none); prev is the price of the trading day before."""
    return json.loads(PRICE_CACHE.read_text()) if PRICE_CACHE.exists() else {}


def cache_prices(prices: dict[str, tuple]) -> None:
    """Add successful fetches {symbol: (price, date[, prev, prev_date])} to PRICE_CACHE. Without prev, a cached
    price of an earlier date becomes prev; a refetch of the same date keeps the cached prev."""
    c = cached_prices()
    for s, (p, d, *prev) in prices.items():
        day, old = f"{d:%Y-%m-%d}", c.get(s, {})
        e = {"price": float(p), "date": day}
        if prev and prev[0] == prev[0]:
            e.update(prev=float(prev[0]), prev_date=f"{prev[1]:%Y-%m-%d}")
        elif old.get("date", day) < day:
            e.update(prev=old["price"], prev_date=old["date"])
        elif old.get("date") == day and "prev" in old:
            e.update(prev=old["prev"], prev_date=old["prev_date"])
        c[s] = e
    PRICE_CACHE.parent.mkdir(parents=True, exist_ok=True)
    PRICE_CACHE.write_text(json.dumps(c, indent=1, sort_keys=True) + "\n")


def rs(x: float) -> str:
    """Rs with Indian digit grouping: Rs 2,83,13,674."""
    if pd.isna(x):
        return "-"
    sign, n = ("-" if round(x) < 0 else ""), f"{abs(x):.0f}"
    head, tail = n[:-3], n[-3:]
    while len(head) > 2:
        tail, head = f"{head[-2:]},{tail}", head[:-2]
    return f"{sign}Rs {head + ',' if head else ''}{tail}"


def num(s: str) -> float:
    return float(s.replace(",", "").replace("$", ""))


@cache
def pdf_text(path: Path) -> str:
    """Text of every page of a PDF, joined by newlines."""
    from pypdf import PdfReader

    logging.getLogger("pypdf").setLevel(logging.CRITICAL)  # "Advanced encoding not implemented" on every E*TRADE PDF
    return "\n".join(p.extract_text() for p in PdfReader(path).pages)
