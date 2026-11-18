# Transfers to IBKR: checklist

Status as of 15 Nov 2026. Nothing was moved: no withdrawal, no transfer, no sale. Accounts:
IBKR individual cash account ending 4563 (Interactive Brokers LLC), Fidelity stock plan account
ending 4972, Alpaca account ending 1593 (behind INDmoney). Background and sources:
[fidelity-to-ibkr.md](fidelity-to-ibkr.md), `tax/migration-indmoney-to-ibkr.md`,
`portfolio/migration-indmoney-to-ibkr.md`.

## Summary
- **A. INDmoney shares -> IBKR (ACATS).** You start it at IBKR between 1 and 4 Dec 2026 (not 27 Nov:
  the Cogent and Immunic event bets are held at INDmoney and must not be frozen around the 30 Nov FDA
  date), after the loss sales have settled and the cash is out. Takes 4-8 business days. IBKR is free;
  Alpaca charges $125 or $25 (not yet clear). Have at least USD 25 free cash at IBKR (now USD 794).
- **B. Fidelity MSFT shares -> IBKR (form + call).** 116 whole shares move; sell the 0.8879
  fraction at Fidelity. File the IBKR "Free of Payment" notice, phone Fidelity, then email the
  signed TOA form. Free on both sides; up to 4 weeks. The form is downloaded.
- **C. ESPP and sale dollars -> IBKR (wire).** Replace the NetBenefits payout instruction (today
  HDFC) with IBKR's USD wire details now, so it is approved long before the first ESPP purchase
  on 31 Mar 2027. The change needs your phone approval in the NetBenefits app, so you must do it.
  Approval 4-7 business days; each wire 5-10 business days, fee $10 or $0.
- **Ready for you:** IBKR wire details (local file), a saved IBKR deposit method "Wire-Fidelity
  SPS", the TOA form, the Fidelity lot list (CSV, in USD) and the phone numbers below.

## Prepared by the agent (15 Nov 2026)
- IBKR deposit notice (request 586434324, USD 100, notice only, no money moved) and the saved
  deposit method "Wire-Fidelity SPS". Wire details:
  - Beneficiary: Interactive Brokers LLC, One Pickwick Plaza, Greenwich, CT 06830, USA.
  - Beneficiary bank: Citibank N.A., 388 Greenwich Street, New York 10013, USA.
  - ABA and SWIFT: in the local wire file below. No intermediary bank listed.
  - Beneficiary account: a virtual account number (VAN) that ends in your IBKR account number.
  - Payment reference (required): `<IBKR account number> / Akarshan Arora`.
  - Full details incl. the VAN: `~/.local/share/superpowers/finance/ibkr-wire-details.txt`
    (only on this Mac, not in git).
- Fidelity "Transfer of assets (TOA)" form: Drive
  `Finance/Investments/Stocks/Fidelity/forms/SPS_INTL_TOA_FORM.pdf`.
- Fidelity lot list before the move: Drive
  `Finance/Investments/Stocks/Fidelity/Fidelity_MSFT_open_lots_2026-11-15.csv` (12 lots,
  116.8879 shares, cost in USD).
- IBKR incoming transfer forms opened and read (not submitted); fields are listed below.

## A. INDmoney (Alpaca) -> IBKR by ACATS
When: 1 - 4 Dec 2026 (moved from 27 Nov on 18 Nov: COGT and IMUX, bought at INDmoney, must not be frozen
around the 30 Nov FDA date; they move with the rest), after the loss and fraction sales settle (T+1). Finish
by mid-Dec, at the latest 31 Dec 2026.

1. [you do] By 20 Nov: secure message to IBKR - do you accept SYRS, SMNR and SCLX (SMNR and SYRS
   are suspended); source account is the Alpaca one ending 1593; Alpaca's fee ($125 or $25).
   Positions to transfer include **SMNR 31.4286** and **SYRS 800** (your decision 15 Nov, option (a)
   of `tax/migration-indmoney-to-ibkr.md` section 3.5): they move in the ACATS and are sold at IBKR
   later at a nominal price to book the loss. If IBKR refuses them, see option (d) there.
2. [you do] 16-25 Nov: loss and fraction sales at INDmoney, as in `tax/migration-indmoney-to-ibkr.md`
   (SHLS fraction only on or after 30 Nov). Keep every contract note.
3. [you do] After the sales settle: withdraw the USD cash to India and keep the FIRC.
4. [you do] Before starting: download the INDmoney trade file and the latest Alpaca monthly
   statement (account title and full account number are on it). Keep the lot file
   (date, quantity, USD cost per lot).
5. [you do] Check IBKR has at least USD 25 free cash (USD 794.51 on 15 Nov) and a W-8BEN.
6. [you do] 1 - 4 Dec: IBKR -> Transfer & Pay -> Transfer Positions -> Incoming ->
   Region "United States" -> "ACATS" -> Go. Saved broker info -> No. Fill in:
   - Where are your assets held: "Another broker"; Broker Name: **Alpaca Securities
     (Part #: 3021)**.
   - Alpaca Securities Account Type: Individual (must match).
   - Account Title: exactly as on the Alpaca statement.
   - Account Number: the full Alpaca number ending 1593, in Alpaca's format.
   - Tax Identification Number: the default for W-8BEN holders.
   - Continue -> full or partial transfer: partial; list GOOGL 9, CRWD 8, NVDA 7, TRVI 161,
     CEG 4, SHLS 45 (only whole shares move; fractions do not). Then authorisation, then confirm.
     Steps 2-4 were not opened (they need the real account number).
7. [you do] Track the status at IBKR (the receiving broker runs ACATS), not at INDmoney.
8. [you do] When the shares arrive: check IBKR shows the original cost and dates; if not, enter
   them (Performance & Reports -> Tax Documents -> Cost Basis). Keep your own lot file anyway.
9. [you do] Jan 2027: collect the Dec Alpaca and IBKR statements and the ACATS confirmations.

Fees and times: IBKR none; Alpaca $125 or $25 per request (debited at IBKR); 4-8 business days;
moved shares may be blocked from withdrawal or transfer out for up to 30 days at IBKR.

## B. Fidelity vested MSFT shares -> IBKR (TOA form + phone call)
When: any time; plan 1-4 weeks. No fixed date. Do steps 1-3 before you send the form.

1. [agent done] Lot list exported (CSV above) and the TOA form downloaded.
2. [you do] Sell the 0.8879 fraction at Fidelity (View or sell shares -> MSFT -> Sell, online,
   $0 plus a tiny fee). Pick the lot if the screen offers it; otherwise Fidelity sells the oldest
   lot first (31 Dec 2024 ESPP lot). Save the trade confirmation. The cash goes to IBKR by flow C.
3. [you do] Secure message to IBKR: what goes in the TOA field "U.S. Intermediary Account
   Number", and whether they want an IBKR contact named on the form.
4. [you do] IBKR -> Transfer & Pay -> Transfer Positions -> Incoming -> Region "United States"
   -> "Free of Payment Transfer of US Securities" -> Go. Fill in:
   - Broker: **NATIONAL FINANCIAL SERVICES LLC (Part #: 0226)** (the list also has
     "Fidelity (Part #: 0226)", same number).
   - Account Number at Broker: your Fidelity stock plan account number (ends 4972).
   - Account Title: prefilled "Akarshan Arora"; must match Fidelity exactly.
   - Tax Identification Number: "None" is the only choice offered.
   - Save Broker Information: your choice.
   - Assets -> Add Asset: MSFT, 116 (or upload a CSV). Continue, then save the letter it shows
     ("View Form", with IBKR DTC 0534).
5. [you do] Fill in the TOA form in English: participant name, I-number, phone; MSFT 116; the lot
   table from the CSV (attach a sheet for more than 3 lots); receiving firm Interactive Brokers
   LLC, phone +1 877 442 2757 (US toll-free) or +1 312 542 6901, your IBKR account number,
   Individual; U.S. intermediary Interactive Brokers LLC, DTC 0534; trade and settlement date
   the same day, at least 5 business days after Fidelity gets the form. Tick "I have contacted
   the receiving firm" and sign by hand.
6. [you do] **Phone Fidelity first** (the form says so). From India: 000 800 040 4768 (global
   toll free), or access code 000 117 then 800 544 0275, or 000 800 050 4058 (local, charges may
   apply). If none work: +1 603 402 5013. Lines open Mon-Fri and from 5 p.m. ET Sunday. Have
   your NetBenefits user name or I-number ready.
7. [you do] Email the signed form from your Microsoft email to sps@fidelity.com (or fax
   1-877-236-4162). Tell IBKR the agreed date.
8. [you do] When the shares arrive: type each lot's quantity, date and total USD cost into IBKR
   (Performance & Reports -> Tax Documents -> Cost Basis -> gear by "Position Transfer").
   Otherwise IBKR treats them as bought on the transfer day.

Fees and times: Fidelity none; IBKR none; up to 4 weeks (trade date at least 5 business days
after Fidelity gets the form; 4 weeks by post).

## C. ESPP dollars and sale proceeds -> IBKR by wire
When: switch the instruction now (week of 16 Nov 2026) so it is approved by about 25 Nov,
well before the first ESPP purchase on 31 Mar 2027.

1. [agent done] IBKR wire details read and saved; deposit method "Wire-Fidelity SPS" saved.
2. [you do] NetBenefits -> View or sell shares -> Take action -> Manage transfer instructions ->
   **Update Instructions**. NetBenefits first sends a push to the NetBenefits app on your phone
   (or "Try another way"); approve it. The agent stopped here.
3. [you do] In the form, choose "Wire to Financial Institution" (a broker, not a bank), currency
   U.S. DOLLAR (USD), and enter from the local file:
   - Receiving institution: Interactive Brokers LLC, One Pickwick Plaza, Greenwich, CT 06830,
     USA; phone +1 877 442 2757.
   - Bank (or intermediary bank, if the form asks for one): Citibank N.A., 388 Greenwich
     Street, New York 10013, USA; ABA and SWIFT in the local wire file.
   - Account number: the VAN from the local file.
   - Further credit / additional instructions: `<IBKR account number> / Akarshan Arora`.
   - Name on account: Akarshan Arora (must match your Fidelity name).
   - Sign electronically, then **you click the final submit**.
   This replaces the HDFC instruction (only one can be active). Changing it cancels any pending
   cash transfer; there was none on 15 Nov.
4. [you do] Wait for approval: 4-7 business days. Fidelity emails or calls if data is wrong.
5. [you do] Each time (from 31 Mar 2027, or now for the fraction sale cash): sell online, wait
   for settlement, create an IBKR deposit notice with "Wire-Fidelity SPS", then NetBenefits ->
   View or sell shares -> cash row (FYIXX) -> Transfer -> amount -> Preview -> submit. Max
   $100,000 a day online; under $25 may be rejected.

Fees and times: Fidelity wire $10 (help page) or $0.00 (transfer screen); IBKR incoming free;
issued in 5-7 business days, arrives in 5-10; tradable at once at IBKR, withdrawable after 3
business days.

## Records for Indian tax (keep before and after each move)
- Before the move: Fidelity lot list (done, 15 Nov), INDmoney trade file and Alpaca statement.
- Per lot: date acquired, quantity, source (RSU vest "DO" or ESPP "SP"), US cost per share in
  USD, and our Indian cost (market value on the vest or purchase date x SBI TT buying rate;
  method in `portfolio/details.md`).
- The move is not a sale: keep the TOA copy, the IBKR "Free of Payment" letter, the ACATS
  confirmations, and the statements showing shares leaving and arriving.
- Each sale and wire: trade confirmation, the Fidelity wire confirmation and the IBKR deposit
  record.
- Schedule FA for CY2026: Alpaca, Fidelity and IBKR accounts (`tax/migration-indmoney-to-ibkr.md`
  section 5).

## Open points and discrepancies
- The HDFC instruction shows "Name on Account" as "SUPARANEE LAOJANAKARSHAN ARORA"; check it.
  For IBKR, the name on the receiving account must match your Fidelity name.
- Fidelity wire fee: $10 (help page) vs $0.00 (transfer screen). Check the first wire.
- IBKR's deposit page says a wire arrives in 1-2 business days; Fidelity says 5-10.
- Alpaca DTC 3021 is from IBKR's broker list only; not confirmed on an Alpaca document.
- Alpaca ACATS fee: $125 vs $25, not resolved.
- Exact NetBenefits "Wire to Financial Institution" fields were not seen (blocked by the phone
  approval); the field mapping in C.3 follows Fidelity's help page.
