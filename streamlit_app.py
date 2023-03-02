import streamlit as st

user_input = st.text_area("Text :")

def write(s):
      #TO DO

button = st.button("Write")

if user_input and button:
         write(user_input)
