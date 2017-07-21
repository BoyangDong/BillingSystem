$( document ).ready(function() {
	
	$dummy = "1234";
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
				/*	var htmlRow=`<tr>
									<td>${responseObject.info.Firm}</td>
									<td>${responseObject.info.Office}</td>
									<td>${responseObject.info.Account}</td>
									<td>${responseObject.info.Currency}</td>
									<td>${responseObject.info.Off_Office}</td>
									<td>${responseObject.info.Off_Account}</td>
									<td>${responseObject.info.Description}</td>
									<td>${responseObject.info.Net_Amount}</td>
									<td>${responseObject.info.Comment_Code}</td>							
								</tr>`;
					$('tbody').append(htmlRow);*/
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
					rows = rows + '<button data-toggle="modal" data-target="#edit-item" class="btn btn-primary edit-item">Edit</button> ';
        			rows = rows + '<button class="btn btn-danger remove-item">Delete</button>';
       				rows = rows + '</td>';
	  				rows = rows + '</tr>';
					$("tbody").append(rows);
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
			toastr.success('New Billing Info is Added!', 'Success Alert', {timeout: 5000});
		});
	})
});