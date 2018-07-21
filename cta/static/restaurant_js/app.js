var app = angular.module("restaurantApp",  ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }])


  .controller("restaurantController", ["$scope", "$http", function($scope, $http){

    
    $scope.searchQuery = function(){
      
      if($scope.searchValue.length == 3){
        $http.get("")
      }
      
    }



  }]);