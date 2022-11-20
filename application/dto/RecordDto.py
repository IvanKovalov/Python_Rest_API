import logging
import numbers

from marshmallow import Schema, fields, validate

from application.validator.RecordValidator import UsersIDValidator, CategoriesIDValidator


class RecordDTO(Schema):
    id = fields.Str(dump_only=True)
    userId = UsersIDValidator()
    recordSum = fields.Integer(required=True)
    categoryId = CategoriesIDValidator()

    def set_user(self, user_id):
        self.userId = user_id

    def set_category(self, category_id):
        self.categoryId = category_id

    def set_sum(self, record_sum):
        self.recordSum = record_sum

    def get_user_id(self):
        return self.userId

    def get_category_id(self):
        return self.categoryId

    def get_sum(self):
        return self.recordSum
