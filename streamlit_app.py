"""import streamlit as st

user_input = st.text_area("Text :")

def write(s):
      #TO DO
      return 0

button = st.button("Write")

if user_input and button:
         write(user_input)"""

import mysql.connector
import streamlit as st

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    config = st.secrets["tidb"]
    return mysql.connector.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        ssl_ca={"ca": config["ssl-ca"]}
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
