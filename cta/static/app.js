angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])



.controller('stayController',["$scope", "$http", "$location" ,function($scope, $http, $filter, $location) {


  $scope.hotelid = {};// hotel object on the basis of id
  $scope.hotel = {};
  $scope.myVar = false;
  var searchKey = '';
  $scope.clearCoor = function () {
    document.getElementById("demo").style.display = "none";
}
  
 // $location.search=

   $scope.result = function(data,status){
    $scope.hotel.search = data;
    searchKey = status;
    console.log("$scope.hotel.search",$scope.hotel.search);
    console.log("$status",status);

   }

   $scope.show = function() {
    console.log("........");
    if($scope.myVar==false){
      $scope.myVar = true;
    }
    else{
      $scope.myVar = false;
    }
  }
 
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
    console.log("status",searchKey);
    $scope.location=document.location.href;
    console.log("$scope.location",$scope.location);
    window.open($scope.location + "/list?" +searchKey+ "=" + $scope.hotel.search);
    console.log("$scope.hotel.city",$scope.hotel.city)     
  } 

  $scope.search = function()  {
    $scope.hotel.search = $scope.hotel.search.toLowerCase();
    console.log("$scope.hotel",$scope.hotel);
  $http({
    method: 'POST',
    url: '/hotel/search',
    data: $scope.hotel

  }).then(function successCallback(response){
  console.log("response",response.data.result);
      $scope.cities = response.data.result.cities;
      $scope.names = response.data.result.names;
      console.log("ye h",$scope.cities,response.data.result.names);

  })

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

.controller('staylistController',["$scope", "$http", function($scope, $http) {

  $scope.room = {};
  $scope.cityid = {};
  $scope.id = [];
  $scope.hotel = {};
  $scope.limit= 10;
  $scope.lim= 5;
  $scope.myVar= false;
  $scope.roomPrice={};
  $scope.roomobj={};
  $scope.hotelobj={};
  $scope.deals=[];
  $scope.imagesData={};
  // $scope.min= 0;
  // $scope.max= 0;
  // $scope.max_price= 0;

   // Get the modal
  //  var mymodal= ;
  //  console.log("modal",mymodal);
   // Get the image and insert it inside the modal - use its "alt" text as a caption
  //  var img = document.getElementById('myImg');
  //  var modalImg = document.getElementById("img01");
   var captionText = document.getElementById("caption");
   
  // $scope.myimg = function(){
  //   document.getElementById('myModal').style.display = "block";
  //   document.getElementById("img01").src = document.getElementById('myImg').src;
  //   // captionText.innerHTML = this.alt;
  //  }
   
   // Get the <span> element that closes the modal
   var span = document.getElementsByClassName("close")[0];
   
   // When the user clicks on <span> (x), close the modal
  //  span.onclick = function() { 
  //      modal.style.display = "none";
  //  }

  //for image pop up
  $scope.openGallery= function(data){
    $scope.imagesData=data;
    console.log("$scope.images",$scope.imagesData);
  }

  //for map pop up

  $scope.openMap= function(data){
    $scope.mapData=data;
    console.log("$scope.mapData",$scope.mapData);
    console.log("$scope.mapData.latitude",$scope.mapData.latitude);
    $scope.myMap();
  }
  $scope.myMap = function () {
    var mapOptions = {
        center: new google.maps.LatLng($scope.mapData.latitude, $scope.mapData.longitude),
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.HYBRID
    }
  console.log("mapOptions",mapOptions);  
var map = new google.maps.Map(document.getElementById("map"), mapOptions);
console.log("map",map);
}

//slide images

  var showDivs=function(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");
    
    var dots = document.getElementsByClassName("demo");

    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].style.opacity = 0.5;
      dots[i].getElementsByClassName("img")[0].style.opacity = 0.5;
      dots[i].className = dots[i].className.replace(" w3-opacity-off", "");
      dots[i].className = dots[i].className.replace(".image-carousel.style1 .slides", ".image-carousel.style1 .slidesactive");


    }
    dots[slideIndex-1].getElementsByClassName("img")[0].style.opacity = 1;
    dots[slideIndex-1].style.opacity = 1;
    
    x[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += "w3-opacity-off";
  }
  var slideIndex = 1;
  
  var plusDivs=function(n) {
      showDivs(slideIndex += n);
  }
  
  $scope.currentDiv=function(n) {
      showDivs(slideIndex = n);
  }

  //++++++++++++++++++++++++++++
  var i=0;
if(window.screen.availWidth >=440){
  console.log(window.screen.availWidth);
  $( ".flex-next" ).click(function() {
    if (($( ".demo" ).css( "transform","translate3d(0px, 0px, 0px)")) && ($scope.imagesData.images.length >= 10) && (i==0)){
  
      $(".demo").css("transform","translate3d(-791px, 0px, 0px)");
      i++;
      return i;
    } 
  
    if (($( ".demo" ).css( "transform","translate3d(-791px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==1)){
  
      $(".demo").css("transform","translate3d(-1582px, 0px, 0px)");
      i++;
      return i;
    } 
    else {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
      i=0;
      return i;
    }
  });
  
  $( ".flex-prev" ).click(function() {
  
    if ($( ".demo" ).css( "transform","translate3d(-1582px, 0px, 0px)") && (i==2)){
      $(".demo").css("transform","translate3d(-791px, 0px, 0px)");
      i--;
      return i;
    } 
  
    if ($( ".demo" ).css( "transform","translate3d(-791px, 0px, 0px)") && (i==1)){
      $(".demo").css("transform","translate3d(0px, 0px, 0px)");
      i--;
      return i;
    } 
    else {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
    }
  });
}
if(window.screen.availWidth <=440){
  console.log(window.screen.availWidth);

  $( ".flex-next" ).click(function() {
    if (($( ".demo" ).css( "transform","translate3d(0px, 0px, 0px)")) && ($scope.imagesData.images.length >= 10) && (i==0)){
  
      $(".demo").css("transform","translate3d(-240px, 0px, 0px)");
      i++;
      return i;
    } 
  
    if (($( ".demo" ).css( "transform","translate3d(-240px, 0px, 0px)")) && ($scope.imagesData.images.length >= 10) && (i==1)){
  
      $(".demo").css("transform","translate3d(-480px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-480px, 0px, 0px)")) && ($scope.imagesData.images.length >= 10) && (i==2)){
  
      $(".demo").css("transform","translate3d(-760px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-760px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==3)){
  
      $(".demo").css("transform","translate3d(-1000px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-1000px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==4)){
  
      $(".demo").css("transform","translate3d(-1240px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-1240px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==5)){
  
      $(".demo").css("transform","translate3d(-1480px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-1480px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==6)){
  
      $(".demo").css("transform","translate3d(-1760px, 0px, 0px)");
      i++;
      return i;
    } 
    if (($( ".demo" ).css( "transform","translate3d(-1760px, 0px, 0px)")) && ($scope.imagesData.images.length >= 20) && (i==7)){
  
      $(".demo").css("transform","translate3d(-2000px, 0px, 0px)");
      i++;
      return i;
    } 
    else {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
      i=0;
      return i;
    }
  });
  
  $( ".flex-prev" ).click(function() {
  
    if ($( ".demo" ).css( "transform","translate3d(-2000px, 0px, 0px)") && (i==7)){
      $(".demo").css("transform","translate3d(-1760px, 0px, 0px)");
      i--;
      return i;
    } 
  
    if ($( ".demo" ).css( "transform","translate3d(-1760px, 0px, 0px)") && (i==6)){
      $(".demo").css("transform","translate3d(-1480px, 0px, 0px)");
      i--;
      return i;
    } 
    if ($( ".demo" ).css( "transform","translate3d(-1480px, 0px, 0px)") && (i==5)){
      $(".demo").css("transform","translate3d(-1240px, 0px, 0px)");
      i--;
      return i;
    } 
    if ($( ".demo" ).css( "transform","translate3d(-1240px, 0px, 0px)") && (i==4)){
      $(".demo").css("transform","translate3d(-1000px, 0px, 0px)");
      i--;
      return i;
    } 
    if ($( ".demo" ).css( "transform","translate3d(-1000px, 0px, 0px)") && (i==3)){
      $(".demo").css("transform","translate3d(-760px, 0px, 0px)");
      i--;
      return i;
    } 
    if ($( ".demo" ).css( "transform","translate3d(-760px, 0px, 0px)") && (i==2)){
      $(".demo").css("transform","translate3d(-480px, 0px, 0px)");
      i--;
      return i;
    } 
    if ($( ".demo" ).css( "transform","translate3d(-480px, 0px, 0px)") && (i==1)){
      $(".demo").css("transform","translate3d(-240px, 0px, 0px)");
      i--;
      return i;
    } 
    else {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
    }
  });
}

//+++++++++++
  // loadMore function

  $scope.loadMore = function() {
    $scope.limit =   $scope.limit + 10;
  }

  $scope.loadmoredeals = function() {
    $scope.lim =   $scope.lim + 5;
  }


//for detail page
  $scope.showDetail=function(roomid){
    window.open('/hotel/detail?id='+roomid,'_self');
    
  }

//for more deals tab  
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
      var str = document.location.search;
      var key = str.split("?");
      var key1 = key[1].split("=");
      console.log("key1",key1);
      $scope.hotelData = response.data.result.hotel;
      console.log("$scope.hotelData",$scope.hotelData);
      if(key1[0]=="name"){
          $scope.city = $scope.hotelData[0].city;
          $http({
            method: 'GET',
            url: '/api/v1/hotel?city=' + $scope.city
          }).then(function successCallback(response) {
        
              $scope.newhotels = response.data.result.hotel;
              console.log("$scope.newhotels",$scope.newhotels);
              for(var j=0;j<$scope.newhotels.length;j++){
                $scope.hotelData.push($scope.newhotels[j]);
              }
              console.log("new",$scope.hotelData);
            }, function errorCallback(response) {
              // called asynchronously if an error occurs
              // or server returns response with an error status.
          })
          
        }
      for(var j=0;j<$scope.hotelData.length;j++){
        $scope.cityid[$scope.hotelData[j].id]= $scope.hotelData[j];
      }
      console.log("$scope.cityid",$scope.cityid);
      loadRoom();
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

var loadRoom=function(){
  $http({
    method: 'GET',
    url: '/api/v1/room'
  }).then(function successCallback(response) {

      $scope.roomdata = response.data.result.rooms;
      console.log("roomdata",$scope.roomdata);
      for(var j=0;j<$scope.roomdata.length;j++){
        $scope.roomPrice[$scope.roomdata[j].id]= $scope.roomdata[j];
      }
      loadDeals();

    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })
}
  
loadDeals=function(){
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
      loadPrice();
      }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })
}
 var loadPrice=function(){
  $scope.hotelData=[];
  $scope.deals=[];
  $http({
    method: 'GET',
    url: '/api/v1/deal?price_start=' + $scope.min + '&price_end=' + $scope.max
  }).then(function successCallback(response) {
      $scope.deals = response.data.result.deal;
      console.log("$scope.deals",$scope.deals);
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

  
 
  
  $scope.getHotelPrice = function(){
    console.log("$scope.hotel.end_price",$scope.hotel.end_price);
    $scope.hotelData=[];
    $scope.deals=[];
    $http({
      method: 'GET',
      url: '/api/v1/deal?price_start=' + $scope.min + '&price_end=' + $scope.hotel.end_price
    }).then(function successCallback(response) {
        $scope.deals = response.data.result.deal;
        console.log("$scope.deals",$scope.deals);
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

  $scope.checkErr = function(){
    $scope.errMessage = '';
    $scope.curDate = new Date();

    var check_in = $scope.hotel.check_in;
    console.log("check in",check_in);
    if($scope.hotel.check_in == undefined){
       $scope.hotel.check_in = check_in;
    }
    
    if(new Date($scope.hotel.check_in) > new Date($scope.hotel.check_out)){
      $scope.errMessage = 'End Date should be greater than start date';
      return false;
    }
    if(new Date($scope.hotel.check_in) < $scope.curDate){
       $scope.errMessage = 'Start date should not be before today.';
       return false;
    }

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

  $scope.getHotelRating = function(){
    console.log("$$scope.hotel.rating",$scope.hotel.rating);
    $scope.hotelData=[];
    $scope.deals=[];

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

  $scope.getHotelStar = function(){
    console.log("$$scope.hotel.star",$scope.hotel.star);
    $scope.hotelData=[];
    $scope.deals=[];

    $http({
      method: 'GET',
      url: '/api/v1/hotel' + document.location.search + '&star=' + $scope.hotel.star
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


}])  

.controller('adminController',["$scope", "$http", function($scope, $http, $filter) {
  $scope.hotel = {}; // main hotel model
  $scope.hotelImg = []; //for all images array
  $scope.images={}; //for one image
  $scope.deals={}; //for deals
  $scope.hotelDeals = []; // for all deals array
  $scope.room={}; //for one room
  $scope.hotelRooms=[]; // for all room array
  $scope.showHotelDetail=false;
  $scope.showRoomDetail=false;
  $scope.roomDetail=false;
  $scope.hotelDetail=true;
  $scope.updateRoomDetail=false;
  $scope.addRoomDetail=false;
  $scope.UpdateImages={}; //image data for update
  $scope.hotelData={}; // hotel data for update 
  $scope.amenitiesData={}; // hotel amenities for update

  $scope.showCreate=function(){
    $scope.hotelDetail=true;
    $scope.showHotelDetail=false;
  }
  $scope.showUpdate=function(){
    $scope.showHotelDetail=true;
    $scope.hotelDetail=false;
    $scope.showRoomDetail=false;
  }
  
  $scope.editRoomsData=function(data){
    $scope.rooms=data;
    $scope.facilities=data.facilities;
    $scope.member=data.member;
    $scope.roomDeals=data.deals;
    $scope.updateRoomDetail=true;
    $scope.showRoomDetail=false;

  }
  $scope.gotoHotelDetail=function(){
    $scope.updateRoomDetail=false;
    $scope.showRoomDetail=true;
    $scope.addRoomDetail=false;
  }
  $scope.editDealData=function(data){
    $scope.deal=data;
  }
  $scope.editHotel=function(data){
    $scope.hotels=data;
    $scope.hotelAmenities=data.amenities;
    $scope.hotelImages=data.images;
    $scope.hotelRooms=data.rooms;
    $scope.showRoomDetail=true;
    $scope.showHotelDetail=false;
    // $scope.Rooms=data;


  }
  $scope.editAmenities=function(){
   console.log('scope.hotels',$scope.hotelAmenities); 
  }
  $scope.editImg=function(data,index){
    $scope.imageData=data;
    // $scope.imagedata=data.id;
    $scope.imgIndex=index;

  }
  $scope.updateImage=function(){
    
    $scope.hotelImages[$scope.imgIndex].image_url=$scope.imageData.image_url;
    $scope.imageData.hotel_id=$scope.hotels.id;
    sendPutCall('/api/v1/image/'+$scope.imageData.id, $scope.imageData);
    createToast("Image Updated!!!","green");
  }
  $scope.updateHotel=function(){
    $scope.hotelData=$scope.hotels;
    
    delete $scope.hotelData.images;
    delete $scope.hotelData.rooms;
    delete $scope.hotelData.amenities;
    sendPutCall('/api/v1/hotel/'+$scope.hotelData.id, $scope.hotelData);
    createToast("Hotel Detail Updated!!!","green");
  }
  $scope.updateAmenities=function(){
    $scope.hotelAmenities.hotel_id=$scope.hotels.id;
    sendPutCall('/api/v1/amenity/'+$scope.hotelAmenities.id, $scope.hotelAmenities);
    createToast("Hotel Amenities Updated!!!","green");
  
  }
  $scope.updateRoom=function(){
    $scope.rooms.hotel_id=$scope.hotels.id;
    delete $scope.rooms.member;
    delete $scope.rooms.check_in;
    delete $scope.rooms.check_out;
    delete $scope.rooms.facilities;
    delete $scope.rooms.deals;
    delete $scope.rooms.hotel;
    sendPutCall('/api/v1/room/'+$scope.rooms.id, $scope.rooms);
    createToast("Room Updated!!!","green");
  }
  $scope.updateFacilities=function(){
    $scope.facilities.room_id=$scope.rooms.id;
    delete $scope.facilities.room;
    sendPutCall('/api/v1/facility/'+$scope.facilities.id, $scope.facilities);
    createToast("Facilities Updated!!!","green");
  }
  $scope.updateMembers=function(){
    $scope.member.room_id=$scope.rooms.id;
    delete $scope.member.room;
    sendPutCall('/api/v1/member/'+$scope.member.id, $scope.member);
    createToast("Members Updated!!!","green");
  }
  $scope.updateDeal=function(){

    $scope.deal.room_id=$scope.rooms.id;
    delete $scope.deal.room;
    delete $scope.deal.website;

    console.log('$scope.deal',$scope.deal);
    sendPutCall('/api/v1/deal/'+$scope.deal.id, $scope.deal);
    createToast("Deal Updated!!!","green");
    
  }
  $scope.addRoom=function(){

    $scope.room.hotel_id = $scope.hotels.id;
    
    $scope.hotelDeals.push($scope.deals);
    $scope.room.deals=$scope.hotelDeals;
    // $scope.hotelRooms.push($scope.room);
    console.log("rooms array",$scope.room);
    sendPostCall('/api/v1/room', $scope.room)

    createToast("'Room Added!!'","green");
    // $scope.deals.hotel_url="";
    $scope.hotelDeals=[];

  }
  $scope.showAddRoom=function(){
    $scope.showRoomDetail=false;
    $scope.addRoomDetail=true;
  }


  $http({
    method: 'GET',
    url: '/api/v1/hotel' 
  }).then(function successCallback(response) {
      // hotelData = response.data.result;
      $scope.hotelsData = response.data.result.hotel;
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
  var sendPostHotel = function(url, data) {
    $scope.hotel.city = $scope.hotel.city.toLowerCase();
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
  var sendPutCall = function(url, data) {
    console.log(data);
    
    $http({
      method: 'PUT',
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
  $scope.hotelDetail=false;
  $scope.roomDetail=true;

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
  $scope.limit=10;
  $scope.deallimit=1;

  
  
  var showDivs=function(n) {
    var i;
    var x = document.getElementsByClassName("mySlides");

    // var tx = document.getElementsByClassName("slider");
    
    var dots = document.getElementsByClassName("demo");

    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length}
    
    for (i = 0; i < dots.length; i++) {
      dots[i].style.opacity = 0.5;
      dots[i].getElementsByClassName("img")[0].style.opacity = 0.5;
      dots[i].className = dots[i].className.replace(" w3-opacity-off", "");
      dots[i].className = dots[i].className.replace(".image-carousel.style1 .slides", ".image-carousel.style1 .slidesactive");


    }
    dots[slideIndex-1].getElementsByClassName("img")[0].style.opacity = 1;
    dots[slideIndex-1].style.opacity = 1;
    
    if(window.screen.availWidth >=440){

      var transform=-870*(slideIndex-1);
    }
    if(window.screen.availWidth <=440){
      var transform=-370*(slideIndex-1);
    
    }
    document.body.style.setProperty('--tx',transform+'px');
    $(".slider").css("transform","translate3d(var(--tx), 0px, 0px)");
    dots[slideIndex-1].className += "w3-opacity-off";
  }
  var slideIndex = 1;

  
  var plusDivs=function(n) {
      showDivs(slideIndex += n);
  }
  
  $scope.currentDiv=function(n) {
    showDivs(slideIndex = n);
  }


  
 

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
    window.open('/hotel/'+roomid,'_self');
    
  }
  $http({
    method: 'GET',
    url: '/api/v1/hotel'
  }).then(function successCallback(response) {
      $scope.hotelsData = response.data.result.hotel;
      for(var j=0;j<$scope.hotelsData.length;j++){
        
        $scope.hotels[$scope.hotelsData[j].id]= $scope.hotelsData[j];
      }
      getrooms();

    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  })

var getrooms=function(){
  $scope.roomData={};
  var search =location.pathname;
  var id = search.split("/");
  $http({
    method: 'GET',
    url: '/api/v1/room?id='+id[2]
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
      

    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  });
}



/************************ slider jquery section  ************************************** */
var i=1;
if(window.screen.availWidth >=440){
  console.log(window.screen.availWidth);
  $( ".flex-next" ).click(function() {
    var totalSlides=($scope.roomData.hotelData.images.length)/10;
    var onSlideImage = (slideIndex+1)%10

    if(onSlideImage==1){
      if (totalSlides>i){
        var transform=-800*i;
        document.body.style.setProperty('--txx',transform+'px');
        $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
        $scope.currentDiv((i*10)+1);

        i++;
        return i;
      } 
    }
    else if(totalSlides< i) {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
      $scope.currentDiv(1);
      i=1;
      return i;
    }
    else{
      slideIndex++;
      $scope.currentDiv(slideIndex);
      return slideIndex;
    }
    
  });
  
  $( ".flex-prev" ).click(function() {
    var backSlideImage = (slideIndex)%10
    if (backSlideImage==1){
      if(1<i){
        i--;
        var transform =-800*(i-1);
        document.body.style.setProperty('--txx',transform+'px');
        $(".demo").css("transform","translate3d(var(--txx), 0px, 0px)");
        $scope.currentDiv(i*10);
        return i;
      }
     
    }else{
      if(slideIndex>1){
        slideIndex--;
        $scope.currentDiv(slideIndex);
        return slideIndex;
      }
    }
  });

}

if(window.screen.availWidth <=440){

  $( ".flex-next" ).click(function() {
    console.log(window.screen.availWidth);
    var totalSlides=($scope.roomData.hotelData.images.length)/3;
    var onSlideImage = (slideIndex+1)%3

    if(onSlideImage==1){
      if (totalSlides>i){
        var transform=-240*i;
        document.body.style.setProperty('--stx',transform+'px');
        $(".demo").css("transform","translate3d(var(--stx), 0px, 0px)");
        $scope.currentDiv((i*3)+1);

        i++;
        return i;
      } 
    }
    else if(totalSlides< i) {
      $(".demo").css("transform","translate3d(0px, 0px, 0px)" );
      $scope.currentDiv(1);
      i=1;
      return i;
    }
    else{
      slideIndex++;
      $scope.currentDiv(slideIndex);
      return slideIndex;
    }
  });
  
  $( ".flex-prev" ).click(function() {

    var backSlideImage = (slideIndex)%3
    if (backSlideImage==1){
      if(1<i){
        i--;
        var transform =-240*(i-1);
        document.body.style.setProperty('--stx',transform+'px');
        $(".demo").css("transform","translate3d(var(--stx), 0px, 0px)");
        $scope.currentDiv(i*3);
        return i;
      }
     
    }else{
      if(slideIndex>1){
        slideIndex--;
        $scope.currentDiv(slideIndex);
        return slideIndex;
      }
    }
  });

}
/************************************************************************************************/



}])
