import streamlit as st

st.title("Text")
st.header("Header")
st.subheader("Subheader")
st.markdown("c'est du **Markdown**")
st.caption("Caption")

code_example = """
def hello():
    print("Hello, World!")
"""
st.code(code_example, language="python")

st.divider()