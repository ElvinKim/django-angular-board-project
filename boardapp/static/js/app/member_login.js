var app = angular.module('app', [])

// Controller
app.controller("MemberLoginCtrl", function($scope, $http) {
    $scope.login = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/member";

        sendData["userId"] = $scope.userId;
        sendData["password"] = $scope.password;

        reqHttpGET($http, reqUrl, sendData, function(data) {
            if(data.STS == SUCCESS) {
                window.location.href = "/board";
            }
        });
    };

    $scope.checkFieldValid = function() {
        if($scope.userId === undefined || $scope.password === undefined) {
            return true;
        } else if(("" + $scope.userId).length == 0 || ("" + $scope.password).length == 0) {
            return true;
        } else {
            return false;
        }
    }
});
