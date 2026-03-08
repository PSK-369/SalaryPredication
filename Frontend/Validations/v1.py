import streamlit as st
import traceback 
import time 
import datetime
import warnings
import requests
import os


warnings.filterwarnings("ignore")


try:
    st.set_page_config(page_title='Auth Form',layout='centered')
    st.title("User Login Form")
    st.write('-------------------------------')
    with st.form(key="user details",clear_on_submit=True,border=True):
        username=st.text_input(label="Enter the username",label_visibility='visible',type='default',help="username is always be some email id like xyz@gmail.com")
        password=st.text_input(label="Enter the password",label_visibility='visible',type='password',help="password showuld be caps lower numbers special chars along with 8 characters as minimum")
        submit=st.form_submit_button(label='submit',type='primary')
        if submit:
            if username == "" and password == "":
                st.error("useranme and password is empty values please fill the details....")
            st.info("Form is submitting....!")
            time.sleep(2)
            st.warning("Form elements are validatings : )")
            try:
                ApiURL=os.getenv("BackendURL",'http://localhost:8000')
                response=requests.post(url=f"{ApiURL}/login",json={"username":username,"password":password},timeout=10)
                if response.status_code == 200:
                    st.info("username and password vaildations is completed")
                    st.balloons()
                    st.switch_page('pages/main.py')
                elif response.status_code == 500:
                    st.error("backend auth server is seems not running")
                elif response.status_code == 404:
                    st.warning("some form input elements are missed")
                else:
                    st.warning("something is not running please check")
            except Exception as e:
                st.code(str(e),language='python')
                st.code(traceback.format_exc())
        else:
            st.error("form is not submitted")

except Exception as e1:
    st.code(str(e1),language='python')
    st.code(traceback.format_exc())
else:
    st.info("no errors in the code")
finally:
    st.write('--------------------------')
    st.info("Finally block is execusted")
    st.header("Thank You....")
    st.feedback(options='stars')