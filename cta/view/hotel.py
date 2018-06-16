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
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        if from_date and to_date:
            from_date = datetime.datetime.fromtimestamp(
                int(from_date)).strftime('%Y-%m-%d %H:%M:%S')
            to_date = datetime.datetime.fromtimestamp(
                int(to_date)).strftime('%Y-%m-%d %H:%M:%S')
            args['check_in'] = from_date
            args['check_out'] = to_date
        args.pop('from_date', None)
        args.pop('to date', None)
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