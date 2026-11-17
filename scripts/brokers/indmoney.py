"""INDmoney US stocks (broker Alpaca).

Exports (Investments/Stocks/INDmoney):
  INDmoney_US_Holdings_<date>.xls                   'Total Value ($)' is quantity x average price (cost), not market value
  INDmoney_US_Trades_SinceInception_to_<date>.xls   every order since the account opened

Run: python -m scripts.brokers.indmoney
"""
import pandas as pd

from scripts.common import latest, read_table, stocks_dir

# Ticker changes: the trade file keeps the old symbol on old orders. Verified by quantity and average price.
RENAMES = {"SAVA": "FLNA"}

# Splits (new shares per old share, effective date). Orders before the date are restated in
# post-split shares so quantities net. Verified by the sell quantity in the trade file and yfinance splits.
SPLITS = {
    "CERO": [("2025-01-08", 1 / 100)],
    "CRWD": [("2026-07-02", 4)],
    "HSDT": [("2025-05-02", 1 / 15), ("2025-07-01", 1 / 50)],
    "KLAC": [("2026-06-12", 10)],
    "SCLX": [("2025-04-15", 1 / 35)],
}


def holdings() -> pd.DataFrame:
    df = read_table(latest(stocks_dir("INDmoney"), "INDmoney_US_Holdings_*.xls"), "Stock Symbol")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df = df[df["Quantity"] > 0]
    df["Avg. Price ($)"] = pd.to_numeric(df["Avg. Price ($)"])
    df["Cost ($)"] = df["Quantity"] * df["Avg. Price ($)"]
    return df[["Stock Symbol", "Holding Since", "Quantity", "Avg. Price ($)", "Cost ($)"]].reset_index(drop=True)


def trades() -> pd.DataFrame:
    """Standard trade table: symbol, when, side, qty, price, amount, fee."""
    df = read_table(latest(stocks_dir("INDmoney"), "INDmoney_US_Trades_*.xls"), "Stock Symbol")
    df = df[df["Transaction Type"].isin(["BUY", "SELL"])]
    t = pd.DataFrame({
        "symbol": df["Stock Symbol"].replace(RENAMES),
        "when": pd.to_datetime(df["Order Execution Time"], format="%d %b %Y, %I:%M %p"),
        "side": df["Transaction Type"],
        "qty": pd.to_numeric(df["Quantity"]),
        "price": pd.to_numeric(df["Price ($)"]),
        "amount": pd.to_numeric(df["Order Amount ($)"]),
        "fee": pd.to_numeric(df["Brokerage ($)"]),
        "order_type": df["Order Type"],
    })
    for symbol, splits in SPLITS.items():
        for day, ratio in splits:
            before = (t.symbol == symbol) & (t.when < pd.Timestamp(day))
            t.loc[before, "qty"] *= ratio
            t.loc[before, "price"] /= ratio
    return t.sort_values("when").reset_index(drop=True)


def main():
    pd.set_option("display.width", 200)
    h = holdings()
    print(h.round(2).to_string(index=False))
    print(f"cost of open positions ${h['Cost ($)'].sum():,.0f}")


if __name__ == "__main__":
    main()
