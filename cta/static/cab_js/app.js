
angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])

.controller('adminCabController',["$scope", "$http", function($scope, $http, $filter) {
    $scope.cab = {}; // main cab model
    $scope.cabImg = []; //for all images array
    $scope.images={}; //for one image

   
    $scope.addImg=function(){
        $scope.cabImg.push($scope.images);
        $scope.images={};
        createToast("'Image Added!!'","green");
    }

    $scope.createCab = function() {
        $scope.cabImg.push($scope.images);
        $scope.cab.images=$scope.cabImg;
        console.log("$scope.cab",$scope.cab);
    }

    var createToast=function(msg, color){
        var x= document.getElementById("snackbar");
        x.innerHTML=msg;
        x.style.backgroundColor=color;
        x.className = "show";
        setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
      }


  }]) 

  .controller('detailController',["$scope", "$http", function($scope, $http, $filter) {
    $scope.cab= {}; // main cab model
    console.log("js file");
    $http({
        method: 'GET',
        url: '/api/v1/cab' 
      }).then(function successCallback(response) {
          
          $scope.cab= response.data.result.cabs;
          console.log("cab data",$scope.cab);
          // this callback will be called asynchronously
          // when the response is available
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
      })
   


  }]) 