var app = angular.module('app', [])

// Controller
app.controller("MemberLoginCtrl", function($scope, $http) {
    $scope.login = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/member?";

        sendData["userId"] = $scope.userId;
        sendData["password"] = Sha256.hash($scope.password);

        reqUrl += serialize(sendData);

        reqHttp("GET", $http, reqUrl, null, function(data) {
            if(data.STS == SUCCESS) {
                window.location.href = "/board/list";
            }
        });
    };


    $scope.moveToJoin = function() {
        window.location.href = "/member/join";
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
