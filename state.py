import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Incrémenter le compteur"):
    st.session_state.counter += 1
    st.write(f"Compteur est à : {st.session_state.counter}")

if st.button("Remettre à zéro le compteur"):
    st.session_state.counter = 0

st.write(f"compteur: {st.session_state.counter}")