<?php
	require 'db_config.php'; 
	
	$sql = $db->prepare("SELECT id, Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM billing_info");
	$sql->execute(); 

	/* Fetch all of the remaining rows in the result set */
	$results = $sql->fetchAll();

	echo json_encode($results); 

?>