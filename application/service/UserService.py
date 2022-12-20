import logging
from passlib.hash import pbkdf2_sha256
from application.models.UserModel import UserModel
from application.models.database import db
from application.repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository(db)
        self.log = logging.getLogger(UserService.__name__)
        self.log.info("Created new instance of User Service")

    def save_user(self, user_dto):
        user = UserModel(
            userName=user_dto["userName"], password=pbkdf2_sha256.hash(user_dto["password"]),
        )
        self.user_repository.save_user(user)
        self.log.info("Saving new User")
        return user

    def get_user(self, user_id):
        self.log.info("Get user by id: " + user_id)
        return self.user_repository.get_user_by_id(int(user_id))
