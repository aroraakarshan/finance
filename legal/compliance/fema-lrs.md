# FEMA and LRS

## Summary
- LRS: USD 250,000 per person per FY, all purposes; ESPP payroll purchases count toward it.
- US-listed shares, ETFs, Irish UCITS and employer ESOP shares are permitted (OPI); gold ETCs and the IBKR deposit award are grey.
- Sale money and dividends abroad (ESPP, RSU or LRS shares): reinvest in permitted OPI (e.g. Irish UCITS ETFs) or bring home within 180 days of each sale; no form needed; check the IBKR $795.
- No FEMA return to file yourself; collect bank Form A2 and Form 26AS (TCS) records per FY.

Owner: `finance-legal`. Written 2026-11-15. Not legal or tax advice: findings and questions for an Indian lawyer/CA ([questions](../questions.md), section "Compliance"). The user decides and acts.

Source tags such as [L1] are listed in [sources.md](sources.md) (all read 2026-11-15). "not verified" = primary text not fetched.

## LRS limit
- Resident individuals may remit up to USD 250,000 per financial year (April-March) for any
  permitted current or capital account transaction, or both together [L1 Q1][L2 para 1].
- The limit counts all money bought or sent through all sources in India in the FY; money brought
  back does not restore it [L1 Q8].
- Not allowed: margin or margin calls abroad, forex trading abroad, FATF non-cooperative
  countries [L1 Q2].
- One designated AD bank branch for capital account remittances; Form A2 per remittance; PAN
  mandatory [L1 Q7, Q12][L2 para 15-16].

## Permitted holdings (overseas portfolio investment, OPI)
- Resident individuals may make OPI within the LRS limit under Schedule III of the OI Rules
  [L3 para 1(ix)(f)][L5 Sch. III para 1(1)]. Schedule III para 1(2)(ii) allows "OPI, including
  by way of reinvestment"; para 3: ESOP/Employee Benefit Scheme shares "without limit" if offered
  globally on a uniform basis [L5].
- OPI may not be made in: unlisted debt instruments; securities issued by an Indian resident (not
  in IFSC); derivatives unless RBI permits; "any commodities including Bullion Depository
  Receipts" [L3 para 1(ix)(a)].
- Units of an overseas fund regulated in its home country are OPI; resident individuals may
  invest [L3 para 1(ix)(e)]. So Irish UCITS ETFs are OPI. ETCs (e.g. gold IGLN) are notes, not
  fund units: the "commodities" bar may apply (`tax/global-actions-2026-11.md` N2).
- ESOP/RSU/ESPP shares up to 10% of the foreign company, without control, are OPI
  [L3 para 1(ix)(f), 22(2)].
- Employer plans: AD banks may allow remittances to buy ESOP shares; **such remittances count
  toward the employee's LRS limit**, though there is no amount cap [L3 para 22(5), 22(7)].
  So ESPP payroll purchases (NXP 2019, Qualcomm 2019-2024, Microsoft 2024-) use LRS.
  RSUs are issued without a remittance; whether anything counts toward LRS for them is not
  stated ([question](../questions.md) C2).
- Crypto: no RBI text permits or bars it (`research/themes/ibkr-global.md` s1).

| Holding | OPI status | Source |
|---|---|---|
| US-listed shares and ETFs (IBKR, Alpaca) | Allowed | [L3 1(ix)(a),(x)] |
| QCOM, NXPI, MSFT from employer plans | Allowed (OPI), LRS counted for ESPP remittances | [L3 1(ix)(f), 22(7)] |
| Irish UCITS ETFs | Allowed (regulated fund units) | [L3 1(ix)(e)] |
| IBKR shares awarded for a cash deposit (15.8392, vests Dec 2026) | **Grey**: listed equity, but acquired as a promotion, not bought with a remittance and not an employer plan; if a "gift" from a non-resident, Sch. III para 2(3) allows it only "in accordance with" FCRA 2010 [L5] | [question](../questions.md) C3 |
| Gold/commodity ETCs | **Grey / likely barred** ("commodities") | [L3 1(ix)(a)]; [question](../questions.md) C8 |
| Options, futures, margin, event contracts | Not allowed | [L1 Q2][L3 1(ix)(a)] |
| Unlisted/OTC bonds, CDs | Grey ("unlisted debt") | [L3 1(ix)(a)] |

## UK investment trusts and bond/T-bill ETFs
Question from `finance-scout`, 2026-11-15: (a) AVI Japan Opportunity Trust (AJOT), a UK
investment trust on the LSE; (b) foreign-listed ETFs incl. an Irish UCITS T-bill ETF (IB01). All
texts read 2026-11-15; options and derivatives: [derivatives-abroad.md](derivatives-abroad.md).

| Rule | Text (short) | Para | Source |
|---|---|---|---|
| OPI meaning | "investment, other than ODI, in foreign securities, but not in any unlisted debt instruments or any security issued by a person resident in India who is not in an IFSC" | OI Rules r.2(1)(s) | [L5] 22 Aug 2022 |
| Foreign security | "any security, in the form of shares, stocks, bonds, debentures or any other instrument denominated or expressed in foreign currency" | FEMA s.2(o) | [D1] 1999 text |
| Debt instruments | Government bonds; corporate bonds; non-equity securitisation tranches; loans; DRs on debt. Fund or ETF units are not in this list | OI Rules r.5(A) | [L5] |
| Individuals | "OPI, including by way of reinvestment", within LRS; Schedule III has no list of instruments and no "regulated" condition | OI Rules Sch. III para 1(1), 1(2)(ii) | [L5] |
| Funds | "units or any other instrument (by whatever name called) issued by an investment fund overseas, duly regulated by the regulator for the financial sector in the host jurisdiction, shall be treated as OPI"; "duly regulated" includes funds regulated "through a fund manager"; resident individuals may invest | MD Overseas Investment Part I para 1(ix)(e) (substituted 7 Jun 2024) | [L3a] updated 1 Apr 2026 |
| Bars | No OPI in unlisted debt, Indian-resident issuers, derivatives (unless RBI permits), commodities | OI Directions para 1(ix)(a) | [L3] |
| Listed | Listed on "a recognised stock exchange outside India" | OI Directions para 1(x) | [L3] |
| LRS | Individuals may do ODI and OPI "in accordance with" the OI Rules/Regulations/Directions | LRS MD para 6 | [L2] 6 Sep 2024 |

| Holding | Finding (our reading) |
|---|---|
| (a) AJOT, UK investment trust | **Allowed as OPI.** It is a UK public limited company ("AVI Japan Opportunity Trust plc", registered in England, "investment company under Section 833 of the Companies Act 2006", shares traded on the LSE) [W1]. Buying its listed shares (well under 10%, no control) is OPI in listed equity of a foreign entity [L5 r.2(1)(s)][L3 1(x)]. Being a fund in substance does not matter: the "regulated fund" test of para 1(ix)(e) is for fund **units**; listed shares need no such test. Its own gearing is the company's borrowing, not the user's margin |
| (b) Foreign-listed equity ETFs | **Allowed** (fund units [L3 1(ix)(e)], listed) |
| (b) Irish UCITS bond/T-bill ETF (IB01) | **Allowed as OPI**, as we read it: a fund unit, not a "debt instrument" (r.5(A) lists bonds, not fund units), and listed in any case, while only **unlisted** debt is barred [L5 r.2(1)(s)][L3 1(ix)(a),(e)]. UCITS are authorised by the Irish regulator (Central Bank of Ireland; not checked on its register). Indian tax: a debt fund may fall in AF s.76 (always short-term): [tax/global-actions-2026-11.md](../../tax/global-actions-2026-11.md) N3 (`finance-tax`) |
| Direct US T-bills / Treasuries | Grey: government bonds are debt instruments [L5 r.5(A)]; usually not exchange-listed, so they may be "unlisted debt" [L3 1(ix)(a)]. Matches the grey point in [research/themes/ibkr-global/cash-and-bonds.md](../../research/themes/ibkr-global/cash-and-bonds.md) (3.3) |

Questions C20-C22 in [questions](../questions.md).

## 180-day rule, reinvestment and dividends
**Plain answer:** money from selling foreign shares (employer ESPP/RSU or LRS-bought) and dividends may stay abroad only if reinvested in permitted OPI (e.g. Irish UCITS ETFs, IB01); cash not reinvested must come to India within 180 days of each sale or dividend. The 90-day rule is for ODI only; no FEMA form is needed for selling, moving or reinvesting.

| Case | Rule (short text) | Para | Source | Answer (our reading) |
|---|---|---|---|---|
| Duty to bring money home | Resident must "realise and repatriate to India" foreign exchange due "within such period ... as may be specified by the Reserve Bank" | FEMA s.8; FEMA 9(R) reg 3 | [D1]; [L8] 2015 text | Base rule for all sale proceeds and dividends |
| Period for individuals | Surrender "received/realised/unspent/unused foreign exchange ... within a period of 180 days from the date of such receipt/realisation" (reg 5-6: 7/60/90 days are for non-individuals) | FEMA 9(R) reg 7 | [L8] | 180 days from each receipt |
| LRS investments | "can retain, reinvest the income earned on the investments. The received/realised/unspent/unused foreign exchange, unless reinvested, shall be repatriated ... within a period of 180 days" | LRS MD para 17; FAQ Q4 | [L2] 6 Sep 2024; [L1] 6 Apr 2023 | (1)(b): LRS-bought shares: reinvest or bring home in 180 days |
| ESPP bought by payroll | ESOP remittances "shall be reckoned towards the LRS limit" | MD para 22(7) | [L3a] 1 Apr 2026 | (1)(a): ESPP is an LRS investment, so para 17 applies directly |
| RSU (no remittance) | Shares are OPI (MD para 1(ix)(f)); individuals may hold "OPI, including by way of reinvestment"; "Reinvestment" = OPI proceeds "exempted from repatriation provisions as long as such proceeds are reinvested within the time specified" in FEMA 9(R) | Sch. III para 1(2)(ii); MD para 1(ix)(c) (written for listed companies) | [L5]; [L3a] | (1)(a): same 180 days with reinvestment; no text written for RSU proceeds (C29) |
| ODI only: 90 days | "A person resident in India having ODI" shall repatriate dues and sale proceeds "within ninety days" | OI Regulations reg 9(4) | [L4] | Not for these shares (OPI, under 10%, no control) |
| Currency | Dues and "sale/winding up proceeds are required to be repatriated to India in freely convertible currencies only" | MD para 11 | [L3a] | When brought home: in USD, not another route |
| (2) Reinvest at IBKR | Irish UCITS ETFs are permitted OPI | MD para 1(ix)(e) | [L3a] | Buying them within 180 days = reinvested; the clock stops for that money |
| (2) Wire Fidelity -> IBKR | No rule names a broker-to-broker transfer | - | - | Not reinvestment and no new clock: the money keeps the date of the sale (C30) |
| (3) Cash at a broker | Individuals may hold foreign currency accounts "with a bank outside India for making remittances under" LRS | FEMA 10(R) reg 5(E)(4) | [L9] 21 Jan 2016 text | Broker cash is not a bank account; holding it short-term between buys is common practice, not written (C31) |
| (3) Each sale, each dividend | "from the date of such receipt/realisation" | FEMA 9(R) reg 7 | [L8] | Each sale or dividend starts its own 180 days for that money; dividends are treated the same unless reinvested |
| Exemptions | Act s.9 exempts limits "as the Reserve Bank may specify" (foreign currency accounts, "employment ... or any other legitimate means") | FEMA s.9(b),(e) | [D1] 1999 text | No RBI limit found that covers ESOP/RSU sale money (not verified) |
| (4) Reporting | OPI by resident individuals: no Form OPI (employer reports ESOP); LRS reporting only on remittances from India | OI Regulations reg 10(3); MD para 17(4) | [L4][L3a] | No FEMA filing to sell, move or reinvest; keep FIRA/bank advice when money comes home. Tax side: [Schedule FA](schedule-fa.md#the-rules) |

| Cash now | Status |
|---|---|
| IBKR $795 | Age and origin unknown (cash deposit Dec 2025? NXPI proceeds 9 Jul 2026 $3,800.32 were reinvested in AVGO/VRT by 14 Jul). If older than 180 days and not reinvested -> repatriate or invest ([question](../questions.md) C4) |
| Alpaca wallet $4,574 (sales 5-9 Nov 2026) | Withdrawal planned before 31 Dec 2026: within 180 days |
| Planned QCOM/MSFT/ESPP sale money | Buy in weekly parts as planned; any dollars still cash 180 days after their sale -> IB01 (permitted OPI) or bring home |

Compared with other notes: [tax/global-actions-2026-11.md](../../tax/global-actions-2026-11.md) N1 says the same (reinvest within 180 days, no new remittance); this adds that ESPP counts as LRS (para 22(7)) and that the 90-day rule does not apply. [tax/FY2026-27/payments-and-refunds.md](../../tax/FY2026-27/payments-and-refunds.md) section 4 says "No RBI text covers RSU/ESPP sale money": partly outdated (ESPP: para 22(7); RSU: Sch. III reinvestment, still no explicit text). [portfolio/plan.md](../../portfolio/plan.md) keeps a 5% "US dollar cash at IBKR, or IB01" buffer: as cash it must be reinvested or brought home within 180 days (the plan itself says so).

## Gifts and inheritance of foreign securities
- Acquiring foreign securities by inheritance or gift under OI Rules Schedule III para 2 does not
  count toward LRS and needs no LRS reporting [L3 para 17(4)].
- Investment by gift or inheritance is classed as OPI or ODI by its nature [L3 para 22(2)].
- A resident individual may not gift an overseas investment to a person resident outside India
  [L3 para 22(4)].
- Schedule III para 2 [L5]: inheritance without limit from a resident (holding lawfully) or from a
  non-resident; gift without limit from a resident relative; gift from a non-resident only under
  FCRA 2010. Heirs' steps: [FEMA for heirs](../estate/foreign-assets.md#fema-foreign-shares-inherited-by-indian-residents).

## Reporting and LRS use per FY
- Form OPI is filed by persons "other than a resident individual"; for ESOP/Employee Benefit
  Scheme OPI the employer's Indian office/subsidiary reports [L4 reg 10(3)][L3 para 22(5)].
  APR applies only to ODI [L4 reg 10(4)]. So the user files no FEMA return for these holdings;
  the bank reports each LRS remittance from Form A2 [L1 Q6][L3 para 17(4)].
- Late reporting is fixed with a late submission fee through the AD bank [L3 para 18].

LRS use per FY (no remittance data in the repository; amounts to come from the user's bank):

| FY | Known outflows | LRS used | TCS (26AS) |
|---|---|---|---|
| 2018-19 | NXP ESPP purchase 2019-02-28 (payroll) | unknown | not applicable before 1 Oct 2020 (not verified) |
| 2019-20 to 2023-24 | Qualcomm ESPP payroll purchases | unknown | unknown |
| 2024-25 | Qualcomm ESPP to May 2024 (not verified); Microsoft ESPP 2024-12-31; INDmoney funding from Aug 2024 | unknown | unknown |
| 2025-26 | Microsoft ESPP (Mar, Jun, Sep, Dec 2025, not verified); INDmoney funding; IBKR cash deposit Dec 2025 | unknown | unknown |
| 2026-27 | Microsoft ESPP; any IBKR/INDmoney deposits | unknown | unknown |

Needed from user: bank LRS statements / Form A2 copies per FY (all banks), INDmoney add-money
history, IBKR deposit history (Activity Statement "Deposits & Withdrawals"), Microsoft payslips
already in Drive show ESPP deductions (`Salary/Microsoft/`).

## TCS on LRS
- TCS on LRS remittances above Rs 10 L in a FY: 20% for purposes other than education/medical;
  Finance Act 2026 cut only education/medical to 2% (Income-tax Act 2025 s.394, earlier
  s.206C(1G)) [B2]. Credited against tax; check Form 26AS/AIS (`tax/new-investments.md` s3).
- Whether the bank collects TCS on an employer's ESPP remittance made for the employee: not
  verified ([question](../questions.md) C2).
