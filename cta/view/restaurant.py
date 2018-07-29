# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Menu,\
    Cuisine, Collection, RestaurantAssociation, Dish
from cta import app
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImageSchema,\
    RestaurantAmenitySchema, CuisineSchema, CollectionSchema, RestaurantAssociationSchema, MenuSchema, DishSchema
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
        is_filter = 0
        if cuisine:
            is_filter = 1
            try:
                cuisine_id = Cuisine.query.filter(Cuisine.cuisine == cuisine).first().id
                restaurant_list = RestaurantAssociation.query.filter(RestaurantAssociation.cuisine_id == cuisine_id).all()
                for restaurant_obj in restaurant_list:
                    cuisine_restaurant_id.append(restaurant_obj.restaurant_id)
            except:
                collection_restaurant_id = []
        if collection:
            is_filter = 1
            try:
                collection_id = Collection.query.filter(Collection.collection == collection).first().id
                restaurant_list = RestaurantAssociation.query.filter(RestaurantAssociation.collection_id == collection_id).all()
                for restaurant_obj in restaurant_list:
                    collection_restaurant_id.append(restaurant_obj.restaurant_id)
            except:
                collection_restaurant_id = []
        if dish:
            is_filter = 1
            try:
                restaurant_list = Dish.query.filter(Dish.dish == dish).all()
                for restaurant_obj in restaurant_list:
                    dish_restaurant_id.append(restaurant_obj.restaurant_id)
            except:
                dish_restaurant_id = []
        if menu:
            is_filter = 1
            try:
                restaurant_list = Menu.query.filter(getattr(Menu, menu).is_(True)).all()
                for restaurant_obj in restaurant_list:
                    menu_restaurant_id.append(restaurant_obj.restaurant_id)
            except:
                menu_restaurant_id = []
        if amenity:
            is_filter = 1
            try:
                restaurant_list = RestaurantAmenity.query.filter(getattr(RestaurantAmenity, amenity).is_(True)).all()
                for restaurant_obj in restaurant_list:
                    amenity_restaurant_id.append(restaurant_obj.restaurant_id)
            except:
                amenity_restaurant_id = []
        if rating:
            is_filter = 1
            try:
                restaurant_list = Restaurant.query.filter(Restaurant.rating >= rating).all()
                for restaurant_obj in restaurant_list:
                    rating_restaurant_id.append(restaurant_obj.id)
            except:
                rating_restaurant_id = []

        if price_start and price_end:
            is_filter = 1
            try:
                restaurant_list = Restaurant.query.filter(Restaurant.price >= price_start, Restaurant.price <= price_end).all()
                for restaurant_obj in restaurant_list:
                    price_restaurant_id.append(restaurant_obj.id)
            except:
                price_restaurant_id = []
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

        if is_filter:
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
    else:
        restaurant = request.json
        restaurant_obj = {
            "name": restaurant.get("name", None),
            "city": restaurant.get("city", None),
            "category": restaurant.get("category", None),
            'rating': Restaurant.get("rating", None),
            "desc": restaurant.get("desc", None),
            "address": restaurant.get("address", None),
            "longitude": json.dumps(restaurant.get("longitude", None)),
            "latitude": json.dumps(restaurant.get("latitude", None)),
            "featured": restaurant.get("featured", None),
            "phone": restaurant.get("phone", None),
            "price": restaurant.get("price", None),
        }
        post = Restaurant(**restaurant_obj)
        post.save()
        restaurant_result = RestaurantSchema().dump(post)
        if restaurant.get("menu"):
            menu = restaurant.get("menu", None)
            menu_obj = {
                "restaurant_id": restaurant_result.data['id'],
                "breakfast": menu.get("breakfast", None),
                "lunch": menu.get("lunch", None),
                "dinner": menu.get("dinner", None),
                "cafe": menu.get("cafe", None),
                "lounge": menu.get("lounge", None),
                "family": menu.get("family", None),
                "bars": menu.get("bars", None),
                "nightlife": menu.get("nightlife", None),
                "street_stalls": menu.get("street_stalls", None),
                "pocket_friendly": menu.get("pocket_friendly", None),
                "diet": menu.get("diet", None),
                "luxury": menu.get("luxury", None),
            }
            Menu(**menu_obj).save()
        if restaurant.get("restaurant_images"):
            for image in restaurant['restaurant_images']:
                image_obj = {
                    "image_url": image.get("image_url", None),
                    "image_type": image.get("image_type", None),
                    "restaurant_id": restaurant_result.data['id']
                }
                RestaurantImage(**image_obj).save()
        if restaurant.get("dishes"):
            for dish in restaurant['dishes']:
                dish_obj = {
                    "dish": dish.get("dish", None),
                    "dish_type": dish.get("dish_type", None),
                    "full_price": dish.get("full_price", None),
                    "half_price": dish.get("half_price", None),
                    "desc": dish.get("desc", None),
                    "image": dish.get("image", None),
                    "restaurant_id": restaurant_result.data['id']
                }
                Dish(**dish_obj).save()
        if restaurant.get("association"):
            for association in restaurant['association']:
                if association.get("cuisines"):
                    cuisines = association.get("cuisines")
                    if cuisines.get("cuisine_id"):
                        cuisine_id = cuisines.get("cuisine_id")
                    else:
                        cuisine_obj = {
                                "cuisine": cuisines.get("cuisine", None),
                            }
                        post = Cuisine(**cuisine_obj).save()
                        post.save()
                        cuisine_result = CuisineSchema().dump(post)
                        cuisine_id = cuisine_result.data['id']
                if association.get("collections"):
                    collections = association.get("collections")
                    if collections.get("collection_id"):
                        collection_id = collections.get("collection_id")
                    else:
                        collection_obj = {
                                "collection": collections.get("collection", None),
                                "image": collections.get("image", None),
                            }
                        post = Collection(**collection_obj).save()
                        post.save()
                        collection_result = CollectionSchema().dump(post)
                        collection_id = collection_result.data['id']
                if association.get("cuisines") or association.get("collections"):
                    association_obj = {
                        "restaurant_id": restaurant_result.data['id'],
                        "cuisine_id": cuisine_id,
                        "collection_id": collection_id,
                    }
                    RestaurantAssociation(**association_obj).save()
        return jsonify({'result': {'restaurant': restaurant}, 'message': "Success", 'error': False})


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
        data = RestaurantAssociation.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantAssociationSchema(many=True).dump(data)
        return jsonify({'result': {'association': result.data}, 'message': "Success", 'error': False})
    else:
        post = RestaurantAssociation(**request.json)
        post.save()
        result = RestaurantAssociationSchema().dump(post)
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
    "city": list(cities),
    "cuisine": list(cuisines),
    "collection": list(collections),
    "dish": list(dishes),
    "menu": list(set(menus)),
    "name": list(names)
    }
    return jsonify({'result': obj, 'message': "Success", 'error': False})

