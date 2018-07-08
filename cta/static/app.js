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
  $scope.myVar= false;
  $scope.roomPrice={};
  $scope.roomobj={};
  $scope.hotelobj={};
  $scope.deals=[];
  $scope.min= 0;
  $scope.max= 0;
  
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

  $scope.show = function() {
    if($scope.myVar==false){
      $scope.myVar = true;
    }
    else{
      $scope.myVar = false;
    }
  }

  $http({
    method: 'GET',
    url: '/api/v1/hotel'+document.location.search
  }).then(function successCallback(response) {
      $scope.hotelData = response.data.result.hotel;
      console.log("$scope.hotelData",$scope.hotelData);
      console.log("...",$scope.hotelData[0].images[0].image_url);
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

  $scope.getHotelRating = function(){
    
    console.log("$$scope.hotel.rating",$scope.hotel.rating);

    $http({
      method: 'GET',
      url: '/api/v1/hotel' + document.location.search + '&rating=' + $scope.hotel.rating
    }).then(function successCallback(response) {
        $scope.hotelData = response.data.result.hotel;
        console.log("$scope.hotelData",$scope.hotelData);
        // this callback will be called asynchronously
        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    })

  }
  $http({
    method: 'GET',
    url: '/api/v1/room'
  }).then(function successCallback(response) {

      $scope.roomdata = response.data.result.rooms;
      console.log("roomdata",$scope.roomdata);
      for(var j=0;j<$scope.roomdata.length;j++){
        $scope.roomPrice[$scope.roomdata[j].id]= $scope.roomdata[j];
      }
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })
  $http({
    method: 'GET',
    url: '/api/v1/deal'
  }).then(function successCallback(response) {

      $scope.dealdata = response.data.result.deal;
      console.log(" $scope.dealdata", $scope.dealdata);
      $scope.min = Math.min.apply(Math,$scope.dealdata.map(function(item){return item.price;}));
      console.log("$scope.min",$scope.min);
      $scope.max= Math.max.apply(Math,$scope.dealdata.map(function(item){return item.price;}));
      console.log("$scope.max",$scope.max);
      }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })
  $scope.getHotelPrice = function(){
    console.log("......");

    $http({
      method: 'GET',
      url: '/api/v1/deal?price_start=' + $scope.hotel.start_price + '&price_end=' + $scope.hotel.end_price
    }).then(function successCallback(response) {
        $scope.deals = response.data.result.deal;
        for(var j=0; j<$scope.deals.length; j++){
          $scope.roomobj=$scope.roomPrice[$scope.deals[j].room];
          $scope.deals[j].roomdata=$scope.roomobj;
          $scope.hotelobj=$scope.cityid[$scope.deals[j].roomdata.hotel];
          $scope.deals[j].roomdata.hoteldata=$scope.hotelobj;

        }
        console.log("deals array",$scope.deals);
        // this callback will be called asynchronously

        // when the response is available
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    })
    
  }

  $scope.getHotelweek = function(){
    
    $scope.hotel.check_in = Date.parse($scope.hotel.check_in)/1000;
    $scope.hotel.check_out = Date.parse($scope.hotel.check_out)/1000;
    console.log("$scope.hotel.check_in",$scope.hotel.check_in);
    $http({
      method: 'GET',
      url: '/api/v1/deal?check_in=' + $scope.hotel.check_in + '&check_out=' + $scope.hotel.check_out
    }).then(function successCallback(response) {
        $scope.deals = response.data.result.deal;
        for(var j=0; j<$scope.deals.length; j++){
          $scope.roomobj=$scope.roomPrice[$scope.deals[j].room];
          $scope.deals[j].roomdata=$scope.roomobj;
          $scope.hotelobj=$scope.cityid[$scope.deals[j].roomdata.hotel];
          $scope.deals[j].roomdata.hoteldata=$scope.hotelobj;

        }
        console.log("deals array",$scope.deals);
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
  $scope.showRoom=false;

  $scope.hideRoom=function(){
    delete $scope.room.default_room_type;
    $scope.showRoom=false;
  }
  $scope.showDefaultRoom=function(){
    $scope.showRoom=true;
  }
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
  var sendPostHotel = function(url, data) {
    console.log(data);
    
    $http({
      method: 'POST',
      url: url,
      data: data
    }).then(function (res) {
      console.log(res);
      $scope.j= res.data.result.hotel.id;
      console.log("j",$scope.j);

      
      createToast("'hotel successfully created!!!'","green");

      },
      // failed callback
      function (req) {
        createToast("'Something went wrong!!!'","red");
        
        setTimeout(function(){ location.reload(); }, 1000);

      })
    
  }

  var sendPostCall = function(url, data) {
    console.log(data);
    
    $http({
      method: 'POST',
      url: url,
      data: data
    }).then(function (res) {
      console.log(res);
      
      // createToast("'hotel successfully created!!!'","green");

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

    $scope.room.hotel_id = $scope.j;
    
    $scope.hotelDeals.push($scope.deals);
    $scope.room.deals=$scope.hotelDeals;
    // $scope.hotelRooms.push($scope.room);
    console.log("rooms array",$scope.room);
    sendPostCall('/api/v1/room', $scope.room)

    createToast("'Room Added!!'","green");
    // $scope.deals.hotel_url="";
    $scope.hotelDeals=[];

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

  sendPostHotel('/api/v1/hotel', $scope.hotel)
}
}])  






.controller('hotelController',["$scope", "$http", function($scope, $http, $filter) {
  $scope.roomData={};
  $scope.hotels={};
  $scope.roomobj={};
  // $scope.firstRate = 0;
  // $scope.secondRate = 3;
  // $scope.readOnly = true;
  // $scope.onItemRating = function(rating){
  //   alert('On Rating: ' + rating);
  // };
  $scope.limit=10;
  $scope.deallimit=1;

  $scope.loadMoreRooms = function() {
    $scope.limit =   $scope.limit + 10;
  }
  $scope.loadMoreDeals = function() {
    $scope.deallimit =   $scope.deallimit + 1;
  }
  $scope.newLocation=function(){
    window.open('/hotel/list','_self');

  }
  $scope.showDetail=function(roomid){
    window.open('/hotel/detail?id='+roomid,'_self');
    
  }
  $http({
    method: 'GET',
    url: '/api/v1/hotel'
  }).then(function successCallback(response) {
      $scope.hotelsData = response.data.result.hotel;
      console.log("$scope.hotelsData",$scope.hotelsData);
      for(var j=0;j<$scope.hotelsData.length;j++){
        
        $scope.hotels[$scope.hotelsData[j].id]= $scope.hotelsData[j];
      }
      console.log("$scope.hotels",$scope.hotels);
      getrooms();

    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

var getrooms=function(){
  $http({
    method: 'GET',
    url: '/api/v1/room'+(location.search)
  }).then(function successCallback(response) {
      for(var i=0; i<response.data.result.rooms.length; i++){
        $scope.roomData= response.data.result.rooms[i];
      }
      
      $scope.hotelobj=$scope.hotels[$scope.roomData.hotel];
      $scope.roomData.hotelData=$scope.hotelobj;
      for(var j=0; j<$scope.roomData.hotelData.rooms.length; j++){
        for(var k=0; k<$scope.roomData.hotelData.rooms[j].deals.length; k++){
          $scope.roomData.hotelData.rooms[j].deals[k].dealsRoom=$scope.roomData.hotelData.rooms[j]
        }
      }
      console.log("roomData",$scope.roomData);
      

      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  });
}

      
}])
