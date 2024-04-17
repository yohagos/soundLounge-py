from pydantic import BaseModel, validator, EmailStr, constr
from typing import Optional, List
from datetime import datetime
import string

class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: EmailStr
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8 or len(v) > 60:
            raise ValueError("Password must be between 8 and 60 characters")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit letter")
        if not any(c in "+-_!?$&#" for c in v):
            raise ValueError('Das Passwort muss mindestens ein Sonderzeichen enthalten.')
        return v

class User(BaseModel):
    firstname: str
    lastname: str
    class Config:
        orm_mode = True

class UserFull(BaseModel):
    id: int
    firstname: str
    lastname: str
    username: EmailStr
    password: str
    created_at: datetime
    
    following: List[User]
    class Config:
        orm_mode = True


