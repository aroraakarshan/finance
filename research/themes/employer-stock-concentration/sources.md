# Employer stock: sources

## Summary
All sources used in this note, with access result and date read. Own data (scripts, award export) and
primary sources (RBI, CRS, FINRA, budget memorandum) carry the main facts; planner pages for the 10% rule
could not be fetched.

Back to the index: [employer-stock-concentration.md](../employer-stock-concentration.md). Written 2026-11-15 by `finance-research`.

| Source | Used for | Access | Checked |
|---|---|---|---|
| `portfolio/summary.md` (commit 21a4c78), `portfolio/accounts.md` | Totals, accounts, employers | Repository | 2026-11-15 |
| `scripts.value`, `etrade.transfers()`, `fidelity.holdings()`, `fidelity.purchases()` | Values, lots, ESPP terms | Own scripts | run 2026-11-15 |
| `Salary/Microsoft/Stock/StockExport_2026-11-08.xlsx` | Unvested awards, vest schedule | Google Drive | 2026-11-15 |
| yfinance (prices, `INR=X`, sectors via `info`) | Drawdowns, volatility, correlation, FX at acquisition | Python | 2026-11-15 |
| `tax/investment-types.md` (finance-tax) | Rates, lot order, MSFT hold-to-LT, estate tax, AF s.76 | Repository | 2026-11-15 |
| `tax/migration-indmoney-to-ibkr.md`, `tax/angelone-metals-and-mf-exits.md` | Set-off, realised gains/losses, no US CGT | Repository | 2026-11-15 |
| Bessembinder 2018, RePEc abstract | Single-stock returns | https://ideas.repec.org/a/eee/jfinec/v129y2018i3p440-457.html | 2026-11-15 |
| Benartzi 2001; "Company Stock, Market Rationality, and Legal Reform" 2004 | Employee stock behaviour | Crossref API abstracts (one query 429) | 2026-11-15 |
| J.P. Morgan "The Agony and the Ecstasy" (2014-09-02) | Catastrophic-loss rates | https://www.chase.com/content/dam/privatebanking/en/mobile/documents/eotm/eotm_2014_09_02_agonyescstasy.pdf | 2026-11-15 |
| CRS RS21115 (2002-03-11) | Enron, ERISA 10% | https://www.everycrsreport.com/reports/RS21115.html | 2026-11-15 |
| FINRA "Concentrate on Concentration Risk" (2022-06-15) | Concentration risk | https://www.finra.org/investors/insights/concentration-risk | 2026-11-15 |
| RBI LRS FAQ (updated 2023-04-06) | 180-day rule | https://www.rbi.org.in/Scripts/FAQView.aspx?Id=115 | 2026-11-15 |
| RBI OI Master Direction (id=12380) | 90-day ODI rule | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12380 | 2026-11-15 |
| Finance (No.2) Bill 2024 memorandum | 12/24-month holding periods | https://www.indiabudget.gov.in/budget2024-25/doc/memo.pdf | 2026-11-15 |
| IBKR spot currency commissions | FX cost | https://www.interactivebrokers.com/en/pricing/commissions-spot-currencies.php | 2026-11-15 |
| iShares CSPX page | TER, domicile | https://www.ishares.com/uk/individual/en/products/253743/ishares-sp-500-b-ucits-etf-acc-fund | 2026-11-15 |
| Failed: Semantic Scholar (429), Investor.gov (403), SEC EDGAR full-text (403), Schwab/Kiplinger (404), Fidelity/Morningstar (403), Vanguard How America Saves PDF (no text), Bing (irrelevant), Wikipedia Lehman (no figure) | - | - | 2026-11-15 |
