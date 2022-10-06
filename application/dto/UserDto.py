class UserDTO:
    def __init__(self):
        self.name = None

    def __get_name__(self):
        return self.name

    def set_name(self, name):
        self.name = name
