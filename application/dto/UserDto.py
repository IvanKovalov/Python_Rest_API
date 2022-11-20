from marshmallow import Schema, fields, validate


class UserDTO(Schema):
    id = fields.Str(dump_only=True)
    userName = fields.Str(required=True, validate=validate.Length(max=40))

    def __get_name__(self):
        return self.userName

    def set_name(self, user_name):
        self.userName = user_name
