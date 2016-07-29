var app = angular.module('app', []);

// Controller
app.controller("BoardWriteCtrl", function($scope, $http, $attrs) {
    $scope.submit = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board";

        sendData["memberId"] = $attrs.memberid;
        sendData["title"] = $scope.title;
        sendData["content"] = $scope.content;

        reqHttp("POST", $http, reqUrl, sendData, function(data) {
            if(data.STS == SUCCESS) {
                window.location.href = "/board/list";
            }
        });
    }
});
