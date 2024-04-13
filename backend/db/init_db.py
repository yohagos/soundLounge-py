from sqlalchemy.orm import Session
from schemas import users
from models import models

def create_init_users(db: Session):
    test_user_1 = models.User(id=1, firstname='Yosef', lastname='Yosef', email='yosef@yosef.de', password='yosefyosef')
    db.add(test_user_1)
    db.commit()
