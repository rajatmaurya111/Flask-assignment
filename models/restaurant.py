from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate, ValidationError, post_load
from datetime import datetime

from pkg_resources import require
# from models.user import User

# db = SQLAlchemy()
from models import db
from models.user import User

class Restaurant(db.Model):
    __tablename_= "restaurants"

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    address = db.Column(db.String(100))
    menu =db.Column(db.String(100))
    description = db.Column(db.String(100))
    status = db.Column(db.Boolean(), nullable=False, default=True ) 
    # owner = db.Column(db.String(100), nullable=False)

    #Relation with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship("User")

    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"{self.id}"

    def get_id(self):
        return self.id



class RestaurantSchema(Schema):
    def validate_user_id(user_id):
        if User.query.get(user_id) is None:
            raise ValidationError("owner does not exit in User")

    
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Length(min=1))
    # created_at = fields.Str()
    address = fields.Str()
    Balance = fields.Int()
    owner = fields.Str()
    status = fields.Bool(load_only=True)
    user_id = fields.Int(validate=validate_user_id, require=True)

    

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