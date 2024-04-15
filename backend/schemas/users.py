from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str

class User(BaseModel):
    firstname: str
    lastname: str
    class Config:
        orm_mode = True

class UserFull(BaseModel):
    id: int
    firstname: str
    lastname: str
    username: str
    password: str
    created_at: datetime
    
    following: List[User]
    class Config:
        orm_mode = True


