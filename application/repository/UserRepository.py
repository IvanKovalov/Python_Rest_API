from flask import abort
from sqlalchemy.exc import IntegrityError

from application.models.UserModel import UserModel


class UserRepository:
    def __init__(self, db):
        self.db = db

    def save_user(self, user_model):
        try:
            self.db.session.add(user_model)
            self.db.session.commit()
        except IntegrityError:
            abort(500, "Failed creating user")

    def get_user_by_id(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def get_all_users(self):
        return UserModel.query.all()
