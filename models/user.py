from pydantic import BaseModel, Field
from typing import Optional
import datetime


class UserModel (BaseModel):
    id: str = Field(...)
    sub: str = Field(...)
    email: str = Field(...)
    username: str = Field(...)
    is_active: bool = Field(...)
    created_at: datetime.datetime = Field(...)
    deleted_at: Optional[datetime.datetime] = Field(...)


class CreateUserModel (BaseModel):
    sub: str = Field(...)
    email: str = Field(...)
    username: str = Field(...)


class CreateUserRequestModel (BaseModel):
    email: str = Field(...)
    password: str = Field(...)
    username: str = Field(...)
