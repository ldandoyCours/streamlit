import streamlit as st

counter = 0

st.write(f"Counter: {counter}")

if st.button("Increment counter"):
    counter += 1
    st.write(f"Counter incremented to: {counter}")
else:
    st.write(f"Counter stays at: {counter}")