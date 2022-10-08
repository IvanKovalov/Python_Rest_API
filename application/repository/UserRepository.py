
class UserRepository:
    def __init__(self):
        self.user_map = {}

    def save_user(self, user_entity):
        self.user_map[user_entity.get_id()] = user_entity.get_name()

    def get_user_by_id(self, user_id):
        return self.user_map.get(user_id)

    def get_all_users(self):
        return self.user_map.items()
