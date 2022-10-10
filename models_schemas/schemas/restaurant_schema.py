import imp
from marshmallow import Schema, fields, validate, ValidationError, post_load
from models_schemas import ma
from models_schemas.models.restaurant_model import Restaurant
from models_schemas.models.user_model import User


class RestaurantSchema(ma.Schema):
    def validate_user_id(user_id):
        if User.query.get(user_id) is None:
            raise ValidationError("owner does not exit in User")
        # pass

    
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Length(min=1))
    # created_at = fields.Str()
    address = fields.Str()
    # owner = fields.Str()
    status = fields.Bool(load_only=True)
    user_id = fields.Int(validate=validate_user_id, require=True)

    

    # age = fields.Int(validate=validate.Range(min=18, max=40))

    # permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))

    class Meta:
        model = Restaurant
        fields = ("id", "name", "email", "address", "user_id")
        
    # owner = fields.Nested(UserSchema)
    

    @post_load
    def make_restaurant(self, data, **kwargs):
        return Restaurant(**data)

# in_date = {"name":"a", "permission":"admin", "age":21}

# try:
#     print(UserSchema().load(in_date))
# except ValidationError as err:
#     print(err.messages)

restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)