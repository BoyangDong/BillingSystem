<?php
require 'db_config.php';

	$post = $_POST; 

	//$da = trim($post['date_input']);
	$da = trim($post['billing_date']);

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
	$com = trim($post['comments']);
	
	$sql = "INSERT INTO billing_info(Date, Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, `Net_Amount`, Comment_Code, Comments) 
			VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

	$stmt = $db->prepare($sql);
	$insert = $stmt->execute([$da, $in, $f, $o, $a, $c, $oo, $oa, $d, $na, $cc, $com]);

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

