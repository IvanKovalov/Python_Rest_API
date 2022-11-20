import logging

from application.models.CategoryModel import CategoryModel
from application.models.database import db
from application.repository.CategoryRepository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository(db)
        self.category_counter = 1
        self.log = logging.getLogger(CategoryService.__name__)
        self.log.info("Created new instance of Category Service")

    def save_category(self, category_dto):
        category = CategoryModel(**category_dto)
        self.category_repository.save_category(category)
        return category

    def get_category(self, category_id):
        # if type(category_id) is int:
        #     if category_id in self.category_repository.category_map.keys():
        #         self.log.info("Find category by id" + category_id)
        #         return self.category_repository.get_category_by_id(int(category_id))
        #     else:
        #         self.log.error("No category with such id")
        #         return Exception('No category with such id')
        # else:
        #     self.log.error("Id not integer")
        #     return Exception('Id not integer')
        self.log.info("Get category by id: " + category_id)
        return self.category_repository.get_category_by_id(int(category_id))

    def get_all(self):
        self.log.info("Get all category")
        return self.category_repository.get_all_category()
