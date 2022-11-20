import logging
import os

from flask import Flask

from application.models.database import db
from application.resources.CategoryController import category_service, category_blp
from application.resources.RecordContoller import record_blp
from application.resources.UserContoller import user_blp, user_service

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
app.register_blueprint(user_blp)
app.register_blueprint(category_blp)
app.register_blueprint(record_blp)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def hello():
    return 'Hello, World!'
