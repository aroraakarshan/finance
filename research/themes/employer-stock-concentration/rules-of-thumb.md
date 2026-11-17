# Employer stock: rules of thumb

## Summary
Keep employer stock under about 10% of investments. Sell RSUs at vest and ESPP shares at purchase: the
value is already taxed as salary, so keeping them is the same as buying employer stock with your pay.
The US "qualifying disposition" rule does not apply to an Indian resident.
What to do: from now on sell every new MSFT vest and ESPP purchase at once ([plan.md](plan.md) tranche 0).

Back to the index: [employer-stock-concentration.md](../employer-stock-concentration.md). Written 2026-11-15 by `finance-research`;
research only, not advice; no orders placed. "not verified" = could not confirm from a source.

## Rules

| Rule | What it says and why | Source (checked) |
|---|---|---|
| **10% cap** | US law (ERISA) limits employer stock in a defined-benefit pension to 10% of plan assets so the pension does not fail with the company. Planners often apply the same 10% to a person's employer stock; a planner page saying so could not be fetched (Schwab/Morningstar/Fidelity pages 403/404), so "planner rule" is not verified. FINRA names company-stock concentration and correlated holdings (same industry) as main sources of concentration risk and says to diversify and rebalance; it gives no number | CRS RS21115 ([risk.md](risk.md)); FINRA "Concentrate on Concentration Risk" (2022-06-15), https://www.finra.org/investors/insights/concentration-risk (2026-11-15) |
| **Sell RSUs at vest** | At vest the full market value is already taxed in India as salary (that value is the Indian cost, as in `scripts.brokers.fidelity`/`etrade`). Keeping the shares is the same as taking the cash and buying the employer stock with it. Selling right after vest gives a gain close to zero | Own scripts |
| **ESPP: sell at purchase** | MSFT ESPP paid exactly 90% of the market value on the purchase day (e.g. $379.35 vs $421.50 on 2024-12-31), at quarter ends (2024-12-31, 2025-03-31, 2025-06-30). So: 10% discount, quarterly, no look-back seen. No purchase after 2025-06-30 in the files; whether you left the plan: not verified. Microsoft plan document: not fetched. Selling at purchase locks the discount (11.1% on the price paid) | Own data (Fidelity confirmations, `fidelity.purchases()`) |
| **"Qualifying disposition" does not apply** | It is a US tax rule for US taxpayers. A nonresident alien pays no US capital gains tax, so for an Indian resident only the Indian holding period matters | `tax/migration-indmoney-to-ibkr.md` 3.2, finance-tax, 2026-11-15 |
| **Staged selling** | Fixed amounts on fixed dates avoid trying to time the top; it is a behaviour aid, not a return advantage | - |
| **Job + stock risk** | Salary and 238 unvested MSFT shares already depend on Microsoft. A bad year for the company can hit job, bonus, unvested awards and held shares together (Enron case in [risk.md](risk.md)) | Award export; CRS RS21115 |
