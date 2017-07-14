<?php
	require_once 'config.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>Add Billing Info</title>
</head>
<body>
<?php

if(isset($_POST['submit'])){
	$data_missing = array(); 
	//firm
	if(empty($_POST['firm'])){
		$data_missing[] = 'D';
	}else{
		$f = trim($_POST['firm']);
	}	
	//office
	if(empty($_POST['office'])){
		$data_missing[] = 'UDN';
	}else{
		$o = trim($_POST['office']);
	}
	//account
	if(empty($_POST['account'])){
		$data_missing[] = 'Account';
	}else{
		$a = trim($_POST['account']);
	}	
	//currency
	if(empty($_POST['currency'])){
		$data_missing[] = 'Currency';
	}else{
		$c = trim($_POST['currency']);
	}	
	//off office
	if(empty($_POST['off_office'])){
		$data_missing[] = 'Off_Office';
	}else{
		$oo = trim($_POST['off_office']);
	}	
	//off account
	if(empty($_POST['off_account'])){
		$data_missing[] = 'Off_Account';
	}else{
		$oa = trim($_POST['off_account']);
	}	
	//description
	if(empty($_POST['description'])){
		$data_missing[] = 'Description';
	}else{
		$d = trim($_POST['description']);
	}	
	//net amount
	if(empty($_POST['net_amount'])){
		$data_missing[] = 'Net_Amount';
	}else{
		$na = trim($_POST['net_amount']);
	}	
	//comment code
	if(empty($_POST['comment_code'])){
		$data_missing[] = 'Comment_Code';
	}else{
		$cc = trim($_POST['comment_code']);
	}	
	if(empty($data_missing)){
		#die(var_dump(ini_get('include_path')));


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
	}else{
		echo 'Enter the missing data below <br />';
		foreach($data_missing as $missing){
			echo "missinig <br />" . $missing;
		}
	}
}
?>
	<form action="http://localhost:8080/budo-billing-app/billing_info_added.php" method="post">
	<table border="0">
		<tr>
			<td>Firm</td>
			<td align="center"><input type="text" name="firm" size="30" value="D" maxlength="1"/></td>
		</tr>
		<tr>
			<td>Office</td>
			<td align="center"><input type="text" name="office" size="30" value="UDN" maxlength="3"/></td>
		</tr>
		<tr>
			<td>Account</td>
			<td align="center"><input type="text" name="account" size="30"/></td>
		</tr>
		<tr>
			<td>Currency</td>
			<td align="center"><input type="text" name="currency" size="30" value="U1" maxlength="2"/></td>
		</tr>
		<tr>
			<td>Off Office</td>
			<td align="center"><input type="text" name="off_office" size="30" value="UDN" maxlength="3"/></td>
		</tr>
		<tr>
			<td>Off Account</td>
			<td align="center"><input type="text" name="off_account" size="30"/></td>
		</tr>
		<tr>
			<td>Description</td>
			<td align="center"><input type="text" name="description" size="30"/></td>
		</tr>
		<tr>
			<td>Net Amount</td>
			<td align="center"><input type="number" name="net_amount" size="30" max="0" value="-0.00" step=".01"/></td>
		</tr>
		<tr>
			<td>Comment Code</td>
			<td align="center"><input type="text" name="comment_code" size="30" value="R" maxlength="1"/></td>
		</tr>

		<tr> 
		<td colspan="2" align="center"><button id="render" name="submit"/>Send</button></td>
		</tr>
	</table>
	</form>
	<script> 

	</script>

</body>
</html>>