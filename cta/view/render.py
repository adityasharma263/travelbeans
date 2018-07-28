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
    args = request.args.to_dict()
    restaurant_data = requests.get(url=restaurant_api_url, params=args).json()['result']['restaurants']
    searched_value = ''
    if args:
        searched_value = list(args.values())[0]
    return render_template("restaurant/restaurant_search.html", restaurant_details=restaurant_data, args=args, searched_value=searched_value)


@app.route("/restaurant/<int:restaurant_id>", methods=['GET'])
def restaurant_detail(restaurant_id):
    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant?id="+str(restaurant_id)
    restaurant_data = requests.get(url=restaurant_api_url).json()['result']['restaurants'][0]
    if restaurant_data['amenities']:
        restaurant_data['amenities'].pop("id", None)
        restaurant_data['amenities'].pop("restaurant", None)
    return render_template("restaurant/restaurant_details.html", restaurant_detail=restaurant_data)

@app.route("/restaurant/search/suggestion", methods=["GET"])
def restaurant_search_sugg():
    args = request.args
    search_query = args.get("q")
    suggestion = requests.post(app.config["DOMAIN_URL"]+"/api/v1/restaurant/search", json={"search" : search_query}).json()
    print(suggestion)
    return suggestion

#=========================== CABS =======================================

@app.route("/cab", methods=['GET'])
def cab():
    return render_template("cab/cab.html")

@app.route('/admin/cab', methods=['GET'])
def cab_admin():
    return render_template('cab/admin_cab.html')   

@app.route('/cab/list', methods=['GET'])
def cab_list():
    return render_template('cab/cab_list.html')    

   
