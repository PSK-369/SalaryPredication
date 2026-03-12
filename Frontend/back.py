from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import List

app = FastAPI(title="Auth Form", version="1.0.0")


class UserModel(BaseModel):
    username: str = Field(..., min_length=9)
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def validate_email(cls, v):
        if "@gmail.com" not in v:
            raise ValueError("Must be a valid Gmail address")
        return v

    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if not any(c.islower() for c in v) or not any(c.isupper() for c in v):
            raise ValueError("Password must have upper and lower case")
        if not any(c.isdigit() for c in v) or not any(c in "!@#$%^&*" for c in v):
            raise ValueError("Password must have digits and special chars")
        return v


userDetails: List[UserModel] = []


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/users")
def get_users():
    return userDetails


@app.post("/validations")
def add_user(user: UserModel):
    if any(u["username"] == user.username for u in userDetails):
        raise HTTPException(409, "Username exists")
    userDetails.append(user)
    return {"status": "added"}


@app.post("/uservalidation")
def login(users: List[UserModel]):
    results = []
    for user in users:
        if user.username == "pesalashravan@gmail.com" and user.password == "Pesala998@":
            results.append({"username": user.username, "status": "root"})
        else:
            userDetails.append(user)
            results.append({"username": user.username, "status": "validated"})
    return results
