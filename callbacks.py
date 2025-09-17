import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if 'info' not in st.session_state:
    st.session_state.info = {}

def step_2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

def step_1():
    st.session_state.info["name"] = ""
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header("Step 1: Informations")
    name = st.text_input("Entrez votre nom", value=st.session_state.info.get("name", ""))

    st.button("Suivant", on_click=step_2, args=(name,))

if st.session_state.step == 2:
    st.header("Step 2: Vérifications")

    st.subheader("Merci de vérifier les informations suivantes:")
    st.write(f"**Nom**: {st.session_state.info.get('name', '')}")

    if st.button("Valider"):
        st.success("Informations validées avec succès!")
        st.balloons()
        st.session_state.info = {}

    st.button("Retour", on_click=step_1)