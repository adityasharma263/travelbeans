# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel, Amenity, Image, Deal, Website, Facility, Member, Room
from cta import app
from flask import jsonify, request
from cta.schema.hotel import HotelSchema, AmenitySchema, ImageSchema, DealSchema, WebsiteSchema, FacilitySchema, MemberSchema, RoomSchema
import datetime


@app.route('/api/v1/hotel', methods=['GET', 'POST'])
def hotel_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        hotels = Hotel.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = HotelSchema(many=True).dump(hotels)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})
    else:
        hotel = request.json
        hotel_obj = {
        "id": hotel.get("id", None),
        "name" : hotel.get("name", None),
        "city" : hotel.get("city", None),
        'rating' : hotel.get("rating", None),
        "desc" : hotel.get("desc", None),
        "address" : hotel.get("address", None),
        "star" : hotel.get("star", None),
        }
        print(hotel_obj)
        post = Hotel(**hotel_obj)
        post.save()
        amenity = hotel.get("amenities", None)
        if amenity:
            amenity_obj = {
                "hotel_id": hotel_obj['id'],
                "Room_cleaning_service": amenity.get("Room_cleaning_service", None),
                "banquets": amenity.get("banquets", None),
                "bar": amenity.get("bar", None),
                "child_baby_cot": amenity.get("child_baby_cot", None),
                "conference_room": amenity.get("conference_room", None),
                "doorman": amenity.get("doorman", None),
                "express_check_in_out": amenity.get("express_check_in_out", None),
                "gym": amenity.get("gym", None),
                "hairdresser": amenity.get("hairdresser", None),
                "indoor_swimming_pool": amenity.get("indoor_swimming_pool", None),
                "laundry_service": amenity.get("laundry_service", None),
                "lift": amenity.get("lift", None),
                "non_smoking_smoking_rooms": amenity.get("non_smoking_smoking_rooms", None),
                "outdoor_swimming_pool": amenity.get("outdoor_swimming_pool", None),
                "pet_allowance": amenity.get("pet_allowance", None),
                "pool": amenity.get("pool", None),
                "porter_service": amenity.get("porter_service", None),
                "restaurant": amenity.get("restaurant", None),
                "spa": amenity.get("spa", None),
                "terrace": amenity.get("terrace", None),
                "twenty_four_hr_reception": amenity.get("twenty_four_hr_reception", None),
                "twenty_four_hr_room_service": amenity.get("twenty_four_hr_room_service", None),
                "wheelchair_accessible": amenity.get("wheelchair_accessible", None),
                "wifi_in_lobby": amenity.get("wifi_in_lobby", None)

            }
            print(amenity_obj)
            Amenity(**amenity_obj).save()
        if hotel['images']:
            for image in hotel['images']:
                image_obj = {
                    "image_url": image.get("image_url", None),
                    "hotel_id": hotel_obj['id']
                }
                print(image_obj)
                Image(**image_obj).save()
        if hotel['rooms']:
            for room in hotel['rooms']:
                room_obj = {
                    "id": hotel.get("id", None),
                    "room_type": hotel.get("room_type", None),
                    "check_in": datetime.datetime.now(),
                    "check_out": datetime.datetime.now(),
                    "status": True,
                    "breakfast": hotel.get("breakfast", None),
                    "balcony": hotel.get("ac", None),
                    "hotel_id": hotel_obj['id']
                }
                print(room_obj)
                Room(**room_obj).save()
                member = room.get("member", None)
                if member:
                    member_obj = {
                    "no_of_adults" : member.get("no_of_adults", None),
                    "total_members" : member.get("total_members", None),
                    "children" : member.get("children", None),
                    "room_id" : room_obj['id'],
                    }
                    print(member_obj)
                    Member(**member_obj).save()
                facility = room.get("facilities", None)
                facility_obj = {
                    "room_id": room_obj['id'],
                    "ac": facility.get("ac", None),
                    "bed_type": facility.get("bed_type", None),
                    "no_of_bed": facility.get("no_of_bed", None),
                    "bathroom_cosmetics": facility.get("bathroom_cosmetics", None),
                    "bathroom_nightie": facility.get("bathroom_nightie", None),
                    "bathroom_towels": facility.get("bathroom_towels", None),
                    "bathroom_with_shower": facility.get("bathroom_with_shower", None),
                    "desk": facility.get("desk", None),
                    "electric_kettle": facility.get("electric_kettle", None),
                    "fan": facility.get("fan", None),
                    "food_serve_at_room": facility.get("food_serve_at_room", None),
                    "free_evening_snacks": facility.get("free_evening_snacks", None),
                    "free_toiletries": facility.get("free_toiletries", None),
                    "hairdryer": facility.get("hairdryer", None),
                    "heater": facility.get("heater", None),
                    "ironing_facility": facility.get("ironing_facility", None),
                    "morning_newspaper": facility.get("morning_newspaper", None),
                    "phone": facility.get("phone", None),
                    "room_safe": facility.get("room_safe", None),
                    "room_seating_area": facility.get("room_seating_area", None),
                    "room_slipper": facility.get("room_slipper", None),
                    "tv": facility.get("tv", None),
                    "view": facility.get("view", None),
                    "wardrobes_closet": facility.get("wardrobes_closet", None),
                    "weighing_machine": facility.get("weighing_machine", None),
                    "wifi": facility.get("wifi", None)
                }
                Facility(**facility_obj).save()
                if room['deals']:
                    for deal in room['deals']:
                        deal_obj = {
                        "id": deal.get("id", None),
                        "price" : deal.get("price", None),
                        "weekend" : deal.get("weekend", None),
                        "hotel_url": deal.get("hotel_url", None),
                        "room_id" : room_obj['id'],
                        "website_id" : deal.get("website_id", None)
                        }
                        print(deal_obj)
                        Deal(**deal_obj).save()
        return jsonify({'result': {'hotel': request.json}, 'message': "Success", 'error': False})


@app.route('/api/v1/room', methods=['GET', 'POST'])
def room_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        check_in = request.args.get('check_in')
        check_out = request.args.get('check_out')
        if check_in and check_out:
            check_in = datetime.datetime.fromtimestamp(
                int(check_in)).strftime('%Y-%m-%d %H:%M:%S')
            check_out = datetime.datetime.fromtimestamp(
                int(check_out)).strftime('%Y-%m-%d %H:%M:%S')
            args['check_in'] = check_in
            args['check_out'] = check_out
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        rooms = Room.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = RoomSchema(many=True).dump(rooms)
        return jsonify({'result': {'rooms': result.data}, 'message': "Success", 'error': False})
    else:
        post = Room(**request.json)
        post.save()
        result = AmenitySchema().dump(post)
        return jsonify({'result': {'room': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/amenity', methods=['GET', 'POST'])
def amenity_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Amenity.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = AmenitySchema(many=True).dump(data)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})
    else:
        post = Amenity(**request.json)
        post.save()
        result = AmenitySchema().dump(post)
        return jsonify({'result': {'amenities': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/images', methods=['GET', 'POST'])
def image_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Image.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = ImageSchema(many=True).dump(data)
        return jsonify({'result': {'images': result.data}, 'message': "Success", 'error': False})
    else:
        post = Image(**request.json)
        post.save()
        result = ImageSchema().dump(post)
        return jsonify({'result': {'image': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/member', methods=['GET', 'POST'])
def member_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        members = Member.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = MemberSchema(many=True).dump(members)
        return jsonify({'result': {'members': result.data}, 'message': "Success", 'error': False})
    else:
        post = Member(**request.json)
        post.save()
        result = MemberSchema().dump(post)
        return jsonify({'result': {'member': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/facility', methods=['GET', 'POST'])
def facility_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        data = Facility.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = FacilitySchema(many=True).dump(data)
        return jsonify({'result': {'facilities': result.data}, 'message': "Success", 'error': False})
    else:
        post = Facility(**request.json)
        post.save()
        result = FacilitySchema().dump(post)
        return jsonify({'result': {'facilities': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/website', methods=['GET', 'POST'])
def website_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        web = Website.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = WebsiteSchema(many=True).dump(web)
        return jsonify({'result': {'website': result.data}, 'message': "Success", 'error': False})
    else:
        post = Website(**request.json)
        post.save()
        result = WebsiteSchema().dump(post)
        return jsonify({'result': {'website': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/deal', methods=['GET', 'POST'])
def deal_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        price = Deal.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = DealSchema(many=True).dump(price)
        return jsonify({'result': {'deal': result.data}, 'message': "Success", 'error': False})
    else:
        post = Deal(**request.json)
        post.save()
        result = DealSchema().dump(post)
        return jsonify({'result': {'deal': result.data}, 'message': 'Success', 'error': False})
