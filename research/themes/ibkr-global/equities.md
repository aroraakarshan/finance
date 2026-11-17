# IBKR global: foreign stocks, Irish UCITS ETFs, fractional shares, mutual funds

Part of [IBKR global products for an Indian resident](../ibkr-global.md). Source tags [S#] are listed in [sources.md](sources.md).

## Summary

- All four are allowed under LRS (listed equity or regulated fund units) [S3].
- Irish accumulating UCITS ETFs (CSPX, VUAA 0.07%; VWRA 0.14%; SWDA 0.20%) fit best: no income
  until sale, 15% US withholding inside the fund, not US-situs for estate tax [S8][S9][S10][S13].
- Single foreign stocks add FX cost (about 0.03%) and order minimums (EUR 3, CHF 5, HKD 18) [S4][S5].
- Tax: long-term after 24 months at 14.95%, else 35.88% (tax/investment-types.md section 1).

## 3. Instruments (equity)

### 3.1 Stocks and ETFs on LSE, Euronext, Xetra, SIX, HKEX, TSE, ASX, SGX
- What: shares listed on foreign exchanges, bought in local currency. Access: yes, needs the
  stock trading permission for each region (permission names not verified).
- IBKR Pro Fixed commission [S4]:

| Market | Fixed rate | Minimum per order | Note |
|---|---|---|---|
| UK (LSE) | 0.05% | GBP 3 | minimum for USD-traded LSE lines: not verified |
| France, Belgium (Euronext) | 0.05% | EUR 3 | Netherlands table not read |
| Germany (Xetra) | 0.05% | EUR 3 | |
| Switzerland (SIX) | 0.05% | CHF 5 | |
| Hong Kong (HKEX) | 0.08% | HKD 18 | |
| Japan (TSE) | 0.08% | JPY 80 | |
| Australia (ASX) | 0.08% | AUD 6 | |
| Singapore (SGX) | 0.08% | SGD 2.50 | |

- Tiered is cheaper (e.g. Europe min EUR 1.25, max EUR 29) but adds exchange/clearing fees [S4].
- Euronext ETFs: EUR 0.75 exchange fee per execution passed through [S4].
- UK: 0.5% stamp duty/SDRT on buying UK company shares [S18]; ETFs: not verified (Irish ETFs are
  not UK-incorporated, so likely exempt - not verified). HK, Japan, Australia, Singapore duties:
  not verified.
- FX: auto-conversion adds about 0.03% to the rate; a manual FX order costs 0.20 bp, min USD 2
  [S5]. US interest on idle USD aside, other currencies held in small amounts earn 0% [S6].
- Custody: IBKR says no custody or platform fees [S16].
- Liquidity: large caps fine; small foreign stocks have wide spreads (not measured).
- Risk: stock risk + currency risk + time-zone (markets open while the user sleeps).
- LRS: allowed (listed equity = OPI) [S3]. Tax: gains long-term after 24 months at 14.95%, else
  35.88%; dividends at slab with credit for foreign tax (Japan treaty 10%, Germany 10% with a slow
  reclaim of the excess, HK 0%) [tax/investment-types.md section 1].

### 3.2 Ireland-domiciled UCITS ETFs (CSPX, VUAA, VWRA, SWDA/IWDA)
| ETF | Index | TER | Income | Domicile | Source |
|---|---|---|---|---|---|
| CSPX (IE00B5BMR087) | S&P 500 | 0.07% | Accumulating | Ireland | [S8] |
| VUAA (IE00BFMXXD54) | S&P 500 | 0.07% | Accumulating | Ireland | [S9] |
| VWRA (IE00BK5BQT80) | FTSE All-World | 0.14% | Accumulating | Ireland | [S9] |
| SWDA/IWDA (IE00B4L5Y983) | MSCI World | 0.20% | Accumulating | Ireland | [S8] |
SWDA (LSE) and IWDA (Euronext Amsterdam) are the same ISIN (exchange tickers: not verified).
- Withholding: US-Ireland treaty Art. 10 caps US tax on portfolio dividends at 15% [S10], so the
  Irish fund suffers 15% on US dividends (inside the fund, cuts return ~0.15-0.2%/yr at a ~1-1.3%
  yield; yield figure not verified). A US-domiciled ETF pays dividends to the user; US default is
  30% for foreign persons [S12]; India-US treaty Art. 10 caps it at 25% for individuals (15% only
  for companies owning 10%+) [S11]. Accumulating UCITS ETFs pay no dividend to the user.
- US estate tax: applies to a non-resident's US-situated assets, including stock of US
  corporations; return needed above USD 60,000 [S13]. An Irish fund is not a US corporation, so
  CSPX/VWRA are outside this rule; US ETFs and QCOM/AVGO/VRT/IBKR/MSFT are inside it [S13].
  Rates 18-40%, no Indian credit; QCOM+MSFT alone are about USD 192.5k, over 3x the threshold
  [tax/investment-types.md section 4].
- PRIIPs/KID: EU/UK retail clients cannot buy US ETFs without a KID. For an Indian resident at
  IB LLC both US and UCITS ETFs should be open: not verified (no IBKR page found).
- Cost: LSE USD lines (CSPX, VUAA, VWRA) Fixed 0.05% [S4] (USD minimum not verified); no FX
  needed if bought in USD.
- LRS: allowed (listed fund units) [S3]. Tax: accumulating = no Indian tax until sale (no
  deemed-income rule found); sale long-term after 24 months at 14.95%, else 35.88%; Ireland
  withholds 0% on distributions to the user; US ETF dividends suffer 25% US withholding (matches
  [S11] above). Bond UCITS may be "always short-term" under AF s.76 (35.88%)
  [tax/investment-types.md sections 0 and 1].

### 3.7 Fractional shares
- 10,500+ US stocks/ETFs from USD 1; also eligible Canadian and European stocks [S19]. Commission
  same as whole shares, min USD 0.01 (greater of 1% or USD 0.01 for fractional trades) [S4 note 11].
- Open to Indian residents at IB LLC: not verified (check the Trading Permissions page).
- LRS: allowed (listed equity). Tax: as whole shares - 24 months, 14.95% / 35.88%
  [tax/investment-types.md section 1].

### 3.8 IBKR mutual fund marketplace
- 50,000+ funds, 500+ families, "available to residents worldwide"; country-specific list via the
  fund search tool [S20]. Non-US residents: many funds free, others GBP/EUR 4.95 per trade
  (Allfunds); Euronext funds 0.1% min EUR 4 [S21]. Which funds an Indian resident sees: not verified.
- LRS: regulated overseas fund units = allowed [S3]. Tax: equity funds like foreign shares
  (24 months, 14.95% / 35.88%); debt funds (>65% debt) may be always short-term under AF s.76
  [tax/investment-types.md sections 0 and 1].
