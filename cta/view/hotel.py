# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel
from cta import app
from flask import jsonify, request
from cta.schema.hotel import HotelSchema


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
        post = Hotel(**request.json)
        post.save()
        result = HotelSchema().dump(post)
        return jsonify({'result': {'hotel': result.data}, 'message': "Success", 'error': False})