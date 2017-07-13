<?php
//Step1
	$db = mysqli_connect('localhost','root','bdong','mydb')
	or die('Error connecting to MySQL server.');
?>
<html>
	<head>
	</head>
 	<body>
 	<h1>Budo Billing App</h1>
 	<?php
	//Step2
		#$query = "SELECT * FROM billing_info";
		$query = "SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM mydb.billing_info;";
		mysqli_query($db, $query) or die('Error querying database.');

		$response = mysqli_query($db, $query);		
		if($response){
			echo '<table align="left" cellspacing="5" cellpadding="8">
			<tr>
				<td align="left"><b>Firm</b></td>
				<td align="left"><b>Office</b></td>
				<td align="left"><b>Account</b></td>
				<td align="left"><b>Currency</b></td>
				<td align="left"><b>Off_Office</b></td>
				<td align="left"><b>Off_Account</b></td>
				<td align="left"><b>Description</b></td>
				<td align="left"><b>Net_Amount</b></td>
				<td align="left"><b>Comment_Code</b></td>
			</tr>';

			while($row = mysqli_fetch_array($response)){
				echo '<tr><td align="left">' . 
					$row['Firm'] . '</td><td align="left">' .
					$row['Office'] . '</td><td align="left">' .
					$row['Account'] . '</td><td align="left">' . 
					$row['Currency'] . '</td><td align="left">' .
					$row['Off_Office'] . '</td><td align="left">' .
					$row['Off_Account'] . '</td><td align="left">' .
					$row['Description'] . '</td><td align="left">' .
					$row['Net_Amount'] . '</td><td align="left">' .
					$row['Comment_Code'] . '</td><td align="left">' ;

				echo '</tr>';
			}
			echo '</table>';
		}else{
			echo "Couldn't issue database query";
			echo mysqli_error($db); 
		}
		mysqli_close($db);		
	?>
	</body>
</html>