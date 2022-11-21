import json

from flask_smorest import Blueprint

from application.dto.CategoryDto import CategoryDTO
from application.service.CategoryService import CategoryService

category_blp = Blueprint('category_blp', __name__)

category_service = CategoryService()


@category_blp.route('/category/', methods=["POST"])
@category_blp.arguments(CategoryDTO)
@category_blp.response(200, CategoryDTO)
def add_category(category_dto):
    return category_service.save_category(category_dto)


@category_blp.route('/category/', methods=["GET"])
@category_blp.response(200, CategoryDTO(many=True))
def show_all_category():
    return category_service.get_all()


@category_blp.route('/category/<category_id>', methods=["GET"])
@category_blp.response(200, CategoryDTO)
def get_category(category_id):
    category = category_service.get_category(category_id)
    return category
