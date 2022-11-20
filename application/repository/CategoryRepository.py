from flask import abort
from sqlalchemy.exc import IntegrityError

from application.models.CategoryModel import CategoryModel


class CategoryRepository:
    def __init__(self, db):
        self.db = db

    def save_category(self, category_model):
        try:
            self.db.session.add(category_model)
            self.db.session.commit()
        except IntegrityError:
            abort(500, "Failed creating category")

    def get_category_by_id(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        return category

    def get_all_category(self):
        return CategoryModel.query.all()
