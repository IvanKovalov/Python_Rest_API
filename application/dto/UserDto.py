class UserDTO:
    def __init__(self):
        pass

    def __get_name__(self):
        return self.name

    def __set_name__(self, name):
        self.name = name
