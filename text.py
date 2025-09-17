import streamlit as st

st.title("Tire")
st.header("Entete")
st.subheader("Sous-entete")
st.markdown("c'est du **Markdown**")
st.caption("Légende")

code_example = """
def hello():
    print("Hello, World!")
"""
st.code(code_example, language="python")

st.divider()