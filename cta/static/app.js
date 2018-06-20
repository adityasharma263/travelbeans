angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', '$locationProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  $locationProvider.html5Mode(true);
}])



.controller('stayController',["$scope", "$http", "$location", function($scope, $http, $location, $filter) {


  


  var hotelData = [];
  $scope.hotels = [];
  $scope.hotel = [];
  $scope.rooms = [];
  $scope.room = [];

  // $location.search=
  
  

  $scope.getHotel = function(city) {
  
    $scope.hotel.city = city;
    console.log("$scope.hotel.city",$scope.hotel.city)
    $http({
      method: 'GET',
      url: '/api/v1/hotel?city=' + $scope.hotel.city
    }).then(function successCallback(response) {
        // hotelData = response.data.result;
        $scope.hotels = response.data.result.hotel;
        console.log("$scope.hotel.city",$scope.hotels);
        // this.router.navigate(['/hotel-list'], { queryParams: { city: $scope.hotel.city} });
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    })
     
  } 

  $scope.getroom = function(check_in,check_out) {
    
      $scope.hotel.check_in = Date.parse(check_in)/1000;
      console.log(" $scope.hotel.check_in ", $scope.hotel.check_in );
      $scope.hotel.check_out = Date.parse(check_out)/1000;
      $http({
        method: 'GET',
        url: '/api/v1/hotel?check_in=' + $scope.hotel.check_in + '&check_out=' + $scope.hotel.check_out
      }).then(function successCallback(response) {
          $scope.hotels = response.data.result.hotel;
          // this.router.navigate(['/hotel-list'], { queryParams: { check_in: 1529379870} ,'check_out' : 1529379870});
          // this callback will be called asynchronously
          // when the response is available
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
      })
       
    } 

  $http({
    method: 'GET',
    url: '/api/v1/hotel' 
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


//  }
}])