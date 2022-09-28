from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str



class PostResponse(PostBase):
    id: int
    published: bool = True
    user_id = int
    user = UserOut
    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    hashed_password: str




class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]= None