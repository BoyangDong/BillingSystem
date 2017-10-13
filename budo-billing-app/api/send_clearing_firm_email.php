<?php

	require 'db_config.php'; 

	require '../PHPMailer/PHPMailerAutoload.php';


	$mail_edf = new PHPMailer();

	$mailto_edf = $_POST['clearing_firm_recipients'];
	$mailSub_edf = $_POST['clearing_firm_mail_sub'];
	$mailMsg_edf = $_POST['clearing_firm_mail_msg'];	

	$file_edf = "attachment/" . basename($_FILES['sheet_attached']['name']); 

	if(move_uploaded_file($_FILES['sheet_attached']['tmp_name'], $file_edf)){
		$mail_edf ->addAttachment($file_edf);		
	}
	// previous issue is that ajax is still trying to process the form and the ajax does not support file upload
	//need to make the ajax support file upload and we'll be good
	$mail_edf ->isSMTP();
	$mail_edf ->SMTPDebug = 0;
	$mail_edf ->SMTPAuth = true;
	$mail_edf ->SMTPSecure = 'TLS';
	$mail_edf ->Host = "west.exch028.serverdata.net";
	$mail_edf ->Port = 587; 
	$mail_edf ->IsHTML(true);
	$mail_edf ->Username = "boyang.dong@budoholdings.com";
	$mail_edf ->Password = "dby19930203dby..";
	$mail_edf ->setFrom("boyang.dong@budoholdings.com", "Boyang Work Email");
	$mail_edf ->Subject = $mailSub_edf;
	$mail_edf ->Body = $mailMsg_edf;

	foreach ($mailto_edf as $r) {
		$mail_edf ->addAddress($r);
	}
	if(!$mail_edf->send()){
		$message = "issue happened while sending email!";
		$send_status = 0;

	}else{
		$message = "Email to clearing Firm, SENT!";		
		$send_status = 1; 
	}

	/*Once the email to clearing firm is sent, push everything to the pool, and truncate the daily rebill database
	  Only when there is a recipient from clearding form this will happen (which means the approver approves).
	*/
	if(count($mailto_edf) > 0){
		$sql_fetch_all = $db->prepare("SELECT Date, Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code, Comments FROM billing_info");
		$sql_fetch_all->execute(); 

		$all_record = $sql_fetch_all->fetchAll();

		foreach($all_record as $value) {
			$sql_push = "INSERT INTO billing_pool(Date, Invoice_Number, Firm, Office, Account, Currency, Off_Office, Off_Account, Description, `Net_Amount`, Comment_Code, Comments) 
					VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

			$date = $value['Date'];
			$in = $value['Invoice_Number'];
			$f = $value['Firm'];
			$o = $value['Office'];
			$a = $value['Account'];

			$c = $value['Currency'];
			$oo = $value['Off_Account'];
			$oa = $value['Off_Account'];
			
			$d = $value['Description'];
			$na = $value['Net_Amount'];
			$cc = $value['Comment_Code'];
			$com = $value['Comments'];

			$stmt = $db->prepare($sql_push);
			$insert = $stmt->execute([$date, $in, $f, $o, $a, $c, $oo, $oa, $d, $na, $cc, $com]);
		}
		try{
			$truncate_table = $db->prepare("TRUNCATE TABLE `billing_info`");
			$truncate_table -> execute();
		}catch(PDOException $e){
			echo $e->getMessage(); 
		}
	}
	echo json_encode(array('message'=>$message, 'send_status'=>$send_status));


?>