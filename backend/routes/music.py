from fastapi import Depends, HTTPException, status, APIRouter, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
from tempfile import NamedTemporaryFile

from schemas.music import MusicBase
from controller.music import save_music
from db.database import get_db

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('', response_model=List[MusicBase])
async def save_music(
    title: str = Form(...), artist: str = Form(...), genre: str = Form(...),
    db: Session = Depends(get_db), file: UploadFile = File(...)
):
    """ with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await file.read())
        temp_file.close()
        with open(temp_file.name, 'rb') as f:
            content = f.read()
            save_music(title, artist, genre, content, db) """
    return 'Done'
