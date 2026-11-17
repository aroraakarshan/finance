"""Interactive Brokers (US stocks).

Exports:
  Investments/Stocks/IBKR/IBKR_<account>_TradeConfirmations_<from>_to_<to>.pdf
      Trade Confirmation Report. Each order has one summary line (exchange '-') followed by
      indented per-exchange fills; only the summary lines are read. Sells have negative quantities.
  Tax/FY*/IBKR/IBKR_[<account>_]ActivityStatement_<period>.csv
      Activity Statement (CSV: section, row kind, fields). The period is read from the file
      ('Statement,Data,Period'), not the name; periods overlap (CY2025, FY2025-26, quarters).
      Read: 'Open Positions' and 'Cash Report' (newest statement), 'Transfers' (shares moved in), 'Trades' (IBKR's
      own realised P/L). IBKR's cost basis for transferred shares is what the old broker sent
      (NXPI $77.615 = ESPP price paid), not the market value at purchase used here.

trades() adds every transfer in as a BUY (order_type TRANSFER_IN) at the cost of the lots that
left ETrade (etrade.transfers(): market value at release or purchase), so pnl.py has the cost.

Run: python -m scripts.brokers.ibkr
"""
import csv
import re

import pandas as pd

from scripts.brokers import etrade
from scripts.common import latest, num, pdf_text, stocks_dir, tax_files

LINE = re.compile(
    r"^U\d+ (?P<symbol>\S+) (?P<date>\d{4}-\d{2}-\d{2}), (?P<time>[\d:]+) \S+ - (?P<side>BUY|SELL) "
    r"(?P<qty>-?[\d,.]+) (?P<price>[\d,.]+) (?P<proceeds>-?[\d,.]+) (?P<comm>-?[\d,.]+) (?P<fee>-?[\d,.]+) (?P<type>\S+)"
)


def confirmations() -> pd.DataFrame:
    """Trades from the Trade Confirmation PDF."""
    pdf = latest(stocks_dir("IBKR"), "IBKR_*_TradeConfirmations_*.pdf")
    rows = []
    for line in pdf_text(pdf).splitlines():
        m = LINE.match(line.strip())
        if m:
            rows.append({
                "symbol": m["symbol"],
                "when": pd.Timestamp(f"{m['date']} {m['time']}"),
                "side": m["side"],
                "qty": abs(num(m["qty"])),
                "price": num(m["price"]),
                "amount": abs(num(m["proceeds"])),
                "fee": abs(num(m["comm"])) + abs(num(m["fee"])),
                "order_type": m["type"],
            })
    return pd.DataFrame(rows)


def section(path, name: str) -> pd.DataFrame:
    """One section of an Activity Statement CSV as a table (Data rows only)."""
    header, rows = None, []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for r in csv.reader(f):
            if len(r) > 2 and r[0] == name:
                if r[1] == "Header":
                    header = r[2:]
                elif r[1] == "Data" and header:
                    rows.append(dict(zip(header, r[2:])))
    return pd.DataFrame(rows)


def statements() -> pd.DataFrame:
    """Activity Statement CSVs with their period: file, start, end."""
    rows = []
    for f in tax_files("IBKR", "IBKR_*ActivityStatement_*.csv"):
        info = section(f, "Statement")
        start, end = info.loc[info["Field Name"] == "Period", "Field Value"].iloc[0].split(" - ")
        rows.append({"file": f, "start": pd.Timestamp(start), "end": pd.Timestamp(end)})
    return pd.DataFrame(rows).sort_values(["end", "start"]).reset_index(drop=True)


def holdings() -> pd.DataFrame:
    """Open positions from the newest Activity Statement: Stock Symbol, Quantity, Avg. Price ($) and
    Cost ($) (IBKR cost basis), Close Price ($), Value ($) (market value), As Of (statement end)."""
    st = statements().iloc[-1]
    p = section(st.file, "Open Positions")
    p = p[p.DataDiscriminator == "Summary"]
    return pd.DataFrame({
        "Stock Symbol": p.Symbol, "Quantity": p.Quantity.map(num), "Avg. Price ($)": p["Cost Price"].map(num),
        "Cost ($)": p["Cost Basis"].map(num), "Close Price ($)": p["Close Price"].map(num),
        "Value ($)": p.Value.map(num), "As Of": st.end,
    }).reset_index(drop=True)


def cash() -> float:
    """Ending cash (USD) in the newest Activity Statement."""
    c = section(statements().iloc[-1].file, "Cash Report")
    return num(c.loc[c["Currency Summary"] == "Ending Cash", "Total"].iloc[0])


def transfers() -> pd.DataFrame:
    """Shares transferred in or out (all statements, overlaps removed): symbol, when, direction, qty, value."""
    rows = [section(f, "Transfers") for f in statements().file]
    t = pd.concat([r for r in rows if len(r)], ignore_index=True)
    t = t[t["Asset Category"] == "Stocks"]
    return pd.DataFrame({
        "symbol": t.Symbol, "when": pd.to_datetime(t.Date), "direction": t.Direction, "qty": t.Qty.map(num),
        "value": t["Market Value"].map(num),
    }).drop_duplicates().sort_values("when").reset_index(drop=True)


def broker_realised() -> pd.DataFrame:
    """IBKR's own realised P/L per sale (its cost basis), from the Activity Statement 'Trades' sections."""
    rows = [section(f, "Trades") for f in statements().file]
    t = pd.concat([r for r in rows if len(r)], ignore_index=True)
    t = t[t.DataDiscriminator == "Order"]
    t = pd.DataFrame({
        "symbol": t.Symbol, "when": pd.to_datetime(t["Date/Time"], format="%Y-%m-%d, %H:%M:%S"), "qty": t.Quantity.map(num),
        "proceeds": t.Proceeds.map(num), "basis": t.Basis.map(num), "realised": t["Realized P/L"].map(num),
    }).drop_duplicates()
    return t[t.qty < 0].sort_values("when").reset_index(drop=True)


def trades() -> pd.DataFrame:
    """Standard trade table: symbol, when, side, qty, price, amount, fee, order_type.

    Transfers in are BUY rows (order_type TRANSFER_IN) at the ETrade lot cost per share; a transfer
    from another broker would be at its market value on the transfer date (order_type TRANSFER_IN_MV)."""
    moved = etrade.transfers()
    cost = moved.groupby("Stock Symbol")["Cost ($)"].sum() / moved.groupby("Stock Symbol")["Quantity"].sum()
    ins = transfers()
    ins = ins[ins.direction == "In"]
    known = ins.symbol.isin(cost.index)
    price = ins.symbol.map(cost).where(known, ins.value / ins.qty)
    tin = pd.DataFrame({
        "symbol": ins.symbol, "when": ins.when, "side": "BUY", "qty": ins.qty, "price": price,
        "amount": ins.qty * price, "fee": 0.0, "order_type": known.map({True: "TRANSFER_IN", False: "TRANSFER_IN_MV"}),
    })
    return pd.concat([tin, confirmations()], ignore_index=True).sort_values("when").reset_index(drop=True)


def main():
    pd.set_option("display.width", 200)
    print(trades().to_string(index=False, float_format="{:.4f}".format))
    h = holdings()
    print(f"\nOpen positions on {h['As Of'].iloc[0]:%Y-%m-%d} (cost = IBKR cost basis):")
    print(h.drop(columns="As Of").round(2).to_string(index=False))
    print(f"cost ${h['Cost ($)'].sum():,.2f}  value ${h['Value ($)'].sum():,.2f}  cash ${cash():,.2f}")
    print("\nIBKR realised P/L (its cost basis):")
    print(broker_realised().to_string(index=False, float_format="{:.4f}".format))


if __name__ == "__main__":
    main()
