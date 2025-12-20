import streamlit as st 
import pandas as pd 
import joblib


try:
    model=joblib.load(r'salary_predication.joblib')
    st.title(" Employee Salary predications ")
    st.write("Model is loaded succesfully ....!")

    st.balloons()

    st.sidebar.write("Enter the input parameters")
    with st.form(key="input-values"):
        with st.sidebar:
            Age=st.number_input('Age',min_value=19,max_value=65,value=35,help='age is between 19 to 65')
            Gender=st.number_input('Gender',min_value=1,max_value=2,value=1,help='male is 1 and female is 2')
            Education_level=st.number_input('Education',min_value=1,max_value=3,value=2,help='1 -> is Bachlors  2 -> is for masters and 3 --> is for PHD')
            submit_button=st.form_submit_button(label='SUBMIT')

    if submit_button:
        data1={
            'Age': Age,
            'gender_encoded': Gender,
            'Education_Level_encoded':Education_level
        }            

        df=pd.DataFrame(data=data1,index=[0])
        predications=model.predict(df)
        st.write(f"The predidated salary is ===> INR [ {predications[0]:,.4f} ]")
        st.write('Thank You ......!')
        st.balloons()


except Exception as e:
    st.error(f"the error is {e}")
    st.code(f"{str(e)} ", language='python')

else:
    print("no errors in the model")

finally:
    print("Finaly Block is exceuted succsufully")   