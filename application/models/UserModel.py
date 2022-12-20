from application.models.database import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(256), nullable=True)
    password = db.Column(db.String(256), nullable=True)

    category = db.relationship("CategoryModel", back_populates="user", lazy="dynamic")
    record = db.relationship("RecordModel", back_populates="user", lazy="dynamic")

    def get_id(self):
        return self.id

    def set_user_name(self, user_name):
        self.userName = user_name

    def get_user_name(self):
        return self.userName

