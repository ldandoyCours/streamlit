import streamlit as st
import pandas as pd

st.title("Element Form")

with st.form(key="my_form"):
    st.subheader("Text input")
    text_input = st.text_input("Enter your name")
    
    st.subheader("Number input")
    number_input = st.number_input("Enter your age")
    
    st.subheader("Textarea")
    textarea = st.text_area("Enter your message")

    st.subheader("Slider")
    slider = st.slider("Select your age", min_value=0, max_value=100, value=25)

    st.subheader("Date input")
    date_input = st.date_input("Select your date")
    time_input = st.time_input("Select your time")

    st.subheader("Selectbox")
    selectbox = st.selectbox("Select your gender", ["Male", "Female"])

    st.subheader("Multiselect")
    multiselect = st.multiselect("Select your hobbies", ["Reading", "Writing", "Coding", "Gaming"])

    st.subheader("Radio")
    radio = st.radio("Select your gender", ["Male", "Female"])

    st.subheader("Checkbox")
    checkbox = st.checkbox("I agree to the terms and conditions")
    
    st.subheader("Button")
    button = st.form_submit_button("Submit")