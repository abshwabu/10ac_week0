from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

def cluster_events(data, num_clusters=5):
    """Cluster news articles based on events."""
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(data['full_content'].fillna(""))
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)
    
    data['event_cluster'] = kmeans.labels_
    return data
