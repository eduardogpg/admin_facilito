$( document ).ready(function() {
  
  function get_user(user) {
    $.ajax({
			url : "http://localhost:8000/client/search/",
			type : "POST",
			data : { user : user },
			success : function(json_data) {
        load_user(json_data)
      },
      error : function(xhr,errmsg,err) {
         console.log("Erro de Ajax")
      }
    });
	};

  function search_user() {
    user = $('#search-user').val()
    get_user(user)
	};
  
  $( "#search-user-form" ).submit(function( event ) {
  	event.preventDefault();
  	search_user();
	});

  function load_user(data){
    $("#search-result ul").empty()
    data.forEach(function (user) {
      console.log(user.username)
      inner_html = " <li>" + user.username  +"<a href='#'> Agregar</a> </li>"
      $("#search-result ul").append(inner_html)
    })
  }
});