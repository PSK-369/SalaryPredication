import streamlit as st
import joblib
import pandas as pd
from datetime import datetime, date  # noqa: ignore

try:
    salary_model = joblib.load(
        r"C:\Shravan\PythonPratice\supervised\machineLearning1\predication01\linear_reg_salary.joblib"  # noqa: ignore
    )

    st.title(" EMP SALARY PREDICATIONS")
    st.write("Model is loaded successfully")
    st.balloons()
    with st.sidebar.form(key="form values"):
        with st.sidebar:
            st.header("Enter the Input values")
            EXP = st.number_input("EXP", min_value=1, max_value=28, value=2)
            AGE = st.number_input("AGE", min_value=17, max_value=65, value=20)
            GENE = st.number_input(
                "GENE",
                min_value=1,
                max_value=2,
                value=2,
                help="1 is male and 2 is for female",
            )
            submit_buttom = st.form_submit_button(label="submit")
            data1 = {"EXP": EXP, "AGE": AGE, "GENE": GENE}
            if submit_buttom:
                st.success("form is submitted succsufully")
            else:
                st.info("form is not submitted")
    dataframe1 = pd.DataFrame(data=data1, index=[0])
    predications = salary_model.predict(dataframe1)
    # print(f" salary is : INR : {abs(predications[0]):,.3f}")
    st.write(f" salary is : INR : {abs(predications[0]):,.3f}")
    st.subheader("Bar chart")
    st.bar_chart(data=dataframe1)
    st.markdown(f"{datetime.now().strftime("%Y-%M-%d %I:%M:%S %p")}")
except Exception as e:
    error = st.error(f"{str(e)} error message")
    st.code(f"{str(e)}", language="python")
    st.info(error)
else:
    pass
    # print("no errors in the code ....!")
finally:
    pass
