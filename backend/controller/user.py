from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from datetime import datetime

from auth.hashing import get_password_hashed
from schemas.users import UserBase
from models.models import User as UserModel, Follower as FollowerModel


def get_user_list(db: Session):
    return db.query(UserModel).all()

def create_user(request: UserBase, db: Session):
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Username {request.username} already exists')
    new_user = UserModel(
        firstname=request.firstname, 
        lastname=request.lastname, 
        username=request.username, 
        password=get_password_hashed(request.password),
        created_at=datetime.now()
    )
    db.add(new_user)
    db.commit()


def get_followers_for_test_user_1(db: Session):
    user = db.query(UserModel).filter(UserModel.username == 'yosef@yosef.de').first()
    return db.query(FollowerModel).filter(FollowerModel.user_id == user.id).all()
