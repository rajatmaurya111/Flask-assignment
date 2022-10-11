import os

from flask import Flask
from flask_restful import Api

from models_schemas import db

from routes.user_route import UserView, UsersView
from routes.restaurant_route import RestaurantRoute


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

    db.init_app(app)

    with app.app_context(): 
        db.create_all()

    #using guide route
    api.add_resource(UserView, '/user/<int:id>', '/user')
    api.add_resource(UsersView, '/users')
    api.add_resource(RestaurantRoute, '/restaurant/<int:id>', '/restaurant')
    

    # to print mapped url
    # print(app.url_map)

    return app
