# Broker MCPs: Alpaca and India

## Summary
Read-only by design: Upstox Analytics Token and Zerodha's hosted Kite MCP, but the user has
neither account. AngelOne SmartAPI (user's broker) has no read-only key and needs PIN + TOTP:
keep using file exports. Dhan and Groww MCPs place real orders: do not use. Alpaca MCP is US
only; use paper keys and data toolsets only. NSE libraries (jugaad-data, nsepython) are
unofficial scrapers: backup only.

Index: [Broker MCP servers and APIs](../mcp-brokers-india.md). Sources [S#]: [sources.md](sources.md).

## Alpaca (official MCP)
- What: `alpacahq/alpaca-mcp-server` v2 (PyPI 2.4.1, 2026-11-04; 1,086 stars, 34 open issues,
  last push 2026-11-13, MIT) [S11][S17][S18]. Stocks, ETFs, options, crypto, news, corporate
  actions. Local stdio only; README warns not to expose it remotely [S17].
- Safety: `ALPACA_PAPER_TRADE` defaults to `true`; paper keys come from a free paper account
  [S17]. `ALPACA_TOOLSETS` limits tools (e.g. `stock-data,news,corporate-actions`) [S17].
  Catch: positions sit in the `trading` toolset with orders, so seeing positions means exposing
  order tools; `watchlists` also writes. No read-only API key type found [S17].
- Cost / data: free plan IEX only, 200 calls/min, 7+ years history; Algo Trader Plus
  $99/month for all US exchanges [S19]. US only; no India/Europe/Japan.
- Use: `finance-trader` (US bars), `finance-news` (news), data toolsets and paper keys only;
  agent paper orders need explicit user approval. Indian resident direct account "not verified".
  Fit **2** - good official server, but US data overlaps yfinance and no read-only key.

## India
**Zerodha Kite MCP (official, `zerodha/kite-mcp-server`)** - 330 stars, 71 open issues,
last push 2026-11-11, MIT, Go [S11][S20]. Hosted `https://mcp.kite.trade/mcp`: login via Kite,
"Read-only access", no API key needed; README says the hosted server excludes order tools
[S20][S21]. Self-hosted needs own Kite Connect key and exposes place/modify/cancel and GTT
tools unless `EXCLUDED_TOOLS=place_order,modify_order,cancel_order,...` is set [S20]. Kite
Connect: Personal free (orders, GTT, alerts, margins, portfolio); Connect adds live WebSocket
and historical candles for Rs 500/month [S22]. Coverage NSE/BSE/MCX via Zerodha. User has no Zerodha
account. Fit **2** (best-designed India MCP, but needs a new account).

**Upstox (official MCP + Analytics Token)** - MCP gives read-only access to holdings, orders,
positions, mutual funds, funds, profile via OAuth [S23]. Analytics Token: free, 1-year,
"strictly read-only", GET only, cannot place or modify orders; covers quotes, historical data,
option chain, fundamentals, news, IPO without static IP; portfolio, orders, P&L need a
whitelisted static IP; one token per account [S24]. SDK `upstox/upstox-python` 192 stars, MIT,
last push 2026-11-09 [S11]. Community Upstox MCPs are tiny (2-5 stars) [S11]. User has no
Upstox account. Fit **3** - read-only by design and free NSE/BSE data with fundamentals; worth
it only if the user opens an Upstox account (for data, it can stay unfunded - "not verified").

**AngelOne SmartAPI (user's Indian broker)** - free APIs [S25]; official SDK
`angel-one/smartapi-python` (180 stars, 21 open issues, last push 2025-05-27, no licence file;
PyPI 1.5.5, 2025-02-07) [S11][S26]. Login = API key + client code + PIN + TOTP from the QR
secret (`pyotp`) -> JWT that can also trade [S26]. Endpoints: profile, funds, holdings, all
holdings, positions, order and trade book, LTP, quote, historical candles, option greeks,
gainers/losers, CAS [S27]. Rate limits: getHolding, getAllHolding, getPosition, order book 1/s;
quote 10/s; orders 9/s combined [S27]. No read-only key or scope found in the docs index [S27]
("not verified" that none exists). No official MCP found; community `bhavesh0009/angel-one-mcp-server`
(7 stars, MIT, last push 2025-07-26) places, modifies and cancels orders and takes password +
TOTP secret in env [S11][S28]. Storing a TOTP secret lets any script log in fully. Fit **2**:
keep using file exports (`scripts.brokers.angelone`); if an API is wanted, a small script with
only GET calls, run by `finance-main` with credentials typed at the prompt.

**Dhan (official MCP)** - `https://mcp.dhan.co/mcp`, OAuth; tools include orders and trading;
docs example "Place a limit buy ... places a real order with confirmation" [S29]. API free;
data API 5/s, 100,000/day [S29][S30]. No account. Fit **1**.

**Groww (official MCP)** - `https://mcp.groww.in/mcp`; examples include placing limit and
stop-loss orders; sell orders need DDPI [S31]. Trade API Rs 499/month + tax (early-bird), data
history up to 3 months [S32]. No account. Fit **1**.

**NSE data** - Official: NSE Data & Analytics sells streaming, snapshot, end-of-day,
historical and corporate data feeds (paid; prices "not verified") [S33]. Unofficial libraries
that call the NSE website: `jugaad-data` (599 stars, 27 issues, last push 2026-11-11, no
licence detected; NSE stocks/F&O/index, RBI rates, AMFI NAV, has caching to avoid blocks)
[S11][S34]; `nsepython` (373 stars, GPL-3.0, last push 2026-10-07; separate "server edition"
for cloud IPs) [S11][S35]. Risks: unofficial, break when NSE changes its site, IP blocks
(`nseindia.com/api` was blocked in our own tests, see `research/sources.md`), NSE website
terms on automated access "not verified" (terms page 404). No orders, so safe on that axis.
Use: `finance-news` (announcements), `finance-scout` (bhavcopy screens) as backup to
niftyindices/screener.in. Fit **2**. (Data-only NSE MCPs such as Tapetide - 150 stars, free
50 calls/day [S36] - belong in the data-MCP file, not here.)
