import streamlit as st

counter = 0

st.write(f"Compteur: {counter}")

if st.button("Incrémenter counter"):
    counter += 1
    st.write(f"Compteur est à: {counter}")
else:
    st.write(f"compteur reste à: {counter}")