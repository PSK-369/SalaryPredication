# class validations(BaseModel):
#     username: str = Field(..., description="Username")
#     password: str = Field(..., description="password")

#     @field_validator("username")
#     @classmethod
#     def username_validation_check(uname: str):
#         if len(username) <= 4:
#             st.warning("You entered below or = charcters")
#         elif "@gmail.com" not in username:
#             st.warning("@gmail is missed")
#         else:
#             st.info("username checks are comepleted and its ok")

#         @field_validator("password")
#         @classmethod
#         def password_validation_check(pass1: str):
#             if password <= 5:
#                 st.warning("you netered below or 5 digits passwords")
#             else:
#                 st.info("password is satisfied")
