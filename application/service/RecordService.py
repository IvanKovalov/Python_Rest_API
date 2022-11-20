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
        # if self.user_repository.get_user_by_id(record_dto.get_user_id()) is None:
        #     self.log.error("try to add record with non-existent user_id")
        #     return "User with such id not registered"
        # elif self.category_repository.get_category_by_id(record_dto.get_category_id()) is None:
        #     self.log.error("try to add record with non-existent category_id")
        #     return "Category with such id not registered"
        # record_entity = RecordEntity()
        # record_entity.set_id(self.record_counter)
        # record_entity.set_user(record_dto.get_user_id())
        # record_entity.set_category(record_dto.get_category_id())
        # record_entity.set_create_date(record_dto.get_create_date())
        # record_entity.set_sum(record_dto.get_sum())
        # self.log.info("Saving new record")
        # self.record_repository.save_record(record_entity)
        # self.record_counter = self.record_counter + 1
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
        # if self.user_repository.get_user_by_id(user_id) is None:
        #     self.log.error("try to add record with non-existent user_id")
        #     return "User with such id not registered"
        # elif type(user_id) is not int:
        #     return Exception('Wrong type of id')
        # else:
        #     self.log.info("Try to get list with records filtered by user_id")
        #     return self.record_repository.get_records_by_user_id(user_id)
        # records = self.record_repository.get_records_by_user_id(user_id)
        return records

    def get_records_by_category_and_user(self, record_query_dto):
        # if self.user_repository.get_user_by_id(user_id) is None:
        #     self.log.error("try to add record with non-existent user_id")
        #     return "User with such id not registered"
        # elif self.category_repository.get_category_by_id(category_id) is None:
        #     self.log.error("try to add record with non-existent category_id")
        #     return "Category with such id not registered"
        # elif type(user_id) is not int or type(category_id) is not int:
        #     self.log.info("Wrong id of user")
        #     return Exception('Wrong type of id')
        # else:
        #     self.log.info("Try to get list of records bu user and record")
        #     return self.record_repository.get_records_by_user_id_and_category_id(user_id, category_id)
        records = self.record_repository.get_records_by_user_id_and_category_id(record_query_dto['userId'], record_query_dto['categoryId'])
        return records


