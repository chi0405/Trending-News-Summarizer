import streamlit as st
import requests
from newsapi import NewsApiClient
from newspaper import Article

news_api_key = "News API key"  # Replace with your News API key
newsapi = NewsApiClient(api_key=news_api_key)

# Create a Streamlit web app
st.title("Trending News and Summaries")

# Define a function to fetch trending news
def get_trending_news():
    top_headlines = newsapi.get_top_headlines(language="en", country="us")
    articles = top_headlines["articles"]
    return articles

# Fetch trending news
trending_news = get_trending_news()

# Display trending news
st.header("Trending News")

for idx, article in enumerate(trending_news, 1):
    st.subheader(f"News #{idx}: {article['title']}")
    st.write(article['description'])
    st.write(f"Source: {article['source']['name']}")
    st.write(f"Published at: {article['publishedAt']}")
    st.write(f"URL: {article['url']}")
    st.write("")


# Select a news article to summarize
selected_article = st.selectbox("Select an article to summarize:", [article['title'] for article in trending_news])

# Summarize the selected article
for article in trending_news:
    if article['title'] == selected_article:
        st.header(f"Summary of '{article['title']}'")
        news_url = article['url']
        news_article = Article(news_url)
        news_article.download()
        news_article.parse()
        summarized_text = news_article.summary
        st.write(summarized_text)


# Run the Streamlit app
if __name__ == "__main__":
    st.set_option('deprecation.showfileUploaderEncoding', False)
