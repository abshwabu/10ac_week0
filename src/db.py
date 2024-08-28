import psycopg2
from sqlalchemy import create_engine
import pandas as pd

# Set up the connection string
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = 'localhost'
USER = 'postgres'
PASSWORD = '123456'
PORT = 5432
DATABASE = 'modeldb'

# Create an engine and connect to the PostgreSQL database
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

# Load CSV data into a DataFrame
news_df = pd.read_csv(r'D:\projects\10ac_week0\data\data.csv')

# Print the column names and the first few rows of the DataFrame
print("Columns in DataFrame:", news_df.columns)
print("First few rows of DataFrame:")
print(news_df.head())

# Remove rows where 'source_id' is NaN
news_df = news_df.dropna(subset=['source_id'])

# Connect to the 'modeldb' database using psycopg2
conn = psycopg2.connect(
    dbname="modeldb",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# SQL command to drop the 'articles' table if it exists
drop_articles_table = "DROP TABLE IF EXISTS articles CASCADE;"
cursor.execute(drop_articles_table)
conn.commit()
print("Articles table dropped successfully.")

# SQL command to drop the 'sources' table if it exists
drop_sources_table = "DROP TABLE IF EXISTS sources;"
cursor.execute(drop_sources_table)
conn.commit()
print("Sources table dropped successfully.")

# SQL command to create the 'sources' table with a primary key
create_sources_table = """
CREATE TABLE sources (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255) NOT NULL
);
"""

# Execute the SQL command
cursor.execute(create_sources_table)
conn.commit()
print("Sources table created successfully.")

# SQL command to create the 'articles' table
create_articles_table = """
CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,
    source_id INTEGER REFERENCES sources(source_id) ON DELETE CASCADE,
    title TEXT,
    description TEXT,
    url TEXT,
    published_at TIMESTAMP,
    content TEXT,
    category VARCHAR(255),
    full_content TEXT
);
"""

# Execute the SQL command
cursor.execute(create_articles_table)
conn.commit()
print("Articles table created successfully.")

# Close the connection
cursor.close()
conn.close()

# Prepare the 'sources' DataFrame
if 'source_name' in news_df.columns:
    sources_df = news_df[['source_name']].drop_duplicates()
else:
    print(f"Warning: 'source_name' column is missing from the DataFrame. Existing columns: {news_df.columns}")

# Insert data into the 'sources' table
if 'source_name' in news_df.columns:
    sources_df.to_sql('sources', con=engine, if_exists='replace', index=False)
else:
    print("Skipping 'sources' table insertion due to missing columns.")

# Prepare the 'articles' DataFrame
article_columns = ['source_id', 'title', 'description', 'url', 'published_at', 'content', 'category', 'full_content']
if all(col in news_df.columns for col in article_columns):
    articles_df = news_df[article_columns]
    # Insert data into the 'articles' table
    articles_df.to_sql('articles', con=engine, if_exists='replace', index=False)
else:
    print(f"Warning: Some required columns for 'articles' are missing. Existing columns: {news_df.columns}")

# Example: Query the number of articles per source
query = """
SELECT source_name, COUNT(*) AS article_count
FROM articles
JOIN sources ON articles.source_id = sources.source_id
GROUP BY source_name
ORDER BY article_count DESC;
"""

result = pd.read_sql(query, con=engine)
print(result)
