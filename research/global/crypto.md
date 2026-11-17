# Crypto (bitcoin, ether) for an Indian resident

Written 2026-11-15 by `finance-research`. Research only, not advice; no orders. Sources [K#] at
the end. "nv" = not verified. Prices: yfinance, BTC/ETH to 2026-11-14 [K1].

## Summary
- Verdict: skip. Buying abroad under LRS is grey, RBI favours a ban (2026-07-08) and GIFT
  platforms may not offer crypto to residents [K5, K6].
- Bitcoin USD 64,365, -48% from its 2025-10-06 peak, 45% volatility; JPM base case 10%/yr,
  bear -9.7%/yr [K1, K9].
- If he insists: at most 1-2% on an FIU-registered Indian exchange (35.88% tax, 1% TDS).

## 1. What it is

- Bitcoin: fixed-supply digital token, no cash flows; price = what the next buyer pays.
  Ether: token of the Ethereum network (fees, staking). Everything else is smaller and riskier.
- Ways to own: (a) coins on an exchange or own wallet; (b) a fund/note that holds coins: US spot
  ETFs (IBIT) or European ETPs (exchange-traded notes, ETN) on Xetra/SIX/LSE/Euronext.

## 2. Access for an Indian resident

| Route | Status | Detail |
|---|---|---|
| Indian exchange (INR) | Legal, taxed, unregulated | Any platform serving Indians must register with FIU-IND under PMLA (since Mar 2023) [K2]. FIU sent notices to 15 offshore platforms and sought app/URL blocks on 2026-09-09; 9 big ones (Binance, Kraken, KuCoin) in Dec 2023, Binance then registered and paid Rs 18.82 Cr [K2]. Coinbase launched in India with INR rails 2026-05-31 (headline only) [K3]. Official FIU registered list: nv |
| LRS remittance to buy coins abroad | Grey | No RBI text permits or bars it; OI Directions bar "commodities" and derivatives, silent on crypto (`research/themes/ibkr-global/rules.md` section 1). Whether banks refuse such remittances: nv (no source found) |
| IBKR spot crypto (Paxos/zerohash) | Grey; eligibility nv | `../themes/ibkr-global/not-allowed.md` 3.10; IBKR page does not list India eligibility [K4] |
| US spot ETFs (IBIT, FBTC) via IBKR | Grey; US-situs | Listed US ETF, so LRS "listed security" logic would apply, but crypto underlying. IFSCA's revised Global Access circular (2025-08-12) bars GIFT City Global Access providers from offering crypto-linked products to Indian residents; Vested stopped IBIT/FBTC etc. on 2025-09-15, existing holders may hold/sell [K5]. IBKR LLC is not a GIFT provider; whether IBKR blocks Indian clients: nv. US estate tax above USD 60k (`us-estate-tax.md`) |
| European ETPs (IB1T, BITC) via IBKR | Grey; not US-situs | Listed notes (see table); same crypto-underlying doubt; IBKR availability for Indian clients: nv |
| GIFT City platforms | Not allowed | IFSCA excludes crypto from permissible products [K5] |

Policy direction: RBI still favours a ban (Reuters via India Today, 2026-07-08); the 2021 ban
bill was never introduced; the government discussion paper has been delayed several times [K6].

| European ETP [K7] | Ticker (exchange, ccy) | ISIN | Issuer domicile | TER | Size |
|---|---|---|---|---|---|
| iShares Bitcoin ETP (physical) | IB1T (Xetra EUR, LSE GBP), BTCN (Euronext USD) | XS2940466316 | Switzerland | 0.15% | EUR 1,226 m |
| CoinShares Physical Bitcoin | BITC (LSE USD, Xetra EUR, SIX) | GB00BLD4ZL17 | Jersey | 0.15% | EUR 1,389 m |
| 21Shares Bitcoin ETP | ABTC (SIX USD), BTCU (LSE USD) | CH0454664001 | Switzerland | 1.49% | EUR 516 m |

## 3. State now

| Item | Last | 1y | 3y/yr | 5y/yr | 10y/yr | Off peak | Vol 3y [K1] |
|---|---|---|---|---|---|---|---|
| Bitcoin (BTC-USD) | USD 64,365 | -31.8% | +21.9% | -0.3% | +57.1% | -48.4% (peak 124,753 on 2025-10-06) | 45% |
| Ether (ETH-USD) | USD 1,774 | -42.9% | -3.6% | -17.4% | - | -63.3% (peak 4,831 on 2025-08-22) | 69% |

- Low this cycle so far USD 58,559 on 2026-06-30 [K1]. US bitcoin ETFs lost about USD 2.35 bn
  in two weeks; IBIT 11 straight days of outflows (headlines 2026-11-14) [K8].
- European ETPs: -29% in 1y in EUR (justETF) [K7].
- No valuation measure exists (no earnings, no yield).

Drawdown history (bitcoin, yfinance closes) [K1]:

| Peak | Trough | Fall |
|---|---|---|
| USD 19,497 (2017-12-16) | USD 3,237 (2018-12-15) | -83% |
| USD 67,567 (2021-11-08) | USD 15,787 (2022-11-21) | -77% |
| USD 124,753 (2025-10-06) | USD 58,559 (2026-06-30) so far | -53% |

## 4. Expected return evidence

| Source (date) | Forecast |
|---|---|
| J.P. Morgan 2027 LTCMA (2026-10-19) [K9, K10] | Bitcoin base 10%/yr over 10 yrs; bear -9.7%/yr, bull +17%/yr. First JPM range; bitcoin "not included as an allocation"; called "speculative" with unstable correlations, not a diversifier |
| Research Affiliates, GMO, Vanguard | No crypto forecast found (nv) |

A -9.7%/yr bear case means about -64% over 10 years: the range is wide on purpose.

## 5. Risks

- Volatility 45% (BTC) / 69% (ETH); three falls of 53-83% in 9 years [K1].
- India: RBI favours a ban; rules can change overnight (Vested/IFSCA, 2025) [K5, K6].
- Tax (Indian exchange): 30% flat (35.88% at his income), only cost deductible, losses cannot be
  set off or carried forward, 1% TDS with an Indian payer [tax/investment-types.md section 3].
  So a loss year costs fully and a gain year is taxed at 35.88%.
- Tax (ETF/ETP units abroad): no row in `tax/investment-types.md`; could be taxed as a foreign
  ETF/note (24 m / 12.5%) or as VDA (30%). CA before buying.
- Correlates with tech/risk assets in sell-offs (JPM: unstable correlation) [K10]; he is 81% in
  US tech already.
- Exchange/custody failure, hacks; offshore apps can be blocked in India [K2].

## 6. Instruments and verdict

| Rank | Instrument | Why |
|---|---|---|
| 1 | Nothing now | Legal grey under LRS, unclear tax on ETPs, 81% already in volatile tech |
| 2 | If he insists: small amount on an FIU-registered Indian exchange | Clear legal footing and tax (35.88%, 1% TDS); cap at 1-2% of portfolio, money he can lose |
| - | IBIT (US-situs), IB1T/BITC (grey + tax unclear), IBKR spot crypto (eligibility nv) | Skip until RBI/CBDT clarify |

**Verdict: skip.** JPM's 10% base case does not pay for a 45-70% volatility asset with grey
LRS status, punitive Indian tax and a regulator that favours a ban.

## Sources (all read 2026-11-15)

- K1 yfinance BTC-USD, ETH-USD. Worked.
- K2 CoinDesk, FIU notices to 15 platforms, 2026-09-09: https://www.coindesk.com/policy/2026/09/09/india-s-financial-intelligence-unit-flags-15-crypto-platforms-for-aml-lapses
- K3 Google News headline "Coinbase launches in India with direct INR rails", 2026-05-31 (page not opened).
- K4 IBKR crypto page: https://www.interactivebrokers.com/en/trading/products-cryptocurrencies.php
- K5 MediaNama, Vested halts crypto ETFs, 2025-09-18: https://www.medianama.com/2025/09/223-vested-finance-stops-crypto-etfs-india/
- K6 India Today (Reuters report), 2026-07-08: https://www.indiatoday.in/business/story/rbi-backs-crypto-ban-again-tax-department-cites-tracking-and-tax-risks-report-2943207-2026-07-08
- K7 justETF: https://www.justetf.com/en/etf-profile.html?isin=XS2940466316 (and GB00BLD4ZL17, CH0454664001)
- K8 Headlines (TradingView/Cointelegraph, Cointribune) 2026-11-14, not opened: https://www.tradingview.com/news/cointelegraph:dcc873f4a094b:0-bitcoin-etfs-shed-2-35b-in-2-weeks-blackrock-s-losing-streak-hits-11/
- K9 J.P. Morgan 2027 LTCMA press release, 2026-10-19: https://www.prnewswire.com/news-releases/jp-morgan-releases-2027-longterm-capital-market-assumptions-projecting-7-0-return-for-6040-portfolio-over-10-15-years-302912421.html
- K10 CoinDesk on JPM bitcoin range, 2026-10-20: https://www.coindesk.com/markets/2026/10/20/jpmorgan-sees-10-annual-bitcoin-returns-topping-stocks-bonds-and-gold-over-next-decade
