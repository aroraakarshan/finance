"""HDFC Bank: savings account balance and fixed deposits (INR).

Exports (Banking/HDFC):
  Savings/HDFC_Savings_<last4>_<from>_to_<to>.csv   NetBanking statement, "Delimited" format; padded
                                                    columns (names and values carry spaces), dates dd/mm/yy,
                                                    rows in date order; 'Closing Balance' after each row;
                                                    a blank first line; narrations may hold unquoted commas
                                                    (RTGS), so rows are split by hand: first cell date,
                                                    last cell closing balance
  Savings/HDFC_Savings_<last4>_<from>_to_<to>.pdf/.xls  same statement (PDF was locked with the Customer ID)
  FD/HDFC_FD_Summary_<date>.pdf                     one row per FD: account, branch, holder, CCY, principal,
                                                    maturity amount, maturity date, rate, start date; no
                                                    current value; principal is "dynamic" (changes on sweep-in,
                                                    part liquidation or TDS recovered from principal); does
                                                    not name the compounding
  FD/HDFC_FD_InterestCert_*, HDFC_TDS_Summary_*, HDFC_TDS_Report_*, HDFC_16A_*  not read here

Quirks: the FD summary, certificates and TDS PDFs carry an owner password only (they open without
one). pypdf splits cells over lines ("10 May\\n2027"), so the FD rows are matched on the joined text.
Only the last 4 digits of any account number leave this module.

Accrued interest (fds(), to today): the summary does not say how interest compounds, so it is
taken from the maturity amount: if principal compounded quarterly over the term gives the maturity
amount (within Rs 5), interest compounds quarterly (HDFC reinvestment FD: whole quarters compound,
then simple interest for the days since the last quarter), else simple (principal x rate x days /
365). The 2026-05-10 FDs match quarterly exactly (Rs 5,30,737.10 -> Rs 5,64,693.10). TDS is not
deducted.

Run: python -m scripts.brokers.hdfc
"""
import re

import pandas as pd

from scripts.common import finance_dir, latest, pdf_text

FD_ROW = re.compile(
    r"(?m)^\d+ \d*(\d{4}) .*?INR ([\d.]+) ([\d.]+) (\d{1,2} \w+)\s+(\d{4})\s+([\d.]+) (\d{1,2} \w+)\s+(\d{4})",
    re.S,
)


def hdfc_dir():
    return finance_dir() / "Banking" / "HDFC"


def grown(principal: float, rate: float, start: pd.Timestamp, day: pd.Timestamp, quarterly: bool) -> float:
    """Principal plus interest from start to day."""
    if not quarterly:
        return principal * (1 + rate / 100 * (day - start).days / 365)
    q = 0
    while start + pd.DateOffset(months=3 * (q + 1)) <= day:
        q += 1
    rest = (day - (start + pd.DateOffset(months=3 * q))).days
    return principal * (1 + rate / 400) ** q * (1 + rate / 100 * rest / 365)


def fds(today: pd.Timestamp | None = None) -> pd.DataFrame:
    """FDs of the newest FD summary: fd (last 4), principal, rate, start, maturity, maturity_amount,
    compounding (quarterly/simple), accrued (interest to today, or to maturity if earlier), value
    (principal + accrued), as_of."""
    path = latest(hdfc_dir() / "FD", "HDFC_FD_Summary_*.pdf")
    rows = [
        {
            "fd": last4,
            "principal": float(principal),
            "rate": float(rate),
            "start": pd.to_datetime(f"{s_day} {s_year}", format="%d %b %Y"),
            "maturity": pd.to_datetime(f"{m_day} {m_year}", format="%d %b %Y"),
            "maturity_amount": float(maturity_amount),
        }
        for last4, principal, maturity_amount, m_day, m_year, rate, s_day, s_year in FD_ROW.findall(pdf_text(path))
    ]
    if not rows:
        raise SystemExit(f"no FD rows in {path.name}")
    as_of = pd.Timestamp(path.stem.rsplit("_", 1)[-1])
    today = (today or pd.Timestamp.today()).normalize()
    text = pdf_text(path).lower()
    for r in rows:
        quarterly = "quarterly" in text or abs(
            grown(r["principal"], r["rate"], r["start"], r["maturity"], True) - r["maturity_amount"]) <= 5
        r["compounding"] = "quarterly" if quarterly else "simple"
        r["accrued"] = grown(r["principal"], r["rate"], r["start"], min(today, r["maturity"]), quarterly) - r["principal"]
        r["value"] = r["principal"] + r["accrued"]
    return pd.DataFrame(rows).assign(as_of=as_of)


def savings_balance() -> tuple[float, pd.Timestamp, str]:
    """(closing balance, date of the last transaction, account last 4) from the newest savings CSV."""
    path = latest(hdfc_dir() / "Savings", "HDFC_Savings_*_to_*.csv")
    rows = []
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.split(",")]
        if re.fullmatch(r"\d\d/\d\d/\d\d", cells[0]):
            rows.append((pd.to_datetime(cells[0], format="%d/%m/%y"), float(cells[-1])))
    if not rows:
        raise SystemExit(f"no transactions in {path.name}")
    day = max(r[0] for r in rows)
    balance = [b for d, b in rows if d == day][-1]
    return balance, day, path.name.split("_")[2]


def main():
    pd.set_option("display.width", 200)
    f = fds()
    print(f"FD summary of {f.as_of.iloc[0]:%Y-%m-%d}")
    print(f.drop(columns="as_of").to_string(index=False, float_format="{:,.2f}".format,
                                            formatters={"start": "{:%Y-%m-%d}".format, "maturity": "{:%Y-%m-%d}".format}))
    print(f"{len(f)} FDs: principal Rs {f.principal.sum():,.2f}, accrued to today Rs {f.accrued.sum():,.2f}, "
          f"at maturity Rs {f.maturity_amount.sum():,.2f}")
    bal, day, last4 = savings_balance()
    print(f"Savings ****{last4}: closing balance Rs {bal:,.2f} on {day:%Y-%m-%d}")


if __name__ == "__main__":
    main()
