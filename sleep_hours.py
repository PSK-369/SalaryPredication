import pandas as pd
import warnings
import streamlit as st
import joblib
import numpy as np
import time
import traceback
from matplotlib import pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")


try:
    model1 = joblib.load("linear_reg.joblib")
    model2 = joblib.load("decesiontree.joblib")
    model3 = joblib.load("random_forest.joblib")
    model4 = joblib.load("knn.joblib")
    st.title("Clothes Price Predications")
    st.divider()
    st.info("Model is loaded successfully...")
    st.balloons()

    st.code("Used : Linear reg + Polynomail + Decesion Tree + Random Forest + KNN")
    st.divider()
    with st.sidebar.form(key="form inputs"):
        st.subheader("form sidebar")
        with st.sidebar:
            st.subheader("Side bar Input parameters")
            st.divider()
            Material_encoded = st.number_input(
                "Material_encoded", min_value=0, max_value=5, value=2
            )

            Size_encoded = st.number_input(
                "Size_encoded", min_value=0, max_value=5, value=3
            )

            Color_encoded = st.number_input(
                "Color_encoded", min_value=0, max_value=5, value=2
            )

            Category_encoded = st.number_input(
                "Category_encoded", min_value=0, max_value=5, value=1
            )
            Brand_encoded = st.number_input(
                "Brand_encoded", min_value=0, max_value=5, value=1
            )
            st.divider()

            submit = st.form_submit_button(label="submit")
            if submit:
                st.warning("form is submitting....!")
                time.sleep(2)
                st.info("form is submitted :) ")
                st.balloons()

            else:
                st.warning("Form is not submitted please submit the form....!")

    data_dict = {
        "Material_encoded": Material_encoded,
        "Size_encoded": Size_encoded,
        "Color_encoded": Color_encoded,
        "Category_encoded": Category_encoded,
        "Brand_encoded": Brand_encoded,
    }
    df1 = pd.DataFrame(data=data_dict, index=[0])
    predication = model1.predict(df1)
    predication1 = model2.predict(df1)
    predication2 = model3.predict(df1)
    predication3 = model4.predict(df1)
    st.code(f"Linear reg: Clothes Predication Price is INR: {abs(predication[0]):,.2f}")
    st.code(
        f"Decesion Tree reg: Clothes Predication Price is INR: {abs(predication1[0]):,.2f}"
    )
    st.code(
        f"random forest reg: Clothes Predication Price is INR: {abs(predication2[0]):,.2f}"
    )
    st.code(f"KNN reg: Clothes Predication Price is INR: {abs(predication3[0]):,.2f}")
    st.divider()

    st.dataframe(df1)
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(13, 10))
        df1.T.plot(kind="barh", ax=ax, color="#ff4d01", legend=True)
        ax.set_title("Features bar Graph")
        st.pyplot(fig)
        st.write("------------------")
    with col2:
        fig, ax = plt.subplots(figsize=(10, 6))
        df1.T.plot(kind="line", ax=ax, color="#ff4d01", legend=True)
        ax.set_title("Features line Graph")
        st.pyplot(fig)
        st.divider()
    col3, col4 = st.columns(2)
    with col3:
        fig, ax = plt.subplots(figsize=(10, 4))
        df1.T.plot(kind="kde", ax=ax, color="#ff4d01", legend=True)
        ax.set_title("Features kde Graph")
        st.pyplot(fig)
        st.write("----------------")
    with col4:
        fig, ax = plt.subplots(figsize=(10, 4))
        df1.T.plot(kind="hist", ax=ax, color="#ff4d01", legend=True)
        ax.set_title("Features kde Graph")
        st.pyplot(fig)
        st.write("----------------")

    st.data_editor(df1)
    st.write("---------------------------------------------------------")
    # st.table(df1)
    col5, col6 = st.columns(2)
    with col5:
        st.scatter_chart(df1)
        st.write("---------------------------------------------------------")
    with col6:
        st.bar_chart(predication3)
        st.write("-----------------------------------------------------")

except Exception as e:
    st.code(str(e), language="python")
    st.error(str(e))
    st.code(traceback.format_exc())

else:
    st.info("No errors in the code....!")
finally:
    print("Final Block is excecuted")
    st.subheader("Thank You ....!")
    st.write("-----------------")
