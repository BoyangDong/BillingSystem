<?php
	require 'db_config.php'; 
	try{
		$sql = "TRUNCATE billing_info";	
		$db->exec($sql);
		echo "1";
	}catch(PDOException $e){
		echo $e->getMessage(); 
	} 
?>