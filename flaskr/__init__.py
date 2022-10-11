import os

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api

from models_schemas import db

from routes.user_route import UserView, UsersView
from routes.restaurant_route import RestaurantRoute
from models_schemas.models.user_model import User
from models_schemas.models.restaurant_model import Restaurant


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)


    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    db.init_app(app)

    with app.app_context(): 
        db.drop_all()
        db.create_all()
    
    # flask admin
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Restaurant, db.session))


    #using guide route
    api.add_resource(UserView, '/user/<int:id>', '/user')
    api.add_resource(UsersView, '/users')
    api.add_resource(RestaurantRoute, '/restaurant/<int:id>', '/restaurant')

    return app
