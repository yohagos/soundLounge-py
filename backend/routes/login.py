from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.database import get_db
from models.models import User
from auth.hashing import verify_password
from auth.token import create_access_token

router = APIRouter(
    tags=['Authentication'],
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid username or password')
    if not verify_password(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Invalid username or password')
    access_token = create_access_token(data={"sub": user.username})
    return {'access_token': access_token, 'token_type': 'Bearer'}