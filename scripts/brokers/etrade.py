"""E*TRADE from Morgan Stanley stock plan accounts (RSU and ESPP from earlier employers).

One login, one stock plan account per employer, named by the last 4 digits in the file names:
QCOM (Qualcomm RSU and ESPP) and NXPI (NXP ESPP). Both accounts were moved to IBKR in Dec 2025
and are empty since then.

Exports:
  Investments/Stocks/ETrade/ETrade_<last4>_BenefitHistory_Expanded_<date>.xlsx
      every grant, vest and ESPP purchase; used only to check that no release or purchase
      confirmation is missing. 'Released Qty' is whole shares; the confirmations have the fractions.
  Investments/Stocks/ETrade/ETrade_<last4>_GainsLosses_TY<year>.xlsx
      only from 2023 and can be incomplete (not read).
  Tax/FY*/ETrade/ETrade_<last4>_<date>_Confirmation_RSRelease[_n].pdf
      one per RSU release: market value per share (cost in India), shares sold to cover tax,
      shares issued. Several releases on one day get _2, _3. Dividend shares are paid as cash in lieu.
  Tax/FY*/ETrade/ETrade_<last4>_<date>_Confirmation_ESPP.pdf
      one per ESPP purchase: purchase value per share (FMV, cost in India) and price paid.
  Tax/FY*/ETrade/ETrade_<last4>_<date>_TradeConfirmation_<SYM>[_n].pdf
      sales. Up to Sep 2023 (E*TRADE Securities) one document lists every trade of the day and
      is downloaded once per release, so identical copies are dropped. From Sep 2023 (Morgan
      Stanley) each document is one trade and two can be identical, so all are kept. Sell-to-cover
      at release is sometimes labelled "Sold Short".
  Tax/FY*/ETrade/ETrade_<last4>_<date>[_AccountStatement|_SingleAccountStatement].pdf
      monthly or quarterly (only periods with activity; the period inside the PDF counts, not the
      name). Read for dividend reinvestments (from Sep 2024), transfers out and the share count
      at the period end. The new platform rounds shares to 3 decimals (NXPI 13.5742 -> 13.575).

Cost basis is the market value at release or purchase (Indian tax). A sell-to-cover sale takes the
shares of the releases it paid for (each up to its own shares sold for tax), a fractional liquidation
takes DRIP shares; other sales and transfers use lots first in, first out.

Run: python -m scripts.brokers.etrade
"""
import re
from collections import deque
from pathlib import Path

import pandas as pd

from scripts.common import latest, num, pdf_text, stocks_dir, tax_files

NAMES = {"QUALCOMM INC": "QCOM", "NXP SEMICONDUCTORS NV": "NXPI"}
STATEMENT = re.compile(r"ETrade_\d{4}_\d{4}-\d\d-\d\d(_AccountStatement|_SingleAccountStatement)?(_\d)?\.pdf$")


def account(path: Path) -> str:
    return path.name.split("_")[1]


def find(pattern: str, t: str, default=None):
    m = re.search(pattern, t)
    return m.group(1) if m else default


def acquisitions() -> pd.DataFrame:
    """RSU releases and ESPP purchases from the confirmation PDFs, one row per lot."""
    rows = {}
    for f in tax_files("ETrade", "ETrade_*_Confirmation_RSRelease*.pdf"):
        t = pdf_text(f)
        sold = num(find(r"Shares Sold \(([\d,.]+)\)", t, "0"))
        issued = num(find(r"Shares Issued ([\d,.]+)", t))
        when = pd.to_datetime(find(r"Release Date (\d\d-\d\d-\d{4})", t), format="%m-%d-%Y")
        award = find(r"Award Number (\S+)", t)
        rows[(account(f), award, when)] = {
            "account": account(f), "symbol": find(r"\((\w+)\)\s*\nAward Number", t), "when": when,
            "type": "RSU", "award": award, "qty": sold + issued,
            "fmv": num(find(r"Market Value Per Share \$([\d,.]+)", t)), "paid": 0.0,
            "sold_for_tax": sold, "net": issued,
            "sale_price": num(find(r"Sale Price Per Share \$([\d,.]+)", t, "0")),
            "sale_amount": num(find(r"Total Sale Price \$([\d,.]+)", t, "0")),
            "sale_fee": num(find(r"Fee \(\$([\d,.]+)\)", t, "0")), "file": f.name}
    for f in tax_files("ETrade", "ETrade_*_Confirmation_ESPP*.pdf"):
        t = pdf_text(f)
        when = pd.to_datetime(find(r"Purchase Date (\d\d-\d\d-\d{4})", t), format="%m-%d-%Y")
        qty = num(find(r"Shares Purchased ([\d,.]+)", t))
        rows[(account(f), "ESPP", when)] = {
            "account": account(f), "symbol": find(r"\((\w+)\)\s*\nPlan", t), "when": when,
            "type": "ESPP", "award": "ESPP", "qty": qty,
            "fmv": num(find(r"Purchase Value per Share \$([\d,.]+)", t)),
            "paid": num(find(r"Purchase Price per Share\s+\([^)]*\) \$([\d,.]+)", t)),
            "sold_for_tax": 0.0, "net": qty, "file": f.name}
    return pd.DataFrame(rows.values()).sort_values(["account", "when"]).reset_index(drop=True)


OLD_TRADE = re.compile(r"^(\d\d/\d\d/\d\d) \d\d/\d\d/\d\d \d+ \d+ (\S+) (SELL|BUY) ([\d,.]+) \$([\d,.]+) .*?PRINCIPAL \$([\d,.]+)", re.M)


def sales() -> pd.DataFrame:
    """Every sale from the trade confirmations, with the account.

    A sell-to-cover with no trade confirmation (Aug 2019, before the files start) is taken from the
    release confirmation: release date, sale price, total sale price and fee."""
    rows, seen = [], set()
    for f in tax_files("ETrade", "ETrade_*_TradeConfirmation_*.pdf"):
        t = pdf_text(f)
        if OLD_TRADE.search(t):
            if t in seen:
                continue
            seen.add(t)
            starts = [m.start() for m in OLD_TRADE.finditer(t)] + [len(t)]
            for a, b in zip(starts, starts[1:]):
                block = t[a:b]
                m = OLD_TRADE.match(block)
                rows.append({
                    "account": account(f), "symbol": m[2], "when": pd.to_datetime(m[1], format="%m/%d/%y"),
                    "side": m[3], "qty": num(m[4]), "price": num(m[5]), "amount": num(m[6]),
                    "fee": num(find(r"COMMISSION \$([\d,.]+)", block, "0")) + num(find(r"FEE \$([\d,.]+)", block, "0")),
                    "fractional": False, "file": f.name})
        else:
            m = re.search(r"(\d\d/\d\d/\d{4}) \d\d/\d\d/\d{4} ([\d,.]+) ([\d,.]+)", t)
            kind = find(r"Transaction Type: ([^\n]+)", t).strip()
            rows.append({
                "account": account(f), "symbol": find(r"Symbol / CUSIP / ISIN: (\S+)", t),
                "when": pd.to_datetime(m[1], format="%m/%d/%Y"), "side": "BUY" if kind == "Bought" else "SELL",
                "qty": num(m[2]), "price": num(m[3]), "amount": num(find(r"Principal \$([\d,.]+)", t)),
                "fee": num(find(r"Commission \$([\d,.]+)", t, "0")) + num(find(r"Transaction Fee \$([\d,.]+)", t, "0")),
                "fractional": "Fractional liquidation" in t, "file": f.name})
    df = pd.DataFrame(rows)
    acq = acquisitions()
    extra = []
    for (acct, when), r in acq[(acq.type == "RSU") & (acq.sold_for_tax > 0)].groupby(["account", "when"]):
        if covers(df, acct, when).empty:
            extra += [{"account": acct, "symbol": x.symbol, "when": when, "side": "SELL", "qty": x.sold_for_tax,
                       "price": x.sale_price, "amount": x.sale_amount, "fee": x.sale_fee, "fractional": False,
                       "file": x.file} for x in r.itertuples()]
    return pd.concat([df, pd.DataFrame(extra)], ignore_index=True).sort_values(["account", "when"]).reset_index(drop=True)


def covers(sold: pd.DataFrame, acct: str, when: pd.Timestamp) -> pd.DataFrame:
    """Sales that pay the tax of the releases on `when`: same account, up to 5 days later, not fractional."""
    return sold[(sold.account == acct) & (sold.when >= when) & (sold.when - when <= pd.Timedelta(days=5)) & ~sold.fractional]


def period(t: str):
    m = re.search(r"Statement Period :\s+(\w+ \d+, \d{4}) - (\w+ \d+, \d{4})", t)
    if m:
        return pd.Timestamp(m[1]), pd.Timestamp(m[2])
    m = re.search(r"For the Period (\w+) (\d+),?(?: (\d{4}))?-\s*(?:([A-Za-z]+) )?(\d+), (\d{4})", t)
    end = pd.Timestamp(f"{m[4] or m[1]} {m[5]}, {m[6]}")
    start = pd.Timestamp(f"{m[1]} {m[2]}, {m[3] or m[6]}")
    return start, end


def position(t: str):
    """Shares held at the period end, or None if the statement does not say."""
    if "There Are No Holdings For This Account" in t:
        return 0.0
    m = re.search(r"(?:QCOM|NXPI) StkPln\s+([\d,.]+) ([\d,.]+) ([\d,.]+)", t)
    if m:
        # last old-platform statement (Sep 2023): quantity blank, price then value 0.00; the shares moved to the new account
        return None if num(m[3]) == 0 else num(m[1])
    m = re.search(r"\((?:QCOM|NXPI)\) (?:Purchases )?([\d,.]+)(?:[^\n]*\nReinvestments[^\n]*\nTotal ([\d,.]+))?", t)
    if m:
        return num(m[2] or m[1])
    return None


def dated(md: str, start: pd.Timestamp, end: pd.Timestamp) -> pd.Timestamp:
    month, day = map(int, md.split("/"))
    return pd.Timestamp(start.year if month > end.month else end.year, month, day)


def statements():
    """(statements, dividend reinvestments, transfers out) from the account statements."""
    stmts = {}
    for f in tax_files("ETrade", "ETrade_*.pdf"):
        if STATEMENT.search(f.name):
            t = pdf_text(f).split("Recap of Cash Management Activity")[0]  # the year-end recap repeats the transfers
            start, end = period(t)
            stmts[(account(f), start, end)] = (f, t)  # same period twice (renamed copy, platform move): keep the later file
    rows, drip, out = [], [], []
    for (acct, start, end), (f, t) in sorted(stmts.items()):
        rows.append({"account": acct, "start": start, "end": end, "shares": position(t), "file": f.name})
        for m in re.finditer(r"(\d{1,2}/\d{1,2}) Dividend Reinvestment (.+?) ACTED AS AGENT\s*\nDIVIDEND REINVESTMENT\s*\n([\d,.]+) ([\d,.]+) \(([\d,.]+)\)", t):
            drip.append({"account": acct, "symbol": NAMES[m[2].strip()], "when": dated(m[1], start, end),
                         "qty": num(m[3]), "price": num(m[4]), "amount": num(m[5])})
        for m in re.finditer(r"(\d{1,2}/\d{1,2}) Transfer out of Account (.+?) TO\s+(.+?)/ ([\d,.]+) \$?\(([\d,.]+)\)", t):
            out.append({"account": acct, "symbol": NAMES[m[2].strip()], "when": dated(m[1], start, end),
                        "qty": num(m[4]), "value": num(m[5]), "to": m[3].strip()})
    return pd.DataFrame(rows), pd.DataFrame(drip), pd.DataFrame(out)


def events() -> pd.DataFrame:
    """Every share movement per account: acquisitions, reinvestments, sales and transfers out."""
    acq, sold = acquisitions(), sales()
    _, drip, out = statements()
    releases = acq[acq.type == "RSU"]

    def order_type(s):
        if s.fractional:
            return "fractional"
        near = releases[(releases.account == s.account) & (releases.when <= s.when) & (s.when - releases.when <= pd.Timedelta(days=5))]
        return "sell-to-cover" if len(near) else "sell"


    parts = [
        pd.DataFrame({"account": acq.account, "symbol": acq.symbol, "when": acq.when, "side": "BUY", "qty": acq.qty,
                      "price": acq.fmv, "amount": acq.qty * acq.fmv, "fee": 0.0, "order_type": acq.type,
                      "cover": acq.sold_for_tax}),
        pd.DataFrame({"account": sold.account, "symbol": sold.symbol, "when": sold.when, "side": sold.side, "qty": sold.qty,
                      "price": sold.price, "amount": sold.amount, "fee": sold.fee,
                      "order_type": sold.apply(order_type, axis=1)}),
    ]
    if len(drip):
        parts.append(drip.assign(side="BUY", fee=0.0, order_type="DRIP"))
    if len(out):
        parts.append(out.assign(side="TRANSFER_OUT", price=out.value / out.qty, amount=out.value, fee=0.0,
                                order_type="to " + out.to)[["account", "symbol", "when", "side", "qty", "price", "amount", "fee", "order_type"]])
    df = pd.concat(parts, ignore_index=True)
    df["cover"] = df.cover.fillna(0.0)
    df["rank"] = (df.side != "BUY").astype(int)
    return df.sort_values(["when", "rank"]).drop(columns="rank").reset_index(drop=True)


def trades() -> pd.DataFrame:
    """Standard trade table: symbol, when, side, qty, price, amount, fee, order_type.

    RSU releases and ESPP purchases are BUY at market value (gross RSU shares; the sell-to-cover is a SELL).
    Transfers out are TRANSFER_OUT rows (amount = market value on the transfer date); pnl.py removes
    the shares at their cost with no profit or loss. The lot costs that move are in transfers()."""
    return events().drop(columns=["account", "cover"])


def lots():
    """Lots over events(): (open lots, lots that left by transfer, notes).

    A sell-to-cover takes first from the releases it covers (same account, released up to 5 days
    before, each up to its own shares sold for tax); a fractional liquidation takes first from
    dividend reinvestment lots (where the fractions come from); the rest is first in, first out."""
    books, moved, notes = {}, [], []
    for e in events().itertuples():
        book = books.setdefault((e.account, e.symbol), deque())
        if e.side == "BUY":
            book.append({"Account": e.account, "Stock Symbol": e.symbol, "Type": e.order_type, "Holding Since": e.when,
                         "Quantity": e.qty, "Avg. Price ($)": e.price, "cover": e.cover})
            continue
        left = e.qty
        if e.order_type in ("sell-to-cover", "fractional"):
            for lot in book:
                if e.order_type == "fractional":
                    cap = lot["Quantity"] if lot["Type"] == "DRIP" else 0.0
                elif lot["Type"] == "RSU" and pd.Timedelta(0) <= e.when - lot["Holding Since"] <= pd.Timedelta(days=5):
                    cap = lot["cover"]
                else:
                    cap = 0.0
                take = min(left, lot["Quantity"], cap)
                if take > 1e-9:
                    lot["Quantity"] -= take
                    lot["cover"] -= take if e.order_type == "sell-to-cover" else 0.0
                    left -= take
            book = books[(e.account, e.symbol)] = deque(lot for lot in book if lot["Quantity"] > 1e-9)
        while left > 1e-9 and book:
            lot = book[0]
            take = min(left, lot["Quantity"])
            if e.side == "TRANSFER_OUT":
                moved.append({**lot, "Quantity": take, "Transferred": e.when, "To": e.order_type[3:]})
            lot["Quantity"] -= take
            left -= take
            if lot["Quantity"] <= 1e-9:
                book.popleft()
        if left > 1e-3:
            notes.append(f"{e.account} {e.symbol}: {e.side.lower()} of {e.qty:g} on {e.when:%Y-%m-%d} "
                         f"has {left:g} shares with no matching acquisition")
        elif left > 1e-6:
            notes.append(f"{e.account} {e.symbol}: {e.side.lower()} of {e.qty:g} on {e.when:%Y-%m-%d} "
                         f"is {left:.4f} shares more than held (share rounding)")
    held = [lot for book in books.values() for lot in book if lot["Quantity"] > 1e-3]
    cols = ["Account", "Stock Symbol", "Type", "Holding Since", "Quantity", "Avg. Price ($)"]
    h = pd.DataFrame(held, columns=cols)
    h["Cost ($)"] = h["Quantity"] * h["Avg. Price ($)"]
    t = pd.DataFrame(moved, columns=cols + ["Transferred", "To"])
    t["Cost ($)"] = t["Quantity"] * t["Avg. Price ($)"]
    return h, t, notes


def holdings() -> pd.DataFrame:
    """Open lots: Account, Stock Symbol, Type (RSU/ESPP/DRIP), Holding Since, Quantity, Avg. Price ($), Cost ($)."""
    return lots()[0]


def transfers() -> pd.DataFrame:
    """Lots that left by transfer to another broker, with their cost (cost basis there)."""
    return lots()[1]


def checks() -> list[str]:
    """Discrepancies: statement gaps, share counts that differ from the statements, missing confirmations."""
    notes = []
    stmts, _, _ = statements()
    ev = events()
    acq = acquisitions()
    for acct, s in stmts.groupby("account"):
        first = acq[acq.account == acct].when.min()
        if pd.notna(first) and s.start.min() > first:
            notes.append(f"{acct}: no statement before {s.start.min():%Y-%m-%d}; first acquisition {first:%Y-%m-%d}")
        for prev, nxt in zip(s.itertuples(), list(s.itertuples())[1:]):
            if nxt.start > prev.end + pd.Timedelta(days=1):
                notes.append(f"{acct}: no statement for {prev.end + pd.Timedelta(days=1):%Y-%m-%d} to {nxt.start - pd.Timedelta(days=1):%Y-%m-%d}")
        for st in s.itertuples():
            if st.shares is None or pd.isna(st.shares):
                continue
            e = ev[(ev.account == acct) & (ev.when <= st.end)]
            held = e[e.side == "BUY"].qty.sum() - e[e.side != "BUY"].qty.sum()
            if abs(held - st.shares) > 1e-3:
                notes.append(f"{acct}: statement {st.end:%Y-%m-%d} shows {st.shares:g} shares, files give {held:g}")
    sold = sales()
    for x in sold[sold.file.str.contains("RSRelease")].itertuples():
        notes.append(f"{x.account}: sale of {x.qty:g} {x.symbol} on {x.when:%Y-%m-%d} has no trade confirmation; taken from {x.file}")
    for (acct, when), r in acq[acq.type == "RSU"].groupby(["account", "when"]):
        cover = covers(sold, acct, when).qty.sum()
        if abs(cover - r.sold_for_tax.sum()) > 1e-3:
            notes.append(f"{acct}: releases on {when:%Y-%m-%d} sold {r.sold_for_tax.sum():g} for tax, trade confirmations show {cover:g}")
    for acct in sorted(set(acq.account)):
        try:
            f = latest(stocks_dir("ETrade"), f"ETrade_{acct}_BenefitHistory_Expanded_*.xlsx")
        except SystemExit:
            notes.append(f"{acct}: no Benefit History export to check the confirmations against")
            continue
        rs = pd.read_excel(f, sheet_name="Restricted Stock")
        rs["Grant Number"] = rs["Grant Number"].ffill()
        for v in rs[(rs["Record Type"] == "Vest Schedule") & (rs["Released Qty"] > 0)].to_dict("records"):
            when = pd.to_datetime(v["Vest Date"], format="%m/%d/%Y")
            if acq[(acq.account == acct) & (acq.award == v["Grant Number"]) & (acq.when == when)].empty:
                notes.append(f"{acct}: release {when:%Y-%m-%d} of {v['Grant Number']} ({v['Released Qty']:g} shares) has no release confirmation")
        es = pd.read_excel(f, sheet_name="ESPP")
        for p in es[es["Record Type"] == "Purchase"].to_dict("records"):
            when = pd.to_datetime(p["Purchase Date"], format="%d-%b-%Y")
            hit = acq[(acq.account == acct) & (acq.type == "ESPP") & (acq.when == when)]
            if hit.empty:
                notes.append(f"{acct}: ESPP purchase {when:%Y-%m-%d} ({p['Purchased Qty.']:g} shares) has no purchase confirmation")
            elif abs(hit.qty.iloc[0] - p["Purchased Qty."]) > 1e-6:
                notes.append(f"{acct}: ESPP purchase {when:%Y-%m-%d} is {hit.qty.iloc[0]:g} shares in the confirmation, "
                             f"{p['Purchased Qty.']:g} in Benefit History")
    return notes


def main():
    pd.set_option("display.width", 200)
    acq = acquisitions()
    print("Acquisitions (cost = market value at release/purchase):")
    print(acq.groupby(["account", "symbol", "type"]).agg(lots=("qty", "size"), first=("when", "min"), last=("when", "max"),
                                                         gross=("qty", "sum"), sold_for_tax=("sold_for_tax", "sum"),
                                                         net=("net", "sum")).round({"gross": 4, "sold_for_tax": 4, "net": 4}).to_string())
    h, moved, notes = lots()
    print("\nOpen positions:")
    print(h.round(2).to_string(index=False) if len(h) else "  none")
    if len(moved):
        print("\nTransferred out (cost basis at the new broker):")
        by = moved.groupby(["Account", "Stock Symbol", "To", "Type"]).agg(
            shares=("Quantity", "sum"), cost=("Cost ($)", "sum"), first=("Holding Since", "min"),
            last=("Holding Since", "max"), on=("Transferred", "max"))
        print(by.round({"shares": 3, "cost": 2}).to_string())
        tot = moved.groupby(["Account", "Stock Symbol"]).agg(shares=("Quantity", "sum"), cost=("Cost ($)", "sum"))
        tot["avg"] = tot.cost / tot.shares
        print(tot.round(2).to_string())
    t = trades()
    print(f"\ntrades {len(t)}: " + ", ".join(f"{k} {v}" for k, v in t.order_type.value_counts().items())
          + f"; fees ${t.fee.sum():,.2f}")
    for n in dict.fromkeys(notes + checks()):
        print("NOTE", n)


if __name__ == "__main__":
    main()
