from cgi import test
import imp
import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from models.user import db as user_db
from models.restaurant import db as restaurant_db

from routes.user_route import UserRoute
from routes.restaurant_route import RestaurantRoute


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    # db = SQLAlchemy(app)
    # ma = Marshmallow(app)

    # sample model
    user_db.init_app(app)
    restaurant_db.init_app(app)
    # ma.init_app(app)
    

    # what is app.app.context?
    with app.app_context(): 
        user_db.create_all() 
        restaurant_db.create_all()

    #using guide route
    api.add_resource(UserRoute, '/user/<int:id>', '/user')
    # api.add_resource(users, '/users')
    api.add_resource(RestaurantRoute, '/restaurant/<int:id>', '/restaurant')
    

    print(app.url_map)


    # if __name__ == '__main__':
    #     app.run(debug=True)

    return app