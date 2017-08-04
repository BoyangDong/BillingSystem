<?php
	
/*	print_r($_FILES);
	print_r($_POST);*/

	require 'db_config.php'; 
	$sql = $db->prepare("SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM billing_info");
	$sql->execute(); 

	/* Fetch all of the remaining rows in the result set */
	$results = $sql->fetchAll();
	$tableSpreadsheet = $tableSpreadsheet . '<br/><br/><br/><table border="1" width="100%">';
	$tableSpreadsheet .= '<thead>
		<tr>
			<th>Firm</th>
			<th>Office</th>
			<th>Account</th>
			<th>Currency</th>
			<th>Off Office</th>
			<th>Off Account</th>
			<th>Description</th>
			<th>Net Amount</th>
			<th>Comment Code</th>
		</tr>
	</thead>';
	foreach($results as $value) {
		$tableSpreadsheet .= '
			<tr>
				<td align="center">'.$value['Firm'].'</td>
				<td align="center">'.$value['Office'].'</td>
				<td align="center">'.$value['Account'].'</td>
				<td align="center">'.$value['Currency'].'</td>
				<td align="center">'.$value['Off_Office'].'</td>
				<td align="center">'.$value['Off_Account'].'</td>
				<td align="center">'.$value['Description'].'</td>
				<td align="center">'.$value['Net_Amount'].'</td>
				<td align="center">'.$value['Comment_Code'].'</td>
			</tr>';
	}

	$tableSpreadsheet .= '</table>';

	require '../PHPMailer/PHPMailerAutoload.php';
	 
	$mailto = $_POST['recipients'];
	$mailSub = $_POST['mail_sub'];
	$mailMsg = $_POST['mail_msg'] . $tableSpreadsheet; //concatenate two strings together the key operator for concatenating two or more strings is "."

	$mailto_edf = $_POST['clearing_firm_recipients'];
	$mailSub_edf = $_POST['clearing_firm_mail_sub'];
	$mailMsg_edf = $_POST['clearing_firm_mail_msg'];	


    // we need to write a query to get all the values from the database and convert it to a table
    // can you copy some statements that you've written earlier for connecting to the db

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


	$mail_edf = new PHPMailer();

	$file_edf = "attachment/" . basename($_FILES['sheet_attached']['name']); 
	echo "<pre>";
	print_r($_FILES);

	if(move_uploaded_file($_FILES['sheet_attached']['tmp_name'], $file_edf)){
		$mail_edf ->addAttachment($file_edf);		
	}
	// previous issue is that ajax is still trying to process the form and the ajax does not support file upload
	//need to make the ajax support file upload and we'll be good yes open it
	$mail_edf ->isSMTP();
	$mail_edf ->SMTPDebug = 0;
	$mail_edf ->SMTPAuth = true;
	$mail_edf ->SMTPSecure = 'ssl';
	$mail_edf ->Host = "smtp.gmail.com";
	$mail_edf ->Port = 465; // or 587
	$mail_edf ->IsHTML(true);
	$mail_edf ->Username = "test.budo@gmail.com";
	$mail_edf ->Password = "test.budo1234";
	$mail_edf ->setFrom("test.budo@gmail.com", "Budo Gmail");
	$mail_edf ->Subject = $mailSub_edf;
	$mail_edf ->Body = $mailMsg_edf;

	foreach ($mailto_edf as $r) {
		$mail_edf ->addAddress($r);
	}
	if(!$mail_edf->send()){
		$message = "issue happened while sending email!";
	}else{
		$message = "email has been sent!";		
	}
	echo json_encode(array('message'=>$message));
?>