#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging


# if set: will only allow homematic parameters from these
myHomematics = [
#     "my.dyndns.adress",
#     "111.222.33.44", # my fixed IP address
];
    
    
# no user-serviceable parts below
    
    

import xmlrpclib
import cgi
import re
import sys

form = cgi.FieldStorage()

print "Content-type: text/plain\n\n"

homematic = form.getvalue("homematic")
if (not homematic):
  print "ERR: No HomeMatic address"
  sys.exit()
if (not re.match('^\w+[\w\.\-]*\w+$', homematic)):
  print "ERR: Invalid HomeMatic address"
  sys.exit()
if isinstance(myHomematics, list):
  if myHomematics:
    if homematic not in myHomematics:
      print "ERR: Unknown HomeMatic address"
      sys.exit()

port = form.getvalue("port")
if (not port):
  port = str(2001)
if (not re.match('^\d+$', port)):
  port = 2001
port = int(port)
if (port < 1 or port > 65534):
  port = 2001
  
channel = form.getvalue("channel")
if (not channel):
  print "ERR: No channel"
  sys.exit()
if (not re.match('^\d+$', channel)):
  print "ERR: Invalid channel (1)"
  sys.exit()
channel = int(channel)
if (channel < 1 or channel > 50):
  print "ERR: Invalid channel (2)"
  sys.exit()

press = form.getvalue("press")
if (not press):
  press = "PRESS_SHORT";
if (not (press == "PRESS_SHORT" or press == "PRESS_LONG")):
  press = "PRESS_SHORT";    

# ifttt {{EnteredOrExited}} handling
eoe = form.getvalue("enterlong")
if (eoe == "entered"):
  press = "PRESS_LONG"
if (eoe == "exited"):
  press = "PRESS_SHORT"

eoe = form.getvalue("entershort")
if (eoe == "entered"):
  press = "PRESS_SHORT"
if (eoe == "exited"):
  press = "PRESS_LONG"


protocol = form.getvalue("protocol")
if (not protocol):
  protocol = "http";
if (not (protocol == "http" or protocol == "https")):
  protocol = "http";

debug = form.getvalue("debug")
if (debug):
  print "protocol: %s\n" % protocol
  print "homematic: %s\n" % homematic
  print "port: %s\n" % port
  print "channel: %s\n" % channel
  print "press: %s\n" % press

url = protocol + "://" + homematic + ":" + str(port)

s = xmlrpclib.ServerProxy(url)
s.setValue('BidCoS-RF:'+str(channel), press, True);

print "OK.\n"

