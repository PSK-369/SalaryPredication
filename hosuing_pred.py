import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load("house_predications.joblib")
    st.title("****** Housing Predictions ******")
    st.write("✅ Model loaded successfully.")

    st.sidebar.write("Enter all required details")

    with st.form(key="form_details"):
        with st.sidebar:
            Area = st.number_input("Area", min_value=1100, max_value=9999, value=3340)
            new_location = st.number_input(
                "New Location (encoded)", min_value=0, max_value=999, value=70
            )
            school = st.number_input("School", min_value=0, max_value=10, value=8)
            Bed = st.number_input("Bed", min_value=0, max_value=10, value=1)
            submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        data1 = {
            "Area": Area,
            "new_location_encoded": new_location,
            "School": school,
            "BED": Bed,
        }
        df = pd.DataFrame(data1, index=[0])
        prediction = model.predict(df)
        st.write(f"The predicted price is ₹{prediction[0]:,.2f}")
        st.write("Thanks you....!")
        st.balloons()

except Exception as e:
    st.error(f"❌ An error occurred: {e}")
    st.code(str(e), language="python")
