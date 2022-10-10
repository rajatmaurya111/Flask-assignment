from flask import jsonify, make_response
from flask_restful import Resource, request

from models_schemas import db

# import models
from models_schemas.models.user_model import User

# import schema
from models_schemas.schemas.user_schema import UserSchema, user_schema, users_schema

from marshmallow import Schema, fields, validate, ValidationError
from constants.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

# class test_page(Resource):
#     def get(self):z
#         return {"w":"This is test page"}

class UserView(Resource):
    '''fetch a user'''
    def get(self, id):
        # guide = User.query.get(id)
        # return user_schema.jsonify(guide)
        current_user = User.query.get(id)
        # check if user exist
        if current_user is None:
            return make_response({'message': "user not exist"}, HTTP_400_BAD_REQUEST)

        print("UserView", UserSchema().dump(current_user))
        if current_user.status:
            return make_response(jsonify(user_schema.dump(current_user)), HTTP_200_OK)
        else:
            return make_response({"message":"user not active"}, HTTP_400_BAD_REQUEST)


    '''create user'''
    def post(self):
        # user_toadd = User.query.get(user_schema.load(request.json).id)
        # # check if user exist
        # if user_toadd:
        #     return make_response({'message': "user already exist"}, HTTP_400_BAD_REQUEST)

        try:
            new_user = user_schema.load(request.json).create()
            return make_response(user_schema.dump(new_user), HTTP_201_CREATED)

        except ValidationError as err:
            return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)

    '''set the user to inactive'''
    def delete(self, id):
        if User.query.get(id) is None:
            return make_response({'message': "user not exist"}, HTTP_400_BAD_REQUEST)

        try:
            current_user = User.query.get(id)
            current_user.status = False
            # current_user.delete()  
            db.session.commit()
            return make_response({"message": "success"}, HTTP_200_OK)
        except:
            return make_response({"status":"failed"}, HTTP_400_BAD_REQUEST)

    '''update a user'''
    def put(self, id):
        # current_user = User.query.get(id)
        if User.query.get(id) is None:
            return make_response({'message': "user not exist"}, HTTP_400_BAD_REQUEST)

        try:
            user_schema.load(request.json)
        except ValidationError as err:
            return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)

        User.query.filter_by(id=id).update((request.get_json()))
        db.session.commit()
        

        # update_data = request.get_json()
        updated_user_data = user_schema.dump(User.query.get(id))
        return make_response({"result": updated_user_data},  HTTP_200_OK)
        # except:
        #     make_response({"status": "Error Occured"}, HTTP_400_BAD_REQUEST)


'''fetch all the users'''
class UsersView(Resource):
    def get(self):
        users = User.query.all()
        return make_response(jsonify(users_schema.dump(users)), HTTP_200_OK)