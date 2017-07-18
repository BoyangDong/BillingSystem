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
	}else{
		echo 'Error Occured <br />';
	}

	$query = "SELECT * FROM billing_info ORDER BY id DESC LIMIT 1";
	$stmt = $db->query($query);

	if(count($stmt)>0){
		$data = $stmt->fetch();
		echo json_encode($data);
	}else{
		echo ' 
			{
				"id":-1,
				"Firm":"Z",
				"Office":"NAN",
				"Account":"-0.00",
				"Currency":"NA",
				"Off_Office":"NAN",
				"Off_Account":"NAN",
				"Description":"NAN",
				"Net_Amount":"0.00",
				"Comment_Code":"N"
			}'; 
	}
	$db = null;

?>

