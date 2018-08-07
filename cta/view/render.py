#-*- coding: utf-8 -*-
__author__ = 'aditya'

from cta import app
from flask import render_template, request, make_response, jsonify
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
    check_location = request.cookies.get("location")

    featured_restaurant_params = {
            "featured":True
            }
    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant"   
            
    featured_restaurant_data = requests.get(url=restaurant_api_url, params=featured_restaurant_params).json()['result']['restaurants']
    cuisine_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant/cuisine"
    cuisine_data = requests.get(url=cuisine_api_url).json()['result']['cuisine']
    

    # if not check_location:
    #     return render_template("restaurant/restaurant_choose_location.html")
    collections = requests.get( str(app.config["DOMAIN_URL"]) +"/api/v1/restaurant/collection").json()['result']['collection']
    return render_template("restaurant/restaurant.html", cuisine_data=cuisine_data, collections=collections, featured_restaurant_data=featured_restaurant_data)

@app.route("/restaurant/collection", methods=["GET"])
def restaurant_collection():
    return render_template("restaurant/collections.html")

@app.route("/restaurant/location")
def restaurant_location():
    locations = [
      'Abu',
      'Agartala',
      'Ahmedabad',
      'Aizawl',
      'Ajmer',
      'Allahabad',
      'Almora',
      'Along',
      'Alwar',
      'Amarnath',
      'Ambala',
      'Amboli',
      'Amritsar',
      'Andaman',
      'Andhra Pradesh',
      'Araku',
      'Arunachal Pradesh',
      'Assam',
      'Auli',
      'Aurangabad',
      'Badrinath',
      'Bagan',
      'Bagdogra',
      'Bakkhali',
      'Bali',
      'Bandhavgarh',
      'Bandipur',
      'Bangalore',
      'Banjar',
      'Barot',
      'Batala',
      'Bhandardara',
      'Bhangarh',
      'Bharatpur',
      'Bhatinda',
      'Bhimashankar',
      'Bhimtal',
      'Bhopal',
      'Bihar',
      'Bikaner',
      'Bir-Billing',
      'Bundi',
      'Chail',
      'Chalakudy',
      'Chamba',
      'Champawat',
      'Chandigarh',
      'Chattisgarh',
      'Cherrapunji',
      'Chikhaldara',
      'Chikmagalur',
      'Chitkul',
      'Chittorgarh',
      'Chumathang',
      'Coimbatore',
      'Coonoor',
      'Coorg',
      'Corbett',
      'Dadra and Nagar Haveli',
      'Dalhousie',
      'Daman',
      'Daman and Diu',
      'Dandeli',
      'Daranghati',
      'Darjeeling',
      'Dehradun',
      'Delhi',
      'Devprayag',
      'Dhana',
      'Dhanaulti',
      'Dharamshala',
      'Dibrugarh',
      'Digha',
      'Dimapur',
      'Diu',
      'Dudhwa',
      'Dwarka',
      'Faridabad',
      'GHNP',
      'Gangotri',
      'Gangtok',
      'Gaya',
      'Ghaziabad',
      'Gir',
      'Goa',
      'Gokarna',
      'Gopalpur',
      'Gorakhpur',
      'Gujarat',
      'Gulmarg',
      'Guntakal',
      'Guptkashi',
      'Gurdaspur',
      'Gurgaon',
      'Guwahati',
      'Haflong',
      'Hampi',
      'Hanoi',
      'Haridwar',
      'Haryana',
      'Himachal Pradesh',
      'Hogenakkal',
      'Hoshiarpur',
      'Hunder',
      'Igatpuri',
      'Imphal',
      'Indore',
      'Itanagar',
      'Jabalpur',
      'Jagdalpur',
      'Jaisalmer',
      'Jakarta',
      'Jalandhar',
      'Jammu and Kashmir',
      'Jharkhand',
      'Jodhpur',
      'Jorhat',
      'Joshimath',
      'Junagadh',
      'Junnar',
      'Kalimpong',
      'Kamshet',
      'Kanatal',
      'Kanchipuram',
      'Kangra',
      'Kanyakumari',
      'Kargil',
      'Karjat',
      'Karnaprayag',
      'Karnataka',
      'Karsog',
      'Kasauli',
      'Kashid',
      'Kasol',
      'Katra',
      'Kaza',
      'Kaziranga',
      'Kedarnath',
      'Kerala',
      'Keylong',
      'Khajjiar',
      'Khajuraho',
      'Khandala',
      'Kharapathar',
      'Khimsar',
      'Kochi',
      'Kodaikanal',
      'Kohima',
      'Kolad',
      'Kollam',
      'Konark',
      'Kota',
      'Kovalam',
      'Kozhikode',
      'Kudremukha',
      'Kufri',
      'Kullu',
      'Kumarakom',
      'Kumbhalgarh',
      'Kurnool',
      'Kurseong',
      'Kurukshetra',
      'Kutch',
      'Lachung',
      'Lakshadweep',
      'Lamayuru',
      'Lambasingi',
      'Lansdowne',
      'Lavasa',
      'Leh',
      'Likir',
      'Lohajung',
      'Lonar',
      'Lucknow',
      'Ludhiana',
      'Madhya Pradesh',
      'Madurai',
      'Mahabaleshwar',
      'Mahabalipuram',
      'Maharashtra',
      'Male',
      'Malvan',
      'Manali',
      'Mandarmani',
      'Mandi',
      'Mandu',
      'Manipur',
      'Maredumilli',
      'Matheran',
      'Mathura',
      'Mawlynnong',
      'Mawsynram',
      'Mcleodganj',
      'Meghalaya',
      'Mizoram',
      'Mohali',
      'Mukteshwar',
      'Mumbai',
      'Munnar',
      'Mussoorie',
      'Mysore',
      'Nagaland',
      'Naggar',
      'Nagpur',
      'Nainital',
      'Nandaprayag',
      'Nandi',
      'Narkanda',
      'Nashik',
      'Naukuchiatal',
      'Neemrana',
      'Nelliyampathy',
      'Netarhat',
      'Noida',
      'Nongstoin',
      'Odisha',
      'Orchha',
      'Osian',
      'Pahalgam',
      'Palakkad',
      'Palampur',
      'Palanpur',
      'Panchgani',
      'Panna',
      'Pasighat',
      'Pathankot',
      'Patiala',
      'Patna',
      'Patnitop',
      'Pattaya',
      'Peermade',
      'Pelling',
      'Periyar',
      'Pithoragarh',
      'Pondicherry',
      'Pune',
      'Punjab',
      'Puri',
      'Pushkar',
      'Raipur',
      'Rajaji',
      'Rajasthan',
      'Rajgir',
      'Rajkot',
      'Rameswaram',
      'Ramtek',
      'Ranchi',
      'Ranikhet',
      'Ranthambore',
      'Ratnagiri',
      'Ravangla',
      'Rudraprayag',
      'Sagar',
      'Samui',
      'Sanchi',
      'Sangli',
      'Saputara',
      'Sariska',
      'Seoni',
      'Shillong',
      'Shimla',
      'Shirdi',
      'Shivanasamundram',
      'Shoghi',
      'Shravanabelagola',
      'Sikkim',
      'Silchar',
      'Siliguri',
      'Similipal',
      'Singalila',
      'Sirmaur',
      'Solan',
      'Sonamarg',
      'Sonipat',
      'Srinagar',
      'Sundarbans',
      'Surat',
      'Tamenglong',
      'Tamil Nadu',
      'Tanakpur',
      'Tarkarli',
      'Tatapani',
      'Tawang',
      'Telangana',
      'Tezpur',
      'Thanjavur',
      'Thenmala',
      'Thiruvananthapuram',
      'Tiruchirappalli',
      'Tirupati',
      'Tiruvannamalai',
      'Tripura',
      'Tura',
      'Udaipur',
      'Ujjain',
      'Unakoti',
      'Uttar Pradesh',
      'Uttarakhand',
      'Uttarkashi',
      'Vadodara',
      'Vagamon',
      'Varkala',
      'Visakhapatnam',
      'Vishnuprayag',
      'Vrindavan',
      'Wayanad',
      'West Bengal',
      'Yamunotri',
      'Yelagiri',
      'Yousmarg',
      'Zirakpur',
      'Ziro',
    ]

    return jsonify({"result": {"locations" : locations}, 'message': "Success", 'error': False})

@app.route("/restaurant/search", methods=['GET'])
def restaurant_search():
    args = request.args.to_dict()
    searched_value = ''
    # searched_key  = ''
    if args:
        searched_value = list(args.values())[0]
        # searched_key = list(args.keys())[0]
    cuisine = args.get("cuisine", None)
    category = args.get("category", None)
    args['collection'] = 'trending'

    cuisine_data = None

    if cuisine:
        cuisine_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant/cuisine"
        cuisine_data = requests.get(url=cuisine_api_url).json()['result']['cuisine']
        

    featured_restaurant_params = {
        "featured":True
        }
    # featured_restaurant_params = args
    # featured_restaurant_params.pop("collection", None)
    # featured_restaurant_params['featured'] = True


    


    restaurant_api_url = str(app.config["DOMAIN_URL"]) + "/api/v1/restaurant"   
    featured_restaurant_data = requests.get(url=restaurant_api_url, params=featured_restaurant_params).json()['result']['restaurants']
    trending_restaurant_data = requests.get(url=restaurant_api_url, params=args).json()['result']['restaurants']

    
    return render_template("restaurant/restaurant_search.html",searched_value=searched_value, trending_restaurant_data=trending_restaurant_data, args=args, featured_restaurant_data=featured_restaurant_data, cuisine_data=cuisine_data)


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
