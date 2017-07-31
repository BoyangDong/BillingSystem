<?php
	require_once 'db_config.php';
	
	$sql = $db->prepare("SELECT * FROM adjustment_history");
	$sql->execute(); 

	/* Fetch all of the remaining rows in the result set */
	$results = $sql->fetchAll();


	
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<div>
			<strong><h4 style="text-align: center; position:relative; top:20px;">Adjustment History</h4></strong>
			<i class="fa fa-refresh" id="refresh" aria-hidden="true"></i>
			</br>
		</div>

	<?php 
		foreach ($results as $row) {
			echo '<div data-id =' . $row['id'] . ' data-name="test">';
			echo '<p class="history" style="margin: 12px;">' . $row['invoice_num'] ;
			echo '<i class="fa fa-pencil-square-o edit-adjustment" id="edit-adjustment" data-toggle="modal" data-target="#edit-adjustment-history" ></i> ';
			echo '<i class="fa fa-trash-o remove-adjustment" id="delete-adjustment"></i></br>';
			echo $row['content'] . '</p>';
			echo '</div>';
		}
	?>
</body>
</html>


	



<!--?php
	foreach ($results as $row) {
		echo '<p>Name: ' . $row['invoice_num'] . '</p>';
		echo '<p>Content : ' . $row['content'] . '</p>';
	}
?-->