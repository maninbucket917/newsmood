from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")

# Load the sentiment analysis module
sentiment_pipeline = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

LABELS = {
    "positive": "positive",
    "neutral": "neutral",
    "negative": "negative"
}

'''
analyze_article

Analyzes the sentiment of the given article text and returns a dictionary containing the sentiment label and score.
'''
def analyze_article(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")
    
    truncated_text = text[:512]  # Limit text to 512 characters

    result = sentiment_pipeline(truncated_text)[0]

    return {
        "label": LABELS.get(result["label"].lower()),
        "score": round(result["score"], 4)
    }