$( document ).ready(function() {

	var tableRowId;
	
	/* Insert into DB and show on the page*/
	$('.add-info').submit(function(e) {
		e.preventDefault();
		$.ajax({
			url: 'api/create.php',
			method: 'POST',
			data: {
				firm: $('input[name="firm"]').val(),
				office: $('input[name="office"]').val(),
				account: $('input[name="account"]').val(),
				currency: $('input[name="currency"]').val(),
				off_office: $('input[name="off_office"]').val(),
				off_account: $('input[name="off_account"]').val(),
				description: $('textarea[name="description"]').val(),
				net_amount: $('input[name="net_amount"]').val(),
				comment_code: $('input[name="comment_code"]').val()
			},
			success: function(response) {
				// template literal
				var responseObject = JSON.parse(response);
				console.log(responseObject);
				if(responseObject.message=="Billing Info Entered") {
					var rows = '';
					rows = rows + '<tr>';
					rows = rows + '<td>'+responseObject.info.Firm+'</td>';
					rows = rows + '<td>'+responseObject.info.Office+'</td>';
					rows = rows + '<td>'+responseObject.info.Account+'</td>';
					rows = rows + '<td>'+responseObject.info.Currency+'</td>';
					rows = rows + '<td>'+responseObject.info.Off_Office+'</td>';
					rows = rows + '<td>'+responseObject.info.Off_Account+'</td>';
					rows = rows + '<td>'+responseObject.info.Description+'</td>';
					rows = rows + '<td>'+responseObject.info.Net_Amount+'</td>';
					rows = rows + '<td>'+responseObject.info.Comment_Code+'</td>';
					rows = rows + '<td data-id="'+responseObject.info.id+'">';
					rows = rows + '<button data-toggle="modal" data-target="#edit-item" class="edit-item">Edit</button> ';
        			rows = rows + '<button class="remove-item">Delete</button>';
       				rows = rows + '</td>';
	  				rows = rows + '</tr>';
					$("tbody").append(rows);
					toastr.success('ADDED!', 'Success', {timeout: 2000});
				}
			},
			fail: function() {
				alert('An error occurred');
			}
		}).done(function(data){
			$("#create-item").find("input[name='account']").val('');
			$("#create-item").find("input[name='off_account']").val('');
			$("#create-item").find("textarea[name='description']").val('');
			$("#create-item").find("input[name='net_amount']").val('');			
		});
	});

	/* Edit Item*/
	$("body").on("click", ".edit-item", function(){
		tableRowId = $(this).parents('tr').index();
		var id = 			$(this).parent("td").data('id');
		var firm = 			$(this).parents("tr").find("td").eq(0).text(); 
		var office = 		$(this).parents("tr").find("td").eq(1).text(); 
		var account = 		$(this).parents("tr").find("td").eq(2).text(); 
		var currency = 		$(this).parents("tr").find("td").eq(3).text(); 
		var off_office = 	$(this).parents("tr").find("td").eq(4).text(); 
		var off_account = 	$(this).parents("tr").find("td").eq(5).text(); 
		var description = 	$(this).parents("tr").find("td").eq(6).text(); 
		var net_amount = 	$(this).parents("tr").find("td").eq(7).text(); 
		var comment_code = 	$(this).parents("tr").find("td").eq(8).text(); 

		$("#edit-item").find("input[name='firm']").val(firm);
		$("#edit-item").find("input[name='office']").val(office);
		$("#edit-item").find("input[name='account']").val(account);
		$("#edit-item").find("input[name='currency']").val(currency);
		$("#edit-item").find("input[name='off_office']").val(off_office);
		$("#edit-item").find("input[name='off_account']").val(off_account);
		$("#edit-item").find("textarea[name='description']").val(description);		
		$("#edit-item").find("input[name='net_amount']").val(net_amount);
		$("#edit-item").find("input[name='comment_code']").val(comment_code);
		
		$("#edit-item").find(".edit-id").val(id);
	});

	/* Update Item*/
	$(".crud-submit-edit").click(function(e){
		e.preventDefault(); 

		var form_action = $("#edit-item").find("form").attr("action");
		var id = $("#edit-item").find(".edit-id").val(); 

		var firm = $("#edit-item").find("input[name='firm']").val();
		var office = $("#edit-item").find("input[name='office']").val();
		var account = $("#edit-item").find("input[name='account']").val();
		var currency = $("#edit-item").find("input[name='currency']").val();
		var off_office = $("#edit-item").find("input[name='off_office']").val();
		var off_account = $("#edit-item").find("input[name='off_account']").val();
		var description = $("#edit-item").find("textarea[name='description']").val();
		var net_amount = $("#edit-item").find("input[name='net_amount']").val();
		var comment_code = $("#edit-item").find("input[name='comment_code']").val();

		if(firm != '' && office != '' && account != '' && currency != '' && off_office != '' && off_account != '' && description != '' && comment_code != ''){
			$.ajax({
				type: 'POST',
				url: "api/update.php",
				data:{
					firm: firm,
					office: office,
					account: account,
					currency: currency,
					off_office: off_office,
					off_account: off_account,
					description: description,
					net_amount: net_amount,
					comment_code: comment_code,
					id: id
				},
				success: function(response) {
					console.log(response);
					var tableRow = $('tbody tr').eq(tableRowId);
					var responseObject = JSON.parse(response);
					tableRow.find('td').eq(0).text(responseObject.Firm);
					tableRow.find('td').eq(1).text(responseObject.Office);
					tableRow.find('td').eq(2).text(responseObject.Account);
					tableRow.find('td').eq(3).text(responseObject.Currency);
					tableRow.find('td').eq(4).text(responseObject.Off_Office);
					tableRow.find('td').eq(5).text(responseObject.Off_Account);
					tableRow.find('td').eq(6).text(responseObject.Description);
					tableRow.find('td').eq(7).text(responseObject.Net_Amount);
					tableRow.find('td').eq(8).text(responseObject.Comment_Code);
				}
			}).done(function(data){
				console.log('ajax done');
				//console.log(data);
				$(".modal").modal('hide');
				toastr.success('UPDATED!', 'Success', {timeout: 2000});
			});
		}else{
			alert('Please fill all the blanks required..');
		}

	});

	/* Remove Item */
	$("body").on("click",".remove-item",function(){
		var id = $(this).parent("td").data('id');
		var c_obj = $(this).parents("tr");
		$.ajax({
	    	dataType: 'json',
		 	type:'POST',
	    	url: 'api/delete.php',
	    	data:{id:id}
	    }).done(function(data){
	        c_obj.remove();
	        toastr.success('DELETED!', 'Success', {timeOut: 2000});
	    });

	});

	/*Send Email Ajax*/
	$(".send-email").click(function(e){
		e.preventDefault();
		var recipients = [];
		$('input[type="checkbox"]').each(function(i) {
			if($(this).is(":checked")) {
				recipients.push($(this).val());	
			}
		});
		console.log("hello world");
		console.log(("input[type=checkbox]:checked").length);
		console.log(recipients);

		$.ajax({
			url: 'api/send_email.php', 
			method: 'POST',
			data: {
				mail_to: recipients,
				mail_sub: $('input[name="mail_sub"]').val(),
				mail_msg: $('textarea[name="mail_msg"]').val()
			},
			success: function(response) {
				console.log(response);
				/*console.log('email ajax done');
				console.log('hello world');*/
				if(true){					
					toastr.success('Email Sent!', 'Success', {timeOut: 5000});
					$(".modal").modal('hide');
				}else{
					toastr.error('Issue Happened while Sending Email..','Failed..', {timeOut: 5000});
				}
			},
			fail: function() {
				toastr.error('Failed..', 'Send Email AJAX Failed..', {timeOut: 5000});
			}
		}).done(function(data){
			
		});
	});

	/*Delete All Event*/
	$("#confirm_delete").click(function(e){
		$.ajax({
			url: 'api/delete_all.php',
			method: 'GET',
			success: function(message) {
				console.log(message);
				if(message == 1){
					$("tbody tr").remove();
					toastr.success('All Gone!', 'Success', {timeOut: 5000});
				}else{
					toastr.error('Issue Happened while Start New..','Failed..', {timeOut: 5000});
				}
			}
		});

	});


});