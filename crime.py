import numpy as np
import pandas as pd
import traceback
import joblib
import streamlit as st
import warnings
import time

warnings.filterwarnings("ignore")
try:
    model = joblib.load("random_classifier.joblib")
    st.info("model is loaded successfully")
    st.subheader("Algorithm is -> random Forest Classifier")
    st.header("Crime name classification Predication")
    st.balloons()
    with st.sidebar.form(key="input parameters"):
        st.subheader("Section Form ")
        st.write("select the values")
        with st.sidebar:
            Offender_Age = st.number_input(
                "Offender_Age", min_value=11, max_value=100, value=15
            )
            Victim_Age = st.number_input(
                "Victim_Age", min_value=0, max_value=100, value=20
            )
            Disposition_encoded = st.number_input(
                "Disposition_encoded", min_value=0, max_value=1, value=1
            )
            Offender_Race_encoded = st.number_input(
                "Offender_Race_encoded", min_value=0, max_value=5, value=2
            )
            Offender_Gender_encoded = st.number_input(
                "Offender_Gender_encoded", min_value=0, max_value=1, value=1
            )
            PersonType_encoded = st.number_input(
                "PersonType_encoded", min_value=0, max_value=2, value=1
            )
            Victim_Race_encoded = st.number_input(
                "Victim_Race_encoded", min_value=0, max_value=5, value=3
            )
            Victim_Gender_encoded = st.number_input(
                "Victim_Gender_encoded", min_value=0, max_value=2, value=1
            )
            Victim_Fatal_Status_encoded = st.number_input(
                "Victim_Fatal_Status_encoded", min_value=0, max_value=1, value=0
            )
            Report_Type_encoded = st.number_input(
                "Report_Type_encoded", min_value=0, max_value=1, value=1
            )
            submit = st.form_submit_button(label="Submit")
            if submit:
                st.warning("form is submitting")
                time.sleep(2)
                st.info("form is submitted")
                st.balloons()
            else:
                st.error("form is not submitted please click on the submit buttom")
    data_dict = {
        "Offender_Age": Offender_Age,
        "Victim_Age": Victim_Age,
        "Disposition_encoded": Disposition_encoded,
        "Offender_Race_encoded": Offender_Race_encoded,
        "Offender_Gender_encoded": Offender_Gender_encoded,
        "PersonType_encoded": PersonType_encoded,
        "Victim_Race_encoded": Victim_Race_encoded,
        "Victim_Gender_encoded": Victim_Gender_encoded,
        "Victim_Fatal_Status_encoded": Victim_Fatal_Status_encoded,
        "Report_Type_encoded": Report_Type_encoded,
    }
    df1 = pd.DataFrame(data=data_dict, index=[0])
    predications1 = model.predict(df1)
    print(f"catageroy name is : - >{abs(predications1[0]):,.2f}")
    st.code(
        f"""catageroy name is : - >{abs(predications1[0]):,.2f} \n 
        based on the input features
            crime names : 
               Drug and Weapon Crimes - 0
               Violence - 5
               Sexual Crimes  - 2
               Theft  - 3
               Vandalism - 4
               Miscellaneous - 1
            """
    )
    st.header("data")
    st.table(df1)
    st.data_editor(df1)
    st.header("charts")
    st.subheader("line chart")
    st.line_chart(df1)
    st.subheader("bar charts")
    st.bar_chart(df1)
    st.subheader("Scatter chart")
    st.scatter_chart(df1)


except Exception as e:
    st.error(f"The Error -- {str(e)}")
    st.code(f"The Error in python language {str(e)}", language="python")
    st.code(traceback.format_exc())
else:
    st.info("no errors in the code yours code good")
finally:
    st.info("final block is executed and no code after this on")
    # st.code(f"Github URL Link -- > {}")
    st.code("Thank You")
    pass
