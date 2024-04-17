from sqlalchemy.orm import Session
import logging

from models.models import Music as MusicModel, User as UserModel
from utils.util import create_timestamp

logging.basicConfig(level=logging.info)

def save_music(title: str, artist: str, genre: str, track: bytes, db: Session):
    user = db.query(UserModel).filter(UserModel.id == 1).first()
    music = MusicModel(title=title, artist=artist, genre=genre, track=track, uploaded_at=create_timestamp(), uploaded_by=user.id)
    db.add(music)
    db.commit()
    logging.info(music)
    return music