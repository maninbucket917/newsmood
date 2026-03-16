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
        page_size = max_results
    )

    articles = []

    # Scan through the articles and extract relevant information for each article
    for article in response["articles"]:
        title = article.get("title") or ""
        description = article.get("description") or ""
        url = article.get("url") or ""

        # Skip articles with missing titles
        if not title:
            continue

        articles.append({
            "title": title,
            "description": description,
            "url": url,
            "source": article.get("source", {}).get("name", "")
        })

    return articles