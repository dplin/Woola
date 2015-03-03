(function(){
    /* Using $resource for CRUD */
    angular.module('gapApp').factory('Item', ['$resource', function($resource){
        return $resource('/api/v1/gap_items/:id', null, {
            /* $resource doesn't have a PUT method.  We need to add it in manually. */
            'update': { method: 'PUT' }
        });
    }]);


    /* Using $http for non CRUD AJAX calls. */
    angular.module('gapApp').factory('Crawler', ['$http', function($http){
        var factory = {};
        factory.item_detail = function(){
            return $http.get('/api/v1/crawler');
        };
        return factory;
    }]);
/*
    angular.module('gapApp').factory('gapFactory', ['$http', function($http){
        var factory = {};
        factory.get_items = function(){
            return $http.get('/api/v1/gap_items');
        };
        return factory;
    }]);

*/
})();

