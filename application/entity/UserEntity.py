class UserEntity:
    def __init__(self):
        self.user_name = None

    def set_name(self, user_name):
        self.user_name = user_name

    def __set_id__(self, user_id):
        self.id = user_id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.user_name

    def to_string(self):
        return "User_id: " + self.id + "User_name: " + self.user_name

    def __eq__(self, other):
        if self.id is other.get_id():
            return True
        else:
            return False

