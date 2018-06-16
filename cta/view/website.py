# -*- coding: utf-8 -*-

from cta.model.website import Website
from cta import app
from flask import jsonify, request
from cta.schema.website import WebsiteSchema


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
        return jsonify({'result': {'price': result.data}, 'message': "Success", 'error': False})
    else:
        post = Website(**request.json)
        post.save()
        result = WebsiteSchema().dump(post)
        return jsonify({'result': {'price': result.data}, 'message': "Success", 'error': False})