# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Tag,\
    Cuisine, Collection, Association, Dish
from cta import app
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImage, RestaurantImageSchema,\
    RestaurantAmenitySchema, CuisineSchema, CollectionSchema, AssociationSchema, TagSchema, DishSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/restaurant', methods=['GET', 'POST'])
def restaurant_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        page = request.args.get('page', None)
        per_page = request.args.get('per_page', None)
        if rating:
            restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.rating >= rating).all()
        elif page:
            restaurants = Restaurant.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        else:
            restaurants = Restaurant.query.filter_by(**args).all()
        result = RestaurantSchema(many=True).dump(restaurants)
        return jsonify({'result': {'restaurants': result.data}, 'message': "Success", 'error': False})