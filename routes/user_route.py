# from flask import Blueprint, render_template, abort


# test_page = Blueprint("test_page", __name__, template_folder="routes")

# # @test_page.route("/")
# @test_page.route("/test_page")
# def s():
#     return "This is the test page"

from flask import jsonify, make_response
from flask_restful import Resource, request
from models.user import User, UserSchema, user_schema, db
from marshmallow import Schema, fields, validate, ValidationError
from constants.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

# class test_page(Resource):
#     def get(self):z
#         return {"w":"This is test page"}

class UserRoute(Resource):
    '''get user details'''
    def get(self, id):
        # guide = User.query.get(id)
        # return user_schema.jsonify(guide)
        current_user = User.query.get(id)
        return make_response(jsonify(user_schema.dump(current_user)), HTTP_200_OK)

    '''create user'''
    def post(self):
        try:
            new_user = user_schema.load(request.json)
            new_user = new_user.create()
            print(new_user.get_id())
            # print(data)
            # new_user.id = new_user.get_id()
            print(new_user, type(new_user))
            return make_response({"result":user_schema.dump(new_user)}, HTTP_201_CREATED)

        except ValidationError as err:
            # print("error", err.messages)
            return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)


    def delete(self, id):
        try:
            current_user = User.query.get(id)
            current_user.delete()  
            return make_response({"message": "success"}, HTTP_200_OK)
        except:
            return make_response({"status":"failed"}, HTTP_400_BAD_REQUEST)

    def put(self, id):
        try:
            # curr_user = User.query.get(id)
            try:
                user_schema.load(request.json)
            except ValidationError as err:
                return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)
            User.query.filter_by(_User__id=id).update((request.get_json()))
            # User.save()
            # print(type(updated_user))
            db.session.commit()
            

            # update_data = request.get_json()
            # curr_user.save()

            # current_user_data. = "john"
            # return jsonify(user_schema.dump(current_user))
            updated_user_data = user_schema.dump(User.query.get(id))
            # print(user_schema.dump(User.query.get(id)))

            return make_response({"result": updated_user_data},  HTTP_200_OK)
        except:
            make_response({"status": "Error Occured"}, HTTP_400_BAD_REQUEST)



# class users(Resource):
#     def get(self):
#         all_guides = User.query.all()
    
#         result = users_schema.dump(all_guides)
#         return result