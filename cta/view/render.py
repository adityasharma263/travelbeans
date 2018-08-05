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

@app.route('/hotel/collection/bed-and-breakfast-travel-beans', methods=['GET'])
def collection1():
    return render_template('hotel/collections/bed-and-breakfast.html')   

@app.route('/hotel/collection/boatstays-travel-beans', methods=['GET'])
def collection2():
    return render_template('hotel/collections/boatstays.html')   

@app.route('/hotel/collection/boutique-hotels-travel-beans', methods=['GET'])
def collection3():
    return render_template('hotel/collections/boutique-hotels.html')  

@app.route('/hotel/collection/budget-hotels-travel-beans', methods=['GET'])
def collection4():
    return render_template('hotel/collections/budget-hotels.html')                

@app.route('/hotel/collection/campsite-travel-beans', methods=['GET'])
def collection5():
    return render_template('hotel/collections/campsite.html')   



#======================== RESTAURANT ============================


@app.route("/restaurant", methods=['GET'])
def restaurant():
    collections = requests.get( str(app.config["DOMAIN_URL"]) +"/api/v1/restaurant/collection").json()['result']['collection']
    return render_template("restaurant/restaurant.html", collections=collections)

@app.route("/restaurant/collection", methods=["GET"])
def restaurant_collection():
    return render_template("restaurant/collections.html")

@app.route("/restaurant/search", methods=['GET'])
def restaurant_search():
    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant"   
    args = request.args.to_dict()
    restaurant_data = requests.get(url=restaurant_api_url, params=args).json()['result']['restaurants']
    searched_value = ''
    searched_key  = ''
    if args:
        searched_value = list(args.values())[0]
        searched_key = list(args.keys())[0]
    return render_template("restaurant/restaurant_search.html", restaurant_details=restaurant_data, args=args, searched_value=searched_value, searched_key=searched_key)


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
    return suggestion


@app.route("/admin/restaurant", methods=["GET"])
def admin_restaurant():
    return render_template("restaurant/restaurant_dashboard.html")


@app.route("/admin/restaurant/amenity", methods=['GET'])
def admin_amenity():
    return render_template("restaurant/restaurant_amenity_dashboard.html")
    

@app.route("/admin/restaurant/dish", methods=['GET'])
def admin_dish():
    return render_template("restaurant/restaurant_dish_dashboard.html")
    

@app.route("/admin/restaurant/collection", methods=['GET'])
def admin_collection():
    return render_template("restaurant/restaurant_collection_dashboard.html")
    

@app.route("/admin/restaurant/cuisine", methods=['GET'])
def admin_cuisine():
    return render_template("restaurant/restaurant_cuisine_dashboard.html")

@app.route("/admin/restaurant/menu", methods=['GET'])
def admin_menu():
    return render_template("restaurant/restaurant_menu_dashboard.html")

@app.route("/admin/restaurant/images", methods=['GET'])
def admin_images():
    return render_template("restaurant/restaurant_images_dashboard.html")

@app.route("/admin/restaurant/association" , methods=['GET'])
def admin_association():
    return render_template("restaurant/restaurant_association_dashboard.html")


#=========================== CABS =======================================


@app.route("/cab", methods=['GET'])
def cab():
    return render_template("cab/cab.html")


@app.route('/admin/cab', methods=['GET'])
def cab_admin():
    return render_template('cab/admin_cab.html')   


@app.route('/cab/list', methods=['GET'])
def cab_list():
    cab_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/cab"
    args = request.args
    cab_data = requests.get(url=cab_api_url, params=args).json()
    return render_template('cab/monthly_rental_list.html', cab_details=cab_data)


@app.route('/cab/detail', methods=['GET'])
def cab_detail():
    return render_template('cab/cab_detail.html')
