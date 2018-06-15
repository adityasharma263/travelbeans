# -*- coding: utf-8 -*-

from cta.model.price import Price
from cta import app
from flask import jsonify, request
from cta.schema.price import PriceSchema


@app.route('/api/v1/price', methods=['GET', 'POST'])
def price_api():
    if request.method == 'GET':
        args = request.args.to_dict()
        args.pop('page', None)
        args.pop('per_page', None)
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        price = Price.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
        result = PriceSchema(many=True).dump(price)
        return jsonify({'result': {'price': result.data}, 'message': "Success", 'error': False})
    else:
        post = Price(**request.json)
        post.save()
        result = PriceSchema().dump(post)
        return jsonify({'result': {'price': result.data}, 'message': "Success", 'error': False})