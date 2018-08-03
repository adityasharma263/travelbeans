var app = angular.module("restaurantApp", ['angular.filter'])
  .config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }])

  // ____________________  Restaurant Home Page Controller ______________________-
  .controller("restaurantController", ["$scope", "$http", '$sce', function ($scope, $http, $sce) {


    var searchSuggestionDiv = document.getElementById("search-suggestion");
    var overlayBox = document.getElementById("overlay-box");
    $scope.searchSuggestion = {};

    overlayBox.onclick = function () {
      searchSuggestionDiv.style.display = "none";
      overlayBox.style.display = "none";
    }

    $scope.searchQuery = function (query) {

      console.log(query);



      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query })
          .then(function (response) {
            searchSuggestionDiv.style.display = "block";
            overlayBox.style.display = "block";
            console.log(response.data.result);
            $scope.searchSuggestion = response.data.result;
          }, function (err) {
            console.log(err);
          });
      } else {
        searchSuggestionDiv.style.display = "none";
        overlayBox.style.display = "none";
      }
    }

    $scope.highlight = function (text, search) {
      if (!search) {
        return $sce.trustAsHtml(text);
      }
      return $sce.trustAsHtml(text.replace(new RegExp(search, 'gi'), '<span class="highlightedText">$&</span>'));
    };



  }])
  // #######################  Search Page Controller ######################
  .controller("searchController", ["$scope", "$http", "$sce", function ($scope, $http, $sce) {

    var restaurantStructure = {};
    var filter = {};
    $scope.filter = {};

    $scope.serverSideRender = true;

    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisine = res.data.result.cuisine;
      }, function (err) {
        console.log(err);
      });

    $scope.getMenubyId = function (restaurantId, restaurantName) {
      console.log("akshay");
      $scope.restaurantName = restaurantName;

      $http.get("/api/v1/restaurant/dish?restaurant_id=" + restaurantId)
        .then(function (res) {
          $scope.restaurantDish = res.data.result.dish;
          console.log($scope.restaurantDish);
        },
        function (err) {
          console.log(err);
        })



    }


    $http.get("/api/v1/restaurant" + window.location.search)
      .then(function (res) {
        var allRestaurants = $scope.restaurants = res.data.result.restaurants;
        console.log("$scope.restaurants =", $scope.restaurants);
        $scope.min_price = Math.min.apply(Math, allRestaurants.map(function (item) { return item.price; }));
        $scope.max_price = Math.max.apply(Math, allRestaurants.map(function (item) { return item.price; }));
        $scope.price_filter = $scope.max_price;
        $scope.filter.price = $scope.max_price;

        console.log($scope.min_price, $scope.max_price, $scope.price_filter);
        for (i in allRestaurants) {
          restaurantStructure[allRestaurants[i].id] = allRestaurants[i];
        };

      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant/collection")
      .then(function (res) {
        $scope.collection = res.data.result.collection;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/dish")
      .then(function (res) {
        $scope.dish = res.data.result.dish;
      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant/association")
      .then(function (res) {
        $scope.association = res.data.result.association;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/amenity")
      .then(function (res) {
        $scope.amenities = res.data.result.amenities[0];
      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant/menu")
      .then(function (res) {
        $scope.menu = res.data.result.menu[0];
        delete $scope.menu.id;
        delete $scope.menu.restaurant;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/amenity")
      .then(function (res) {
        $scope.amenities = res.data.result.amenities[0];
        delete $scope.amenities.id;
        delete $scope.amenities.restaurant;
      }, function (err) {
        console.log(err);
      });



    $scope.getFilterRestaurant = function (filterName, filterValue) {


      filter[filterName] = filterValue;

      $http.get("/api/v1/restaurant", { params: filter })
        .then(function (res) {
          $scope.restaurants = res.data.result.restaurants;
          // $scope.serverSideRender = false;
          console.log($scope.restaurants);

        }, function (err) {
          console.log(err);
        });

    }

    $scope.amenityAndMenuFilter = function (filterType, filterValue) {

      var filter = {}
      filter[filterValue] = true;

      var filterTypeResponse = {
        menu: "menu",
        amenity: "amenities"
      }

      $http.get("/api/v1/restaurant/" + filterType, { params: filter })
        .then(function (res) {
          var amenitiesAndMenuFilterResponse = res.data.result[filterTypeResponse[filterType]];

          var restaurant = [];
          for (i in amenitiesAndMenuFilterResponse) {
            restaurant.push(restaurantStructure[amenitiesAndMenuFilterResponse[i].restaurant])
          }

          $scope.restaurants = restaurant;
          // $scope.serverSideRender = false;

        }, function (err) {
          console.log(err);
        });


    }



    var searchSuggestionDiv = document.getElementById("search-suggestion");
    var overlayBox = document.getElementById("overlay-box");
    $scope.searchSuggestion = {};

    overlayBox.onclick = function () {
      searchSuggestionDiv.style.display = "none";
      overlayBox.style.display = "none";
    }

    $scope.searchQuery = function (query) {

      console.log(query);



      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query })
          .then(function (response) {
            searchSuggestionDiv.style.display = "block";
            overlayBox.style.display = "block";
            console.log(response.data.result);
            $scope.searchSuggestion = response.data.result;
          }, function (err) {
            console.log(err);
          });
      } else {
        searchSuggestionDiv.style.display = "none";
        overlayBox.style.display = "none";
      }
    }

    $scope.highlight = function (text, search) {
      if (!search) {
        return $sce.trustAsHtml(text);
      }
      return $sce.trustAsHtml(text.replace(new RegExp(search, 'gi'), '<span class="highlightedText">$&</span>'));
    };

    $scope.priceFilter = function (maxPrice) {

      $http.get("/api/v1/restaurant?price_start=" + $scope.min_price + "&price_end=" + maxPrice)
        .then(function (res) {
          $scope.restaurants = res.data.result.restaurants;
          console.log($scope.restaurants);
          // $scope.serverSideRender = false;
        }, function (err) {
          console.log(err);
        })

    };
  }])

  // ============= Dashboard Controller =====================

  .controller("dashboarController", ["$scope", "$http", "$location", function ($scope, $http, $location) {

    $scope.restaurantData = {
      association: [{

        "collections": {

        },
        "cuisines": {

        }
      }]
    };

    $scope.image_types = {
      1: "Ambience",
      2: "Food",
      3: "Menu"
    }

    $scope.restaurantData.images = [
      {

        "image_type": null,
        "image_url": ""
      }
    ]


    $scope.restaurantData.dishes = [
      {
        "desc": "",
        "dish": "",
        "dish_type": null,
        "full_price": null,
        "half_price": null,
        "image": "",

      }
    ]

    $scope.addMoreDish = function () {

      var moreDishes = {
        "desc": "",
        "dish": "",
        "dish_type": null,
        "full_price": null,
        "half_price": null,
        "image": "",

      }

      $scope.restaurantData.dishes.push(moreDishes);
    };

    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisine = res.data.result.cuisine;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/collection")
      .then(function (res) {
        $scope.collection = res.data.result.collection;
      }, function (err) {
        console.log(err);
      });

    $scope.functionCalling = "Add";

    $scope.Add = function () {
      // $scope.restaurantData.dishes = $scope.dishes;
      console.log($scope.restaurantData);

      // return;
      $http.post("/api/v1/restaurant", $scope.restaurantData)
        .then(function (res) {
          // $scope.restaurants.push(res.data.result.restaurant);
          console.log(res);
          alert("Restaurant added!");
        }, function (err) {
          alert("Error =>\n" + err);

          console.log(err);
        })
    }
    $scope.Update = function () {
      $http.put("/api/v1/restaurant", {})




    }




    $scope.addMoreRestaurantImages = function () {
      var addImages = {

        "image_type": null,
        "image_url": ""
      }

      $scope.restaurantData.images.push(addImages);
    };


    function getQueryStringValue(key) {
      return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
    }

    $scope.addMoreAssociation = function () {
      var addAssociation = {
        "collections": {

        },
        "cuisines": {

        }
      }
      $scope.restaurantData.association.push(addAssociation);



    }





    $scope.amenities = {
      "alcohol": null,
      "beer": null,
      "brunch": null,
      "buffet": null,
      "city_view": null,
      "desserts_and_bakes": null,
      "full_bar_available": null,
      "gastro_pub": null,
      "group_meal": null,
      "home_delivery": true,
      "kid_friendly": true,
      "live_entertainment": null,
      "live_music": true,
      "live_sports_screening": null,
      "nightlife": null,
      "outdoor_seating": null,
      "parking": null,
      "private_dining_area_available": true,
      "seating": null,
      "serves_jain_food": null,
      "serves_non_veg": null,
      "smoking_area": null,
      "sunday_roast": null,
      "table_booking_recommended": null,
      "table_reservation_required": null,
      "takeaway": null,
      "valet_parking": null,
      "vegetarian_only": null,
      "wheelchair_accessible": null,
      "wifi": true
    }

    $scope.categories = [
      "bistro",
      "ethnic",
      "fine_dining ",
      "trattoria ",
      "teppanyaki_ya ",
      "osteria",
      "drive_in ",
      "drive_thru",
      "pizzeria ",
      "taverna",
      "fast_casual ",
      "pop_up",
      "Café",
      "iner",
      "ramen_ya ",
      "teahouse ",
      "fast_food",
      "buffet",
      "cafeteria ",
      "luncheonette ",
      "tapas_bar",
      "steakhouse ",
      "all_you_can_eat_restaurant ",
      "kosher",
      "dinner_in_the_Sky ",
      "dark_restaurant ",
      "a_la_carte ",
      "gastropub ",
      "brasserie ",
      "chiringuito",
      "food_truck",
      "churrascaria",
      "food_court",
      "restrobars",
      "street_stalls",
      "theme_resturants",
      "coffee_shop",
      "coffee_house",
      "cabaret",
      "tea_shop",
    ]

    $scope.menu = [
      "bars",
      "breakfast",
      "cafe",
      "diet",
      "dinner",
      "family",
      "lounge",
      "lunch",
      "luxury",
      "nightlife",
      "pocket_friendly",
      "street_stalls"
    ]

    $scope.locations = [
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








  }])
  .controller("collectionController", ["$scope", "$http", "$sce", function ($scope, $http, $sce) {

    var searchSuggestionDiv = document.getElementById("search-suggestion");
    var overlayBox = document.getElementById("overlay-box");
    $scope.searchSuggestion = {};

    overlayBox.onclick = function () {
      searchSuggestionDiv.style.display = "none";
      overlayBox.style.display = "none";
    }

    $scope.searchQuery = function (query) {

      console.log(query);



      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query })
          .then(function (response) {
            searchSuggestionDiv.style.display = "block";
            overlayBox.style.display = "block";
            console.log(response.data.result);
            $scope.searchSuggestion = response.data.result;
          }, function (err) {
            console.log(err);
          });
      } else {
        searchSuggestionDiv.style.display = "none";
        overlayBox.style.display = "none";
      }
    }

    $scope.highlight = function (text, search) {
      if (!search) {
        return $sce.trustAsHtml(text);
      }
      return $sce.trustAsHtml(text.replace(new RegExp(search, 'gi'), '<span class="highlightedText">$&</span>'));
    };

    $scope.getCollectionByLocation = function () {
      $http.get("/api/v1/restaurant?city=" + $scope.selectLocation)
        .then(function (res) {
          $scope.restaurants = res.data.result.restaurants;

          var collections = {};

          for (i in $scope.restaurants) {
            for (j in $scope.restaurants[i].association) {

              collections[$scope.restaurants[i].association[j].collections.collection] = $scope.restaurants[i].association[j].collections;
            }
          }

          $scope.collections = collections;

          console.log(collections);



        }, function (err) {
          console.log(err);
        })
    }

    $scope.locations = [
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




  }])

var Locations = [
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