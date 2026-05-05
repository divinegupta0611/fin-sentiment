import feedparser

def fetch_company_news(company_name, limit=5):
    query = company_name.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}+stock+OR+business"
    feed = feedparser.parse(url)
    news_list = []
    for entry in feed.entries[:limit]:
        news_list.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return news_list
