#!/usr/bin/python

#
# smartcard functions
#

def getReaderName():
	return 'Fujitsu Siemens Computers SmartCard USB 2A 00 00'

def getSmartcardName():
	return 'HU-CA Smartcard for Matthias Bock'


import bobo

def is_present():
	return True

def not_present():
	reader = getReaderName()
	return open('smartcard/not_present.html').read() #% (reader)

def is_locked():
	return False

def enter_pin():
	return open('smartcard/enter_pin.html').read() #% (getReaderName(), getSmartcardName())

@bobo.query('/smartcard')
def smartcard():
	if is_present():
		if is_locked():
			return enter_pin()
		else:
			return open('smartcard/details.html').read()
	else:
		return not_present()
