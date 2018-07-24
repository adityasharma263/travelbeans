# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Menu,\
    Cuisine, Collection, Association, Dish
from cta import app
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImageSchema,\
    RestaurantAmenitySchema, CuisineSchema, CollectionSchema, AssociationSchema, MenuSchema, DishSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/restaurant', methods=['GET', 'POST'])
def restaurant_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        cuisine = request.args.get('cuisine')
        args.pop('cuisine', None)
        menu = request.args.get('menu')
        args.pop('menu', None)
        amenity = request.args.get('amenity')
        args.pop('amenity', None)
        collection = request.args.get('collection')
        args.pop('collection', None)
        dish = request.args.get('dish')
        args.pop('dish', None)
        price_start = request.args.get('price_start', None)
        price_end = request.args.get('price_end', None)
        args.pop('price_start', None)
        args.pop('price_end', None)
        page = request.args.get('page', None)
        per_page = request.args.get('per_page', None)
        cuisine_restaurant_id = []
        collection_restaurant_id = []
        dish_restaurant_id = []
        rating_restaurant_id = []
        price_restaurant_id = []
        menu_restaurant_id =[]
        amenity_restaurant_id = []
        common_id = []
        if cuisine:
            cuisine_id = Cuisine.query.filter(Cuisine.cuisine == cuisine).first().id
            restaurant_list = Association.query.filter(Association.cuisine_id == cuisine_id).all()
            for restaurant_obj in restaurant_list:
                cuisine_restaurant_id.append(restaurant_obj.restaurant_id)
        if collection:
            collection_id = Collection.query.filter(Collection.collection == collection).first().id
            restaurant_list = Association.query.filter(Association.collection_id == collection_id).all()
            for restaurant_obj in restaurant_list:
                collection_restaurant_id.append(restaurant_obj.restaurant_id)
        if dish:
            dish_id = Dish.query.filter(Dish.dish == dish).first().id
            restaurant_list = Association.query.filter(Association.dish_id == dish_id).all()
            for restaurant_obj in restaurant_list:
                dish_restaurant_id.append(restaurant_obj.restaurant_id)
        if menu:
            restaurant_list = Menu.query.filter(getattr(Menu, menu).is_(True)).all()
            for restaurant_obj in restaurant_list:
                menu_restaurant_id.append(restaurant_obj.restaurant_id)
        if amenity:
            restaurant_list = RestaurantAmenity.query.filter(getattr(RestaurantAmenity, amenity).is_(True)).all()
            for restaurant_obj in restaurant_list:
                amenity_restaurant_id.append(restaurant_obj.restaurant_id)
        if rating:
            restaurant_list = Restaurant.query.filter(Restaurant.rating >= rating).all()
            for restaurant_obj in restaurant_list:
                rating_restaurant_id.append(restaurant_obj.restaurant_id)
        if price_start and price_end:
            restaurant_list = Restaurant.query.filter(Restaurant.price >= price_start, Restaurant.price <= price_end).all()
            for restaurant_obj in restaurant_list:
                price_restaurant_id.append(restaurant_obj.restaurant_id)
        obj = {
            "cuisine": cuisine_restaurant_id,
            "collection": collection_restaurant_id,
            "dish": dish_restaurant_id,
            "price": price_restaurant_id,
            "rating": rating_restaurant_id,
            "amenity": amenity_restaurant_id,
            "menu": menu_restaurant_id
        }
        for key, value in obj.items():
            if value:
                if not common_id:
                    common_id = value
                else:
                    common_id = list(set(common_id).intersection(value))

        if common_id:
            if page and per_page:
                restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(common_id))\
                    .offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
            else:
                restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(common_id)).all()
        else:
            if page and per_page:
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


@app.route('/api/v1/restaurant/menu', methods=['GET', 'POST'])
def restaurant_menu_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Menu.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = MenuSchema(many=True).dump(data)
        return jsonify({'result': {'menu': result.data}, 'message': "Success", 'error': False})
    else:
        post = Menu(**request.json)
        post.save()
        result = MenuSchema().dump(post)
        return jsonify({'result': {'menu': result.data}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/search', methods=['GET', 'POST'])
def restaurant_search_api():
    search = request.json
    search = search['search']
    cities = []
    names = []
    cuisines = []
    collections = []
    dishes = []
    menus = []
    restaurant_cities = Restaurant.query.distinct(Restaurant.city).filter(Restaurant.city.ilike('%' + search + '%')).order_by(Restaurant.city).all()
    for restaurant_city in restaurant_cities:
        cities.append(restaurant_city.city)
    restaurant_names = Restaurant.query.distinct(Restaurant.name).filter(Restaurant.name.ilike('%' + search + '%')).order_by(Restaurant.name).all()
    for restaurant_name in restaurant_names:
        names.append(restaurant_name.name)
    restaurant_cuisines = Cuisine.query.distinct(Cuisine.cuisine).filter(Cuisine.cuisine.ilike('%' + search + '%')).order_by(Cuisine.cuisine).all()
    for restaurant_cuisine in restaurant_cuisines:
        cuisines.append(restaurant_cuisine.cuisine)
    restaurant_collections = Collection.query.distinct(Collection.collection).filter(Collection.collection.ilike('%' + search + '%')).order_by(Collection.collection).all()
    for restaurant_collection in restaurant_collections:
        collections.append(restaurant_collection.collection)
    restaurant_dishes = Dish.query.distinct(Dish.dish).filter(Dish.dish.ilike('%' + search + '%')).order_by(Dish.dish).all()
    for restaurant_dish in restaurant_dishes:
        dishes.append(restaurant_dish.dish)
    restaurant_menus = ['dinner', 'cafe', 'breakfast', 'street_stalls', 'bars', 'lounge', 'diet', 'luxury', 'lunch', 'family',
                  'nightlife', 'pocket_friendly']
    for restaurant_menu in restaurant_menus:
        if restaurant_menu.startswith(search):
            menus.append(restaurant_menu)
    obj = {
    "cities": list(cities),
    "cuisines": list(cuisines),
    "collections": list(collections),
    "dishes": list(dishes),
    "menus": list(set(menus)),
    "names": list(names)
    }
    return jsonify({'result': obj, 'message': "Success", 'error': False})

