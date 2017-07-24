<?php
	require_once 'api/db_config.php';
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
    <link href="//cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/css/toastr.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Overpass|Quantico|Graduate|Ubuntu" rel="stylesheet">

	<script type="text/javascript" language="javascript" src="js/item-ajax.js"></script>
	<link rel="stylesheet" href="css/style.css"/>
	
	<title>Budo Billing System</title>  	
</head>
<body>

	<!--Header Bar-->
	<nav class="navbar navbar-default">
		<div class="container-fluid">
		<div class="navbar-header">
	    	<a class="navbar-brand" href="http://www.budoholdings.com/">
	    	<img alt="Brand" id="budo_logo" src="images/budo_logo.jpg">
	      	</a>
	    </div>
	  </div>
	</nav>
	<!--Container-->
	<div class="container">
		<div class="row">
			<div class="col-lg-8"> <h2 id="header">Daily Billing System</h2></div>
			<div class="col-lg-1"> 
				<input type="button" class="btn btn-primary" value="New Sheet"/>
			</div>
			<div class="col-lg-1"> 
				<input type="button" class="btn btn-warning" value="Adjustmnt"/>
			</div>
			<div class="col-lg-1">
				<form method="post" action="api/export.php">
					<input type="submit" name="export" id="export" class="btn btn-info" value="csv Export"/>
				</form>
			</div>
			<div class="col-lg-1"> 
				<button type="button" id="createBtn" class="btn btn-success" data-toggle="modal" data-target="#create-item"> 
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
							<th>Firm</th>
							<th>Office</th>
							<th>Account</th>
							<th>Currency</th>
							<th>Off Office</th>
							<th>Off Account</th>
							<th>Description</th>
							<th>Net Amount</th>
							<th>Comment Code</th>
							<th width="140px">Action</th>
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

		<!--create item modal-->
		<div class="modal fade" id="create-item" tabindex="-1" role="dialog" aria-labelledby="createLabel">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        		<h4 class="modal-title" id="createLabel"><strong>Create New Billing Info</strong></h4>
		      		</div>
			      	<div class="modal-body">
			      		<form data-toggle="validator" action="api/create.php" class="add-info" method="POST">
			      			<div class="form-group">
								<label class="control-label" for="title">Firm</label>
								<input type="text" name="firm" class="form-control" value="D" maxlength="1" data-error="Please enter title." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Office</label>
								<input type="text" name="office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Account</label>
								<input type="text" name="account" class="form-control" data-error="Please enter account." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Currency</label>
								<input type="text" name="currency" class="form-control" value="U1" maxlength="2" data-error="Please enter currency." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Office</label>
								<input type="text" name="off_office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Account</label>
								<input type="text" name="off_account" class="form-control" data-error="Please enter off account." required />
								<div class="help-block with-errors"></div>
							</div>

							<div class="form-group">
								<label class="control-label" for="title">Net Amount (-)</label>
								<input type="number" name="net_amount" class="form-control" max="0" value="-0.00" step=".01" data-error="Please enter a VALID net amount." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Description</label>
								<textarea name="description" class="form-control" data-error="Please enter description." required></textarea>
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Comment Code</label>
								<input type="text" name="comment_code" class="form-control" value="R" maxlength="1" data-error="Please enter comment code." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<button type="submit" id="submit" class="btn crud-submit btn-success">Submit</button>
							</div>
			      		</form>
					</div>
				</div>
			</div>
		</div>

		<!--EDIT ITEM MODAL-->
		<div class="modal fade" id="edit-item" tabindex="-1" role="dialog" aria-labelledby="editLabel">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
		        		<h4 class="modal-title" id="editLabel"><strong>Edit Panel</strong></h4>
		      		</div>
			      	<div class="modal-body">
			      		<form data-toggle="validator" action="api/update.php" class="add-info" method="POST">
							<input type="hidden" name="id" class="edit-id"> <!--Different from Create Modal-->
			      			<div class="form-group">
								<label class="control-label" for="title">Firm</label>
								<input type="text" name="firm" class="form-control" value="D" maxlength="1" data-error="Please enter title." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Office</label>
								<input type="text" name="office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Account</label>
								<input type="text" name="account" class="form-control" data-error="Please enter account." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Currency</label>
								<input type="text" name="currency" class="form-control" value="U1" maxlength="2" data-error="Please enter currency." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Office</label>
								<input type="text" name="off_office" class="form-control" value="UDN" maxlength="3" data-error="Please enter office." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Off Account</label>
								<input type="text" name="off_account" class="form-control" data-error="Please enter off account." required />
								<div class="help-block with-errors"></div>
							</div>

							<div class="form-group">
								<label class="control-label" for="title">Net Amount (-)</label>
								<input type="number" name="net_amount" class="form-control" max="0" value="-0.00" step=".01" data-error="Please enter a VALID net amount." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Description</label>
								<textarea name="description" class="form-control" data-error="Please enter description." required></textarea>
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<label class="control-label" for="title">Comment Code</label>
								<input type="text" name="comment_code" class="form-control" value="R" maxlength="1" data-error="Please enter comment code." required />
								<div class="help-block with-errors"></div>
							</div>
							<div class="form-group">
								<button type="submit" id="submit" class="btn crud-submit-edit btn-success">Update</button>
							</div>
			      		</form>
					</div>
				</div>
			</div>
		</div>
	</div>
	<footer class="footer">
		Version 0.1.0
	</footer>
	<noscript> 
		<h3>This site requires JavaScript. </h3>
	</noscript>
</body>
</html>