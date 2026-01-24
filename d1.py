import pandas as pd
import streamlit as st
import joblib
import time
import traceback


try:
    model1 = joblib.load("class1.joblib")
    model2 = joblib.load("class2.joblib")
    model3 = joblib.load("class3.joblib")
    st.info("Model is loaded successfully")
    st.title("Employees Resigned or not ")
    st.header("Used classification algorithms  logistic +  decision + randomforeset")

    with st.sidebar.form(key="input parameters"):
        st.subheader("side bar section")
        st.balloons()
        with st.sidebar:
            st.write("Chooose the input parameters")
            Age = st.number_input("age", min_value=18, max_value=100, value=20)
            Tenure = st.number_input("Tenure", min_value=1, max_value=80, value=20)
            UsageFrequency = st.number_input(
                "UsageFrequency", min_value=1, max_value=100, value=20
            )
            SupportCalls = st.number_input(
                "SupportCalls", min_value=18, max_value=40, value=20
            )
            Payements = st.number_input(
                "Payment Delay", min_value=0, max_value=30, value=20
            )
            TotalSpend = st.number_input(
                "TotalSpend", min_value=100, max_value=1000, value=200
            )
            LastInteraction = st.number_input(
                "LastInteraction", min_value=1, max_value=30, value=20
            )
            Genderencoded = st.number_input(
                "Genderencoded", min_value=0, max_value=1, value=0
            )
            SubscriptionTypeencoded = st.number_input(
                "SubscriptionTypeencoded", min_value=0, max_value=2, value=2
            )
            ContractLengthencoded = st.number_input(
                "ContractLengthencoded", min_value=0, max_value=2, value=2
            )
            submit_buttom = st.form_submit_button(label="submit")
            if submit_buttom:
                st.warning("Form is submitting....!")
                time.sleep(5)
                st.info("Form is sumitted")
                st.balloons()
            else:
                st.warning("form is not submitted please submit the form")

    data_dict = {
        "Age": Age,
        "Tenure": Tenure,
        "UsageFrequency": UsageFrequency,
        "SupportCalls": SupportCalls,
        "Payements": Payements,
        "TotalSpend": TotalSpend,
        "LastInteraction": LastInteraction,
        "Genderencoded": Genderencoded,
        "SubscriptionTypeencoded": SubscriptionTypeencoded,
        "ContractLengthencoded": ContractLengthencoded,
    }

    df1 = pd.DataFrame(data=data_dict, index=[0])
    predication1 = model1.predict(df1)
    print(abs(predication1[0]))
    st.code(
        f"The Chrun employee::: 0 not resigned:: 1 means leaved from ORG :--> {abs(predication1[0])}"
    )

except Exception as e:
    st.code(f"error is {str(e)}")
    st.code(traceback.format_exc(), language="python")

else:
    st.info("No errors in the code")
finally:
    st.code("final balock is excecuted")
