
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from application.models.UserModel import UserModel

login_blp = Blueprint('login_blp', __name__)


@login_blp.route('/login', methods=['POST'])
def login():
    if request.is_json:
        id = request.json['id']
        userName = request.json['userName']
    else:
        id = request.form['id']
        userName = request.form['userName']

    user = UserModel.query.filter_by(id=id, userName=userName).first()

    if user and pbkdf2_sha256.verify(request.json['password'], user.password):
        access_token = create_access_token(identity=user.id)
        return jsonify(message='Login Successful', access_token=access_token)
    else:
        return jsonify('Bad email or Password'), 401


