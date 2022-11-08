import logging

from application.entity.UserEntity import UserEntity
from application.repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_counter = 1
        self.log = logging.getLogger(UserService.__name__)

        self.log.info("Created new instance of User Service")

    def save_user(self, user_dto):
        if user_dto.__get_name__() is None:
            self.log.error("Wrong data")
            return 403
        user_entity = UserEntity()
        user_entity.set_name(user_dto.__get_name__())
        user_entity.__set_id__(self.user_counter)
        self.user_counter = self.user_counter + 1
        self.log.info("Saving user")
        self.user_repository.save_user(user_entity)

    def get_user(self, id):
        self.log.info("Get user by id")
        return self.user_repository.get_user_by_id(int(id))
