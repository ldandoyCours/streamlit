import streamlit as st
import pandas as pd

st.title("Element Form")

with st.form(key="my_form"):
    st.subheader("Text input")
    text_input = st.text_input("Entrez votre nom")
    
    st.subheader("Number input")
    number_input = st.number_input("Entrez votre age")
    
    st.subheader("Textarea")
    textarea = st.text_area("Entrez votre message")

    st.subheader("Slider")
    slider = st.slider("Select votre age", min_value=0, max_value=100, value=25)

    st.subheader("Date input")
    date_input = st.date_input("Select la date")
    time_input = st.time_input("Select l'heure")

    st.subheader("Selectbox")
    selectbox = st.selectbox("Select votre gender", ["Male", "Female"])

    st.subheader("Multiselect")
    multiselect = st.multiselect("Select votre hobbies", ["Lire", "Ecrire", "Coder", "Jouer"])

    st.subheader("Radio")
    radio = st.radio("Select votre genrer", ["Homme", "Femme"])

    st.subheader("Checkbox")
    checkbox = st.checkbox("J'accpete les conditions")
    
    st.subheader("Button")
    button = st.form_submit_button("Envoyez")