from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from schemas.users import UserBase
from models.models import User as UserModel, Follower as FollowerModel


def get_user_list(db: Session):
    return db.query(UserModel).all()

def get_followers_for_test_user_1(db: Session):
    user = db.query(UserModel).filter(UserModel.username == 'yosef@yosef.de').first()
    return db.query(FollowerModel).filter(FollowerModel.user_id == user.id).all()
