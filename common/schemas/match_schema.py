from marshmallow import Schema, fields

from ..validations import must_not_be_blank
from . import JobSchema, UserSchema


class MatchSchema(Schema):
    id = fields.Int(dump_only=True)
    user = fields.Nested(UserSchema)
    user_id = fields.Int()
    job = fields.Nested(JobSchema)
    job_id = fields.Int(required=True)
    interest = fields.Bool(required=True, validate=must_not_be_blank)
