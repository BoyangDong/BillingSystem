<?php
require 'db_config.php';

	$post = $_POST; 

	$in = trim($post['invoice_number']);
	$f = trim($post['firm']);
	$o = trim($post['office']);
	$a = trim($post['account']);

	$c = trim($post['currency']);
	$oo = trim($post['off_office']);
	$oa = trim($post['off_account']);
	
	$d = trim($post['description']);
	$na = trim($post['net_amount']);
	$cc = trim($post['comment_code']);
	
	$sql = "INSERT INTO billing_info(Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, `Net_Amount`, Comment_Code) 
			VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

	$stmt = $db->prepare($sql);
	$insert = $stmt->execute([$in, $f, $o, $a, $c, $oo, $oa, $d, $na, $cc]);

	if(count($insert)){
		$message = 'Billing Info Entered';
	}else{
		$message = 'Error Occured While Inserting Data into DB...<br />';
	}

	$query = "SELECT * FROM billing_info ORDER BY id DESC LIMIT 1";
	$stmt = $db->query($query);

	if(count($stmt)>0){
		$data = $stmt->fetch();
		echo json_encode(array('info'=>$data, 'message'=>$message));
	}else{
		echo 'Not Able to Fetch the Latest Data from the table...'; 
	}
	$db = null;

?>

