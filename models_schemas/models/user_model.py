from datetime import datetime

from models_schemas import db

class User(db.Model):
    __tablename_= "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow,
        nullable=False
    )
    password = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), default="normal-user")
    city = db.Column(db.String(100))
    status = db.Column(db.Boolean(), nullable=False, default=True ) 
    Zipcode = db.Column(db.Integer)
    Balance = db.Column(db.Integer)

    #Relation with restaurant model
    restaurants = db.relationship('Restaurant', backref='user')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f"{self.__id}"

    def get_id(self):
        return self.__id
