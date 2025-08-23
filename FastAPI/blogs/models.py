from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



# we call this just the sqlalchemy model, for the db

class Blog(Base):
    __tablename__ = "FastAPI"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    creator = relationship("User", back_populates="blogs")
    user_id = Column(Integer, ForeignKey('User.id'))


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="creator")