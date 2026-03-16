from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

'''
get_articles

Returns a list of articles from the News API based on the given query and max results.
'''
def get_articles(query: str, max_results: int = 20) -> list[dict]:
    if max_results < 1:
        raise ValueError("max_results must be at least 1")
    
    api = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))

    response = api.get_everything(
        q = query,
        language = "en",
        sort_by = "relevancy",
        page_size = 100
    )

    articles = []

    # Scan the page to skip entries with no titles or removed content and stop once enough articles are collected
    for article in response.get("articles", []):
        if len(articles) >= max_results:
            break

        title = (article.get("title") or "").strip()
        description = (article.get("description") or "").strip()
        url = (article.get("url") or "").strip()
        source = (article.get("source", {}).get("name") or "").strip()

        is_removed = title.lower() == "[removed]" or description.lower() == "[removed]"
        if not title or not url or is_removed:
            continue

        articles.append({
            "title": title,
            "description": description,
            "url": url,
            "source": source
        })

    return articles