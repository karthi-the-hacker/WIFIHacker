<?php

if (!empty($_SERVER['HTTP_CLIENT_IP'])) 
    {
      $ipaddress =  urlencode($_SERVER['HTTP_CLIENT_IP']);
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))  
    {
      $ipaddress =  urlencode($_SERVER['HTTP_X_FORWARDED_FOR']);
    }
else
    {
      $ipaddress =  urlencode($_SERVER['REMOTE_ADDR']);
    }

$browser = urlencode($_SERVER['HTTP_USER_AGENT']);




