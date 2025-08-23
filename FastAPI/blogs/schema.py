from pydantic import BaseModel
from typing import List

# this schema we call it a pydantic model, also response_model refers to response_schema 
class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
      orm_mode = True
  
    
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    creator: ShowUser
    # we are using the Config() class with orm_mode=True so that it knows the we have a orm pydantic model
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

