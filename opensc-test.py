#! /usr/bin/env python

from smartcard.System import readers

# define the APDUs used in this script
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x0A, 0xA0, 0x00, 0x00, 0x00, 0x62,
    0x03, 0x01, 0x0C, 0x06, 0x01]
COMMAND = [0x00, 0x00, 0x00, 0x00]

# get all the available readers
r = readers()
print "Available readers:", r

reader = r[0]
print "Using:", reader

connection = reader.createConnection()
connection.connect()

data, sw1, sw2 = connection.transmit(SELECT)
print data
print "Select Applet: %02X %02X" % (sw1, sw2)

data, sw1, sw2 = connection.transmit(COMMAND)
print data
print "Command: %02X %02X" % (sw1, sw2)
