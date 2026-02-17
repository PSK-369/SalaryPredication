import traceback
import pandas as pd
from matplotlib import pyplot as plt
import datetime
import warnings
import joblib
import streamlit as st


warnings.filterwarnings("ignore")

# basic form
st.title("User Authenticaion Form")
st.set_page_config(page_title="Loan Approved or not Pred", layout="centered")
with st.form(key="Inputs form", clear_on_submit=True):
    username = st.text_input(
        label="username",
        label_visibility="visible",
        type="default",
        help="enter the email dummy email id",
    )
    password = st.text_input(
        label="password",
        label_visibility="visible",
        type="password",
        help="enter the password details",
    )
    submit = st.form_submit_button(label="submit", type="primary")

    if submit:
        if len(username) <= 4:
            st.warning("You entered below 4 characters or = charcter or empty fields")
        elif "@gmail.com" not in username:
            st.warning("@gmail is missed")
        elif len(password) <= 5:
            st.warning("you netered below or 5 digits passwords")
        else:
            st.code(
                f"username and password is ok and username is:  {username} and password is : {password}"
            )
            st.balloons()
            st.info("Validation checks are completed")
        if username == "admin@gmail.com" or password == "admin@gmail.com":
            st.warning("you entered admin rights")


try:
    st.write("----------------")
    st.write("------------")
    st.header("Loan Approval Status Check")
    model1 = joblib.load("logi.joblib")
    model2 = joblib.load("tree.joblib")
    model3 = joblib.load("random.joblib")
    model4 = joblib.load("knn.joblib")
    st.code("models used Logi + Tree + Random + KNN")
    st.info("Models are loaded succeesfully")

    st.divider()
    with st.sidebar.form(key="inputs", clear_on_submit=True, border=True):
        with st.sidebar:
            st.subheader("Input values")
            st.write("-------------")
            ApplicantIncome = st.number_input(
                label="ApplicantIncome",
                label_visibility="visible",
                min_value=150,
                max_value=100000,
                help="choose the range",
                value=200,
            )
            CoapplicantIncome = st.number_input(
                label="CoapplicantIncome",
                label_visibility="visible",
                min_value=0,
                max_value=10000,
                value=100,
                help="choose the range",
            )
            LoanAmount = st.number_input(
                label="LoanAmount",
                label_visibility="visible",
                min_value=10,
                max_value=10000,
                value=100,
                help="choose the range",
            )
            Loan_Amount_Term = st.number_input(
                label="Loan_Amount_Term",
                label_visibility="visible",
                min_value=0,
                max_value=100000,
                value=10,
                help="choose the range",
            )
            Credit_History = st.number_input(
                label="Credit_History",
                label_visibility="visible",
                min_value=0,
                max_value=1,
                value=1,
                help="choose the range",
            )
            Gender_encoded = st.number_input(
                label="Gender_encoded",
                label_visibility="visible",
                min_value=0,
                max_value=1,
                value=1,
                help="choose the gender [0 female and 1 male]",
            )
            Property_Area_Encoded = st.number_input(
                label="Property_Area_Encoded",
                label_visibility="visible",
                min_value=0,
                max_value=2,
                value=1,
                help="choose the proerty area",
            )
            Education_encoded = st.number_input(
                label="Education_encoded",
                label_visibility="visible",
                min_value=0,
                max_value=0,
                value=0,
                help="Always be 0",
            )
            model_dict = {
                "Linear": model1,
                "Tree": model2,
                "Random": model3,
                "KNN": model4,
            }
            Model_selection1 = st.selectbox(
                label="Choose the models",
                options=["Linear", "Tree", "Random", "KNN", "ALL"],
            )
            submit = st.form_submit_button(label="submit", type="primary")
            if submit:
                st.warning("form is submitting")
                import time

                time.sleep(2)
                st.info("form is submitted....!")
                st.balloons()
            else:
                st.error("form is not submitted")
    data_dict = {
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Gender_encoded": Gender_encoded,
        "Property_Area_Encoded": Property_Area_Encoded,
        "Education_encoded": Education_encoded,
    }
    st.code("0 -> Means Loan Approval Cancelled and 1 -> Means Loan Approved")
    df1 = pd.DataFrame(data=data_dict, index=[0])
    if Model_selection1 == "Linear":
        predication1 = model1.predict(df1)
        st.code(
            f"Model name is {Model_selection1 } Classification Model and result is --> {abs(predication1[0])}"
        )

    elif Model_selection1 == "Tree":
        predication2 = model2.predict(df1)
        st.code(
            f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication2[0])}"
        )
    elif Model_selection1 == "Random":
        predication3 = model3.predict(df1)
        st.code(
            f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication3[0])}"
        )

    elif Model_selection1 == "KNN":
        predication4 = model4.predict(df1)
        st.code(
            f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication4[0])}"
        )
    else:
        if Model_selection1 == "ALL":
            predication5 = model1.predict(df1)
            st.code(
                f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication5[0])}"
            )
            predication6 = model2.predict(df1)
            st.code(
                f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication6[0])}"
            )
            predication7 = model2.predict(df1)
            st.code(
                f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication7[0])}"
            )
            predication8 = model2.predict(df1)
            st.code(
                f"Model name is {Model_selection1} Classification Model and result is --> {abs(predication8[0])}"
            )

    st.write("------------------")
    st.subheader("Data Features")
    st.table(df1)
    st.write("---------------")
    st.subheader("Model details Json Format")
    st.json(model_dict)

    st.write("------------------------")
    st.dataframe(df1)
    st.subheader("Some statical Images")
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(10, 10))
        df1.T.plot(kind="barh", ax=ax, color="#ff4d01")
        st.pyplot(fig)

        st.divider()

    with col2:
        fig, ax = plt.subplots(figsize=(5, 5))
        df1.T.plot(kind="kde", ax=ax, color="#ff4d01", legend=True)
        plt.xticks(rotation=20)
        st.pyplot(fig)
        st.divider()

    fig, ax = plt.subplots(figsize=(10, 6))
    df1.T.plot(kind="hist", ax=ax, color="#ff4d01")
    st.pyplot(fig)
    st.divider()

except Exception as e:
    st.code(str(e))
    st.code(traceback.format_exc())
else:
    st.info("No errors in the code...!")
finally:
    st.subheader("Thank You")
    st.feedback(options="stars")
    st.write("--------------------------")
