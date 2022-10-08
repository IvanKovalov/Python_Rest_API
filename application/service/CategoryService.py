import logging

from application.entity.CategoryEntity import CategoryEntity
from application.repository.CategoryRepository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()
        self.category_counter = 1
        self.log = logging.getLogger(CategoryService.__name__)
        self.log.info("Created new instance of Category Service")

    def save_category(self, category_dto):
        category_entity = CategoryEntity()
        category_entity.set_id(self.category_counter)
        category_entity.set_name(category_dto.__get_name__())
        if category_dto.__get_name__() is None:
            self.log.error("Wrong data")
            return 404
        self.log.info("Saving Category id dict")
        self.category_repository.save_category(category_entity)
        self.category_counter = self.category_counter + 1

    def get_category(self, category_id):
        if type(category_id) is int:
            if category_id in self.category_repository.category_map.keys():
                self.log.info("Find category by id" + category_id)
                return self.category_repository.get_category_by_id(int(category_id))
            else:
                self.log.error("No category with such id")
                return Exception('No category with such id')
        else:
            self.log.error("Id not integer")
            return Exception('Id not integer')

    def get_all(self):
        self.log.info("Get all category")
        return self.category_repository.get_all_category()
