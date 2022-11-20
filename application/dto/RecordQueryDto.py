from marshmallow import Schema, fields

from application.validator.RecordValidator import UsersIDValidator, CategoriesIDValidator


class RecordQueryDto(Schema):
    userId = UsersIDValidator()
    categoryId = CategoriesIDValidator()
