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


    var collection_desc = document.getElementsByClassName("collection-desc")

    if (collection_desc.length) {
      for (i in collection_desc) {
        console.log(collection_desc[i]);
        try {
          $clamp(collection_desc[i], { clamp: 2 });
        } catch (error) {
          console.log(error);
        }

      }


    }

    $scope.searchQuery = function (query, cityLocation) {

      console.log(query);



      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query, city: cityLocation })
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

    $scope.setValues = function (location) {
      $http.post("/restaurant/set-value", { location: location })
        .then(function (res) {
          console.log("set values success");
          window.location.reload();
        }, function (err) {
          console.log(err);
        })

    }


    $scope.getLocationByGPS = function () {

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {

          var lat = position.coords.latitude;
          var long = position.coords.longitude;
          var params = {
            latitude: lat,
            longitude: long
          }

          $http.get("/restaurant", { params: params })
            .then(function (res) {
              window.location.reload()
            }, function (err) {
              alert("Some error occur! Please Try different method.");

            })

        }, function (err) {
          alert("Some error occur! Please Try different method.");
        });
      } else {
        alert("Geolocation is not supported by this browser.");
      }



    }



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


    function getQueryStringValue(key) {
      return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
    }


    $scope.getCapitalize = function (stringValue) {
      var string = stringValue.replace("_", " ").split(" ");

      var capitalizeString = "";

      for (i in string) {
        capitalizeString += string[i].charAt(0).toUpperCase() + string[i].slice(1) + " ";
      }

      return capitalizeString;

    }

    $scope.reload = function () {
      window.location.reload();
    }

    var map;
    $scope.showMap = function (lat, long, restaurantName) {
      var latLong = { lat: lat, lng: long }


      map = new google.maps.Map(document.getElementById('show-restaurant-map'), {
        center: latLong,
        zoom: 15
      });

      var marker = new google.maps.Marker({
        position: latLong,
        map: map,
        title: restaurantName
      });

      $scope.restaurantName = restaurantName;

    }


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

    function capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }

    $scope.setValues = function (location) {
      $http.post("/restaurant/set-value", { location: location })
        .then(function (res) {
          console.log("set values success");
        }, function (err) {
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


        if (getQueryStringValue("name")) {
          console.log("in the name")
          $http.get("/api/v1/restaurant?city=" + $scope.userLocation)
            .then(function (res) {
              var mergeRestaurantList = res.data.result.restaurants;
              $scope.restaurants = $scope.restaurants.concat(mergeRestaurantList);
              console.log("merged");

            }, function (err) {
              console.log(err);
            });


        }

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

    // $http.get("/api/v1/restaurant/amenity")
    //   .then(function (res) {
    //     $scope.amenities = res.data.result.amenities[0];
    //   }, function (err) {
    //     console.log(err);
    //   });


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

    $scope.searchQuery = function (query, cityLocation) {

      console.log(query);
      console.log(cityLocation);


      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query, city: cityLocation })
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

    $scope.getImageForResults = function (imagesArray) {

      for (i in imagesArray) {
        if (imagesArray[i].image_type == 1 || imagesArray[i].image_type == 2) {
          return imagesArray[i].image_url;
        }
      }

      return "/Restaurant SVG Icons/placeholder.png";


    }

    $scope.categories_data = {
      "bistro": 1,
      "ethnic": 2,
      "fine_dining": 3,
      "trattoria": 4,
      "teppanyaki_ya": 5,
      "osteria": 6,
      "drive_in": 7,
      "drive_thru": 8,
      "pizzeria": 9,
      "taverna": 10,
      "fast_casual": 11,
      "pop_up": 12,
      "Café": 13,
      "iner": 14,
      "ramen_ya": 15,
      "teahouse": 16,
      "fast_food": 17,
      "buffet": 18,
      "cafeteria": 19,
      "luncheonette": 20,
      "tapas_bar": 21,
      "steakhouse": 22,
      "all_you_can_eat_restaurant": 23,
      "kosher": 24,
      "dinner_in_the_Sky": 25,
      "dark_restaurant": 26,
      "a_la_carte": 27,
      "gastropub": 28,
      "brasserie": 29,
      "chiringuito": 30,
      "food_truck": 31,
      "churrascaria": 32,
      "food_court": 33,
      "restrobars": 34,
      "street_stalls": 35,
      "theme_resturants": 36,
      "coffee_shop": 37,
      "coffee_house": 38,
      "cabaret": 39,
      "tea_shop": 40
    }


    $scope.categories_data_reverse = {
      "1": "bistro",
      "2": "ethnic",
      "3": "fine_dining",
      "4": "trattoria",
      "5": "teppanyaki_ya",
      "6": "osteria",
      "7": "drive_in",
      "8": "drive_thru",
      "9": "pizzeria",
      "10": "taverna",
      "11": "fast_casual",
      "12": "pop_up",
      "13": "Café",
      "14": "iner",
      "15": "ramen_ya",
      "16": "teahouse",
      "17": "fast_food",
      "18": "buffet",
      "19": "cafeteria",
      "20": "luncheonette",
      "21": "tapas_bar",
      "22": "steakhouse",
      "23": "all_you_can_eat_restaurant",
      "24": "kosher",
      "25": "dinner_in_the_Sky",
      "26": "dark_restaurant",
      "27": "a_la_carte",
      "28": "gastropub",
      "29": "brasserie",
      "30": "chiringuito",
      "31": "food_truck",
      "32": "churrascaria",
      "33": "food_court",
      "34": "restrobars",
      "35": "street_stalls",
      "36": "theme_resturants",
      "37": "coffee_shop",
      "38": "coffee_house",
      "39": "cabaret",
      "40": "tea_shop"
    }

  }])

  // ============= Dashboard Controller =====================

  .controller("dashboardController", ["$scope", "$http", "$location", function ($scope, $http, $location) {

    var put_restaurant_id = null;

    $scope.restaurantData = {
      association: [{

        "collections": {

        },
        "cuisines": {

        }
      }]
    };

    $scope.restaurantData.restaurent_chain = {};

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

    $http.get("/restaurant/location")
      .then(function (res) {
        $scope.locations = res.data.result.locations;
      })

    $scope.getRestaurantByLocation = function (location) {
      $http.get("/api/v1/restaurant", {params : {city: location}})
        .then(function (res) {
          $scope.restaurants = res.data.result.restaurants;
          
          $scope.serchFilter = location;
        }, function (err) {
          console.log(err);
        });
    }

    $scope.getRestaurantByLocation("Delhi");
    


    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisine = res.data.result.cuisine;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/chain")
      .then(function (res) {
        $scope.restaurent_chain = res.data.result.restaurent_chain;
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

      delete $scope.restaurantData.amenities
      delete $scope.restaurantData.association;
      delete $scope.restaurantData.dishes;
      delete $scope.restaurantData.id;
      delete $scope.restaurantData.images;
      delete $scope.restaurantData.menus;

      console.log(" $scope.restaurantData =", $scope.restaurantData);

      $http.put("/api/v1/restaurant/" + put_restaurant_id, $scope.restaurantData)
        .then(function (res) {
          console.log(res);

        }, function (err) {
          console.log(err);
        })




    }
    $scope.deleteRestaurant = function (restaurantId, index) {

      $http.delete("/api/v1/restaurant/" + restaurantId)
        .then(function (res) {
          $scope.restaurants.splice(index, 1);
          alert("Deleted!!");
        }, function (err) {
          alert("err " + err);
        })

    }




    $scope.addMoreRestaurantImages = function () {
      var addImages = {

        "image_type": null,
        "image_url": ""
      }

      $scope.restaurantData.images.push(addImages);
    };




    $scope.addMoreAssociation = function () {
      var addAssociation = {
        "collections": {

        },
        "cuisines": {

        }
      }
      $scope.restaurantData.association.push(addAssociation);



    }


    $scope.editRestaurant = function (restaurantData) {
      $scope.functionCalling = "Update";
      $scope.disable_amenity = true;
      $scope.disable_association = true;
      $scope.disable_dish = true;
      $scope.disable_menu = true;
      $scope.disable_images = true;


      restaurantData.phone = parseInt(restaurantData.phone);
      put_restaurant_id = restaurantData.id;

      for (i in restaurantData.association) {
        restaurantData.association[i].collections.collection_id = restaurantData.association[i].collections.id + ""
        restaurantData.association[i].cuisines.cuisine_id = restaurantData.association[i].cuisines.id + ""
        restaurantData.association[i].collections.collection = null;
        restaurantData.association[i].collections.image = null;
        restaurantData.association[i].collections.desc = null;
        restaurantData.association[i].collections.featured = null;
      }

      for (i in restaurantData.images) {
        restaurantData.images[i].image_type = restaurantData.images[i].image_type + ""
      }

      restaurantData.category = restaurantData.category + ""

      $scope.restaurantData = restaurantData;
      console.log(restaurantData);
      console.log($scope.restaurantData);




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

    $scope.categories_data = [
      {
        "bistro": 1
      },
      {
        "ethnic": 2
      },
      {
        "fine_dining": 3
      },
      {
        "trattoria": 4
      },
      {
        "teppanyaki_ya": 5
      },
      {
        "osteria": 6
      },
      {
        "drive_in": 7
      },
      {
        "drive_thru": 8
      },
      {
        "pizzeria": 9
      },
      {
        "taverna": 10
      },
      {
        "fast_casual": 11
      },
      {
        "pop_up": 12
      },
      {
        "Café": 13
      },
      {
        "iner": 14
      },
      {
        "ramen_ya": 15
      },
      {
        "teahouse": 16
      },
      {
        "fast_food": 17
      },
      {
        "buffet": 18
      },
      {
        "cafeteria": 19
      },
      {
        "luncheonette": 20
      },
      {
        "tapas_bar": 21
      },
      {
        "steakhouse": 22
      },
      {
        "all_you_can_eat_restaurant": 23
      },
      {
        "kosher": 24
      },
      {
        "dinner_in_the_Sky": 25
      },
      {
        "dark_restaurant": 26
      },
      {
        "a_la_carte": 27
      },
      {
        "gastropub": 28
      },
      {
        "brasserie": 29
      },
      {
        "chiringuito": 30
      },
      {
        "food_truck": 31
      },
      {
        "churrascaria": 32
      },
      {
        "food_court": 33
      },
      {
        "restrobars": 34
      },
      {
        "street_stalls": 35
      },
      {
        "theme_resturants": 36
      },
      {
        "coffee_shop": 37
      },
      {
        "coffee_house": 38
      },
      {
        "cabaret": 39
      },
      {
        "tea_shop": 40
      }
    ]

    $scope.categories = [
      "bistro",
      "ethnic",
      "fine_dining",
      "trattoria",
      "teppanyaki_ya",
      "osteria",
      "drive_in",
      "drive_thru",
      "pizzeria",
      "taverna",
      "fast_casual",
      "pop_up",
      "Café",
      "iner",
      "ramen_ya",
      "teahouse",
      "fast_food",
      "buffet",
      "cafeteria",
      "luncheonette",
      "tapas_bar",
      "steakhouse",
      "all_you_can_eat_restaurant",
      "kosher",
      "dinner_in_the_Sky",
      "dark_restaurant",
      "a_la_carte",
      "gastropub",
      "brasserie",
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

    var collection_desc = document.getElementsByClassName("collection-desc")

    if (collection_desc.length) {
      for (i in collection_desc) {
        console.log(collection_desc[i]);
        try {
          $clamp(collection_desc[i], { clamp: 2 });
        } catch (error) {
          console.log(error);
        }

      }
    }

    $scope.searchQuery = function (query, cityLocation) {

      console.log(query);



      if (query.length >= 2) {
        $http.post("/api/v1/restaurant/search", { search: query, city: cityLocation })
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
  .controller("dashboardAmenityController", ["$scope", "$http", function ($scope, $http) {
    $scope.disable_update = true;

    $http.get("/api/v1/restaurant/amenity")
      .then(function (res) {
        $scope.amenity = res.data.result.amenities;
        $scope.amenities = $scope.amenity[0]
        delete $scope.amenities.id;
        delete $scope.amenities.restaurant;


      }, function (err) {
        console.log(err);
      })

    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      })

    $scope.editAmenity = function (restaurantData) {
      console.log(restaurantData);
      $scope.disable_update = false;
      $scope.restaurantData = {}
      $scope.restaurantData.amenities = restaurantData.amenities;


    }

    $scope.update = function () {
      var amenityId = $scope.restaurantData.amenities.id
      delete $scope.restaurantData.amenities.id;
      delete $scope.restaurantData.amenities.restaurant;

      console.log($scope.restaurantData.amenities);

      $http.put("/api/v1/restaurant/amenity/" + amenityId, $scope.restaurantData.amenities)
        .then(function (res) {
          console.log(res);
          alert("Updated!!")
        }, function (err) {
          alert("err = " + err.data);
          console.log(err);
        })
    }


  }])
  .controller("dashboardDishController", ["$http", "$scope", "$q", function ($http, $scope, $q) {


    $scope.disable_update = true;
    $scope.functionCall = "update";
    var restaurant_id = null;

    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      })


    $scope.editDish = function (restaurantData) {
      console.log(restaurantData);
      $scope.disable_update = false;
      $scope.addDish = false;
      $scope.functionCall = "update";
      restaurant_id = restaurantData.id;

      $scope.restaurantData = restaurantData;
    }

    $scope.update = function () {
      var dishList = [];

      for (i in $scope.restaurantData.dishes) {
        var dishId = $scope.restaurantData.dishes[i].id
        delete $scope.restaurantData.dishes[i].id;
        delete $scope.restaurantData.dishes[i].restaurant;

        dishList.push($http.put("/api/v1/restaurant/dish/" + dishId, $scope.restaurantData.dishes[i]))
      }


      $q.all(dishList)
        .then(function (res) {
          alert("updated!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })


    }

    $scope.deleteDish = function (dishId, index) {
      $http.delete("/api/v1/restaurant/dish/" + dishId)
        .then(function (res) {

          $scope.restaurantData.dishes.splice(index, 1)

          alert("Deleted!!");

        },
        function (err) {
          console.log(err);
          alert("err " + err.status + " (" + err.statusText + ")");
        })
    }


    $scope.addMoreDish = function () {
      $scope.addDish = true;
      $scope.functionCall = "Add"
      $scope.restaurantData = {};

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
    }


    $scope.addMore = function () {
      var moreDishes = {
        "desc": "",
        "dish": "",
        "dish_type": null,
        "full_price": null,
        "half_price": null,
        "image": "",

      }

      $scope.restaurantData.dishes.push(moreDishes);
    }

    $scope.Add = function () {

      var dishList = [];

      for (i in $scope.restaurantData.dishes) {
        $scope.restaurantData.dishes[i].restaurant_id = restaurant_id;

        dishList.push($http.post("/api/v1/restaurant/dish", $scope.restaurantData.dishes[i]))
      }


      $q.all(dishList)
        .then(function (res) {
          alert("Added!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })
    }


  }])
  .controller("dashboardCollectionController", ["$scope", "$http", "$q", function ($scope, $http, $q) {

    $scope.disable_update = true;
    $scope.addCollection = false;
    $scope.functionCall = "update";
    var restaurant_id = null;

    $http.get("/api/v1/restaurant/collection")
      .then(function (res) {
        $scope.collections = res.data.result.collection;
      }, function (err) {
        console.log(err)
      })

    $scope.editCollection = function (collection) {

      $scope.disable_update = false;
      $scope.addCollection = false;
      $scope.functionCall = "update";
      $scope.collectionData = collection;
      console.log($scope.collectionData)

    }

    $scope.deleteCollection = function (collectionId, index) {

      $http.delete("/api/v1/restaurant/collection/" + collectionId)
        .then(function (res) {
          alert("deleted!!");
          $scope.collections.splice(index, 1);
        }, function (err) {
          alert("err " + err)
        })

    }

    $scope.addMoreCollection = function () {
      $scope.addCollection = true;
      $scope.disable_update = false;
      $scope.functionCall = "Add"
      $scope.restaurantData = {}
      $scope.restaurantData.collections = [
        {
          "collection": "",
          "image": "",
          "desc": "",
          "featured": null
        }
      ]
    }

    $scope.addMore = function () {

      var addCollection = {
        "collection": "",
        "image": "",
        "desc": "",
        "featured": null
      }
      $scope.restaurantData.collections.push(addCollection);
    }

    $scope.Add = function () {

      console.log($scope.restaurantData);
      var collectionList = [];

      for (i in $scope.restaurantData.collections) {

        collectionList.push($http.post("/api/v1/restaurant/collection", $scope.restaurantData.collections[i]))
      }


      $q.all(collectionList)
        .then(function (res) {
          alert("Added!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })





    }

    $scope.update = function () {
      var collectionId = $scope.collectionData.id;
      delete $scope.collectionData.id

      $http.put("/api/v1/restaurant/collection/" + collectionId, $scope.collectionData)
        .then(function (res) {
          alert("updated!!");

        }, function (err) {
          alert("err =" + err);
          console.log(err);
        })

    }


  }])
  .controller("dashboardCuisineController", ["$scope", "$http", "$q", function ($scope, $http, $q) {
    $scope.disable_update = true;
    $scope.functionCall = "update";


    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisines = res.data.result.cuisine;
      }, function (err) {
        console.log(err)

      })

    $scope.editCuisine = function (cuisine) {
      $scope.cuisineData = cuisine;
      $scope.disable_update = false;
      $scope.functionCall = "update";
      $scope.addCuisine = false;
    }

    $scope.addNewCuisine = function () {
      $scope.addCuisine = true;
      $scope.functionCall = "Add";
      $scope.disable_update = false;


      $scope.cuisineData = [
        {
          cuisine: null
        }
      ]


    }

    $scope.addMore = function () {
      var addCusine = {
        cuisine: null,
        desc: null,
        image: null,
        featured: false
      };

      $scope.cuisineData.push(addCusine);
    }

    $scope.Add = function () {
      console.log($scope.cuisineData);
      var cuisineList = [];

      for (i in $scope.cuisineData) {

        cuisineList.push($http.post("/api/v1/restaurant/cuisine", $scope.cuisineData[i]))
      }


      $q.all(cuisineList)
        .then(function (res) {
          alert("Added!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })

    }

    $scope.deleteCollection = function (cuisineId, index) {

      $http.delete("/api/v1/restaurant/cuisine/" + cuisineId)
        .then(function (res) {

          alert("delete");

        }, function (err) {
          console.log(err)
        })

    }



    $scope.update = function () {
      var cuisineId = $scope.cuisineData.id;
      delete $scope.cuisineData.id

      $http.put("/api/v1/restaurant/cuisine/" + cuisineId, $scope.cuisineData)
        .then(function (res) {
          alert("Updated!!")
        }, function (err) {
          console.log(err)
          alert("err = " + err)
        })
    }



  }])
  .controller("dashboardMenuController", ["$scope", "$http", function ($scope, $http) {

    $scope.disable_update = true;

    $http.get("/api/v1/restaurant/menu")
      .then(function (res) {
        $scope.menu = res.data.result.menu;
        $scope.menus = $scope.menu[0];
        delete $scope.menus.id;
        delete $scope.menus.restaurant;
      }, function (err) {
        console.log(err);
      })


    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      })

    $scope.editAmenity = function (restaurantData) {
      console.log(restaurantData);
      $scope.disable_update = false;
      $scope.restaurantData = {}
      $scope.restaurantData.menus = restaurantData.menus;


    }

    $scope.update = function () {
      var menuId = $scope.restaurantData.menus.id
      delete $scope.restaurantData.menus.id;
      delete $scope.restaurantData.menus.restaurant;

      console.log($scope.restaurantData.menus);

      $http.put("/api/v1/restaurant/menu/" + menuId, $scope.restaurantData.menus)
        .then(function (res) {
          console.log(res);
          alert("Updated!!")
        }, function (err) {
          alert("err = " + err.data);
          console.log(err);
        })
    }





  }])
  .controller("dashboardImagesController", ["$scope", "$http", "$q", function ($scope, $http, $q) {

    $scope.image_types = {
      1: "Ambience",
      2: "Food",
      3: "Menu"
    }
    $scope.disable_update = true;
    var restaurant_id = null;
    $scope.functionCall = "update";

    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      })

    $scope.editImages = function (restaurantData) {
      $scope.disable_update = false;
      restaurant_id = restaurantData.id;
      for (i in restaurantData.images) {
        restaurantData.images[i].image_type = restaurantData.images[i].image_type + ""
      }
      $scope.restaurantData = {}
      $scope.restaurantData.images = restaurantData.images;


    }

    $scope.update = function () {

      var imageList = [];

      for (i in $scope.restaurantData.images) {
        var imageId = $scope.restaurantData.images[i].id;
        delete $scope.restaurantData.images[i].id;
        delete $scope.restaurantData.images[i].restaurant;

        imageList.push($http.put("/api/v1/restaurant/image/" + imageId, $scope.restaurantData.images[i]))
      }


      $q.all(imageList)
        .then(function (res) {
          alert("updated!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })


    }

    $scope.deleteImage = function (imageId) {
      $http.delete("/api/v1/restaurant/image/" + imageId)
        .then(function (res) {

          alert("delete");

        }, function (err) {
          console.log(err)
        })
    }


    $scope.addMoreImages = function () {
      $scope.addImages = true;
      $scope.functionCall = "Add";

      $scope.restaurantData = {};
      $scope.restaurantData.images = [
        {

          "image_type": null,
          "image_url": ""
        }
      ]
    }

    $scope.addMoreRestaurantImages = function () {
      var addImages = {

        "image_type": null,
        "image_url": ""
      }

      $scope.restaurantData.images.push(addImages);
    };


    $scope.Add = function () {

      console.log($scope.restaurantData);
      var imageList = [];

      for (i in $scope.restaurantData.images) {

        $scope.restaurantData.images[i].restaurant_id = restaurant_id;
        imageList.push($http.post("/api/v1/restaurant/images", $scope.restaurantData.images[i]))
      }


      $q.all(imageList)
        .then(function (res) {
          alert("Added!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })

    }
  }])
  .controller("dashboardAssociationController", ["$scope", "$http", "$q", function ($scope, $http, $q) {

    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/collection")
      .then(function (res) {
        $scope.collections = res.data.result.collection;
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {

        $scope.cuisines = res.data.result.cuisine;
        console.log($scope.cuisines);
      }, function (err) {
        console.log(err);
      });





    $scope.editAssociation = function (restaurant) {
      console.log("akshay");
      var collections = restaurant.collections
      var cuisines = restaurant.cuisines
      $scope.restaurantId = restaurant.id;

      $http.get("/api/v1/restaurant/association?restaurant_id=" + restaurant.id)
        .then(function (res) {
          $scope.associations = res.data.result.association;
          console.log($scope.associations);
        }, function (err) {
          console.log(err);
        });

    }



    $scope.update = function () {

      var associationList = [];
      console.log($scope.associations);


      for (i in $scope.associations) {
        var associationId = $scope.associations[i].id;
        delete $scope.associations[i].id;

        $scope.associations[i].collection_id = $scope.associations[i].collection;
        delete $scope.associations[i].collection;

        $scope.associations[i].cuisine_id = $scope.associations[i].cuisine;
        delete $scope.associations[i].cuisine;

        $scope.associations[i].restaurant_id = $scope.associations[i].restaurant;
        delete $scope.associations[i].restaurant;

        if ($scope.associations[i].collection_id == "null") {
          $scope.associations[i].collection_id = null

        }
        if ($scope.associations[i].cuisine_id == "null") {
          $scope.associations[i].cuisine_id = null;
        }

        associationList.push($http.put("/api/v1/restaurant/association/" + associationId, $scope.associations[i]))
      }


      $q.all(associationList)
        .then(function (res) {
          alert("updated!!");
        }, function (err) {
          alert("err =" + err)
          console.log(err);
        })



    }

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




// var collection_desc = document.getElementById("collection-desc")

// $clamp(collection_desc, {clamp: 2});