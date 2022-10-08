class CategoryEntity:
    def __init__(self):
        self.category_id = None
        self.category_name = None

    def set_name(self, category_name):
        self.category_name = category_name

    def set_id(self, category_id):
        self.category_id = category_id

    def get_id(self):
        return self.category_id

    def get_name(self):
        return self.category_name

    def to_string(self):
        return "Category id: " + self.category_id + "\n" + "Category_name: " + self.category_name

    def __eq__(self, other):
        if self.category_id is other.get_id():
            return True
        else:
            return False
