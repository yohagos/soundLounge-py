from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from datetime import datetime
import logging

from auth.hashing import get_password_hashed
from schemas.users import UserBase
from models.models import User as UserModel, Follower as FollowerModel

logging.basicConfig(level=logging.INFO)


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

def delete_user(username: str, db: Session):
    try:
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if user:
            # Lösche die Einträge in der Follower-Tabelle, die den Benutzer als follower_id haben
            db.query(UserModel).filter(FollowerModel.follower_id == user.id).delete()
            # Lösche die Einträge in der Follower-Tabelle, die den Benutzer als user_id haben
            db.query(FollowerModel).filter(FollowerModel.user_id == user.id).delete()
            # Lösche den Benutzer selbst
            db.delete(user)
            db.commit()
            logging.info(f"Benutzer {username} und seine Follower wurden erfolgreich gelöscht.")
        else:
            logging.warning(f"Benutzer {username} wurde nicht gefunden.")
    except Exception as e:
        logging.error(f"Fehler beim Löschen des Benutzers {username}: {str(e)}")
        db.rollback()

def get_follower_for_user(db: Session, user_id: int):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user:
        return user.following
    return None
