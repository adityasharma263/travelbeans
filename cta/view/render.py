#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta.model.hotel import Hotel
from cta import app
from cta.schema.hotel import HotelSchema
from flask import request, jsonify, render_template


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/hotel', methods=['GET'])
def hotel():
    args = request.args.to_dict()
    args.pop('page', None)
    args.pop('per_page', None)
    per_page = int(request.args.get('per_page', 10))
    page = int(request.args.get('page', 1))
    hotel = Hotel.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
    data = HotelSchema(many=True).dump(hotel)
    return render_template('stay.html',hotel=data,per_page=per_page,page=page)


@app.route('/hotel/list', methods=['GET'])
def hotel_list():
    return render_template('staylist.html')


@app.route('/hotel/detail', methods=['GET'])
def hotel_id():
    return render_template('staydetail.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')    


