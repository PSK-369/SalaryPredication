from statistics import mode
import traceback
import joblib
import pandas as pd
import streamlit as st
import warnings
import time
import seaborn as sns
from matplotlib import pyplot as plt


warnings.filterwarnings("ignore")
try:
    model1 = joblib.load("class3_random.joblib")
    st.header("Algorithm --> Random Forest Classification")
    st.balloons()
    st.title("Coffee Name Predication")
    st.info("Model is loaded successfully")
    with st.sidebar.form(key="inputs"):
        st.subheader("Side bar Section")
        with st.sidebar:
            st.write("Select the input parameters")
            hour_of_day = st.number_input(
                "hour_of_day", min_value=1, max_value=24, value=2
            )
            money = st.number_input("money", min_value=18, max_value=40, value=20)
            Weekdaysort = st.number_input(
                "Weekdaysort", min_value=1, max_value=7, value=2
            )
            Monthsort = st.number_input("Monthsort", min_value=1, max_value=12, value=2)
            Time_of_Day_enocoded = st.number_input(
                "Time_of_Day_enocoded", min_value=0, max_value=2, value=2
            )
            Weekday_encoded = st.number_input(
                "Weekday_encoded", min_value=0, max_value=6, value=2
            )
            Month_name_encoded = st.number_input(
                "Month_name_encoded", min_value=0, max_value=11, value=2
            )

            submit = st.form_submit_button(label="submit")
            if submit:
                st.spinner("Sumitting")
                time.sleep(2)
                st.info("form is submitted")
                st.balloons()
    data_dict = {
        "hour_of_day": hour_of_day,
        "money": money,
        "Weekdaysort": Weekdaysort,
        "Monthsort": Monthsort,
        "Time_of_Day_enocoded": Time_of_Day_enocoded,
        "Weekday_encoded": Weekday_encoded,
        "Month_name_encoded": Month_name_encoded,
    }
    df1 = pd.DataFrame(data=data_dict, index=[0])
    pred = model1.predict(df1)
    print(f"Coffee name is : {pred[0]}")
    st.code(
        f"""Coffee Name is : {pred[0]} \n
            'Americano with Milk': 1,
             'Latte': 2,
             'Americano': 3,
             'Cappuccino': 4,
             'Cortado': 5,
             'Hot Chocolate': 6,
             'Cocoa': 7,
             'Espresso': 8
            """
    )

    st.header("Data Header Sections")
    st.table(df1)

    st.data_editor(df1)

    st.dataframe(df1)
    st.subheader("Feature Values")
    fig, ax = plt.subplots(figsize=(16, 5))
    sns.set_theme(style="darkgrid")
    df1.T.plot(kind="bar", legend=False, ax=ax, color="orange")
    ax.set_title("Input Feature Values")
    ax.set_ylabel("Value")
    ax.set_xlabel("Feature")
    plt.xticks(rotation=50, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 5))
    sns.set_theme(style="darkgrid")
    df1.T.plot(kind="line", ax=ax, color="orange")
    ax.set_title("Input Feature Values")
    ax.set_ylabel("Value")
    ax.set_xlabel("Feature")
    plt.xticks(rotation=50, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 5))
    sns.set_theme(style="darkgrid")
    df1.T.plot(kind="density", ax=ax, color="#ff4d01")
    ax.set_title("Input Feature Values")
    ax.set_ylabel("Value")
    ax.set_xlabel("Feature")
    plt.xticks(rotation=50, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 5))
    sns.set_theme(style="darkgrid")
    df1.T.plot(kind="kde", ax=ax, color="#ff4d01")
    ax.set_title("Input Feature Values")
    ax.set_ylabel("Value")
    ax.set_xlabel("Feature")
    plt.xticks(rotation=50, ha="right")
    plt.tight_layout()
    st.pyplot(fig)

except Exception as e:
    st.code(f"{str(e)} error", language="python")
    st.code(traceback.format_exc(), language="python")

else:
    st.info("no errors in the code")
finally:
    st.header("Thank You .....!")
