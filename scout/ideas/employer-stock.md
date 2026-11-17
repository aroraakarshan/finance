# Idea 1. Reduce employer-stock concentration - DECIDED (2026-11-15)

## Summary
- DECIDED by the user 2026-11-15 (`portfolio/decisions.md` lines 16-19; steps in `portfolio/plan.md`
  sections 2-3, 2026-11-15):
  - QCOM: keep about 134 shares (about 7% of the total); sell about 430 (432) in Nov-Dec 2026, after the
    CA confirms the lot choice and before QCOM's results (about 3 Feb 2027), and 195 in Apr 2027 (627 in all).
  - MSFT: sell each vested lot on its long-term date (2027-01-01 to 2028-09-01) and every new vest at
    once; vested MSFT goes to 0 by Sep 2028.
  - ESPP at 15% of pay from the 1 Jan 2027 offering, each purchase sold the same day, dollars to IBKR
    (enrolled 2026-11-15).
  - Every QCOM/MSFT sale and ESPP purchase is split inside IBKR in USD: EXUS 45%, IJPA 10%, XDEW 10%,
    AVGS 15%, XDWH 5%, XDW0 5%, FLXC 3%, Latin America 2%, USD cash or IB01 5%.
- Japan/HK names with lots above Rs 40k are long-term buys, not trades: `AGENTS.md` "Trading rules"
  (trading rules cover only the Rs 2 L budget, one position at most 20% = Rs 40k; long-term buys follow
  `portfolio/plan.md`).
- Basis: research `research/themes/employer-stock-decision/qcom-msft.md`, `.../espp.md`,
  `research/themes/employer-stock-concentration/plan.md`; tax `tax/employer-stock.md` (all QCOM about
  Rs 5.66 L tax whenever sold; holding MSFT lots to long-term saves about Rs 1.56 L).
- QCOM and MSFT are 60.8% of the Rs 2,97,58,520 total today (`research/themes/employer-stock-concentration.md` s1).

## Details
- Situation (`portfolio/summary.md` (2026-11-15); shares: `research/themes/employer-stock-concentration.md` s1, restated on Rs 2,97,58,520; scout
  arithmetic matches): QCOM $131,250 = 41.5%, MSFT $61,235 = 19.3%, together 60.8% of the total;
  semiconductors (QCOM, AVGO, NVDA) 43.0%; US tech (QCOM, MSFT, AVGO, NVDA, CRWD, IONQ, SHLS, GOOGL)
  64.0%; US single stocks 65.7%. Of market investments only (without HDFC bank cash and physical gold):
  54.4% / 25.4% / 79.8% / 56.4% / 84.0% / 86.2%. The fall comes only from the larger total: the QCOM
  and MSFT dollar values are unchanged, and the bank cash is mostly locked in FDs to 2027-05-10.
  Unvested MSFT adds about 238 shares gross (same note).
- Idea (now decided, see Summary): a staged move out of QCOM first, keep each existing MSFT lot until it turns long-term, sell
  new MSFT vests at vest, and hold the proceeds in Irish accumulating UCITS ETFs at IBKR. This changes
  the domicile (not US-situs) and the single-stock risk; it does not remove USD/INR risk.
- Research basis: `research/themes/employer-stock-concentration.md` s5 (staged proposal, reconciled
  with the tax note); `research/themes/investment-universe.md` s3 item 1; `research/themes/ibkr-global.md`
  s3.2 (UCITS facts, LRS allowed).
- Tax basis: `tax/employer-stock.md` (finance-tax, 2026-11-15, uncommitted; supersedes
  `tax/investment-types.md` s5): all QCOM about Rs 5.66 L tax (LT 14.95%); MSFT lots held to long-term save
  about Rs 1.56 L; ESPP restart about 7.1% net. `tax/investment-types.md` s1 (UCITS), s7.
- Still open for the execution (the decision itself is made):
  - CA: specific-lot choice vs first in, first out for QCOM at IBKR (s5.2 item 1, s7 item 3).
  - QCOM Indian cost method. Proposed: $141.86/share (method A, market value at each vest, each
    sell-to-cover matched to its own vest; now used by `etrade.transfers()` per `STATUS.md`). Earlier
    snapshot: $143.91 (first in, first out across vests). IBKR shows $133.55 (US basis, ESPP at price
    paid). The method difference is explained but not validated: needs CA plus IBKR lot reports. The
    $141.86 figure is cited only with that flag.
  - Form 16 perquisite values instead of yfinance FX (s7 item 4); all FX in the tax note is
    approximate, not SBI TT rates.
  - Fidelity statements Jan-Jun 2025 (`STATUS.md` Next 5).
  - CA: no deemed income on accumulating UCITS (s7 item 7).
  - These sales are the user's decided long-term rebalance (user places the orders), not trading-budget
    trades under the paper-trading rules. IBKR entity and cash/margin account type (user).
- Not copied here: the lot-by-lot tranche tables (research plan.md, tax/employer-stock.md).
- Not part of this idea: bond UCITS, US money market funds (possibly always short-term at 35.88%,
  AF s.76; `tax/investment-types.md` s0 item 1).

Back to [Ideas](../ideas.md).
