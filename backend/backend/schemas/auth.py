from pydantic import BaseModel, EmailStr, Field, field_validator
import phonenumbers as pn
from phonenumbers.phonenumberutil import NumberParseException
from backend.core.secutiry import password_schema


class RegisterUser(BaseModel):
    email: EmailStr
    password: str
    full_name: str = Field(max_length=320)
    phone: str | None = Field(default=None, max_length=20)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v:str):
        try:
            parsed = pn.parse(v, None)
        except NumberParseException:
            pass
        if any(c.isalpha() for c in  v):
            raise ValueError("Invalid number")
        return v


    @field_validator("password")
    @classmethod
    def validate_password(cls, v:str):
        if not password_schema.validate(v):
            raise ValueError("Invalid password")
        return v

class LoginUser(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v:str):
        if not password_schema.validate(v):
            raise ValueError("Invalid password")
        return v

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'

class TokenSchema(BaseModel):
    refresh_token: str