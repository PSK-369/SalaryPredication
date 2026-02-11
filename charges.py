from traceback import format_exc
import traceback
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
import time
import streamlit as st
import joblib

warnings.filterwarnings("ignore")

Username = "testprice"
Password = "testprice"


def sample_Login_page(user, password) -> str:
    if Username == user and Password == password:
        st.info("Login is succssfull....!")
    elif Username != user or Password != password:
        raise Exception(
            "Please enter the username and password details \n FYInformation: username and password is : testprice"
        )
    elif Username == "" or Password == " ":
        raise Exception("Fresh Page")
    else:
        st.info("Fresh Page")


def main_function():
    try:
        model1 = joblib.load("Linear.joblib")
        model2 = joblib.load("poly.joblib")
        model3 = joblib.load("poly1.joblib")
        model4 = joblib.load("decesion.joblib")
        model5 = joblib.load("ran.joblib")
        model6 = joblib.load("knn.joblib")
        model7 = joblib.load("lasso.joblib")
        st.divider()
        st.title("Medical Insurance Cost Predication")
        st.divider()
        st.code("Used Algo reg [Linear + Poly2 + Poly3 + Lasso + Tree + Random + KNN ]")
        st.balloons()
        st.write("---")
        with st.sidebar.form(key="form inputs"):
            st.write("side bar")
            with st.sidebar:
                st.write("choose the parameters")
                st.write("--------")
                age = st.number_input("age", min_value=18, max_value=80, value=30)
                bmi = st.number_input("bmi", min_value=10, max_value=80, value=20)
                children = st.number_input(
                    "children", min_value=1, max_value=30, value=3
                )
                region_encoded = st.number_input(
                    "region_encoded",
                    min_value=1,
                    max_value=3,
                    value=3,
                    help="'southwest':0, 'southeast':1, 'northwest':2, 'northeast':3",
                )
                smoker_enocoded = st.number_input(
                    "smoker_enocoded",
                    min_value=0,
                    max_value=1,
                    value=1,
                    help=""" "yes":1,"no":0 """,
                )
                sex_encoded = st.number_input(
                    "sex_encoded",
                    min_value=0,
                    max_value=1,
                    value=0,
                    help="'male': 0, 'female': 1 ",
                )
                model_dict = {
                    "Linear": model1,
                    "ploy degree2": model2,
                    "Decesion Tree": model4,
                    "Random forest": model5,
                    "Knn": model6,
                    "other": [model3, model7],
                    "all": [model1, model2, model3, model4, model5, model5, model6],
                }
                options = st.selectbox("modelname selection", options=model_dict.keys())
                submit1 = st.form_submit_button(label="Submit Form")
        if submit1:
            st.warning("Form is submitting.....")
            time.sleep(2)
            st.info("form is submitted")
            st.balloons()
        else:
            st.warning("Form is not submitted")
        st.write("-----------")
        data_dict = {
            "age": age,
            "bmi": bmi,
            "children": children,
            "region_encoded": region_encoded,
            "smoker_enocoded": smoker_enocoded,
            "sex_encoded": sex_encoded,
        }
        df1 = pd.DataFrame(data=data_dict, index=[0])
        pred1 = model1.predict(df1)
        pred2 = model2.predict(df1)
        pred3 = model3.predict(df1)
        pred4 = model4.predict(df1)
        pred5 = model5.predict(df1)
        pred6 = model6.predict(df1)
        pred7 = model7.predict(df1)
        if options == "Linear":
            st.code(
                f"Model: Linear Regression\nCharge Amount: INR {abs(pred1[0]):,.2f}",
                language="text",
            )
        elif options == "ploy degree2":
            st.code(
                f"Model: Polynomial (Degree 2)\nCharge Amount: INR {abs(pred2[0]):,.2f}",
                language="text",
            )
        elif options == "Decesion Tree":
            st.code(
                f"Model: Decision Tree\nCharge Amount: INR {abs(pred4[0]):,.2f}",
                language="text",
            )
        elif options == "Random forest":
            st.code(
                f"Model: Random Forest\nCharge Amount: INR {abs(pred5[0]):,.2f}",
                language="text",
            )
        elif options == "Knn":
            st.code(
                f"Model: KNN\nCharge Amount: INR {abs(pred6[0]):,.2f}", language="text"
            )
        else:
            if options == "other":
                st.code(
                    f"Model: Lasso\nCharge Amount: INR {abs(pred7[0]):,.2f}",
                    language="text",
                )
                st.code(
                    f"Model: Polynomial (Degree 3)\nCharge Amount: INR {abs(pred3[0]):,.2f}",
                    language="text",
                )
            elif options == "all":
                st.code(
                    f"Model: Linear Regression\nCharge Amount: INR {abs(pred1[0]):,.2f}",
                    language="text",
                )
                st.code(
                    f"Model: Polynomial (Degree 2)\nCharge Amount: INR {abs(pred2[0]):,.2f}",
                    language="text",
                )
                st.code(
                    f"Model: Decision Tree\nCharge Amount: INR {abs(pred4[0]):,.2f}",
                    language="text",
                )
                st.code(
                    f"Model: Random Forest\nCharge Amount: INR {abs(pred5[0]):,.2f}",
                    language="text",
                )
                st.code(
                    f"Model: KNN\nCharge Amount: INR {abs(pred6[0]):,.2f}",
                    language="text",
                )
        st.write("-------------------")
        st.subheader("Models details")
        st.json(model_dict)
        st.subheader("features data editor")
        st.data_editor(df1)
        st.write("-----------------------")
        st.subheader("Charts")
        st.dataframe(df1)
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(8, 8))
            cl1 = ["#ff4d01", "#ffffff"]
            sns.set_theme(style="white", palette=cl1)
            df1.T.plot(kind="barh", color="#ff4d01", ax=ax)
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots(figsize=(8, 8))
            cl1 = ["#ff4d01", "#ffffff"]
            sns.set_theme(style="white", palette=cl1)
            df1.T.plot(kind="kde", color="#ff4d01", ax=ax)
            st.pyplot(fig)
        col3, col4 = st.columns(2)
        with col3:
            fig, ax = plt.subplots(figsize=(8, 8))
            cl1 = ["#ff4d01", "#ffffff"]
            sns.set_theme(style="white", palette=cl1)
            df1.T.plot(kind="hist", color="#ff4d01", ax=ax)
            st.pyplot(fig)
        with col4:
            fig, ax = plt.subplots(figsize=(8, 8))
            cl1 = ["#ff4d01", "#ffffff"]
            sns.set_theme(style="white", palette=cl1)
            df1.T.plot(kind="line", color="#ff4d01", ax=ax)
            st.pyplot(fig)
    except Exception as e:
        st.code(f"{str(e)}", language="text")
        st.code(traceback.format_exc())
    else:
        st.info("No errors in the model")
    finally:
        st.code("Thank You....!")


try:
    st.set_page_config(page_title="Login", layout="centered")
    st.title(" Medical Insurance Predictor")
    st.markdown("#### Please authenticate to continue")
    with st.form(key="inputs", clear_on_submit=True, border=True):
        user = st.text_input("Enter the username", help="testprice")
        password = st.text_input("Enter the password", help="testprice")
        submit = st.form_submit_button(label="submit")
    if submit:
        sample_Login_page(user, password)
        st.info("form is submitting")
        time.sleep(3)
        st.info("form is submitted")

except Exception as e:
    st.code(f"{str(e)}")
    # st.code(f"{traceback.format_exc()}")
else:
    st.code("No errors in the code")

main_function()
