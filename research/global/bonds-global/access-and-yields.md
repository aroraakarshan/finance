# Global bonds: access and current yields

Back to [Global bonds index](../bonds-global.md). Sources: [sources](sources.md).

## Summary
- Listed Irish UCITS bond ETFs (AGGU, ITPS, IEMB, ...) are allowed under LRS; direct foreign bonds are OTC (grey); US-listed bond ETFs are US-situs.
- 10y yields are near 20-year highs: UK 5.21%, Bund 3.43%, JGB 2.84%, Canada 3.78%, Australia 5.28% (Sep); real yields 2-2.9%.
- Credit spreads are thin (US IG 0.89%, HY 3.20%, 12 Nov 2026): credit is not cheap.
- What to do: if any bond ETF, prefer one accumulating Irish line; see the index verdict table.

## 1. Access for an Indian resident

- Buying foreign government bonds directly at IBKR is OTC: LRS status grey [ibkr-global/rules.md 1].
  Listed Irish UCITS bond ETFs on LSE/Xetra = listed foreign funds = allowed under LRS.
- US-listed bond ETFs (EMB, EMLC, LQD, HYG): US-situs (US estate tax above $60k), 25% US
  withholding on distributions [tax/investment-types.md]. Prefer the UCITS lines below.

| Exposure | UCITS ETF (LSE ticker) | ISIN | TER | Size | Dist/Acc | Source |
|---|---|---|---|---|---|---|
| Global aggregate, USD hedged | AGGU | IE00BZ043R46 | 0.10% | EUR 3,792 m | Acc | justETF [J] |
| Global aggregate, unhedged | AGGG | IE00B3F81409 | 0.10% | EUR 2,449 m | Dist | [J] |
| Global govt bonds, unhedged | IGLA | IE00BYZ28V50 | 0.20% | EUR 541 m | Acc | [J] |
| US TIPS | ITPS | IE00B1FZSC47 | 0.10% | EUR 3,393 m | Acc | [J] |
| Euro inflation-linked govt | IBCI (Xetra IBC1) | IE00B0M62X26 | 0.09% | EUR 1,803 m | Acc | [J]; LSE ticker IBCI not verified |
| UK index-linked gilts | INXG | IE00B1FZSD53 | 0.10% | EUR 557 m | Dist | [J] |
| USD IG corporate | LQDE | IE0032895942 | 0.20% | EUR 3,392 m | Dist | [J] |
| USD high yield | IHYU | IE00B4PY7Y77 | 0.50% | EUR 1,889 m | Dist | [J] |
| EM USD sovereign | IEMB | IE00B2NPKV68 | 0.45% | EUR 3,435 m | Dist | [J] |
| EM local-currency govt | SEML | IE00B5M4WH52 | 0.50% | EUR 4,856 m | Dist | [J] |

- "AGGH": ISIN not verified (IE00BDBRDM35 is the EUR-hedged line, Xetra EUNA, not USD) [J].
- "Hedged" here means hedged to USD. For an INR investor the USD exposure stays.

## 2. Valuation now: 10-year government yields vs history

| Country | 10y now (date) | 1y ago | 10y avg | 20y avg | Rank in 20y | Real 10y | Curve |
|---|---|---|---|---|---|---|---|
| US (ref.) | 5.10% (12 Nov) [F] | 4.08% | 2.94% | 2.89% | 99th pct | TIPS 2.86% [F] | 2y 4.86%, 3m 4.32% |
| UK | 5.21% (11 Nov) [BoE] | 4.64% | 2.38% | 2.75% | 99th pct | 2.02% [BoE] | 5y 4.88%, 20y 5.68% |
| Germany | 3.43% (13 Nov) [BB] | 2.79% | 1.03% | 1.65% | 88th pct | not verified | 2y 3.13%, 30y 3.83% |
| Japan | 2.84% (12 Nov) [MoF] | 1.71% | 0.52% | 0.74% | Sep 2026 = 20y high | not verified | 2y 1.86%, 30y 3.97% |
| Australia | 5.28% (Sep 2026 avg) [F] | 4.30% | 2.92% | 3.66% | 81st pct | not verified | RBA blocked |
| Canada | 3.78% (12 Nov) [BoC] | 3.22% | 2.34% | 2.53% | 93rd pct | RRB 1.94% [BoC] | 2y 3.33% |
| EM local (GBI-EM) | not verified | - | - | - | - | - | - |

- Averages and ranks: FRED OECD monthly series (to Sep 2026), so "now" daily values differ a bit
  from the monthly ones (UK Sep 5.24%, Bund 3.47%, JGB 3.05%, Canada 3.88%) [F].
- Reading: every major market is near its highest yield in 15-20 years; Japan moved most
  (1.71% -> 2.84% in a year). Curves are upward sloping (long end above short end) in UK, Germany,
  Japan, Canada: investors are paid for duration again.
- Credit (ICE indices via FRED, 12 Nov 2026) [F]: US IG yield 5.96%, spread 0.89% (3y range
  0.73-1.23%); US HY yield 8.16%, spread 3.20% (3y range 2.59-4.61%); Euro HY 6.43%; EM corporate
  6.54%; EM HY corporate 8.62%. FRED now keeps only 3 years of ICE data, so long-run spread
  averages are not verified here. Yields are high because government yields are high; spreads are
  in the lower half of their 3-year range (credit is not cheap).
