<?php
	
/*	print_r($_FILES);
	print_r($_POST);*/

	require '../PHPMailer/PHPMailerAutoload.php';
	 
	$mailto = $_POST['recipients'];
	$mailSub = $_POST['mail_sub'];
	$mailMsg = $_POST['mail_msg'];

	$mail = new PHPMailer();

	$file = "attachment/" . basename($_FILES['sheet_attached']['name']); 
	echo "<pre>";
	print_r($_FILES);

	if(move_uploaded_file($_FILES['sheet_attached']['tmp_name'], $file)){
		$mail ->addAttachment($file);		
	}
	// previous issue is that ajax is still trying to process the form and the ajax does not support file upload
	//need to make the ajax support file upload and we'll be good yes open it
	$mail ->isSMTP();
	$mail ->SMTPDebug = 0;
	$mail ->SMTPAuth = true;
	$mail ->SMTPSecure = 'ssl';
	$mail ->Host = "smtp.gmail.com";
	$mail ->Port = 465; // or 587
	$mail ->IsHTML(true);
	$mail ->Username = "test.budo@gmail.com";
	$mail ->Password = "test.budo1234";
	$mail ->setFrom("test.budo@gmail.com", "Budo Gmail");
	$mail ->Subject = $mailSub;
	$mail ->Body = $mailMsg;

	foreach ($mailto as $r) {
		$mail ->addAddress($r);
	}
	if(!$mail->send()){
		$message = "issue happened while sending email!";
	}else{
		$message = "email has been sent!";		
	}
	echo json_encode(array('message'=>$message));
?>