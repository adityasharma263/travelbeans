angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])



.controller('stayController',["$scope", "$http", "$location" ,function($scope, $http, $filter, $location) {


  $scope.hotelid = {};// hotel object on the basis of id
  $scope.hotel = {};

 // $location.search=
  
  var jsonToQueryString = function(json) {
    return '?' +
      Object.keys(json).map(function(key) {
        if(json[key]){
          return encodeURIComponent(key) + '=' +
            encodeURIComponent(json[key]);
        } else {
          return '';
        }
      }).join('&');
  }

  $scope.getHotel = function() {
    // console.log("$location.path",$location.path);
    $scope.location=document.location.href;
    console.log("$scope.location",$scope.location);
    window.open($scope.location + "/list?city="+ $scope.hotel.city);
    console.log("$scope.hotel.city",$scope.hotel.city)     
  } 

       
    

  $http({
    method: 'GET',
    url: '/api/v1/hotel' 
  }).then(function successCallback(response) {
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

.controller('staylistController',["$scope", "$http", function($scope, $http, $filter) {

  $scope.room = {};
  $scope.cityid = {};
  $scope.id = [];
  $scope.hotel = {};
  $scope.limit= 10;
  
  // loadMore function
  $scope.loadMore = function() {
    $scope.limit =   $scope.limit + 10;
  }

  var closePopUp = function() {
    $(".popAlertBox").css("top", "-110%");
  }

  $scope.openModal = function() {
    $(".js-pop-deals").css("top", "50%");
  };

  $(".close-btn").click(closePopUp);

  $http({
    method: 'GET',
    url: '/api/v1/hotel'+document.location.search
  }).then(function successCallback(response) {
      $scope.hotelData = response.data.result.hotel;
      console.log("$scope.hotelData",$scope.hotelData);
      for(var j=0;j<$scope.hotelData.length;j++){
        $scope.cityid[$scope.hotelData[j].id]= $scope.hotelData[j];
      }
      console.log("$scope.cityid",$scope.cityid);

      // $scope.room.check_in = Date.parse($scope.room.check_in)/1000;
      // console.log(" $scope.room.check_in ", $scope.room.check_in );
      // $scope.room.check_out = Date.parse($scope.room.check_out)/1000;

      // $http({
      //   method: 'GET',
      //   url: '/api/v1/room?check_in=' + $scope.room.check_in + '&check_out=' + $scope.room.check_out
      // }).then(function successCallback(response) {
      //     $scope.rooms = response.data.result.hotel;
      //     console.log("$scope.rooms",$scope.rooms);
      //     for(var j=0;j<$scope.rooms.length;j++){
      //         $scope.id[j] = $scope.rooms[j].hotel_id;
      //     }
      //     console.log("id",$scope.id);
      //   }, function errorCallback(response) {
      //     // called asynchronously if an error occurs
      //     // or server returns response with an error status.
      // })

    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

  // $scope.getHotelRating = function(){
    
  //   console.log("$$scope.hotel.rating",$scope.hotel.rating);

  //   $http({
  //     method: 'GET',
  //     url: '/api/v1/hotel' + document.location.search + '&rating=' + $scope.hotel.rating
  //   }).then(function successCallback(response) {
  //       $scope.hotelData = response.data.result.hotel;
  //       console.log("$scope.hotelData",$scope.hotelData);
  //       // this callback will be called asynchronously
  //       // when the response is available
  //     }, function errorCallback(response) {
  //       // called asynchronously if an error occurs
  //       // or server returns response with an error status.
  //   })

  // }

  $scope.getHotelPrice = function(){
    
    console.log("$$scope.hotel.price",$scope.hotel.price);

    $http({
      method: 'GET',
      url: '/api/v1/deal?price=' + $scope.hotel.price
    }).then(function successCallback(response) {
        $scope.deals = response.data.result.deal;
        console.log("$scope.deals",$scope.deals);
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    })

  }

}])  

.controller('adminController',["$scope", "$http", function($scope, $http, $filter) {
  $scope.hotel = {}; // main hotel model
  $scope.hotelImg = []; //for all images array
  $scope.images={}; //for one image
  $scope.deals={}; //for deals
  $scope.hotelDeals = []; // for all deals array
  $scope.room={}; //for one room
  $scope.hotelRooms=[]; // for all room array

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
      console.log(res);
      return res;
      createToast("'hotel successfully created!!!'","green");

      },
      // failed callback
      function (req) {
        createToast("'Something went wrong!!!'","red");
      })
    
  }

  

  $scope.removeInput = function (index) {
      $scope.hotel.images.splice(index, 1);
  }

  $scope.openRoom = function () {
    
    $(".js-pop-room").css("top", "50%");
    
  };
  onload=function(){
    window.scrollBy(0, -900);

  }
  $scope.createRoom=function(){

    // $scope.room.hotel_id = j;
    
    $scope.hotelDeals.push($scope.deals);
    $scope.room.deals=$scope.hotelDeals;
    // $scope.hotelRooms.push($scope.room);
    console.log("rooms array",$scope.room);
  // sendPostCall('/api/v1/hotel', $scope.hotelRoom)

    createToast("'Room Added!!'","green");
    $scope.deals.hotel_url="";

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
$scope.createHotel = function() {
  // e.preventDefault()

  $scope.hotelImg.push($scope.images);
  $scope.hotel.images=$scope.hotelImg;

  console.log("$scope.hotel",$scope.hotel);

  // sendPostCall('/api/v1/hotel', $scope.hotel)
  // return $scope.j= res.data.result.hotel;
}
}])  






.controller('hotelController', function($scope, $http) {
  
    $http({
      method: 'GET',
      url: '/api/v1/hotel/'+(location.pathname).substr(7)
    }).then(function successCallback(response) {
        $scope.hotelData = response.data.result.hotel;
         
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
      
  })
