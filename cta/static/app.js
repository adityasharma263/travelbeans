angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}])

.controller('stayController',["$scope", "$http", function($scope, $http, $filter) {

  var hotelData = [];
  $scope.hotels = [];

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
}])