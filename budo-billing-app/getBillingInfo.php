<!DOCTYPE html>
<html>
<head>
	<title>Information Gathered</title>
</head>
<body>
	<?php
		$firm = $_POST['firm'];
		$office = $_POST['office'];
		$account = $_POST['account'];

		$currency = $_POST['currency'];
		$off_office = $_POST['off_office'];
		$off_account = $_POST['off_account'];

		$description = $_POST['description'];
		$net_amount = $_POST['net_amount'];
		$comment_code = $_POST['comment_code'];

		echo "$firm" . "</br>";
		echo "$office" . "</br>";
		echo "$account" . "</br>";

	?>
</body>
</html>