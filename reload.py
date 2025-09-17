import streamlit as st

st.title("Reload")

name = st.text_input("Entrez votre nom")
age = st.number_input("Entrez votre age")

print(name, age)