class ConverterUtil:
    def user_converter(self, user):
        print("user_converter", user)
        userParsed = {
            "id": user.id,
            "sub": user.sub,
            "email": user.email,
            "username": user.username,
            "is_active": user.is_active,
            "created_at": user.created_at,
            "deleted_at": user.deleted_at
        }

        print("userParsed", userParsed)

        return userParsed
