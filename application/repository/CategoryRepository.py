
class CategoryRepository:
    def __init__(self):
        self.category_map = {}

    def save_category(self, category_entity):
        self.category_map[category_entity.get_id()] = category_entity.get_name()

    def get_category_by_id(self, category_id):
        return self.category_map.get(category_id)

    def get_all_category(self):
        return self.category_map
