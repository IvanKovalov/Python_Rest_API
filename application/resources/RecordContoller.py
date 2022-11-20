from flask_smorest import Blueprint

from application.dto.RecordDto import RecordDTO
from application.dto.RecordQueryDto import RecordQueryDto
from application.resources.CategoryController import category_service
from application.resources.UserContoller import user_service
from application.service.RecordService import RecordService

record_blp = Blueprint('record_blp', __name__)

record_service = RecordService(user_service.user_repository, category_service.category_repository)

record_blp.route('/records/<user_id>', methods=["GET"])


@record_blp.route('/records/<user_id>', methods=["GET"])
@record_blp.response(200, RecordDTO(many=True))
def show_records_by_user_id(user_id):
    return record_service.get_records_by_id(int(user_id))


@record_blp.route('/record/', methods=["POST"])
@record_blp.arguments(RecordDTO)
@record_blp.response(200, RecordDTO)
def add_record(record_dto):
    # record_dto = RecordDTO()
    # request_data = request.get_json()
    # record_dto.set_user(int(request_data['user_id']))
    # record_dto.set_category(int(request_data['category_id']))
    # record_dto.set_create_date(datetime.date.today())
    # record_dto.set_sum(int(request_data['sum']))
    return record_service.add_record(record_dto)


@record_blp.route('/records/', methods=["POST"])
@record_blp.arguments(RecordQueryDto)
@record_blp.response(200, RecordDTO(many=True))
def get_records_by_user_and_category(record_query_dto):
    return record_service.get_records_by_category_and_user(record_query_dto)
