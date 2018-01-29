<!DOCTYPE HTML>

<?php
	
	// Include personnel info
	include "api/db_config.php"; 

    // Start the session
    session_start();
?>

<html>
    <head>
		<meta charset="utf-8"> 
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		<link href="https://fonts.googleapis.com/css?family=Overpass|Quantico|Graduate|Ubuntu" rel="stylesheet">

		<link rel="stylesheet" href="css/style.css"/>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

		<title>Welcome Page</title>
    </head>
    
    <body>
    	<!--Header Bar-->
		<nav class="navbar navbar-default">
			<div class="container-fluid">
			<div class="navbar-header">
				<a class="navbar-brand">
				<img alt="Brand" id="budo_logo" src="images/budo_logo.jpg">
				</a>		      	
		    </div>
		  </div>
		</nav>
		<!-- form for login -->
        <div class="container">
	        <div class="row">
	        	<div class="col-lg-4"></div>
	        	<div class="col-lg-3 login_panel"> 
	        	<?php
	        		if(isset($_POST['username']) && isset($_POST['password'])){
	        			$un = $_POST['username'];
	        			$pw = md5($_POST['password']);
	        			$stmt = $db->prepare("SELECT * FROM personnel WHERE Username=? AND Password=?");
	        			$stmt->bindParam(1, $un);
	        			$stmt->bindParam(2, $pw);
	        			$stmt->execute(); 
	        			$row = $stmt->fetch();
	        			$user = $row['Username'];
	        			$pass = $row['Password'];
	        			$user_type =$row['Type'];
	        			if($un == $user && $pw == $pass){	        				
	        				$_SESSION['username'] = $user;
	        				$_SESSION['password'] = $pass;
	        				$_SESSION['type'] 	  = $user_type;
	        				$_SESSION['loggedIn'] = true;
	        				echo $user_type;
	       					session_start();	
        					header('Location: app.php');		
	        			}else{
	        	?>
			    			<div class="alert alert-danger alert-dismissible" role="alert">
			    				<button type="button" class="close" data-dismiss="alert" aria-label="Close"> 
			    					<span aria-hidden="true">&times;</span></button>
			    					<strong>Oops!</strong> Invalid Credentials..
			    				</button> 
			    			</div>
	        	<?php
	        			}
	        		}
	        	?>
					<form method="post" action="index.php">
						<h4><b>Welcome to Rebill Archive</b></h4></br>
						<!--input type="id" name="eid" id="eid" class="form-control input-sm chat-input" placeholder="employee id"><br/-->
						<input type="text" name="username" id="username" class="form-control input-sm chat-input" placeholder="username"><br/>
						<input type="password" name="password" id="password" class="form-control input-sm chat-input" placeholder="password"><br/>
					 	<input type="submit" class="btn btn-info" value="Log In">
					</form>
	        	</div>
	        	<div class="col-lg-5"></div>
			</div>
        </div>
	    <footer class="footer">
			Version 1.0
		</footer>
		<noscript> 
			<h3>This site requires JavaScript. </h3>
		</noscript>
    </body>
</html>