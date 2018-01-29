<?php
	require 'db_config.php';

	$output_bills = [];
	if(isset($_POST["start_date"], $_POST["end_date"])){
		$q = "  
			SELECT * FROM billing_pool  
			WHERE Date BETWEEN '".$_POST["start_date"]."' AND '".$_POST["end_date"]."'  
		"; 
		$query = $db->prepare($q); 
		$query->execute();
		$output_bills = $query->fetchAll(); 
	}
	echo json_encode($output_bills);

?>