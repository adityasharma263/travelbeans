# -*- coding: utf-8 -*-

from cta.model.restaurant import RestaurantImage, Restaurant, RestaurantAmenity, Menu,\
    Cuisine, Collection, RestaurantAssociation, Dish
from cta import app, db
from flask import jsonify, request
from cta.schema.restaurant import RestaurantSchema, RestaurantImageSchema,\
    RestaurantAmenitySchema, CuisineSchema, CollectionSchema, RestaurantAssociationSchema, MenuSchema, DishSchema
import simplejson as json


@app.route('/api/v1/restaurant', methods=['GET', 'POST'])
def restaurant_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        # cuisine = request.args.get('cuisine')
        # args.pop('cuisine', None)
        # menu = request.args.get('menu')
        # args.pop('menu', None)
        # amenity = request.args.get('amenity')
        # args.pop('amenity', None)
        # collection = request.args.get('collection')
        # args.pop('collection', None)
        # dish = request.args.get('dish')
        # args.pop('dish', None)
        price_start = request.args.get('price_start', None)
        price_end = request.args.get('price_end', None)
        args.pop('price_start', None)
        args.pop('price_end', None)
        page = request.args.get('page', 1)
        per_page = request.args.get('per_page', 20)
        # cuisine_restaurant_id = []
        # collection_restaurant_id = []
        # dish_restaurant_id = []
        # rating_restaurant_id = []
        # price_restaurant_id = []
        # menu_restaurant_id =[]
        # amenity_restaurant_id = []
        # common_id = []
        # is_filter = 0
        # if cuisine:
        #     is_filter = 1
        #     try:
        #         cuisine_id = Cuisine.query.filter(Cuisine.cuisine == cuisine).first().id
        #         restaurant_list = RestaurantAssociation.query.filter(RestaurantAssociation.cuisine_id == cuisine_id).all()
        #         for restaurant_obj in restaurant_list:
        #             cuisine_restaurant_id.append(restaurant_obj.restaurant_id)
        #     except:
        #         cuisine_restaurant_id = []
        # if collection:
        #     is_filter = 1
        #     try:
        #         collection_id = Collection.query.filter(Collection.collection == collection).first().id
        #         restaurant_list = RestaurantAssociation.query.filter(RestaurantAssociation.collection_id == collection_id).all()
        #         for restaurant_obj in restaurant_list:
        #             collection_restaurant_id.append(restaurant_obj.restaurant_id)
        #     except:
        #         collection_restaurant_id = []
        # if dish:
        #     is_filter = 1
        #     try:
        #         restaurant_list = Dish.query.filter(Dish.dish == dish).all()
        #         for restaurant_obj in restaurant_list:
        #             dish_restaurant_id.append(restaurant_obj.restaurant_id)
        #     except:
        #         dish_restaurant_id = []
        # if menu:
        #     is_filter = 1
        #     try:
        #         restaurant_list = Menu.query.filter(getattr(Menu, menu).is_(True)).all()
        #         for restaurant_obj in restaurant_list:
        #             menu_restaurant_id.append(restaurant_obj.restaurant_id)
        #     except:
        #         menu_restaurant_id = []
        # if amenity:
        #     is_filter = 1
        #     try:
        #         restaurant_list = RestaurantAmenity.query.filter(getattr(RestaurantAmenity, amenity).is_(True)).all()
        #         for restaurant_obj in restaurant_list:
        #             amenity_restaurant_id.append(restaurant_obj.restaurant_id)
        #     except:
        #         amenity_restaurant_id = []
        # if rating:
        #     is_filter = 1
        #     try:
        #         restaurant_list = Restaurant.query.filter(Restaurant.rating >= rating).all()
        #         for restaurant_obj in restaurant_list:
        #             rating_restaurant_id.append(restaurant_obj.id)
        #     except:
        #         rating_restaurant_id = []
        #
        # if price_start and price_end:
        #     is_filter = 1
        #     try:
        #         restaurant_list = Restaurant.query.filter(Restaurant.price >= price_start, Restaurant.price <= price_end).all()
        #         for restaurant_obj in restaurant_list:
        #             price_restaurant_id.append(restaurant_obj.id)
        #     except:
        #         price_restaurant_id = []
        # obj = {
        #     "cuisine": cuisine_restaurant_id,
        #     "collection": collection_restaurant_id,
        #     "dish": dish_restaurant_id,
        #     "price": price_restaurant_id,
        #     "rating": rating_restaurant_id,
        #     "amenity": amenity_restaurant_id,
        #     "menu": menu_restaurant_id
        # }
        # for key, value in obj.items():
        #     if value:
        #         if not common_id:
        #             common_id = value
        #         else:
        #             common_id = list(set(common_id).intersection(value))
        #
        # if is_filter:
        #     if page and per_page:
        #         restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(common_id))\
        #             .offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        #     else:
        #         restaurants = Restaurant.query.filter_by(**args).filter(Restaurant.id.in_(common_id)).all()
        # else:
        #     if page and per_page:
        #         restaurants = Restaurant.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        #     else:
        #         restaurants = Restaurant.query.filter_by(**args).all()
        q = db.session.query(Restaurant).outerjoin(Restaurant.amenities).outerjoin(Restaurant.cuisines)\
            .outerjoin(Restaurant.collections).outerjoin(Restaurant.dishes).outerjoin(Restaurant.menus)
        for key in args:
            if key in Restaurant.__dict__:
                q = q.filter(getattr(Restaurant, key) == args[key])
            elif key in RestaurantAmenity.__dict__:
                q = q.filter(getattr(RestaurantAmenity, key) == args[key])
            elif key in Menu.__dict__:
                q = q.filter(getattr(Menu, key) == args[key])
            elif key in Collection.__dict__:
                q = q.filter(getattr(Collection, key) == args[key])
            elif key in Cuisine.__dict__:
                q = q.filter(getattr(Cuisine, key) == args[key])
            elif key in Dish.__dict__:
                q = q.filter(getattr(Dish, key) == args[key])
        if price_start and price_end:
            q = q.filter(Restaurant.price >= price_start, Restaurant.price <= price_end)
        elif rating:
            q = q.filter(Restaurant.rating >= rating)
        data = q.offset((page - 1) * per_page).limit(per_page).all()
        result = RestaurantSchema(many=True).dump(data)
        return jsonify({'result': {'restaurants': result.data}, 'message': "Success", 'error': False})
    else:
        restaurant = request.json
        restaurant_obj = {
            "name": restaurant.get("name", None),
            "city": restaurant.get("city", None),
            "nearest_metro_station": restaurant.get("nearest_metro_station", None),
            "especially": restaurant.get("especially", None),
            "category": restaurant.get("category", None),
            'rating': restaurant.get("rating", None),
            "desc": restaurant.get("desc", None),
            "address": restaurant.get("address", None),
            "longitude": json.dumps(restaurant.get("longitude", None)),
            "latitude": json.dumps(restaurant.get("latitude", None)),
            "featured": restaurant.get("featured", None),
            "phone": restaurant.get("phone", None),
            "price": restaurant.get("price", None),
        }
        post = Restaurant(**restaurant_obj)
        # p = Restaurant()
        # a = RestaurantAssociation()
        # a.cuisine_id = Cuisine()
        # p.cuisines.append(a)
        post.save()
        restaurant_result = RestaurantSchema().dump(post)
        if restaurant.get("amenities"):
            amenity = restaurant.get("amenities", None)
            amenity_obj = {
                "restaurant_id": restaurant_result.data['id'],
                "home_delivery": amenity.get("home_delivery", None),
                "private_dining_area_available": amenity.get("private_dining_area_available", None),
                "kid_friendly": amenity.get("kid_friendly", None),
                "table_reservation_required": amenity.get("table_reservation_required", None),
                "table_booking_recommended": amenity.get("table_booking_recommended", None),
                "wheelchair_accessible": amenity.get("wheelchair_accessible", None),
                "buffet": amenity.get("buffet", None),
                "wifi": amenity.get("wifi", None),
                "live_entertainment": amenity.get("live_entertainment", None),
                "live_music": amenity.get("live_music", None),
                "live_sports_screening": amenity.get("live_sports_screening", None),
                "valet_parking": amenity.get("valet_parking_available", None),
                "parking": amenity.get("parking", None),
                "group_meal": amenity.get("group_meal", None),
                "smoking_area": amenity.get("smoking_area", None),
                "desserts_and_bakes": amenity.get("desserts_and_bakes", None),
                "full_bar_available": amenity.get("full_bar_available", None),
                "serves_jain_food": amenity.get("serves_jain_food", None),
                "vegetarian_only": amenity.get("vegetarian_only", None),
                "serves_non_veg": amenity.get("serves_non_veg", None),
                "nightlife": amenity.get("nightlife", None),
                "city_view": amenity.get("city_view", None),
                "brunch": amenity.get("brunch", None),
                "sunday_roast": amenity.get("sunday_roast", None),
                "gastro_pub": amenity.get("gastro_pub", None),
                "beer": amenity.get("beer", None),
                "outdoor_seating": amenity.get("outdoor_seating", None),
                "takeaway": amenity.get("takeaway", None),
                "alcohol": amenity.get("alcohol", None),
                "seating": amenity.get("seating", None),
            }
            RestaurantAmenity(**amenity_obj).save()
        if restaurant.get("menus"):
            menu = restaurant.get("menus", None)
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
        if restaurant.get("images"):
            for image in restaurant['images']:
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
                        print(cuisine_id)
                    else:
                        cuisine_obj = {
                                "cuisine": cuisines.get("cuisine", None),
                            }
                        print(cuisine_obj)
                        post = Cuisine(**cuisine_obj)
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
                                "featured": collections.get("featured", None),
                                "desc": collections.get("desc", None),
                                "image": collections.get("image", None),
                            }
                        post = Collection(**collection_obj)
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


@app.route('/api/v1/restaurant/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_id(id):
    if request.method == 'PUT':
        print(request.json)
        put = Restaurant.query.filter_by(id=id).update(request.json)
        if put:
            Restaurant.update_db()
            hotels = Restaurant.query.filter_by(id=id).first()
            result = RestaurantSchema(many=False).dump(hotels)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant = Restaurant.query.filter_by(id=id).first()
        if not restaurant:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        restaurant_amenities = RestaurantAmenity.query.filter_by(restaurant_id=id).first()
        if restaurant_amenities:
            RestaurantAmenity.delete_db(restaurant_amenities)
        restaurant_menu = Menu.query.filter_by(restaurant_id=id).first()
        if restaurant_menu:
            Menu.delete_db(restaurant_menu)
        restaurant_images = RestaurantImage.query.filter_by(restaurant_id=id).all()
        if restaurant_images:
            for restaurant_image in restaurant_images:
                RestaurantImage.delete_db(restaurant_image)
        restaurant_dishes = Dish.query.filter_by(restaurant_id=id).all()
        if restaurant_dishes:
            for restaurant_dish in restaurant_dishes:
                Dish.delete_db(restaurant_dish)
        restaurant_associations = RestaurantAssociation.query.filter_by(restaurant_id=id).all()
        if restaurant_associations:
            for restaurant_association in restaurant_associations:
                RestaurantAssociation.delete_db(restaurant_association)
        Restaurant.delete_db(restaurant)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/amenity/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_amenity_id(id):
    if request.method == 'PUT':
        put = RestaurantAmenity.query.filter_by(id=id).update(request.json)
        if put:
            RestaurantAmenity.update_db()
            s = RestaurantAmenity.query.filter_by(id=id).first()
            result = RestaurantAmenitySchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_amenities = RestaurantAmenity.query.filter_by(id=id).first()
        if not restaurant_amenities:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        RestaurantAmenity.delete_db(restaurant_amenities)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/image/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_image_id(id):
    if request.method == 'PUT':
        put = RestaurantImage.query.filter_by(id=id).update(request.json)
        if put:
            RestaurantImage.update_db()
            s = RestaurantImage.query.filter_by(id=id).first()
            result = RestaurantImageSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_images = RestaurantImage.query.filter_by(id=id).first()
        if not restaurant_images:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        RestaurantImage.delete_db(restaurant_images)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/menu/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_menu_id(id):
    if request.method == 'PUT':
        put = Menu.query.filter_by(id=id).update(request.json)
        if put:
            Menu.update_db()
            s = Menu.query.filter_by(id=id).first()
            result = MenuSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_menu = Menu.query.filter_by(id=id).first()
        if not restaurant_menu:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Menu.delete_db(restaurant_menu)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/cuisine/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_cuisine_id(id):
    if request.method == 'PUT':
        put = Cuisine.query.filter_by(id=id).update(request.json)
        if put:
            Cuisine.update_db()
            s = Cuisine.query.filter_by(id=id).first()
            result = CuisineSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_cuisine = Cuisine.query.filter_by(id=id).first()
        if not restaurant_cuisine:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        restaurant_associations = RestaurantAssociation.query.filter_by(cuisine_id=id).all()
        if restaurant_associations:
            for restaurant_association in restaurant_associations:
                RestaurantAssociation.delete_db(restaurant_association)
        Cuisine.delete_db(restaurant_cuisine)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/collection/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_collection_id(id):
    if request.method == 'PUT':
        put = Collection.query.filter_by(id=id).update(request.json)
        if put:
            Collection.update_db()
            s = Collection.query.filter_by(id=id).first()
            result = CollectionSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_collection = Collection.query.filter_by(id=id).first()
        if not restaurant_collection:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        restaurant_associations = RestaurantAssociation.query.filter_by(collection_id=id).all()
        if restaurant_associations:
            for restaurant_association in restaurant_associations:
                RestaurantAssociation.delete_db(restaurant_association)
        Collection.delete_db(restaurant_collection)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/dish/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_dish_id(id):
    if request.method == 'PUT':
        put = Dish.query.filter_by(id=id).update(request.json)
        if put:
            Dish.update_db()
            s = Dish.query.filter_by(id=id).first()
            result = DishSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_dish = Dish.query.filter_by(id=id).first()
        if not restaurant_dish:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Dish.delete_db(restaurant_dish)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


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


@app.route('/api/v1/restaurant/association/<int:id>', methods=['PUT', 'DELETE'])
def restaurant_association_id(id):
    if request.method == 'PUT':
        put = RestaurantAssociation.query.filter_by(id=id).update(request.json)
        if put:
            RestaurantAssociation.update_db()
            s = RestaurantAssociation.query.filter_by(id=id).first()
            result = RestaurantAssociationSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        restaurant_association = RestaurantAssociation.query.filter_by(id=id).first()
        if not restaurant_association:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        RestaurantAssociation.delete_db(restaurant_association)
        return jsonify({'result': {}, 'message': "Success", 'error': False})


@app.route('/api/v1/restaurant/search', methods=['GET', 'POST'])
def restaurant_search_api():
    restaurant_search = request.json
    search = restaurant_search['search']
    city = restaurant_search['city']
    names = []
    cuisines = []
    collections = []
    dishes = []
    menus = []
    categories = []
    localities = []
    restaurant_city_id = []
    try:
        restaurant_list = Restaurant.query.filter(Restaurant.city == city).all()
        for restaurant_obj in restaurant_list:
            restaurant_city_id.append(restaurant_obj.id)
    except:
        restaurant_city_id = []
    restaurant_localities = Restaurant.query.distinct(Restaurant.locality).filter(Restaurant.locality.ilike('%' + search + '%'))\
        .order_by(Restaurant.locality).all()
    for restaurant_locality in restaurant_localities:
        localities.append(restaurant_locality.locality)
    restaurant_names = Restaurant.query.distinct(Restaurant.name).filter(Restaurant.id.in_(restaurant_city_id)).filter(
        Restaurant.name.ilike('%' + search + '%')).order_by(Restaurant.name).all()
    for restaurant_name in restaurant_names:
        names.append(restaurant_name.name)
    restaurant_cuisines = Cuisine.query.distinct(Cuisine.cuisine).filter(Restaurant.id.in_(restaurant_city_id))\
        .filter(Cuisine.cuisine.ilike('%' + search + '%')).order_by(Cuisine.cuisine).all()
    for restaurant_cuisine in restaurant_cuisines:
        cuisines.append(restaurant_cuisine.cuisine)
    restaurant_collections = Collection.query.distinct(Collection.collection).filter(Restaurant.id.in_(restaurant_city_id))\
        .filter(Collection.collection.ilike('%' + search + '%')).order_by(Collection.collection).all()
    for restaurant_collection in restaurant_collections:
        collections.append(restaurant_collection.collection)
    restaurant_dishes = Dish.query.distinct(Dish.dish).filter(Restaurant.id.in_(restaurant_city_id))\
        .filter(Dish.dish.ilike('%' + search + '%')).order_by(Dish.dish).all()
    for restaurant_dish in restaurant_dishes:
        dishes.append(restaurant_dish.dish)
    restaurant_menus = ['dinner', 'cafe', 'breakfast', 'street_stalls', 'bars', 'lounge', 'diet', 'luxury', 'lunch', 'family',
                  'nightlife', 'pocket_friendly']
    for restaurant_menu in restaurant_menus:
        if restaurant_menu.startswith(search):
            menus.append(restaurant_menu)
    restaurant_categories = ["bistro", "ethnic", "fine_dining", "trattoria", "teppanyaki_ya", "osteria", "drive_in", "drive_thru",
                             "pizzeria","taverna", 'fast_casual', "pop_up", "Cafe", 'iner', 'ramen_ya', "teahouse", "fast_food",
                             "cafeteria", 'luncheonette', "tapas_bar", "steakhouse", "all_you_can_eat_restaurant", "kosher",
                             "dinner_in_the_Sky", "dark_restaurant", "a_la_carte", "gastropub", "brasserie", "chiringuito",
                             "food_truck", 'churrascaria', 'food_court', 'restrobars', 'street_stalls', "theme_resturants",
                             "coffee_shop","coffee_house","cabaret","tea_shop", "buffet"]
    for restaurant_category in restaurant_categories:
        if restaurant_category.startswith(search):
            categories.append(restaurant_category)
    obj = {
    "cuisine": list(cuisines),
    "collection": list(collections),
    "dish": list(dishes),
    "menu": list(set(menus)),
    "locality": list(set(localities)),
    "category": list(set(categories)),
    "name": list(names)
    }
    return jsonify({'result': obj, 'message': "Success", 'error': False})

