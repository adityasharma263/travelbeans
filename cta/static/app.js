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
  $scope.images=[];//for one image
  $scope.deals=[];
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

  var sendPostCall = function(url, data) {
    console.log(data);
    
    $http({
      method: 'POST',
      url: url,
      data: data
    }).then(function (res) {
        console.log("res",res);
      },
      // failed callback
      function (req) {
        alert("Something went wrong!!");
      })
  }

  $scope.createHotel = function() {
    // e.preventDefault()
    i++;
    $scope.hotel.id = i;
    $scope.hotel.deals.hotel = i;
    $scope.hotel.facilities.hotel = i;
    $scope.hotel.amenities.hotel = i;
    $scope.hotel.member.hotel = i;
    $scope.hotel.images.hotel = i;
    console.log("$scope.hotel.id",$scope.hotel.id);
    console.log("$scope.hotel",$scope.hotel);
    
    if($scope.hotelImg.length || $scope.hotelDeals.length){
      $scope.hotelImg.push($scope.images.images_url);
      $scope.hotelDeals.push($scope.deals);
      $scope.hotel.deals=$scope.hotelDeals;
      $scope.hotel.images=$scope.hotelImg;

    }
    else{
      console.log("imagesurl",$scope.images.images_url);
      $scope.hotel.images=$scope.images.images_url;
      $scope.hotel.deals=$scope.deals;
    }

    console.log("$scope.hotel",$scope.hotel);

    // sendPostCall('/api/v1/hotel', $scope.hotel)
    delete $scope.hotelDeals;
    delete $scope.deals;
    
  }

  // $scope.hotel.images = [{
  //   value: null
  // }];

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
    console.log("before push",$scope.images.images_url);
    $scope.hotelImg.push($scope.images.images_url);
    delete $scope.images.images_url;
    console.log("after push",$scope.hotelImg);

  }

  $scope.addPrice=function(){
    console.log("before push",$scope.deals);
    $scope.hotelDeals.push($scope.deals);
    delete $scope.deals;
    console.log("after push",$scope.hotelDeals);

  }
  



}])  