from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id            = Column(Integer, primary_key=True)
    username      = Column(String(30))
    name          = Column(String(30))
    password      = Column(String(30))
    email         = Column(String(30))
    country       = Column(String(30))
    sing          = Column(Boolean, default = False)
    guitar        = Column(Boolean, default = False)
    drums         = Column(Boolean, default = False)
    flute         = Column(Boolean, default = False)
    videos = relationship("Video", 
    back_populates="user")
    

class Video(Base):
    __tablename__ = 'Video'
    id            = Column(Integer, primary_key=True)
    user_id       = Column(Integer, ForeignKey("User.id"))
    video         = Column(String(140))
    description   = Column(String(140))
    publish       = Column(Boolean, default = True)
    other_video   = Column(Integer, default = 0)
    rating        = Column(Integer, default = 0)
    owner         = Column(Integer, default = 0)
    user = relationship("User", back_populates="videos")
    comments = relationship("Comment", back_populates="video")


    # ADD YOUR FIELD BELOW ID

class Comment(Base):
    __tablename__ = 'Comment'
    id            = Column(Integer, primary_key=True)
    video_id      = Column(Integer, ForeignKey("Video.id"))
    video         = Column(Integer, default = 0)
    comment       = Column(String(140))
    video = relationship("Video", back_populates="comments")
# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel