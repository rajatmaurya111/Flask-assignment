from pickle import GET
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate, ValidationError, post_load
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    __tablename_= "user"

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    city = db.Column(db.String(100))
    Zipcode = db.Column(db.Integer)
    Balance = db.Column(db.Integer)



    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"{self.__id}"

    def get_id(self):
        return self.__id

class UserSchema(Schema):
    
    name = fields.Str(validate=validate.Length(min=2))
    email = fields.Str(validate=validate.Length(min=1))
    # age = fields.Int(validate=validate.Range(min=18, max=40))
    # permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))

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