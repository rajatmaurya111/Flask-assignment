import email
from flask import jsonify, make_response
from flask_restful import Resource, request

from models_schemas import db

# import models
from models_schemas.models.user_model import User

# import schema
from models_schemas.schemas.user_schema import UserSchema, user_schema, users_schema

from marshmallow import ValidationError
from constants import consts, http_status_code

class UserView(Resource):
    
    def get(self, id): 
        """fetch a user"""
        current_user = User.query.get_or_404(id)

        if current_user.active:
            return make_response(jsonify(user_schema.dump(current_user)), http_status_code.HTTP_200_OK)
        else:
            return make_response(consts.USER_NOT_ACTIVE, http_status_code.HTTP_404_NOT_FOUND)
    
    def post(self):
        """create user"""
        #chek if user already exist
        if  User.query.filter_by(email=request.json.get("email")).first():
            return make_response(consts.USER_ALREADY_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        try:
            new_user = user_schema.load(request.json).create()
            return make_response(user_schema.dump(new_user), http_status_code.HTTP_201_CREATED)

        except ValidationError as err:
            return make_response({consts.ERROR_MESSAGE_KEY: err.messages}, http_status_code.HTTP_400_BAD_REQUEST)

    def delete(self, id):
        """set the user to inactive"""
        current_user = User.query.get_or_404(id)
        current_user.active = False
        current_user.save()
        
        return make_response(consts.REQUEST_SUCCESS, http_status_code.HTTP_200_OK)
    
    def put(self, id):
        """update a user"""
        User.query.get_or_404(id) 
      
        try:
            user_schema.validate(request.json)
        except ValidationError as err:
            return make_response({consts.ERROR_MESSAGE_KEY: err.messages}, http_status_code.HTTP_400_BAD_REQUEST)

        User.query.filter_by(id=id).update(request.get_json())
        db.session.commit()
        
        updated_user_data = user_schema.dump(User.query.get(id))
        return make_response({consts.UPDATED_MESSAGE_KEY: updated_user_data},  http_status_code.HTTP_200_OK)


class UsersView(Resource):
    """Users view"""

    def get(self):
        '''fetch all the users'''
        users = User.query.all()
        return make_response(jsonify(users_schema.dump(users)), http_status_code.HTTP_200_OK)
