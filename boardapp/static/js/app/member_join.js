var app = angular.module('app', [])

// CONTROLLER
app.controller("MemberJoinCtrl", function($scope, $http) {
    // FUNCTION
    $scope.register = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/member";

        sendData["userId"] = $scope.userId;
        sendData["password"] = Sha256.hash($scope.password);

        reqHttp("POST", $http, reqUrl, sendData, function(data) {
            console.log(data);
            if(data.STS == SUCCESS) {
                window.location.href = "/member/login";
            }
        });
    };


    $scope.moveToLogin = function() {
        window.location.href = "/member/login";
    }


    $scope.checkFieldValid = function() {
        if($scope.userId === undefined || $scope.password === undefined || $scope.checkPassword === undefined) {
            return true;
        } else if(("" + $scope.userId).length == 0 || ("" + $scope.password).length == 0 || ("" + $scope.checkPassword).length == 0) {
            return true;
        } else if($scope.password != $scope.checkPassword) {
            return true;
        } else {
            return false;
        }
    }
});

