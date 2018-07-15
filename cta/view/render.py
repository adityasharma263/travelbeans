#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta.model.hotel import Hotel
from cta import app
from cta.schema.hotel import HotelSchema
from flask import request, jsonify, render_template


@app.route('/hotel', methods=['GET'])
def hotel():
    return render_template('stay.html')


@app.route('/hotel/list', methods=['GET'])
def hlist():
    return render_template('staylist.html')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')    


@app.route('/hotel/detail/<string:name>', methods=['GET'])
def stay_id(name):
    hotel = Hotel.query.filter_by(name=name).first()
    if not hotel:
        return render_template('404.html'), 404
    data = HotelSchema().dump(hotel).data
    return render_template('staydetail.html', hotel=data)