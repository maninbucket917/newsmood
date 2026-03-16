# NewsMood

A news sentiment analysis tool built with Streamlit, HuggingFace Transformers, and NewsAPI. Enter a topic to see the overall sentiment of recent news articles, as well as the top headlines driving those sentiments.

NewsMood fetches recent news articles on a topic of your choice and runs each one through a machine learning sentiment model. Results are displayed as a donut chart showing the overall sentiment breakdown, along with the top articles per category with confidence scores.

## Technologies

- **[Streamlit](https://streamlit.io)** - Web UI
- **[HuggingFace Transformers](https://huggingface.co)** - Sentiment analysis performed by `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **[NewsAPI](https://newsapi.org)** - News article fetching
- **[Plotly](https://plotly.com)** - Donut chart visualisation

## Installation

1. Clone the repo and navigate into it:
    ```bash
    git clone https://github.com/maninbucket917/newsmood.git
    cd newsmood
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add:
    ```
    NEWS_API_KEY=your_newsapi_key_here
    HF_TOKEN=your_huggingface_token_here  # optional
    ```
    Get a free NewsAPI key at [newsapi.org](https://newsapi.org). HuggingFace token is optional but removes rate limit warnings.

## Usage

```bash
streamlit run app.py
```

Then open your browser, enter a topic in the sidebar, and hit **Analyze**.