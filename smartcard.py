#!/usr/bin/python

#
# smartcard functions
#

import bobo
from opensc import *

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
