from flask import abort
from sqlalchemy.exc import IntegrityError

from application.models.RecordModel import RecordModel


class RecordRepository:
    def __init__(self, db):
        self.db = db
        self.record_list = list()

    def save_record(self, record_entity):
        self.record_list.append(record_entity)
        try:
            self.db.session.add(record_entity)
            self.db.session.commit()
        except IntegrityError:
            abort(500, "Failed creating record")

    def get_records_by_user_id(self, user_id):
        # record_map = {}
        # for record in self.record_list:
        #     if record.get_user_id() is user_id:
        #         record_map[record.get_id()] = {'user_id': record.get_user_id(),
        #                                        'record_id': record.get_id(),
        #                                        'category_id': record.get_category_id(),
        #                                        'sum': record.get_sum()}
        # return record_map
        return RecordModel.query.filter_by(userId=user_id).all()

    def get_records_by_user_id_and_category_id(self, user_id, category_id):
        # record_map = {}
        # for record in self.record_list:
        #     if record.get_user_id() is user_id and record.get_category_id() is category_id:
        #         record_map[record.get_id()] = {'user_id': record.get_user_id(),
        #                                        'record_id': record.get_id(),
        #                                        'category_id': record.get_category_id(),
        #                                        'sum': record.get_sum()}
        # return record_map

        return RecordModel.query.filter_by(userId=user_id, categoryId=category_id).all()
