from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime

from db.database import Base


class Follower(Base):
    __tablename__='followers'
    id = Column(Integer,primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    follower_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    following = relationship('User', secondary='followers',
                             primaryjoin=id == Follower.user_id,
                             secondaryjoin=id == Follower.follower_id,
                             cascade="all, delete",
                             backref='followers')
    music = relationship('Music', back_populates='creator')
    
class Music(Base):
    __tablename__ = 'musics'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    track = Column(LargeBinary)
    uploaded_at = Column(DateTime)
    uploaded_by = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='music')

