import streamlit as st

if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_checkbox():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Click me", value=st.session_state.checkbox, on_change=toggle_checkbox)

if st.session_state.checkbox:
    user_input = st.text_input("Enter your name", value=st.session_state.get("user_input", ""))
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User input: {user_input}")