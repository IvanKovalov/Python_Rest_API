from application.repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def save_user(self, user_dto):
        user_name = user_dto.__get_name__()
        if user_name is None:
            return 404
        self.user_repository.save_user(user_name)

    def get_user(self, id):
        return self.user_repository.get_user_by_id(int(id))
