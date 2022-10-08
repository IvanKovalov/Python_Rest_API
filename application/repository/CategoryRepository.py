
class CategoryRepository:
    def __init__(self):
        self.category_map = {}
        self.category_counter = 1

    def save_category(self, category_name):
        self.category_map[self.category_counter] = category_name
        self.category_counter = self.category_counter + 1

    def get_category_by_id(self, category_id):
        return self.category_map.get(category_id)

    def get_all_category(self):
        return self.category_map
