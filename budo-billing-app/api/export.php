<?php
require 'db_config.php';

$today = new DateTime();
$date = $today->format('Y_m_d');
$filename = $date . '_EDF_Budo_Rebills'; 

$attachment_config = 'Content-Disposition: attachment; filename='. $filename .'.csv';

if(isset($_POST["export"]))
{
	$query = "SELECT * FROM billing_info ORDER BY id DESC";
	header('Content-Type: text/csv; charset=utf8');
	header($attachment_config);
	$output = fopen("php://output", "w");
	fputcsv($output, array('Firm', 'Office', 'Account', 'Currency', 'Off Office', 'Off Account', 'Description', 'Net Amount', 'Comment Code'));
	
	//foreach ($db -> query("SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, Net_Amount, Comment_Code FROM billing_info") as $row) {
	foreach ($db -> query("SELECT Firm, Office, Account, Currency, Off_Office, Off_Account, Description, cast(Net_Amount AS CHAR), Comment_Code FROM billing_info") as $row) {
		fputcsv($output, $row);
	}
}




?>