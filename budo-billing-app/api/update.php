<?php  
	require "db_config.php"; 

	$id = $_POST["id"];

	$post = $_POST;

	$sql = "UPDATE billing_info SET  Invoice_Number= '".$post['invoice_number']."'
									,Firm= '".$post['firm']."'
									,Office = '".$post['office']."' 
									,Account = '".$post['account']."' 
									,Currency = '".$post['currency']."' 
									,Off_Office = '".$post['off_office']."' 
									,Off_Account = '".$post['off_account']."' 
									,Description = '".$post['description']."' 
									,Net_Amount = '".$post['net_amount']."' 
									,Comment_Code = '".$post['comment_code']."' 
			WHERE id = '".$id."'";

	//Prepare Statement
	$stmt = $db->prepare($sql);

	//execute the query
	$stmt->execute(); 

	$query = "SELECT * FROM billing_info WHERE id = '".$id."'"; 
	$stmt = $db->query($query);

	$data = $stmt->fetch();
	echo json_encode($data); 

?>