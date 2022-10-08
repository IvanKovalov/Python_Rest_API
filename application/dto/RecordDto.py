class RecordDTO:
    def __init__(self):
        self.user_id = None
        self.category_id = None
        self.record_create_date = None
        self.record_sum = None

    def set_user(self, user_id):
        self.user_id = user_id

    def set_category(self, category_id):
        self.category_id = category_id

    def set_create_date(self, create_date):
        self.record_create_date = create_date

    def set_sum(self, record_sum):
        self.record_sum = record_sum

    def get_user_id(self):
        return self.user_id

    def get_category_id(self):
        return self.category_id

    def get_create_date(self):
        return self.record_create_date

    def get_sum(self):
        return self.record_sum
