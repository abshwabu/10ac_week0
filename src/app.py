import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets

import dask.dataframe as dd
import streamlit as st

@st.cache_data
def load_data_with_dask(file_path,):
    return dd.read_csv(file_path,on_bad_lines='skip')

news_df = load_data_with_dask(r'D:\projects\10ac_week0\data\data.csv')
metadata_df= load_data_with_dask(r'D:\projects\10ac_week0\data\domains_location.csv')



st.title("News Analysis Dashboard")

st.sidebar.title("Navigation")
# Display the datasets
st.header("News Data Overview")
st.write("Displaying the first few rows of the news dataset:")
st.dataframe(news_df.head())

st.write("Displaying the first few rows of the metadata dataset:")
st.dataframe(metadata_df.head())

# Display some summary statistics
st.header("Summary Statistics")
st.write(news_df.describe())
from sklearn.feature_extraction.text import TfidfVectorizer
from keybert import KeyBERT

# Keyword Extraction with TF-IDF
def extract_keywords_tfidf(data, column):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(data[column].fillna(""))
    keywords = vectorizer.get_feature_names_out()
    return keywords

# Streamlit UI for keyword extraction
st.header("Keyword Extraction")

method = st.selectbox("Select a method for keyword extraction", ["TF-IDF", "KeyBERT"])

if method == "TF-IDF":
    st.subheader("Keywords using TF-IDF")
    keywords = extract_keywords_tfidf(news_df, 'full_content')
    st.write(keywords)

elif method == "KeyBERT":
    st.subheader("Keywords using KeyBERT")
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(news_df['full_content'].dropna().iloc[0], keyphrase_ngram_range=(1, 2), stop_words='english')
    st.write(keywords)
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Topic Modeling with LDA
def lda_topic_modeling(data, num_topics=5):
    count_vectorizer = CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform(data['full_content'].fillna(""))

    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(count_data)

    return lda, count_vectorizer

st.header("Topic Modeling")

num_topics = st.slider("Number of Topics", 2, 10, 5)
lda_model, count_vectorizer = lda_topic_modeling(news_df, num_topics=num_topics)

# Display topics
st.write("Topics Identified:")
def display_topics(model, feature_names, num_top_words):
    topics = {}
    for topic_idx, topic in enumerate(model.components_):
        topics[topic_idx] = " ".join([feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]])
    return topics

topics = display_topics(lda_model, count_vectorizer.get_feature_names_out(), 10)
for topic_idx, topic in topics.items():
    st.write(f"**Topic {topic_idx}:** {topic}")
from sklearn.cluster import KMeans

def cluster_events(data, num_clusters=5):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(data['full_content'].fillna(""))

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    data['event_cluster'] = kmeans.labels_
    return data

st.header("Event Clustering")

num_clusters = st.slider("Number of Event Clusters", 2, 10, 5)
clustered_data = cluster_events(news_df, num_clusters=num_clusters)

st.write("Displaying event clusters:")
st.dataframe(clustered_data[['title', 'event_cluster']].head(10))
# Topic Trends Over Time
st.header("Topic Trends Over Time")

if st.checkbox("Show Topic Trends"):
    news_df['published_at'] = pd.to_datetime(news_df['published_at'])
    topic_trends = news_df.groupby([news_df['published_at'].dt.date, 'event_cluster']).size().unstack(fill_value=0)

    plt.figure(figsize=(10, 6))
    sns.heatmap(topic_trends.T, cmap='coolwarm')
    plt.title("Topic Trends Over Time")
    plt.xlabel("Date")
    plt.ylabel("Topic")
    st.pyplot(plt)
