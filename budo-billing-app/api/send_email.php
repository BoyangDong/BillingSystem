<?php
	
/*	print_r($_FILES);
	print_r($_POST);*/

	require 'db_config.php'; 
	$sql = $db->prepare("SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM billing_info");
	$sql->execute(); 

	/* Fetch all of the remaining rows in the result set */
	$results = $sql->fetchAll();
	$tableSpreadsheet = '';
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


    // we need to write a query to get all the values from the database and convert it to a table
    // can you copy some statements that you've written earlier for connecting to the db

	$mail = new PHPMailer();
	//print_r($_FILES);
	// an array of length 0 is not null.
	// using count helps us determine if it's empty or not instead of using isset
	if(count($_FILES) > 0){
		$file = "attachment/" . basename($_FILES['sheet_attached']['name']); 
		if(move_uploaded_file($_FILES['sheet_attached']['tmp_name'], $file)){
			$mail ->addAttachment($file);		
		}
	}

	// previous issue is that ajax is still trying to process the form and the ajax does not support file upload
	//need to make the ajax support file upload and we'll be good
/*	$mail ->isSMTP();
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
	$mail ->Body = $mailMsg;*/

	$mail ->isSMTP();
	$mail ->SMTPDebug = 0;
	$mail ->SMTPAuth = true;
	$mail ->SMTPSecure = 'TLS';
	$mail ->Host = "west.exch028.serverdata.net";
	$mail ->Port = 587; 
	$mail ->IsHTML(true);
	$mail ->Username = "rebill@budoholdings.com";
	$mail ->Password = "123Password!";
	$mail ->setFrom("rebill@budoholdings.com", "Budo Rebill Email");
	$mail ->Subject = $mailSub;
	$mail ->Body = $mailMsg;

	foreach ($mailto as $r) {
		$mail ->addAddress($r);
	}
	if(!$mail->send()){
		echo $mail->ErrorInfo;
		$message = "issue happened while sending email!";
		$send_status = 0;
	}else{
		$message = "Email SENT!";
		$send_status = 1;		
	}

	echo json_encode(array('message'=>$message, 'send_status'=>$send_status));


?>