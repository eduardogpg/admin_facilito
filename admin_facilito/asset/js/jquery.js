$( document ).ready(function() {

  function create_post(user) {
    $.ajax({
			url : "http://localhost:8000/client/search/",
			type : "POST",
			data : { user : user },

			success : function(json) {
				console.log("success");
        console.log(json)
      },
      error : function(xhr,errmsg,err) {
         console.log("Erro de Ajax")
      }
    });
	};

  function search_user() {
    user = $('#search-user').val()
    console.log(user)
    create_post(user)
	};
  
  $( "#search-user-form" ).submit(function( event ) {
  	event.preventDefault();
  	search_user();
	});

});