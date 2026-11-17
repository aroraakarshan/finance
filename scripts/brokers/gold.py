"""Physical gold: purchase invoices and today's value at the Indian gold rate.

Invoices (Investments/Gold/<yyyy-mm-dd>_<Seller>_Invoice.pdf), three layouts, all parsed:
  Varnika    Bathinda jeweller (Tanishq franchise layout): per item gross price, scheme discount, net
             metal weight, making charges, purity (karat), SGST/CGST, product value; diamond/stone
             weight but no stone price, so stones = gross price - gold value - making
  TanishqDubai  Titan Global Retail, Dubai, in AED: per item purity, net weight, making, net amount,
             discount, VAT 5%; the invoice is in
             another person's name
  BhimaGold  Bhima Gold online orders: purity, rate per gram, net weight, jewel amount (gold), VA
             (making), SGST/CGST on the full value, then a promotional offer (equal to the VA) off
             the payable amount
Gold value on each invoice = net gold weight x the seller's rate for that purity on that day; all
other cost (stones, hallmarking) goes to 'other'. AED is converted at AED_INR below.
Quirk: Google Drive sometimes refuses a file never opened on this Mac ("Operation not permitted");
reading it once from the shell (`head -c 4 <file>`) or marking the folder available offline fixes it.

Rate today: IBJA (India Bullion and Jewellers Association, ibjarates.com) PM rate per 10 g for
999 (24K), 916 (22K) and 750 (18K), without GST or making, the reference rate Indian banks and
jewellers quote. If IBJA is not reachable: international gold (yfinance GC=F, USD per troy oz) x
USD/INR (FBIL reference rate of the same day, scripts.value.usdinr; Yahoo INR=X daily bars are a day
behind) / 31.1035 g x premium, the premium being IBJA 999 / that international price on
the last day both were fetched (cached), else 1.06 (Indian customs duty 5% + AIDC 1%). Offline or
if both fail: the cached rate, with its date. 22K and 18K by the IBJA ratio 916/999 and 750/999.
Value = net gold weight x today's rate (stones, making and GST are not resold).

Run: python -m scripts.brokers.gold [--offline]
"""
import argparse
import html
import logging
import re

import pandas as pd
import requests

from scripts.common import cache_prices, cached_prices, every, finance_dir, num, pdf_text

# AED -> INR for the Dubai invoice: yfinance AEDINR=X close of 2025-12-24 (invoice date).
AED_INR = {"2025-12-24": 24.3507}
IBJA_URL = "https://www.ibjarates.com/"
TROY_OZ_G = 31.1035
DUTY = 1.06
FINENESS = {24: 999, 22: 916, 18: 750}

VARNIKA_ITEM = re.compile(
    r"\n([A-Za-z][^\n]*)\n([\d.]+)\n([\d.]+) ([\d.]+)\s+([\d.]+)\s+(\d+\.\d\d)(\d+\.\d{3})G\*- (\d+)Karat \d+N\n\d+\n"
    r"([\d,.]+)\n\d+\s+([\d.]+)\n\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)")
TANISHQ_ITEM = re.compile(
    r"\n([A-Z][a-z][^\n]*)\n[^\n]*\nG\*-(\d+) Karat (\d+) ([\d.]+) ([\d.]+) ([\d,]+\.\d\d) ([\d,]+\.\d\d) "
    r"([\d,]+\.\d\d) ([\d,]+\.\d\d) ([\d.]+)% ([\d,]+\.\d\d) ([\d,]+\.\d\d)")


def gold_dir():
    return finance_dir() / "Investments" / "Gold"


def kind(desc: str) -> str:
    d = desc.upper()
    return "coin" if "COIN" in d else "bar" if re.search(r"\bBAR\b", d) else "jewellery"


def purity(karat: int) -> str:
    return f"{karat}K" if karat in (24, 22) else f"other ({karat}K)"


def item(when, seller, path, desc, karat, grams, rate, making, other, discount, tax, paid, currency="INR", fx=1.0):
    return {"date": when, "seller": seller, "invoice": path.name, "item": kind(desc), "description": desc.title() if desc.isupper() else desc,
            "karat": karat, "purity": purity(karat), "grams": grams, "rate_on_invoice": rate,
            "gold_value": grams * rate * fx, "making": making * fx, "other": other * fx, "discount": discount * fx,
            "tax": tax * fx, "paid": paid * fx, "currency": currency, "paid_native": paid, "fx": fx}


def varnika(path, t):
    when = pd.to_datetime(re.search(r"Date: (\d\d/\d\d/\d{4})", t)[1], format="%d/%m/%Y")
    r24, r22, r18 = map(float, re.search(r"Gold \(Rs\.\):([\d.]+) Rs/([\d.]+) Rs/([\d.]+) Rs/", t).groups())
    rate = {24: r24, 22: r22, 18: r18}
    out = []
    for desc, _stone_g, _ct, net, gross, value, _gross_g, karat, making, hm, disc, sgst, cgst in VARNIKA_ITEM.findall(t):
        karat, net, gross, making, disc = int(karat), float(net), float(gross), num(making), float(disc)
        gold = net * rate[karat]
        out.append(item(when, "Varnika", path, desc, karat, net, rate[karat], making, gross - gold - making + float(hm),
                        disc, float(sgst) + float(cgst), float(value)))
    return out, num(re.search(r"Total Amount Paid\s+([\d,.]+)", t)[1])


def tanishq_dubai(path, t):
    when = pd.to_datetime(re.search(r"Date :(\d\d-\w{3}-\d{4})", t)[1], format="%d-%b-%Y")
    fx = AED_INR[f"{when:%Y-%m-%d}"]
    r24, r22, r18 = map(float, re.search(r"Gold \(AED\) : ([\d.]+)/([\d.]+)/([\d.]+)", t).groups())
    rate = {24: r24, 22: r22, 18: r18}
    out = []
    for desc, karat, _qty, _gross_g, net, making, amount, disc, _excl, _pct, vat, total in TANISHQ_ITEM.findall(t):
        karat, net = int(karat), float(net)
        gold = net * rate[karat]
        out.append(item(when, "Tanishq Dubai", path, desc, karat, net, rate[karat], num(making),
                        num(amount) - gold - num(making), num(disc), num(vat), num(total), "AED", fx))
    return out, num(re.search(r"([\d,]+\.\d\d)\nValue in words", t)[1]) * fx


def bhima(path, t):
    when = pd.to_datetime(re.search(r"Order Date:(\d\d/\d\d/\d{4})", t)[1], format="%d/%m/%Y")
    m = re.search(r"GrossAmount\n1\n(.*?)\n\d{6}\n(\d+)K\n", t, re.S)
    rate, _qty, _gross_g, _stone_g, net, jewel, va, stone, _gross = map(float, re.findall(r"[\d.]+", t[m.end():])[:9])
    tax = sum(float(x) for x in re.findall(r"\n[SC]GST\n([\d.]+)", t))
    promo = float(re.search(r"Promotional Offer\n([\d.]+)", t)[1])
    paid = float(re.search(r"Net Amount\n([\d.]+)", t)[1])
    return [item(when, "Bhima Gold", path, " ".join(m[1].split()), int(m[2]), net, rate, va,
                 stone + jewel - net * rate, promo, tax, paid)], paid


READERS = {"Varnika": varnika, "TanishqDubai": tanishq_dubai, "BhimaGold": bhima}


def items() -> tuple[pd.DataFrame, list[str]]:
    """One row per invoice line (money in INR), and notes for invoices that did not parse or add up."""
    rows, notes = [], []
    for path in every(gold_dir(), "*_Invoice.pdf"):
        seller = path.stem.split("_")[1]
        if seller not in READERS:
            notes.append(f"gold invoice {path.name}: no reader for seller {seller}")
            continue
        got, paid = READERS[seller](path, pdf_text(path))
        if not got:
            notes.append(f"gold invoice {path.name}: no item lines found")
        elif abs(sum(r["paid"] for r in got) - paid) > 2 * got[0]["fx"]:
            notes.append(f"gold invoice {path.name}: items add up to Rs {sum(r['paid'] for r in got):,.0f}, "
                         f"invoice total Rs {paid:,.0f}")
        rows += got
    return pd.DataFrame(rows), notes


def invoices(it: pd.DataFrame) -> pd.DataFrame:
    """Per invoice: date, seller, items, purities, grams, gold value, making, other, discount, tax, paid (INR)."""
    return it.groupby(["date", "seller", "invoice", "currency", "fx"], as_index=False).agg(
        item=("item", lambda s: ", ".join(sorted(set(s)))), purity=("purity", lambda s: ", ".join(sorted(set(s)))),
        grams=("grams", "sum"), gold_value=("gold_value", "sum"), making=("making", "sum"), other=("other", "sum"),
        discount=("discount", "sum"), tax=("tax", "sum"), paid=("paid", "sum"), paid_native=("paid_native", "sum"))


def ibja() -> tuple[dict[int, float], pd.Timestamp]:
    """Newest IBJA PM rates per gram {24, 22, 18} and their date."""
    resp = requests.get(IBJA_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
    resp.raise_for_status()
    page = html.unescape(resp.text)
    m = re.search(r'data-label="PM"><strong>(\d\d/\d\d/\d{4})</strong></td>\s*'
                  r'<td[^>]*"Gold 999">(\d+)</td>\s*<td[^>]*"Gold 995">\d+</td>\s*'
                  r'<td[^>]*"Gold 916">(\d+)</td>\s*<td[^>]*"Gold 750">(\d+)</td>', page)
    if not m:
        raise ValueError("IBJA page layout changed: PM rate row not found")
    return {24: int(m[2]) / 10, 22: int(m[3]) / 10, 18: int(m[4]) / 10}, pd.to_datetime(m[1], format="%d/%m/%Y")


def international(day: pd.Timestamp | None = None) -> tuple[float, pd.Timestamp]:
    """International gold in INR per gram (GC=F x FBIL USD/INR of the same day / 31.1035) on `day` or the last
    close before today. Not Yahoo INR=X: its daily bar dated D holds the previous trading day's close."""
    import yfinance as yf

    from scripts.value import usdinr  # here: scripts.value imports this module

    logging.getLogger("yfinance").setLevel(logging.CRITICAL)
    d = yf.download("GC=F", period="15d", auto_adjust=False, progress=False)["Close"].squeeze("columns").dropna()
    d = d[(d.index < pd.Timestamp.today().normalize()) & (d.index.dayofweek < 5)]  # GC=F has Sunday bars
    if day is not None:
        d = d[d.index == day]
    for t in reversed(d.index):  # newest close with an FBIL rate of the same day (none on Indian holidays)
        fx = usdinr(t)
        if fx is not None and fx[1] == t:
            return float(d[t] * fx[0] / TROY_OZ_G), t
    raise ValueError("no GC=F close with an FBIL USD/INR of the same day")


def rates(offline: bool = False) -> tuple[dict[int, float], pd.Timestamp, str]:
    """Indian gold rate per gram for 24K, 22K, 18K: (rates, date, source)."""
    cache = cached_prices()
    if not offline:
        try:
            r, day = ibja()
            fresh = {f"IBJA-{FINENESS[k]}": (v, day) for k, v in r.items()}
            try:
                intl, _ = international(day)
                fresh["GOLD-PREMIUM"] = (r[24] / intl, day)
            except Exception:
                pass
            cache_prices(fresh)
            return r, day, f"IBJA PM rate of {day:%Y-%m-%d} (ibjarates.com)"
        except Exception as e:
            ibja_error = e
        try:
            intl, day = international()
            prem = cache.get("GOLD-PREMIUM", {}).get("price", DUTY)
            r24 = intl * prem
            r = {k: r24 * FINENESS[k] / 999 for k in FINENESS}
            return r, day, (f"IBJA not reachable ({ibja_error}); international gold x USD/INR of {day:%Y-%m-%d} "
                            f"x {prem:.3f} (IBJA premium{' of ' + cache['GOLD-PREMIUM']['date'] if 'GOLD-PREMIUM' in cache else ': none cached, customs duty 6%'})")
        except Exception:
            pass
    if "IBJA-999" not in cache:
        raise SystemExit("no gold rate: IBJA and yfinance not reachable and nothing cached")
    day = pd.Timestamp(cache["IBJA-999"]["date"])
    return ({k: cache[f"IBJA-{FINENESS[k]}"]["price"] for k in FINENESS}, day,
            f"cached IBJA PM rate of {day:%Y-%m-%d} ({'offline' if offline else 'network failure'})")


def valued(it: pd.DataFrame, r: dict[int, float]) -> pd.DataFrame:
    """Items with rate_now (per gram) and value_now (INR)."""
    it = it.copy()
    it["rate_now"] = it.karat.map(lambda k: r.get(k, r[24] * k / 24))
    it["value_now"] = it.grams * it.rate_now
    return it


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--offline", action="store_true", help="use the cached gold rate")
    args = ap.parse_args()
    pd.set_option("display.width", 220)
    it, notes = items()
    r, day, source = rates(args.offline)
    it = valued(it, r)
    print(f"Gold rate per gram: 24K Rs {r[24]:,.1f}, 22K Rs {r[22]:,.1f}, 18K Rs {r[18]:,.1f} ({source})\n")
    cols = ["date", "seller", "item", "description", "purity", "grams", "gold_value", "making", "other", "discount",
            "tax", "paid", "value_now"]
    print(it[cols].to_string(index=False, float_format="{:,.2f}".format, formatters={"date": "{:%Y-%m-%d}".format}))
    for c, fx in it[it.currency != "INR"][["currency", "fx"]].drop_duplicates().itertuples(index=False):
        print(f"{c} converted at {fx} INR")
    by = it.groupby("purity").agg(grams=("grams", "sum"), paid=("paid", "sum"), value_now=("value_now", "sum"))
    print("\n" + by.to_string(float_format="{:,.2f}".format))
    print(f"total {it.grams.sum():.3f} g, paid Rs {it.paid.sum():,.0f}, value now Rs {it.value_now.sum():,.0f}")
    for n in notes:
        print("NOTE", n)


if __name__ == "__main__":
    main()
