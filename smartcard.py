#!/usr/bin/python

from opensc import *

def smartcard_is_present():
	return True

def smartcard_not_present():
	reader = getReaderName()
	return open('smartcard_not_present.html').read() % (reader)

def smartcard_is_locked():
	return False

def enter_pin():
	return open('smartcard_enter_pin.html').read() % (getReaderName(), getSmartcardName())

def smartcard_menu():
	reader = getReaderName()
	return open('smartcard_menu.html').read() # % (getReaderName(), getSmartcardName())
