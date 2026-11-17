# Move US shares from INDmoney (Alpaca) to Interactive Brokers

Status as of 15 Nov 2026. Source: Gmail thread "ACATS transfer of US stocks to Interactive
Brokers" (INDmoney ticket #3576996, 4 threads, 9 messages) and the INDmoney holdings report of
8 Nov 2026. No mail from Interactive Brokers or Alpaca about a transfer was found.

## Goal and why
From the user's mail of 8 Nov 2026: "I want to move my US stocks to Interactive Brokers so all
my US holdings are in one account. My other US shares are already there. This is a firm
decision." Method: ACATS transfer of stocks (and, if possible, cash) from the Alpaca account
behind INDmoney to the existing IBKR account (ending 4563).

## Timeline
| Date (IST) | From | Subject | What happened |
|---|---|---|---|
| 5 Nov 2026 | (INDmoney trades) | - | Sold out BSX, IONR, FLNA, KLAC, PSI, URA (before the ticket). |
| 7 Nov, 21:51 | User -> usstockssupport@indmoney.com | ACATS transfer of US stocks to Interactive Brokers | Request raised: transfer stocks and cash to IBKR via ACATS. Asked 4 questions: (1) is the Alpaca account in my own name, (2) can wallet cash move, (3) transfer-out fee and fractional shares, (4) can SYRS and SMNR move. |
| 7 Nov, 21:51 | INDmoney US Stocks Support | Ticket Received ... [#3576996] | Auto acknowledgement, ticket #3576996. |
| 7 Nov, 22:24 | INDmoney US Stocks Support | Re: ACATS transfer ... [#3576996] | Asked for a time to call. |
| 8 Nov, 01:15 | INDmoney US Stocks Support | ACATS transfer ... | "Waiting for your response." |
| 8 Nov, 01:54 | INDmoney Transactions | Your US Stocks - Holdings Report is here! | Holdings report (IND-HOLDINGS_REPORT...-2026-11-08-V04.xls). Trade report and Tax P&L reports also mailed the same night. |
| 8 Nov, 02:02 | User | ACATS transfer ... | Email only, no call; firm decision; repeated the 4 questions. |
| 8 Nov, 03:09 | User | Re: ACATS transfer ... [#3576996] | New question: holdings/trade reports show Alpaca account ending 1593, monthly statements show ending 2423 - which one to give IBKR? |
| 9 Nov, 13:59 | User | ACATS transfer ... | Asked for an update. |
| 9 Nov, 15:36 | INDmoney US Stocks Support | Re: ACATS transfer ... [#3576996] | Ticket moved to the share transfer team. |
| 9 Nov, 15:43 | support@indmoneyglobal.com (share transfer team) | Re: ACATS transfer ... [#3576996] | Answer: fees, cash, fractional shares, trading freeze, IBKR must start the ACATS; account number is the one ending 1593 (see Costs below). |
| 9 Nov, 20:00 | INDmoney Transactions | SELL order of GE Vernova Inc. ... | Sold the whole GEV position (0.872929 sh, fractional only) for $706.03. |
| 10 Nov, 16:15 | INDmoney US Stocks Support | ACATS transfer ... - 3576996 | Ticket closed for no reply ("feel free to reopen"). |

No forms, rejections or charges have appeared yet; no transfer has been started at IBKR.

## Current status
| Item | Status |
|---|---|
| Ask INDmoney how transfer-out works | Done (answer 9 Nov) |
| Alpaca account number to use | Answered as the one ending 1593; the number ending 2423 on monthly statements was not explained. Open. |
| Account held in user's own name (question 1) | Not answered. Open. |
| Can SYRS / SMNR move | Not answered: INDmoney says it depends on IBKR accepting them. Open, ask IBKR. |
| Fractional GEV | Done (sold 9 Nov). Other fractions still held. |
| Cash plan (withdraw to India, or buy whole SGOV/GOVT and move them) | Not decided. |
| Keep USD 25 free in IBKR for the transfer debit | Not done / not confirmed. |
| ACATS request started at IBKR | Not started. |
| INDmoney ticket #3576996 | Closed 10 Nov (can be reopened by replying). |

Overall: **pending, waiting on the user**. Nothing is blocked by a broker.

### Next action for the user
1. Ask IBKR (Client Services / secure message in the IBKR portal) whether SYRS, SMNR and SCLX
   can be received by ACATS, and which Alpaca account number to use (ending 1593 vs 2423).
   If needed, reopen INDmoney ticket #3576996 (reply to usstockssupport@indmoney.com) to ask
   about the 2423 number and the account holder name.
2. Decide on the wallet cash: withdraw to the Indian bank, or buy whole shares of SGOV/GOVT
   (no INDmoney brokerage) to move them too.
3. Decide on fractions: sell them first, or let them be liquidated in the transfer.
4. Keep at least USD 25 cash in the IBKR account.
5. Start the incoming ACATS transfer in the IBKR portal (receiving broker starts it; source
   broker Alpaca Securities). Track status with IBKR, not INDmoney.

## Costs and constraints (from the 9 Nov answer)
- Alpaca outgoing ACATS fee: "Base Fee - $125 per transfer request".
- The same mail also says "a USD 25 debit balance will be transferred to [the] receiving
  [broker] to cover the outgoing transfer fee"; keep USD 25 in IBKR. **Discrepancy:** $125 vs
  $25 is not explained; confirm with INDmoney or IBKR before starting.
- Cash cannot move by ACATS. Options: withdraw to the Indian bank at any time, or buy whole
  SGOV/GOVT shares and move them; leftover cash must be withdrawn.
- Only whole shares move; fractional shares cannot and "may be liquidated" in the process.
- Trading, deposits, buys and sells are frozen in INDmoney during the transfer.
- The receiving broker (IBKR) starts the transfer and gives status updates.
- Terms: https://www.indmoney.com/page/global-access-transfer-out-terms
- Tax: not mentioned in the mails. Note that selling or liquidating fractions (and the GEV sale)
  are sales for capital gains; moving shares by ACATS is not a sale, but check that IBKR
  receives the original cost basis and dates.

## Holdings in scope
INDmoney holdings report of 8 Nov 2026 (`scripts.brokers.indmoney`), with GEV removed after the
9 Nov sale. Positions shown as about 1e-9 shares (FLNA, URA, PSI, KLAC, BSX) are leftovers of
the 5 Nov sales and are treated as zero.

| Symbol | Quantity | Whole shares that can move | Fraction left (sell/liquidated) | Cost ($) | Note |
|---|---|---|---|---|---|
| GOOGL | 9.160599 | 9 | 0.160599 | 2884.51 | |
| CRWD | 8.490700 | 8 | 0.490700 | 1495.58 | |
| NVDA | 7.494930 | 7 | 0.494930 | 1329.30 | |
| TRVI | 161.679000 | 161 | 0.679000 | 1196.47 | |
| CEG | 4.286771 | 4 | 0.286771 | 997.06 | |
| IONQ | 13.239410 | 13 | 0.239410 | 498.53 | |
| SHLS | 45.210150 | 45 | 0.210150 | 236.86 | |
| SYRS | 800.000000 | 800 | 0 | 217.84 | IBKR acceptance unconfirmed (user asked) |
| SMNR | 31.428570 | 31 | 0.428570 | 187.00 | IBKR acceptance unconfirmed (user asked) |
| SCLX | 31.428570 | 31 | 0.428570 | 185.74 | not asked about; check with IBKR too |
| GEV | 0 (was 0.872929) | 0 | - | - | sold 9 Nov for $706.03 |

Cost of open positions about $9,229 (report total $10,226 minus GEV $997). Holdings were not
re-downloaded after 8 Nov; refresh the report before starting, as quantities may have changed.
Wallet cash balance is not in the mails.
