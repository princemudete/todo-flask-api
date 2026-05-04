from flask_marshmallow import Marshmallow
from marshmallow import fields, validate

from .models import Todo

ma = Marshmallow()


class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    completed = fields.Bool()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)