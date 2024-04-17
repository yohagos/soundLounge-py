from fastapi import APIRouter, Depends, UploadFile, File, Header
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas.users import UserFull, UserBase
from schemas.followers import Followers
from controller.user import get_user_list, create_user, get_followers_for_test_user_1

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', response_model=List[UserFull])
def get_users(db: Session = Depends(get_db)):
    return get_user_list(db)

@router.post('')
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    """ 
    Create a new user 
    - username will be the email adress
    - password  is hashed before saving to database, min 8 length, atleast 1 uppercase, atleast 1 digit and 1 special character
    """
    return create_user(request, db)

@router.get('/followers', response_model=List[Followers])
def get_followers(db: Session = Depends(get_db)):
    return get_followers_for_test_user_1(db)