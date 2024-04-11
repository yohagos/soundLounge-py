from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str

class UserFull(BaseModel):
    id: int
    firstname: str
    lastname: str
    username: str
    password: str
    created_at: str
