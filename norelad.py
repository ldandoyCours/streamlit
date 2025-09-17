import streamlit as st

st.title("Rechargement")

with st.form(key="my_form"):
    name = st.text_input("Entrez votre nom")
    age = st.number_input("Entrez votre age")

    print(name, age)

    st.form_submit_button("Envoyez")