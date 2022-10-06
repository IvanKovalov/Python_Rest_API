from application.entity.UserEntity import UserEntity


class UserRepository:
    def __init__(self):
        self.user_map = {}
        self.user_counter = 1

    def save_user(self, user_name):
        user_entity = UserEntity()
        user_entity.set_nam(user_name)
        user_entity.__set_id__(self.user_counter)
        self.user_map.pop(self.user_counter, user_entity)
        self.user_map[self.user_counter] = user_entity
        self.user_counter = self.user_counter + 1

    def get_user_by_id(self, user_id):
        return self.user_map.get(user_id)

    def get_all_users(self):
        return self.user_map.items()
