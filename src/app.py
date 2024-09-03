import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('../src'))

from preprocessing import merge_datasets
from keyword_extraction import extract_keywords_tfidf
from topic_modeling import lda_topic_modeling
from event_clustering import cluster_events

# Load data from CSVs
@st.cache_data
def load_datasets():
    data = pd.read_csv('data/data.csv')
    domain_location = pd.read_csv('data/domains_location.csv')
    return data, domain_location

data_df, domain_location_df = load_datasets()

# Merge datasets
merged_df = merge_datasets(data_df, domain_location_df)

st.title("News Analysis Dashboard")

st.sidebar.title("Navigation")

# Display the merged dataset
st.header("Merged Data Overview")
st.write("Displaying the first few rows of the merged dataset:")
st.dataframe(merged_df.head())

# Keyword extraction
if st.sidebar.checkbox("Keyword Extraction"):
    st.subheader("Keyword Extraction")
    method = st.selectbox("Select a method for keyword extraction", ["TF-IDF"])
    if method == "TF-IDF":
        keywords = extract_keywords_tfidf(merged_df, 'full_content')
        st.write("Extracted Keywords:")
        st.write(keywords)

# Topic modeling
if st.sidebar.checkbox("Topic Modeling"):
    st.subheader("Topic Modeling")
    num_topics = st.slider("Number of Topics", 2, 10, 5)
    lda_model, count_vectorizer = lda_topic_modeling(merged_df, num_topics=num_topics)
    st.write("Topic Modeling Results:")
    st.write(f"LDA Model with {num_topics} topics created.")

# Event Clustering
if st.sidebar.checkbox("Event Clustering"):
    st.subheader("Event Clustering")
    num_clusters = st.slider("Number of Event Clusters", 2, 10, 5)
    clustered_data = cluster_events(merged_df, num_clusters=num_clusters)
    st.write("Event Clustering Results:")
    st.dataframe(clustered_data[['title', 'event_cluster']].head(10))
