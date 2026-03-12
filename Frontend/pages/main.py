from matplotlib.pylab import rand
import streamlit as st
import joblib
import traceback
import warnings
import datetime
import os
import time
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

try:
    st.set_page_config(page_title="Main Form For Machine Learning", layout="centered")
    st.title("Most Addicated Social Media Platform")
    BasePath = os.path.dirname(os.path.abspath(__file__))
    print(BasePath)

    # Load models using the variable (no quotes around BasePath)
    logistic = joblib.load(os.path.join(BasePath, "LogisticRegression.joblib"))
    decision = joblib.load(os.path.join(BasePath, "DecisionTreeClassifier.joblib"))
    random = joblib.load(os.path.join(BasePath, "RandomForestClassifier.joblib"))
    knn = joblib.load(os.path.join(BasePath, "KNeighborsClassifier.joblib"))
    svc = joblib.load(os.path.join(BasePath, "SVC.joblib"))

    st.info("Models are loaded successfully")
    st.balloons()
    st.write("---------------------")

    with st.sidebar.form(key="Input paramerters", clear_on_submit=True):
        with st.sidebar:
            st.subheader("Choose the input parameters")
            st.write("---------------------")
            Age = st.number_input(
                label="Enter the age",
                min_value=5,
                max_value=90,
                label_visibility="visible",
                help="always be choose the above 5",
            )
            Avg_Daily_Usage_Hours = st.number_input(
                label="Enter the Avg_Daily_Usage_Hours",
                min_value=1,
                max_value=23,
                label_visibility="visible",
                help="always be choose the above 1",
            )
            Sleep_Hours_Per_Night = st.number_input(
                label="Enter the Sleep_Hours_Per_Night",
                min_value=3,
                max_value=10,
                label_visibility="visible",
                help="always be choose the above 3",
            )
            Mental_Health_Score = st.number_input(
                label="Enter the Mental_Health_Score",
                min_value=4,
                max_value=10,
                label_visibility="visible",
                help="always be choose the above 4",
            )
            Conflicts_Over_Social_Media = st.number_input(
                label="Enter the Conflicts_Over_Social_Media",
                min_value=2,
                max_value=10,
                label_visibility="visible",
                help="always be choose the above 2",
            )
            Addicted_Score = st.number_input(
                label="Enter the Addicted_Score",
                min_value=2,
                max_value=10,
                label_visibility="visible",
                help="always be choose the above 2",
            )
            Gender_encoded = st.number_input(
                label="Enter the Gender_encoded",
                min_value=1,
                max_value=2,
                label_visibility="visible",
                help="Here always be 1 -> Male or 2-> Female ",
            )
            Academic_Level_Encoded = st.number_input(
                label="Enter the Academic_Level_Encoded",
                label_visibility="visible",
                min_value=0,
                max_value=2,
                help="""
            2 -- Undergraduate     
            0 --   Graduate          
            1 -- High School 
            """,
            )
            Affects_Academic_Performance_Encoded = st.number_input(
                label="Enter the Affects_Academic_Performance_Encoded",
                min_value=0,
                max_value=2,
                label_visibility="visible",
                help="Imapcted or not Yes 1 and no 0",
            )
            model_selection = st.selectbox(
                label="Choose the model name",
                options=[
                    "ALL",
                    "ANYRANDOM",
                    "LOGISTIC",
                    "DECISIONTREE",
                    "RANDOMFOREST",
                    "KNNCLASSIFIER",
                    "SVC",
                ],
                label_visibility="visible",
            )
            submit = st.form_submit_button(label="submit", type="primary")
            st.write("-------------")
            if submit:
                st.warning("Form is submitting")
                time.sleep(3)
                st.warning("validating the elements")
                time.sleep(2)
                st.info("Form is submitted and Validation is completed")
                st.balloons()
            else:
                st.error("Form is not submitted")
                st.write("------------------------")
    model_elements = {
        "Age": Age,
        "Avg_Daily_Usage_Hours": Avg_Daily_Usage_Hours,
        "Sleep_Hours_Per_Night": Sleep_Hours_Per_Night,
        "Mental_Health_Score": Mental_Health_Score,
        "Conflicts_Over_Social_Media": Conflicts_Over_Social_Media,
        "Addicted_Score": Addicted_Score,
        "Gender_encoded": Gender_encoded,
        "Academic_Level_Encoded": Academic_Level_Encoded,
        "Affects_Academic_Performance_Encoded": Affects_Academic_Performance_Encoded,
    }
    df1 = pd.DataFrame(data=model_elements, index=[0])
    st.code(
        f""" Platform names are 
    {
    1, 'Instagram',
    6, 'TikTok',
    0, 'Facebook',
    10, 'WhatsApp',
    7, 'Twitter',
    4, 'LinkedIn',
    9, 'WeChat',
    5, 'Snapchat',
    3, 'LINE',
    2, 'KakaoTalk',
    8, 'VKontakte',
    11, 'YouTube' } """
    )
    st.write("-----------------")
    if model_selection == "ALL":
        all1 = logistic.predict(df1)
        all2 = decision.predict(df1)
        all3 = random.predict(df1)
        all4 = knn.predict(df1)
        all5 = svc.predict(df1)
        st.code(
            f"selection Model  is : {model_selection} and results are \n {all1[0]}  {all2[0]} {all3[0]} {all4[0]} {all5[0]}"
        )
        st.write("------------------------")
    elif model_selection == "ANYRANDOM":
        results2 = decision.predict(df1)
        st.code(
            f" selection Model  is : {model_selection} -- Most Used PlatForm {results2[0]}"
        )
    elif model_selection == "LOGISTIC":
        results1 = logistic.predict(df1)
        st.code(
            f"selection Model  is : {model_selection} -- Most Used PlatForm {results1[0]}"
        )
    elif model_selection == "DECISIONTREE":
        results2 = decision.predict(df1)
        st.code(
            f"selection Model  is : {model_selection} -- Most Used PlatForm {results2[0]}"
        )
    elif model_selection == "RANDOMFOREST":
        results3 = random.predict(df1)
        st.code(
            f"selection Model  is : {model_selection} -- Most Used PlatForm {results3[0]}"
        )
    elif model_selection == "KNNCLASSIFIER":
        results4 = knn.predict(df1)
        st.code(
            f"selection Model  is : {model_selection} -- Most Used PlatForm {results4[0]}"
        )
    else:
        if model_selection == "SVC":
            results5 = knn.predict(df1)
            st.code(
                f"selection Model  is : {model_selection} -- Most Used PlatForm {results5[0]}"
            )
            st.write("-------------------------")
    st.header("Data Frames")
    st.data_editor(df1)
    st.dataframe(df1)
    st.write("------------------------------")
    st.header("Normal Charts")
    st.bar_chart(df1)
    st.write("-----------------------")
    st.scatter_chart(df1)
    st.write("---------------------------------")

    figure, axes = plt.subplots(1, 2)
    df1.T.plot(kind="barh", ax=axes[0], fontsize=20)
    df1.T.plot(kind="kde", ax=axes[1], fontsize=20)
    plt.subplots_adjust(wspace=0.9, hspace=0.9)
    st.pyplot(figure)
    st.write("------------------------------")
except Exception as e:
    st.write("---------------------")
    st.code(f"serror code is {str(e)}", language="text")
    st.code(traceback.format_exc())
finally:
    st.write("--------------------------")
    st.subheader("Thank you...!")
    st.feedback("faces")
