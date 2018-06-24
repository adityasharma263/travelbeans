angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])



.controller('stayController',["$scope", "$http", function($scope, $http, $filter) {


  $scope.hotelData = [];
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
      url: '/api/v1/hotel',
      params: {
        city: $scope.hotel.city
      }
    }).then(function successCallback(response) {
        // hotelData = response.data.result;
        $scope.hotelData = response.data.result.hotel;
        console.log("$scope.hotel.city",$scope.hotelData);
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

.controller('adminController',["$scope", "$http", function($scope, $http, $filter) {
  var i;
  $scope.hotel = {};
  $scope.hotelImg = []; //for all images in the hotel
  $scope.images={};//for one image
  $scope.deals={};
  $scope.hotelDeals = [];

  $http({
    method: 'GET',
    url: '/api/v1/hotel' 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.hotels = response.data.result.hotel;
      if($scope.hotels.length > 0){
          i = $scope.hotels.length;
      }
      else{
        i=0;
      }
      console.log("i===",i);
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  $http({
    method: 'GET',
    url: '/api/v1/website' 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.websites = response.data.result.website;
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  var sendPostCall = function(url, data) {
    console.log(data);
    
    $http({
      method: 'POST',
      url: url,
      data: data
    }).then(function (res) {
      createToast("'hotel successfully created!!!'","green");
      $scope.hotelDeals=[];
      $scope.deals={};
      $scope.images={};
      $scope.hotelImg=[];
      delete $scope.hotel.amenities;
      delete $scope.hotel.facilities;
      delete $scope.hotel.room_type;
      delete $scope.hotel.member;
      delete $scope.hotel.balcony;
      delete $scope.hotel.breakfast;
      },
      // failed callback
      function (req) {
        createToast("'Something went wrong!!!'","red");
      })
    
  }

  $scope.createHotel = function() {
    // e.preventDefault()
    
    i++;
    $scope.hotel.id = i;
    $scope.hotelImg.push($scope.images);
    $scope.hotel.images=$scope.hotelImg;
    $scope.hotelDeals.push($scope.deals);
    $scope.hotel.deals=$scope.hotelDeals;
    console.log("$scope.hotel",$scope.hotel);

    sendPostCall('/api/v1/hotel', $scope.hotel)
  }

  $scope.addInput = function () {
      console.log("new input");
      $scope.hotel.images.push({
          value: null
      });
  }

  $scope.removeInput = function (index) {
      $scope.hotel.images.splice(index, 1);
  }

  $scope.openRoom = function () {
    
    $(".js-pop-room").css("top", "50%");
    
  };
  $scope.addImg=function(){
    $scope.hotelImg.push($scope.images);
    delete $scope.images.image_url;
    createToast("'Image Added!!'","green");

  }
  $scope.addPrice=function(){
    $scope.hotelDeals.push($scope.deals);
    $scope.deals={};
    createToast("'price Added!!'","green");

  }
var createToast=function(msg, color){
  var x= document.getElementById("snackbar");
  x.innerHTML=msg;
  x.style.backgroundColor=color;
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
}])  

.controller('hotelController', function($scope, $http) {
  
    $http({
      method: 'GET',
      url: '/api/v1/hotel/'+(location.pathname).substr(7)
    }).then(function successCallback(response) {
        $scope.hotelData = response.data.result.hotel;
        // $scope.eventData.description= $scope.eventData.description.replace("\n", "<br>");
         
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
      
  })
