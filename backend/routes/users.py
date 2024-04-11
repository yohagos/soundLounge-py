from fastapi import APIRouter, Depends, UploadFile, File, Header
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from ..schemas.users import UserBase, UserFull

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', response_model=List[UserFull])
def get_users():
    return get_user_list()