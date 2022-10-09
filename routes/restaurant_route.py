
from multiprocessing import current_process
from flask import jsonify, make_response
from flask_restful import Resource, request
from models.restaurant import Restaurant, RestaurantSchema, restaurant_schema, db as r_db
from marshmallow import Schema, fields, validate, ValidationError
from constants.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

# class test_page(Resource):
#     def get(self):z
#         return {"w":"This is test page"}

class RestaurantRoute(Resource):
    # '''get user details'''
    def get(self, id):
        # guide = User.query.get(id)
        # return user_schema.jsonify(guide)
        current_restaurant = Restaurant.query.get(id)
        return make_response(jsonify(restaurant_schema.dump(current_restaurant)), HTTP_200_OK)
    

    '''create Restaurant'''
    def post(self):
        try:
        
            new_restaurant = restaurant_schema.load(request.json)
            new_restaurant.create()
            # r_db.session.add(new_restaurant)
            # r_db.session.commit()
            # new_restaurant = new_restaurant.create()
            # print(new_restaurant.get_id())
            # print(data)
            # print(new_restaurant, type(new_restaurant))

            # return "HI"
            return make_response({"result":restaurant_schema.dump(new_restaurant)}, HTTP_201_CREATED)
        except ValidationError as err:
            # print("error", err.messages)
            return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)