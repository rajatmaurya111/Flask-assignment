from models_schemas import ma

from marshmallow import Schema, fields, validate, post_load

from models_schemas.models.user_model import User
from models_schemas.schemas.restaurant_schema import RestaurantSchema

class UserSchema(ma.Schema): 
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Email(), required=True)
    type = fields.Str(validate=validate.OneOf(["normal-user", "restraunt-owner"]))
    created_at = fields.Str()
    password = fields.Str(validate=validate.Length(min=6))
    city = fields.Str(validate=validate.Length(min=2))
    Zipcode = fields.Int()
    Balance = fields.Int(validate=validate.Range(min=0))
    status = fields.Bool(load_only=True)
    
    class Meta:
        model = User
        fields = ("id", "name", "email", "type", "city", "Zipcode", "Balance", "restaurants", "password")
        
 
    restaurants = fields.List(fields.Nested(RestaurantSchema))
 
    @post_load
    def make_user(self,data, **kwargs):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
