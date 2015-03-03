(function(){
  $( ".crawler" ).click(function() {
    $.ajax({
       url: '/api/v1/crawler/',
       data: { url: $('#test_url').val() },
       error: function(request, error) {
          console.log('hahaha error:' + error);
       },
       success: function(data) {
            console.log(data);
       },
       type: 'GET'
    });

    return false;
  });
})();

