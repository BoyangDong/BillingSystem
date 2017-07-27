<?php
require 'db_config.php';

if(isset($_POST["export"]))
{
	$query = "SELECT * FROM billing_info ORDER BY id DESC";
	header('Content-Type: text/csv; charset=utf8');
	header('Content-Disposition: attachment; filename=billing_today.csv');
	$output = fopen("php://output", "w");
	fputcsv($output, array('Firm', 'Office', 'Account', 'Currency', 'Off Office', 'Off Account', 'Description', 'Net Amount', 'Comment Code'));
	
	foreach ($db -> query("SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM billing_info") as $row) {
		fputcsv($output, $row);
	}
}
?>