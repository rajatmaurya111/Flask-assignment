from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def commit(self):
        db.session.add(self)
        db.session.commit()



class UserSchema(ma.Schema):
    class Meta:
        fields = ('title', 'content')


user_schema = UserSchema()
users_schema = UserSchema(many=True)