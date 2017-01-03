<?php

header("Content-type: text/plain");

$homematic = $_REQUEST["homematic"];
if (!$homematic) die("ERR: No HomeMatic address");
if (!preg_match('/^\w+[\w\.\-]*\w+$/', $homematic)) die("ERR: Invalid HomeMatic address");

$port = $_REQUEST["port"];
if (!$port) $port = 2001;
if (!preg_match('/^\d+$/', $port)) $port = 2001;
if (($port < 1) or ($port > 65534)) $port = 2001;

$channel = $_REQUEST["channel"];
if (!$channel) die("ERR: No channel");
if (!preg_match('/^\d+$/', $channel)) die("ERR: Invalid channel (1)");
if (($channel < 1) or ($channel > 50)) die("ERR: Invalid channel (2)");

$press = $_REQUEST["press"];
if (!$press) $press = "PRESS_SHORT";
if (!(($press == "PRESS_SHORT") or ($press == "PRESS_LONG"))) $press = "PRESS_SHORT";

// ifttt {{EnteredOrExited}} handling
$eoe = $_REQUEST["enterlong"];
if ($eoe == "entered") $press = "PRESS_LONG";
if ($eoe == "exited") $press = "PRESS_SHORT";

$eoe = $_REQUEST["entershort"];
if ($eoe == "entered") $press = "PRESS_SHORT";
if ($eoe == "exited") $press = "PRESS_LONG";


$protocol = $_REQUEST["protocol"];
if (!$protocol) $protocol = "http";
if (!(($protocol == "http") or ($protocol == "https"))) $protocol = "http";

$debug = $_REQUEST["debug"];
if ($debug) {
  print "protocol: $protocol\n";
  print "homematic: $homematic\n";
  print "port: $port\n";
  print "channel: $channel\n";
  print "press: $press\n";
}

$url = $protocol . "://" . $homematic . ":" . $port;

require_once "phpxmlrpc-src/Autoloader.php";
PhpXmlRpc\Autoloader::register();

use PhpXmlRpc\Value;
use PhpXmlRpc\Request;
use PhpXmlRpc\Client;

$client = new Client($url);
$response = $client->send(new Request('setValue', array(new Value("BidCoS-RF:".$channel), new Value($press), new Value(True, 'boolean'))));

print "done.\n"

?>