import streamlit as st

st.title("Reload")

form_values = {
    "name": None,
    "age": 0,
    "gender": None,
    "hobbies": [],
}

with st.form(key="my_form"):
    form_values["name"] = st.text_input("Enter your name", value=form_values["name"])
    form_values["age"] = st.number_input("Enter your age", value=form_values["age"])
    form_values["gender"] = st.selectbox("Select your gender", ["Male", "Female"], index=form_values["gender"])
    form_values["hobbies"] = st.multiselect("Select your hobbies", ["Reading", "Writing", "Coding", "Gaming"], default=form_values["hobbies"])

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        if not all(form_values.values()):
            st.error("Please fill in all fields")
            st.stop()
        else:
            st.balloons()
            
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")
            
            print(form_values)
