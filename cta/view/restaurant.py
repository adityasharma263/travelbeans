# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel, Amenity, Image, Deal, Website, Facility, Member, Room
from cta import app
from flask import jsonify, request
from cta.schema.hotel import HotelSchema, AmenitySchema, ImageSchema, DealSchema, WebsiteSchema, FacilitySchema, MemberSchema, RoomSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/hotel', methods=['GET', 'POST'])
def hotel_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        rating = request.args.get('rating')
        args.pop('rating', None)
        page = request.args.get('page', None)
        per_page = request.args.get('per_page', None)
        if rating:
            hotels = Hotel.query.filter_by(**args).filter(Hotel.rating >= rating).all()
        elif page:
            hotels = Hotel.query.filter_by(**args).offset((int(page) - 1) * int(per_page)).limit(int(per_page)).all()
        else:
            hotels = Hotel.query.filter_by(**args).all()
        result = HotelSchema(many=True).dump(hotels)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})