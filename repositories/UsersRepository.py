import datetime

from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal
from entities.user import User
from models.user import CreateUserModel, UserModel
from uuid import uuid4


class UsersRepository:

    async def create_user(
            self,
            user: CreateUserModel,
            db: Session
    ) -> UserModel:
        print("UsersRepository-create_user", user.email)
        db_user = User(email=user.email,
                       username=user.username, sub=uuid4())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    async def find_user_by_email(
            self,
            email: str,
            db: Session
    ):
        db_user = db.query(User).filter(User.email == email).first()
        return db_user
