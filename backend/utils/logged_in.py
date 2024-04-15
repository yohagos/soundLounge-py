from sqlalchemy.orm import Session
from models.models import User

from . import logged_in

log_in: str

def get_user():
    return log_in

def set_logged_in(user: str):
    logged_in.log_in = user