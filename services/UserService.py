
from sqlalchemy.orm import Session

from models.user import CreateUserModel, CreateUserRequestModel, UserModel
from repositories.UsersRepository import UsersRepository
from utils.ConverterUtil import ConverterUtil

converterUtil = ConverterUtil()

usersRepository = UsersRepository()


class UserService:

    async def create_user(
        self,
        user: CreateUserRequestModel,
        db: Session
    ):
        try:
            checkUser = await usersRepository.find_user_by_email(user.email, db)
            print("checkUser", checkUser)
            if checkUser:
                return {
                    "message": "Email already in use",
                    "data": converterUtil.user_converter(checkUser),
                    "status": 404
                }

            userCreated = await usersRepository.create_user(user, db)

            return {
                "message": "User created",
                "data": converterUtil.user_converter(userCreated),
                "status": 201
            }
        except Exception as error:
            return {
                "message": "Erro interno do servidor",
                "data": str(error),
                "status": 500
            }
