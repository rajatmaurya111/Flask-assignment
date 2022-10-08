from doctest import debug_script
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate, ValidationError, post_load
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()

class Restaurant(db.Model):
    __tablename_= "restaurant"

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    address = db.Column(db.String(100))
    type =db.Column(db.String(100))
    description = db.Column(db.String(100))


    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"{self.__id}"

    def get_id(self):
        return self.__id

class RestaurantSchema(Schema):
    
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Length(min=1))
    # created_at = fields.Str()
    city = fields.Str()
    address = fields.Str()
    Balance = fields.Int()
    # age = fields.Int(validate=validate.Range(min=18, max=40))

    # permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))

    # class Meta:
    #     fields = ("name", "email")
    #     model = User

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