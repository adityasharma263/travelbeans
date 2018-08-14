angular.module('comparetravel', ['angular.filter'])
.config(['$interpolateProvider', function($interpolateProvider ,$locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  // $locationProvider.html5Mode(true);
}])


.constant("Constants",{

   Car_types : {

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
                    20:    'Family Car ',
                    21:    'Grand Tourer',
                    22:    'Sub Compact ',
                    23:    'Electric Cars',
                    24:    'Limousine',
                    25:    'Commercial Vehical',
                    26:    'Recreational Vehical',
                    27:    'Carvan',
                    28:    'Economic Car',
                    29:    'Hybrid Electric Vehical ',
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
                    60:    'Entry Level Luxury ',
                    61:    'Mid Sized Luxury',
                    62:    'Economy Car',
                    63:    'Mid Sized Sedan'

   }

})

.constant("bank_type",{
    
       bank : {
               1: 'Allahabad Bank',
               2: 'Andhra Bank',
               3: 'Axis Bank',
               4: 'Bank of Bahrain and Kuwait',
               5: 'Bank of Baroda - Corporate Banking',
               6: 'Bank of Baroda - Retail Banking',
               7: 'Bank of India',
               8: 'Bank of Maharashtra',
               9: 'Canara Bank',
               10:'Central Bank of India',
               11:'City Union Bank',
               12:'Corporation Bank',
               13:'Deutsche Bank',
               14:'Development Credit Bank',
               15:'Dhanlaxmi Bank',
               16:'Federal Bank',
               17:'ICICI Bank',
               18:'IDBI Bank',
               19:'Indian Bank',
               20:'Indian Overseas Bank',
               21:'IndusInd Bank',
               22:'ING Vysya Bank',
               23:'Jammu and Kashmir Bank',
               24:'Karnataka Bank Ltd',
               25:'Karur Vysya Bank',
               26:'Kotak Bank',
               27:'Laxmi Vilas Bank',
               28:'Oriental Bank of Commerce',
               29:'Punjab National Bank - Corporate Banking',
               30:'Punjab National Bank - Retail Banking',
               31:'Punjab & Sind Bank',
               32:'Shamrao Vitthal Co-operative Bank',
               33:'South Indian Bank',
               34:'State Bank of Bikaner & Jaipur',
               35:'State Bank of Hyderabad',
               36:'State Bank of India',
               37:'State Bank of Mysore',
               38:'State Bank of Patiala',
               39:'State Bank of Travancore',
               40:'Syndicate Bank',
               41:'Tamilnad Mercantile Bank Ltd.',
               42:'UCO Bank',
               43:'Union Bank of India',
               44:'United Bank of India',
               45:'Vijaya Bank',
               46:'Yes Bank Lt',
    
       }
})

.constant("Cabs",{

    Cab_types : {
 
                     1:     'Monthly Rental',
                     2:     'Sightseeing',
                     3:     'Luxury', 
                     4:     'Outstation',
                     5:     'Self Drive', 
                     6:     'Hire a Driver ',
                     7:     'Quick Cabs'
                   
 
    }
 
 
 
 
 
 })

 .factory('dataShare',function($rootScope){
    var service = {};
    service.data = false;
    service.sendData = function(data){
        this.data = data;
        $rootScope.$broadcast('data_shared');
    };
    service.getData = function(){
      return this.data;
    };
    return service;
  })
 

.controller('Cab_HomeController',["$scope", "$http","dataShare", function($scope, $http, dataShare, $filter) {
    $scope.info = {};

    $scope.getCabs = function(id) {
        // console.log("$location.path",$location.path);
        console.log("$scope.info",$scope.info);
        dataShare.sendData($scope.info);
        $scope.location=document.location.href;
        console.log("$scope.location",$scope.location);
        window.open($scope.location + "/list?city=" + $scope.info.pickup_location + "&cab_type=" + id ,'_self'); 
      } 
    
  
  }])


.controller('CabListController',["$scope", "$http","Constants","dataShare", function($scope, $http, Constants, dataShare, $filter) {
    
    $scope.car_types = Constants.Car_types;
    var info = {};
    $scope.info = {};
    $scope.cab_type = 1;

    var str = document.location.search.split("&");
    var type = str[1].split("=");
    $scope.cab_type = type[1];
    
    


    $scope.$on('data_shared',function(){
                            info =  dataShare.getData();    
             $scope.info = info;

    })
    console.log("$scope.info",$scope.info);

    $http({
        method: 'GET',
        url: '/api/v1/cab' + document.location.search
      }).then(function successCallback(response) {

          $scope.cabs= response.data.result.cabs;
          console.log("$scope.cabs",$scope.cabs);
          // this callback will be called asynchronously
          // when the response is available
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
      })

    $scope.type = function(id)  {
        return $scope.car_types[id]
    }

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



//--------------------cab detail/booking controller-----------------------  


  .controller('detailController',["$scope", "$http","bank_type", function($scope, $http, bank_type, $filter) {
    $scope.bank = bank_type.bank;
    
    $scope.cab= {}; // main cab model
    console.log("js file");
    $http({
        method: 'GET',
        url: '/api/v1/cab' 
      }).then(function successCallback(response) {
          $scope.cab= response.data.result.cabs;
          console.log("$scope.bank",$scope.bank);
          
          console.log("cab data",$scope.cab);
          // this callback will be called asynchronously
          // when the response is available
          getdeal();
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
      })
   
      var getdeal=function(){
        $scope.deal={};
        $scope.cabs={};
        var search =location.pathname;
        var id = search.split("/");
        $http({
          method: 'GET',
          url: '/api/v1/cab'
        }).then(function successCallback(response) {
            for(var i=0; i<response.data.result.cabs.length; i++){
                for(var j=0; j<response.data.result.cabs[i].deals.length; j++){
                    if(response.data.result.cabs[i].id==1 && response.data.result.cabs[i].deals[j].id==1){
                        $scope.cabs =response.data.result.cabs[i];
                        $scope.deal =response.data.result.cabs[i].deals[j];

                        console.log("cab[]",$scope.cabs );         
                        console.log("deal[]",$scope.deal );     
                        
                        return $scope.cabs,$scope.deal ;
                        
                        
              }
            }
        }
          }, function errorCallback(response) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
        });
      }

  }]) 