from fastapi import APIRouter, Depends, UploadFile, File, Header
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas.users import UserFull
from controller.user_services import get_user_list

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('', response_model=List[UserFull])
def get_users(db: Session = Depends(get_db)):
    return get_user_list(db)