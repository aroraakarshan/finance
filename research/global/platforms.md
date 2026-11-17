# Platforms: every way an Indian resident can invest abroad (Nov 2026)

Written 2026-11-15. Market research, not advice; no orders. Every fact has a source tag [P#] (list at
the end, all read 2026-11-15). "not verified" = no primary source found. IBKR products, fees, SYEP,
bonds: see [ibkr-global](../themes/ibkr-global.md) (not repeated). INDmoney -> IBKR move: see
[migration](../../portfolio/migration-indmoney-to-ibkr.md). Estate tax: [us-estate-tax](../themes/us-estate-tax.md).

## Summary
- Keep IBKR (IB LLC, cash account) as the only foreign broker: cheapest at this size, and it has Irish UCITS ETFs that avoid US estate tax.
- Finish the INDmoney -> IBKR transfer and close INDmoney US. Do not add Angel One US, Groww, Vested or similar apps (US-listed only, 0.1-0.25% per trade); avoid Stockal.
- Indian international funds are nearly all closed and ETFs trade at 11-86% premiums: skip. GIFT City funds and NSE IX Global Access: watch, not now.
- LRS allows listed stocks/ETFs/funds and property; not margin, derivatives or forex trading. TCS 20% on investment remittances above Rs 10 L per FY (a tax credit).

## 1. What LRS / FEMA allows (RBI text)

| Item | Status | Source (date) |
|---|---|---|
| Limit | USD 250,000 per FY, all purposes together (travel, gifts, investing) | LRS Master Direction para 7, updated 2024-09-06 [P1] |
| Listed foreign shares, ETFs, regulated foreign funds | Allowed (OPI) | OI Directions 2022-08-22, para 1(ix)(e)(f) [P2] |
| Margin / margin calls to overseas exchanges or counterparties | NOT allowed | LRS MD para 5 [P1] |
| Derivatives (options, futures, CFDs, event contracts) | NOT allowed "unless otherwise permitted by RBI" | OI Directions para 1(ix)(a) [P2] |
| Unlisted debt; commodities incl. bullion depository receipts | NOT allowed as OPI | same [P2] |
| Forex trading abroad / on unauthorised platforms | NOT allowed; penal action under FEMA. Alert list last expanded 2025-11-19 (+7: Starnet FX, CapPlace, Mirrox, Fusion Markets, Trive, NXG Markets, Nord FX); list "not exhaustive" | RBI via Upstox [P3]; LRS FAQ Q2 (2023-04-06) [ibkr-global/sources.md S2] |
| Property abroad | ALLOWED ("acquisition of immovable property abroad") | LRS MD para 6 [P1]; OI Rules rule 21 [P2 para 25] |
| Unlisted foreign shares (startups, private cos) | Counts as ODI (any unlisted equity, or >=10% / control of a listed one); individuals only in an operating entity, not financial services (relaxed in IFSC) | OI Directions 1(vi), 22, 24 [P2] |
| Foreign currency account abroad or in GIFT IFSC | Allowed; no domestic settlements from IFSC accounts | LRS MD para 6, 11 [P1] |
| Bank loan to fund capital-account LRS | NOT allowed | LRS MD para 12 [P1] |
| Idle sale proceeds | Reinvest or bring back within 180 days | LRS MD para 17 [P1] |
| Crypto | Grey; GAP framework excludes crypto | IFSCA circular 2025-08-12 via CAM [P4] |
| Paperwork | Form A2 per remittance, one designated bank branch; bank account >=1 yr or extra checks | LRS MD Annex [P1] |

Pending (not law): RBI reportedly proposed a Rs 50 L sub-limit for some LRS uses (business travel,
pilgrimage) and a bar on LRS for foreign fixed deposits; listed stocks/funds reported to stay
allowed; "no start date" (Zee Business 2026-10-27 via Livemint [P5], The Hindu 2026-11-12 [P6]).
Not found on rbi.org.in: not verified.

## 2. Cost of moving money out

- **TCS** (s.206C(1G); new Act s.394 [tax/investment-types.md]): no TCS up to Rs 10 L per FY across all
  LRS purposes (from Budget 2025); above that 20% for investment. Budget 2026 cut education/medical
  to 2% and tour packages to flat 2%; investment stays 20% (Upstox 2026-02-01 and 2026-05-20 [P7];
  ICICI/HDFC notices effective 2026-04-01 via Livemint [P8]). TCS is a tax credit (Form 27D/26AS,
  adjust in ITR or advance tax), so it is a cash-flow cost, not a loss.
- **Bank wire (SBI/HDFC/ICICI)**: fixed fee about Rs 500-1,000 plus about 2% spread over interbank
  (India INX GA interview, Aug 2026, an interested party [P9]); ET puts bank FX at 1.5-2% over spot
  vs ~40 paise for some fintechs (2025-12-22 [P10]). Bank-specific fee pages need JavaScript: not verified.
- **Wise**: its INR purpose-code list has no "investment abroad" code (2026-11-15 [P11]), so not usable
  to fund a broker (not verified with Wise). **Niyo, BookMyForex**: compared for transfer cost by ET
  [P10]; investment purpose support not verified.
- **In-app funding (INDmoney, Groww, Angel One, Zerodha)**: bank rate; Zerodha states 0.5-1.2% over
  RBI reference [P12]; INDmoney lists 0.5-1.2% "charged by bank" [P13].

## 3. Platform table

Costs = commission; FX markup; remittance fee; custody / inactivity. US stocks unless noted.

| Platform | Entity / regulator | Markets | Costs | Min | Pros | Cons | Open / install |
|---|---|---|---|---|---|---|---|
| **IBKR (IB LLC)** - current | Interactive Brokers LLC (SEC/FINRA, SIPC); IB India is a separate SEBI broker for Indian markets only [ibkr-global/rules.md s.2] | US, LSE, Euronext, Xetra, SIX, HKEX, TSE, ASX, SGX [ibkr-global] | USD 0.005/sh min USD 1 (US); 0.05% min GBP/EUR 3 (Europe); FX 0.2 bp min USD 2; Indian bank wire cost; no custody/platform fee [ibkr-global/sources.md S4,S5,S16]; inactivity: none found | none | Cheapest at size; Irish UCITS ETFs (no US estate tax); one account | Bank FX spread; English-only support; time zones | IBKR Mobile, IBKR Desktop, TWS, Client Portal (pages live [P14]) |
| **NSE IX Global Access** | NSEIX GA IFSC Ltd, first IFSCA GAP [P15] | US stocks/ETFs (Feb 2026); 7 European markets + 8,200 UCITS ETFs (2026-11-13) [P15,P16] | Not published in fetchable form: not verified | ~USD 10 [P17] | Indian regulator layer; UCITS access; fractional | New; costs unknown; liquidity via partners | nseixga.com app; PAN/Aadhaar KYC [P17] |
| **India INX GA (BSE)** via brokers | IFSCA GAP; 150+ broker partners [P9] | All US-listed stocks [P9] | Zerodha 0.1% min USD 0.01 max USD 10 [P12] | none | Low cap per order; no FX profit at INXGA [P9] | Partner broker unnamed; UCITS access not confirmed [P12] | Zerodha Kite (beta, resident individuals) |
| **Angel One US** (user has Angel One) | GIFT City route, IFSCA approval [P18] | US stocks/ETFs, fractional | 0 brokerage to Dec 2026, then 0.1% min USD 0.99; bank FX; GST [P18] | not stated | Same app as Indian account | US-situs only; promo pricing | Angel One app (rollout to all by mid-Nov 2026) |
| **Groww US** | Groww IFSC (IFSCA GAP); individual Alpaca account [P19] | 10,000+ US stocks/ETFs | 0.1% min USD 1; bank FX; no AMC [P20] | USD 1 | Own-name account at Alpaca | Shut Jan 2024, relaunched 2026-09-29 [P21] | Groww app |
| **Upstox US** | GIFT City route | US | 0.25% min 0.01 max USD 25; IFSCA turnover fee [P20] | - | - | Higher % | Upstox app |
| **INDmoney** - exiting | INDmoney IFSC (IFSCA); clearing Alpaca, DriveWealth, GTN [P13] | US stocks/ETFs | 0.25%/trade; FX 0.5-1.2%; withdrawals free [P13]; ACATS out USD 125 [migration] | USD 1 | Free ITR Schedule FA | Cost; fractional shares cannot move | Close after ACATS |
| **Vested** | VF Securities Inc (FINRA/SIPC) + IFSCA GAP (Apr 2026) [P22,P23] | US stocks/ETFs, OTC | 0.25% (Basic) / 0.15% (Premium Rs 375-450/mo), max USD 35; OTC 0.5%; USD withdrawal USD 5 [P22] | USD 1 | SIPs, tax module | % fee, US-only | - |
| **Appreciate** | Appreciate Broking IFSC (IFSCA BD); custody DriveWealth [P24] | US | USD 0.10 or 0.05% + USD 0.01/share + IFSCA 0.005% [P24] | Rs 1 | Low small-ticket cost | Per-share fee | - |
| **Stockal / Borderless** | Stockal Securities (SEBI); DriveWealth [P25] | US | not checked | - | - | ~30 investors allege Rs 100 Cr+ unauthorised liquidation on 2026-10-15; DriveWealth disclaims liability (Moneycontrol 2026-11-04 [P25]) | Avoid |
| **Kuvera (CRED)** | not verified | US equities launched Sep 2026 [P26] | not verified | - | - | New | - |
| **Charles Schwab Intl** | Charles Schwab & Co (SIPC) | US | USD 0 listed equity; USD 0 min; USD 25 outgoing wire [P27] | none | Cheap US trading | India acceptance not verified; no UCITS | - |
| **Saxo** | - | - | - | - | - | home.saxo/en-in returns Not Found [P28]; India acceptance not verified | - |
| **Webull, moomoo, Tiger, eToro** | - | - | - | - | - | No India-resident offering found (not verified); CFD/derivative products barred under LRS [P2] | - |
| **NSE IX UDRs** (2022; HDFC Sec, ICICI Direct, Kotak) | NSE IX | ~50 US stocks [P9] | not verified | - | Rupee-funded via IFSC | Narrow list; status 2026 not verified | - |
| **GIFT City outbound funds** | IFSCA funds: PPFAS S&P 500 / Nasdaq 100 FoF, HDFC Dev/EM, DSP Global, Edelweiss China [P29] | Pooled US/global | FX ~2% round trip + fund fees [P29] | USD 500 (PPFAS, from 2026-08-25), others USD 5,000; top-up USD 500 [P29] | Outside MF cap | No SIP; short-term tax ~42.75% claimed [P29] (tax note: "unsettled") | Fund's IFSC portal |
| **GIFT AIFs** | IFSCA | varies | - | USD 150,000 [P30] | - | High min | - |
| **IFSC bank USD account / FD** | Bank IFSC units | USD deposit | rates not verified | - | Allowed by LRS para 11 [P1] | Reported RBI plan to bar LRS for foreign FDs [P5] | - |
| **Indian international FoFs/ETFs** (rupees, no LRS/TCS) | SEBI MFs | Global | ETF premiums: Nasdaq 100 ETF 11.0%, Q50 86.3%, FANG+ 34.5% (2026-11-06) [P31] | - | No remittance | $7 bn industry / $1 bn ETF / $1 bn per AMC caps since 2008, hit Jan 2022 [P32]; on 2026-11-06 only Baroda BNP Aqua FoF (lumpsum+SIP) and PGIM Global Real Estate FoF (lumpsum) take new money; 58 closed [P31]; AMFI asking RBI to raise cap (2026-06-28 [P33]) | - |

Tax (one line, tax/investment-types.md): foreign shares/ETFs LTCG 12.5% after 24 months else slab;
dividends at slab with credit for treaty withholding; Irish accumulating UCITS no tax till sale;
US-situs holdings above USD 60k face US estate tax (all US-stock apps above; not UCITS). GIFT funds: unsettled.

## 4. Recommended setup for this user (conditional; user decides)

- **Keep IBKR (IB LLC, cash account) as the only foreign broker.** It is the cheapest per trade at
  this size, and the only route here with confirmed Irish UCITS ETFs, which matters with 81% in
  US-situs QCOM+MSFT [us-estate-tax].
- **Finish the INDmoney -> IBKR ACATS** and close INDmoney US afterwards [migration].
- **Do not add another US app** (Angel One US, Groww, Vested, Appreciate): US-listed only, 0.1-0.25%
  per trade, and it splits records. Avoid Stockal [P25].
- **Indian international FoFs/ETFs: skip** - nearly all closed; ETFs at 11-86% premiums [P31].
- **GIFT City funds / NSE IX GA: watch, not now.** They duplicate IBKR UCITS at higher FX cost;
  revisit if NSE IX GA publishes low UCITS costs.
- **Funding:** one designated bank branch; fewer, larger wires; first Rs 10 L per FY has no TCS,
  above it 20% TCS (claim in ITR; check advance-tax impact). Watch the RBI LRS proposal [P5].

## 5. What to install / open (step by step)

1. Phone: install **IBKR Mobile**; enable IB Key two-factor login.
2. Mac: install **IBKR Desktop** (daily use, learning); **TWS** only for advanced order tools.
3. **Client Portal** (web): confirm entity = IB LLC, account type = Cash, W-8BEN valid, permissions =
   US + UK/Europe stocks and ETFs only (no options/futures/margin) [ibkr-global/rules.md s.2, ibkr-global/not-allowed.md 3.12].
4. Bank: use net-banking outward remittance ("investment in foreign equity" purpose; ask the bank
   for the code), Form A2, IBKR wire details from Client Portal; keep Form 27D for TCS.
5. Start the ACATS transfer in the IBKR portal per [migration] steps 1-5.
6. Nothing else to open. Keep Angel One for Indian MFs and gold/silver.

## Sources (read 2026-11-15; score 1-5)

- P1 RBI LRS Master Direction (upd. 2024-09-06): rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10192 (5)
- P2 RBI FEM (Overseas Investment) Directions 2022-08-22: rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12381 (5)
- P3 Upstox, RBI alert list, 2025-11-19: upstox.com/news/personal-finance/trading/rbi-alert-list-updated-...-184938/ (3)
- P4 Cyril Amarchand, GAPs in IFSC, 2026-07-13: corporate.cyrilamarchandblogs.com/2026/07/global-access-providers-in-ifsc-gift-city-a-gateway-to-global-markets/ (4)
- P5 Livemint, RBI Rs 50 L LRS sub-limit, 2026-10-28: livemint.com/...-11793174934652.html (3)
- P6 The Hindu explainer, 2026-11-12: thehindu.com/business/Economy/why-rbi-wants-to-cap-...-article71693547.ece (3)
- P7 Upstox Budget 2026 TCS, 2026-02-01 (article-188714) and TCS guide 2026-05-20 (article-1667) (3)
- P8 Livemint, ICICI/HDFC TCS notices, 2026-04-20: livemint.com/...-11776689734056.html (3)
- P9 Moneycontrol, India INXGA interview, 2026-08-13: moneycontrol.com/...-14004358.html (3)
- P10 ET, direct broker vs Indian platforms 2025-12-22 (126088056); Niyo vs BookMyForex 2025-12-23 (126139339) (2)
- P11 Wise INR purpose codes: wise.com/help/articles/6hAFdOM3eAYMyvnOQ0c1g/inr-purpose-codes (4)
- P12 CNBC-TV18, Zerodha US stocks beta, 2026-10-19: cnbctv18.com/...-20014858.htm (3)
- P13 INDmoney US stocks page: indmoney.com/us-stocks (4)
- P14 IBKR platform pages (HTTP 200): interactivebrokers.com/en/trading/ibkr-desktop.php, tws.php, ibkr-mobile.php (5)
- P15 BusinessLine, NSEIX GA Europe, 2026-11-13: thehindubusinessline.com/...article71697970.ece (3)
- P16 Moneycontrol, NSE IX GA launch, 2026-02-25: moneycontrol.com/...-13842990.html (3)
- P17 Moneycontrol, how NSEIX GA works, 2026-03-25: moneycontrol.com/...-13870321.html (3)
- P18 Fortune India, Angel One US stocks, 2026-10-19: fortuneindia.com/markets/...-165667 (3)
- P19 Groww blog, US stocks guide, 2026-11-05: groww.in/blog/investing-in-us-stocks-through-groww (4)
- P20 Moneycontrol, Zerodha vs Groww vs Upstox, 2026-10-22: moneycontrol.com/...-14057101.html (3)
- P21 Groww shut 2024-01-23 (Business Today/ET headlines); relaunch BusinessLine 2026-09-29 (headline only) (2)
- P22 Vested India pricing (modified 2026-06-30): vestedfinance.com/in/pricing/ (5)
- P23 ET, Vested GAP licence, 2026-04-29: economictimes.indiatimes.com/...130603617.cms (3)
- P24 Appreciate home page fee table: appreciatewealth.com (via r.jina.ai) (4)
- P25 Moneycontrol, Stockal unauthorised liquidation, 2026-11-04: moneycontrol.com/...-14067863.html (3)
- P26 Times of India, Kuvera by CRED US equities, 2026-09-28: timesofindia.indiatimes.com/...134546384.cms (2)
- P27 Schwab International account and pricing pages: international.schwab.com/us-investing-brokerage-account, /pricing (4)
- P28 Saxo India: home.saxo/en-in (Not Found page) (1)
- P29 Livemint, GIFT City funds, 2026-09-02: livemint.com/...-11788363937758.html (3)
- P30 ET, GIFT City for residents, 2026-06-12: economictimes.indiatimes.com/...131676324.cms (3)
- P31 Value Research, international funds open, 2026-11-06: valueresearchonline.com/stories/230182/ (4)
- P32 Value Research, 12 still take SIP, 2026-07-03: valueresearchonline.com/stories/228977/ (4)
- P33 Livemint, AMFI seeks cap review, 2026-06-28: livemint.com/...-11782637240095.html (3)

Open checks: NSE IX GA fee schedule; Saxo/Schwab/eToro India acceptance; IFSC bank FD rates; RBI
notification of the LRS proposal; bank purpose code and TT spread at the user's bank.
