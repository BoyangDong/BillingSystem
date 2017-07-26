<?php
	
	require '../PHPMailer/PHPMailerAutoload.php';
	 
	$mailto = $_POST['mail_to'];
	$mailSub = $_POST['mail_sub'];
	$mailMsg = $_POST['mail_msg'];

	$mail = new PHPMailer();
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