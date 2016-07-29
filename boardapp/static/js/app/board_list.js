var app = angular.module('app', ["ui.bootstrap"]).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});;


// CONTROLLER
app.controller("UserInfoCtrl", function($scope, $http){
    $scope.logout = function() {
        window.location.href = "/member/logout";
    }

    $scope.moveToLogin = function() {
        window.location.href = "/member/login";
    }
});


app.controller("BoardListCtrl", function($scope, $http) {
    // VARIABLE
    $scope.currentPage = 1;
    $scope.numPerPage = 10;
    $scope.maxSize = 5;


    //WATCH FUNCTION
    $scope.$watch('currentPage + numPerPage', function() {
        var begin = (($scope.currentPage - 1) * $scope.numPerPage)
        var end = begin + $scope.numPerPage;

        $scope.displayBoardList($scope, $http, $scope.currentPage);
    });


    // FUNCTION
    $scope.moveToView = function($event, posting) {
        window.location.href = "/board/view/" + posting.id;
    }


    $scope.displayBoardList = function($scope, $http, pageIdx) {
        var sendData = {};
        var reqUrl = MAIN_URL + "/api/board?page=" + pageIdx;

        reqHttp("GET", $http, reqUrl, null,  function(data) {
            if(data.STS == SUCCESS) {
                var resData = data.DAT;
                var boardList = resData.board_list;
                $scope.boardList = boardList;
                $scope.totalCnt = resData.total_cnt;
            }
        });
    }

    $scope.displayBoardList($scope, $http, 1);
});


app.controller("BtnCtrl", function($scope, $http) {
    $scope.moveToWrite = function(){
        window.location.href = "/board/write";
    }
});
