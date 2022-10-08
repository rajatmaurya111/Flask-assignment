# from flask import Blueprint, render_template, abort


# test_page = Blueprint("test_page", __name__, template_folder="routes")

# # @test_page.route("/")
# @test_page.route("/test_page")
# def s():
#     return "This is the test page"

from flask import jsonify
from flask_restful import Resource, request
from models.user import User, user_schema, users_schema
from marshmallow import Schema, fields, validate, ValidationError

# class test_page(Resource):
#     def get(self):
#         return {"w":"This is test page"}

class user(Resource):
    # def get(self, id):
    #     guide = User.query.get(id)
    #     return user_schema.jsonify(guide)
    def post(self):
        # print("request", request.json)


        # name = request.json['name']
        # email = request.json['email']

        # new_user = User(name, email)

       
        try:
            new_user = user_schema.load(request.json)
            new_user = new_user.create()
            # print(data)
            print(new_user, type(new_user))
            return jsonify(user_schema.dump(new_user))

            


        except ValidationError as err:
            print("error", err.messages)
            return "Error occured"

        # new_user.create()

        # user = User.query.get(new_user.get_id())
        # print("user", type(user))

        # print(user_schema.dump(user))

        # data = user_schema.dump(user)




        # return jsonuser
        # return jsonify(data)

class users(Resource):
    def get(self):
        all_guides = User.query.all()
    
        result = users_schema.dump(all_guides)
        return result
