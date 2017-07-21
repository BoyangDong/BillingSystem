<?php
	require 'db_config.php'; 

	$id = $_POST["id"]; 

	$sql = "DELETE FROM billing_info WHERE id = '".$id."'"; 

	$result = $db->exec($sql);

	echo json_encode([$id]); 
?>