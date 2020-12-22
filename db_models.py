from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, DateTime
from sqlalchemy.orm import relationship
from database import Base, session, engine

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' %self.username

class Tweets(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    screen_name = Column(String(50), nullable=False)
    text = Column(String(50), nullable=False)
    user_data = relationship('TwitterUser', backref='twitter_user')
    def __repr__(self):
        return '<Tweets %r>' %self.id

class TwitterUser(Base):
    __tablename__ = 'twitteruser'

    id = Column(Integer, primary_key=True)
    screen_name = Column(String(50), nullable=False)
    followers = Column(Integer, nullable=False)
    following = Column(Integer, nullable=False)
    tweets = relationship('Tweets', backref='texts')
    def __repr__(self):
        return '<TwitterUser %r>' %self.screen_name

    