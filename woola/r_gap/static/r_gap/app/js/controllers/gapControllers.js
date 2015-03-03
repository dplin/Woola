(function(){
    angular.module('gapApp').controller('gapController', ['$scope', 'Item', function($scope, Item){

        // Get a list of items.  GET /collection
        $scope.items = Item.query(function(data){
            //console.log("SUCCESS");
        }, function(error){
            //console.log("ERROR");
        });

        // Get single item.  GET /collection/:id
        $scope.itemDetail = function(item){
            return Item.get({ id: item.id }, function(data){ console.log(data); });
        };

        // Delete an item.  DELETE /collection/:id
        $scope.deleteItem = function(item, index){
            item.$delete({ id: item.id }, function(){
                console.log("successfully peformed delete!");
                $scope.items.splice(index, 1);
            });
        };

        // Insert an item.  POST /collection
        $scope.saveItem = function() {

            var json_data = {
                "item_id": "BR3842234",
                "item_image": "http://www.yahoo.ca/abc.jpg",
                "item_name": "Wool Pants",
                "item_price": "499.99",
                "item_url": "http://www.google.ca"
            };

            Item.save(json_data, function(data){
                // Success
                $scope.items.push(data);

                console.log(data);
            }, function(data){
                // Error
                console.log(data);
            });
        };

        // Update an item.  PUT /collection/:id
        //$scope.itemDetail.$update(function(){/* Success */});
    }]);
})();
