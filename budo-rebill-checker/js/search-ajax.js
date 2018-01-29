$(document).ready(function(){

	$("#filter").click(function(e){
		console.log("filter applied");

		var start_date = document.querySelector('input[name="from_date"]').value; 
		var end_date = document.querySelector('input[name="to_date"]').value;
		var queryLength = -1;

		if(start_date != '' && end_date != ''){
			$.ajax({
				url: 'api/filter_history.php',
				method: 'POST',
				data: { start_date: start_date, end_date: end_date },
				success: function(message){
					var responseObject = JSON.parse(message);
					queryLength = responseObject.length;
					console.log(queryLength);
					if (0 == queryLength){
						toastr.warning('No Record There','Hmm..', {timeOut: 5000});
					}else if (queryLength > 0){
						toastr.success(queryLength + ' record(s) found!', 'Query Succeed', {timeOut: 5000});
						$("tbody tr").remove();
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
							rows = rows + '<td>'+obj.Date+'</td>';
		       				rows = rows + '</td>';
			  				rows = rows + '</tr>';
							$("tbody").append(rows);
						}
					}else {
						toastr.error('Issue Happened','Failed..', {timeOut: 5000});
					}									
				}
			});
		}else{
			alert("Pick a Date & Range!");

		}

	});

});