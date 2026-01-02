import pandas as pd
import time
import streamlit as st
import joblib
import warnings

warnings.filterwarnings("ignore")


try:
    logistic = joblib.load("logstic.joblib")
    decesion = joblib.load("Decesion.joblib")
    st.balloons()
    st.header("Social Media Affected or not to studies")
    st.title("Logistic Regression [Classifiers]")
    st.code("Models are loaded succssfully")
    with st.sidebar.form(key="form-inputs"):
        with st.sidebar:
            st.info("this is the side bar section")
            st.header("Choose the input parameters")
            Age = st.number_input("Age", min_value=10, max_value=30, value=20)
            Avg_Daily_Usage_Hours = st.number_input(
                "Avg_Daily_Usage_Hours", min_value=1, max_value=24, value=20
            )
            Sleep_Hours_Per_Night = st.number_input(
                "Sleep_Hours_Per_Night", min_value=1, max_value=15, value=10
            )
            Mental_Health_Score = st.number_input(
                "Mental_Health_Score", min_value=1, max_value=20, value=1
            )
            Conflicts_Over_Social_Media = st.number_input(
                "Conflicts_Over_Social_Media", min_value=1, max_value=6, value=2
            )
            Addicted_Score = st.number_input(
                "Addicted_Score", min_value=1, max_value=30, value=20
            )
            Relationship_Status_encoded = st.number_input(
                "Relationship_Status_encoded", min_value=0, max_value=3, value=2
            )
            Most_Used_Platform_encoded = st.number_input(
                "Most_Used_Platform_encoded", min_value=1, max_value=12, value=2
            )
            Gender_encoded = st.number_input(
                "Gender_encoded", min_value=0, max_value=3, value=2
            )
            Academic_Level_enoded = st.number_input(
                "Academic_Level_enoded", min_value=1, max_value=3, value=2
            )
            submit_button = st.form_submit_button(label="submit")
            if submit_button:
                with st.spinner("form is submitting"):
                    time.sleep(3)
                    st.info("form is submitted")
                    st.balloons()
            else:
                st.warning("form is not submitted")
    values_dict = {
        "Age": Age,
        "Avg_Daily_Usage_Hours": Avg_Daily_Usage_Hours,
        "Sleep_Hours_Per_Night": Sleep_Hours_Per_Night,
        "Mental_Health_Score": Mental_Health_Score,
        "Conflicts_Over_Social_Media": Conflicts_Over_Social_Media,
        "Addicted_Score": Addicted_Score,
        "Relationship_Status_encoded": Relationship_Status_encoded,
        "Most_Used_Platform_encoded": Most_Used_Platform_encoded,
        "Gender_encoded": Gender_encoded,
        "Academic_Level_enoded": Academic_Level_enoded,
    }
    df7 = pd.DataFrame(data=values_dict, index=[0])
    predication1 = logistic.predict(df7)
    st.code(
        "if 1 means not affeted to acadamics and 2 means students are affected to acadamics "
    )
    st.code("Logistic regression results")
    st.code(f"the predication value is ===> {abs(predication1[0]):,.2f}")

    # predication2 = decesion.predict(df7)
    # st.code("decesion tree classifier results")
    # st.code(f"the predication value is ===> {abs(predication2[0]):,.2f}")

    st.subheader("data")
    st.table(df7)

    st.subheader("data editor")
    st.data_editor(df7)

    st.subheader("bar chart")
    st.bar_chart(df7)

    st.subheader("line chart")
    st.line_chart(df7)


except Exception as e:
    st.error(f"{str(e)}")
    st.code(f"{str(e)}", language="python")
else:
    st.info("no errors in the code")
finally:
    st.info("final block is executed irrespective the error code")
