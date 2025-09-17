import streamlit as st

st.title("Reload")

form_values = {
    "name": None,
    "age": 0,
    "gender": None,
    "hobbies": [],
}

with st.form(key="my_form"):
    form_values["name"] = st.text_input("Entrez votre nom", value=form_values["name"])
    form_values["age"] = st.number_input("Entrez votre age", value=form_values["age"])
    form_values["gender"] = st.selectbox("Selectionnez votre genrer", ["Male", "Female"], index=form_values["gender"])
    form_values["hobbies"] = st.multiselect("Selectionnez vos hobbies", ["Lire", "Ecrire", "Coder", "Jouer"], default=form_values["hobbies"])

    submit_button = st.form_submit_button("Envoyer")
    if submit_button:
        if not all(form_values.values()):
            st.error("Merci de remplir tous les champs")
            st.stop()
        else:
            st.balloons()
            
            st.write("### Informations")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
            
            print(form_values)