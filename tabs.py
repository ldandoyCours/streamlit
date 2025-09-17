import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("C'est la tab 1")

with tab2:
    st.write("C'est la tab 2")

with tab3:
    st.write("C'est la tab 3")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("C'est la col 1")

with col2:
    st.write("C'est la col 2")



