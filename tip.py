import streamlit as st
import pandas as pd
import joblib
import time
import warnings


warnings.filterwarnings("ignore")


try:
    model = joblib.load("tipspredication.joblib")
    st.info("model is loaded succesfully")
    st.header("decesion tree regressor")
    st.subheader("Hotel Servant tips Predications")
    st.balloons()

    with st.sidebar.form(key="inputs", border=True):
        with st.sidebar:
            st.header("Choose the values")
            total_bill = st.number_input(
                "total_bill Dollars", min_value=1, max_value=80, value=2
            )
            sex_encoded = st.number_input(
                "sex_encoded", min_value=0, max_value=1, value=1
            )
            smoker_encoded = st.number_input(
                "smoker_encoded", min_value=0, max_value=1, value=0
            )
            day_encoded = st.number_input(
                "day_encoded", min_value=0, max_value=7, value=2
            )
            submit_buttom = st.form_submit_button(
                label="submit", help="click on the submit buttom"
            )

            if submit_buttom:
                st.info("Form is submitting")
                time.sleep(5)
                st.info("Form is submitted successfully....!")
                st.balloons()
            else:
                st.warning("Form is not submitted")

    data_dict = {
        "total_bill": total_bill,
        "sex_encoded": sex_encoded,
        "smoker_encoded": smoker_encoded,
        "day_encoded": day_encoded,
    }
    df1 = pd.DataFrame(data=data_dict, index=[0])
    predication = model.predict(df1)
    st.code(f" Servant got the tips in dollars ---> {abs(predication[0]):,.2f}")
    print(f"{abs(predication[0]):,.2f}")
    st.header("Input choosed values in table format")
    st.table(df1)
    st.header("Data Editor values")
    st.data_editor(df1)
    st.header("line chart")
    st.line_chart(df1)
    st.header("barchart")
    st.bar_chart(df1)

except Exception as e:
    st.error(f"{str(e)} <<--- error ")
    st.code(f"{str(e)}", language="python")
else:
    print("no errors in the code")
    st.info("no errors in the code")
finally:
    print("final block is executed succesfully")
    st.info("Final block is executed")
