from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def lda_topic_modeling(data, num_topics=5):
    """Perform LDA topic modeling."""
    count_vectorizer = CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform(data['full_content'].fillna(""))
    
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(count_data)
    
    return lda, count_vectorizer
