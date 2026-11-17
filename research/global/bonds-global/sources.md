# Global bonds: sources

Back to [Global bonds index](../bonds-global.md).

## Summary
- All sources read 2026-11-15; central banks and FRED for yields, justETF for fund data, JPM/Vanguard/AQR for forecasts.

## Sources (read 2026-11-15)

- [F] FRED CSV https://fred.stlouisfed.org/graph/fredgraph.csv?id=<id>: IRLTLT01{GB,DE,JP,AU,CA}M156N, DGS10/2/3MO, DFII10, BAML* (ICE)
- [BoE] BoE IADB IUDSNZC/IUDMNZC/IUDLNZC (5/10/20y nominal), IUDMRZC (10y real): https://www.bankofengland.co.uk/boeapps/database/
- [BB] Bundesbank API, BBSIS ...R02XX/R10XX/R30XX: https://api.statistiken.bundesbank.de/rest/data/BBSIS/
- [MoF] Japan MoF JGB curve: https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv
- [BoC] Bank of Canada Valet BD.CDN.{2YR,10YR,RRB}.DQ.YLD: https://www.bankofcanada.ca/valet/
- [J] justETF profiles by ISIN (fund size in EUR, data 2026-11-15): https://www.justetf.com/en/etf-profile.html?isin=<ISIN>
- [Y] Yahoo Finance via yfinance (IB01.L, AGGU.L, AGGG.L, ITPS.L, LQDE.L, IHYU.L, IEMB.L, SEML.L, GBPUSD=X)
- [JPM] https://www.prnewswire.com/news-releases/jp-morgan-releases-2027-longterm-capital-market-assumptions-projecting-7-0-return-for-6040-portfolio-over-10-15-years-302912421.html
- [V] https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html
- [AQR] https://www.aqr.com/Insights/Research/Alternative-Thinking/2026-Capital-Market-Assumptions-for-Major-Asset-Classes (PDF)
- Tax lines: tax/investment-types.md sections 0-1.
