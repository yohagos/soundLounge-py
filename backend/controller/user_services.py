from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from schemas.users import UserBase
from models.models import User as UserModel

#def get_user_list():

def get_user_list(db: Session):
    return db.query(UserModel).all()

