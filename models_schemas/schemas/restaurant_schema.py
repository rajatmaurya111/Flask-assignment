from models_schemas import ma
from marshmallow import Schema, fields, validate, ValidationError, post_load

from models_schemas.models.restaurant_model import Restaurant
from models_schemas.models.user_model import User

from constants import message_const


class RestaurantSchema(ma.Schema):
    def validate_user_id(user_id):
        if User.query.get(user_id) is None:
            raise ValidationError(message_const.USER_NOT_EXIST)
    
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Bool(load_only=True)
    user_id = fields.Int(validate=validate_user_id, require=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "email", "address","user_id")

    @post_load
    def make_restaurant(self, data, **kwargs):
        return Restaurant(**data)

restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)