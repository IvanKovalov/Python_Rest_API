class UserDTO:
    def __init__(self):
        self.user_name = None

    def __get_name__(self):
        return self.user_name

    def set_name(self, user_name):
        self.user_name = user_name
