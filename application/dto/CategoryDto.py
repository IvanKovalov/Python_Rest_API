from marshmallow import fields, Schema

from application.validator.RecordValidator import UsersIDValidator


class CategoryDTO(Schema):
    id = fields.Str(dump_only=True)
    categoryName = fields.Str(required=True)
    ownerId = UsersIDValidator()
    private = fields.Boolean(required=False)
    def __get_name__(self):
        return self.categoryName

    def set_name(self, category_name):
        self.categoryName = category_name
