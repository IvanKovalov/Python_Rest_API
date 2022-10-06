class UserEntity:
    def __init__(self):
        self.name = None

    def set_nam(self, name):
        self.name = name

    def __set_id__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
