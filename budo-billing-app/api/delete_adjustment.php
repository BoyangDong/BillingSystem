<?php
	require 'db_config.php'; 

	$id = $_POST["id"]; 

	$sql = "DELETE FROM adjustment_history WHERE id = '".$id."'"; 

	$result = $db->exec($sql);

	echo json_encode([$id]); 
?>