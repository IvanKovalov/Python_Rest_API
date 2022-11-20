from datetime import datetime

from sqlalchemy import func

from application.models.database import db


class RecordModel(db.Model):
    __tablename__ = "record"
    id = db.Column(db.Integer, primary_key=True)
    recordSum = db.Column(db.Float, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    categoryId = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    createdAt = db.Column(db.TIMESTAMP, server_default=func.now())

    user = db.relationship("UserModel", back_populates="record")
    category = db.relationship("CategoryModel", back_populates="record")

    def get_id(self):
        return self.id

    def set_record_sum(self, record_sum):
        self.recordSum = record_sum

    def get_record_sum(self):
        return self.recordSum

    def set_user_id(self, user_id):
        self.userId = user_id

    def get_user_id(self):
        return self.userId

    def set_category_id(self, category_id):
        self.categoryId = category_id

    def get_category_id(self):
        return self.categoryId

    def get_creation_time(self):
        return self.createdAt



