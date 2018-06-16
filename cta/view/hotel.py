# -*- coding: utf-8 -*-

from cta.model.hotel import Hotel
from cta import app
from flask import jsonify, request
from cta.schema.hotel import HotelSchema
import datetime


@app.route('/api/v1/hotel', methods=['GET', 'POST'])
def hotel_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        date_from = request.args.get('date_from')
        date_to = request.args.get('date_to')
        if date_from and date_to:
            date_from = datetime.datetime.fromtimestamp(
                int(date_from)).strftime('%Y-%m-%d %H:%M:%S')
            date_to = datetime.datetime.fromtimestamp(
                int(date_to)).strftime('%Y-%m-%d %H:%M:%S')
            args['check_in'] = date_from
            args['check_out'] = date_to
        args.pop('date_from', None)
        args.pop('date_to', None)
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