<?php
require 'db_config.php';
require '../XLSXWriter/xlsxwriter.class.php';

$today = new DateTime();
$date = $today->format('Y_m_d');
$filename = $date . '_EDF_Budo_Rebills'; 

header('Content-disposition: attachment; filename="'.XLSXWriter::sanitize_filename($filename).'.xlsx"');
header("Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
header('Content-Transfer-Encoding: binary');
header('Cache-Control: must-revalidate');
header('Pragma: public');  
// I am using pdo for my db connection so I can't use mysql_query to query the databse, and the method has now been
// removed in php 7 so it's not even advisable to use it anymore.  -- 11/5/17 Bo
$query = $db->prepare("SELECT * FROM billing_info ORDER BY id DESC");
$query->execute();
$results = $query->fetchAll(); 
//$rows = mysql_fetch_assoc($result); 
$header = array(
	'Firm'=>'string',
	'Office'=>'string',
	'Account'=>'string',
	'Currency'=>'string',
	'Off Office'=>'string',
	'Off Account'=>'string',
	'Description'=>'string',
	'Net Amount'=>'price',
	'Comment Code'=>'string',
);

$columnheadersinDb = array('Firm', 'Office', 'Account', 'Currency', 'Off_Office', 'Off_Account', 'Description', 'Net_Amount', 'Comment_Code'); 

$writer = new XLSXWriter();
$writer->writeSheetHeader('Sheet1', $header);
foreach($results as $eachRow) {
	$array = array();
	foreach($columnheadersinDb as $column) {
		array_push($array, $eachRow[$column]);
	}
	$writer->writeSheetRow('Sheet1', $array);
}

//$writer->writeSheet($array,'Sheet1', $header);//or write the whole sheet in 1 call    
$writer->writeToStdOut();
//$writer->writeToFile('example.xlsx');
//echo $writer->writeToString();
exit(0);

// This is how the .csv file is made -- 11/5/17 Bo
/*$attachment_config = 'Content-Disposition: attachment; filename='. $filename .'.csv';

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
}*/

?>