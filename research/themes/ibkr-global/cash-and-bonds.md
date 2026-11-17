# IBKR global: bonds, money funds, idle cash, share lending

Part of [IBKR global products for an Indian resident](../ibkr-global.md). Source tags [S#] are listed in [sources.md](sources.md).

## Summary

- USD cash earns 0% on the first USD 10k, then 3.38% (rates as of 2026-11-13); the user's USD 795
  earns nothing [S6].
- Direct US bonds and CDs are LRS-grey (OTC debt) [S3]; bond ETFs and money funds may be always
  short-term under AF s.76 at 35.88% (tax/investment-types.md sections 0 and 1).
- For idle USD prefer cash interest; for long-term money prefer equity UCITS (see 3.13).
- Do not enrol in SYEP: a loan may count as a sale and reset the holding period.

## 3. Instruments (cash and debt)

### 3.3 US Treasuries, T-bills, corporate and municipal bonds, CDs
- Commission [S14]: Treasuries 0.002% of face, min USD 5; corporate and CDs 0.1% of first USD 10k
  face (min USD 1), 0.025% above, max USD 250; munis 0.05% (min USD 1). USD 50 extra if the bond
  desk handles the order by phone. T-bills are sold in USD 100 steps at Treasury auction [S15];
  IBKR minimum lot: not verified.
- Liquidity: Treasuries deep, trade ~22 h/day at IBKR [S17]; corporates/munis/CDs thin.
- Risk: Treasuries low credit risk, price falls if rates rise; corporates add credit risk.
- LRS: GREY. OPI may not be in "unlisted debt instruments" [S3]; most US bonds and CDs trade OTC,
  not on a recognised exchange. Munis give US tax-exemption that a non-US person does not need.
  Listed Treasury ETFs are clean on LRS (listed fund units [S3]) but not on tax (below).
- Tax: interest at slab 35.88%. US withholding 0% on Treasuries (portfolio interest), registered
  corporates and CDs. Corporate bonds and US bond ETFs may be "always short-term" under AF s.76
  ("unlisted bond" / >65% debt fund), so every gain is taxed at 35.88% whatever the holding
  period; T-bill discount: interest vs gain unsettled. Munis: US exemption does not carry over
  [tax/investment-types.md sections 0 and 1].

### 3.4 US money market funds and IBKR alternatives
- IBKR has a mutual fund marketplace (below) but no default sweep into money funds ("We do not
  sweep your cash into low-yield programs") [S6]. Whether US money funds are sold to Indian
  residents at IB LLC: not verified. Alternatives: IBKR cash interest (3.5 below), short Treasury ETFs.
- LRS: regulated fund units = allowed [S3]. Tax: dividends at slab with 25% US withholding
  (interest-dividend exemption depends on fund designation, not verified at IBKR); gains probably
  always short-term under AF s.76, 35.88% [tax/investment-types.md section 1]. Same 35.88% as cash
  interest but with a 25% US withholding layer and a CA question, so cash above USD 10k is simpler.

### 3.5 Interest on idle cash
- USD: 0% on the first USD 10,000; 3.38% (benchmark - 0.5%) above it for Pro, 2.38% for Lite;
  rates as of 2026-11-13 [S6]. Full rate needs NAV > USD 100,000; below that the rate is cut in
  proportion to NAV; the USD 10k zero-band applies per currency [S6]. Paid monthly [S6].
- User: USD 795 earns nothing. Only cash above USD 10k earns. INR cash earns 0% [S6].
- Also note: the Insured Bank Deposit Sweep (FDIC) eligibility for Indian residents: not verified.
- LRS: holding cash abroad is allowed, but unused funds fall under the 180-day rule [S2 Q4].

### 3.6 Stock Yield Enhancement Program (SYEP)
- IBKR lends the user's fully-paid shares; pays 50% of the market lending rate on collateral [S7].
- Eligible: margin accounts, or cash accounts with liquid net worth > USD 25,000. IB India clients
  NOT eligible; Indian clients of IB LLC eligible [S7].
- Risks: lent shares may not be SIPC-protected (collateral given instead), voting rights lost,
  dividends on lent shares may come as "payment in lieu" (US withholding treatment: not verified)
  [S7]. Big-cap shares like QCOM/AVGO rarely earn much (no rate data checked).
- LRS: grey (securities lending is not named in [S1][S3]). Tax: fee and substitute dividends at
  slab; foreign lending is outside the Indian SLB exclusion, so each loan MAY count as a sale and
  reset the 24-month holding period (CA) [tax/investment-types.md sections 0 and 1]. This risk
  outweighs the small fee on large caps: do not enrol.

### 3.13 Changes after the tax note (tax/investment-types.md, 2026-11-15)

- Conflict, fixed: section 3.3 first proposed listed Treasury ETFs as the "safer route" (fit 4).
  The tax note says US bond ETFs and money funds may be always short-term under AF s.76 (35.88%)
  [tax/investment-types.md sections 0 and 1]. Fit cut to 2 (Treasury ETFs) and 1 (money funds).
  Cash interest above USD 10k is also taxed at 35.88% but has no AF s.76 or 25% US withholding
  question, so for idle USD prefer cash interest; for long-term money prefer equity UCITS
  ([equities.md](equities.md) 3.2).
- Conflict, fixed: SYEP fit cut from 2 to 1 (loans may count as sales and reset holding periods).
- Agrees ([equities.md](equities.md) 3.2): Irish accumulating UCITS (no income until sale, Ireland 0%, not US-situs) stay fit 5;
  US ETF dividends 25% withholding matches [S11].
