from cgi import test
import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from models.user import db, ma
from routes.test_page import test_page

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)

    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    # db = SQLAlchemy(app)
    # ma = Marshmallow(app)

    # sample model
    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():
        db.create_all() 

    #using guide route
    api.add_resource(test_page, '/')
    
    

    app.url_map()

    # if __name__ == '__main__':
    #     app.run(debug=True)

    return app