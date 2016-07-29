var app = angular.module('app', ["ngSanitize"]).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});;

// CONTROLLER
app.controller("BoardViewCtrl", function($scope, $http, $attrs) {
    // VARIABLE
    $scope.boardId = $attrs.id;
    $scope.memberId = $attrs.memberid;
    $scope.member = $attrs.member;

    // FUNCTION
    $scope.initPosting = function($scope, $http) {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board/" + $attrs.id;

        reqHttp("GET", $http, reqUrl, null, function(data) {
            var resData = data.DAT;
            var posting = resData.posting;
            $scope.posting = posting;
            $scope.title = posting.title;
            $scope.content = (posting.content).replace(/ /g, "&nbsp").replace(/(?:\r\n|\r|\n)/g, '<br />');
            $scope.commentList = posting.comments;
        });
    }


    $scope.editPosting = function() {
        window.location.href = "/board/edit/" + $scope.posting.id;
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


app.directive("submitComment", ['$http', function($http) {
    return {
        restrict : "A",
        link : function($scope, element) {
            element.bind("keydown", function(event) {
                if(event.which === 13) {
                    var sendData = {};
                    var reqUrl = MAIN_URL + "/api/comment/";

                    sendData["memberId"] = $scope.memberId;
                    sendData["boardId"] = $scope.boardId;
                    sendData["comment"] = $scope.comment;

                    reqHttp("POST", $http, reqUrl, sendData, function(data) {
                        if(data.STS == SUCCESS) {
                            var resData = data.DAT;
                            var newComment = {};
                            newComment["id"] = resData.id;
                            newComment["comment"] = resData.comment;
                            newComment["comment_writer"] = $scope.member;
                            newComment["regdt"] = resData.regdt;

                            $scope.commentList.push(newComment);

                            $scope.comment = "";
                        }
                    });
                }
            });
        }
    }
}]);
