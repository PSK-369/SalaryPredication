import warnings
from pydantic import BaseModel, Field, field_validator
from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

warnings.filterwarnings("ignore")
app = FastAPI(title='Auth Form', version='1.0.0', summary='Auth form')

class UserClass(BaseModel):
    username: str = Field(..., description='Username', examples=['xyz@gmail.com'])
    password: str = Field(..., description='Password', examples=['shravan@123S'])

    @field_validator('username')
    @classmethod
    def username_len_check(cls, value: str) -> str:
        if len(value) <= 2:
            raise HTTPException(status_code=422, detail="Username length must be > 2")
        return value

    @field_validator('username')
    @classmethod
    def username_gmail_check(cls, value: str) -> str:
        if "@gmail.com" not in value:
            raise HTTPException(status_code=422, detail="Username must contain @gmail.com")
        return value

    @field_validator('password')
    @classmethod
    def password_len_check(cls, value: str) -> str:
        if len(value) <= 5:
            raise HTTPException(status_code=422, detail="Password must be > 5 characters")
        return value

    @field_validator('password')
    @classmethod
    def password_strong_check(cls, value: str) -> str:
        has_lower = any(c.islower() for c in value)
        has_upper = any(c.isupper() for c in value)
        has_digit = any(c.isdigit() for c in value)
        has_special = any(c in '!@#$%^&*' for c in value)
        if not (has_lower and has_upper and has_digit and has_special):
            raise HTTPException(status_code=422, detail="Password strength check failed")
        return value


user_store: List[UserClass] = []

@app.get("/")
def health_check():
    return {"status": "Auth server is running"}

@app.get("/users", response_model=List[UserClass])
def get_all_users():
    return user_store

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserClass):
    # Check if user already exists
    if any(u.username == user.username for u in user_store):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_store.append(user)
    return {"message": "User registered successfully", "username": user.username}

@app.post("/login")
def login_user(credentials: UserClass):
    # Hardcoded root check (for demo)
    if credentials.username == 'shravan123@gmail.com' and credentials.password == 'Shravan123@':
        return {"message": "Login successful", "access_type": "root", "username": credentials.username}
    
    # Check registered users
    for user in user_store:
        if user.username == credentials.username and user.password == credentials.password:
            return {"message": "Login successful", "username": credentials.username}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")