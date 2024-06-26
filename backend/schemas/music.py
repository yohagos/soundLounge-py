from pydantic import  BaseModel
from typing import List, Optional
from datetime import datetime

from schemas.users import User

class MusicBase(BaseModel):
    id: int
    title: str
    artist: str
    genre: str
    uploaded_at: datetime
    uploaded_by: int
    track: str
    creator: User

class Music(BaseModel):
    title: str
    artist: str
    genre: str
    track: str
    uploaded_at: datetime
    uploaded_by: int

    class Config:
        from_attributes = True
