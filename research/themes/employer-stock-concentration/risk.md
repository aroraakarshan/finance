# Employer stock: risk facts

## Summary
QCOM fell 44% and MSFT 37% in the last 10 years (both bottomed on 2022-11-03); in 2000-2002 QCOM fell 87%
and took until 2014 to recover. Studies show most single stocks lag T-bills and about 40% suffer a lasting
70%+ fall. Holding your employer's stock ties savings to the same risk as your job.
What to do: treat the QCOM + MSFT block (43.1% of the Rs 4.21 Cr total, 79.8% of the broker accounts; 2026-11-15) as the main risk; see [plan.md](plan.md).

Back to the index: [employer-stock-concentration.md](../employer-stock-concentration.md). Written 2026-11-15 by `finance-research`;
research only, not advice; no orders placed. "not verified" = could not confirm from a source.

## Drawdowns and volatility

Own calculation, yfinance dividend-adjusted daily closes 2016-11-14 to 2026-11-13 (run 2026-11-15):

| | Max drawdown (peak -> trough) | Back to peak | Volatility (yearly) | Worst 1-year | CAGR |
|---|---|---|---|---|---|
| QCOM | -44.3% (2021-12-15 -> 2022-11-03) | 2024-05-02 | 40.4% | -40.9% | 13.1% |
| MSFT | -37.1% (2021-11-19 -> 2022-11-03) | 2023-06-15 | 27.9% | -35.3% | 26.1% |
| SOXX (semis ETF) | -45.8% | 2023-12-13 | 35.5% | -37.8% | 29.3% |
| SPY (S&P 500) | -33.7% (Covid 2020) | 2020-08-10 | 18.0% | -19.7% | 15.1% |
| URTH (MSCI World) | -34.0% (Covid 2020) | 2020-08-24 | 17.3% | -22.1% | 13.1% |

Longer history (yfinance, full series to 2026-11-13):

| Stock | Max drawdown | Peak -> trough | Back to peak |
|---|---|---|---|
| QCOM | -86.8% | 2000-01-03 -> 2002-08-05 | 2014-03-18 |
| MSFT | -69.4% | 1999-12-27 -> 2009-03-09 | 2014-07-16 |

Daily-return correlation 2016-2026 (same yfinance data):

| Pair | Correlation |
|---|---|
| QCOM-MSFT | 0.46 |
| QCOM-SOXX | 0.74 |
| MSFT-SPY | 0.76 |

The two employer stocks do not hedge each other; both fell to a low on the same day (2022-11-03).

## Evidence on single-stock and employee-stock risk

| Study / case | Finding | Source (checked) |
|---|---|---|
| Bessembinder, "Do stocks outperform Treasury bills?", Journal of Financial Economics 129(3), 2018, 440-457, DOI 10.1016/j.jfineco.2018.06.004 | Most US stocks in CRSP since 1926 had lifetime returns below one-month T-bills; the best 4% of companies explain the whole net gain of the US market | Abstract via RePEc, https://ideas.repec.org/a/eee/jfinec/v129y2018i3p440-457.html (2026-11-15) |
| J.P. Morgan "Eye on the Market: The Agony and the Ecstasy" (2014-09-02, date from file name) | Of about 13,000 Russell 3000 stocks 1980-2014, about 40% had a "catastrophic loss" (fell 70%+ from peak and stayed 60%+ below); Information Technology 57%. Median stock's lifetime return vs the Russell 3000: -54%; two-thirds underperformed | https://www.chase.com/content/dam/privatebanking/en/mobile/documents/eotm/eotm_2014_09_02_agonyescstasy.pdf (2026-11-15) |
| Longboard's similar study | Not fetched (not verified) | - |
| Enron | 62% of the assets of Enron's 401(k) plan were Enron stock on 2000-12-31; the share went from over $80 (Jan 2001) to under 70 cents (Jan 2002) | CRS report RS21115, P. Purcell, 2002-03-11, https://www.everycrsreport.com/reports/RS21115.html (2026-11-15) |
| Lehman Brothers | Employees were large holders and lost job and savings together (widely reported); an exact ownership figure was not found (not verified) | - |
| Benartzi, "Excessive Extrapolation and the Allocation of 401(k) Accounts to Company Stock", Journal of Finance 56(5), 2001, 1747-1764, DOI 10.1111/0022-1082.00388 | About a third of large-plan assets were in company stock; employees put more in after good past returns (39.7% vs 10.4%), but those allocations did not predict future returns | Crossref abstract (2026-11-15) |
| "Company Stock, Market Rationality, and Legal Reform" (2004, DOI 10.2139/ssrn.573504; authors not verified) | Job and company stock are correlated; for a long-tenure worker a dollar of company stock may be worth under 50 cents after risk | Crossref abstract (2026-11-15) |
