from flask import jsonify, make_response
from flask_restful import Resource, request

from models_schemas import db

# import models
from models_schemas.models.user_model import User

# import schema
from models_schemas.schemas.user_schema import UserSchema, user_schema, users_schema

from marshmallow import ValidationError
from constants import http_status_code, message_const

class UserView(Resource):
    '''fetch a user'''
    def get(self, id): 
        current_user = User.query.get(id)
        # check if user exist
        if current_user is None:
            return make_response(message_const.USER_NOT_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        # print("UserView", UserSchema().dump(current_user))
        if current_user.status:
            return make_response(jsonify(user_schema.dump(current_user)), http_status_code.HTTP_200_OK)
        else:
            return make_response(message_const.USER_NOT_ACTIVE, http_status_code.HTTP_400_BAD_REQUEST)


    '''create user'''
    def post(self):
        #chek if user already exist
        if User.query.filter_by(email=request.json["email"]).first():
            return make_response(message_const.USER_ALREADY_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        try:
            new_user = user_schema.load(request.json).create()
            return make_response(user_schema.dump(new_user), http_status_code.HTTP_201_CREATED)

        except ValidationError as err:
            return make_response({message_const.ERROR_MESSAGE_KEY: err.messages}, http_status_code.HTTP_400_BAD_REQUEST)

    '''set the user to inactive'''
    def delete(self, id):
        if User.query.get(id) is None:
            return make_response({message_const.USER_NOT_EXIST}, http_status_code.HTTP_400_BAD_REQUEST)


        current_user = User.query.get(id)
        current_user.status = False
        # current_user.delete()  
        db.session.commit()
        return make_response(message_const.REQUEST_SUCCESS, http_status_code.HTTP_200_OK)

    '''update a user'''
    def put(self, id):
        # current_user = User.query.get(id)
        if User.query.get(id) is None:
            return make_response(message_const.USER_NOT_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        try:
            user_schema.load(request.json)
        except ValidationError as err:
            return make_response({message_const.ERROR_MESSAGE_KEY: err.messages}, http_status_code.HTTP_400_BAD_REQUEST)

        User.query.filter_by(id=id).update((request.get_json()))
        db.session.commit()
        
        updated_user_data = user_schema.dump(User.query.get(id))
        return make_response({message_const.UPDATED_MESSAGE_KEY: updated_user_data},  http_status_code.HTTP_200_OK)


'''fetch all the users'''
class UsersView(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify(users_schema.dump(users)), http_status_code.HTTP_200_OK)
        