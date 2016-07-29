function reqHttp(method, $http, url, data, success_callback, fail_callback) {
    var httpObj = {
        url: url,
        method: method
    }

    if(method == "POST" || method == "PUT") {
        httpObj["headers"] = {'Content-Type': 'application/x-www-form-urlencoded'};
        httpObj["transformRequest"] = function(obj) {
                                            var str = [];
                                            for(var p in obj)
                                            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                                            return str.join("&");
                                        };
        httpObj["data"] = data;
    }

    $http(httpObj).then(function(response) {
        success_callback(response.data)
    },
    function(response) { // optional
        if(fail_callback) {
            fail_callback(response.data);
        }
    });
}


function serialize(obj) {
    var str = [];

    for(var p in obj) {
        if (obj.hasOwnProperty(p)) {
            str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
    }

    return str.join("&");
}