#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta import app
from flask import render_template


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

########## HOTEL

@app.route('/hotel', methods=['GET'])
def hotel():
    return render_template('stay.html')


@app.route('/hotel/list', methods=['GET'])
def hotel_list():
    return render_template('stay_list.html')


@app.route('/hotel/detail/<int:id>', methods=['GET'])
def hotel_detail(id):
    return render_template('stay_detail.html')


@app.route('/admin/hotel', methods=['GET'])
def admin():
    return render_template('admin_hotel.html')


