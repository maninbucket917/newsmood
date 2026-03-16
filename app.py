import streamlit as st
import plotly.graph_objects as go
from processor import process_articles

st.set_page_config(page_title="NewsMood", page_icon="📰", layout="wide")
st.title("NewsMood")
st.caption("A tool to analyze the sentiment of news articles.")

# Sidebar
with st.sidebar:
    st.header("Search Options")
    topic = st.text_input("Topic", placeholder="Enter a topic to search for...")
    max_results = st.slider("Max number of articles to search", min_value=5, max_value=50, value=20, step=5)
    search = st.button("Analyze", width='stretch')

# Main area
if search:
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        with st.spinner(f'Fetching and analysing articles about "{topic}"...'):
            try:
                results = process_articles(topic, max_results)
            except ValueError as e:
                st.error(str(e))
                st.stop()
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.stop()

        # Group articles by sentiment label
        grouped = {"positive": [], "negative": [], "neutral": []}
        for article in results:
            label = article["sentiment"]["label"]
            if label in grouped:
                grouped[label].append(article)

        # Sort each group by score descending and take top 3
        top = {
            label: sorted(articles, key=lambda x: x["sentiment"]["score"], reverse=True)[:3]
            for label, articles in grouped.items()
        }

        # Display donut chart + articles in two columns
        if not any(top.values()):
            st.warning("No results to display.")
        else:
            st.subheader(f'Sentiment breakdown for "{topic}"')

            col_chart, col_articles = st.columns([1, 1], gap="large")

            with col_chart:
                counts = {label: len(articles) for label, articles in grouped.items()}

                fig = go.Figure(go.Pie(
                    labels=[l.capitalize() for l in counts.keys()],
                    values=list(counts.values()),
                    hole=0.6,
                    marker_colors=["#278327", "#6b2018", "#1c6ba0"],
                    textinfo="label+percent",
                    hovertemplate="<b>%{label}</b><br>%{value} articles<br>%{percent}<extra></extra>"
                ))
                fig.update_layout(
                    showlegend=False,
                    height=400,
                    margin=dict(l=20, r=20, t=20, b=20),
                    annotations=[dict(
                        text=f"{len(results)}<br>articles",
                        x=0.5, y=0.5,
                        font_size=18,
                        showarrow=False
                    )]
                )
                st.plotly_chart(fig, width='stretch')

            with col_articles:
                st.subheader("Top articles by sentiment")

                badge_colors = {
                    "positive": "#278327",
                    "negative": "#6b2018",
                    "neutral":  "#1c6ba0"
                }

                for label in ["positive", "negative", "neutral"]:
                    if top[label]:
                        st.markdown(f"**{label.capitalize()}**")
                        for article in top[label]:
                            score = article["sentiment"]["score"]
                            color = badge_colors[label]
                            st.markdown(
                                f'- [{article["title"]}]({article["url"]}) '
                                f'— *{article["source"]}* '
                                f'<span style="background-color:{color}; color:white; '
                                f'padding:1px 6px; border-radius:8px; font-size:0.75em;">'
                                f'{score:.0%}</span>',
                                unsafe_allow_html=True
                            )