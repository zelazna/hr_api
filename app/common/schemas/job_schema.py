from marshmallow import Schema, fields


# https://marshmallow.readthedocs.io/en/latest/examples.html#quotes-api-flask-sqlalchemy
class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    text = fields.Str()
    url = fields.Str()
    email = fields.Str()
    ref = fields.Str()
