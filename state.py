import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to: {st.session_state.counter}")

if st.button("Reset counter"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")