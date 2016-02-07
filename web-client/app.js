(function(){
    var app = angular.module('RaspWind', [])

    app.controller('RaspWindController', function(){
        this.windSpeed = 10;
        this.date = new Date();
    })
})();
