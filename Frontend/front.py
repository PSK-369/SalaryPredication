import streamlit as st
import joblib
import traceback
import warnings
import datetime
import time
import requests
import os

warnings.filterwarnings("ignore")

try:
    st.set_page_config(page_title="User Auth Form", layout="centered")
    st.title("User Auth Form")
    with st.form(key="input values", border=True, clear_on_submit=True):
        username = st.text_input(
            label="Enter the username", label_visibility="visible", type="default"
        )
        password = st.text_input(
            label="Enter the password", label_visibility="visible", type="password"
        )
        submit = st.form_submit_button(label="submit", type="primary")
        if submit:
            st.info("Form is submitting")
            time.sleep(2)
            apiurl = os.getenv("BackURL", "http://localhost:2003")
            response = requests.post(
                url=f"{apiurl}/uservalidation",
                timeout=3,
                json=[{"username": username, "password": password}],
            )
            print(f"{apiurl}/uservalidation")
            if response.status_code == 200:
                st.info("username and password validations are completed")
                st.switch_page("pages/main.py")
            elif response.status_code == 404:
                st.info("some issue 404")
            elif response.status_code == 500:
                st.warning(
                    "backend service is not running please check and internal server error"
                )
            else:
                st.code(response.json())
        else:
            if (
                username == ""
                and password == ""
                and username == None
                and password == None
            ):
                st.error(
                    "usernae and password is either empty fields are none entered .....!"
                )
            st.warning("Form elements are not submitted")
except Exception as e:
    st.code(str(e), language="text")
finally:
    st.header("Final Block is executed")
    st.subheader("Thank you")
    st.feedback(options="faces")
