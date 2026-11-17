# Move Microsoft shares and ESPP sale dollars from Fidelity to IBKR (in USD)

Status as of 15 Nov 2026. Read only: nothing was submitted, sold or changed. Accounts: Fidelity
NetBenefits stock plan account ending 4972 (international participant), Interactive Brokers
LLC individual cash account ending 4563.

## Summary
- **Shares (A):** possible, free on both sides, whole shares only. Fidelity says international
  (non-US) share transfers cannot be done online and do not use ACATS: you fill in Fidelity's
  "Transfer of assets (TOA)" form, and Fidelity sends the shares from DTC 0226 (National
  Financial Services) to IBKR's DTC number 0534. On the IBKR side you file a "Free of Payment
  Transfer of US Securities" notice (not ACATS). Fidelity says it can take up to 4 weeks; you
  must phone Fidelity before you email the form. Cost basis and purchase dates do not move
  with the shares. IBKR records them as bought on the transfer day at that day's price until
  you type each lot in yourself.
- **Cash (B):** possible in USD. NetBenefits keeps **one** set of payout instructions. Today
  that is a USD wire to HDFC Bank India, ending 9102 (approved 15 Sep 2026). To send money to
  IBKR you replace it with a "Wire to Financial Institution" set holding IBKR's USD bank
  details and your IBKR account number. Fidelity takes up to 4 business days to approve the
  change (the instructions page says 4-7). At least one name on the receiving account must
  match your Fidelity name. Online limit is $100,000 a day; amounts under $25 may be rejected.
  Fidelity's help page says $10 per wire; the transfer screen showed a $0.00 fee, and the
  Sep 2026 wire had no fee and arrived in full. Allow 5-10 business days. IBKR charges nothing for incoming wires.
- **Which to use (C):**
  - (i) Vested MSFT lots sold one by one on their long-term dates: move the whole shares to
    IBKR once with the TOA form. Then sell each lot at IBKR on its date and buy the funds the
    same day. This saves 6+ separate wires of 5-10 days each. First type each lot's date and
    cost into IBKR, and sell the 0.8879-share fraction at Fidelity.
  - (ii) Each ESPP purchase sold the same day: sell at Fidelity (online sales cost $0 plus a
    tiny activity fee) and wire the dollars to IBKR. A share transfer is too slow (at least 5
    business days of notice, up to 4 weeks) for a same-day sale.
  - Both need the wire instructions changed from HDFC to IBKR. While they point to IBKR, every
    cash payout from Fidelity goes there.

## A. Move shares (Fidelity TOA form -> IBKR Free of Payment transfer)
Before you start:
- Whole shares only. Today there are 116.8879 MSFT, so 116 can move. Sell the 0.8879 at
  Fidelity or leave it there.
- Pick the lots and keep their details (see "Records to keep" below).
- Check that your name in IBKR matches your Fidelity name exactly. IBKR says the "Account
  title must match exactly" and does not allow a change of owner.

Steps:
1. At IBKR: Transfer & Pay -> Transfer Positions -> Incoming. Set Region to "United States".
   Choose "Free of Payment Transfer of US Securities" -> Go.
2. Fill in the form:
   - Broker: "NATIONAL FINANCIAL SERVICES LLC (Part #: 0226)". The list also has
     "Fidelity (Part #: 0226)", which is the same number.
   - Account Number at Broker: your Fidelity stock plan account number.
   - Account Title: your full name, exactly as at Fidelity.
   - Tax Identification Number: as asked.
   - Assets: Add Asset -> MSFT and the number of shares.
   - Continue. At the end IBKR shows a letter of authorisation ("View Form") with its DTC
     number 0534. Save it.
   - IBKR calls this request "notifications only": nothing moves until Fidelity sends the
     shares.
3. In NetBenefits: Stock plans -> Statements & records -> Additional forms -> "Transfer of
   assets (TOA)" -> "Print the transfer of assets (TOA) form (PDF)".
4. Fill in the form in English:
   - Participant name, participant number (the I-number) and phone with country code.
   - MSFT and the number of whole shares (or "all available"; fractions are left out).
   - For chosen lots, fill in the lot table: shares from the lot, date acquired, cost basis
     per share. If you name more than three lots, attach a sheet.
   - Receiving Financial Institution: Interactive Brokers LLC, its phone number, your IBKR
     account number and registration type (Individual).
   - U.S. Intermediary Institution: Interactive Brokers LLC, DTC 0534. Ask IBKR whether it
     wants your IBKR account number in "U.S. Intermediary Account Number"; the form says to
     check with the receiving broker.
   - Trade date and settlement date: the same day, at least 5 business days after Fidelity
     gets the form by email or fax. By post, allow 4 weeks.
   - In the blank space at the bottom, add the IBKR contact (name, email, phone) and the dates.
   - Tick "I have contacted the receiving firm", then sign by hand.
5. Phone Fidelity Stock Plan Services to verify the request. The form says: "Prior to
   emailing, you must call Fidelity to verify the transfer request."
   - From India, use the number listed on NetBenefits -> Contact Us -> Asia Pacific -> India.
   - From elsewhere, call +1 603 402 5013.
6. Send the signed form by one of these:
   - Email from your **employer-provided** email address to sps@fidelity.com.
   - Fax to 1-877-236-4162 ("TOA Deliveries").
   - Post to Fidelity Stock Plan Services, P.O. Box 770001, Cincinnati, OH 45277-0043.
7. Tell IBKR the transfer is coming and the agreed date. The form says the receiving broker
   should alert its intermediary so the shares are accepted on that date.
8. When the shares arrive, enter the cost basis at IBKR: Performance & Reports -> Tax
   Documents -> Cost Basis -> gear icon by "Position Transfer". Type each lot's quantity,
   acquisition date and total cost.
   - Use the US figures Fidelity shows (Fidelity lot view -> Asset currency).
   - Keep the Indian figures in our own records.
9. Update `scripts.brokers.*` and `accounts.md` once the shares are at IBKR.

Records to keep, because IBKR will not get them and Indian cost differs from US cost:
- Per lot: date acquired, number of shares, source (RSU vest or ESPP purchase), and Fidelity's
  US cost basis per share in USD.
- Our Indian cost per lot: the market value at vest or purchase, and the SBI TT buying rate on
  the right date. Current method is in `details.md` ("Our cost").
- Get Fidelity's lot list before the move: NetBenefits -> View or sell shares -> MSFT "View
  share details" -> Export -> "Current shares (CSV)".
- The TOA form copy, the Fidelity statement that shows the shares leaving, and the IBKR
  statement that shows them arriving.

## B. Send sale dollars to IBKR in USD
One-time setup:
1. At IBKR: Transfer & Pay -> Deposit -> "Use a new deposit method" -> currency "United States
   Dollar (USD)" -> Bank Wire -> Go.
   - Fill in Sending Institution "Fidelity Stock Plan Services" and an account nickname.
   - Fill in an amount. You can make it a recurring notification.
   - Click Next to get the wire instructions. This creates a deposit notice; it moves no
     money, but you must do it to see the details.
   - Write down the beneficiary bank, its ABA routing number and SWIFT code, the beneficiary
     name and account, and the reference. The reference is your IBKR account number and name;
     if space is short, the account number only.
   - IBKR says routing details depend on the currency and IBKR entity, so read them from this
     screen and do not copy them from elsewhere.
2. In NetBenefits: View or sell shares -> Take action -> "Manage transfer instructions" ->
   "Update Instructions".
   - Choose "Wire to Financial Institution" and currency U.S. DOLLAR (USD).
   - Enter IBKR's bank details from step 1. If IBKR lists an intermediary bank, enter it too.
   - Put your IBKR account number and name in the further-credit or additional-instructions
     field.
   - Sign electronically.
3. Wait for approval: up to 4 business days per the help page, 4-7 per the instructions page.
   - This **replaces** the HDFC instruction; only one set can be active.
   - To go back to HDFC later, update again (another approval wait). Deleting an instruction
     needs a phone call.

Each time:
1. Sell in NetBenefits: View or sell shares -> MSFT -> Sell, online.
   - Choose specific lots if offered; otherwise Fidelity sells first-in, first-out.
   - Wait for the sale to settle.
2. Create an IBKR deposit notice for the amount, or use the recurring one: Transfer & Pay ->
   Deposit -> saved method.
3. In NetBenefits: View or sell shares -> cash row (FYIXX) -> Transfer -> amount ->
   "Preview transfer" -> submit.
   - Up to $100,000 a day online; call for more.
   - Under $25 may be rejected.
4. The money arrives at IBKR in 5-10 business days. You can trade with it at once. IBKR holds
   it 3 business days before you can withdraw it.

Alternative (no instruction change): Fidelity wires USD to the HDFC account in your name, which
is what is set up today. HDFC would normally credit an Indian savings account in rupees, which
is what we want to avoid. You would then have to send it out again under LRS. IBKR's own
deposit page also lists "Direct ACH Transfer" and "Link a New Bank Account", but Fidelity Stock
Plan Services pays out only by wire or check, so these do not apply.

## Fees and times
| Step | Fee | Time | Source |
|---|---|---|---|
| Fidelity share transfer out (TOA) | none ("no service charges on share transfer") | up to 4 weeks; trade date at least 5 business days after the form arrives | TOA form; fidelity.com SPS FAQ |
| IBKR incoming Free of Payment (DTC) | none | same day Fidelity delivers | IBKR transfer screen; IBKR FAQ 32668619 |
| IBKR DWAC (not to use) | USD 100 per transfer | same day | IBKR transfer screen |
| Fidelity online sale | $0 plus activity assessment fee $0.01-0.03 per $1,000 | settles next business day | Microsoft plan fee PDF |
| Fidelity sale through a representative | $32.95 | - | Microsoft plan fee PDF |
| Fidelity wire | $0 (Sep 2026 wire arrived in full; help page says $10) | issued in 5-7 business days (help); "average of 5-10 business days" (screen) | NetBenefits wire help; transfer screen |
| Change wire instructions | none stated | up to 4 business days (help); 4-7 (screen) | NetBenefits wire help; Transfer instructions page |
| IBKR incoming wire | none (banks in between may take a fee) | credited on arrival; withdrawal hold 3 business days | IBKR FAQ 27284795; IBKR deposit screen |
| Fidelity annual fee | $25, waived with a balance of $100 or more or outstanding grants | yearly | Microsoft plan fee PDF |

## Sources (all seen 15 Nov 2026)
- NetBenefits, logged in:
  - View or sell shares: MSFT row has only Sell, and the cash row has Transfer.
  - Transfer instructions: one approved USD wire to HDFC, 15 Sep 2026; "Allow 4-7 business
    days to approve any changes".
  - Cash Transfer screen: fee $0.00, under $25 may be rejected, 5-10 business days.
  - Statements & records -> Additional forms: "Transfer of assets (TOA) ... Non-US transfers
    cannot be made online."
  - MSFT lot view: date acquired, cost basis, share source, CSV export.
- Fidelity TOA form `SPS_INTL_TOA_FORM.pdf`, form id 537798.8.0 / 1.904327.102: the steps,
  DTC 0226, phone check, email, fax and post details, "ACAT is unavailable" wording, whole
  shares, no charge, up to 4 weeks.
- Fidelity "Transaction fees for Microsoft Corporation stock plan participants" PDF, id
  891539.4.0 (linked from the NetBenefits plan summary).
- NetBenefits help "About Requesting a Wire or Check":
  https://scs.fidelity.com/webxpress/help/topics_isp/learn_wire_check.shtml
  - Wire to Financial Institution, one active set, name match, review up to 4 business days.
  - $10 per wire, $100,000 a day online, 5-7 business days.
- fidelity.com Stock Plan Services (global), "Explore your account" FAQ, which covers the
  International Transfer Request Form and says Fidelity charges no fee:
  https://www.fidelity.com/stock-plan-services/global/your-account
- Fidelity Participant Agreement (international): shares are held in a Participant Trust.
- IBKR Client Portal, logged in: Transfer Positions -> Incoming -> United States lists ACATS,
  Free of Payment, DRS ($25) and DWAC ($100).
  - The Free of Payment form's broker list has NFS/Fidelity 0226.
  - Deposit -> USD -> Bank Wire form (4 steps, recurring notification option, 3-day
    withdrawal hold).
- IBKR guides and FAQs:
  - ibkrguides.com Free of Payment transfer
    (clientportal/transferandpay/foptrans.htm and enterfoptrans.htm; updated Oct 2025 and
    Apr 2026).
  - FAQ 32668619: Free of Payment transfer via DTC, DTC 0534, no IBKR fee.
  - FAQ 1146101228: Fidelity = NFS DTC 0226.
  - FAQ 32655975: employee plan shares need same-name, electronic, unrestricted holding.
  - FAQ 28216784: non-US taxpayers - cost basis generally not sent; default acquisition date
    is the transfer date.
  - ibkrguides positiontransfer.htm: manual cost basis entry (Oct 2025).
  - FAQ 27280950: wire details only after a deposit notice.
  - FAQ 77828941: reference field.
  - FAQ 27284795: no fee for incoming deposits.
  - FAQ 28221565: third-party deposits.
  - FAQ 29083510: wire timing.
  - Open a FAQ at https://www.interactivebrokers.com/lib/cstools/faq/#/content/<id>.

## Not verified
- Whether an IBKR ACATS request against NFS 0226 would work for this stock plan account. The
  TOA form is Fidelity's stated route ("when the standard transfer process (ACAT) is
  unavailable"), so these steps use it; ACATS was not tried.
- What IBKR wants in the TOA "U.S. Intermediary Account Number" field, and whether it wants
  its own contact named on the form. Ask IBKR support (Message Center) before sending.
- IBKR's USD wire bank details for IB LLC. They are shown only after a deposit notice, which
  was not created.
- The exact fields of NetBenefits' "Update Instructions" form for "Wire to Financial
  Institution" (not opened), and whether the sell screen offers lot choice (the help glossary
  lists "Choose Specific Shares").
- India phone number for Fidelity (the page needs a country pick; not read).
- The "Name on account" on the approved HDFC instruction shows a longer combined name. Check
  it is right. For IBKR, the IBKR account title must match your Fidelity name.
- Indian rules (CA to confirm):
  - Keeping sale proceeds abroad and reinvesting them at IBKR (FEMA/LRS; see `plan.md`).
  - Which lot counts as sold for Indian tax after a move.
  - IBKR commission per sale (not checked here).
