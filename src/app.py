import psycopg2
import streamlit as st

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'modeldb'
DB_USER = 'postgres'
DB_PASS = '123456'

@st.cache_resource
def init_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

conn = init_connection()

def run_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    except psycopg2.Error as e:
        st.error(f"An error occurred: {e}")
        conn.rollback()  # Rollback the transaction if there's an error
        return None

st.title("PostgreSQL Streamlit Dashboard")

query = "SELECT * FROM Sources LIMIT 10;"
rows = run_query(query)

if rows:
    for row in rows:
        st.write(row)
else:
    st.write("No results due to an error in the query.")
