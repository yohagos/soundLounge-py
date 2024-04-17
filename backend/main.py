from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import users, login, music

from db.database import engine, SessionLocal
from db.init_db import create_init_users
from models.models import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(users.router)
app.include_router(music.router)

Base.metadata.create_all(engine)

def init_db():
    db = SessionLocal()
    create_init_users(db)
    db.close()

init_db()
