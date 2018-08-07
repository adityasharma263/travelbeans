angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])

.constant('Constants', {
    
    Car_type: {
                1:     'Sedan',
                2:     'Mini SUV',
                3:     'Compact Car', 
                4:     'Sports Car',
                5:     'Convertable',
                6:     'Coupe',
                7:     'Mini Van',
                8:     'Hatchback', 
                9:     'Off rode vehical',
                10:    'Pickup Truck',
                11:    'Station Wagon', 
                12:    'Cross Over',
                13:    'Full Sized Car',
                14:    'Mid Sized Car',
                15:    'Utility Vehical', 
                16:    'Hybrid Car',
                17:    'Roadster',
                18:    'Touring Car',
                19:    'Super Car',
                20:    'Family Car', 
                21:    'Grand Tourer',
                22:    'Sub Compact',
                23:    'Electric Cars',
                24:    'Limousine',
                25:    'Commercial Vehical',
                26:    'Recreational Vehical', 
                27:    'Carvan',
                28:    'Economic Car',
                29:    'Hybrid Electric Vehical', 
                30:    'Executive Car',
                31:    'City Car',
                32:    'Compact SUV',
                33:    'Super Mini Car',
                34:    'Micro Car',
                35:    'Pony Car',
                36:    'Landaulet',
                37:    'Light Commercial', 
                38:    'Tempo Traveller',
                39:    'Kei Car',
                40:    'Vintage Car',
                41:    'TUV ',
                42:    'MUV',
                43:    'Certified Pre Owned',
                44:    'Small Cars',
                45:    'Luxury Cars',
                46:    'Compact SUV',
                47:    'Mid Sized SUV',
                48:    'Full Sized SUV',
                49:    'Passenger Van',
                50:    'Cargo Van',
                51:    'Luxury Gran Saloon',
                52:    'Muscle Car',
                53:    'Mini Bus',
                54:    'Pre Owned',
                55:    'MPV',
                56:    'Notchback',
                57:    'Pheaton',
                58:    'Hardtop',
                59:    'Spyder',
                60:    'Entry Level Luxury', 
                61:    'Mid Sized Luxury',
                62:    'Economy Car',
                63:    'Mid Sized Sedan'
    }
})


//----------------cab list controller-------------------

.controller('CabListController',["$scope", "$http","Constants", function($scope, $http, Constants, $filter) {

    $scope.car_types = Constants.Car_type;

    $scope.type = function(id) {
        return $scope.car_types[id]
      }

    
    $http.get("/api/v1/cab?cab_type=" + "1")
    .then(function (res) {
      $scope.cabs = res.data.result.cabs;
      console.log("$scope.cabs",$scope.cabs);
    }, function (err) {
      console.log(err);
    });

  }]) 



// ######## cab admin controller ############
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

//--------------------cab detail/booking controller-----------------------  

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