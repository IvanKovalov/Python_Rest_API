class CategoryDTO:
    def __init__(self):
        self.category_name = None

    def __get_name__(self):
        return self.category_name

    def set_name(self, category_name):
        self.category_name = category_name

