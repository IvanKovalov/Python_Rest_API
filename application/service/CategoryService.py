from application.repository.CategoryRepository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def save_category(self, category_dto):
        category_name = category_dto.__get_name__()
        if category_name is None:
            return 404
        self.category_repository.save_category(category_name)

    def get_category(self, category_id):
        if type(category_id) is int:
            if category_id in self.category_repository.category_map.keys():
                return self.category_repository.get_category_by_id(int(category_id))
            else:
                return Exception('No category with such id')
        else:
            return Exception('Id not integer')

    def get_all(self):
        return self.category_repository.get_all_category()
