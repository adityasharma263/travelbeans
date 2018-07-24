var app = angular.module("restaurantApp", ['angular.filter'])
  .config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }])


  .controller("restaurantController", ["$scope", "$http", function ($scope, $http) {


    $scope.searchQuery = function () {

      if ($scope.searchValue.length == 3) {
        $http.get("")
      }

    }



  }])
  .controller("searchController", ["$scope", "$http", function ($scope, $http) {

    var restaurantStructure = {}

    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisine = res.data.result.cuisine;
      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
        var allRestaurants = $scope.restaurants;
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


    $http.get("/api/v1/restaurant/tag")
      .then(function (res) {
        $scope.tag = res.data.result.tag[0];
        console.log("$scope.tag =",$scope.tag);
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

      var filter = {}
      filter[filterName] = filterValue;
      $http.get("/api/v1/restaurant", { params: filter })
        .then(function (res) {
          $scope.restaurants = res.data.result.restaurants;
        }, function (err) {
          console.log(err);
        });

    }

    $scope.amenityAndTagFilter = function (filterType, filterValue) {

      var filter = {}
      filter[filterValue] = true;

      var filterTypeResponse={
        tag : "tag",
        amenity : "amenities"
      }

      $http.get("/api/v1/restaurant/"+filterType, { params: filter })
        .then(function (res) {
          var amenitiesAndTagFilterResponse = res.data.result[filterTypeResponse[filterType]];
          
          var restaurant = [];
          for (i in amenitiesAndTagFilterResponse) {
            restaurant.push(restaurantStructure[amenitiesAndTagFilterResponse[i].restaurant])
          }

          $scope.restaurants = restaurant;

        }, function (err) {
          console.log(err);
        });


    }

  }])