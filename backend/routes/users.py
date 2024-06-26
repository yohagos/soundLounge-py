from fastapi import APIRouter, Depends, UploadFile, File, Header
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas.users import UserFull, UserBase, User
from schemas.followers import Followers
from controller.user import get_user_list, create_user, delete_user, get_follower_for_user

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', response_model=List[UserFull])
def get_users(db: Session = Depends(get_db)):
    """ 
    Get a list of all Users
    """
    return get_user_list(db)

@router.post('')
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    """ 
    Create a new User 
    - username will be the email adress
    - password  is hashed before saving to database, min 8 length, atleast 1 uppercase, atleast 1 digit and 1 special character
    """
    return create_user(request, db)

@router.delete('')
async def remove_user(username: str, db: Session = Depends(get_db)):
    delete_user(username, db)
    return 'Done'

@router.get('/{user_id}/followers', response_model=List[User])
def get_followers(user_id: int, db: Session = Depends(get_db)):
    """ 
    Get Followers for specific User 
    """
    return get_follower_for_user(db, user_id)