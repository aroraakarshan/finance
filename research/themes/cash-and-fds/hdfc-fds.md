# HDFC FDs: break early or wait to 10 May 2027 (2026-11-15)

## Summary
- HDFC pays 1% less than the booking-date rate for the period actually held if an FD is broken (rule for deposits under Rs 3 Cr).
- Breaking the 9 FDs now gains at most ~Rs 6,000 (SFBs, ~10 new banks) and can lose ~Rs 28,000 after tax: wait to 10 May 2027.
- One FD (Rs 5.31 L) can be broken alone for an urgent need, at about Rs 3,700-5,100 of interest before tax.
- The general rule for any FD (also PGB) is in [pgb.md](pgb.md) section 2.

Back to the index: [cash-and-fds](../cash-and-fds.md). Research only, not advice; no orders. User: 35.88% slab, new regime; after tax at slab = yield x 0.6412. "nv" = not verified.

## Break or wait

HDFC rule for deposits under Rs 3 Cr booked after 22 Jul 2023 (HDFC FD rate page, rates from 4 Nov 2026, read 2026-11-15). On premature withdrawal, including sweep-in or partial withdrawal, the rate is "1% lower" than the rate on the booking date for the period actually held, not the contracted rate.

- Breaking on 17 Nov 2026 means 191 days held, so the "6 months 1 day to 9 months" bucket applies. That bucket's rate on 10 May 2026 is nv. Today it is 5.65% (from 4 Nov 2026), so the break rate is about 4.65% (scenarios 4.40-4.90%). After a break there would be 174 days left to 10 May 2027.

| Per FD (Rs 5,30,737 principal) | Book rate 5.40% (break 4.40%) | 5.65% (4.65%) | 5.90% (4.90%) |
|---|---|---|---|
| Interest paid on break | Rs 12,198 | Rs 12,896 | Rs 13,594 |
| Interest lost vs 6.25% contract for 191 days (before tax) | ~Rs 5,100 | ~Rs 4,400 | ~Rs 3,700 |
| Switch to arbitrage (6.71%, 23.92% tax): gain or loss vs waiting, after tax | -Rs 738 | -Rs 274 | +Rs 191 |
| Switch to liquid fund (6.53%, slab) | -Rs 3,114 | -Rs 2,653 | -Rs 2,191 |
| Switch to 182-day T-bill (6.52%, slab) | -Rs 3,131 | -Rs 2,669 | -Rs 2,208 |
| Switch to an SFB FD at 8.25% (only if that rate applied to 174 days; it is for selected longer tenors) | -Rs 260 | +Rs 205 | +Rs 670 |
| All 9 FDs into arbitrage | -Rs 6,644 | -Rs 2,466 | +Rs 1,715 |
| All 9 FDs into liquid / T-bill | -Rs 28,000 | -Rs 24,000 | -Rs 20,000 |
| All 9 FDs into SFB FDs at 8.25% (needs ~10 SFBs to stay inside DICGC) | -Rs 2,336 | +Rs 1,847 | +Rs 6,034 |

Method (computed 2026-11-15). Waiting gives Rs 5,64,693 per FD, and its interest is taxed at slab. Breaking gives principal plus interest at the break rate (2 quarters compounded plus 7 days), taxed at slab. That amount is then reinvested for 174 days at the switch rate after its own tax. Arbitrage returns are trailing, not promised.

- **Wait:** at best a switch gains about Rs 6,000 on Rs 47.8 L (SFBs, ~10 new banks), and usually loses.
- **Partial break:** the 9 deposits are separate, so one FD can be broken for an urgent need. That costs about Rs 3,700-5,100 of interest before tax (Rs 2,400-3,300 after tax).
- **Sweep-in:** a sweep-in withdrawal is charged the same 1% penalty (HDFC page, note 1). The same page (note 4) says "partial withdrawal and sweep-in facility is not allowed (except for amounts greater than or equal to 25 crs)". Whether that note covers deposits under Rs 3 Cr is unclear. Whether these 9 FDs are linked to savings as sweep-in is also nv. Check in NetBanking.
- **Before 10 May 2027:** decide where the Rs 50.82 L goes ([proposal.md](proposal.md)). Do not let it auto-renew by default; the auto-renew setting is nv.
