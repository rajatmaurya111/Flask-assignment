import email
from flask import jsonify, make_response
from flask_restful import Resource, request

from models_schemas.models.restaurant_model import Restaurant
from models_schemas.schemas.restaurant_schema import restaurant_schema
from models_schemas import db

from marshmallow import ValidationError
from constants import consts, http_status_code


class RestaurantRoute(Resource):
    '''get user details'''
    def get(self, id):
        current_restaurant = Restaurant.query.get(id)

        # check if restaurant exist
        if current_restaurant is None:
            return make_response(consts.USER_NOT_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        if current_restaurant.status:
            return make_response(jsonify(restaurant_schema.dump(current_restaurant)), http_status_code.HTTP_200_OK)
        else:
            return make_response(consts.USER_NOT_ACTIVE, http_status_code.HTTP_400_BAD_REQUEST)
    

    '''create Restaurant'''
    def post(self):
        #chek if restaurant already exist
        if Restaurant.query.filter_by(email=request.json["email"]).first():
            return make_response(consts.RESTAURANT_ALREADY_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        try:
            new_restaurant = restaurant_schema.load(request.json).create() 
            return make_response(restaurant_schema.dump(new_restaurant), http_status_code.HTTP_201_CREATED)

        except ValidationError as err:
            return make_response({consts.ERROR_MESSAGE_KEY: err.messages}, http_status_code.HTTP_400_BAD_REQUEST)


  
    def delete(self, id):
         # check if restaurant exist
        if Restaurant.query.get(id) is None:
            return make_response(consts.USER_NOT_EXIST, http_status_code.HTTP_400_BAD_REQUEST)

        try:
            current_restaurant = Restaurant.query.get(id)
            current_restaurant.status = False 
            db.session.commit()

            return make_response(consts.REQUEST_SUCCESS, http_status_code.HTTP_200_OK)
        except:
            return make_response(consts.REQUEST_FAILED, http_status_code.HTTP_400_BAD_REQUEST)
