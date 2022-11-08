import datetime
import json
import logging

from flask import Flask, request

from application.dto.CategoryDto import CategoryDTO
from application.dto.RecordDto import RecordDTO
from application.dto.UserDto import UserDTO
from application.service.CategoryService import CategoryService
from application.service.RecordService import RecordService
from application.service.UserService import UserService

app = Flask(__name__)
user_service = UserService()
category_service = CategoryService()
record_service = RecordService(user_service.user_repository, category_service.category_repository)
logging.basicConfig(level=logging.INFO,  format='%(asctime)s %(levelname)s:%(message)s')


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/user/', methods=["POST"])
def user():
    user_dto = UserDTO()
    request_data = request.get_json()
    user_name = request_data['name']
    user_dto.set_name(user_name)
    user_service.save_user(user_dto)
    return app.make_response('200')


@app.route('/user/<user_id>', methods=["GET"])
def get_user(user_id):
    user1 = user_service.get_user(user_id)
    return app.make_response(json.dumps(user1))


@app.route('/category/', methods=["POST"])
def add_category():
    request_data = request.get_json()
    category_name = request_data['name']
    category_dto = CategoryDTO()
    category_dto.set_name(category_name)
    category_service.save_category(category_dto)
    return app.make_response('200')


@app.route('/category/', methods=["GET"])
def show_all_category():
    return app.make_response(json.dumps(category_service.get_all()))


@app.route('/records/<user_id>', methods=["GET"])
def show_records_by_user_id(user_id):
    return app.make_response(record_service.get_records_by_id(int(user_id)))


@app.route('/record/', methods=["POST"])
def add_record():
    record_dto = RecordDTO()
    request_data = request.get_json()
    record_dto.set_user(int(request_data['user_id']))
    record_dto.set_category(int(request_data['category_id']))
    record_dto.set_create_date(datetime.time.hour)
    record_dto.set_sum(int(request_data['sum']))
    return app.make_response(json.dumps(record_service.add_record(record_dto)))


@app.route('/records/', methods=["POST"])
def get_records_by_user_category():
    request_data = request.get_json()
    user_id = int(request_data['user_id'])
    category_id = int(request_data['category_id'])
    return app.make_response(record_service.get_records_by_category_and_user(user_id, category_id))