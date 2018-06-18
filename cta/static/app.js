angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}])

.controller('stayController',["$scope", "$http", function($scope, $http, $filter) {

  var hotelData = [];
  $scope.hotels = [];
  $scope.hotel = [];

  // var jsonToQueryString = function(json) {
  //   return '?' +
  //     Object.keys(json).map(function(key) {
  //       if(json[key]){
  //         return encodeURIComponent(key) + '=' +
  //           encodeURIComponent(json[key]);
  //       } else {
  //         return '';
  //       }
  //     }).join('&');
  // }

  // $scope.getHotel = function(hotel) {
    // if(hotel.from_date) {
    //   hotel.from_date = Date.parse(hotel.from_date)/1000;
    // }
    // if(hotel.to_date) {
    //   hotel.to_date = Date.parse(hotel.to_date)/1000;
    // }
    
   
    // console.log(hotel.city);

  $http({
    method: 'GET',
    url: '/api/v1/hotel', 
    params: $scope.hotel 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.hotels = response.data.result.hotel;
      console.log("$scope.hotels=====",$scope.hotels);
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  $http({
    method: 'GET',
    url: '/api/v1/price' 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.price = response.data.result.hotel;
      console.log("$scope.price=====",$scope.price);
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  $http({
    method: 'GET',
    url: '/api/v1/room',
    params: $scope.hotel
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.rooms = response.data.result.hotel;
      console.log("$scope.rooms=====",$scope.rooms);
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  $http({
    method: 'GET',
    url: '/api/v1/member',
    params: $scope.hotel 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.members = response.data.result.hotel;
      console.log("$scope.members=====",$scope.members);
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })
// }
}])