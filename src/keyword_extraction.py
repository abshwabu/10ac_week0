from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords_tfidf(data, column):
    """Extract keywords using TF-IDF."""
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform(data[column].fillna(""))
    keywords = vectorizer.get_feature_names_out()
    return keywords
