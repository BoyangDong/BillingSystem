<?php
//Step1

$host = '127.0.0.1';
$db   = 'mydb';
$user = 'root';
$pass = 'bdong';
$charset = 'utf8';

try 
{
	$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
	$opt = [
	    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
	    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
	    PDO::ATTR_EMULATE_PREPARES   => false,
	];
	$db = new PDO($dsn, $user, $pass, $opt);
}
catch(Exception $e)
{
	die($e->getMessage());
}

