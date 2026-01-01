import joblib
import pandas as pd
import streamlit as st
import time


try:
    model1 = joblib.load("decesion_reg.joblib")
    model2 = joblib.load("linear_reg.joblib")
    st.balloons()
    st.header(
        "Decesion tree regression + Linear Regression Model is loaded successfully ....."
    )
    st.title("Exam Score predication ")
    with st.form(key="form-inputs"):
        with st.sidebar:
            st.header("Choose the input parameters ranges")
            age = st.number_input("age", min_value=17, max_value=30, value=30)
            study_hours = st.number_input(
                "study_hours", min_value=1, max_value=10, value=8
            )
            class_attendance = st.number_input(
                "class_attendance", min_value=30, max_value=90, value=30
            )
            sleep_hours = st.number_input(
                "sleep_hours", min_value=0, max_value=10, value=8
            )
            exam_difficulty_encoded = st.number_input(
                "exam_difficulty_encoded", min_value=0, max_value=3, value=2
            )
            facility_rating_encoded = st.number_input(
                "facility_rating_encoded", min_value=0, max_value=3, value=1
            )
            study_method_encoded = st.number_input(
                "study_method_encoded", min_value=0, max_value=6, value=2
            )
            sleep_quality_encoded = st.number_input(
                "sleep_quality_encoded", min_value=0, max_value=4, value=2
            )
            gender_encoded = st.number_input(
                "gender_encoded", min_value=0, max_value=3, value=2
            )
            course_encoded = st.number_input(
                "course_encoded", min_value=0, max_value=7, value=2
            )
            internet_access_encoded = st.number_input(
                "internet_access_encoded", min_value=1, max_value=2, value=1
            )
            submit_buttom = st.form_submit_button(label="submit")

            if submit_buttom:
                st.spinner("form is submitting")
                time.sleep(3)
                st.success("form is submitted")
                st.balloons()
            else:
                st.warning("form is not submitted")
    data_dict = {
        "age": age,
        "study_hours": study_hours,
        "class_attendance": class_attendance,
        "sleep_hours": sleep_hours,
        "exam_difficulty_encoded": exam_difficulty_encoded,
        "facility_rating_encoded": facility_rating_encoded,
        "study_method_encoded": study_method_encoded,
        "sleep_quality_encoded": sleep_quality_encoded,
        "gender_encoded": gender_encoded,
        "course_encoded": course_encoded,
        "internet_access_encoded": internet_access_encoded,
    }

    df1 = pd.DataFrame(data=data_dict, index=[0])
    prediations1 = model1.predict(df1)
    st.code("this the decisiontree regressor")
    st.code(f"The Exam score is {abs(prediations1[0]):,.2f}")
    st.code("this the linear regressor")
    prediations2 = model2.predict(df1)
    st.code(f"The Exam score is {abs(prediations2[0]):,.2f}")
    st.write("Thank you ....!")
    if prediations1 < prediations2:
        st.info("Linear regression is good")
    else:
        st.info("decesion tree regressor is good")

    st.header("bar chart")
    st.bar_chart(df1)

    st.header("line chart")
    st.line_chart(df1)

    st.code("showing the interms of table format")
    st.table(df1)
    st.data_editor(df1)

except Exception as e:
    st.error(f"{str(e)}")
    st.code(str(e), language="python")

else:
    st.success("no errors in the code")
finally:
    st.success("no errors in the code and final balock is executed")
