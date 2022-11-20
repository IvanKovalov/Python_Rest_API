
from flask_smorest import Blueprint

from application.dto.UserDto import UserDTO
from application.service.UserService import UserService

user_blp = Blueprint('user_blp', __name__)
user_service = UserService()


@user_blp.route('/user/', methods=["POST"])
@user_blp.arguments(UserDTO)
@user_blp.response(200, UserDTO)
def user(user_data):
    return user_service.save_user(user_data)


@user_blp.route('/user/<user_id>', methods=["GET"])
@user_blp.response(200, UserDTO)
def get_user(user_id):
    user = user_service.get_user(user_id)
    return user
