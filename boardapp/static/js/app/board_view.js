var app = angular.module('app', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});;

// Controller
app.controller("BoardViewCtrl", function($scope, $http, $attrs) {
    // FUNCTION
    $scope.initPosting = function($scope, $http) {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board/" + $attrs.id;

        reqHttp("GET", $http, reqUrl, null, function(data) {
            var resData = data.DAT;
            $scope.posting = resData.posting;
        });
    }


    $scope.editPosting = function() {
        console.log($scope.posting.id);
    }


    $scope.deletePosting = function() {
        var reqUrl = MAIN_URL + "/api/board/" + $attrs.id;

        reqHttp("DELETE", $http, reqUrl, null, function(data) {
            if(data.STS == SUCCESS) {
                window.location.href = "/board/list";
            }
        });
    }

    $scope.initPosting($scope, $http);
});
