(function(){
    var app = angular.module('RaspWind', ['chart.js'])

    app.controller('RaspWindController', function(){
        this.windSpeed = 10;
        this.date = new Date();
    });

    app.controller('LineCtrl', ['$scope', '$timeout', function ($scope, $timeout) {
        $scope.labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
        $scope.series = ['Series A', 'Series B'];
        $scope.data = [
            [65, 59, 80, 81, 56, 55, 40],
            [28, 48, 40, 19, 86, 27, 90]
        ];

        $scope.onClick = function (points, evt) {
            console.log(points, evt);
        };

        $scope.onHover = function (points) {
            if (points.length > 0) {
                console.log('Point', points[0].value);
            } else {
                console.log('No point');
            }
        };

        $timeout(function () {
            $scope.labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
            $scope.data = [
                [28, 48, 40, 19, 86, 27, 90],
                [65, 59, 80, 81, 56, 55, 40]
            ];
            $scope.series = ['Series C', 'Series D'];
        }, 3000);
  }]);
})();
