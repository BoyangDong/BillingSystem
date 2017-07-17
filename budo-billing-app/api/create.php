<?php
require 'db_config.php';

	$post = $_POST; 

	$f = trim($post['firm']);
	$o = trim($post['office']);
	$a = trim($post['account']);

	$c = trim($post['currency']);
	$oo = trim($post['off_office']);
	$oa = trim($post['off_account']);
	
	$d = trim($post['description']);
	$na = trim($post['net_amount']);
	$cc = trim($post['comment_code']);
	
	$sql = "INSERT INTO billing_info(Firm, Office, Account, Currency, Off_Office, Off_Account, Description, `Net_Amount`, Comment_Code) 
			VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)";

	$stmt = $db->prepare($sql);
	$insert = $stmt->execute([$f, $o, $a, $c, $oo, $oa, $d, $na, $cc]);

	if(count($insert)){
		echo 'Billing Info Entered';
		$db = null;
	}else{
		echo 'Error Occured <br />';
	}

?>

