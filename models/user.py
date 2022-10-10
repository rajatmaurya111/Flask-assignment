from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate, ValidationError, post_load
from datetime import datetime

# from models.restaurant import Restaurant

from models import db
# db = SQLAlchemy()

class User(db.Model):
    __tablename_= "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    type = db.Column(db.String(100), default="normal-user")
    city = db.Column(db.String(100))
    status = db.Column(db.Boolean(), nullable=False, default=True ) 
    Zipcode = db.Column(db.Integer)
    Balance = db.Column(db.Integer)

    #Relation with restaurant model
    restaurants = db.relationship('Restaurant', backref='user')


    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # @classmethod
    # def save(self):
    #     db.session.commit()
    

    def __repr__(self):
        return f"{self.__id}"

    def get_id(self):
        return self.__id

class UserSchema(Schema):
    # __id = fields.Int()
    id = fields.Int(load_only=True)
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Email())
    type = fields.Str(validate=validate.OneOf(["normal-user", "restraunt-owner"]))
    created_at = fields.Str()
    city = fields.Str(validate=validate.Length(min=2))
    Zipcode = fields.Int()
    Balance = fields.Int(validate=validate.Range(min=0))
    status = fields.Bool(load_only=True)
    
    # class Meta:
    #     fields = ("name", "email")
    #     model = User

    @post_load
    def make_user(self,data, **kwargs):
        return User(**data)


# in_date = {"name":"a", "permission":"admin", "age":21}
# try:
#     print(UserSchema().load(in_date))
# except ValidationError as err:
#     print(err.messages)

user_schema = UserSchema()
users_schema = UserSchema(many=True)