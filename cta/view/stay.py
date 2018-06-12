# -*- coding: utf-8 -*-

from cta.model.stay import Stay
from cta import app
from flask import jsonify, request
from cta.schema.stay import StaySchema


@app.route('/api/v1/stay', methods=['GET', 'POST'])
def stay_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        stay = Stay.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = StaySchema(many=True).dump(stay)
        return jsonify({'result': {'stay': result.data}, 'message': "Success", 'error': False})
    else:
        post = Stay(**request.json)
        post.save()
        result = StaySchema().dump(post)
        return jsonify({'result': {'stay': result.data}, 'message': "Success", 'error': False})