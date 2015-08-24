(function () {
    'use strict';

    var app = angular.module('app', ['ngRoute', 'angular.filter', 'uiSwitch', 'ui.router']);

    app.config(function() {
    });

    app.directive('showtab',
      function () {
        return {
            link: function (scope, element) {
                element.click(function(e) {
                    e.preventDefault();
                    $(element).tab('show');
                });
            }
        };
    });

    app.service('AppsService', ['$http', function($http) {
        this.list = function(callback) {
            $http.get('/stub/apps.json').success(function(data, status, headers, config) {
                console.log(data, status, headers, config);
                if (callback) {
                  callback(data.system, data.apps);
                }
            }).error(function(data, status, headers, config) {
                console.log(data, status, headers, config);
            });
        };
    }]);

    app.controller('appsController', ['$scope', '$http', function($scope, $http) {
        $http.get('server/apps.json').
          success(function(data, status, headers, config) {
            console.log(data, status, headers, config);
          }).
          error(function(data, status, headers, config) {
            console.log('error');
            console.log(data, status, headers, config);
          });
    }]);

})();
