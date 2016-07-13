var app = angular.module('app', [])

// Controller
app.controller("MemberJoinCtrl", function($scope, $http) {
    $scope.register = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/member?";

        sendData["userId"] = $scope.userId;
        sendData["password"] = $scope.password;

        reqUrl += serialize(sendData)

        reqHttpGet($http, reqUrl, function(data) {
            console.log(data);
            if(data.STS == SUCCESS) {

                //window.location.href = "/member/login";
            }
        });
    };

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

