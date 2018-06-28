#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta.model.hotel import Hotel
from cta import app
from cta.schema.hotel import HotelSchema
from flask import request, jsonify, render_template
import time
from  sqlalchemy.sql.expression import func
from cta import db


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
def hlist():
    args = request.args.to_dict()
    args.pop('page', None)
    args.pop('per_page', None)
    per_page = int(request.args.get('per_page', 10))
    page = int(request.args.get('page', 1))
    hotel = Hotel.query.filter_by(**args).offset((page - 1) * per_page).limit(per_page).all()
    data = HotelSchema(many=True).dump(hotel)
    return render_template('staylist.html',hotel=data,per_page=per_page,page=page)    

@app.route('/home', methods=['GET'])
def home():
    
    return render_template('index.html')

@app.route('/admin', methods=['GET'])
def admin():
    
    return render_template('admin.html')    

@app.route('/hotel-list/<string:name>', methods=['GET'])
def stay_id(name):
    hotel = Hotel.query.filter_by(name=name).first()
    if not hotel:
        return render_template('404.html'), 404
    data = HotelSchema().dump(hotel).data
    return render_template('staydetail.html', hotel=data)
    