#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta.model.hotel import Hotel
from cta import app
from cta.schema.hotel import HotelSchema
from flask import request, render_template
import requests

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
    return render_template('stay.html', hotel=data, per_page=per_page, page=page)


@app.route('/hotel/list', methods=['GET'])
def hotel_list():
    return render_template('staylist.html')


@app.route('/hotel/detail', methods=['GET'])
def hotel_detail_id():
    return render_template('staydetail.html')


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')    

@app.route('/hotel/detail', methods=['GET'])
def stay_id():
    # hotel = Hotel.query.filter_by(id=id).first()
    # if not hotel:
        # return render_template('404.html'), 404
    data = HotelSchema().dump(hotel).data
    return render_template('staydetail.html', hotel=data)

#======================== Restaurant Section ============================

@app.route("/restaurant" , methods=['GET'])
def restaurant():
    return render_template("restaurant/Home Page With Chefs Recipies.html")


@app.route("/restaurant/search" , methods=['GET'])
def restaurant_search():
    restaurant_api_url = "http://localhost:5001/api/v1/restaurant"
    restaurant_filter = request.args
    # fetching restaurent data from api
    restaurant_request = requests.get(url=restaurant_api_url, params=restaurant_filter)
    # get json data from the api
    restaurant_data = restaurant_request.json()
    #render jinja template and pass restaurant_data as restaurant_details and acccess with in the template
    # we can access restaurant data as restaurant_details
    return render_template("restaurant/SERP Resturants.html", restaurant_details=restaurant_data)

@app.route("/restaurant/<restaurant_id>")
def restaurant_details(restaurant_id):
    single_restaurant_api_url = "http://demo7014540.mockable.io/api/v1/resturant?id="+restaurant_id
    


    return ""