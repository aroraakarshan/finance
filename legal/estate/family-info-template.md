# Family information sheet (template)

## Summary
A blank sheet that tells the family which accounts exist, who to contact, where the will and
statements are, and what to do first after a death. Copy it outside git, fill it in (last 4
digits only, no passwords), keep it with the will and tell the executor where it is.

Owner: `finance-legal`. Template written 2026-11-15. Not legal advice.

How to use: copy this file OUTSIDE the git repository (for example next to the will, or a
printed copy in a safe place), fill it in, and tell the executor where it is. Update it once a
year. Never write passwords, PINs, PAN, Aadhaar, full account numbers or client IDs here: last 4
digits only. Detailed rules and steps: [Estate and nominations](README.md).

Last updated: ____________  By: ____________

## 1. Key people

| Role | Name | Relationship | Phone | Email | Notes |
|---|---|---|---|---|---|
| Executor (named in the will) | | | | | |
| Backup executor | | | | | |
| Guardian for minor children (if any) | | | | | |
| Chartered accountant (India) | | | | | Has past returns, Schedule FA |
| Lawyer (India) | | | | | Has the will copy? |
| US tax adviser (for Form 706-NA) | | | | | |
| Employer HR / benefits (Microsoft India) | | | | | Group life, gratuity, PF, final pay |

## 2. Will and documents

| Item | Where it is | Notes |
|---|---|---|
| Original will (date: ______) | | Registered? Y/N, office: ______ |
| Copies of the will | | |
| This sheet (filled copy) | | |
| Life insurance policies | | |
| Property papers | | |
| Locker (bank, branch, locker last 4) | | Key kept at: ______; locker nominee(s): ______ |
| Google Drive `Finance/` folder (statements; see below) | Account owner: ______ | How the executor gets access: ______ |

Where statements are, in Google Drive `Finance/`:
- `Tax/FY<yyyy-yy>/<broker>/` - statements, confirmations, 1042-S, tax P&L for ETrade, Fidelity,
  IBKR, INDmoney, Angel One.
- `Tax/FY<yyyy-yy>/Income Tax Site/`, `ITR/`, `<employer>/` - AIS, TIS, 26AS, returns, Form 16.
- `Investments/Stocks/<broker>/` - holdings exports (AngelOne, INDmoney, IBKR, ETrade, Fidelity).
- `Salary/<employer>/` - payslips, EPF passbooks, Microsoft stock export (RSU grants).
- `Banking/`, `Bills/`, `Investments/Gold/`.

## 3. Accounts in India

| Institution | Type | Last 4 | Nominee(s) and % | Joint holder | Statements in | Notes |
|---|---|---|---|---|---|---|
| AngelOne (DP: CDSL/NSDL) | Demat + trading | | | | `Investments/Stocks/AngelOne/` | |
| CAMS / KFintech (via AngelOne) | MF folios (list AMCs) | | | | `Tax/FY*/Angel One/` | One nominee per folio |
| EPFO (UAN last 4: ____) | EPF / EPS / EDLI | | | - | `Salary/<employer>/` | Old Qualcomm, NXP accounts merged? Y/N |
| Bank: ______ | Savings / FD | | | | `Banking/` | |
| Bank: ______ | Savings / FD | | | | | |
| PPF (bank/post office) | PPF | | | - | | |
| NPS (CRA) | Tier I | | | - | | |
| Insurer: ______ | Term life, cover Rs ____ | Policy last 4 | | - | | |
| Insurer: ______ (premium paid by: ______) | Term life on my life, cover Rs ____, expires ______ | Policy last 4 | | - | | Policyholder/proposer: ______ (if not me, the claim goes to the policyholder) |
| Employer group life | Life cover Rs ____ | | | - | HR | |
| Health insurance | | | | - | | |
| Property | | - | - | | | Title deed at: ______ |
| Loans / credit cards | | | - | | | Debts to settle |

## 4. Accounts outside India

| Institution | Type | Last 4 | Beneficiary / TOD set? | Statements in | Notes |
|---|---|---|---|---|---|
| Interactive Brokers (entity: ______) | Brokerage (US shares, UCITS ETFs) | | | `Tax/FY*/IBKR/` | Main US account |
| Fidelity NetBenefits | Microsoft stock plan (RSU, ESPP) | | | `Tax/FY*/Fidelity/` | Unvested awards vest at death (Microsoft award form) |
| INDmoney / Alpaca | US brokerage | | | `Tax/FY*/INDmoney/` | Being moved to IBKR by Dec 2026 |
| ETrade (Morgan Stanley) | Old Qualcomm / NXP plans | | | `Tax/FY*/ETrade/` | Emptied Dec 2025; closed? Y/N |

## 5. What to do first after a death

India (first weeks):
1. Get 10-15 copies of the death certificate (municipal office); a copy with a QR code is
   accepted by SEBI-regulated firms.
2. Find the will and this sheet; tell the executor and the CA.
3. Employer (if still employed): HR for final pay, gratuity, group life insurance, PF/EPS/EDLI
   claims.
4. Insurance: nominee files claims with each insurer.
5. Banks: nominee(s) claim deposits; locker opened with the bank.
6. AngelOne demat and MF folios: nominee files a transmission request (form, own demat CML,
   death certificate). Without a nominee: indemnity and affidavit-cum-NOC from all heirs (up to
   Rs 30 L in demat), or will / legal heir certificate / succession certificate above that.
   Nominees hold for the legal heirs and pass the shares on (reason code TLH, no tax on that step).
7. EPF: claims through the EPFO / employer; NPS through the CRA; PPF at the bank (account closes).

Foreign brokers (next):
8. Tell IBKR, Fidelity (Microsoft stock plan), INDmoney/Alpaca and ETrade (if still open). Ask
   each for its estate checklist for a non-US resident. Expect the accounts to be frozen.
9. Inherited foreign shares do not use the heirs' LRS limit; heirs must show them in Schedule FA
   in their own tax returns.

US estate tax (deadline):
10. If US shares and US ETFs were worth more than $60,000 at death, a US Form 706-NA is due
    within 9 months of the date of death (tax due then too; filing can be extended 6 months
    with Form 4768). The brokers release assets only after an IRS transfer certificate. Get a
    US tax adviser early. Details: [foreign assets](foreign-assets.md#us-estate-tax-and-brokers) and `research/themes/us-estate-tax.md`.
11. Irish UCITS ETFs: no Irish inheritance tax for Indian-resident heirs (s.75 CATCA 2003), but
    they are still held at the broker and follow its process.

Tax for heirs (India): no inheritance tax; heirs pay capital gains tax only when they sell, using
the deceased's cost and holding period. Keep the cost records in `Finance/`.
