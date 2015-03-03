(function(){
    var gapApp = angular.module('gapApp', ['ngResource', 'ngCookies']).config(['$httpProvider', '$interpolateProvider', '$locationProvider', '$resourceProvider', function($httpProvider, $interpolateProvider, $locationProvider, $resourceProvider) {
        // Fix Django template tag conflict
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
        // Django trailing slash requirement
        $resourceProvider.defaults.stripTrailingSlashes = false;
        //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        //$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    }]).run(['$http', '$cookies', function($http, $cookies){
        // For CSRF token compatibility with Django
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    }]);
})();

