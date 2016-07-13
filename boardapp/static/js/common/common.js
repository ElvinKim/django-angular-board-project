function reqHttpPost($http, url, data, success_callback, fail_callback) {
    $http({
    url: url,
    method: "POST",
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    transformRequest: function(obj) {
        var str = [];
        for(var p in obj)
        str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        return str.join("&");
    },
    data: data
    })
    .then(function(response) {
        success_callback(response.data)
    },
    function(response) { // optional
        if(fail_callback) {
            fail_callback(response.data);
        }
    });
}

function reqHttpGet($http, url, success_callback, fail_callback) {
	$http({
       url: url,
       method:"GET"
  	}).then(function(response) {
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