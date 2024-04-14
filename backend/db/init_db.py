from sqlalchemy.orm import Session
from datetime import datetime
from schemas import users
from models import models

def create_init_users(db: Session):
    test_user_1 = models.User(firstname='Yosef', lastname='Yosef', username='yosef@yosef.de', password='yosefyosef', created_at=datetime.now())
    test_user_2 = models.User(firstname='Max', lastname='Max', username='max@max.de', password='maxmax', created_at=datetime.now())
    test_user_3 = models.User(firstname='James', lastname='James', username='james@james.de', password='james', created_at=datetime.now())
    test_user_4 = models.User(firstname='Ben', lastname='Ben', username='ben@ben.de', password='benben', created_at=datetime.now())
    test_user_5 = models.User(firstname='Mike', lastname='Mike', username='mike@mike.de', password='mikemike', created_at=datetime.now())
    test_user_6 = models.User(firstname='Paddy', lastname='Paddy', username='paddy@paddy.de', password='paddypaddy', created_at=datetime.now())
    if not check_if_user_exists(db, test_user_1):
        db.add(test_user_1)
    if not check_if_user_exists(db, test_user_2):
        db.add(test_user_2)
    if not check_if_user_exists(db, test_user_1):
        db.add(test_user_3)
    if not check_if_user_exists(db, test_user_1):
        db.add(test_user_4)
    if not check_if_user_exists(db, test_user_1):
        db.add(test_user_5)
    if not check_if_user_exists(db, test_user_1):
        db.add(test_user_6)
    db.commit()
    test_followers(db)

def check_if_user_exists(db: Session, user: models.User):
    user_exists = db.query(models.User).filter(models.User.username == user.username).first()
    return user_exists is not None

def test_followers(db: Session):
    user1 = db.query(models.User).filter(models.User.id == 1).first()
    user2 = db.query(models.User).filter(models.User.id == 2).first()
    
    if not db.query(models.Follower).filter(
        models.Follower.user_id == user1.id and models.Follower.follower_id == user2.id
        ).first():
        follower = models.Follower(user_id=user1.id, follower_id=user2.id)
        db.add(follower)
        db.commit()
