var app = angular.module('app', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});;

// Controller
app.controller("BoardEditCtrl", function($scope, $http, $attrs) {
    // FUNCTION
    $scope.initPosting = function($scope, $http) {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board/" + $attrs.id;

        reqHttp("GET", $http, reqUrl, null, function(data) {
            var resData = data.DAT;
            var posting = resData.posting;

            $scope.title = posting.title;
            $scope.content = posting.content;
        });
    }


    $scope.submit = function() {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board/" + $attrs.id;

        sendData["memberId"] = $attrs.memberid;
        sendData["postingId"] = $attrs.id;
        sendData["title"] = $scope.title;
        sendData["content"] = ($scope.content).trim();

        reqHttp("PUT", $http, reqUrl, sendData, function(data) {
            console.log(data);
            if(data.STS == SUCCESS) {
                window.location.href = "/board/list";
            }
        });
    };

    $scope.initPosting($scope, $http);
});
