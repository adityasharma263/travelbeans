# -*- coding: utf-8 -*-
__author__ = 'aditya'

from cta.model.stay import Stay
from cta import app
from cta.schema.stay import StaySchema
from flask import request, jsonify, render_template
import time
from  sqlalchemy.sql.expression import func
from cta import db


@app.route('/stay', methods=['GET'])
def home():
    args = request.args.to_dict()
    args.pop('page', None)
    args.pop('per_page', None)
    per_page = int(request.args.get('per_page', 10))
    page = int(request.args.get('page', 1))
    stay = Stay.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
    data = StaySchema(many=True).dump(stay)
    return render_template('stay.html',stay=data,per_page=per_page,page=page)

@app.route('/stay/<string:slug>', methods=['GET'])
def stay_id(slug):
    events = Event.query.filter_by(slug=slug).first()
    if not stay:
        return render_template('404.html'), 404
    data = StaySchema().dump(stay).data
    return render_template('stayss.html', stay=data)
    