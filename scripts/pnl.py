"""Realised profit/loss per stock from a broker's trade history (average-cost method).

Corporate actions are not in the trade files. A sell larger than the shares held is treated
as a split (the cost is kept, the share count is raised to the sold quantity) and reported.
Ticker changes are mapped in each broker reader (RENAMES). A TRANSFER_OUT row (shares moved to
another broker) removes the shares at their average cost with no profit or loss.

Run: python -m scripts.pnl indmoney|ibkr|etrade
"""
import sys

import pandas as pd

from scripts.brokers import etrade, ibkr, indmoney

BROKERS = {"indmoney": indmoney, "ibkr": ibkr, "etrade": etrade}


def realised(trades: pd.DataFrame):
    """Return (per-sale DataFrame, open positions {symbol: (qty, cost)}, notes)."""
    pos, rows, notes = {}, [], []
    for t in trades.itertuples():
        qty, cost = pos.get(t.symbol, (0.0, 0.0))
        if t.side == "BUY":
            pos[t.symbol] = (qty + t.qty, cost + t.amount)
            continue
        if t.side == "TRANSFER_OUT":
            left = max(qty - t.qty, 0.0)
            pos[t.symbol] = (left, cost * left / qty if qty else 0.0)
            continue
        if qty > 0 and t.qty > qty * 1.01:
            notes.append(f"{t.symbol}: sold {t.qty:g} but held {qty:g} (ratio {t.qty / qty:.2f}); treated as a split")
            qty = t.qty
        elif qty == 0:
            notes.append(f"{t.symbol}: sell with no recorded buy (bought before this file starts); cost unknown")
        avg = cost / qty if qty else 0.0
        rows.append({"symbol": t.symbol, "when": t.when, "proceeds": t.amount, "cost": avg * t.qty,
                     "pnl": t.amount - avg * t.qty if qty else float("nan")})
        pos[t.symbol] = (max(qty - t.qty, 0.0), cost - avg * min(t.qty, qty))
    return pd.DataFrame(rows), {s: p for s, p in pos.items() if p[0] > 1e-6}, notes


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "indmoney"
    t = BROKERS[name].trades()
    sales, open_pos, notes = realised(t)
    by = sales.groupby("symbol").agg(cost=("cost", "sum"), proceeds=("proceeds", "sum"), pnl=("pnl", "sum"))
    by["pct"] = 100 * by.pnl / by.cost
    print(by.sort_values("pnl").round(1).to_string())
    known = by.pnl.dropna()
    print(f"\ntrades {len(t)} ({(t.side == 'BUY').sum()} buys, {(t.side == 'SELL').sum()} sells, {(t.side == 'TRANSFER_OUT').sum()} transfers out), fees ${t.fee.sum():,.2f}")
    print(f"realised ${known.sum():,.0f}  winners {(known > 0).sum()}  losers {(known < 0).sum()}  "
          f"median per stock {by.pct.median():.1f}%")
    print(f"cost of open positions ${sum(c for _, c in open_pos.values()):,.0f}")
    if hasattr(BROKERS[name], "holdings"):
        held = set(BROKERS[name].holdings()["Stock Symbol"])
        for s, (q, c) in open_pos.items():
            if s not in held:
                notes.append(f"{s}: {q:g} shares (cost ${c:,.0f}) open in trades but not in holdings; "
                             "check for a ticker change, reverse split or delisting")
    for n in dict.fromkeys(notes):
        print("NOTE", n)


if __name__ == "__main__":
    main()
