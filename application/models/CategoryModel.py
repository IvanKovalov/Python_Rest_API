from application.models.database import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(256), nullable=True)
    ownerId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    private = db.Column(db.Boolean, nullable=True, default=False)

    user = db.relationship("UserModel", back_populates="category")
    record = db.relationship("RecordModel", back_populates="category", lazy="dynamic")

    def get_id(self):
        return self.id

    def set_category_name(self, category_name):
        self.categoryName = category_name

    def get_category_name(self):
        return self.categoryName

    def set_owner_id(self, owner_id):
        self.ownerId = owner_id

    def get_owner_id(self):
        return self.ownerId

    def set_private(self, private):
        self.private = private

    def is_private(self):
        return self.private
