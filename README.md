# get2xmlrpc4homematic
API Web Hook forwarding GET requests as XMLRPC calls for a HomeMatic system


Provides scripts to be used on your webserver.

The scripts will accept GET requests parameters, and issue an XMLRPC call
  to your HomeMatic CCU(2) for remote control functionality.

This works well with the IFTTT Makers Channel.


For now, it will only trigger the 50 virtual controls in the HomeMatic CCU(2).

You can use scripts in the HomeMatic to translate this into settings on your hardware.
This keeps this scripts as simple as possible.


Prerequisites:
===============

You need a web server where you can run Python or PHP scripts.

Port 2001 of your CCU has to be exposed to the internet.
  Look into your router manual to see how this is done.
  You can use another external port with Port Forwarding.

  If you have a dynamic internet IP address, using a DynDNS service is recommended.
  Many routers also offer to manage this for you.

Using the Firewall functionality of your CCU is HIGHLY recommended, 
  as otherwise everyone who sees that open port can issue commands to it!
  Set it up to only accept requests from you web server.


Setting up:
============

Copy the scripts to your webserver.

The Python script api.py is currently running as CGI.
Changes may be required to run it with mod_python or FastCGI.


Usage:
=======

You can set the following parameters on a GET request:

homematic
	HomeMatic CCU2 address
	required
	accepted values: DNS name or IP address

channel
	Channel to trigger
	required
	accepted values: numbers 1 to 50

procotol
	Protocol to use
	optional
	accepted values: http or https
	defaults to http if unset or unaccepted value

port
	Port to connect to
	optional
	accepted values: numbers 1 to 65534
	defaults to 2001 if unset or unaccepted value

press
	Keypress to trigger
	optional
	accepted values: PRESS_LONG & PRESS_SHORT
	defaults to PRESS_SHORT if unset or unaccepted value

debug
	Output parameters to user
	optional
	accepted values: any computational "true" value 

example usage:

http://my.web.server/some/path/api.php?homematic=my.dyndns.adress&channel=21

  will create an XMLRPC call to http://my.dyndns.address:2001
  triggering BidCoS-RF:21 with PRESS_SHORT
