# from flask import Blueprint, render_template, abort


# test_page = Blueprint("test_page", __name__, template_folder="routes")

# # @test_page.route("/")
# @test_page.route("/test_page")
# def s():
#     return "This is the test page"

from hashlib import new
from flask_restful import Resource, request
from models.user import User, user_schema, users_schema

class test_page(Resource):
    def get(self):
        return {"w":"This is test page"}

class user(Resource):
    def get(self, id):
        guide = User.query.get(id)
        return user_schema.jsonify(guide)
    def post(self):
        title = request.json['title']
        content = request.json['content']

        new_guide = User(title, content)

        # db.session.add(new_guide)
        # db.session.commit()
        new_guide.commit()

        guide = User.query.get(new_guide.id)

        return user_schema.jsonify(guide)

class users(Resource):
    def get(self):
        all_guides = User.query.all()
    
        result = users_schema.dump(all_guides)
        return result
