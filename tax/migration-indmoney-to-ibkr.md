# Tax plan: moving US shares from INDmoney (Alpaca) to IBKR

## Summary

- Moving the US shares from INDmoney to IBKR (ACATS) is not a sale: no tax; cost and buy dates carry over.
- 16-25 Nov 2026: sell SCLX, IONQ and the fractions except SHLS (orders placed for 16 Nov); SMNR and SYRS are untradeable: decided to move them to IBKR by ACATS (ask IBKR first) and sell there later; the loss counts in the year of that sale (section 3.5). With QCOM sale 1 in 2026-27 (the plan, `portfolio/plan.md`) every rupee of loss saves 14.95% this year: SCLX + IONQ (about -Rs 35,209) save about Rs 5,264, no carry-forward; if QCOM sale 1 slips past 31 Mar 2027, it carries forward instead ([loss-harvesting.md](loss-harvesting.md)).
- SHLS: the Array (ARRY) merger is a taxable exchange in India (not in the US). Do not sell before Mon 30 Nov (35.88% vs 14.95%); if you do not want ARRY, sell on or after 30 Nov.
- Withdraw the leftover cash to India (keep the FIRC). Start the ACATS on 1-4 Dec (user decision 18 Nov, so COGT/IMUX at INDmoney are not frozen around the 30 Nov FDA date) and finish before 31 Dec 2026, so Alpaca appears only in the CY2026 Schedule FA.
- Pay advance tax on any gains by 15 Dec 2026 / 15 Mar 2027.

Prepared 15 Nov 2026 by `finance-tax`. PLAN ONLY: no orders, no emails. The user decides and
trades; former "CA to confirm" points are answered in `ca-questions.md`.
Note: the `finance-tax` role now covers the tax effect of every buy and sell decision
(`roles/finance-tax.md`).

Sources (cited below by short name):
- [rules]: Indian rules note of mid-Nov 2026. Old law = Income-tax Act 1961; new law =
  Income-tax Act 2025, in force from 1 Apr 2026. Tax year 2026-27 = 1 Apr 2026 - 31 Mar 2027.
- [numbers]: FIFO lot work of 15 Nov 2026, using the INDmoney trade file to 8 Nov 2026, the GEV
  sale mail of 9 Nov 2026, Alpaca statements to Oct 2026, IBKR files to 6 Nov 2026, ITR JSONs
  and AngelOne files to 7-8 Nov 2026.
- Prices: yfinance closes of 13 Nov 2026.
- INR "approx": yfinance USDINR for the last day of the month before the trade. This is not the
  SBI TT buying rate, so expect about 0.5% error.
- [migration]: `portfolio/migration-indmoney-to-ibkr.md` (status of 15 Nov 2026).

Surcharge note (added 15 Nov 2026): the employer-stock work (`empstock.md`, work folder
`finance-tax-migration`) puts 2026-27 income at about Rs 1.06 Cr before capital gains, so a 15%
surcharge applies (capped at 15% on s.112/111A/112A gains; 2025 s.197/196/198). Effective rates
incl. 4% cess: LT 12.5% -> 14.95%; s.111A 20% -> 23.92%; ST at slab -> 35.88%. Figures below
were first worked at 13% (12.5% + cess) and are now shown at 14.95% (x 1.15).

## 0. Short answer

1. The ACATS move itself is not a sale: no tax, and the original cost and buy dates carry over.
2. The only taxable events are the forced fraction sales (gain about +$49 / +Rs 6,448 if sold at
   13 Nov prices) and any loss sales you choose to make.
3. Before the move, sell the INDmoney positions that are losses in rupees: SCLX, SMNR, IONQ,
   and SYRS if a buyer exists. Together they give about -Rs 51,800 to -Rs 70,100 of short-term
   loss. SMNR and SYRS turned out untradeable (15 Nov): SCLX + IONQ give about -Rs 35,209
   (section 3.5).
4. With QCOM sale 1 in 2026-27 (the plan; LTCG about Rs 24.4 L, `employer-stock/staged-sale.md`),
   all 2026-27 losses are set off this year against the NXPI and QCOM gains; nothing carries
   forward. SCLX + IONQ (about -Rs 35,209) save about Rs 5,264 (14.95%); the fraction gains
   (about +Rs 7,155) cost about Rs 1,070. If QCOM sale 1 is postponed past 31 Mar 2027, the silver
   sales alone use up the NXPI gain and the INDmoney loss carries forward instead (about
   Rs 27,300-47,000, only if the ITR is filed by 31 Jul 2027). Sell anyway: the loss is real and
   these lots may not move to IBKR.
5. Do not sell NVDA or the GOOGL 21-Nov-2025 lot for "losses": they are gains in rupees.
6. There is no reason to wait for SHLS/SYRS to turn long-term (30 Nov 2026) unless you plan to
   sell SHLS. Sell SYRS by 27 Nov while it is still short-term, if any buyer exists (not at
   INDmoney: suspended, section 3.5).
   SHLS is being bought by Array for shares (section 8A). In India that exchange is a taxable
   sale even though it is tax-free in the US. Do not sell SHLS before 30 Nov. If you do not want
   ARRY, sell SHLS on or after 30 Nov (long-term, 14.95%).
7. Withdraw the leftover cash to India rather than buying SGOV/GOVT, unless the amount is large.
8. Aim to finish the move before 31 Dec 2026, so that the Alpaca account appears only in the
   CY2026 Schedule FA.

## 1. Is the ACATS transfer taxable?

No.
- Only a "transfer" (sale, exchange, giving up or ending of rights) creates capital gains
  (1961 s.2(47); 2025 s.2(109)).
- Moving shares between custodians in your own name has no buyer, no price and no change of
  beneficial owner.
- The Act treats the beneficial owner, not the custodian, as the owner (1961 s.45(2A);
  2025 s.67(7)-(8)).
- Vania Silk Mills (SC 1991): a transfer needs the asset to pass to another person.
- The holding period runs from the original purchase date; nothing in 1961 s.2(42A) /
  2025 s.2(101) restarts it.

Likely (`ca-questions.md`): there is no CBDT circular on foreign broker-to-broker moves. The view rests on
general principle and on the treatment of off-market demat moves between your own accounts
[rules s.1].

US side: a nonresident alien pays no US tax on gains from US shares unless present in the US
183+ days (IRC s.871(a)(2)) [rules s.3].

## 2. Forced fraction sales

Only whole shares move; fractions "may be liquidated" by Alpaca [migration, mail 9 Nov 2026].

Rates:
- US shares held more than 24 months are long-term: LTCG at 12.5%, no indexation, no Rs 1.25
  lakh exemption (1961 s.2(42A), s.112; 2025 s.2(101), s.197).
- Shares held 24 months or less are short-term: taxed at your slab rate (s.111A / 2025 s.196
  needs STT, so it does not apply).
- Add surcharge (capped at 15% on these gains) and 4% cess [rules s.2].

Fractions sold FIFO from the oldest open lot, at 13 Nov 2026 closes [numbers A.4]. All are
short-term today.

| Symbol | Fraction | From lot | Gain USD | Gain INR approx |
|---|---|---|---|---|
| CRWD | 0.490700 | 2025-10-27 | +46.07 | +4,803 |
| CEG | 0.286771 | 2026-07-01 | +13.65 | +1,323 |
| TRVI | 0.679044 | 2025-06-20 | +5.18 | +533 |
| GOOGL | 0.160599 | 2025-11-21 | -0.59 | +257 |
| NVDA | 0.494930 | 2025-07-30 | -7.21 | +166 |
| SHLS | 0.210155 | 2024-11-27 | +0.64 | +73 (LT from 30 Nov 2026) |
| IONQ | 0.239410 | 2025-08-01 | -2.10 | -133 |
| SMNR | 0.428571 | 2026-06-16 | -2.35 | -226 |
| SCLX | 0.428571 | 2025-07-25 | -4.15 | -349 |
| SYRS | 0 | - | - | - |
| Total | | | +49.14 (proceeds ~$338) | +6,448 |

How to keep this small:
- Sell the fractions yourself, with limit orders, before the transfer. A forced liquidation
  gives you no control over the price or the date.
- Sell them before 31 Mar 2027, so that they fall in the same tax year as the loss sales of
  section 3 and the losses absorb the gains.
- If you sell the whole SCLX, SMNR and IONQ positions (section 3), their fractions go with them.
- FIFO: Indian practice and INDmoney's own tax report match sales FIFO. FIFO is the law only
  for demat holdings (1961 s.45(2A); 2025 s.67(7)(c)). Keep FIFO for consistency.
  The CRWD fraction from the newer 2026-07-15 lot would show a smaller gain, but INDmoney
  cannot pick lots.
- The tax is small in any case: Rs 6,448 at 35.88% (30% slab + 15% surcharge + cess) is about Rs 2,300 at worst, before
  any set-off.

## 3. Loss harvesting

### 3.1 Position so far in tax year 2026-27 (to 15 Nov 2026) [numbers B]

| Broker | Short-term | Long-term |
|---|---|---|
| INDmoney (12 sales incl. GEV 9 Nov) | -$2,751.97 net, approx -Rs 2,16,582 | 0 |
| IBKR (NXPI 9 Jul 2026, cost = FMV $91.32) | 0 | +$2,622.72, approx +Rs 2,76,457 |
| AngelOne | 0 | 0 |
| Brought forward from earlier years | 0 | 0 |
| Net after set-off | | approx +Rs 59,875 LTCG at 12.5% |

Brought-forward losses are nil: the revised ITR for AY2026-27 (8 Nov 2026) set off the Rs 2,394
LTCL and carried nothing forward [numbers D.1].

INDmoney's own FY2026-27 tax report shows -Rs 1,31,066: it leaves out the FLNA sale of 5 Nov
and the GEV sale of 9 Nov (section 12).

### 3.2 Set-off rules [rules s.3]

- Short-term loss offsets any capital gain; long-term loss offsets only long-term gain
  (1961 s.70; 2025 s.108(2)).
- No capital loss offsets salary (1961 s.71(3); 2025 s.109(2)).
- Unused loss carries forward 8 years, only if the ITR is filed by the due date (31 July for
  non-audit cases): 1961 s.74, s.80 with s.139(1); 2025 s.111, s.121 with s.263(1).
- India has no wash-sale rule; you may sell and buy back.
  - Dividend/bonus stripping (1961 s.94(7)/(8); 2025 s.175(8)/(9)) does not apply.
  - GAAR (Chapter X-A; 2025 s.178-179) needs a tax benefit above Rs 3 crore.
  - A buy-back at market is a genuine transaction (Azadi Bachao 2003, Vodafone 2012).
- US: no US capital gains tax for a nonresident alien, so the US wash-sale rule (IRC s.1091)
  does not matter.

### 3.3 Candidates (prices of 13 Nov 2026) [numbers E]

| Lot | USD | INR approx | Notes |
|---|---|---|---|
| SCLX 31.43 sh (2025-07-25, 2025-08-04) | -327.60 | -27,863 | On full trade cost. On the broker's split cost: about -$140.80. |
| SYRS 800 sh (2024-11-27) | -217.76 | -18,310 | Price $0.0001; there may be no buyer. Short-term until 27 Nov 2026, long-term from 30 Nov. |
| SMNR 31.43 sh (2026-06-16) | -172.23 | -16,555 | On broker cost $187. If cost = FMV on receipt: only -$14 to -$80 (section 8). |
| IONQ 13.24 sh (2025-08-01) | -116.18 | -7,346 | |
| GOOGL 6.24 sh (2025-11-26) | -164.31 | -2,533 | Small in INR. |
| NVDA all lots (2025-07-30) | -108.58 | +2,557 | Gain in INR (rupee fell from ~85.7-88.2 to ~95.15). Do not sell for a loss. |
| GOOGL 2.92 sh (2025-11-21) | -10.76 | +4,675 | Gain in INR. Do not sell for a loss. |
| IBKR AVGO 10 (2026-07-14) | -446.80 | -41,097 | Alternative |
| IBKR VRT 3 (2026-07-09) | -380.20 | -35,820 | Alternative |
| AngelOne ICICI Pru Silver ETF (2025-12-26, 2026-01-21 lots) | | -47,538 | Alternative; short-term until 27 Dec 2026 / 22 Jan 2027 |
| AngelOne other metals (ABSL Silver lots, ICICI Silver FoF, Motilal Gold+Silver FoF) | | -17,071 / -15,123 / -5,741 | Alternative |

### 3.4 Recommendation

1. Sell at INDmoney, before the transfer: SCLX, SMNR, SYRS (by 27 Nov, if a buyer exists) and
   IONQ (all whole shares and fractions).
   - These are the lots IBKR may not accept (SYRS, SMNR, SCLX - not yet confirmed
     [migration]).
   - They would also arrive at IBKR with doubtful cost data.
   - Loss: about -Rs 52,000 to -Rs 70,000 (less if SMNR cost = FMV, as in section 8).
   - Update 15 Nov: SMNR and SYRS cannot be sold at INDmoney; see section 3.5.
2. GOOGL 2025-11-26 lot: optional, only -Rs 2,533. INDmoney cannot sell a chosen lot: a sale of
   6.24 sh is matched FIFO against the 2025-11-21 lot first (an INR gain). Not worth it; move
   GOOGL whole.
3. Effect: the remaining LTCG is about Rs 59,875 + Rs 6,448 (fractions) = about Rs 66,300.
   - Loss: Rs 51,800 - 70,100 (SCLX 27,863 + SMNR 16,555 + IONQ 7,346, + SYRS 18,310).
   - With QCOM sale 1 in 2026-27 (the plan): the silver loss (about -Rs 78,094,
     `angelone-metals-and-mf-exits.md`) and the INDmoney loss both offset this year's NXPI and QCOM
     gains at 14.95%. SCLX + IONQ (-Rs 35,209) save about Rs 5,264; no carry-forward.
   - If QCOM sale 1 slips past 31 Mar 2027: the silver sales use up the Rs 66,323 and the
     INDmoney loss carries forward 8 years (about Rs 27,300-47,000 without SMNR/SYRS), only if the
     ITR is filed by 31 Jul 2027. See [loss-harvesting.md](loss-harvesting.md) section 6.
4. Buying back: allowed, but a buy-back restarts the 24-month clock. Example: IONQ would turn
   long-term on 2 Aug 2027 if kept, but only 24 months after the new purchase if sold and bought
   back. Buy back only names you would buy anyway, at IBKR after the move. Note the AGENTS.md
   rule "Excluded: stocks under $5": it rules out buying back SCLX, SMNR and SYRS.
5. IBKR loss lots (AVGO, VRT): with QCOM sale 1 they would also save 14.95% this year; selling
   them is an investment choice (and restarts the clock if rebought), not needed for tax.
   - The planned MF exits [numbers E.4] give LTCG of Rs 13,366, which is inside the Rs 1.25
     lakh s.112A exemption.
   - Do not spend short-term loss on exempt gain; set it against the NXPI gain first
     [rules s.10]. No fixed order in the Act; you fill the set-off table (likely).

### 3.5 Untradeable SMNR/SYRS and the last fractions

Orders placed 15 Nov 2026 for the 16 Nov US open (day orders, limit; finance-main):
SCLX all 31.4286 @ $1.43, IONQ all 13.2394 @ $28.88, fractions CRWD 0.4907 @ $226.61,
CEG 0.2868 @ $280.20, TRVI 0.679 @ $13.65. SMNR and SYRS cannot be sold at INDmoney ("Trading
is not allowed on this stock / suspended by the exchange"). GOOGL and NVDA fractions not yet
placed. Actual losses come from the contract notes; figures here are at 13 Nov prices.

SMNR and SYRS: no loss until there is a transfer (AF s.2(109), ex 1961 s.2(47): a sale, or the
extinguishment of the rights). A suspension, deregistration or a price near zero is not a
transfer [`global-actions-2026-11.md` row 18].

| Option | Tax effect | Catch |
|---|---|---|
| (a) Include them in the ACATS to IBKR, then sell there (OTC/grey market) at any nominal price | The sale books the loss in the year of sale | IBKR often rejects suspended or non-transferable securities: ask IBKR first (step 1 of section 10) |
| (b) Leave them at Alpaca | No loss until sold or extinguished | The Alpaca account cannot be closed: Schedule FA A2/A3 rows continue for CY2027 and later |
| (c) Wait for extinguishment (liquidation, cancellation). SYRS filed Form 15 (deregistered) on 2025-03-20 [`research/themes/holdings-events-2026-11.md`] | Loss in the year the rights are extinguished | Needs evidence (company or broker notice of cancellation) |
| (d) Ask INDmoney/Alpaca whether they buy worthless positions (some US brokers pay $0.01) | That is a sale: loss in the year of sale | Get a trade confirmation |
| Abandon or write off with no consideration | Disputed: no transfer without an asset passing (SC, Vania Silk Mills 1991) vs extinguishment rulings | CA |

Decision 2026-11-15 (user, via finance-main): option (a).
- Ask IBKR before starting the ACATS whether it accepts SMNR and SYRS (suspended); if yes, include
  them in the transfer and sell at IBKR later at a nominal price.
- Tax effect: the loss is booked in the tax year of the IBKR sale. Sold by 31 Mar 2027: it counts in
  2026-27 (SMNR short-term; SYRS long-term from 30 Nov 2026, so an LT loss that offsets only LT
  gains): with QCOM sale 1 in 2026-27 both save 14.95% this year (SMNR about Rs 2,475, SYRS about
  Rs 2,737); otherwise they add to the carry-forward. Sold later: it falls in that year, with 8 years from then.
- If IBKR refuses them: fallback (b) leave them at Alpaca and/or (d) ask INDmoney/Alpaca to buy
  them for a nominal price. Under (b) the Alpaca account stays open and Schedule FA A2/A3 rows
  continue for CY2027 (tax year 2027-28) and later.

| Lot | Loss | If realised after 31 Mar 2027 |
|---|---|---|
| SYRS 800 sh (2024-11-27, cost $217.84) | -$217.76, about -Rs 18,310 | Long-term from 30 Nov 2026: an LT loss offsets only LT gains |
| SMNR 31.43 sh (2026-06-16) | Broker cost $187: about -Rs 16,555; FMV cost (dividend view, section 8): -$14 to -$80 | Short-term until 17 Jun 2028 |

- The INDmoney loss sold now is SCLX + IONQ, about -Rs 35,209 (SCLX on full cost; less on the
  broker's split cost, -$140.80). With QCOM sale 1 in 2026-27 (the plan) it saves about Rs 5,264
  this year and nothing carries forward. Only if QCOM sale 1 slips past 31 Mar 2027: the 2026-27
  carry-forward is about Rs 27,300 (with the 7 MF exits) to Rs 47,000 (without), SMNR/SYRS
  excluded unless realised by 31 Mar 2027.
- They can still be booked in the later year they are sold or extinguished; the 8-year
  carry-forward runs from that year.
- The SMNR receipt itself may be dividend income in 2026-27 (section 8): unchanged.

GOOGL and NVDA fractions (about +Rs 257 and +Rs 166, section 2): the tax is the same whether you
sell them or Alpaca liquidates them in the transfer - short-term at slab (35.88%) on a tiny INR
gain, in 2026-27 if the transfer completes before 31 Mar 2027. Selling yourself gives price
control and a dated contract note; liquidation comes at an unknown price and date. Recommend:
sell both with limit orders in the same 16-25 Nov window.

## 4. Leftover cash

The wallet balance is unknown: no file shows it [numbers F]. Cash cannot move by ACATS
[migration].

| | Withdraw USD to an Indian bank | Buy whole SGOV/GOVT and move them |
|---|---|---|
| Indian income tax | None: your own capital coming back. Keep the bank FIRC and the broker statement. | Distributions are dividends, taxed at slab (1961 s.56(2)(i); 2025 s.92(2)(a)). |
| US tax | None | 25% withholding under DTAA Art.10(2)(b) with W-8BEN (30% without it). "Interest-related dividends" (IRC s.871(k)) may be exempt or refunded via 1042-S. |
| Foreign tax credit | - | Allowed under 1961 s.90 / 2025 s.159, Rule 128 / Rules 2026 r.76, limited to the Indian tax. Needs Form 67 (old law: by the end of the AY), now Form 44 (r.76(10),(12)): within 12 months of the end of the tax year, so by 31 Mar 2028 for 2026-27, with the ITR filed on time. |
| Capital gains on exit | - | Unclear whether a US debt ETF is a "specified mutual fund" (1961 s.50AA; 2025 s.76(5)(b)). Likely it is ("by whatever name called"): every gain short-term at slab (`ca-questions.md`). |
| Schedule FA / FSI / TR | Only the account balance | Extra A3 rows, plus FSI and TR entries |
| Other | Outward TCS (s.206C(1G) / 2025 s.394) applies only if you later send money abroad again; check with the bank about the LRS 180-day rule. | US estate tax: only a $60,000 exemption for nonresident aliens on US assets, whatever the broker. |

Recommendation: withdraw the cash to India after the fraction and loss sales settle (T+1).
- Leave nothing at Alpaca.
- Keep at least USD 25 free in IBKR for the transfer debit [migration].
- Buy SGOV/GOVT only if the cash is large and you want to keep it in USD at IBKR anyway.

## 5. Schedule FA for calendar year 2026 (ITR for tax year 2026-27)

Period: 1 Jan - 31 Dec 2026 [rules s.5]. The ITR forms under the 2025 Act are not yet notified;
check their instructions when they come out.

Table A2 (custodial accounts): one row per account and nature of amount (D = dividend,
S = sale proceeds), the same style as the revised AY2026-27 return [numbers D.3].

| Account | What to show for CY2026 |
|---|---|
| Alpaca ending 2423 | Held until the "Omnisub Account Migration" of 5 May 2026. Peak 1 Jan - 5 May; closing 0; dividends and any sale proceeds up to 5 May (check the Jan-Apr statements). |
| Alpaca ending 1593 | From 5 May 2026. Peak, closing (0 if the move is done and the cash withdrawn by 31 Dec), dividends, and gross sale proceeds of 2026 sales (LLY, SNPS, META, the 5 Nov sales, GEV, fractions, harvest sales). Not the shares moved out. |
| IBKR ending 4563 | Peak, closing at 31 Dec, dividends, and proceeds (NXPI 9 Jul 2026 $3,800.32). |
| Fidelity ending 4972; E*Trade ending 7855/8803 | As for other foreign accounts. E*Trade closed at 0 in CY2025; include it only if the account still existed at any time in 2026 (A2 covers accounts held at any time in the year; likely). |

Table A3 (each holding):
- Initial value = the original cost; date of acquiring = the original buy date (the same lot
  rows as the CY2025 return: one row per Alpaca lot, FIFO).
- Peak value in 2026, closing value at 31 Dec 2026, dividends, and sale proceeds only for lots
  actually sold.
- Moved shares: one row per lot (A3 has no account column, ITR-2 AY2026-27 schema), with the
  original date and cost, the peak for 2026 and the closing value at IBKR; likely
  (`ca-questions.md`). Two rows would count the peak value twice.
- SMNR: a new row dated 2026-06-16, with an initial value per section 8.

Exchange rates: SBI TT buying rate on the peak date (for peak values) and on 31 Dec (for closing
values) [rules s.5].

Do not copy INDmoney's draft CY2026 Schedule FA [numbers D.3]:
- It has fake 2026-05-06 "purchase" rows for SHLS, TRVI, LLY, IONQ and SYRS (these are the
  account-migration entries).
- It has no SMNR and no FLNA rows.
- It shows closing 0 everywhere.
- Its A2 Alpaca peak/closing figures (3,955 / 3,470) are not in INR.

Black Money Act 2015 (s.42, s.43): Rs 10 lakh penalty for a missing or wrong foreign-asset
disclosure. The Rs 20 lakh relief (from 1 Oct 2024) does not help here: the foreign assets are
far above it (IBKR closing Rs 1,20,24,250 in CY2025 [numbers D.3]).

Schedule FSI: US-source dividends and capital gains (NXPI, INDmoney sales). Schedule TR: the
US tax withheld on dividends, with Form 44 (Form 67 under the old rules).

## 6. Records to keep

Keep them permanently, or at least 6+ years after the final sale.
- Reassessment limit: 4 years 3 months, up to 6 years 3 months under 2025 s.282(1), the longer limit only if escaped income is Rs 50 L or more.
- Under the Black Money Act there is in effect no time limit (BMA s.4(3), s.72(c)) [rules s.6].
- The burden of proving cost and date is on you (1961 s.48/s.55; 2025 s.72/s.90).

| Record | Why |
|---|---|
| INDmoney trade file since inception, holdings report, Consolidated Tax Reports FY2025-26 / FY2026-27 | Lot cost and dates (IBKR may show wrong or no cost) |
| Alpaca monthly statements for 2423 and 1593, incl. May 2026 (account migration) and June 2026 (SMNR spin-off, SCLX cost change) | Account history, SMNR evidence |
| ACATS confirmations from Alpaca/INDmoney and IBKR; the IBKR statement showing the shares coming in | Proof that the move was not a sale |
| Sell mails for GEV, the fractions and the harvest sales | GEV is not in the trade file |
| Your own lot file (the FIFO table in [numbers] A.1), kept after the move | IBKR's cost basis can be wrong |
| Scilex distribution notice, record/pay dates, SMNR price on 16 Jun 2026, 1099/1042-S | Section 8 |
| SBI TT buying rates for every trade month, bank FIRC/FIRA for withdrawals | FX conversion |
| NXPI ESPP confirmation and the FY2018-19 Form 16/payslip with the perquisite | Section 7 |

## 7. NXPI (ESPP bought 28 Feb 2019 at $77.62; FMV $91.32)

- Cost for Indian tax = FMV $91.32 per share: the value already taxed as salary
  (1961 s.17(2)(vi) and s.49(2AA); 2025 s.17(1)(d) and s.73(1) Table Sl.4) [rules s.7].
- Use the INR value in the FY2018-19 Form 16 if available (not yet checked).
- Long-term since 1 Mar 2021: LTCG at 12.5% (1961 s.112; 2025 s.197).

| Sale | Tax year | Gain USD | INR approx | Source |
|---|---|---|---|---|
| E*Trade 0.575 sh, 9 Dec 2025 ($130.68 total) | 2025-26 | +78.17 | +7,944 | [numbers C.2] |
| IBKR 0.1165 sh, 11 Dec 2025 (forced, code L) | 2025-26 | +15.85 | +1,611 | [numbers C.2]; filed as LTCG Rs 9,206 in the revised ITR |
| IBKR 12.8835 sh, 9 Jul 2026 ($3,800.32) | 2026-27 | +2,622.72 | +2,76,457 | [numbers B.2] |

- IBKR shows cost $77.615 (P/L +$2,799.28). Ignore that for Indian tax; use $91.32.
- The E*Trade -> IBKR ACATS move (Dec 2025) was not a sale (section 1).
- Lesson: IBKR force-sold 0.1165 NXPI because the ACATS debit (-$16.49) left the account with
  negative cash. That is why USD cash must be in IBKR before this move.

## 8. SCLX -> SMNR stock distribution (16 Jun 2026)

What happened [numbers A.1]:
- Alpaca booked 31.428571 SMNR as a "Stock SpinOff" (1 SMNR per SCLX) at $5.95 = $187.00.
- It cut the SCLX cost from $372.54 to $185.74.
- SMNR traded at only $0.90-3.00 that day (yfinance), so it was worth about $28-94.

Indian treatment (likely; `ca-questions.md`) [rules s.9]:
- Not a demerger: that needs a Companies Act s.230-232 scheme (1961 s.2(19AA); 2025 s.2(35)).
  So no cost split and no holding-period tacking.
- Prevailing view: a dividend in kind, if Scilex had accumulated profits (1961 s.2(22)(a);
  2025 s.2(40)(a)).
  - FMV is taxed at slab (s.56(2)(i) / 2025 s.92(2)(a)).
  - SMNR cost = that FMV; holding from 16 Jun 2026; SCLX keeps its full $372.54 cost.
- Scilex has an accumulated deficit (-$921.8 M at 31 Dec 2025, 10-K filed 2026-04-10), so the dividend view fails. Then the fallbacks are:
  - a gift-type receipt over Rs 50,000 (s.56(2)(x); 2025 s.92(2)(m)) - not met at about
    Rs 2,700-8,900;
  - or a capital receipt with SMNR cost possibly nil.

INR effect if SCLX and SMNR are both sold (approx, 13 Nov prices):

| View | Income at slab | Capital loss |
|---|---|---|
| Broker split (cost $185.74 / $187) | 0 | SCLX -$140.80 + SMNR -$172.23 = -$313 |
| No income, SMNR cost nil (likely) | 0 | SCLX -$327.60 + SMNR about +$14 = about -$314 |
| Dividend at FMV (only with accumulated profits) | +$28 to +$94 (about Rs 2,700-8,900) | SCLX -$327.60 + SMNR -$14 to -$80 = -$342 to -$408 |

The dividend view adds a small slab-taxed income but a bigger capital loss: about the same net
result. Use the nil-cost view consistently in the ITR, Schedule FA (SMNR initial value nil) and lot file.

## 8A. SHLS - Array merger

What is known (`research/themes/holdings-events-2026-11.md`, lines 19 and 65):
- Shoals (SHLS) agreed a stock-for-stock merger with Array (ARRY): 1.6931 ARRY per SHLS share.
- Announced about 4-5 Nov 2026 (Rule 425 filing of 5 Nov 2026).
- Vote and closing dates are not verified.
- Your holding: 45.210155 SHLS, bought 27 Nov 2024 at $5.239 (cost $236.86), long-term from
  Mon 30 Nov 2026 [numbers A.1, A.3].

### Indian tax of the exchange (resident)

The exchange is taxable in India, even if it is tax-free in the US under IRC s.368.
- "Transfer" includes the "exchange" of an asset and the "extinguishment of any rights therein"
  (1961 s.2(47)(i)-(ii); 2025 s.2(109)(a)-(b)). Your SHLS shares end and ARRY shares replace
  them.
- CIT v. Mrs. Grace Collis (SC 2001, 248 ITR 323): the swap of shares in an amalgamation is a
  transfer; that is why the Act needs a specific exemption. Case cited from knowledge, not
  re-read; the Act check below supports it (likely).
- None of the exemptions fits a US-US merger. Checked in the 2025 Act text (as amended by
  Finance Act 2026, extraction of 10 Jun 2026; GitHub abaasairam-ai/income-tax-rag
  `docs-text/income-tax-act-2025.txt`):

| 1961 Act | 2025 Act | Covers | Applies to SHLS -> ARRY? |
|---|---|---|---|
| s.47(vii) | s.70(1)(f) | A shareholder swapping shares in an amalgamation, only if the amalgamated company is an Indian company | No: Array is a US company |
| s.47(viab) | s.70(1)(g) | Shares of an Indian company passed from one foreign company to another in an amalgamation | No: no Indian-company shares |
| s.47(viac) | s.70(1)(h) | Shares of a foreign company that get their value mainly from an Indian company (s.9(10)(a)) | No |

- The matching cost carry-over (2025 s.73(1) Table Sl.2) and holding-period tacking
  (2025 s.2(101)(c)(B)(II)) also apply only when the shares received are of an Indian
  amalgamated company. So neither carries over to ARRY.

How the gain is worked out:
- Sale value = the FMV of the ARRY shares on the closing date, plus any cash paid for a
  fraction of an ARRY share. Where the consideration is not money, its FMV on the date of
  transfer is the full value (1961 s.50D; 2025 s.80).
- Cost of SHLS = $236.86 (original cost). It is long-term if the close is on or after 30 Nov
  2026: 12.5% (1961 s.112; 2025 s.197), 14.95% with surcharge and cess.
- Cost of ARRY = the FMV on the closing date that was taxed as the sale value. The holding
  period of ARRY starts on the closing date, so a new 24-month clock starts.
  - There is no express section for this.
  - It follows the general rule that cost is what you gave up to acquire the asset (the
    principle behind 1961 s.48 / 2025 s.72).
  - Likely (`ca-questions.md`).
- FX: convert the sale value at the SBI TT buying rate for the last day of the month before the
  closing month (r.206) [rules s.2].

Other effects:
- Tax without cash: you owe Indian tax on the gain but receive only ARRY shares (plus a few
  dollars for the fraction). Pay the tax from other money by the next advance-tax date
  (15 Dec / 15 Mar; 2025 s.408, s.425(4)).
- Fraction: 45.210155 x 1.6931 = 76.545 ARRY. That is 76 shares plus about 0.545 paid in cash
  (about $2.64 at $4.84). Only 45 whole SHLS move to IBKR, so there it would be 76.19 ARRY.
- Schedule FA: in the calendar year of the close, SHLS shows closing 0 with the gross proceeds
  (the FMV of the ARRY received). ARRY appears as a new A3 row: acquired on the closing date,
  initial value = that FMV.
- Schedule FSI: it is a US-source capital gain.

### Numbers (yfinance closes of 13 Nov 2026: SHLS $8.29, ARRY $4.84; refreshed 15 Nov 2026)

- Deal value per SHLS = 1.6931 x $4.84 = $8.19, close to the $8.29 SHLS price.
- Gain on the whole 45.210155 SHLS at $8.29: +$137.94, approx +Rs 15,745 [numbers A.1].
- Tax on that gain:
  - Sold before 30 Nov (short-term, slab incl. surcharge and cess 35.88%): about Rs 5,650.
  - Sold, or exchanged in the merger, on or after 30 Nov (long-term, 14.95%): about Rs 2,350.
- The exchange gain is fixed by the ARRY price on the closing date, not today's price.
- If the gain falls in 2026-27, the loss sales of section 3 absorb it first, so the extra tax
  may be nil.

### Recommendation

1. Do not sell SHLS before Mon 30 Nov 2026: it is short-term until then (35.88% vs 14.95%).
2. After 30 Nov, selling SHLS and letting the merger exchange it give about the same Indian tax:
   both are long-term gains.
3. The merger also produces a cash fraction and restarts the 24-month clock on ARRY.
4. So if you do not want ARRY, selling SHLS after 30 Nov is cleaner. You can sell before the
   transfer at INDmoney (then do not move it) or later at IBKR.
5. Moving SHLS by ACATS is still not taxable.
6. If the merger closes while trading is frozen during the transfer, nothing changes for Indian
   tax: it is the same exchange, on the closing date.
7. Whether to keep ARRY is your investment choice, not a tax point.

## 9. Timing

Lots that move, with the date each turns long-term (held more than 24 months) [numbers A.1, A.3]:

| Symbol | Whole sh | Lot buy date (US) | Long-term from | Gain 13 Nov USD / INR approx |
|---|---|---|---|---|
| SHLS | 45 | 2024-11-27 | Mon 30 Nov 2026 | +137.94 / +15,745 |
| SYRS | 800 | 2024-11-27 | Mon 30 Nov 2026 | -217.76 / -18,310 (untradeable, section 3.5) |
| TRVI | 161 | 2025-06-20; 2025-07-23; 2025-07-25 | 21 Jun 2027; 24 Jul 2027; 26 Jul 2027 | +1,010.45 / +1,07,768 |
| SCLX | 31 | 2025-07-25; 2025-08-04 | 26 Jul 2027; 5 Aug 2027 | sell (section 3) |
| NVDA | 7 | 2025-07-30 | 31 Jul 2027 | -108.58 / +2,557 |
| IONQ | 13 | 2025-08-01 | 2 Aug 2027 | sell (section 3) |
| CRWD | 8 | 2025-10-27; 2026-07-15 | 28 Oct 2027; 16 Jul 2028 | +428.48 / +44,346 |
| GOOGL | 9 | 2025-11-21; 2025-11-26 | 22 Nov 2027; 27 Nov 2027 | -175.07 / +2,142 |
| SMNR | 31 | 2026-06-16 | 17 Jun 2028 (if receipt = acquisition) | untradeable (section 3.5) |
| CEG | 4 | 2026-07-01 | 2 Jul 2028 | +204.09 / +19,781 |

Note: the broker's "Holding Since" dates are first-ever buys, not the open lots. SCLX does NOT
turn long-term in Nov 2026.

What matters for timing:
- Long-term dates: the move is not a sale, so these dates do not force you to wait. Waiting for
  30 Nov helps only if you plan to sell SHLS soon (14.95% instead of 35.88%). The Array merger
  (section 8A) is also a taxable exchange: if it closes before 30 Nov the gain is short-term
  (unlikely, as the dates are not yet known). SYRS should be sold (if possible at all, section 3.5)
  BEFORE it turns long-term (by Fri 27 Nov; 26 Nov is Thanksgiving, 27 Nov a half day), so that
  its loss stays short-term and can offset any gain.
- Tax year end, 31 Mar 2027: losses booked by then count for 2026-27 (the silver sales cover
  the NXPI LTCG; with QCOM sale 1 in 2026-27 the INDmoney losses offset QCOM, otherwise they
  carry forward). Gains
  realised after it fall in 2027-28.
- Calendar year end, 31 Dec 2026: if the move and the cash withdrawal finish by 31 Dec, the
  Alpaca accounts close at 0 in the CY2026 FA. If it spills into Jan 2027, Alpaca 1593 must also
  be reported in the CY2027 FA (tax year 2027-28).
- Cost of waiting:
  - Trading is frozen during the move (about 1-2 weeks) [migration].
  - The fee ($125 or $25) does not depend on timing and is still unresolved.
  - FX does not matter for an in-kind move.
- Advance tax: 75% is due by 15 Dec 2026 and 100% by 15 Mar 2027 (1961 s.211; 2025 s.408).
  - Rs 1,50,000 was paid on 9 Nov 2026 [numbers D.2]; check it against the total.
  - Gains realised after an instalment date can be covered in later instalments without s.234C
    interest (2025 s.425(4)).

Recommended window:
- 16-25 Nov 2026: loss sales and fraction sales.
- 1-4 Dec 2026: start the ACATS (user decision 18 Nov), after the sales settle (T+1) and the cash is out; must finish by 31 Dec 2026.
- Target: complete by mid-Dec 2026, with slack before 31 Dec.

## 10. Recommended step order

1. Ask IBKR (secure message), before starting the ACATS, whether it accepts SYRS and SMNR
   (suspended; decision section 3.5: move them if accepted) and SCLX, and confirm the source
   account (ending 1593, not 2423) and the fee ($125 vs $25) [migration].
2. Refresh the INDmoney holdings and trade export, and get the wallet cash balance.
3. 16-25 Nov: with limit orders, sell all of SCLX and IONQ (placed for 16 Nov). SMNR and SYRS
   are untradeable: move them to IBKR if accepted (step 1, section 3.5). With QCOM sale 1 in 2026-27
   the loss saves 14.95% this year (about Rs 5,264); otherwise it carries forward (ITR by 31 Jul 2027).
4. Same days: sell the remaining fractions (CRWD, CEG, TRVI placed; GOOGL, NVDA still to place). SHLS fraction only on
   or after Mon 30 Nov (long-term from then; sections 8A, 9).
5. Save every sell mail and contract note. Note the GEV sale fee when it shows up.
6. After settlement (T+1), withdraw all USD cash to the Indian bank and keep the FIRC. Or buy
   whole SGOV/GOVT only if the cash is large (section 4).
7. Make sure IBKR holds at least USD 25 free cash and that a W-8BEN is on file at IBKR.
8. Start the incoming ACATS at IBKR (1-4 Dec). Move: GOOGL 9, CRWD 8, NVDA 7,
   TRVI 161, CEG 4, SHLS 45, plus SMNR 31 and SYRS 800 if IBKR accepts them (if not, fallback
   (b)/(d) in section 3.5).
8a. SHLS: if you do not want ARRY, sell it on or after Mon 30 Nov - either at INDmoney before
   the transfer starts (then leave it out of the transfer) or later at IBKR. Never before
   30 Nov. If you keep it, track the vote and closing dates and set aside the tax on the
   exchange gain (section 8A).
9. When the shares arrive, check that IBKR shows the original cost and dates. Keep your own lot
   file either way.
9a. Sell SMNR and SYRS at IBKR at a nominal price (limit order, keep the confirmation); by
   31 Mar 2027 if the loss is wanted in 2026-27 (section 3.5).
10. Before 15 Dec: recompute the 2026-27 tax and pay the advance tax due.
11. In Jan 2027: collect the Dec statements from Alpaca and IBKR and the ACATS confirmations,
    and build the CY2026 Schedule FA (section 5).

## 11. Questions for the user (former CA points answered in `ca-questions.md`)

1. Your slab rate (it decides how much short-term gains and the SMNR "dividend" cost).
2. SMNR/SCLX treatment, and whether Scilex had accumulated profits (section 8).
3. Whether ACATS is "not a transfer" (principle only) and how to show moved shares in A3:
   two rows or one (section 5).
4. Whether SGOV/GOVT is a "specified mutual fund" under s.50AA / 2025 s.76.
5. FX method: cost converted at the rate of the month before purchase (practice, not express
   text); NXPI INR cost from the Form 16.
6. The order of set-off between gains at different rates (STCL against NXPI LTCG rather than
   exempt s.112A gains).
7. Whether the CY2025 A2 row for Alpaca (number 1593, opened 2024-06-10) should have been
   2423, and whether a fix is needed.
8. Wallet cash amount, and whether you want to keep USD abroad (decides section 4).
9. Whether you want to keep IONQ/SCLX exposure; buying back restarts the holding period.
10. Surcharge and rates: checked in the Finance Bill 2026 memo (`ca-questions.md`).
11. SHLS -> ARRY: confirm that the exchange is taxable, that the cost of ARRY is its FMV on the
    closing date and that its holding period starts on that date (section 8A). The user decides
    whether to keep ARRY.

## 12. Discrepancies that matter for tax

From [numbers] unless stated.
1. INDmoney's FY2026-27 tax report leaves out the FLNA sale of 5 Nov 2026 (-$739.43 net) and the
   GEV sale of 9 Nov 2026. Do not file from that report.
2. [numbers] gives the FLNA INR effect two ways: -Rs 61,565 (B.1) and -Rs 53,914
   (discrepancy list). Recompute with SBI TT rates.
3. INDmoney's FY2025-26 report leaves out SCLX 22 Aug 2025 (+$224.16 net) and HSDT
   22 Aug 2025 (-$116.66). The revised ITR other-STCG of Rs 30,203 does not match the broker's
   Rs 44,944. Accepted by user 2026-11-15, no further revision (decisions.md, 15 Nov 2026).
4. GEV sale: not in the trade file, and its fee is unknown.
5. The INDmoney draft CY2026 Schedule FA is wrong (section 5).
6. Alpaca account numbers: 2423 until 5 May 2026, 1593 after. The CY2025 FA reported 1593 with
   opening date 2024-06-10.
7. Broker "Holding Since" dates are first-ever buys (IONQ, SCLX, NVDA), not the open lots.
8. SCLX/SMNR cost split by Alpaca ($186.80 moved to SMNR) is far above SMNR's fair value.
9. Alpaca March 2026 statement shows ST +$116.58 / LT -$117.05 "realised" on the SAVA -> FLNA
   rename. That was not a sale; ignore it.
10. The migration doc puts the open cost at about $9,229 (the broker's SCLX cost); FIFO trade
    cost is $9,415.53. The difference is the SCLX/SMNR cost and the NVDA +$0.17.
11. IBKR NXPI cost $77.615 vs the Indian cost of $91.32 (section 7).
12. SYRS is worth about $0.08 in total; it may be impossible to sell or transfer.
13. The Alpaca fee is quoted as both $125 and $25 [migration].
14. AY2025-26: the JSON due date says 31 Jul 2025, but the return was filed 13 Sep 2025 under
    s.139(1). It is on time only if the 15 Sep 2025 extension applies; this matters for the
    loss carried forward then (already used up).
