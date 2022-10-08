import logging

from application.entity.RecordEntity import RecordEntity
from application.repository.RecordRepository import RecordRepository


class RecordService:
    def __init__(self):
        self.record_counter = 1
        self.record_repository = RecordRepository()
        self.log = logging.getLogger(RecordService.__name__)
        self.log.info("Created new instance of Record Service")

    def add_record(self, record_dto):
        record_entity = RecordEntity()
        record_entity.set_id(self.record_counter)
        record_entity.set_user(record_dto.get_user_id())
        record_entity.set_category(record_dto.get_category_id())
        record_entity.set_create_date(record_dto.get_create_date())
        record_entity.set_sum(record_dto.get_sum())
        self.log.info("Saving new record")
        self.record_repository.save_record(record_entity)
        self.record_counter = self.record_counter + 1

    def get_records_by_id(self, user_id):
        if type(user_id) is not int:
            return Exception('Wrong type of id')
        else:
            self.log.info("Try to get list with records filtered by user_id")
            return self.record_repository.get_records_by_user_id(user_id)

    def get_records_by_category_and_user(self, user_id, category_id):

        if type(user_id) is not int or type(category_id) is not int:
            self.log.info("Wrong id of user")
            return Exception('Wrong type of id')
        else:
            self.log.info("Try to get list of records bu user and record")
            return self.record_repository.get_records_by_user_id_and_category_id(user_id, category_id)


