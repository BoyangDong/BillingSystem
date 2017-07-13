<?php

require_once('../mysql_connect.php');

$query = "SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM mydb.billing_info;";

$response = @mysql_query($dbc, $query);

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

}


?>