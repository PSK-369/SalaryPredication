import pandas as pd
import streamlit as st
import joblib
import warnings
import traceback
import time

warnings.filterwarnings("ignore")
# Index(['age', 'weight', 'height'], dtype='object')

try:
    model = joblib.load("logistic_regression.joblib")
    st.info("Model is loaded successfully")
    st.header("Algorithm is --> Logistic Regression with multiclass classfication")
    st.title("Clothes Size[x,xl,l,xxl,xxxl etc..] predications")
    with st.sidebar.form(key="form inputs"):
        st.header("side bar section")
        with st.sidebar:
            st.subheader("Choose the input parameters")
            st.balloons()
            age = st.number_input("age", min_value=17, max_value=100, value=30)
            weight = st.number_input("weight", min_value=38, max_value=100, value=40)
            height = st.number_input("height", min_value=147, max_value=300, value=178)
            submitt_button = st.form_submit_button(label="submit")
            if submitt_button:
                st.warning("form is submitting")
                time.sleep(5)
                st.info("form is submitted")
                st.balloons()
            else:
                st.warning("form is not submitted")

    data_dict = {"age": age, "weight": weight, "height": height}
    df1 = pd.DataFrame(data=data_dict, index=[0])
    predication = model.predict(df1)
    print(f"cloth size predication is {abs(predication[0])}")
    st.code(
        f"""Clothe size :====>>  {abs(predication)}
            ('M', 1)
             ('S', 2)
             ('XXXL', 6)
             ('XL', 3)
             ('L', 0)
             ('XXS', 5)
             ('XXL', 4)
            
            """
    )
    st.header("Data related")
    st.table(df1)
    st.data_editor(df1)

    st.header("some charts")
    st.line_chart(df1)
    st.bar_chart(df1)

    pass
except Exception as e:
    st.error(f"{str(e)} <--------- error code")
    st.code(f"{traceback.format_exc()}")
    pass
else:
    st.write("No errors")
finally:
    st.header("Final block is executed")
    link = "https://github.com/PSK-369/SalaryPredication/tree/clothesSizeApp01"
    st.code(f" github link is : {link}")
    st.header("Thank You...!")
