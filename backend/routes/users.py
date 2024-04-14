from fastapi import APIRouter, Depends, UploadFile, File, Header
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas.users import UserFull
from schemas.followers import Followers
from controller.user_services import get_user_list, get_followers_for_test_user_1

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', response_model=List[UserFull])
def get_users(db: Session = Depends(get_db)):
    return get_user_list(db)

@router.get('followers', response_model=List[Followers])
def get_followers(db: Session = Depends(get_db)):
    return get_followers_for_test_user_1(db)