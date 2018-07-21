#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta import app
from flask import render_template, request
import requests


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


#======================== HOTEL ============================


@app.route('/hotel', methods=['GET'])
def hotel():
    return render_template('hotel/hotel.html')


@app.route('/hotel/list', methods=['GET'])
def hotel_list():
    return render_template('hotel/hotel_list.html')


@app.route('/hotel/<hotel_id>', methods=['GET'])
def hotel_detail(hotel_id):
    return render_template('hotel/hotel_detail.html')


@app.route('/admin/hotel', methods=['GET'])
def admin():
    return render_template('hotel/admin_hotel.html')


#======================== RESTAURANT ============================


@app.route("/restaurant", methods=['GET'])
def restaurant():
    return render_template("restaurant/restaurant.html")


@app.route("/restaurant/search", methods=['GET'])
def restaurant_search():
    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant"
    args = request.args
    restaurant_data = requests.get(url=restaurant_api_url, params=args).json()
    return render_template("restaurant/restaurant_search.html", restaurant_details=restaurant_data)


@app.route("/restaurant/<restaurant_id>", methods=['GET'])
def restaurant_detail(restaurant_id):
    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant"
    restaurant_data = requests.get(url=restaurant_api_url, params={id: restaurant_id}).json()
    return render_template("restaurant/restaurant_detail.html", restaurant_detail=restaurant_data)

@app.route("/restaurant/search/suggestion", methods=["GET"])
def restaurant_search_sugg():
    args = request.args
    
    return ""