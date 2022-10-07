# from flask import Blueprint, render_template, abort


# test_page = Blueprint("test_page", __name__, template_folder="routes")

# # @test_page.route("/")
# @test_page.route("/test_page")
# def s():
#     return "This is the test page"

from flask_restful import Resource
from models.user import User, user_schema

class test_page(Resource):
    def get(self):
        return {"w":"This is test page"}

class guide(Resource):
    def get(self):
        print("Hi")
        # guide = User.query.get(id)
        # return user_schema.jsonify(guide)
        return {"HI":"how"}
