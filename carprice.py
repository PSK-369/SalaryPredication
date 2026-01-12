import pandas as pd
import streamlit as st
import joblib
import time
import warnings
import traceback


warnings.filterwarnings("ignore")
try:
    model = joblib.load("random_regressor.joblib")
    st.info("model is loaded successfully")
    st.code("This model is build based on Random Regressor")

    st.header("Seconds Cars Price Predications")
    st.balloons()
    with st.sidebar.form(key="input form parameters"):
        st.header("Side section")
        st.balloons()
        st.subheader("Choose the input parameters")
        with st.sidebar:
            year = st.number_input("Year", min_value=1995, max_value=2030, value=2000)
            kms_driven = st.number_input(
                "Kms_Driven", min_value=0, max_value=4000000, value=1000
            )
            fuel_type_encoded = st.number_input(
                "Fuel_Type",
                min_value=1,
                max_value=3,
                value=2,
                help="Petrol - 1 and Diesel -2 and LPG -3",
            )
            company_encoded = st.number_input(
                "Company_enocoded", min_value=1, max_value=25, value=10
            )
            submit_form = st.form_submit_button(label="Submit")
            if submit_form:
                st.info("form is submitting.....")
                time.sleep(3)
                st.info("form is submitted")
                st.balloons()
            else:
                st.warning("form is not submitted")

    data_dict = {
        "year": year,
        "kms_driven": kms_driven,
        "fuel_type_encoded": fuel_type_encoded,
        "company_encoded": company_encoded,
    }
    df1 = pd.DataFrame(data=data_dict, index=[0])
    predaction1 = model.predict(df1)
    print(f"predication values is {predaction1}")
    st.code(f"Seconds Car Price is : ==== {abs(predaction1[0]):,.2f}")
    st.header("Choosed data is ")
    st.table(df1)
    st.header("Editor Data")
    st.data_editor(df1)
    st.header("===== Charts ======")
    st.subheader("Input data Line Charts")
    st.line_chart(df1)
    st.subheader("Input data bar chart")
    st.bar_chart(df1)
except Exception as e:
    st.error(f"{str(e)} --- Error")
    st.code(f"{str(e)}", language="python")
    st.code(f"{traceback.format_exc()}", language="python")
else:
    st.info("No errors in the models")
finally:
    st.info("Code completed and final block is executed....")
    st.code(
        f"git hub code link: --> https://github.com/PSK-369/SalaryPredication/tree/secondscarpriceApp01"
    )
    st.header("Thank You ")
