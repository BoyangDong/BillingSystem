<?php
	require 'db_config.php'; 

	/* Once process button is hit, flush out the existing data */
	try{
		$sql = "TRUNCATE billing_info";	
		$db->exec($sql);
		$deleteStatus = 1;
	}
	catch(PDOException $e){
		$deleteStatus = 0;
	} 
	/* Have the data ready based on users selection */
	$user_selection = implode(', ', $_POST['recurring_group']);
	$da = trim($_POST['billing_date']);
	// create a string to hold all the user selection with comma separated
	// need to FIRST OF convert it to string so that the statement can use
	$query = $db->prepare('SELECT * FROM recurring_charges WHERE Type IN ('.$user_selection.')'); 
	$query->execute();
	$results = $query->fetchAll();
	/* Copy recurring charges into the working table*/
	foreach($results as $value ) {
		$sql = "INSERT INTO billing_info(Date, Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount) 
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

		$stmt = $db->prepare($sql);
		$insert = $stmt->execute([$da, $value['Invoice_Number'], $value['Firm'], $value['Office'], $value['Account'], $value['Currency'], $value['Off_Office'], $value['Off_Account'], $value['Description'], $value['Net_Amount']]);
	}

	echo json_encode(array('data' =>$results, 'delete'=>$deleteStatus));

?>