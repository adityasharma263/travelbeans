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

    $http.get("/api/v1/restaurant/cuisine")
      .then(function (res) {
        $scope.cuisine = res.data.result.cuisine;
        console.log($scope.cuisine);
      }, function (err) {
        console.log(err);
      });


      $http.get("/api/v1/restaurant")
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
        console.log("$scope.resturants =",$scope.restaurants);
      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant/collection")
      .then(function (res) {
        $scope.collection = res.data.result.collection;
        console.log($scope.collection);
      }, function (err) {
        console.log(err);
      });

    $http.get("/api/v1/restaurant/dish")
      .then(function (res) {
        $scope.dish = res.data.result.dish;
        console.log($scope.dish);
      }, function (err) {
        console.log(err);
      });


    $http.get("/api/v1/restaurant/association")
      .then(function (res) {
        $scope.association = res.data.result.association;
        console.log($scope.association);
      }, function (err) {
        console.log(err);
      });


    // $http.get("/api/v1/restaurant/tag")
    //   .then(function (res) {
    //     $scope.tag = res.data.result.tag;
    //     console.log($scope.tag);
    //   }, function (err) {
    //     console.log(err);
    //   });

    $http.get("/api/v1/restaurant/amenity")
      .then(function (res) {
        $scope.amenities = res.data.result.amenities;
        console.log($scope.amenities);
      }, function (err) {
        console.log(err);
      });



    $scope.getFilterRestaurant = function(filterName, filterValue){

      var filter = {

      }
      filter[filterName] = filterValue;
      $http.get("/api/v1/restaurant", {params:filter})
      .then(function (res) {
        $scope.restaurants = res.data.result.restaurants;
      }, function (err) {
        console.log(err);
      });

    }

  }])