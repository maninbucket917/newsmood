from news_client import get_articles
from analyzer import analyze_article

'''
process_articles

Processes articles based on the given query and max results, returning a list of dictionaries containing article information and sentiment analysis results.
'''
def process_articles(query: str, max_results: int = 20) -> list[dict]:
    articles = get_articles(query, max_results)

    results = []

    for article in articles:
        # Combine the title and description for sentiment analysis
        text = f"{article['title']} {article['description']}"
        sentiment = analyze_article(text)

        results.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "source": article["source"],
            "sentiment": sentiment
        })

    return results