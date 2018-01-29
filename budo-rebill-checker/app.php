<?php
	require_once 'api/db_config.php';
	// Start the session
	ob_start();
	session_start();
    
	// Check to see if actually logged in. If not, redirect to login page
	if (!isset($_SESSION['loggedIn']) || $_SESSION['loggedIn'] == false) {
		header("Location: index.php");
	}
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8"> 
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/1000hz-bootstrap-validator/0.11.5/validator.min.js"></script>
	<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/js/toastr.min.js"></script>
	<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>

	<link rel="stylesheet" href="http://code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <link href="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/css/toastr.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Overpass|Quantico|Graduate|Ubuntu" rel="stylesheet">

	<script type="text/javascript" language="javascript" src="js/search-ajax.js"></script>

	<link rel="stylesheet" href="css/style.css"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<title>Rebill Archive</title>
</head>
<body>
	<!--Header Bar-->
	<nav class="navbar navbar-default">
		<div class="container-fluid">
		<div class="navbar-header">
	    	<a class="navbar-brand">
	    	<img alt="Brand" id="budo_logo" src="images/budo_logo.jpg">
	      	</a>
	    	<form method="post" action="logout.php">
		    	<button type="submit" class="btn btn-default btn-sm" id="logoutLblPos">
	        		<span class="glyphicon glyphicon-log-out"></span> Logout
				</button>				
			</form>
	    </div>
	  </div>
	</nav>
	<!--Container-->
	<div class="container">
		<!--Synchronization Icon-->
		<!--main-->
		<div class="row header-row">
			<div class="col-lg-7"> <h2 id="header">Rebill Archive Checker</h2></div> 
			<div class="col-lg-2"> <input type="date" name="from_date" id="from_date" class="form-control" title="Start Date"></div>
			<div class="col-lg-2"> <input type="date" name="to_date" id="to_date" class="form-control" title="End Date"></div>
			<div class="col-lg-1"> <i type="submit" class="fa fa-search fa-2x" name="filter" id="filter" value="Search" title="Search"></i></div>
		</div>

		<!--Main Table Body-->
		<div class="panel panel-info"> 
			<div class="panel-heading" style="font-family: 'Ubuntu', cursive;">Billing History</div>
			<div class="panel-body">
				<!--table class="table table-bordered"--> 
				<table class="table table-bordered table-striped table-hover"> 
					<thead> 
						<tr> 
							<th>Invoice #</th>
							<th>Firm</th>
							<th>Office</th>
							<th>Account</th>
							<th>Currency</th>
							<th>Off Office</th>
							<th>Off Account</th>
							<th>Description</th>
							<th>Net Amount</th>
							<th>Comment</th>
							<th>Date</th>
						</tr>
					</thead>
				<tbody>
				<?php //this is where the recurring charge can be preloaded.?>
				</tbody>
				</table> 
				<!--Pagination-->
				<ul id="pagination" class="pagination-sm">
			</div>
		</div>	

	</div>
	<div>
		<button type="button" class="btn btn-info" id="myBtn" onclick="topFunction()">Top</button>
	</div>

	<script>
		// When the user scrolls down 40px from the top of the document, show the button
		window.onscroll = function() {scrollFunction()};

		function scrollFunction() {
		if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
	    	document.getElementById("myBtn").style.display = "block";
		} else {
	        document.getElementById("myBtn").style.display = "none";
	    	}
		}
		// When the user clicks on the button, scroll to the top of the document
		function topFunction() {
			document.body.scrollTop = 0;
			document.documentElement.scrollTop = 0;
		}
	</script>
	<!--Submit for Approval Modal-->
	<div><br><br><br></div>
	<footer class="footer">
		Version 1.0
	</footer>
	<noscript> 
		<h3>This site requires JavaScript. </h3>
	</noscript>
</body>
</html>