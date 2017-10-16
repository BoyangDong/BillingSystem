$( document ).ready(function() {

	getDataAndDisplay();

	var tableRowId;
	var billingDateObj; 

	/* Insert into DB and show on the page*/
	$('.add-info').submit(function(e) {
		e.preventDefault();
		
		billingDateObj = document.querySelector('input[type="date"]');

		$.ajax({
			url: 'api/create.php',
			method: 'POST',
			data: {
				billing_date: billingDateObj.value,
				invoice_number: $('input[name="invoice_number"]').val(),
				firm: $('input[name="firm"]').val(),
				office: $('input[name="office"]').val(),
				account: $('input[name="account"]').val(),
				currency: $('input[name="currency"]').val(),
				off_office: $('input[name="off_office"]').val(),
				off_account: $('input[name="off_account"]').val(),
				description: $('textarea[name="description"]').val(),
				net_amount: $('input[name="net_amount"]').val(),
				comment_code: $('input[name="comment_code"]').val(),
				comments: $('input[name="comments"]').val()
			},
			success: function(response) {
				// template literal
				var responseObject = JSON.parse(response);
				console.log(responseObject);
				if(responseObject.message=="Billing Info Entered") {
					var rows = '';
					rows = rows + '<tr>';
					rows = rows + '<td>'+responseObject.info.Invoice_Number+'</td>';
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
					rows = rows + '<i class="fa fa-pencil-square-o edit-item" id="pencil" data-toggle="modal" data-target="#edit-item" ></i> ';
        			rows = rows + '<i class="fa fa-trash-o remove-item" id="trash"></i>';
        			//rows = rows + '<i class="fa fa-adjust adjust-item" id="adj"></i>';
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
			$("#create-item").find("input[name='invoice_number']").val('#');
			$("#create-item").find("input[name='firm']").val('D');
			$("#create-item").find("input[name='office']").val('UDN');
			$("#create-item").find("input[name='account']").val('');
			$("#create-item").find("input[name='currency']").val('U1');
			$("#create-item").find("input[name='off_office']").val('UDN');
			$("#create-item").find("input[name='off_account']").val('');
			$("#create-item").find("input[name='net_amount']").val('');	
			$("#create-item").find("textarea[name='description']").val('');				
			$("#create-item").find("input[name='comment_code']").val('R');	
			$("#create-item").find("input[name='comments']").val('');			
		});
	});

	/* Edit Item*/
	$("body").on("click", ".edit-item", function(){
		tableRowId = $(this).parents('tr').index();
		var id = 			$(this).parent("td").data('id');

		var invoice_number =$(this).parents("tr").find("td").eq(0).text(); 
		var firm = 			$(this).parents("tr").find("td").eq(1).text(); 
		var office = 		$(this).parents("tr").find("td").eq(2).text(); 
		var account = 		$(this).parents("tr").find("td").eq(3).text(); 
		var currency = 		$(this).parents("tr").find("td").eq(4).text(); 
		var off_office = 	$(this).parents("tr").find("td").eq(5).text(); 
		var off_account = 	$(this).parents("tr").find("td").eq(6).text(); 
		var description = 	$(this).parents("tr").find("td").eq(7).text(); 
		var net_amount = 	$(this).parents("tr").find("td").eq(8).text(); 
		var comment_code = 	$(this).parents("tr").find("td").eq(9).text(); 

		$("#edit-item").find("input[name='invoice_number']").val(invoice_number);
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

		console.log(id); 

	});

	/* Update Item*/
	$(".crud-submit-edit").click(function(e){
		e.preventDefault(); 

		var form_action = $("#edit-item").find("form").attr("action");
		var id = $("#edit-item").find(".edit-id").val(); 

		var invoice_number = $("#edit-item").find("input[name='invoice_number']").val();
		var firm = $("#edit-item").find("input[name='firm']").val();
		var office = $("#edit-item").find("input[name='office']").val();
		var account = $("#edit-item").find("input[name='account']").val();
		var currency = $("#edit-item").find("input[name='currency']").val();
		var off_office = $("#edit-item").find("input[name='off_office']").val();
		var off_account = $("#edit-item").find("input[name='off_account']").val();
		var description = $("#edit-item").find("textarea[name='description']").val();
		var net_amount = $("#edit-item").find("input[name='net_amount']").val();
		var comment_code = $("#edit-item").find("input[name='comment_code']").val();
		var comments = $("#edit-item").find("input[name='comments']").val();

		console.log("updates from here" + id + " " + invoice_number);

		if(invoice_number != '' && firm != '' && office != '' && account != '' && currency != '' && off_office != '' && off_account != '' && description != '' && comment_code != ''){
			$.ajax({
				type: 'POST',
				url: "api/update.php",
				data:{
					invoice_number: invoice_number, 
					firm: firm,
					office: office,
					account: account,
					currency: currency,
					off_office: off_office,
					off_account: off_account,
					description: description,
					net_amount: net_amount,
					comment_code: comment_code,
					id: id,
					comments: comments
				},
				success: function(response) {
					console.log(response);
					var tableRow = $('tbody tr').eq(tableRowId);
					var responseObject = JSON.parse(response);
					tableRow.find('td').eq(0).text(responseObject.Invoice_Number);
					tableRow.find('td').eq(1).text(responseObject.Firm);
					tableRow.find('td').eq(2).text(responseObject.Office);
					tableRow.find('td').eq(3).text(responseObject.Account);
					tableRow.find('td').eq(4).text(responseObject.Currency);
					tableRow.find('td').eq(5).text(responseObject.Off_Office);
					tableRow.find('td').eq(6).text(responseObject.Off_Account);
					tableRow.find('td').eq(7).text(responseObject.Description);
					tableRow.find('td').eq(8).text(responseObject.Net_Amount);
					tableRow.find('td').eq(9).text(responseObject.Comment_Code);
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
	$("form[name='sendMail']").submit(function(e){
		e.preventDefault();
		var formData = new FormData(this); //'this' referes to the particular form itself, since the selector can match more than one element "form[name='sendMail']"
		var id = $(this).attr('id');
		var apiUrl = 'api/send_clearing_firm_email.php';
		if(id === 'user-submit-for-approval-form' || id === 'reject-user-form') { // in js '3' == 3 is true, but '3' === 3 is false 
			apiUrl = 'api/send_email.php';			
		}
		$.ajax({
			url: apiUrl, 
			method: 'POST',
			data: formData,
			async: false,
			cache: false,
			contentType: false,
			processData: false,
			success: function(response) {
				var r = JSON.parse(response);
				console.log(r);
				/*console.log('email ajax done');
				console.log('hello world');*/
				if(r.send_status){					
					toastr.success(r.message, 'Success', {timeOut: 5000});
					$(".modal").modal('hide');
				}else{
					toastr.error(r.message, 'Failed..', {timeOut: 5000});
				}
			},
			fail: function() {
				toastr.error('Failed..', 'Send Email AJAX Failed..', {timeOut: 5000});
			}
		}).done(function(data){
			
		});
	});

	/*Start a New Page Event*/
	$("#confirm_delete").click(function(e){
		// select only the ones that are checked. 
		var recurring_group = [];
		var billingDateObj = document.querySelector('input[type="date"]');

		$('input[type="checkbox"]:checked').each(function(index) {
			recurring_group.push('"'+this.value+'"'); // it's in string already but mysql requires that strings are quoted
		});
		// the post on the html is not really necessary because we are already using javascript to handle the post.
		// if posting to the php backend straight from the html we could have done that
		// but that will make the page to reload
		console.log(recurring_group);
		// so an empty array was initialized to recurring_group, so that we can push each selection into the array.
		// now if the user did not check any of the checkboxes then the recurring_group wil be an empty array like this []
		// the empty array just cannot be sent to the backend anyhow
		// that's why do a check on if the array is empty, so if it is empty, it'll send an empty string
		// otherwise it will send the array itself.
		// now on the php end, only check if it was an array that was sent or a string is required. bearing in mind that if a string
		// is sent then that means te user did not select anything
		$.ajax({
			url: 'api/delete_all.php',
			method: 'POST',
			data: { 
				billing_date: billingDateObj.value,
				recurring_group: recurring_group.length ? recurring_group : ''
			}, 
			success: function(message) {
				var responseDetails = JSON.parse(message);
				console.log(responseDetails.data);
				if(responseDetails.delete == 1){
					$("tbody tr").remove();
					toastr.success('A New Sheet Created!', 'Success', {timeOut: 5000});
					for(var i = 0; i < responseDetails.data.length; i++){
						var obj = responseDetails.data[i];
						var rows = '';
						rows = rows + '<tr>';
						rows = rows + '<td>'+obj.Invoice_Number+'</td>';
						rows = rows + '<td>'+obj.Firm+'</td>';
						rows = rows + '<td>'+obj.Office+'</td>';
						rows = rows + '<td>'+obj.Account+'</td>';
						rows = rows + '<td>'+obj.Currency+'</td>';
						rows = rows + '<td>'+obj.Off_Office+'</td>';
						rows = rows + '<td>'+obj.Off_Account+'</td>';
						rows = rows + '<td>'+obj.Description+'</td>';
						rows = rows + '<td>'+obj.Net_Amount+'</td>';
						rows = rows + '<td>'+obj.Comment_Code+'</td>';
						rows = rows + '<td data-id="'+obj.id+'">';
						rows = rows + '<i class="fa fa-pencil-square-o edit-item" id="pencil" data-toggle="modal" data-target="#edit-item" ></i> ';
	        			rows = rows + '<i class="fa fa-trash-o remove-item" id="trash"></i>';
	        			//rows = rows + '<i class="fa fa-adjust adjust-item" id="adj"></i>';
	       				rows = rows + '</td>';
		  				rows = rows + '</tr>';
						$("tbody").append(rows);
					}
					getDataAndDisplay();				
				}else{
					toastr.error('Issue Happened while Start New..','Failed..', {timeOut: 5000});
				}
			}
		});

	});

	/* Synchronization Icon */
	$("body").on("click", ".sync", function(){
		console.log("sync icon is clicked..");
		getDataAndDisplay();
	});

	function getDataAndDisplay() {
		console.log('here');
		$.ajax({
			url: "api/sync.php",
			method: "GET", 
			success: function(response){
				$("tbody tr").remove();
				var responseObject = JSON.parse(response);
				if(0==responseObject.length){
					toastr.info('Start a Sheet with Date Specified!', 'Howdy', {timeOut: 5000});
				}else{
					for(var i = 0; i < responseObject.length; i++){
						var obj = responseObject[i];
						var rows = '';
						rows = rows + '<tr>';
						rows = rows + '<td>'+obj.Invoice_Number+'</td>';
						rows = rows + '<td>'+obj.Firm+'</td>';
						rows = rows + '<td>'+obj.Office+'</td>';
						rows = rows + '<td>'+obj.Account+'</td>';
						rows = rows + '<td>'+obj.Currency+'</td>';
						rows = rows + '<td>'+obj.Off_Office+'</td>';
						rows = rows + '<td>'+obj.Off_Account+'</td>';
						rows = rows + '<td>'+obj.Description+'</td>';
						rows = rows + '<td>'+obj.Net_Amount+'</td>';
						rows = rows + '<td>'+obj.Comment_Code+'</td>';
						rows = rows + '<td data-id="'+obj.id+'">';
						rows = rows + '<i class="fa fa-pencil-square-o edit-item" id="pencil" data-toggle="modal" data-target="#edit-item" ></i> ';
	        			rows = rows + '<i class="fa fa-trash-o remove-item" id="trash"></i>';
	        			//rows = rows + '<i class="fa fa-adjust adjust-item" id="adj"></i>';
	       				rows = rows + '</td>';
		  				rows = rows + '</tr>';
						$("tbody").append(rows);
					}					
					toastr.success('Synced with DB!', 'Success', {timeOut: 800});
				}
			}
		});
	}

});