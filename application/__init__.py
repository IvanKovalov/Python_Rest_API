# import application.views
import json

from flask import Flask, request

from application.dto.UserDto import UserDTO
from application.service.UserService import UserService

app = Flask(__name__)
user_service = UserService()


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/user/', methods=["POST"])
def user():
    user_dto = UserDTO()
    request_data = request.get_json()
    user_name = request_data['name']
    user_dto.__set_name__(user_name)
    user_service.save_user(user_dto)
    return app.make_response('200')


@app.route('/user/<user_id>', methods=["GET"])
def get_user(user_id):
    user1 = user_service.get_user(user_id)
    return app.make_response(json.dumps(user1.__dict__))
