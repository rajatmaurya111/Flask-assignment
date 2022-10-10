# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from datetime import datetime

# from pkg_resources import require
# from models.user import User
# UserSchema

# db = SQLAlchemy()
from models_schemas import db



# from models.user import User

class Restaurant(db.Model):
    __tablename_= "restaurants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)  
    # owner = db.Column(db.String(100))
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

