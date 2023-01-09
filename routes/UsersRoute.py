from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import CreateUserModel, CreateUserRequestModel, UserModel
from services.UserService import UserService
from db.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


userService = UserService()


@router.post('/', status_code=201, response_model=UserModel, response_description="Create a new user")
async def rota_criar_usuario(
    user: CreateUserRequestModel,
    db: Session = Depends(get_db)
):
    result = await userService.create_user(user, db)

    if result["status"] != 201:
        raise HTTPException(
            status_code=result["status"], detail=result["message"])
    else:
        return result["data"]
