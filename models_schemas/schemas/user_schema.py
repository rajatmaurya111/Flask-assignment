from models_schemas import ma

from marshmallow import fields, validate, post_load

from models_schemas.models.user_model import User
from models_schemas.schemas.restaurant_schema import RestaurantSchema
from  constants import consts

class UserSchema(ma.Schema): 
    """User Schema"""

    name = fields.Str(validate=validate.Length(min=consts.MIN_NAME_LENGTH))
    email = fields.Str(validate=validate.Email(), required=True)
    type = fields.Str(validate=validate.OneOf(consts.USER_TYPES))
    created_at = fields.Str()
    password = fields.Str(validate=validate.Length(min=consts.MIN_PASSWORD_LENGTH), load_only=True, required=True)
    city = fields.Str()
    zipcode = fields.Str(validate=validate.Length(equal=consts.ZIPCODE_LENGTH))
    balance = fields.Int(validate=validate.Range(min=consts.MIN_BALANCE))
    active = fields.Bool(load_only=True)    
    
    class Meta:
        model = User
        fields = ("id", "name", "email", "type", "city", "zipcode", "balance", "restaurants", "password")
 
    restaurants = fields.List(fields.Nested(RestaurantSchema))
 
    @post_load
    def make_user(self,data, **kwargs):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
