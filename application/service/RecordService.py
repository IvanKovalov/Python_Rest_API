import logging

from flask import abort

from application.models.RecordModel import RecordModel
from application.models.database import db
from application.repository.CategoryRepository import CategoryRepository
from application.repository.RecordRepository import RecordRepository


class RecordService:
    def __init__(self, user_repository, category_repository):
        self.record_counter = 1
        self.record_repository = RecordRepository(db)
        self.user_repository = user_repository
        self.category_repository = CategoryRepository(db)
        self.log = logging.getLogger(RecordService.__name__)
        self.log.info("Created new instance of Record Service")

    def add_record(self, record_dto):
        category = self.category_repository.get_category_by_id(record_dto['categoryId'])
        if category.is_private():
            if category.get_owner_id() is record_dto['userId']:
                record = RecordModel(**record_dto)
                self.record_repository.save_record(record)
                return record
            else:
                abort(404, "It is private category, u do not have access")
        else:
            record = RecordModel(**record_dto)
            self.record_repository.save_record(record)
            return record

    def get_records_by_id(self, user_id):
        records = self.record_repository.get_records_by_user_id(user_id)
        return records

    def get_records_by_category_and_user(self, record_query_dto):
        records = self.record_repository.get_records_by_user_id_and_category_id(record_query_dto['userId'],
                                                                                record_query_dto['categoryId'])
        return records
