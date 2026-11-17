"""Fidelity Stock Plan Services (NetBenefits): Microsoft RSU and ESPP shares (MSFT).

Exports:
  Salary/Microsoft/Stock/StockExport_<date>.xlsx
      Microsoft stock award portal export. Sheet 'Transactions' has every RSU vest: gross shares,
      fair market value, 'Shares For Taxes' (withheld, fractional, never reach Fidelity) and
      'Net Shares' (deposited at Fidelity). Fidelity itself has no release confirmation.
  Tax/FY*/Fidelity/Fidelity_<date>_Tradeconfirmations_TradeConfirmation.pdf
      ESPP purchases (quantity, price paid, market value at purchase). Some are not trades
      (Jan 2025: core money market fund change).
  Tax/FY*/Fidelity/Fidelity_<date>_Statements_<title>.pdf, Fidelity_Statement_<from>_to_<to>.pdf
      only for periods with activity; the title can name other months than the period inside.
      Read for the MSFT share count and US cost basis (ESPP at price paid, RSU at deposit value)
      at the period end, and for any sale ("You Sold" under Securities Bought & Sold).
  Investments/Stocks/Fidelity/Fidelity_ESPP_Activity_<year>.csv
      ESPP plan activity; only used to check that every purchase has a confirmation.

No sale has happened yet, so the sale line format is unknown: a sale found in a statement is
reported, not read. Dividends are paid in cash, not reinvested.
Cost basis is the market value at vest or purchase (Indian tax), so ESPP cost differs from the
statement's US cost basis (price paid).

Run: python -m scripts.brokers.fidelity
"""
import re
from pathlib import Path

import pandas as pd

from scripts.common import finance_dir, latest, num, pdf_text, stocks_dir, tax_files


def vests() -> pd.DataFrame:
    """RSU vests from the Microsoft stock export: when, award, gross, fmv, withheld, net."""
    f = latest(finance_dir() / "Salary" / "Microsoft" / "Stock", "StockExport_*.xlsx")
    df = pd.read_excel(f, sheet_name="Transactions", dtype={"Award ID": str})
    df = df[df["Transaction Type"] == "Stock Award Vest"]
    return pd.DataFrame({
        "when": pd.to_datetime(df["Transaction Date"]), "award": df["Award Type"].astype(str),
        "gross": df["Transaction Amt"].astype(float), "fmv": df["Fair Market Value"].astype(float),
        "withheld": df["Shares For Taxes"].astype(float), "net": df["Net Shares"].astype(float),
    }).sort_values("when").reset_index(drop=True)


def purchases() -> pd.DataFrame:
    """ESPP purchases from the trade confirmations: when, symbol, qty, paid (per share), fmv (per share)."""
    rows = {}
    for f in tax_files("Fidelity", "*Tradeconfirmations*.pdf"):
        t = pdf_text(f)
        m = re.search(r"YOU PURCHASED ([\d,.]+) AT \$([\d,.]+) PURCHASE PRICE", t)
        if not m:
            continue
        when = pd.to_datetime(re.search(r"PLAN on (\w{3}/\d\d/\d{4})", t)[1], format="%b/%d/%Y")
        value = re.search(r"SYMBOL: (\w+)\n[^\n]+\n\s*\$([\d,.]+)", t)  # first amount is 'Market Value at Purchase'
        qty = num(m[1])
        rows[when] = {"when": when, "symbol": value[1], "qty": qty, "paid": num(m[2]), "fmv": num(value[2]) / qty,
                      "file": f.name}
    return pd.DataFrame(rows.values()).sort_values("when").reset_index(drop=True)


def period(t: str):
    m = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4}) - ([A-Z][a-z]+ \d{1,2}, \d{4})", t)
    return pd.Timestamp(m[1]), pd.Timestamp(m[2])


def statements() -> pd.DataFrame:
    """One row per statement period: start, end, shares, us_cost, sales (count of 'You Sold' MSFT lines)."""
    rows = {}
    for f in tax_files("Fidelity", "*Statement*.pdf"):
        t = pdf_text(f)
        start, end = period(t)
        if "YearEnd" in f.name or (start.month, start.day, end.month, end.day) == (1, 1, 12, 31):
            continue
        m = re.search(r"\(MSFT\)\s+\S+ ([\d,.]+) \$[\d,.]+ \$[\d,.]+ (\$[\d,.]+|unknown)", t)
        cost = None if m and m[2] == "unknown" else num(m[2]) if m else 0.0  # some statements show cost "unknown"
        rows[(start, end)] = {
            "start": start, "end": end, "shares": num(m[1]) if m else 0.0, "us_cost": cost,
            "sales": len(re.findall(r"MICROSOFT CORP[^\n]*You Sold", t)), "file": f.name}
    return pd.DataFrame(rows.values()).sort_values("start").reset_index(drop=True)


def lots() -> pd.DataFrame:
    v, p = vests(), purchases()
    return pd.concat([
        pd.DataFrame({"Stock Symbol": "MSFT", "Type": "RSU", "Holding Since": v.when, "Quantity": v.net,
                      "Avg. Price ($)": v.fmv, "Paid ($)": 0.0, "US Cost ($)": v.net * v.fmv}),
        pd.DataFrame({"Stock Symbol": p.symbol, "Type": "ESPP", "Holding Since": p.when, "Quantity": p.qty,
                      "Avg. Price ($)": p.fmv, "Paid ($)": p.paid, "US Cost ($)": p.qty * p.paid}),
    ], ignore_index=True).sort_values("Holding Since").reset_index(drop=True)


def holdings() -> pd.DataFrame:
    """Open lots: Stock Symbol, Type (RSU/ESPP), Holding Since, Quantity, Avg. Price ($) = market value at
    acquisition, Paid ($) per share, Cost ($). No sales yet, so every lot is open."""
    h = lots()
    h["Cost ($)"] = h["Quantity"] * h["Avg. Price ($)"]
    return h.drop(columns="US Cost ($)")


def trades() -> pd.DataFrame:
    """Standard trade table: symbol, when, side, qty, price, amount, fee, order_type.
    Only acquisitions (BUY at market value: RSU net shares, ESPP shares); no sale has happened."""
    h = lots()
    return pd.DataFrame({
        "symbol": h["Stock Symbol"], "when": h["Holding Since"], "side": "BUY", "qty": h["Quantity"],
        "price": h["Avg. Price ($)"], "amount": h["Quantity"] * h["Avg. Price ($)"], "fee": 0.0, "order_type": h["Type"],
    })


def checks() -> list[str]:
    notes = []
    s, lt, p = statements(), lots(), purchases()
    for prev, nxt in zip(s.itertuples(), list(s.itertuples())[1:]):
        if nxt.start > prev.end + pd.Timedelta(days=1):
            gap = lt[(lt["Holding Since"] > prev.end) & (lt["Holding Since"] < nxt.start)]
            what = f"; {len(gap)} acquisitions in it ({', '.join(f'{d:%Y-%m-%d}' for d in gap['Holding Since'])})" if len(gap) else ""
            notes.append(f"no statement for {prev.end + pd.Timedelta(days=1):%Y-%m-%d} to {nxt.start - pd.Timedelta(days=1):%Y-%m-%d}{what}")
    for st in s.itertuples():
        if st.sales:
            notes.append(f"statement {st.file} has {st.sales} MSFT sale(s); sales are not read yet, add them to trades()")
        # an ESPP purchase settles 1-2 days after the purchase date; RSU shares are deposited on the vest date
        e = lt[lt["Holding Since"] + pd.to_timedelta((lt.Type == "ESPP") * 2, unit="D") <= st.end]
        if pd.isna(st.us_cost):
            notes.append(f"statement {st.end:%Y-%m-%d} shows the cost basis as unknown")
        if abs(e.Quantity.sum() - st.shares) > 1e-3 or (pd.notna(st.us_cost) and abs(e["US Cost ($)"].sum() - st.us_cost) > 1):
            notes.append(f"statement {st.end:%Y-%m-%d}: {st.shares:g} shares, US cost {st.us_cost}; "
                         f"files give {e.Quantity.sum():g} shares, ${e['US Cost ($)'].sum():,.2f}")
    for f in sorted(stocks_dir("Fidelity").glob("Fidelity_ESPP_Activity_*.csv")):
        a = pd.read_csv(f, encoding="utf-8-sig")
        for r in a[a["Transaction Type"] == "Share purchase"].itertuples():
            when, qty = pd.Timestamp(r[1]), num(r.Quantity.split()[0])
            hit = p[p.when == when]
            if hit.empty:
                notes.append(f"ESPP purchase {when:%Y-%m-%d} ({qty:g} shares, {f.name}) has no trade confirmation")
            elif abs(hit.qty.iloc[0] - qty) > 1e-6:
                notes.append(f"ESPP purchase {when:%Y-%m-%d}: {hit.qty.iloc[0]:g} shares in the confirmation, {qty:g} in {f.name}")
    return notes


def main():
    pd.set_option("display.width", 200)
    h = holdings()
    print(h.round({"Quantity": 4, "Avg. Price ($)": 2, "Paid ($)": 2, "Cost ($)": 2}).to_string(index=False))
    by = h.groupby("Type").agg(shares=("Quantity", "sum"), cost=("Cost ($)", "sum"))
    print(by.round(2).to_string())
    print(f"MSFT {h.Quantity.sum():.3f} shares, cost (market value at acquisition) ${h['Cost ($)'].sum():,.2f}")
    s = statements().iloc[-1]
    print(f"latest statement {s.end:%Y-%m-%d}: {s.shares:g} shares, US cost basis {s.us_cost}")
    for n in checks():
        print("NOTE", n)


if __name__ == "__main__":
    main()
