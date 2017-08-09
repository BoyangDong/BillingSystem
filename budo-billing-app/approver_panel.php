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
	<script type="text/javascript" src="js/datepicker.js"></script>
    <link href="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/css/toastr.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Overpass|Quantico|Graduate|Ubuntu" rel="stylesheet">

	<script type="text/javascript" language="javascript" src="js/item-ajax.js"></script>
	<script type="text/javascript" language="javascript" src="js/BootSideMenu.js"></script>
	<script type="text/javascript" language="javascript" src="js/slide-panel.js"></script>
	<link rel="stylesheet" href="css/datepicker.css"/>
	<link rel="stylesheet" href="css/style.css"/>
	<link rel="stylesheet" href="css/BootSideMenu.css"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	
	<title>Budo Billing System</title>  	
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
		<form method="POST" action="api/sync.php">
			<i class="fa fa-refresh sync" data-toggle="tooltip" aria-hidden="true" title="Sync with DB"></i>
		</form>

		<!--main-->
		<div class="row header-row">
			<div class="col-lg-9"> <h2 id="header">Billing System Approver Panel</h2></div> 
			<div class="col-lg-1"> 
				<input type="button" class="btn btn-default" id="start_new" value="Start New" data-toggle="modal" data-target="#start-new-modal"/>
				<?php include 'modals/start-new-modal.php'; ?>
			</div>
			<!--div class="col-lg-1"> 
				<input type="button" class="btn btn-warning" id="show_adjustment_history" value="Adjustmnt"/>
			</div-->	
			<div class="col-lg-1">
				<form method="post" action="api/export.php">
					<input type="submit" name="export" id="export" class="btn btn-default" value="csv Export"/>
				</form>
			</div>
			<div class="col-lg-1"> 
				<button type="button" id="createBtn" class="btn btn-default" data-toggle="modal" data-target="#create-item"> 
					Create 
				</button>	
			</div>
		</div>

		<!--Main Table Body-->
		<div class="panel panel-info"> 
			<div class="panel-heading">Info Management </div>

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
							<th width="75px">Action</th>
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
		<?php
			include 'modals/create-modal.php';
			include 'modals/edit-modal.php';
		?>
	</div>
	<!--Submit for Approval Modal-->
	<div>
		<div class="col-lg-8"></div>
		<div class="col-lg-1">
			<!--form method="post" action="api/export.php"-->
			<button type="submit" class="btn btn-danger btn-lg" id="reject-form" data-toggle="modal" data-target="#reject-modal" style="margin-bottom: 80px">Reject</button>
		</div>
		<div class="col-lg-1">		
			<!--form method="post" action="api/export.php"-->
			<button type="submit" class="btn btn-success btn-lg" id="submit-form" data-toggle="modal" data-target="#email-clearing-firm-modal" data-toggle="" aria-hidden="true" title="Sync with DB" style="margin-bottom: 80px">
				<div data-toggle="tooltip" aria-hidden="true" title="Sync with DB">Send</div>
			</button>
		</div>
		<div class="col-lg-2"></div>
		<?php
			include 'modals/email-clearing-firm-modal.php';
			include 'modals/reject-modal.php'; 
		?>
	</div>
	<!--div id="sidemenu"> 
		<?php 
		//	include 'modals/adjustment_panel/adjustment-history.php'
		?>
	</div-->
	<footer class="footer">
		Version 1.0
	</footer>
	<noscript> 
		<h3>This site requires JavaScript. </h3>
	</noscript>
</body>
</html>