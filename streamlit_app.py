import mysql.connector
import streamlit as st

# Initialize connection.
def init_connection():
    config = st.secrets["tidb"]
    return mysql.connector.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        ssl_ca=config["ssl-ca"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

user_input = st.text_area('Question:')    
    
option = st.selectbox('Class :', ('Weather', 'Clock', 'Calendar', 'Map', 'Phone', 'Email', 'Calculator', 'Translator', 'Web search', 'Social media', 'Small talk', 'Message', 'Reminders', 'Music'))


def write(s,c):
      r = run_query("SELECT * FROM classification")
      st.write(r)

button = st.button("Write")

if user_input and button:
         write(user_input,option)
