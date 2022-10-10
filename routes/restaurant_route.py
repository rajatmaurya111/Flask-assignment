
from symbol import import_from
from flask import jsonify, make_response
from flask_restful import Resource, request
from models.restaurant import Restaurant, RestaurantSchema, restaurant_schema
# , db as r_db
from models import db
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
        # current_restaurant = Restaurant.query.get(id)
        # return make_response(jsonify(restaurant_schema.dump(current_restaurant)), HTTP_200_OK)
        

        current_restaurant = Restaurant.query.get(id)
        # check if restaurant exist
        if current_restaurant is None:
            return make_response({'message': "user not exist"}, HTTP_400_BAD_REQUEST)

        if current_restaurant.status:
            return make_response(jsonify(restaurant_schema.dump(current_restaurant)), HTTP_200_OK)
        else:
            return make_response({"message":"user not active"}, HTTP_400_BAD_REQUEST)
    

    '''create Restaurant'''
    def post(self):
       
        # restaurant_toadd = Restaurant.query.get(restaurant_schema.load(request.json).id)
        # # check if restaurant exist
        # if restaurant_toadd:
        #     return make_response({'message': "user already exist"}, HTTP_400_BAD_REQUEST)

        try:
            new_restaurant = restaurant_schema.load(request.json).create()
            return make_response({"result":restaurant_schema.dump(new_restaurant)}, HTTP_201_CREATED)

        except ValidationError as err:
            return make_response({"error": err.messages}, HTTP_400_BAD_REQUEST)



    def delete(self, id):
        # try:
        #     current_restaurant = Restaurant.query.get(id).delete() 
        #     return make_response({"message": "success"}, HTTP_200_OK)
        # except:
        #     return make_response({"status":"failed"}, HTTP_400_BAD_REQUEST)
        if Restaurant.query.get(id) is None:
            return make_response({'message': "user not exist"}, HTTP_400_BAD_REQUEST)



        try:
            current_restaurant = Restaurant.query.get(id)
            current_restaurant.status = False
            # current_restaurant.delete()  
            # r_db.session.commit()
            db.session.commit()
            return make_response({"message": "success"}, HTTP_200_OK)
        except:
            return make_response({"status":"failed"}, HTTP_400_BAD_REQUEST)
