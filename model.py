from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__  = 'Users'
    id             = Column(Integer, primary_key=True)
    username       = Column(String(30))
    name           = Column(String(30))
    password       = Column(String(30))
    email          = Column(String(30))
    country        = Column(String(30))
    sing           = Column(Boolean, default = False)
    guitar         = Column(Boolean, default = False)
    drums          = Column(Boolean, default = False)
    flute          = Column(Boolean, default = False)

class Videos(Base):
    __tablename__  = 'Videos'
    id             = Column(Integer, primary_key=True)
    video          = Column(String(140))
    description    = Column(String(140))
    publish        = Column(Boolean, default = True)
    otherVideo     = Column(Integer, default = None)
    comment        = Column(String(140), default = None)
    rating         = Column(Integer, default = 0)
    poster         = Column(String(140))
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel