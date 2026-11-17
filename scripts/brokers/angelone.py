"""Angel One: Indian stocks/ETFs and mutual funds.

Exports (Investments/Stocks/AngelOne):
  AngelOne_CombinedHolding_<date>.xlsx  password-protected (PAN in capitals); sheets Summary, Equity, Mutual Funds
  AngelOne_MF_Holdings_<date>.xlsx      not protected; mutual funds only

Run: python -m scripts.brokers.angelone   (asks for the password; or set ANGELONE_PASSWORD)
"""
import getpass
import os
import re

import pandas as pd

from scripts.common import decrypt, latest, read_table, stocks_dir, tax_files

NUM = ["Total Quantity", "Avg Trading Price", "LTP", "Invested Value", "Market Value", "Overall Gain/Loss"]
MF_NUM = ["Units", "Invested Value", "Unrealized P&L", "Unrealized P&L %"]
EQUITY_FILE = "AngelOne_CombinedHolding_*.xlsx"
MF_FILE = "AngelOne_MF_Holdings_*.xlsx"


def file_date(pattern: str) -> pd.Timestamp:
    """Date in the name of the newest file matching pattern."""
    return pd.Timestamp(latest(stocks_dir("AngelOne"), pattern).stem.rsplit("_", 1)[-1])


def equity(password: str) -> pd.DataFrame:
    src = decrypt(latest(stocks_dir("AngelOne"), EQUITY_FILE), password)
    df = read_table(src, "Company Name", sheet="Equity")
    df = df[df["Company Name"].notna() & (df["Client ID"] != "Total")]
    df[NUM] = df[NUM].apply(pd.to_numeric)
    return df[["Company Name", "MarketCap", "Sector"] + NUM].reset_index(drop=True)


def mutual_funds() -> pd.DataFrame:
    df = read_table(latest(stocks_dir("AngelOne"), MF_FILE), "Fund Name")
    df = df[df["Fund Name"].notna()]
    value = next(c for c in df.columns if c.startswith("Value as on"))
    df = df.rename(columns={value: "Market Value"})
    df[MF_NUM + ["Market Value"]] = df[MF_NUM + ["Market Value"]].apply(pd.to_numeric)
    return df[["Fund Name", "Category", "Sub Category"] + MF_NUM + ["Market Value"]].reset_index(drop=True)


def open_holdings() -> tuple[pd.DataFrame, pd.Timestamp]:
    """Stocks and ETFs from the 'Open Holdings' table of the newest TaxPnL (not password protected):
    isin, symbol, qty, avg_price, cost (buy value), close (its closing rate); and the download date."""
    files = tax_files("Angel One", "AngelOne_TaxPnL_*.xlsx")
    if not files:
        raise SystemExit("no AngelOne_TaxPnL_*.xlsx in Tax/FY*/Angel One")
    path = max(files, key=lambda f: (re.search(r"FY\d{4}-\d{2}", f.stem)[0], re.findall(r"\d{4}-\d{2}-\d{2}", f.stem)))
    raw = pd.read_excel(path, sheet_name="Equity+Bonds+SGB Trade Details", header=None)
    start = raw.index[raw[0].astype(str).str.startswith("Open Holdings")][0] + 1
    rows = []
    for r in raw.iloc[start + 1:].itertuples(index=False):
        if pd.isna(r[0]) or pd.isna(r[1]):
            break
        rows.append({"isin": r[0], "symbol": str(r[1]).strip(), "qty": float(r[2]), "avg_price": float(r[3]),
                     "cost": float(r[4]), "close": float(r[7])})
    return pd.DataFrame(rows), pd.Timestamp(re.findall(r"\d{4}-\d{2}-\d{2}", path.stem)[-1])


def main():
    pd.set_option("display.width", 200)
    pw = os.environ.get("ANGELONE_PASSWORD") or getpass.getpass("AngelOne file password: ")
    eq, mf = equity(pw), mutual_funds()
    print(eq.round(2).to_string(index=False))
    print()
    print(mf.round(2).to_string(index=False))
    for name, d in (("Equity", eq), ("Mutual funds", mf)):
        inv, val = d["Invested Value"].sum(), d["Market Value"].sum()
        print(f"{name}: invested {inv:,.0f}  value {val:,.0f}  gain {val - inv:,.0f} ({100 * (val / inv - 1):.2f}%)")


if __name__ == "__main__":
    main()
