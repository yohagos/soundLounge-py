from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

from db.database import Base

user_follower_table = Table(
    'user_follower', 
    Base.metadata, 
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('follower_id', ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    followers = relationship('Follower', back_populates='followers', secondary=user_follower_table)
    #followed_by = relationship('Follower', backref='followed', foreign_keys='Follower.user_id')

    
class Follower(Base):
    __tablename__='followers'
    id = Column(Integer,primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    follower_id = Column(Integer, ForeignKey('users.id'))

    users = relationship('User',  viewonly=True, secondary=user_follower_table, back_populates='users')

    """ followed = relationship('User', foreign_keys=[user_id])
    follower = relationship('User', foreign_keys=[follower_id]) """
