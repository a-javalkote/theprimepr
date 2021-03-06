from pydantic import BaseModel, Field, Json
from datetime import datetime
from typing import List, Optional
from pydantic.schema import schema


class SiteInfo(BaseModel):
    name: Optional[str]
    value: Json

    class Config:
	    orm_mode=True

class Category(BaseModel):
    name: str
    slug: str
    description: str
    parent_id: int
    counter:int
    status: int

    class Config:
	    orm_mode=True

class UpdateCategory(BaseModel):
    name: str
    slug: str
    description: str
    parent_id: int

    class Config:
        orm_mode=True

class SingleCategory(BaseModel):
    id: int
    name: str
    slug: str
    description: str 

    class Config():
        orm_mode = True

class CategoryForPost(BaseModel):
    id: int
    name: str
    slug: str

    class Config():
        orm_mode = True


class AutherName(BaseModel):
    id: int
    first_name: str
    last_name: str 

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Register(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email_id: str
    role_id: int = 2


class ChangePassword(BaseModel):
    password: str
    
    class Config:
	    orm_mode=True

class VerifyEmailId(BaseModel):
    email_verify_code: str

class UpdateUsers(VerifyEmailId):
    first_name: str
    last_name: str

    class Config:
	    orm_mode=True

class Users(UpdateUsers):
    id: int
    username: str
    password: str
    role_id: int = 2
    status: int

    class Config:
	    orm_mode=True

    
class Post(BaseModel):
    title: str
    slug: str
    short_desc: str
    description: str
    meta_desc: str
    meta_keyword: str
    post_img: str
    post_tag: str
    category_id: int
    auther_id: int
    approved:int
    created_datetime: datetime
    published_datetime: datetime
    status: int

    class Config:
	    orm_mode=True

class SinglePost(BaseModel):
    id: int
    title: str
    slug: str
    description: str 
    post_tag: str
    post_img: str
    category: CategoryForPost
    auther : AutherName
    meta_desc: str
    meta_keyword: str 
    published_datetime: datetime   
    
    class Config():
        orm_mode = True

class UpdatePost(BaseModel):
    title: str
    slug: str
    short_desc: str
    description: str 
    post_tag: str
    category: CategoryForPost
    auther : AutherName
    meta_desc: str
    meta_keyword: str   
    
    class Config():
        orm_mode = True

class CategorywisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str 
    post_img: str
    post_tag: str
    auther : AutherName  
    published_datetime: datetime   
    
    class Config():
        orm_mode = True

class AutherwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str 
    post_img: str
    post_tag: str
    category: CategoryForPost
    published_datetime: datetime   
    
    class Config():
        orm_mode = True

class TagwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str
    post_img: str
    post_tag: str 
    category: CategoryForPost
    auther : AutherName 
    published_datetime: datetime   
    
    class Config():
        orm_mode = True

class SerachwisePost(BaseModel):
    id: int
    title: str
    slug: str
    short_desc: str
    post_img: str
    post_tag: str
    category: CategoryForPost
    auther : AutherName
    published_datetime: datetime   
    
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
