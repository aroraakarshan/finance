# Silver and gold: what changed between versions

## Summary
- Your decision 16 Nov: sell all silver (ABSL too) and no extra gold; GOLDIETF Rs 1,97,734 only; gold 3.53%, silver 0%.
- First version used AngelOne as the base; on the total, metals are below the guideline, so the Rs 5 L cut was withdrawn.
- Tax figures replaced by the finance-tax lot-level note; ABSL trim dropped (FIFO gain).

Back to the index: [silver-gold](../silver-gold.md). Written 2026-11-15 by `finance-research`, updated 2026-11-15 (see "What changed"). Total-based shares as of `portfolio/summary.md` commit 1a65a2e (2026-11-15; total Rs 2,83,13,674 incl. HDFC savings and FDs; US at 13 Nov close, USD/INR 94.0338). Research only, not advice; no orders placed. "Checked" = date the source was read. "not verified" = could not confirm.

## What changed in the 2026-11-15 update
- **Total re-based again (summary.md commit 1a65a2e):** total Rs 2,83,13,674 (was Rs 2,26,82,726); adds HDFC
  savings Rs 8,54,314 (13 Nov) and 9 FDs Rs 47,76,634 principal (6.25%, 10 May 2026 -> 10 May 2027). Metals
  2.93% of total, QCOM+MSFT 63.9%. Amounts kept: gold target Rs 11.3 L is now 4.0% of total (not 5%), metals
  target Rs 15.5 L is 5.5%. Conclusion unchanged (metals further below guidance); one change: option C can be
  funded from savings/FDs in India instead of repatriated QCOM proceeds.
- **Total re-based (summary.md commit 21a4c78):** total Rs 2,26,82,726 (was Rs 2,23,19,002); US $213,304
  (was $209,436; INDmoney now $14,653 incl. wallet cash $4,574.05). AngelOne unchanged. All "% of total"
  recomputed; shifts are under 0.1 point and no conclusion changes.
- **Denominator.** The first version compared metals with AngelOne (Rs 26.25 L) and assumed only ~$15k in
  the US. `portfolio/summary.md` (2026-11-15) puts total investments at **Rs 2,26,82,726** (US $213,304 x
  94.0338 + AngelOne Rs 26,24,910). Metals are 31.6% of AngelOne but only **3.7% of total**. Every share
  below now shows both bases.
- **Conclusion reversed on size.** Against the 7.5-15% gold guideline (WGC) on the whole portfolio, metals
  are *below* range, not 2-4x above it. The problem is the mix (88% silver, gold 0.43% of total) and four
  overlapping products, not the amount. The old "cut to Rs 5 L" (= 2.2% of total) is withdrawn.
- **New proposal (conditional).** Merge into ABSL Silver ETF + one gold ETF at the same size, then build
  gold toward ~5% of total. With QCOM/MSFT at ~80% of total, gold (correlation ~0.08 with both) is the
  diversifier; funding beyond today's metals depends on the employer-stock plan (proceeds stay abroad).
- **Tax.** Replaced my estimates with `tax/angelone-metals-and-mf-exits.md` (lot-level, by `finance-tax`):
  unrealised loss about **-Rs 81,600** at 13 Nov prices (not -Rs 64,000); all lots bought 2025-11-10 to
  2026-11-02, so dates are now known; a new loss saves only **14.95%**, about Rs 9,900 at most this year.
- **ABSL trim dropped.** The tax note shows a partial ABSL sale is not "about no gain/loss": FIFO sells
  the cheap lots first (+Rs 2,925). The new proposal keeps ABSL whole.
- **Decided 2026-11-15 (user via finance-main):** gold target = 5% of total (~Rs 14.2 L at Rs 2,83,13,674),
  i.e. ~Rs 10.1 L on top of the ~Rs 4.07 L merge proceeds; ETF = GOLDIETF; funded by the HDFC savings surplus
  (Rs 2.54 L, Nov-Dec 2026) and the 10 May 2027 FD maturity (Rs 7.55 L, May-Jul 2027). Replaces the Rs 11.3 L
  (4.0%) gold target. Metals target now ~Rs 18.4 L = 6.5% of total. Gold-buy tax added from finance-tax (options-and-proposal.md s8).
- **Recomputed 2026-11-15 with physical gold; the user decided 5% incl. physical** (summary.md commit 7d88cf8,
  total Rs 2,97,58,520; physical gold 79.56 g 22K + 29.50 g 18K = Rs 12,90,192, IBJA 13 Nov). Target
  Rs 14,87,926; gap Rs 1,97,734 to GOLDIETF from the merge; the other ~Rs 1,94,466 proposed for Kotak
  Arbitrage then UTI Nifty 50. Savings (Rs 2.54 L) and FD (Rs 7.55 L) gold tranches removed. Metals after the
  plan 6.42% of total (gold 5.00%, silver 1.42%). The FD-interest tax line was dropped with the FD tranches.
- **Re-based to Rs 4,20,97,035 (summary.md commit 0dd3a98 and later; adds Punjab Gramin Bank FDs Rs 72 L and
  savings Rs 10 L, both estimates, and EPF Rs 41,03,127, locked).** The user decided 15 Nov: gold stays at 5% of
  the new total incl. physical = Rs 21,04,852, so GOLDIETF Rs 8,14,660 in all: Rs 1,97,734 from the silver merge
  (18 Nov - 9 Dec) + ~Rs 6,16,926 from PGB savings (15 Dec 2026, 15 Jan 2027). Rest of the merge (~Rs 1,94,466)
  to Kotak Arbitrage then UTI Nifty 50: decided then, withdrawn 16 Nov (see below). Metals now 5.04%, after the plan 6.01%
  (gold 5.00%, silver 1.01%); QCOM+MSFT 43.1%. Conclusion: same target share, larger GOLDIETF amount.
- **Your decision 16 Nov (portfolio/decisions.md row 11; plan.md; targets.md line 24; commit f2e4c6c):** no extra
  gold: the ~Rs 6,16,926 of GOLDIETF from Punjab Gramin Bank savings (15 Dec 2026, 15 Jan 2027) and the 5% target
  (Rs 8,14,660 of GOLDIETF) are dropped; gold target about 3.5% of total (jewellery + GOLDIETF), band 3-6%, no
  top-ups, no gold from the maturing FDs. The silver-to-gold swap stays: GOLDIETF 2 x Rs 98,867 = Rs 1,97,734.
  Also: sell ALL silver incl. the ABSL Silver ETF (whole holding, Wed 18 Nov; net ~-Rs 13,216; tax pending
  finance-tax); its money: pending user decision (one combined choice for the unassigned money).
  The "keep ABSL whole" line and the FIFO-trim point are gone. Metals after the plan: Rs 14,87,926 = 3.53%
  (gold only; silver 0%).
- **Correction 16 Nov (finance-main):** the ABSL money (~Rs 4.23 L) and the rest of the silver money (~Rs 1.94 L)
  have no destination yet; with the unassigned HDFC savings (~Rs 10.5 L) they are one pending user decision (one combined choice for the unassigned money).
  No Kotak Arbitrage then UTI Nifty 50 route (no parking plus monthly manual moves).
