import numpy as np
import pandas as pd
import statistics as sts
import seaborn as sns
import joblib
import streamlit as st
import time
from matplotlib import pyplot as plt
from fastapi import FastAPI, HTTPException, status
from typing import List, Dict, Optional, Any, Set
from pydantic import BaseModel, Field, field_validator, model_validator
import warnings


warnings.filterwarnings("ignore")

application = FastAPI(
    title="Basic Auth Form",
    version="1.0.0",
    summary="It is a basic auth form backend code form",
)


class UserModel(BaseModel):
    username: str = Field(
        ...,
        title="Enter the username",
        description="Enter the username without any special symbols",
        examples=["shravan kumar"],
    )
    useremail: str = Field(
        ...,
        title="Enter the useremail",
        description="Enter the user email",
        examples=["shravan@123@gmail.com"],
    )
    userpassword: str = Field(
        ...,
        titke="Enter the password",
        description="Enter the password details with special charcters",
        examples=["shravan123@Kumar"],
    )

    @field_validator("username")
    @classmethod
    def username_validation_check(cls, username: str) -> str:
        lower_username = str.lower(username)
        remove_the_trimspaces = str.strip(lower_username)
        if len(remove_the_trimspaces) <= 10:
            raise HTTPException(
                status_code=404, detail="username length is not matched"
            )
        return remove_the_trimspaces

    @field_validator("useremail")
    @classmethod
    def user_email_validation_check(cls, useremail: str) -> str:
        if "@gmail.com" not in useremail:
            raise HTTPException(status_code=404, detail="@gmail.com is missed")
        return useremail

    @field_validator("userpassword")
    @classmethod
    def user_password_validation_check(cls, userpassword: str) -> str:

        lowercaseCheck = any(c.islower() for c in userpassword)
        uppercaseCheck = any(c.isupper() for c in userpassword)
        digitsCheck = any(c.isdigit() for c in userpassword)
        specialChars = any(c in "!@#$%^&*/?" for c in userpassword)

        if not (lowercaseCheck and uppercaseCheck and digitsCheck and specialChars):
            raise ValueError(
                "Password must contain: lowercase, uppercase, digit, and special char (!@#$%^&*/?)"
            )

        return userpassword

    @model_validator(mode="after")
    @property
    def final_validations_checks(self):
        if (
            self.username == "ShravanKumarPesala"
            and self.useremail == "Shravan123@gmail.com"
            and self.userpassword == "Shravan123@"
        ):
            return {
                "username": self.username,
                "useremail": self.useremail,
                "userpassword": self.userpassword,
            }
        else:
            raise HTTPException(
                status_code=404, detail="root user credentails are not mateched"
            )


userDetails: List[UserModel]


@application.get("/")
def root_health_check():
    return {"healthcheck": "passed"}


@application.get("/userdetailscheck")
def user_details_check():
    return userDetails


@application.post("/userauth")
def user_details_post(userdetails: UserModel):
    if (
        userdetails.username == "ShravanKumarPesala"
        and userdetails.useremail == "Shravan123@gmail.com"
        and userdetails.userpassword == "Shravan123@"
    ):
        return {
            "username": userdetails.username,
            "useremail": userdetails.useremail,
            "userpassword": userdetails.userpassword,
            "auth details": "successfull login",
        }
    raise HTTPException(status_code=400, detail="user credentails are not matched")
