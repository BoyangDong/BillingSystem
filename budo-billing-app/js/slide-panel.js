$(document).ready(function(){
	$('#sidemenu').BootSideMenu({
		side: 'left',
		pushBody: false
	});

	/*Adjustment History Panel Funtionalities*/
	$("body").on("click",".remove-adjustment", function(){
		console.log($(this).parents('div').data("id")); //.data('name')
		console.log($(this).parents('div').data("name"));
		console.log("starting from hererere");

		var id = $(this).parents('div').data("id"); 
		var h_obj = $(this).parents("div[data-id="+id+"]"); //insead 
		$.ajax({
	    	dataType: 'json',
		 	type:'POST',
	    	url: 'api/delete_adjustment.php',
	    	data:{id} //convension from es6, same as {id:id}
	    }).done(function(data){
	        h_obj.remove();
	        toastr.success('ADJUSTMENT DELETED!', 'Success', {timeOut: 2000});
	    });
	});

});


