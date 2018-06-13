angular.module('comparetravel', ['720kb.datepicker'])
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{{');
  $interpolateProvider.endSymbol('}}');
}])

.controller('stayController', function($scope, $http, $filter) {


  var stayData = [];


  $scope.stays = {};

//   var count=1;
//   $scope.next =function(){
//        count +=1;  
//       //  console.log("in the next fn");
//        $scope.pageChanged();


//      }

     

//    $scope.previous =function(pageNum){
//        console.log("pageNum",pageNum);
//        count = pageNum;
//         $scope.pageChanged();
//      }
//      $scope.pageChanged =function(){
//       $http({
//               method: 'GET',
//               url: '/api/v1/events?page='+count
//             }).then(
     
//             // success callback
//             function(res){
//               console.log("pageChanged fn ");
//               console.log("res.data",res.data);
//                newEventData = res.data.result;
                
//                 $scope.events = newEventData;
//             //   for(i=0 ; i< newEventData.length;i++){
//             //     $scope.events.push(newEventData[i]);

//             //   }
              

//               // $scope.events.push(res.data.result);
//               console.log($scope.events);
//             },
//             // failed callback
//             function(req){
//             alert("Something wents wrong!!"); 
//             })        
//      }
     

  $http({
    method: 'GET',
    url: '/api/v1/stay'
  }).then(function successCallback(response) {
      stayData = response.data;
      $scope.stays = stayData.result;
      console.log("$scope.stays = ",$scope.stays);
      // $scope.sort='start_time';
      // numPages();
      // this callback will be called asynchronously
      // when the response is available
    }, function errorCallback(response) {
      // called asynchronously if an error occurs
      // or server returns response with an error status.
  });

  

//   var numPages = function () {
//     console.log("$scope.events.total_events",EventData.total_events);
//     console.log("$scope.events.page_size",EventData.page_size);

//     var fpages = (EventData.total_events / EventData.page_size);
//     console.log("fpages",fpages);
//     var ipages = parseInt(EventData.total_events / EventData.page_size);
//     console.log("ipages",ipages);
//     if((fpages-ipages)>0.5){
//         $scope.pages= ipages+1;
//     }
//     else{
//         $scope.pages = ipages;
//     }
//     console.log("$scope.pages",$scope.pages);
//     ;
//   }

//   $scope.getNumber = function(num) {
    
//     console.log("num",num);
//     return new Array(num);   
// }
// $( 'ul.nav li' ).on( 'click', function() {
//     $( this ).parent().find( 'li.active' ).removeClass( 'active' );
//     $( this ).addClass( 'active' );
// });

})