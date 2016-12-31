#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

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

port = form.getvalue("port")
if (not port):
  port = 2001
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
if (not (press == "PRESS_SHORT" or press == "LONG_PRESS")):
  press = "PRESS_SHORT";    

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

