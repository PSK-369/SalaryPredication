import numpy as np
import pandas as pd
import statistics as sts
import seaborn as sns
import joblib
import streamlit as st
import time
from matplotlib import pyplot as plt
import streamlit as st
import requests
import os
import warnings

warnings.filterwarnings("ignore")


try:
    st.set_page_config(page_title="Auth Form", layout="centered")
    st.balloons()
    st.header("User Authentication Form")
    with st.form(key="Enter the user inputs", clear_on_submit=True):
        username = st.text_input(
            label="Enter the username",
            value="ShravanKumarPesala",
            label_visibility="visible",
            help="Enter the username like shravan Kumar Pesala",
        )
        useremail = st.text_input(
            label="Enter the useremail",
            value="Shravan123@gmail.com",
            label_visibility="visible",
            help="Enter the user email shravan@gmail.com",
        )
        userpassword = st.text_input(
            label="Enter the user password",
            value="Shravan123@",
            label_visibility="visible",
            help="Enter the user password",
        )
        submit = st.form_submit_button(
            label="click on the submit button", type="primary"
        )
        if submit:
            st.info("you clicked submit icon")
            st.warning("Form elaments are validatiing...")
            baseURL = os.getenv("backendURL", "http://localhost:8000")
            response = requests.post(
                url=f"{baseURL}/userauth",
                timeout=5,
                json={
                    "username": username,
                    "useremail": useremail,
                    "userpassword": userpassword,
                },
            )
            if response.status_code == 404:
                st.warning(
                    f"Invalid credentials: {response.json().get('detail', 'Unknown error')}"
                )
            elif response.status_code == 500:
                st.warning("Check backend service is running....!")
            elif response.status_code == 200:
                st.info("Login is successfull :)")
            else:
                st.error(
                    f"Some other is issue please check the validation backend code {response.text}"
                )
        else:
            if username == "" or useremail == "" or userpassword == "":
                st.warning("Form elemets are empty fields")
            else:
                st.error("Form elements are not submitted")

except Exception as e:
    st.code(f"{str(e)}", language="python")
else:
    st.info("no errors in the code")
finally:
    st.info("Final Block is executed")
    st.header("Thank You....!")
    st.balloons()
