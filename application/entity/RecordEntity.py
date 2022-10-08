class RecordEntity:
    def __init__(self):
        self.record_id = None
        self.user_id = None
        self.category_id = None
        self.record_create_date = None
        self.record_sum = None

    def set_id(self, record_id):
        self.record_id = record_id

    def set_user(self, user_id):
        self.user_id = user_id

    def set_category(self, category_id):
        self.category_id = category_id

    def set_create_date(self, create_date):
        self.record_create_date = create_date

    def set_sum(self, record_sum):
        self.record_sum = record_sum

    def get_id(self):
        return self.record_id

    def get_user_id(self):
        return self.user_id

    def get_category_id(self):
        return self.category_id

    def get_create_date(self):
        return self.record_create_date

    def get_sum(self):
        return self.record_sum

    def toString(self):
        return "Record id:" + str(self.record_id) + ' ' + "User_id:" + str(self.user_id) + " " + "Category id:" + str(self.category_id) + " " + "Sum:" + str(self.record_sum)

    def __eq__(self, other):
        if self.record_id is other.get_id():
            return True
        else:
            return False
