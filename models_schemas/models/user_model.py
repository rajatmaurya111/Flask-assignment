from datetime import datetime

from models_schemas import db
from constants import consts

class User(db.Model):
    __tablename_= "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(consts.MAX_NAME_LENGTH), nullable=False)
    email = db.Column(db.String(consts.MAX_EMAIL_LENGTH), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    password = db.Column(db.String(consts.MAX_PASSWORD_LENGTH), nullable=False)
    type = db.Column(db.String(), default=consts.USER_TYPES_DEFAULT)
    city = db.Column(db.String(consts.MAX_CITY_LENGHT))
    active = db.Column(db.Boolean(), nullable=False, default=True ) 
    zipcode = db.Column(db.Integer)
    balance = db.Column(db.Integer)

    #Relation with restaurant model
    restaurants = db.relationship('Restaurant', backref='user')

    def create(self):
        db.session.add(self)
        self.save()
        return self

    def delete(self):
        db.session.delete(self)
        self.save()
    
    def save(self):
        db.session.commit()


    def __repr__(self):
        return f"{self.id}"

