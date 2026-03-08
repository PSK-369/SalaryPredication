import joblib
import pandas as pd 
import time 
import warnings 
import streamlit as st 
import os 
import traceback
import datetime
from matplotlib import pyplot as plt 
import seaborn as sns

warnings.filterwarnings('ignore')


try:
    st.title("Married Life Predication")
    time1=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p")
    st.code(time1)
    st.write('--------------------------')
    st.code("{(2, 'Medium'), (0, 'High'), (1, 'Low'):}")
    st.code("used Models : Logistic regression + Decision Tree + Random Forest + KNN Classifier + SVC")
    st.write('----------------------------')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    Model_dir=os.path.join(BASE_DIR,'..','..','..','Modeljoblibfiles')
    Model_dir=os.path.abspath(Model_dir)
    logistic=joblib.load(os.path.join(Model_dir,'logistic.joblib'))
    decision=joblib.load(os.path.join(Model_dir,'decision.joblib'))
    random=joblib.load(os.path.join(Model_dir,'random.joblib'))
    knn=joblib.load(os.path.join(Model_dir,'knn.joblib'))
    svc=joblib.load(os.path.join(Model_dir,'svc.joblib'))
    st.info("models are loaded succssfully")
    st.divider()
    with st.sidebar.form(key="inputs",clear_on_submit=True,border=True):
        with st.sidebar:
             st.header("Sidebar Section chooose the imput parameters")
             Education_Level_encoded=st.number_input(label='Education_Level_encoded',help='''(0, 'Graduate'): 
                  (3, 'School'): ,
                  (2, 'Postgraduate'): ,
                  (1, 'PhD'): ''',min_value=0,max_value=3,value=1)
             Caste_Match_encoded=st.number_input(label='Education_Level_encoded',help='''{(1, 'Same'), (0, 'Different')} ''',min_value=0,max_value=1,value=1)
             Religion_encoded=st.number_input(label='Religion_encoded',help='''{(1, 'Hindu'): ,
             (2, 'Muslim'): ,
             (0, 'Christian'): ,
             (3, 'Others'): ,
             (4, 'Sikh'): } ''',min_value=0,max_value=4,value=1)
             Urban_Rural_encoded=st.number_input(label='Urban_Rural_encoded',help='''{(1, 'Urban'): , (0, 'Rural'): }''',min_value=0,max_value=1,value=1)
             Income_Level_encoded=st.number_input(label='Income_Level_encoded',help='''{(2, 'Middle'): , (1, 'Low'): , (0, 'High'): }''',min_value=0,max_value=2,value=1)
             Spouse_Working_encoded=st.number_input(label='Spouse_Working_encoded',help='''{(1, 'Yes'): , (0, 'No'): } ''',min_value=0,max_value=1,value=1)
             Inter_Religion_encoded=st.number_input(label='Inter_Religion_encoded',help=''' yes 1 no 0 ''',min_value=0,max_value=1,value=1)
             model_selection=st.selectbox("Choose the model",options=['All','ANYRandom','Logistic','Decision','Random','KNN','SVC'])
             submit=st.form_submit_button(label="submit",type='primary')
             st.write('--------------')
    if submit:
        st.warning("Form is submitting")
        time.sleep(2)
        st.warning("Form elements are validating")
        time.sleep(1)
        st.info("form is submitted ")
        st.balloons()
    else:
        st.error("Form is not submitted so please submit the form")
    model_dict={
        'Education_Level_encoded':Education_Level_encoded, 
        'Caste_Match_encoded':Caste_Match_encoded, 
        'Religion_encoded':Religion_encoded,
        'Urban_Rural_encoded':Urban_Rural_encoded, 
        'Income_Level_encoded':Income_Level_encoded, 
        'Spouse_Working_encoded':Spouse_Working_encoded,
        'Inter_Religion_encoded':Inter_Religion_encoded
    }
    df1=pd.DataFrame(data=model_dict,index=[0])
    st.code("{(2, 'Medium'), (0, 'High'), (1, 'Low'):}")
    if model_selection == 'Logistic':
        y_logistic=logistic.predict(df1)
        st.code(f"model name is {model_selection} and predicated value is {abs(y_logistic[0])}")
        if y_logistic == 0:
            st.info("Marital life was so happy")
        elif y_logistic == 1:
            st.warning("Martial life was not happy so sad, ready to take a divorce")
        else:
            st.error("Martital life was medium no happy and no sad just keep going")
    elif model_selection == 'Decision':
        y_decision=decision.predict(df1)
        st.code(f"model name is {model_selection} and predicated value is {abs(y_decision[0])}")
        if y_decision == 0:
            st.info("Marital life was so happy")
        elif y_decision == 1:
            st.warning("Martial life was not happy so sad, ready to take a divorce")
        else:
            st.error("Martital life was medium no happy and no sad just keep going")
    elif model_selection == 'Random':
         y_random=random.predict(df1)
         st.code(f"model name is {model_selection} and predicated value is {abs(y_random[0])}")
         if y_random == 0:
             st.info("Marital life was so happy")
         elif y_random == 1:
             st.warning("Martial life was not happy so sad, ready to take a divorce")
         else:
             st.error("Martital life was medium no happy and no sad just keep going")
             
    elif model_selection == 'KNN':
         y_knn=knn.predict(df1)
         st.code(f"model name is {model_selection} and predicated value is {abs(y_knn[0])}")
         if y_knn == 0:
             st.info("Marital life was so happy")
         elif y_knn == 1:
             st.warning("Martial life was not happy so sad, ready to take a divorce")
         else:
             st.error("Martital life was medium no happy and no sad just keep going")
    
    elif model_selection == 'SVC':
         y_svc=svc.predict(df1)
         st.code(f"model name is {model_selection} and predicated value is {abs(y_svc[0])}")
         if y_svc == 0:
             st.info("Marital life was so happy")
         elif y_svc == 1:
             st.warning("Martial life was not happy so sad, ready to take a divorce")
         else:
             st.error("Martital life was medium no happy and no sad just keep going")
    
    elif model_selection == 'ANYRandom':
         y_svc=svc.predict(df1)
         st.code(f"model name is {model_selection} and predicated value is {abs(y_svc[0])}")
         if y_svc == 0:
             st.info("Marital life was so happy")
         elif y_svc == 1:
             st.warning("Martial life was not happy so sad, ready to take a divorce")
         else:
             st.error("Martital life was medium no happy and no sad just keep going")
    else:
        if model_selection == 'All':
            y_logistic=logistic.predict(df1)
            st.code(f"model name is {model_selection} and predicated value is {abs(y_logistic[0])}")
            if y_logistic == 0:
                st.info("Marital life was so happy")
            elif y_logistic == 1:
                st.warning("Martial life was not happy so sad, ready to take a divorce")
            else:
                st.error("Martital life was medium no happy and no sad just keep going")
            y_decision=decision.predict(df1)
            st.code(f"model name is {model_selection} and predicated value is {abs(y_decision[0])}")
            if y_decision == 0:
                st.info("Marital life was so happy")
            elif y_decision == 1:
                st.warning("Martial life was not happy so sad, ready to take a divorce")
            else:
                st.error("Martital life was medium no happy and no sad just keep going")
            y_random=random.predict(df1)
            st.code(f"model name is {model_selection} and predicated value is {abs(y_random[0])}")
            if y_random == 0:
                st.info("Marital life was so happy")
            elif y_random == 1:
                st.warning("Martial life was not happy so sad, ready to take a divorce")
            else:
                st.error("Martital life was medium no happy and no sad just keep going")
            y_knn=knn.predict(df1)
            st.code(f"model name is {model_selection} and predicated value is {abs(y_knn[0])}")
            if y_knn == 0:
                st.info("Marital life was so happy")
            elif y_knn == 1:
                st.warning("Martial life was not happy so sad, ready to take a divorce")
            else:
                st.error("Martital life was medium no happy and no sad just keep going")
            st.write('----------------------------------')
    st.header("Data")
    st.dataframe(df1)
    st.table(df1)
    st.write('---------------------------')
    st.header('Input data charts')
    sns.set_theme(style="white", palette=['#ff4d01'])
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(data=df1, ax=ax) 
    sns.countplot(data=df1, ax=ax) 
    ax.set_title("Bar Plot")
    st.pyplot(fig)
            
except  Exception as e:
    st.code(str(e),language='text')
    st.code(traceback.format_exc())
else:
    st.info("No errors in the code")
finally:
    st.header("Thanks You..")
    st.feedback(options='thumbs')