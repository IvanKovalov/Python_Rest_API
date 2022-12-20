import logging

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from application.models.database import db
from application.resources.CategoryController import category_blp
from application.resources.RecordContoller import record_blp
from application.resources.UserContoller import user_blp
from application.security.login import login_blp

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
app.register_blueprint(user_blp)
app.register_blueprint(category_blp)
app.register_blueprint(record_blp)
app.register_blueprint(login_blp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/pyt'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change on production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def hello():
    return 'Hello, World!'


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ),
        401,
    )
