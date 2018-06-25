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
  $scope.hotelid = {};

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
      for(var j=0;j<$scope.hotels.length;j++){
        $scope.hotelid[$scope.hotels[j].id]= $scope.hotels[j];
      }
      console.log("$scope.hotelid",$scope.hotelid);
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
  var i ,j;
  $scope.hotel = {}; // main hotel model
  $scope.hotelImg = []; //for all images array
  $scope.images={}; //for one image
  $scope.deals={}; //for deals
  $scope.hotelDeals = []; // for all deals array
  $scope.room={}; //for one room
  $scope.hotelRooms=[]; // for all room array

  $http({
    method: 'GET',
    url: '/api/v1/hotel' 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.hotels = response.data.result.hotel;
      if($scope.hotels.length > 0){
          console.log("in i",$scope.hotels);
          i = $scope.hotels.length;
          if(i > 0){
            console.log("in j",$scope.hotels)
            var z, k;
            z=i-1;
            k = $scope.hotels[z].rooms.length;
            n=k-1;
            j=$scope.hotels[z].rooms[n].id;
          }
          else{
            j=0;
          }
      }
      else{
        i=0;
        j=0;
      }
      
      console.log("i===",i);
      console.log("j==",j);
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

      },
      // failed callback
      function (req) {
        createToast("'Something went wrong!!!'","red");
      })
    
  }

  $scope.createHotel = function() {
    // e.preventDefault()
    
    i++;
    j++;
    $scope.room.id = j;
    $scope.hotel.id = i;
    $scope.hotelImg.push($scope.images);
    $scope.hotel.images=$scope.hotelImg;

    $scope.hotelDeals.push($scope.deals);
    $scope.room.deals=$scope.hotelDeals;

    $scope.hotelRooms.push($scope.room);
    $scope.hotel.rooms=$scope.hotelRooms;

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
  $scope.addRoom=function(){
    j++;
    $scope.room.id = j;
    $scope.hotelDeals.push($scope.deals);
    $scope.room.deals=$scope.hotelDeals;
    $scope.hotelRooms.push($scope.room);
    createToast("'Room Added!!'","green");
    $scope.room={};
    $scope.images={};
    $scope.hotelDeals=[];
    $scope.deals={};

  }
  $scope.addImg=function(){
    $scope.hotelImg.push($scope.images);
    $scope.images={};
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
