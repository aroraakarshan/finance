# News and sentiment sources

Checked 2026-11-15.

## Summary
- Add the free **NSE announcement RSS** feeds for India filings (poll daily: each holds about one day).
- Keep Google and Bing News RSS; GDELT is a free no-key backup (rate limited today).
- Paid APIs (Finnhub, Marketaux, Alpha Vantage, NewsAPI) are US-centric or too small free.
- FinBERT: local, non-commercial licence; use on headlines as one input only.

Back to the index: [libraries-and-news.md](../libraries-and-news.md).

## 2. News and sentiment sources

| Source | Cost / limits | India | Quality, delay, history | Credentials | Fit |
|---|---|---|---|---|---|
| NSE announcement RSS | free | NSE only | Primary filings; live (lastBuildDate 13:25 IST today, ttl 5 min); 79 items in main feed | none | 5 |
| BSE notices RSS | free | BSE | Exchange notices (bulletins), 26 items; company announcement API blocked | none | 2 |
| Google News RSS | free | yes | Already our best route (sources.md score 5); link decoding can 429 | none | 5 |
| Bing News RSS | free | yes | Direct links, backup when Google 429s (sources.md 5) | none | 5 |
| GDELT DOC 2.0 API | free | yes (`sourcecountry:IN`) | Global, 3-month rolling window, tone histograms, up to 250 articles/query; limit 1 request per 5 s | none | 3 |
| Finnhub | free key; sentiment premium | no for company news | `/company-news` "only available for North American companies", free tier 1 year history; `/news-sentiment` US only and "Premium Access Required" | API key (env var) | 2 |
| Marketaux | free 100 req/day, 3 articles/request; $29/month 2,500/day 20 articles; $49, $99, $199 tiers | claims 80+ markets; NSE depth not verified | Entity tagging + sentiment per entity | API key | 2 |
| Alpha Vantage NEWS_SENTIMENT | now labelled Premium in docs; free key 25 req/day; premium $49.99-$249.99/month | not verified | Per-ticker sentiment score with bands; `demo` key result for AAPL started with an irrelevant tokenised-stock page (noisy) | API key | 2 |
| NewsAPI.org | Developer free: 24 h delay, 1 month back, 100 req/day, dev/testing only; Business $449/month | not verified | General news, no sentiment | API key | 1 |
| FinBERT (ProsusAI/finbert) | free, runs locally (BERT-base, CPU ok) | English text only | 3 labels pos/neg/neutral; trained on Financial PhraseBank (2014 sentences); no support or updates promised | none | 3 |

Sources: NSE https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml (also
`Financial_Results.xml`, `Board_Meetings.xml`, `Corporate_action.xml`, `Insider_Trading.xml`
all HTTP 200; needs a browser User-Agent); BSE https://www.bseindia.com/data/xml/notices.xml
(works) and api.bseindia.com AnnSubCategoryGetData (403 Access Denied); GDELT docs
https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/ (4 live queries all got the
"one request every 5 seconds" message, so no result rows verified today); Finnhub
https://finnhub.io/static/swagger.json (pricing page is JavaScript, free-tier rate not
verified); Marketaux https://www.marketaux.com/pricing; Alpha Vantage
https://www.alphavantage.co/documentation/ and https://www.alphavantage.co/premium/; NewsAPI
https://newsapi.org/pricing; FinBERT https://huggingface.co/ProsusAI/finbert (GitHub
ProsusAI/finBERT: 2282 stars, 8 open issues, Apache-2.0 code, push 2026-10-12).

FinBERT details: model weights are **CC BY-NC-SA 4.0 (non-commercial only)**; code is
Apache-2.0. Personal research use fits the licence. Limits: trained on short English news
sentences, so it misreads Indian corporate-filing language, sarcasm, numbers ("profit down
2% vs expected 10% drop" reads negative) and long articles (512-token cap). Use on headlines
only, as one input to our -2..+2 score, never as the score itself. Would need `transformers`
+ `torch` in a separate venv (large install; not done).

Update 2026-11-15 (finance-scout feed test, scout/sources-notes.md): all NSE RSS feeds return HTTP 200, but each holds only about the last day, so a weekly scan needs daily polling or the NSE filing pages; the insider-trading RSS stops at 2 May 2026 (insider data moved to the XBRL feed api/corporates-pit-gg) and the financial-results RSS is sparse (3 items, newest 3 Nov).
