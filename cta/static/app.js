angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}])

.controller('stayController',["$scope", "$http", function($scope, $http, $filter) {

  var hotelData = [];
  $scope.hotels = [];
  $scope.hotel = [];
  $scope.rooms = [];
  $scope.room = [];



  

  $scope.getHotel = function(city) {
  
    $scope.hotel.city = city;
    console.log("$scope.hotel.city",$scope.hotel.city)
    $http({
      method: 'GET',
      url: '/api/v1/hotel?city=' + $scope.hotel.city
    }).then(function successCallback(response) {
        // hotelData = response.data.result;
        $scope.hotels = response.data.result.hotel;
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    })
    
   
  } 

  // $scope.getroom = function(check_in,check_out) {
    
  //     $scope.room.check_in = Date.parse(check_in)/1000;
  //     console.log(" $scope.room.check_in", $scope.room.check_in);
  //     $scope.room.check_out = Date.parse(check_out)/1000;
  
  //     $http({
  //       method: 'GET',
  //       url: '/api/v1/room?check_in=' + $scope.room.check_in + '&check_out=' + $scope.room.check_out
  //     }).then(function successCallback(response) {  
  //         // hotelData = response.data.result;
  //         $scope.rooms = response.data.result.hotel;
  //         for(var i=0;i<rooms.length;i++) 
  //           {

  //             $http({
  //               method: 'GET',
  //               url: '/api/v1/hotel?id=' + $scope.rooms[i].hotel
  //             }).then(function successCallback(response) {
  //                 // hotelData = response.data.result;
  //                 $scope.hotels = response.data.result.hotel;
  //                 // this callback will be called asynchronously
  //                 // when the response is available
  //               }, function errorCallback(response) {
  //                 // called asynchronously if an error occurs
  //                 // or server returns response with an error status.
  //             })
              
  //           }  

  //         // this callback will be called asynchronously
  //         // when the response is available
  //       }, function errorCallback(response) {
  //         // called asynchronously if an error occurs
  //         // or server returns response with an error status.
  //     })
      
     
  //   }

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
//  }
}])