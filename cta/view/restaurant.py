# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Tag,\
    Cuisine, Collection, Association, Dish
from cta import app
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImageSchema,\
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


@app.route('/api/v1/restaurant/amenity', methods=['GET', 'POST'])
def restaurant_amenity():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = RestaurantAmenity.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantAmenitySchema(many=True).dump(data)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})
    else:
        post = RestaurantAmenity(**request.json)
        post.save()
        result = RestaurantAmenitySchema().dump(post)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/images', methods=['GET', 'POST'])
def restaurant_image_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = RestaurantImage.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantImageSchema(many=True).dump(data)
        return jsonify({'result': {'images': result.data}, 'message': "Success", 'error': False})
    else:
        post = RestaurantImage(**request.json)
        post.save()
        result = RestaurantImageSchema().dump(post)
        return jsonify({'result': {'image': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/tag', methods=['GET', 'POST'])
def restaurant_tag_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Tag.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = TagSchema(many=True).dump(data)
        return jsonify({'result': {'tag': result.data}, 'message': "Success", 'error': False})
    else:
        post = Tag(**request.json)
        post.save()
        result = TagSchema().dump(post)
        return jsonify({'result': {'tag': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/cuisine', methods=['GET', 'POST'])
def restaurant_cuisine_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Cuisine.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CuisineSchema(many=True).dump(data)
        return jsonify({'result': {'cuisine': result.data}, 'message': "Success", 'error': False})
    else:
        post = Cuisine(**request.json)
        post.save()
        result = CuisineSchema().dump(post)
        return jsonify({'result': {'cuisine': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/collection', methods=['GET', 'POST'])
def restaurant_collection_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Collection.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = CollectionSchema(many=True).dump(data)
        return jsonify({'result': {'collection': result.data}, 'message': "Success", 'error': False})
    else:
        post = Collection(**request.json)
        post.save()
        result = CollectionSchema().dump(post)
        return jsonify({'result': {'collection': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/dish', methods=['GET', 'POST'])
def restaurant_dish_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Dish.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = DishSchema(many=True).dump(data)
        return jsonify({'result': {'dish': result.data}, 'message': "Success", 'error': False})
    else:
        post = Dish(**request.json)
        post.save()
        result = DishSchema().dump(post)
        return jsonify({'result': {'dish': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/association', methods=['GET', 'POST'])
def restaurant_association_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Association.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = AssociationSchema(many=True).dump(data)
        return jsonify({'result': {'association': result.data}, 'message': "Success", 'error': False})
    else:
        post = Association(**request.json)
        post.save()
        result = AssociationSchema().dump(post)
        return jsonify({'result': {'association': result.data}, 'message': "Success", 'error': False})