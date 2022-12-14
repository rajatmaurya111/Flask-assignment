from models_schemas import ma
from marshmallow import fields, validate, ValidationError, post_load

from models_schemas.models.restaurant_model import Restaurant
from models_schemas.models.user_model import User

from constants import consts


class RestaurantSchema(ma.Schema):
    """Restaurant Schema"""
    def validate_user_id(user_id):
        if User.query.get(user_id) is None:
            raise ValidationError(consts.USER_NOT_EXIST)
    
    name = fields.Str(validate=validate.Length(min=consts.MIN_NAME_LENGTH))
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    active = fields.Bool(load_only=True)
    user_id = fields.Int(validate=validate_user_id, require=True)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "email", "address", "menu", "user_id")
