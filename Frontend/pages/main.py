from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import statistics as sts
import seaborn as sns
import joblib
import streamlit as st
import time
from matplotlib import pyplot as plt
import streamlit as st
import requests
import os
import warnings
import requests

warnings.filterwarnings("ignore")

try:
    try:
        st.header("Dieases Type Predication")
        st.code(
            "Models  are used in Logistic + Decision +Random + KNN + SVC classification"
        )
        st.balloons()
        Logistic_classification = joblib.load("logistic_regression.joblib")
        Decision_classification = joblib.load("DecisionTreeClassifier_instance.joblib")
        Random_classification = joblib.load("RandomForestClassifier_Instance.joblib")
        Knn_classification = joblib.load("KNeighborsClassifier_instance.joblib")
        Svc_classification = joblib.load("SVCClassifier_instance.joblib")
        st.info("Models are loaded successfully....!")
        st.code("('Hypertension', 1), ('Diabetes', 0), ('Obesity', 2)")
        model_selection = {
            "Logistic_classification": Logistic_classification,
            "Decision_classification": Decision_classification,
            "Random_classification": Random_classification,
            "Knn_classification": Knn_classification,
            "Svc_classification": Svc_classification,
        }
        st.code(model_selection.items())

    except Exception as e2:
        st.code(str(e2), language="python")

    else:
        st.info("No Errors in the code")

    try:
        st.set_page_config(page_title="This is the main page URL", layout="centered")
        with st.sidebar.form(key="inputs passing", clear_on_submit=True, border=True):
            with st.sidebar:
                st.write("Choose the input parameters")
                st.divider()
                Age = st.number_input(
                    label="Age",
                    label_visibility="visible",
                    help="18 ---> 80",
                    value=20,
                    min_value=18,
                    max_value=80,
                )
                Weight_kg = st.number_input(
                    label="Weight in Kg",
                    label_visibility="visible",
                    help="20 ---> 80",
                    min_value=20,
                    max_value=100,
                )
                Height_cm = st.number_input(
                    label="Height_cm",
                    label_visibility="visible",
                    help="150 cm ---> 200cm",
                    value=100,
                )
                BMI = st.number_input(
                    label="BMI",
                    label_visibility="visible",
                    help="40-->90",
                    value=42,
                )

                Blood_Pressure_mmHg = st.number_input(
                    label="Blood_Pressure_mmHg",
                    label_visibility="visible",
                    help="110---> 190",
                    value=100,
                )

                Gender_Encoded = st.number_input(
                    label="Gender_Encoded",
                    label_visibility="visible",
                    help="0 - male and 1 female",
                    value=1,
                )

                Physical_Activity_Level_Encoded = st.number_input(
                    label="Height_Physical_Activity_Level_Encodedcm",
                    label_visibility="visible",
                    help="{('Active', 0): , ('Moderate', 1):, ('Sedentary', 2):}",
                    value=100,
                )

                Dietary_Restrictions_Encoded = st.number_input(
                    label="Dietary_Restrictions_Encoded",
                    label_visibility="visible",
                    help="{('Low_Sodium', 0): , ('Low_Sugar', 1): }",
                    value=1,
                )

                Allergies_Encoded = st.number_input(
                    label="Allergies_Encoded",
                    label_visibility="visible",
                    help="{('Gluten', 0):, ('Peanuts', 1):}",
                    value=0,
                )

                Diet_Recommendation_Encoded = st.number_input(
                    label="Diet_Recommendation_Encoded",
                    label_visibility="visible",
                    help="{('Balanced', 0): , ('Low_Sodium', 2):, ('Low_Carb', 1):}",
                    value=1,
                )
                choice = st.selectbox(
                    "select the machine leaning model",
                    options=[
                        "Logistic_classification",
                        "Decision_classification",
                        "Random_classification",
                        "Knn_classification",
                        "Svc_classification",
                        "All",
                    ],
                )
                submit = st.form_submit_button(
                    label="Submit", help="Click on the submit buttom", type="primary"
                )
                if submit:
                    st.warning("Clicked form")
                    import time

                    time.sleep(2)
                    st.warning("Form elements are submitting")
                    time.sleep(2)
                    st.info("Form elements are submitted")
                else:
                    st.error("Form elements are not submitted")
    except Exception as e1:
        st.code(str(e1), language="python")
    try:
        dict_fields = {
            "Age": Age,
            "Weight_kg": Weight_kg,
            "Height_cm": Height_cm,
            "BMI": BMI,
            "Blood_Pressure_mmHg": Blood_Pressure_mmHg,
            "Gender_Encoded": Gender_Encoded,
            "Physical_Activity_Level_Encoded": Physical_Activity_Level_Encoded,
            "Dietary_Restrictions_Encoded": Dietary_Restrictions_Encoded,
            "Allergies_Encoded": Allergies_Encoded,
            "Diet_Recommendation_Encoded": Diet_Recommendation_Encoded,
        }
        st.code("('Hypertension', 1), ('Diabetes', 0), ('Obesity', 2)")
        df1 = pd.DataFrame(data=dict_fields, index=[0])
        if choice == "Svc_classification":
            svc_pred = Svc_classification.predict(df1)
            st.code(f"Model name is {choice} and predication is {svc_pred[0]}")
        elif choice == "Logistic_classification":
            logi = Logistic_classification.predict(df1)
            st.code(f"Model name is {choice} and predication is {logi[0]}")
        elif choice == "Decision_classification":
            decision = Decision_classification.predict(df1)
            st.code(f"Model name is {choice} and predication is {decision[0]}")
        elif choice == "Random_classification":
            random = Random_classification.predict(df1)
            st.code(f"Model name is {choice} and predication is {random[0]}")
        elif choice == "Knn_classification":
            knn = Knn_classification.predict(df1)
            st.code(f"Model name is {choice} and predication is {knn[0]}")
        elif choice == "All":
            svc_pred = Svc_classification.predict(df1)
            logi = Logistic_classification.predict(df1)
            decision = Decision_classification.predict(df1)
            random = Random_classification.predict(df1)
            knn = Knn_classification.predict(df1)
            st.code(
                f"Model name is {choice} and predication is {svc_pred[0]} {logi[0]} {decision[0]} {random[0]} {knn[0]}"
            )
        else:
            st.warning("None of the models are not selected or not selected")

    except Exception as e3:
        st.code(str(e3))
    else:
        st.info("Main predication code is working fine")

    st.header("Some Data Presentation")
    st.write("----------------------------")
    st.json(model_selection)
    st.table(df1)

    st.subheader("Some data visual representation")
    st.write("-------------")
    st.bar_chart(df1)

    col1, col2 = st.columns(2, border=True)
    with col1:
        figure, axes = plt.subplots(1, 1)
        df1.T.plot(kind="bar", ax=axes, color="#ff4d01")
        st.pyplot(figure)

    with col2:
        figure, axes = plt.subplots(1, 1)
        df1.T.plot(kind="hist", ax=axes, color="#ff4d01")
        st.pyplot(figure)
except Exception as e0:
    st.code(str(e0), language="python")

else:
    st.info("No errors in the final code section")

finally:
    st.info("Final Code block is executed")
    st.feedback("faces")
