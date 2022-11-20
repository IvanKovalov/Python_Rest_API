import numbers

from flask import abort
from marshmallow import fields, ValidationError

from application.models.CategoryModel import CategoryModel
from application.models.UserModel import UserModel


class UsersIDValidator(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return 0
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            if not isinstance(value, numbers.Integral):
                abort(400, "UserId not integer")
                raise ValueError
            user = UserModel.query.get(value)
            if user is None:
                abort(400, "User with such id not exist")
                raise ValueError
            return value
        except ValueError as error:
            raise ValidationError("UserId wrong data") from error


class CategoriesIDValidator(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return 0
        return value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            if not isinstance(value, numbers.Integral):
                abort(400, "Category id not integer")
                raise ValueError
            category = CategoryModel.query.get(value)
            if category is None:
                abort(400, "Category with such id not exist")
                raise ValueError
            return value
        except ValueError as error:
            raise ValidationError("CategoryId wrong data") from error

